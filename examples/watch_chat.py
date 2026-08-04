"""Create a chat, then watch it stream over the Connect-RPC bridge.

Server-streaming RPCs aren't part of the generated REST SDK, so they live in
`textql_sdk.streaming`. Prefer `watch_chat` for anything long-lived — it carries
run lifecycle events (`run_started`, `run_complete`, `run_error`) plus every
cell as it's produced. See STREAMING.md for the other streaming methods.

Reading cell state
------------------
Every `cell` event carries a **full snapshot** of that cell, not a delta, so key
by `cell.id` and replace what you're holding. Three fields tell you where it is:

* `complete` — terminal. Branch on this, not on `lifecycle`. It's polymorphic
  server-side: a markdown cell is complete as soon as it's created, while a SQL
  cell is only complete once executed. Comparing `lifecycle` to
  `LIFECYCLE_EXECUTED` yourself marks non-executable cells as never finishing.
* `lifecycle` — the raw state. `LIFECYCLE_EXECUTING` is the one worth surfacing,
  so a long query reads as in-flight rather than as a finished empty cell.
* `exec_error` — per-cell failure. A run can reach `run_complete` with
  individual cells that errored, so this is *not* covered by `run_error`.

Activate your venv, then:

    python examples/watch_chat.py
    python examples/watch_chat.py "plot sinx"

With uv, prefix the same command with `uv run`:

    uv run python examples/watch_chat.py "plot sinx"

See examples/README.md for setup under either package manager.
"""

import asyncio
import os
import sys
from dataclasses import dataclass

import httpx
from connectrpc.errors import ConnectError as ConnectRpcError
from dotenv import load_dotenv

from textql_sdk import Textql
from textql_sdk._connect.public import chat_pb2
from textql_sdk._connect.public.chat_pb2 import WatchChatRequest
from textql_sdk.models import (
    ConnectError,
    TextqlRPCPublicParadigmParadigm,
    TextqlRPCPublicParadigmUniversalOptions,
    Universal,
)
from textql_sdk.streaming import create_streaming_client

# Non-terminal states worth showing. Anything absent is either terminal (see
# cell_status) or too noisy to be useful (CREATING, CREATED).
LIFECYCLE_MARKERS = {
    chat_pb2.LIFECYCLE_EXECUTING: "⏳ executing",
    chat_pb2.LIFECYCLE_HANDOFF_PENDING: "⏸  waiting for input",
}


def cell_text(cell) -> str:
    """Pull the human-readable text out of a Cell.

    A Cell is a oneof over ~50 cell types; `WhichOneof("value")` names the
    active one and each keeps its text in a different field. We cover the
    common conversational types and fall back to the type name otherwise.
    """
    kind = cell.WhichOneof("value")
    if kind is None:
        return "(empty)"
    payload = getattr(cell, kind)
    url = getattr(payload, "url", "")
    if url:
        name = getattr(payload, "name", "")
        return f"{name}: {url}" if name else url
    for field_name in ("content", "summary", "status", "query", "code"):
        text = getattr(payload, field_name, "")
        if text:
            return text
    return f"({kind})"


def cell_status(cell) -> str:
    """One-line terminal status for a cell that just reported complete."""
    if cell.exec_error:
        return f"✗ failed: {cell.exec_error}"
    if cell.lifecycle == chat_pb2.LIFECYCLE_HALTED:
        return "⏹  halted"
    took = f" ({cell.duration_ms}ms)" if cell.HasField("duration_ms") else ""
    return f"✓ done{took}"


@dataclass
class CellView:
    """What we've already rendered for one cell, so we only print what changed."""

    text: str = ""
    lifecycle: int = chat_pb2.LIFECYCLE_UNKNOWN
    complete: bool = False
    failed: bool = False
    opened: bool = False


def render_cell(cell, views: dict[str, CellView]) -> None:
    view = views.setdefault(cell.id, CellView())
    text = cell_text(cell)

    if not view.opened:
        print(f"\n[{cell.WhichOneof('value')} {cell.id[:8]}] ", end="", flush=True)
        view.opened = True

    if text.startswith(view.text):
        # Monotonic growth — the common case while a cell streams tokens.
        delta = text[len(view.text) :]
        if delta:
            print(delta, end="", flush=True)
    elif text != view.text:
        # Content was replaced rather than appended, e.g. a SQL cell swapping
        # its query for query + results on EXECUTING -> EXECUTED. Slicing a
        # delta here would print garbage, so reprint the whole thing.
        print(f"\n  ↻ {text}", end="", flush=True)
    view.text = text

    if cell.lifecycle != view.lifecycle:
        view.lifecycle = cell.lifecycle
        marker = LIFECYCLE_MARKERS.get(cell.lifecycle)
        if marker:
            print(f"  {marker}", end="", flush=True)

    # Latch `complete` so a re-emitted snapshot doesn't print the status twice.
    if cell.complete and not view.complete:
        view.complete = True
        view.failed = bool(cell.exec_error)
        print(f"\n  {cell_status(cell)}", flush=True)


async def main() -> None:
    load_dotenv()
    message = (
        sys.argv[1] if len(sys.argv) > 1 else "Tell me about this month's usage?"
    )

    # Configure the SDK once; streaming inherits its server + API key.
    # Set TEXTQL_SERVER_URL for on-prem/dev; it defaults to the cloud server.
    sdk = Textql(
        api_key=os.environ["TEXTQL_API_KEY"],
        server_url=os.environ.get("TEXTQL_SERVER_URL"),
        async_client=httpx.AsyncClient(
            follow_redirects=True,
            timeout=httpx.Timeout(None, connect=10.0),
        ),
    )
    streaming = create_streaming_client(sdk)

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
        model="MODEL_SONNET_5",
        paradigm=paradigm,
    )
    if isinstance(created, ConnectError):
        raise RuntimeError(f"create_chat failed: {created}")
    assert created.chat is not None
    chat_id = created.chat.id
    print(f"Chat created: {chat_id}")

    opened = asyncio.Event()
    views: dict[str, CellView] = {}

    async def watch() -> None:
        try:
            async for event in streaming.chats.watch_chat(
                WatchChatRequest(chat_id=chat_id)
            ):
                kind = event.WhichOneof("payload")
                if kind == "opened":
                    print("watch opened")
                    opened.set()
                elif kind == "cell":
                    render_cell(event.cell, views)
                elif kind == "run_started":
                    print("run started")
                elif kind == "run_complete":
                    # A run completes even when individual cells failed, so
                    # report those instead of a bare "run complete".
                    failed = [cid for cid, v in views.items() if v.failed]
                    pending = [cid for cid, v in views.items() if not v.complete]
                    print("\nrun complete")
                    if failed:
                        ids = ", ".join(c[:8] for c in failed)
                        print(f"  {len(failed)} cell(s) failed: {ids}")
                    if pending:
                        print(f"  {len(pending)} cell(s) never reached a terminal state")
                    return
                elif kind == "run_error":
                    print()
                    raise RuntimeError(f"run error: {event.run_error}")
                elif kind == "heartbeat":
                    pass  # keepalive
        except ConnectRpcError as e:
            raise RuntimeError(f"watch_chat failed: {e.code}") from e

    watch_task = asyncio.create_task(watch())
    await opened.wait()

    # 3) Start the run; watch_task receives cells + lifecycle until run_complete.
    run = await sdk.chats.run_async(chat_id=chat_id, model="MODEL_SONNET_5")
    if isinstance(run, ConnectError):
        watch_task.cancel()
        raise RuntimeError(f"run failed: {run}")

    await watch_task


if __name__ == "__main__":
    asyncio.run(main())
