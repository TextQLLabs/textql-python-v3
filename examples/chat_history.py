"""Print the cell history of a chat.

`get_history` returns the chat's cells oldest-first, paginated with
`limit`/`skip` and a `has_more` flag. A cell is a union over ~50 variants
(`TextCell`, `PyCell`, `SQLCell`, …); `textql_sdk.helpers.cell_text` unwraps
any of them into a `(kind, text)` pair so you don't have to match on each type.

Pass a chat ID, or omit it to use your most recently updated chat.
Activate your venv, then:

    python examples/chat_history.py
    python examples/chat_history.py <chat-id>

With uv, prefix the same command with `uv run`:

    uv run python examples/chat_history.py <chat-id>

See examples/README.md for setup under either package manager.
"""

import os
import sys

from dotenv import load_dotenv

from textql_sdk import Textql
from textql_sdk.helpers import cell_text
from textql_sdk.models import ConnectError

PAGE_SIZE = 50

load_dotenv()
sdk = Textql(
    api_key=os.environ["TEXTQL_API_KEY"],
    server_url=os.environ.get("TEXTQL_SERVER_URL"),
)

def most_recent_chat_id() -> str:
    """The org's most recently updated chat — see examples/list_chats.py."""
    listed = sdk.chats.get_all(
        limit=1,
        sort_by="CHAT_SORT_FIELD_UPDATED_AT",
        sort_direction="CHAT_SORT_DIRECTION_DESC",
    )
    if isinstance(listed, ConnectError):
        raise RuntimeError(f"get_all failed: {listed}")
    chats = listed.chats or []
    if not chats:
        raise SystemExit("No chats in this org — run examples/watch_chat.py first.")
    chat_id = chats[0].id
    assert isinstance(chat_id, str), "get_all returned a chat with no ID"
    print(f"Using most recent chat: {chat_id} — {chats[0].summary or '(untitled)'}")
    return chat_id


chat_id = sys.argv[1] if len(sys.argv) > 1 else most_recent_chat_id()

# Page through the history; `skip` is the offset, `has_more` says keep going.
skip = 0
while True:
    resp = sdk.chats.get_history(chat_id=chat_id, limit=PAGE_SIZE, skip=skip)
    if isinstance(resp, ConnectError):
        raise RuntimeError(f"get_history failed: {resp}")

    cells = resp.cells or []
    for cell in cells:
        kind, text = cell_text(cell)
        stamp = cell.timestamp.isoformat() if cell.timestamp else "—"
        # Cells stream in, so a trailing one may still be incomplete.
        pending = "" if cell.complete else " …"
        preview = text.replace("\n", " ")[:120] or "(no text)"
        print(f"[{stamp}] {kind:<16} {preview}{pending}")

    skip += len(cells)
    if not resp.has_more or not cells:
        break

print(f"\n{skip} cell(s) total")
