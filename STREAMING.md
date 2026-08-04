# Streaming (Connect-RPC bridge)

The TextQL API exposes several **server-streaming** RPCs that have no HTTP/JSON
shape in the OpenAPI spec, so they are not part of the Speakeasy-generated SDK
surface. This package bridges them with [Connect-RPC](https://connectrpc.com)
via `textql_sdk.streaming` — a hand-written module that talks the Connect
protocol directly to the same gateway, authenticated with the same
`tql_api_key`.

> Prefer `watch_chat` for anything long-lived — it carries run lifecycle events
> (`run_started`, `run_complete`, `run_error`) and heartbeats; `stream_chat` is
> the run-scoped cell firehose for one-shot scripts.

## Usage

Configure the server and API key once on the `Textql` SDK; streaming inherits
both. You never pass a server URL or deal with the `/rpc/public` mount:

```python
import asyncio, os
from textql_sdk import Textql
from textql_sdk.streaming import create_streaming_client
from textql_sdk._connect.public.chat_pb2 import WatchChatRequest


async def main():
    sdk = Textql(api_key=os.environ["TEXTQL_API_KEY"])  # server_url optional
    streaming = create_streaming_client(sdk)

    async for event in streaming.chats.watch_chat(WatchChatRequest(chat_id=chat_id)):
        payload = event.WhichOneof("payload")
        if payload == "cell":
            ...  # event.cell is a Cell
        elif payload == "run_complete":
            ...  # run finished
        elif payload == "heartbeat":
            pass  # keepalive, safe to ignore


asyncio.run(main())
```

An on-prem/dev host set on the SDK is picked up automatically:

```python
sdk = Textql(api_key=..., server_url="https://your-host")
streaming = create_streaming_client(sdk)  # streams to https://your-host/rpc/public
```

Setting `TEXTQL_SERVER_URL` names the host once for every client instead —
`Textql()`, `create_streaming_client()`, and `create_connect_client()` all read
it, and an explicit `server_url` still wins. Without an SDK instance, pass
`api_key=` directly and the same lookup applies, falling back to the server list
the generated SDK uses (from the Speakeasy config):

```python
streaming = create_streaming_client(api_key=os.environ["TEXTQL_API_KEY"])
```

### Sync

Use `create_streaming_client_sync` for a blocking iterator instead of an async
one:

```python
from textql_sdk.streaming import create_streaming_client_sync

streaming = create_streaming_client_sync(sdk)
for update in streaming.agents.stream_agent_status(StreamAgentStatusRequest()):
    print(update.agent_id, update.status)
```

## Streaming methods

| Method | Emits |
| --- | --- |
| `chats.watch_chat(WatchChatRequest(chat_id=...))` | `WatchChatEvent` (opened, cell, run lifecycle, handoff, heartbeat) |
| `chats.stream_chat(RunChatRequest(...))` | `Cell` per update while a run executes |
| `agents.stream_agent_status(StreamAgentStatusRequest())` | `AgentStatusUpdate` for every visible agent run transition |
| `apps.stream_app_activity(StreamAppActivityRequest(app_id=...))` | `AppActivityStreamEvent` (activity batches, presence, heartbeat) |
| `dashboards.watch_dashboard_health(WatchDashboardHealthRequest(dashboard_id=...))` | `DashboardHealthEvent` on health transitions |
| `playbooks.stream_template_data_status(StreamTemplateDataStatusRequest(...))` | `TemplateDataStatusUpdate` per template-data row |

Request/response types live under `textql_sdk._connect.public.<service>_pb2`.

### Reading cell state

`watch_chat` and `stream_chat` emit a **full snapshot** of a cell on every
update, never a delta. Key by `cell.id` and replace what you're holding — don't
concatenate, or a cell that rewrites its content mid-run (a SQL cell swapping
its query for query + results) will render as garbage.

Three fields tell you where a cell is:

| Field | Use it for |
| --- | --- |
| `complete` | Terminal state. **Branch on this**, not on `lifecycle`. |
| `lifecycle` | `LIFECYCLE_EXECUTING` — render the cell as in-flight. |
| `exec_error` | Per-cell failure. |

`complete` is polymorphic server-side: a non-executable cell (markdown, text) is
complete as soon as it's created, while an executable one (SQL, Python) is only
complete once it has executed or halted. Comparing `lifecycle` to
`LIFECYCLE_EXECUTED` yourself marks every markdown cell as never finishing.

`exec_error` is per cell and is **not** covered by the `run_error` event — a run
can reach `run_complete` with individual cells that failed. Check both.

`examples/watch_chat.py` implements this.

For any other service in `textql_sdk._connect`, use the escape hatch:

```python
from textql_sdk.streaming import create_connect_client
from textql_sdk._connect.public.feed_connect import FeedServiceClient

feed = create_connect_client(FeedServiceClient, sdk)
```

## Notes

- **Transport**: server-streaming rides on the `connect-python` runtime
  (`pyqwest`). Client-streaming RPCs are not exercised by this bridge.
- **Types**: streaming methods return protobuf message types (vendored under
  `textql_sdk._connect`), which differ in shape from the Speakeasy-generated
  Pydantic models for the same protos.
- **Long-lived idle streams** may be closed by intermediary proxies if nothing
  is sent for a while; `watch_chat` and `stream_app_activity` send periodic
  heartbeats, the others emit only on activity. Wrap consumption in a reconnect
  loop for anything long-running.

## Regenerating the vendored types

`src/textql_sdk/_connect` is generated from the platform protos (not by
Speakeasy — it survives `speakeasy run`):

```bash
DEMO2_DIR=/path/to/demo2 ./scripts/generate-connect.sh
```

The buf plugin versions in that script are pinned to match the `connect-python`
runtime; bump them together.

The last step runs `scripts/postprocess-connect.py`, which fixes up what the
codegen leaves behind. It is idempotent, so you can also run it standalone
against an already-generated tree:

- **Relative-ises absolute imports in the `.pyi` stubs.** protoletariat only
  rewrites the `.py` files: its patterns key on protoc's alias convention
  (`import auth_pb2 as auth__pb2`), while the pyi plugin emits
  `as _auth_pb2`, so nothing matches. It decides what stays absolute by what is
  on disk, which is why it runs *after* the tree is trimmed — `google/api` is
  kept and becomes relative, `google/protobuf` is deleted and stays absolute so
  it resolves from the installed runtime.
- **Prunes package-stub entries** for the subtrees the script deletes.
- **Prepends `# pylint: skip-file` and `# mypy: ignore-errors`.** Generated
  protobuf code is never clean under either tool (~64k pylint messages), and CI
  runs both. `ignore-errors` only suppresses *reporting* inside those files, so
  callers still get real protobuf types.

## Dependencies: edit gen.yaml, never pyproject.toml

`pyproject.toml` and `pylintrc` are Speakeasy-managed (they are listed in
`.speakeasy/gen.lock`) and are regenerated from scratch on every
`speakeasy run`. Anything hand-added to them is silently dropped on the next
generation — which then fails CI, because `uv sync --dev` uninstalls the
runtime deps and the whole `_connect` tree stops resolving.

The runtime and typing deps this bridge needs therefore live in
`.speakeasy/gen.yaml`, which Speakeasy renders into `pyproject.toml`:

```yaml
python:
  additionalDependencies:
    main:
      connect-python: ">=0.9.0"
      protobuf: ">=6.31,<8"
    dev:
      types-protobuf: ">=6.31"
```

For the same reason, lint/typecheck opt-outs for the generated tree cannot go
in `pyproject.toml` or `pylintrc` — they are injected per-file by
`scripts/postprocess-connect.py`.
