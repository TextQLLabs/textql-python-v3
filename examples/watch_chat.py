"""Create a chat, then watch it stream over the Connect-RPC bridge.

Server-streaming RPCs aren't part of the generated REST SDK, so they live in
`textql_sdk.streaming`. Prefer `watch_chat` for anything long-lived — it carries
run lifecycle events (`run_started`, `run_complete`, `run_error`) plus every
cell as it's produced. See STREAMING.md for the other streaming methods.

    uv run python examples/watch_chat.py
    uv run python examples/watch_chat.py "plot sinx"
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

    printed: dict[str, int] = {}
    streaming_id = ""

    async def watch() -> None:
        nonlocal streaming_id
        try:
            async for event in streaming.chats.watch_chat(
                WatchChatRequest(chat_id=chat_id)
            ):
                kind = event.WhichOneof("payload")
                if kind == "opened":
                    print("watch opened")
                    opened.set()
                elif kind == "cell":
                    cell = event.cell
                    text = cell_text(cell)
                    if cell.id != streaming_id:
                        if streaming_id:
                            print()
                        print(f"[{cell.WhichOneof('value')} {cell.id}] ", end="", flush=True)
                        streaming_id = cell.id
                    already = printed.get(cell.id, 0)
                    if len(text) > already:
                        print(text[already:], end="", flush=True)
                        printed[cell.id] = len(text)
                elif kind == "run_started":
                    print("run started")
                elif kind == "run_complete":
                    if streaming_id:
                        print()  # close the last cell line
                    print("run complete")
                    return
                elif kind == "run_error":
                    if streaming_id:
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
