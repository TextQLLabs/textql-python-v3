# SandboxAdminService

## Overview

### Available Operations

* [list_sandbox_files](#list_sandbox_files) - Live filesystem of a running sandbox. Both are NO-OP (read-only) and only  return data while the worker is alive; available=false otherwise.
* [restart_sandbox](#restart_sandbox) - Restart a stopped/reaped sandbox by re-acquiring a worker for the same  sandbox_id, preserving the original owner. Same scoping as StopSandbox  (owner, or sandbox:write_private for org-wide).

## list_sandbox_files

Live filesystem of a running sandbox. Both are NO-OP (read-only) and only
 return data while the worker is alive; available=false otherwise.

### Example Usage

<!-- UsageSnippet language="python" operationID="SandboxAdminService_ListSandboxFiles" method="post" path="/textql.rpc.public.sandbox_admin.SandboxAdminService/ListSandboxFiles" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.sandbox_admin_service.list_sandbox_files()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `sandbox_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `path`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Directory to list, relative to the sandbox files root ("" = root).  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SandboxAdminServiceListSandboxFilesResponse](../../models/sandboxadminservicelistsandboxfilesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## restart_sandbox

Restart a stopped/reaped sandbox by re-acquiring a worker for the same
 sandbox_id, preserving the original owner. Same scoping as StopSandbox
 (owner, or sandbox:write_private for org-wide).

### Example Usage

<!-- UsageSnippet language="python" operationID="SandboxAdminService_RestartSandbox" method="post" path="/textql.rpc.public.sandbox_admin.SandboxAdminService/RestartSandbox" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.sandbox_admin_service.restart_sandbox()

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

**[models.SandboxAdminServiceRestartSandboxResponse](../../models/sandboxadminservicerestartsandboxresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |