"""A live interactive chat: one chat, many turns, one stream.

`watch_chat` attaches to a *chat* rather than to a run, so a single stream spans
the whole conversation — `run_complete` ends a turn, not the session. That makes
it the right primitive for a REPL, and it's why this script keeps one long-lived
watch task while the prompt loop drives turn after turn.

Each turn is two unary calls: `send_message` queues the user turn, then
`run_chat` starts the agent. `run_chat` doesn't return until the run finishes,
so the cells arrive on the watch stream, not from its return value.

    uv run python examples/interactive_chat.py             # start a new chat
    uv run python examples/interactive_chat.py <chat_id>   # resume an existing one

With pip, activate your venv and drop the `uv run` prefix:

    python examples/interactive_chat.py

See examples/README.md for setup under either package manager.

Resuming replays the chat's existing cells before the first prompt, so you see
the context you're continuing from.

Type /exit (or Ctrl-D) to quit. Ctrl-C mid-turn cancels the in-flight run before
exiting, since dropping the stream on its own would leave the agent running.
"""

import asyncio
import os
import sys

import httpx
from connectrpc.errors import ConnectError as ConnectRpcError
from dotenv import load_dotenv

from textql_sdk import Textql
from textql_sdk._connect.public.chat_pb2 import WatchChatRequest
from textql_sdk.models import (
    ConnectError,
    TextqlRPCPublicParadigmParadigm,
    TextqlRPCPublicParadigmUniversalOptions,
    Universal,
)
from textql_sdk.streaming import create_streaming_client

MODEL = "MODEL_SONNET_5"
RECONNECT_DELAY_S = 2.0


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
    for field in ("content", "summary", "status", "query", "code"):
        text = getattr(payload, field, "")
        if text:
            return text
    return f"({kind})"


def check(result, what: str):
    """Unary methods return `Union[Result, ConnectError]` — and that ConnectError
    is a pydantic model, not an exception, so an unchecked call fails later at
    the attribute access instead of here. (Streams raise the *other*
    ConnectError, `connectrpc.errors.ConnectError`.)"""
    if isinstance(result, ConnectError):
        raise RuntimeError(f"{what} failed: {result}")
    return result


class Printer:
    """Prints cells as deltas, since a cell is re-sent as it grows.

    State outlives any single turn: cells are keyed by id, so the same instance
    keeps working across the whole conversation.
    """

    def __init__(self) -> None:
        self._printed: dict[str, int] = {}
        self._open_id = ""

    def feed(self, cell) -> None:
        if cell.id != self._open_id:
            self.close()
            print(f"[{cell.WhichOneof('value')} {cell.id}] ", end="", flush=True)
            self._open_id = cell.id
        text = cell_text(cell)
        already = self._printed.get(cell.id, 0)
        if len(text) > already:
            print(text[already:], end="", flush=True)
            self._printed[cell.id] = len(text)

    def close(self) -> None:
        """End the in-progress cell line, if any."""
        if self._open_id:
            print()
            self._open_id = ""


async def prompt(label: str = "\nyou> ") -> str:
    """input() blocks the event loop, which would stall the watch task and its
    heartbeats, so it goes to a thread."""
    return await asyncio.to_thread(input, label)


async def converse(sdk, streaming, chat_id: str, read_line=prompt) -> None:
    """Drive turns against an existing chat until the user quits."""
    printer = Printer()
    opened = asyncio.Event()
    turn_done = asyncio.Event()

    async def watch() -> None:
        """One stream for the whole session, reconnecting as needed.

        Idle streams get closed by intermediary proxies, so a dropped connection
        is normal rather than fatal. Replaying the last `cursor` as
        `resume_cursor` picks up where we left off instead of redelivering the
        whole chat.
        """
        cursor = ""
        while True:
            try:
                async for event in streaming.chats.watch_chat(
                    WatchChatRequest(chat_id=chat_id, resume_cursor=cursor)
                ):
                    if event.cursor:
                        cursor = event.cursor
                    kind = event.WhichOneof("payload")

                    if kind == "cell":
                        printer.feed(event.cell)
                    elif kind == "opened":
                        opened.set()
                    elif kind == "run_started":
                        printer.close()
                        print("--- run started")
                    elif kind == "run_complete":
                        printer.close()
                        print("--- run complete")
                        turn_done.set()  # ends the turn, not the session
                    elif kind == "handoff_pending":
                        # The agent halted for input (an approval or questions
                        # cell). No run_complete is coming, so release the
                        # prompt: the next message is the answer.
                        printer.close()
                        print(
                            "--- waiting for your input "
                            f"({event.handoff_pending.handoff_marker})"
                        )
                        turn_done.set()
                    elif kind == "run_error":
                        printer.close()
                        print(f"--- run error: {event.run_error.error}")
                        turn_done.set()
                    elif kind == "heartbeat":
                        pass  # keepalive
            except asyncio.CancelledError:
                raise
            except ConnectRpcError as e:
                printer.close()
                print(f"--- stream dropped ({e.code}), resuming in {RECONNECT_DELAY_S}s")
                await asyncio.sleep(RECONNECT_DELAY_S)
            else:
                # A clean end of stream (rather than an error) means the server
                # closed it; reattach with the cursor.
                await asyncio.sleep(RECONNECT_DELAY_S)

    watch_task = asyncio.create_task(watch())
    try:
        await opened.wait()

        while True:
            try:
                message = (await read_line()).strip()
            except EOFError:
                print()
                break
            if not message:
                continue
            if message in ("/exit", "/quit"):
                break

            turn_done.clear()
            check(
                await sdk.chats.send_async(chat_id=chat_id, message=message),
                "send_message",
            )
            try:
                # run_chat is unary and doesn't return until the run ends; the
                # cells arrive on the watch stream meanwhile. Checking its result
                # before waiting matters: a failed run emits no run_complete, so
                # waiting first would hang forever.
                check(
                    await sdk.chats.run_async(chat_id=chat_id, model=MODEL),
                    "run_chat",
                )
                # The stream can still be draining cells after run_chat returns,
                # so the turn ends on run_complete rather than on that return.
                await turn_done.wait()
            except (asyncio.CancelledError, KeyboardInterrupt):
                # Abandoning the stream doesn't stop the run; the server keeps
                # going until told otherwise.
                await sdk.chats.cancel_stream_async(chat_id=chat_id)
                raise
    finally:
        watch_task.cancel()
        await asyncio.gather(watch_task, return_exceptions=True)
        print(f"\nchat id: {chat_id}")
        print(f"resume with: uv run python examples/interactive_chat.py {chat_id}")


async def main() -> None:
    load_dotenv()
    resume_chat_id = sys.argv[1] if len(sys.argv) > 1 else None

    # Configure the SDK once; streaming inherits its server + API key.
    # The read timeout must stay unset: turns can idle for minutes.
    sdk = Textql(
        api_key=os.environ["TEXTQL_API_KEY"],
        server_url=os.environ.get("TEXTQL_SERVER_URL"),
        async_client=httpx.AsyncClient(
            follow_redirects=True,
            timeout=httpx.Timeout(None, connect=10.0),
        ),
    )
    streaming = create_streaming_client(sdk)

    if resume_chat_id:
        chat_id = resume_chat_id
        print(f"Resuming chat: {chat_id}")
    else:
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
        # No `message=` here: the prompt loop sends every turn, including the
        # first, so there's one code path instead of two.
        created = check(
            await sdk.chats.create_chat_async(model=MODEL, paradigm=paradigm),
            "create_chat",
        )
        assert created.chat is not None
        chat_id = created.chat.id
        print(f"Chat created: {chat_id}")

    await converse(sdk, streaming, chat_id)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
