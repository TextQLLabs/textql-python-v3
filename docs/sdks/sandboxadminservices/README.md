# SandboxAdminServices

## Overview

### Available Operations

* [list_sandbox_egress](#list_sandbox_egress) - Outbound HTTP(S) calls a sandbox made (the egress ledger). Durable — reads  the recorded table, so it works for stopped sandboxes too.
* [list_sandbox_spend](#list_sandbox_spend) - Per-lease compute usage for a sandbox, computed from lease durations × the  compute rate. Durable (reads the lease table), so it works for stopped  sandboxes. This is usage (ACUs), not the invoiced dollar amount.

## list_sandbox_egress

Outbound HTTP(S) calls a sandbox made (the egress ledger). Durable — reads
 the recorded table, so it works for stopped sandboxes too.

### Example Usage

<!-- UsageSnippet language="python" operationID="SandboxAdminService_ListSandboxEgress" method="post" path="/textql.rpc.public.sandbox_admin.SandboxAdminService/ListSandboxEgress" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.sandbox_admin_services.list_sandbox_egress()

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

## list_sandbox_spend

Per-lease compute usage for a sandbox, computed from lease durations × the
 compute rate. Durable (reads the lease table), so it works for stopped
 sandboxes. This is usage (ACUs), not the invoiced dollar amount.

### Example Usage

<!-- UsageSnippet language="python" operationID="SandboxAdminService_ListSandboxSpend" method="post" path="/textql.rpc.public.sandbox_admin.SandboxAdminService/ListSandboxSpend" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.sandbox_admin_services.list_sandbox_spend()

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