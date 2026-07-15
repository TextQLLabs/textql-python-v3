# SandboxAdmin

## Overview

### Available Operations

* [stop](#stop) - StopSandbox

## stop

StopSandbox

### Example Usage

<!-- UsageSnippet language="python" operationID="SandboxAdminService_StopSandbox" method="post" path="/textql.rpc.public.sandbox_admin.SandboxAdminService/StopSandbox" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.sandbox_admin.stop()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `sandbox_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SandboxAdminServiceStopSandboxResponse](../../models/sandboxadminservicestopsandboxresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |