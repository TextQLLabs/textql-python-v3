# McpServices

## Overview

### Available Operations

* [upsert_mcp_servers](#upsert_mcp_servers) - UpsertMCPServers

## upsert_mcp_servers

UpsertMCPServers

### Example Usage

<!-- UsageSnippet language="python" operationID="MCPService_UpsertMCPServers" method="post" path="/textql.rpc.public.mcp.MCPService/UpsertMCPServers" -->
```python
from textql_sdk import TextQL
from textql_sdk.utils import parse_datetime


with TextQL() as text_ql:

    res = text_ql.mcp_services.upsert_mcp_servers(mcp_servers=[
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