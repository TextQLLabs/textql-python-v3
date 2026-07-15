<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.agents.create()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from textql_sdk import TextQL

async def main():

    async with TextQL() as text_ql:

        res = await text_ql.agents.create_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->