# RBACService

## Overview

RBAC service for managing roles, permissions, and access control

### Available Operations

* [rbac_service_set_role_permissions](#rbac_service_set_role_permissions) - Bulk add/remove permissions on a role in one call, producing a single audit entry for the whole edit.

## rbac_service_set_role_permissions

Bulk add/remove permissions on a role in one call, producing a single audit entry for the whole edit.

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_SetRolePermissions" method="post" path="/textql.rpc.public.rbac.RBACService/SetRolePermissions" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac_service.rbac_service_set_role_permissions()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `role_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `add_permission_ids`                                                | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `remove_permission_ids`                                             | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RBACServiceSetRolePermissionsResponse](../../models/rbacservicesetrolepermissionsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |