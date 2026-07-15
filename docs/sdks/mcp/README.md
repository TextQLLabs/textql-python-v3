# Mcp

## Overview

### Available Operations

* [initiate_o_auth_flow](#initiate_o_auth_flow) - InitiateOAuthFlow
* [toggle_server](#toggle_server) - ToggleMCPServer

## initiate_o_auth_flow

InitiateOAuthFlow

### Example Usage

<!-- UsageSnippet language="python" operationID="MCPService_InitiateOAuthFlow" method="post" path="/textql.rpc.public.mcp.MCPService/InitiateOAuthFlow" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.mcp.initiate_o_auth_flow()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `server_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MCPServiceInitiateOAuthFlowResponse](../../models/mcpserviceinitiateoauthflowresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## toggle_server

ToggleMCPServer

### Example Usage

<!-- UsageSnippet language="python" operationID="MCPService_ToggleMCPServer" method="post" path="/textql.rpc.public.mcp.MCPService/ToggleMCPServer" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.mcp.toggle_server()

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

**[models.MCPServiceToggleMCPServerResponse](../../models/mcpservicetogglemcpserverresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |