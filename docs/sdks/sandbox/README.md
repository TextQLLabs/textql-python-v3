# Sandbox

## Overview

### Available Operations

* [execute_query](#execute_query) - ExecuteQuery

## execute_query

ExecuteQuery

### Example Usage

<!-- UsageSnippet language="python" operationID="SandboxQueryService_ExecuteQuery" method="post" path="/textql.rpc.public.sandbox_query.SandboxQueryService/ExecuteQuery" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.sandbox.execute_query(body={
        "sql_query": {},
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                             | Type                                                                                                                                  | Required                                                                                                                              | Description                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                                | [models.TextqlRPCPublicSandboxQuerySandboxExecuteQueryRequest](../../models/textqlrpcpublicsandboxquerysandboxexecutequeryrequest.md) | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `connect_timeout_ms`                                                                                                                  | *Optional[float]*                                                                                                                     | :heavy_minus_sign:                                                                                                                    | N/A                                                                                                                                   |
| `retries`                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                      | :heavy_minus_sign:                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                   |

### Response

**[models.SandboxQueryServiceExecuteQueryResponse](../../models/sandboxqueryserviceexecutequeryresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |