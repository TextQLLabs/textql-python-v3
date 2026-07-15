# Rbacs

## Overview

### Available Operations

* [get_role](#get_role) - GetRole

## get_role

GetRole

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_GetRole" method="post" path="/textql.rpc.public.rbac.RBACService/GetRole" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.rbacs.get_role()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `role_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RBACServiceGetRoleResponse](../../models/rbacservicegetroleresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |