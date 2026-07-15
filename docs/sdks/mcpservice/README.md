# McpService

## Overview

### Available Operations

* [handle_o_auth_callback](#handle_o_auth_callback) - HandleOAuthCallback

## handle_o_auth_callback

HandleOAuthCallback

### Example Usage

<!-- UsageSnippet language="python" operationID="MCPService_HandleOAuthCallback" method="post" path="/textql.rpc.public.mcp.MCPService/HandleOAuthCallback" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.mcp_service.handle_o_auth_callback()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `server_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `code`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `state`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MCPServiceHandleOAuthCallbackResponse](../../models/mcpservicehandleoauthcallbackresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |