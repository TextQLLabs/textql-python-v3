"""Watch a chat over the Connect-RPC streaming bridge.

Server-streaming RPCs aren't part of the generated REST SDK, so they live in
`textql_sdk.streaming`. `watch_chat` emits the full run lifecycle plus every
cell as it's produced. See STREAMING.md for the other streaming methods.

    uv run python examples/watch_chat.py <chat_id>
"""

import asyncio
import os
import sys

from dotenv import load_dotenv
from connectrpc.errors import ConnectError

from textql_sdk import Textql
from textql_sdk.streaming import create_streaming_client
from textql_sdk._connect.public.chat_pb2 import WatchChatRequest


async def main() -> None:
    load_dotenv()
    if len(sys.argv) < 2:
        raise SystemExit("usage: python examples/watch_chat.py <chat_id>")
    chat_id = sys.argv[1]

    # Configure the SDK once; streaming inherits its server + API key.
    # Set TEXTQL_SERVER_URL for on-prem/dev; it defaults to the cloud server.
    sdk = Textql(
        api_key=os.environ["TEXTQL_API_KEY"],
        server_url=os.environ.get("TEXTQL_SERVER_URL"),
    )
    streaming = create_streaming_client(sdk)

    try:
        async for event in streaming.chats.watch_chat(WatchChatRequest(chat_id=chat_id)):
            kind = event.WhichOneof("payload")
            if kind == "cell":
                print(f"cell: {event.cell.id}")
            elif kind == "run_started":
                print("run started")
            elif kind == "run_complete":
                print("run complete")
                break
            elif kind == "run_error":
                print(f"run error: {event.run_error}")
                break
            elif kind == "heartbeat":
                pass  # keepalive
    except ConnectError as e:
        raise RuntimeError(f"watch_chat failed: {e.code}") from e


if __name__ == "__main__":
    asyncio.run(main())
