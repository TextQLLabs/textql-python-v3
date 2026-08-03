"""List chats in your org, newest first.

`get_all` is paginated (`limit`/`offset`) and returns `total_count` alongside
the page, so you can keep paging until you've seen everything. It also takes
filters — `search_term`, `bookmarked_only`, `created_after`, `source`, … — see
docs/sdks/chats for the full set.

Activate your venv, then:

    python examples/list_chats.py
    python examples/list_chats.py "revenue"

With uv, prefix the same command with `uv run`:

    uv run python examples/list_chats.py "revenue"

See examples/README.md for setup under either package manager.
"""

import os
import sys

from dotenv import load_dotenv

from textql_sdk import Textql
from textql_sdk.models import ConnectError

PAGE_SIZE = 10

load_dotenv()
sdk = Textql(
    api_key=os.environ["TEXTQL_API_KEY"],
    server_url=os.environ.get("TEXTQL_SERVER_URL"),
)

search_term = sys.argv[1] if len(sys.argv) > 1 else None

resp = sdk.chats.get_all(
    limit=PAGE_SIZE,
    offset=0,
    search_term=search_term,
    sort_by="CHAT_SORT_FIELD_UPDATED_AT",
    sort_direction="CHAT_SORT_DIRECTION_DESC",
)
if isinstance(resp, ConnectError):
    raise RuntimeError(f"get_all failed: {resp}")

chats = resp.chats or []
print(f"{len(chats)} of {resp.total_count} chat(s)")
for chat in chats:
    updated = chat.updated_at.isoformat() if chat.updated_at else "—"
    running = " [running]" if chat.is_running else ""
    print(f"  {chat.id}  {updated}  {chat.summary or '(untitled)'}{running}")

# Paging: bump `offset` by PAGE_SIZE until you've collected `total_count`.
if resp.total_count and resp.total_count > len(chats):
    print(f"\n… {resp.total_count - len(chats)} more; re-run with offset={PAGE_SIZE}")
