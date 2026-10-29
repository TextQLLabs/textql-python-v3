# Harnesses

## Overview

### Available Operations

* [list](#list) - ListHarnesses

## list

ListHarnesses

### Example Usage

<!-- UsageSnippet language="python" operationID="HarnessService_ListHarnesses" method="post" path="/textql.rpc.public.harness.HarnessService/ListHarnesses" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY"),
) as textql:

    res = textql.harnesses.list(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                          | [models.TextqlRPCPublicHarnessListHarnessesRequest](../../models/textqlrpcpublicharnesslistharnessesrequest.md) | :heavy_check_mark:                                                                                              | N/A                                                                                                             |
| `connect_timeout_ms`                                                                                            | *Optional[float]*                                                                                               | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.HarnessServiceListHarnessesResponse](../../models/harnessservicelistharnessesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |