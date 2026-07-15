# SandboxAdmin

## Overview

### Available Operations

* [get_sandbox](#get_sandbox) - GetSandbox
* [list_sandbox_egress](#list_sandbox_egress) - Outbound HTTP(S) calls a sandbox made (the egress ledger). Durable — reads  the recorded table, so it works for stopped sandboxes too.
* [list_executions](#list_executions) - ListSandboxExecutions
* [list_sandbox_files](#list_sandbox_files) - Live filesystem of a running sandbox. Both are NO-OP (read-only) and only  return data while the worker is alive; available=false otherwise.
* [list_sandbox_spend](#list_sandbox_spend) - Per-lease compute usage for a sandbox, computed from lease durations × the  compute rate. Durable (reads the lease table), so it works for stopped  sandboxes. This is usage (ACUs), not the invoiced dollar amount.
* [list](#list) - ListSandboxes
* [read_file](#read_file) - ReadSandboxFile
* [restart_sandbox](#restart_sandbox) - Restart a stopped/reaped sandbox by re-acquiring a worker for the same  sandbox_id, preserving the original owner. Same scoping as StopSandbox  (owner, or sandbox:write_private for org-wide).
* [stop](#stop) - StopSandbox

## get_sandbox

GetSandbox

### Example Usage

<!-- UsageSnippet language="python" operationID="SandboxAdminService_GetSandbox" method="post" path="/textql.rpc.public.sandbox_admin.SandboxAdminService/GetSandbox" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.sandbox_admin.get_sandbox()

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

**[models.SandboxAdminServiceGetSandboxResponse](../../models/sandboxadminservicegetsandboxresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_sandbox_egress

Outbound HTTP(S) calls a sandbox made (the egress ledger). Durable — reads
 the recorded table, so it works for stopped sandboxes too.

### Example Usage

<!-- UsageSnippet language="python" operationID="SandboxAdminService_ListSandboxEgress" method="post" path="/textql.rpc.public.sandbox_admin.SandboxAdminService/ListSandboxEgress" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.sandbox_admin.list_sandbox_egress()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `connect_timeout_ms`                                                     | *Optional[float]*                                                        | :heavy_minus_sign:                                                       | N/A                                                                      |
| `sandbox_id`                                                             | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | N/A                                                                      |
| `limit`                                                                  | *Optional[int]*                                                          | :heavy_minus_sign:                                                       | Max calls to return (newest first). Server clamps to a sane default/cap. |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |

### Response

**[models.SandboxAdminServiceListSandboxEgressResponse](../../models/sandboxadminservicelistsandboxegressresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_executions

ListSandboxExecutions

### Example Usage

<!-- UsageSnippet language="python" operationID="SandboxAdminService_ListSandboxExecutions" method="post" path="/textql.rpc.public.sandbox_admin.SandboxAdminService/ListSandboxExecutions" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.sandbox_admin.list_executions()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `sandbox_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SandboxAdminServiceListSandboxExecutionsResponse](../../models/sandboxadminservicelistsandboxexecutionsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_sandbox_files

Live filesystem of a running sandbox. Both are NO-OP (read-only) and only
 return data while the worker is alive; available=false otherwise.

### Example Usage

<!-- UsageSnippet language="python" operationID="SandboxAdminService_ListSandboxFiles" method="post" path="/textql.rpc.public.sandbox_admin.SandboxAdminService/ListSandboxFiles" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.sandbox_admin.list_sandbox_files()

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

## list_sandbox_spend

Per-lease compute usage for a sandbox, computed from lease durations × the
 compute rate. Durable (reads the lease table), so it works for stopped
 sandboxes. This is usage (ACUs), not the invoiced dollar amount.

### Example Usage

<!-- UsageSnippet language="python" operationID="SandboxAdminService_ListSandboxSpend" method="post" path="/textql.rpc.public.sandbox_admin.SandboxAdminService/ListSandboxSpend" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.sandbox_admin.list_sandbox_spend()

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

**[models.SandboxAdminServiceListSandboxSpendResponse](../../models/sandboxadminservicelistsandboxspendresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list

ListSandboxes

### Example Usage

<!-- UsageSnippet language="python" operationID="SandboxAdminService_ListSandboxes" method="post" path="/textql.rpc.public.sandbox_admin.SandboxAdminService/ListSandboxes" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.sandbox_admin.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `status`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | One of: running \| stopped \| all. Defaults to running.             |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SandboxAdminServiceListSandboxesResponse](../../models/sandboxadminservicelistsandboxesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## read_file

ReadSandboxFile

### Example Usage

<!-- UsageSnippet language="python" operationID="SandboxAdminService_ReadSandboxFile" method="post" path="/textql.rpc.public.sandbox_admin.SandboxAdminService/ReadSandboxFile" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.sandbox_admin.read_file()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `sandbox_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `path`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | File to read, relative to the sandbox files root.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SandboxAdminServiceReadSandboxFileResponse](../../models/sandboxadminservicereadsandboxfileresponse.md)**

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

    res = text_ql.sandbox_admin.restart_sandbox()

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