# textql-sdk examples

Runnable scripts for the Python SDK. Every example works the same under **pip**
or **uv** — pick whichever your project already uses.

| Example | What it shows |
| --- | --- |
| [`watch_chat.py`](watch_chat.py) | One chat, one run, streamed over Connect-RPC and printed as a flat event log |
| [`list_chats.py`](list_chats.py) | List chats with paging, sorting, and search |
| [`chat_history.py`](chat_history.py) | Page through a chat's cells and render each one |
| [`cancel_chat.py`](cancel_chat.py) | Start a long-running chat and cancel it mid-run |
| [`create_agent.py`](create_agent.py) | Create an agent and trigger it |
| [`create_playbook.py`](create_playbook.py) | Create a scheduled playbook and configure delivery |

## Setup

The examples need the SDK plus `python-dotenv` (used only to load `.env`; the
SDK itself doesn't require it).

### pip

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e .                 # or: pip install textql-sdk
pip install python-dotenv
```

### uv

```bash
uv venv --python 3.11            # first time only
uv sync
uv add python-dotenv
```

## Credentials

Create a `.env` at the repo root:

```bash
TEXTQL_API_KEY=your-api-key
# Optional — set for on-prem/dev; defaults to the cloud server.
TEXTQL_SERVER_URL=https://app.textql.com
```

The examples that create a chat (`watch_chat.py`, `cancel_chat.py`) expect a
real connector: replace the placeholder `connector_ids=[1]` in the paradigm
with your own connector ID(s). The read-only ones (`list_chats.py`,
`chat_history.py`) work as-is.

## Running

With pip, activate the venv and run the script directly:

```bash
python examples/watch_chat.py
```

With uv, prefix the same command with `uv run`:

```bash
uv run python examples/watch_chat.py
```

Both are run from the repo root, not from inside `examples/`.

## Streaming

Server-streaming RPCs (`watch_chat`, `stream_chat`, …) aren't part of the
generated REST surface — they live in `textql_sdk.streaming`, over Connect-RPC.
See [STREAMING.md](../STREAMING.md) for the full method list and the details of
the bridge.
