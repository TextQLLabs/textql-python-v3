# Mcps

## Overview

### Available Operations

* [clear_o_auth_token](#clear_o_auth_token) - ClearOAuthToken
* [get_servers](#get_servers) - GetMCPServers

## clear_o_auth_token

ClearOAuthToken

### Example Usage

<!-- UsageSnippet language="python" operationID="MCPService_ClearOAuthToken" method="post" path="/textql.rpc.public.mcp.MCPService/ClearOAuthToken" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.mcps.clear_o_auth_token()

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

**[models.MCPServiceClearOAuthTokenResponse](../../models/mcpserviceclearoauthtokenresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_servers

GetMCPServers

### Example Usage

<!-- UsageSnippet language="python" operationID="MCPService_GetMCPServers" method="post" path="/textql.rpc.public.mcp.MCPService/GetMCPServers" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.mcps.get_servers(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                  | [models.TextqlRPCPublicMCPGetMCPServersRequest](../../models/textqlrpcpublicmcpgetmcpserversrequest.md) | :heavy_check_mark:                                                                                      | N/A                                                                                                     |
| `connect_timeout_ms`                                                                                    | *Optional[float]*                                                                                       | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.MCPServiceGetMCPServersResponse](../../models/mcpservicegetmcpserversresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |