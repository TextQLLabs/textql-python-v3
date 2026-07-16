<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
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
        api_key=os.getenv("TEXTQL_API_KEY", ""),
    ) as textql:

        res = await textql.agents.create_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->