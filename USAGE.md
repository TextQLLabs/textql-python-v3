<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from textql_sdk import Textql


with Textql() as textql:

    res = textql.agents.create()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from textql_sdk import Textql

async def main():

    async with Textql() as textql:

        res = await textql.agents.create_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->