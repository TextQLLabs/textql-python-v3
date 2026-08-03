"""Start a long-running chat, then cancel it mid-run.

`run` holds its connection open for the whole run, so to cancel one you need
the run in flight while you do something else — here it's an asyncio task, and
the SDK's async client is configured with no read timeout so it isn't cut off
early. `cancel_stream` answers with `exists`: True if there was a live stream
to kill, False if the run had already finished. `get(chat_id).chat.is_running`
is how you observe the state either side of it.

Activate your venv, then:

    python examples/cancel_chat.py

With uv, prefix the same command with `uv run`:

    uv run python examples/cancel_chat.py

See examples/README.md for setup under either package manager.
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

# Deliberately open-ended so the run is still going when we cancel it.
PROMPT = "Profile every table you can see, one at a time, in as much detail as possible."
POLL_INTERVAL_S = 1.0
POLL_TIMEOUT_S = 90.0
# Let the run do a little work first, so there's something to interrupt.
GRACE_S = 10.0


async def main() -> None:
    load_dotenv()
    sdk = Textql(
        api_key=os.environ["TEXTQL_API_KEY"],
        server_url=os.environ.get("TEXTQL_SERVER_URL"),
        async_client=httpx.AsyncClient(
            follow_redirects=True,
            timeout=httpx.Timeout(None, connect=10.0),
        ),
    )

    async def is_running(chat_id: str) -> bool:
        resp = await sdk.chats.get_async(chat_id=chat_id)
        if isinstance(resp, ConnectError):
            raise RuntimeError(f"get failed: {resp}")
        assert resp.chat is not None
        return bool(resp.chat.is_running)

    async def wait_for_running(chat_id: str, *, running: bool) -> bool:
        """Poll until `is_running` matches `running`. False on timeout."""
        deadline = asyncio.get_running_loop().time() + POLL_TIMEOUT_S
        while asyncio.get_running_loop().time() < deadline:
            if await is_running(chat_id) == running:
                return True
            await asyncio.sleep(POLL_INTERVAL_S)
        return False

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
        message=PROMPT,
        model="MODEL_SONNET_5",
        paradigm=paradigm,
    )
    if isinstance(created, ConnectError):
        raise RuntimeError(f"create_chat failed: {created}")
    assert created.chat is not None
    chat_id = created.chat.id
    assert isinstance(chat_id, str), "create_chat returned no chat ID"
    print(f"Chat created: {chat_id}")

    # Fire the run without awaiting it — it only returns once the run ends.
    run_task = asyncio.create_task(
        sdk.chats.run_async(chat_id=chat_id, model="MODEL_SONNET_5")
    )
    print("Run started — waiting for the chat to report is_running…")

    try:
        if not await wait_for_running(chat_id, running=True):
            raise SystemExit(
                f"Chat never started running within {POLL_TIMEOUT_S:.0f}s "
                "— nothing to cancel."
            )
        print(f"Chat is running — letting it work for {GRACE_S:.0f}s, then cancelling…")
        await asyncio.sleep(GRACE_S)

        # True = there was a live stream and we killed it.
        cancelled = await sdk.chats.cancel_stream_async(chat_id=chat_id)
        if isinstance(cancelled, ConnectError):
            raise RuntimeError(f"cancel_stream failed: {cancelled}")
        print(f"cancel_stream: exists={cancelled.exists}")

        if await wait_for_running(chat_id, running=False):
            print("Chat is no longer running — cancel took effect.")
        else:
            print(f"Still running after {POLL_TIMEOUT_S:.0f}s — cancel didn't land.")
    finally:
        # The cancelled run returns (or errors) shortly after; don't leak the task.
        run_task.cancel()
        await asyncio.gather(run_task, return_exceptions=True)

    # Whatever the run produced before the cancel is still in the history.
    history = await sdk.chats.get_history_async(chat_id=chat_id, limit=10)
    if isinstance(history, ConnectError):
        raise RuntimeError(f"get_history failed: {history}")
    print("\nCells produced before the cancel:")
    for cell in history.cells or []:
        kind, text = cell_text(cell)
        print(f"  {kind:<16} {text.replace(chr(10), ' ')[:100] or '(no text)'}")


if __name__ == "__main__":
    asyncio.run(main())
