"""Create a chat, then watch it stream over the Connect-RPC bridge.

Server-streaming RPCs aren't part of the generated REST SDK, so they live in
`textql_sdk.streaming`. Prefer `watch_chat` for anything long-lived — it carries
run lifecycle events (`run_started`, `run_complete`, `run_error`) plus every
cell as it's produced. See STREAMING.md for the other streaming methods.

Reading cell state
------------------
Every `cell` event carries a **full snapshot** of that cell, not a delta, so key
by `cell.id` and re-render from the snapshot. Three fields tell you where it is:

* `complete` — terminal. Branch on this, not on `lifecycle`. It's polymorphic
  server-side: a markdown cell is complete as soon as it's created, while a SQL
  cell is only complete once executed. Comparing `lifecycle` to
  `LIFECYCLE_EXECUTED` yourself marks non-executable cells as never finishing.
* `lifecycle` — the raw state. `LIFECYCLE_EXECUTING` is the one worth surfacing,
  so a long query reads as in-flight rather than as a finished empty cell.
* `exec_error` — per-cell failure. A run can reach `run_complete` with
  individual cells that errored, so this is *not* covered by `run_error`.

Printing a cell
---------------
A `Cell` is a oneof over ~50 payload types. This prints them as the flat event
log the v2 SSE stream (`POST /v2/chats/stream`) produces: an execution step
appears once when it starts running, carrying the query or code the model
generated, and once when it finishes, carrying the result.

    cell  sql 4f2a91c8-…  running
          SELECT customer, sum(amount) AS revenue FROM orders GROUP BY 1
    cell  sql 4f2a91c8-…  done  842ms
          12 rows × 2 cols
          | customer | revenue |
    text  Acme led at $12,000.
    done  completed

`watch_chat` re-sends a full snapshot on every update, so `CellPrinter` (in
`textql_sdk.cell_render`, not here) collapses those to those two events. See
that module to change what a cell type looks like.

Custom TLS
----------
Set ``TEXTQL_CA_BUNDLE`` to a PEM path to trust a private CA (corporate proxy,
on-prem gateway). The SDK and the streaming bridge use *different* HTTP stacks —
``httpx`` for unary REST calls, ``pyqwest`` for Connect streaming — so the bundle
has to be handed to both. See ``build_tls`` below.

Activate your venv, then:

    python examples/watch_chat.py
    python examples/watch_chat.py "plot sinx"

With uv, prefix the same command with `uv run`:

    uv run python examples/watch_chat.py "plot sinx"

See examples/README.md for setup under either package manager.
"""

# pylint: disable=no-member,no-name-in-module
# chat_pb2 builds its members at import time, so pylint can't see
# WatchChatRequest. Suppressed in-file because pylintrc is Speakeasy-managed and
# overwritten on every `speakeasy run` (see scripts/postprocess-connect.py).
# pyright, which gates CI, resolves it fine.

import asyncio
import os
import pathlib
import sys
from typing import Optional, Union

import httpx
import pyqwest
from connectrpc.errors import ConnectError as ConnectRpcError
from dotenv import load_dotenv

from textql_sdk import Textql
from textql_sdk._connect.public.chat_pb2 import WatchChatRequest
from textql_sdk.cell_render import CellPrinter
from textql_sdk.models import (
    ConnectError,
    TextqlRPCPublicParadigmParadigm,
    TextqlRPCPublicParadigmUniversalOptions,
    Universal,
)
from textql_sdk.streaming import create_streaming_client

# Matches fe/src/lib/clients/WatchChatClient.ts, which is the reference consumer
# of this stream.
MAX_RECONNECT_ATTEMPTS = 7
BASE_RECONNECT_DELAY_S = 0.5


def build_tls() -> tuple[Union[bool, str], Optional[pyqwest.Client]]:
    """Resolve TEXTQL_CA_BUNDLE into config for both HTTP stacks.

    Returns ``(httpx_verify, connect_http_client)``. With no bundle set, both
    fall back to their defaults, which already trust the system store.
    """
    bundle = os.environ.get("TEXTQL_CA_BUNDLE")
    if not bundle:
        return True, None

    ca_pem = pathlib.Path(bundle).read_bytes()
    # tls_include_system_certs is not optional here: a transport you construct
    # yourself starts with an empty trust store, so omitting it fails *every*
    # TLS handshake, not just ones needing the private CA.
    transport = pyqwest.HTTPTransport(
        tls_ca_cert=ca_pem,
        tls_include_system_certs=True,
    )
    return bundle, pyqwest.Client(transport)


async def main() -> None:
    load_dotenv()
    message = (
        sys.argv[1] if len(sys.argv) > 1 else "Tell me about this month's usage?"
    )

    # Configure the SDK once; streaming inherits its server + API key. TLS is
    # the exception — the two stacks are separate, so pass it to each.
    # Set TEXTQL_SERVER_URL for on-prem/dev; it defaults to the cloud server.
    verify, connect_client = build_tls()
    sdk = Textql(
        api_key=os.environ["TEXTQL_API_KEY"],
        server_url=os.environ.get("TEXTQL_SERVER_URL"),
        async_client=httpx.AsyncClient(
            follow_redirects=True,
            timeout=httpx.Timeout(None, connect=10.0),
            verify=verify,
        ),
    )
    streaming = create_streaming_client(sdk, http_client=connect_client)

    paradigm = TextqlRPCPublicParadigmParadigm(
        type="TYPE_UNIVERSAL",
        version=1,
        options=Universal(
            universal=TextqlRPCPublicParadigmUniversalOptions(
                sql_enabled=True,
                python_enabled=True,
                connector_ids=[1],  # replace with your connector ID(s)
            )
        ),
    )

    # 1) Create the chat (message is the first user turn).
    created = await sdk.chats.create_chat_async(
        message=message,
        model="MODEL_SONNET_4_6",
        paradigm=paradigm,
    )
    if isinstance(created, ConnectError):
        raise RuntimeError(f"create_chat failed: {created}")
    assert created.chat is not None
    chat_id = created.chat.id
    assert isinstance(chat_id, str), "create_chat returned a chat with no ID"

    out = CellPrinter()
    out.note("chat", chat_id)

    opened = asyncio.Event()

    # Resume state. `cursor` advances on every event; `last_complete_cell_id`
    # only on cells that reported complete. Both are replayed on reconnect so
    # the server resumes instead of re-sending the whole chat.
    cursor = ""
    last_complete_cell_id = ""

    def build_request() -> WatchChatRequest:
        request = WatchChatRequest(chat_id=chat_id)
        if last_complete_cell_id:
            request.latest_complete_cell_id = last_complete_cell_id
        if cursor:
            request.resume_cursor = cursor
        return request

    async def watch() -> None:
        nonlocal cursor, last_complete_cell_id
        attempt = 0

        while True:
            try:
                async for event in streaming.chats.watch_chat(build_request()):
                    attempt = 0  # a delivered event means the stream is healthy
                    if event.cursor:
                        cursor = event.cursor

                    kind = event.WhichOneof("payload")
                    if kind == "opened":
                        out.note("watch", "opened")
                        opened.set()
                    elif kind == "cell":
                        if event.cell.complete:
                            last_complete_cell_id = event.cell.id
                        out.cell(event.cell)
                    elif kind == "run_started":
                        out.note("run", "started")
                    elif kind == "run_complete":
                        out.flush()
                        failed, pending = out.failed(), out.unfinished()
                        # `run_complete` fires even when individual cells
                        # failed; only `run_error` fails the run itself.
                        out.note("done", "completed")
                        if failed:
                            out.note("", f"{len(failed)} cell(s) failed: "
                                     + ", ".join(failed))
                        if pending:
                            out.note("", f"{len(pending)} cell(s) never reached "
                                     "a terminal state")
                        return
                    elif kind == "run_error":
                        # Terminal: the run itself failed, so don't reconnect.
                        out.flush()
                        out.note("done", f"failed: {event.run_error}")
                        raise RuntimeError(f"run error: {event.run_error}")
                    elif kind == "handoff_pending":
                        out.note(
                            "handoff", event.handoff_pending.handoff_marker
                        )
                    elif kind == "heartbeat":
                        pass  # keepalive
            except ConnectRpcError as e:
                # Transport-level failure. Idle streams get closed by proxies on
                # long runs, so retry from the cursor rather than giving up.
                attempt += 1
                if attempt > MAX_RECONNECT_ATTEMPTS:
                    raise RuntimeError(
                        f"watch_chat failed after {MAX_RECONNECT_ATTEMPTS} "
                        f"reconnect attempts: {e.code}"
                    ) from e
                delay = BASE_RECONNECT_DELAY_S * 2 ** (attempt - 1)
                out.note("retry", f"stream dropped ({e.code}); "
                         f"reconnecting in {delay:.1f}s")
                await asyncio.sleep(delay)
                continue

            # Generator ended without run_complete — same treatment.
            attempt += 1
            if attempt > MAX_RECONNECT_ATTEMPTS:
                raise RuntimeError("watch_chat ended without run_complete")
            await asyncio.sleep(BASE_RECONNECT_DELAY_S * 2 ** (attempt - 1))

    watch_task = asyncio.create_task(watch())
    await opened.wait()

    # 3) Start the run; watch_task receives cells + lifecycle until run_complete.
    run = await sdk.chats.run_async(chat_id=chat_id, model="MODEL_SONNET_4_6")
    if isinstance(run, ConnectError):
        watch_task.cancel()
        raise RuntimeError(f"run failed: {run}")

    await watch_task


if __name__ == "__main__":
    asyncio.run(main())
