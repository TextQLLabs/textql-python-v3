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
sdk = Textql(api_key=..., server_url="https://your-host")  # e.g. from TEXTQL_SERVER_URL
streaming = create_streaming_client(sdk)  # streams to https://your-host/rpc/public
```

Without an SDK instance, pass `api_key=` directly (`server_url` then defaults to
the same server list the generated SDK uses, from the Speakeasy config):

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
runtime in `pyproject.toml`; bump them together.
