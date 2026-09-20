# Mcp

## Overview

### Available Operations

* [clear_o_auth_token](#clear_o_auth_token) - ClearOAuthToken
* [delete](#delete) - DeleteMCPServer
* [get_servers](#get_servers) - GetMCPServers
* [handle_o_auth_callback](#handle_o_auth_callback) - HandleOAuthCallback
* [initiate_o_auth_flow](#initiate_o_auth_flow) - InitiateOAuthFlow
* [toggle_server](#toggle_server) - ToggleMCPServer
* [upsert_mcp_servers](#upsert_mcp_servers) - UpsertMCPServers

## clear_o_auth_token

ClearOAuthToken

### Example Usage

<!-- UsageSnippet language="python" operationID="MCPService_ClearOAuthToken" method="post" path="/textql.rpc.public.mcp.MCPService/ClearOAuthToken" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.mcp.clear_o_auth_token()

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

## delete

DeleteMCPServer

### Example Usage

<!-- UsageSnippet language="python" operationID="MCPService_DeleteMCPServer" method="post" path="/textql.rpc.public.mcp.MCPService/DeleteMCPServer" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.mcp.delete()

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

## get_servers

GetMCPServers

### Example Usage

<!-- UsageSnippet language="python" operationID="MCPService_GetMCPServers" method="post" path="/textql.rpc.public.mcp.MCPService/GetMCPServers" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.mcp.get_servers(body={})

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

## handle_o_auth_callback

HandleOAuthCallback

### Example Usage

<!-- UsageSnippet language="python" operationID="MCPService_HandleOAuthCallback" method="post" path="/textql.rpc.public.mcp.MCPService/HandleOAuthCallback" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.mcp.handle_o_auth_callback()

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

## initiate_o_auth_flow

InitiateOAuthFlow

### Example Usage

<!-- UsageSnippet language="python" operationID="MCPService_InitiateOAuthFlow" method="post" path="/textql.rpc.public.mcp.MCPService/InitiateOAuthFlow" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.mcp.initiate_o_auth_flow()

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
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.mcp.toggle_server()

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

## upsert_mcp_servers

UpsertMCPServers

### Example Usage

<!-- UsageSnippet language="python" operationID="MCPService_UpsertMCPServers" method="post" path="/textql.rpc.public.mcp.MCPService/UpsertMCPServers" -->
```python
import os
from textql_sdk import Textql
from textql_sdk.utils import parse_datetime


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.mcp.upsert_mcp_servers(mcp_servers=[
        {
            "sse_config": {},
            "created_at": parse_datetime("2023-01-15T01:30:15.01Z"),
            "updated_at": parse_datetime("2023-01-15T01:30:15.01Z"),
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                    | *Optional[float]*                                                                       | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `mcp_servers`                                                                           | List[[models.TextqlRPCPublicMCPMCPServer](../../models/textqlrpcpublicmcpmcpserver.md)] | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.MCPServiceUpsertMCPServersResponse](../../models/mcpserviceupsertmcpserversresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |