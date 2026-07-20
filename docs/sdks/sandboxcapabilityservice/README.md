# SandboxCapabilityService

## Overview

### Available Operations

* [sandbox_capability_service_execute_write](#sandbox_capability_service_execute_write) - ExecuteWrite
* [sandbox_capability_service_put_asset](#sandbox_capability_service_put_asset) - PutAsset
* [sandbox_capability_service_send_notify](#sandbox_capability_service_send_notify) - SendNotify
* [sandbox_capability_service_state_op](#sandbox_capability_service_state_op) - StateOp

## sandbox_capability_service_execute_write

ExecuteWrite

### Example Usage

<!-- UsageSnippet language="python" operationID="SandboxCapabilityService_ExecuteWrite" method="post" path="/textql.rpc.public.sandbox_capability.SandboxCapabilityService/ExecuteWrite" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.sandbox_capability_service.sandbox_capability_service_execute_write()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                                    | *Optional[float]*                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                      | N/A                                                                                                                                                                     |
| `name`                                                                                                                                                                  | *Optional[str]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | N/A                                                                                                                                                                     |
| `connector_id`                                                                                                                                                          | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | N/A                                                                                                                                                                     |
| `statement`                                                                                                                                                             | *Optional[str]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | N/A                                                                                                                                                                     |
| `parameters`                                                                                                                                                            | List[[models.TextqlRPCPublicSandboxQuerySandboxQueryParam](../../models/textqlrpcpublicsandboxquerysandboxqueryparam.md)]                                               | :heavy_minus_sign:                                                                                                                                                      | N/A                                                                                                                                                                     |
| `max_rows`                                                                                                                                                              | [Optional[models.TextqlRPCPublicSandboxCapabilitySandboxExecuteWriteRequestMaxRows]](../../models/textqlrpcpublicsandboxcapabilitysandboxexecutewriterequestmaxrows.md) | :heavy_minus_sign:                                                                                                                                                      | N/A                                                                                                                                                                     |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.SandboxCapabilityServiceExecuteWriteResponse](../../models/sandboxcapabilityserviceexecutewriteresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## sandbox_capability_service_put_asset

PutAsset

### Example Usage

<!-- UsageSnippet language="python" operationID="SandboxCapabilityService_PutAsset" method="post" path="/textql.rpc.public.sandbox_capability.SandboxCapabilityService/PutAsset" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.sandbox_capability_service.sandbox_capability_service_put_asset()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `file_name`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `content_type`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `data`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SandboxCapabilityServicePutAssetResponse](../../models/sandboxcapabilityserviceputassetresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## sandbox_capability_service_send_notify

SendNotify

### Example Usage

<!-- UsageSnippet language="python" operationID="SandboxCapabilityService_SendNotify" method="post" path="/textql.rpc.public.sandbox_capability.SandboxCapabilityService/SendNotify" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.sandbox_capability_service.sandbox_capability_service_send_notify()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                      | *Optional[float]*                                                                                                         | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `name`                                                                                                                    | *Optional[str]*                                                                                                           | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `subject`                                                                                                                 | *Optional[str]*                                                                                                           | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `body`                                                                                                                    | *Optional[str]*                                                                                                           | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `parameters`                                                                                                              | List[[models.TextqlRPCPublicSandboxQuerySandboxQueryParam](../../models/textqlrpcpublicsandboxquerysandboxqueryparam.md)] | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |

### Response

**[models.SandboxCapabilityServiceSendNotifyResponse](../../models/sandboxcapabilityservicesendnotifyresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## sandbox_capability_service_state_op

StateOp

### Example Usage

<!-- UsageSnippet language="python" operationID="SandboxCapabilityService_StateOp" method="post" path="/textql.rpc.public.sandbox_capability.SandboxCapabilityService/StateOp" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.sandbox_capability_service.sandbox_capability_service_state_op()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `op`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `scope`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `key`                                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `value`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SandboxCapabilityServiceStateOpResponse](../../models/sandboxcapabilityservicestateopresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |