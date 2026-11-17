<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY"),
) as textql:

    res = textql.agents.create()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
import os
from textql_sdk import Textql

async def main():

    async with Textql(
        api_key=os.getenv("TEXTQL_API_KEY"),
    ) as textql:

        res = await textql.agents.create_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->
## Get numbers from a completed run

`query_one_shot` starts a run and returns its chat ID immediately; its answer
and cells are not completed results. The handwritten `wait_for_tables` helper
waits for completion using the existing polling RPC, then returns the existing
typed SQL dataframes from the latest turn:

```python
from textql_sdk.helpers import table_rows, wait_for_tables

started = sdk.chats.query_one_shot(question="Show revenue by month", paradigm=paradigm)
tables = wait_for_tables(sdk, started.chat_id, timeout=300)
for table in tables:
    print(table.preview)  # True means the server returned a truncated preview.
    print(table_rows(table))  # int, float, bool, string, or None for SQL NULL.
```

Pass the chat ID returned by an agent trigger or playbook run in the same way.
The helper does not start a run. Do not start another turn on that chat while
waiting. It uses the SDK's configured authentication, server, and HTTP client;
the deployment must already support `PollChatEvents` and turn-complete history
pagination (`GetChatHistory` with `limit=1`).

The return value is a list of `TextqlRPCPublicDataframeDataFrameWithInfo` objects;
it preserves schema, info, and preview flags. `table_rows` converts protobuf integer
strings to Python integers and empty values to `None`. Decimal columns use doubles.
Each record contains one row. The server caps each SQL table at 100 rows.
The server caps inline rows at 64 KiB per history response. It does not download full tables
when `preview` is true. A text-only answer returns `[]`: numbers written only in
prose are not extracted, and this is not caller-defined, schema-validated JSON.
Run errors and failed/incomplete SQL cells raise `RuntimeError`; waiting longer
than `timeout` raises `TimeoutError`. SDK HTTP/transport errors propagate, and a
transport timeout may occur sooner. A timeout does not cancel the server run.

Until using an SDK release containing this helper, consume the run lifecycle with
`watch_chat` (see [STREAMING.md](STREAMING.md)), then call
`sdk.chats.get_history(chat_id=chat_id, limit=1)` and inspect each
`SQLCell.sql_cell.dataframe`, including `exec_error`, `complete`, and `preview`.

Inline SQL rows require the server fix for B-360129. Only the chat owner can read
these rows. The server checks current chat and connector read access on each request.
Shared chats, other cell types, and old results return metadata. `table_rows` raises
`ValueError` when the server omits rows. Check `table.preview` before using a partial result.
