# Sandboxes

## Overview

### Available Operations

* [list_executions](#list_executions) - ListSandboxExecutions
* [list](#list) - ListSandboxes
* [read_file](#read_file) - ReadSandboxFile

## list_executions

ListSandboxExecutions

### Example Usage

<!-- UsageSnippet language="python" operationID="SandboxAdminService_ListSandboxExecutions" method="post" path="/textql.rpc.public.sandbox_admin.SandboxAdminService/ListSandboxExecutions" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.sandboxes.list_executions()

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

## list

ListSandboxes

### Example Usage

<!-- UsageSnippet language="python" operationID="SandboxAdminService_ListSandboxes" method="post" path="/textql.rpc.public.sandbox_admin.SandboxAdminService/ListSandboxes" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.sandboxes.list()

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

    res = text_ql.sandboxes.read_file()

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