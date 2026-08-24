"""Hold one chat open and keep sending turns to it.

There is no session object — multi-turn is a `chat_id` you hold onto.
`chats.send(chat_id=...)` appends your message, starts a run server-side and
returns immediately; everything the model produces arrives on `watch_chat`,
which subscribes to *the chat*, not to your send. One stream serves the whole
conversation: the server's chat pubsub is persistent, emitting `run_complete`
per run and resetting on the next `run_started`.

Attach the watch **before** the first send, or a fast run's early cells are
already gone when you subscribe. The initial attach sends no
`latest_complete_cell_id`, so the server replays the chat's full history —
that's why resuming an existing chat prints its backlog. Reconnects do send it,
and replay only what was missed.

Typing while a run is in flight sends with `steering=True`: the message is
delivered *into* the running turn ("stop, actually do X") instead of queueing
another one. A model that doesn't support steering takes it as an ordinary
turn. Output keeps printing while you type, so a mid-run line looks garbled in
the terminal — it still sends fine.

Unlike `watch_chat.py`, this reconnects forever with a capped backoff: a
session left open for an afternoon should outlive a deploy. Codes that
reconnecting can't fix (auth, permissions, not-found) still raise.

    python examples/multi_turn.py                 # new chat
    python examples/multi_turn.py <chat-id>       # resume an existing chat

`/quit` or ctrl-D ends the session; the chat stays. With uv, prefix the command
with `uv run`. See examples/README.md for setup and STREAMING.md for the other
streaming RPCs.
"""

# pylint: disable=no-member,no-name-in-module
# chat_pb2 builds its members at import time, so pylint can't see
# WatchChatRequest. Suppressed in-file because pylintrc is Speakeasy-managed and
# overwritten on every `speakeasy run` (see scripts/postprocess-connect.py).
# pyright, which gates CI, resolves it fine.

import asyncio
import os
import ssl
import sys
import threading
from contextlib import aclosing
from typing import Any, AsyncGenerator, Optional, cast

import httpx
import truststore
from connectrpc.code import Code
from connectrpc.errors import ConnectError as ConnectRpcError
from dotenv import load_dotenv

from textql_sdk import Textql
from textql_sdk._connect.public.chat_pb2 import WatchChatEvent, WatchChatRequest
from textql_sdk.cell_render import CellPrinter
from textql_sdk.models import (
    ConnectError,
    TextqlRPCPublicParadigmParadigm,
    TextqlRPCPublicParadigmUniversalOptions,
    Universal,
)
from textql_sdk.streaming import create_streaming_client

PROMPT = "you>  "
# Longer than the server's ~20s heartbeat, so only a wedged connection trips it.
WATCHDOG_TIMEOUT_S = 30.0
BASE_RECONNECT_DELAY_S = 0.5
MAX_RECONNECT_DELAY_S = 30.0

RETRYABLE_CODES = frozenset(
    {
        Code.UNAVAILABLE,
        Code.DEADLINE_EXCEEDED,
        Code.RESOURCE_EXHAUSTED,
        Code.ABORTED,
        Code.INTERNAL,
    }
)


class Prompt:
    """The `you> ` line, drawn at most once between turns: the input loop and
    the watcher both want to draw it, and a resumed chat replays `run_complete`."""

    def __init__(self) -> None:
        self._shown = False

    def show(self) -> None:
        if self._shown:
            return
        self._shown = True
        print(PROMPT, end="", flush=True)

    def clear(self) -> None:
        """Call before the watcher prints: the prompt left the line open, so
        cells would start halfway across it."""
        if self._shown:
            print(flush=True)
        self._shown = False

    def consumed(self) -> None:
        """Call after the user submits: their newline already ended the line."""
        self._shown = False


def stdin_lines() -> "asyncio.Queue[Optional[str]]":
    """Pump stdin into a queue from a daemon thread — a blocking read can't be
    cancelled, and a non-daemon one holds exit open. `None` is EOF (ctrl-D)."""
    loop = asyncio.get_running_loop()
    queue: "asyncio.Queue[Optional[str]]" = asyncio.Queue()

    def pump() -> None:
        for line in sys.stdin:
            loop.call_soon_threadsafe(queue.put_nowait, line.strip())
        loop.call_soon_threadsafe(queue.put_nowait, None)

    threading.Thread(target=pump, daemon=True, name="stdin").start()
    return queue


async def create_chat(sdk: Textql) -> str:
    """Create an empty chat. `create_chat(message=...)` only pre-fills the first
    cell — it starts no run, so the first turn goes through `send` like the rest."""
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
    created = await sdk.chats.create_chat_async(
        model="MODEL_SONNET_5",
        paradigm=paradigm,
    )
    if isinstance(created, ConnectError):
        raise RuntimeError(f"create_chat failed: {created}")
    assert created.chat is not None
    chat_id = created.chat.id
    assert isinstance(chat_id, str), "create_chat returned a chat with no ID"
    return chat_id


class Watcher:
    """One `watch_chat` subscription, held open across every turn."""

    def __init__(
        self, streaming: Any, chat_id: str, out: CellPrinter, prompt: Prompt
    ) -> None:
        self._streaming = streaming
        self._chat_id = chat_id
        self._out = out
        self._prompt = prompt
        self._cursor = ""
        self._latest_complete_cell_id = ""
        self._reported_failed: set[str] = set()
        self._healthy = False
        self.opened = asyncio.Event()
        # Set while a run is in flight, so the next line typed steers it.
        self.running = asyncio.Event()

    def _request(self) -> WatchChatRequest:
        request = WatchChatRequest(chat_id=self._chat_id)
        if self._latest_complete_cell_id:
            request.latest_complete_cell_id = self._latest_complete_cell_id
        if self._cursor:
            request.resume_cursor = self._cursor
        return request

    def _handle(self, event: WatchChatEvent) -> None:
        self._healthy = True  # resets the reconnect backoff in run_forever
        if event.cursor:
            self._cursor = event.cursor

        kind = event.WhichOneof("payload")
        if kind == "opened":
            self.opened.set()
        elif kind == "cell":
            if event.cell.complete:
                self._latest_complete_cell_id = event.cell.id
            self._prompt.clear()
            self._out.cell(event.cell)
        elif kind == "run_started":
            self.running.set()
            self._prompt.clear()
            self._out.note("run", "started")
        elif kind == "run_complete":
            self._end_turn(event.run_complete.final_cell_id, "completed")
        elif kind == "run_error":
            # Not fatal: the chat is still usable, so re-prompt for the next turn.
            self._end_turn("", f"failed: {event.run_error}")
        elif kind == "handoff_pending":
            self._prompt.clear()
            self._out.note("handoff", event.handoff_pending.handoff_marker)
        # heartbeat: keepalive, nothing to print.

    def _end_turn(self, final_cell_id: str, status: str) -> None:
        self._prompt.clear()
        self._out.flush()
        if final_cell_id:
            self._latest_complete_cell_id = final_cell_id
        # `run_complete` fires even when cells failed, and the printer keeps
        # every cell of the session — so report only this turn's failures.
        failed = [c for c in self._out.failed() if c not in self._reported_failed]
        self._reported_failed.update(failed)
        self._out.note("done", status)
        if failed:
            self._out.note("", f"{len(failed)} cell(s) failed: " + ", ".join(failed))
        self.running.clear()
        self._prompt.show()

    async def _consume(self) -> None:
        """Consume one connection until it ends. Raises `asyncio.TimeoutError` if
        it goes quiet; `aclosing` releases the socket `wait_for` left mid-read."""
        stream = cast(
            AsyncGenerator[WatchChatEvent, None],
            self._streaming.chats.watch_chat(self._request()),
        )
        async with aclosing(stream) as events:
            while True:
                event = await asyncio.wait_for(anext(events, None), WATCHDOG_TIMEOUT_S)
                if event is None:
                    return
                self._handle(event)

    async def run_forever(self) -> None:
        attempt = 0
        while True:
            try:
                await self._consume()
                # The server ends the stream to ask for a reconnect when its
                # event source goes unhealthy — not a failure.
                reason = "stream ended"
            except asyncio.TimeoutError:
                reason = f"no events for {WATCHDOG_TIMEOUT_S:.0f}s"
            except ConnectRpcError as e:
                if e.code is Code.CANCELED:
                    # The transport turns our own `task.cancel()` into a Connect
                    # error; put it back or the task ends "failed" and prints.
                    raise asyncio.CancelledError from None
                # Idle streams get closed by proxies on long runs, so retry from
                # the cursor — but only for codes that mean a lost connection.
                if e.code not in RETRYABLE_CODES:
                    raise
                reason = f"stream dropped ({e.code.value})"

            if self._healthy:
                attempt = 0  # the last connection worked, so this drop is fresh
                self._healthy = False
            attempt += 1
            delay = min(
                BASE_RECONNECT_DELAY_S * 2 ** (attempt - 1), MAX_RECONNECT_DELAY_S
            )
            self._prompt.clear()
            self._out.note("retry", f"{reason}; reconnecting in {delay:.1f}s")
            await asyncio.sleep(delay)


async def converse(
    sdk: Textql,
    chat_id: str,
    lines: "asyncio.Queue[Optional[str]]",
    watcher: Watcher,
    out: CellPrinter,
    prompt: Prompt,
) -> None:
    """Send every line typed. Returns on `/quit` or ctrl-D."""
    prompt.show()
    while True:
        line = await lines.get()
        prompt.consumed()  # the terminal echoed the line and its newline
        if line is None or line in ("/quit", "/exit"):
            out.note("bye", chat_id)
            return
        if not line:
            prompt.show()
            continue

        steering = watcher.running.is_set()
        sent = await sdk.chats.send_async(
            chat_id=chat_id, message=line, steering=steering
        )
        if isinstance(sent, ConnectError):
            out.note("error", f"send failed: {sent}")
            prompt.show()
            continue

        # `run_started` lags the send by a cold sandbox's boot, so treat the run
        # as live now — else a line typed in that gap opens a competing turn.
        watcher.running.set()
        out.note(
            "sent",
            f"cell {sent.cell_id}" + ("  (steering the active run)" if steering else ""),
        )


async def main() -> None:
    load_dotenv()

    # Set TEXTQL_SERVER_URL for on-prem/dev; it defaults to the cloud server.
    ctx = truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    sdk = Textql(
        api_key=os.environ["TEXTQL_API_KEY"],
        server_url=os.environ.get("TEXTQL_SERVER_URL"),
        async_client=httpx.AsyncClient(
            follow_redirects=True,
            timeout=httpx.Timeout(None, connect=10.0),
            verify=ctx,
        ),
    )
    streaming = create_streaming_client(sdk)

    out = CellPrinter()
    prompt = Prompt()
    lines = stdin_lines()

    chat_id = sys.argv[1] if len(sys.argv) > 1 else await create_chat(sdk)
    out.note("chat", chat_id)

    watcher = Watcher(streaming, chat_id, out, prompt)
    watch_task = asyncio.create_task(watcher.run_forever())

    # Subscribe before the first send, or a fast run's early cells are gone.
    opened_task = asyncio.create_task(watcher.opened.wait())
    await asyncio.wait({watch_task, opened_task}, return_when=asyncio.FIRST_COMPLETED)
    if not watcher.opened.is_set():
        opened_task.cancel()
        await watch_task  # re-raises whatever kept the stream from opening
        raise RuntimeError("watch ended before the chat opened")

    talk_task = asyncio.create_task(converse(sdk, chat_id, lines, watcher, out, prompt))
    done, pending = await asyncio.wait(
        {watch_task, talk_task}, return_when=asyncio.FIRST_COMPLETED
    )
    for task in pending:
        task.cancel()
    # Or asyncio reports the cancelled watcher as an unretrieved exception.
    await asyncio.gather(*pending, return_exceptions=True)
    for task in done:
        task.result()  # surface a watcher failure instead of exiting quietly


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print()
