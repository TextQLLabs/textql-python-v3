"""Async chat — useful when embedding TextQL in a FastAPI or async service.

This example exercises the full chat creation API: model selection,
research mode, fast inference, methodology, and paradigm. It then runs
the chat, reads the history, and cleans up.

    uv run python examples/async_chat.py
"""

import asyncio
import os
from dotenv import load_dotenv
from textql_sdk import Textql
from textql_sdk.models import (
    ConnectError,
    SQL,
    TextqlRPCPublicParadigmParadigm,
    TextqlRPCPublicParadigmSQLOptions,
)

load_dotenv()

async def main():
    async with Textql(api_key=os.environ["TEXTQL_API_KEY"], server_url="http://app.textql.com") as sdk:

        sql_paradigm = TextqlRPCPublicParadigmParadigm(
            type="TYPE_SQL",
            options=SQL(sql=TextqlRPCPublicParadigmSQLOptions(
                connector_ids=[1234, 5678],  # replace with your connector IDs
            )),
        )

        chat = await sdk.chats.create_chat_async(
            message="Which connector has the most data, and how does it compare to last month?",
            model="MODEL_SONNET_5",
            paradigm=sql_paradigm,
        )
        if isinstance(chat, ConnectError):
            raise RuntimeError(f"create_chat failed: {chat}")
        assert chat.chat is not None
        chat_id = chat.chat.id
        print(f"Chat created: {chat_id}")

        run = await sdk.chats.run_async(
            chat_id=chat_id,
            model="MODEL_SONNET_4_6",
            research=True,
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
            role = "user" if cell else "assistant"
            preview = str(cell or "")[:120].replace("\n", " ")
            print(f"\n[{role}] {preview}")


asyncio.run(main())
