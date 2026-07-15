# McpServers

## Overview

### Available Operations

* [delete](#delete) - DeleteMCPServer

## delete

DeleteMCPServer

### Example Usage

<!-- UsageSnippet language="python" operationID="MCPService_DeleteMCPServer" method="post" path="/textql.rpc.public.mcp.MCPService/DeleteMCPServer" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.mcp_servers.delete()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `id`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MCPServiceDeleteMCPServerResponse](../../models/mcpservicedeletemcpserverresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |