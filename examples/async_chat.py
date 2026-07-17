"""Async chat — useful when embedding TextQL in a FastAPI or async service.

This example exercises the full chat creation API: model selection,
research mode, fast inference, methodology, and paradigm. It then runs
the chat, reads the history, and cleans up.

    uv run python examples/async_chat.py
"""

import asyncio
import os
import httpx
from dotenv import load_dotenv
from textql_sdk import Textql
from textql_sdk.helpers import cell_text
from textql_sdk.models import (
    ConnectError,
    TextqlRPCPublicParadigmParadigm,
    TextqlRPCPublicParadigmUniversalOptions,
    Universal,
)

load_dotenv()


async def main():
    async with Textql(
        api_key=os.environ["TEXTQL_API_KEY"],
        server_url="https://rodney.ngrok.io",
        async_client=httpx.AsyncClient(follow_redirects=True, timeout=None),
    ) as sdk:

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

        chat = await sdk.chats.create_chat_async(
            message="Tell me about this month's usage?",
            model="MODEL_SONNET_5",
            paradigm=paradigm,
        )
        if isinstance(chat, ConnectError):
            raise RuntimeError(f"create_chat failed: {chat}")
        assert chat.chat is not None
        chat_id = chat.chat.id
        print(f"Chat created: {chat_id}")

        run = await sdk.chats.run_async(
            chat_id=chat_id,
            model="MODEL_SONNET_4_6",
            fast_mode=False,
        )
        if isinstance(run, ConnectError):
            raise RuntimeError(f"run failed: {run}")
        print("Run complete.")

        history = await sdk.chats.get_history_async(chat_id=chat_id)
        if isinstance(history, ConnectError):
            raise RuntimeError(f"get_history failed: {history}")
        assert history.cells is not None
        print(f"\nHistory: {len(history.cells)} cell(s)")
        for cell in history.cells or []:
            kind, text = cell_text(cell)
            print(f"\n[{kind}]\n{text}")


asyncio.run(main())
