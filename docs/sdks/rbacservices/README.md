# RbacServices

## Overview

### Available Operations

* [assign_role_to_member](#assign_role_to_member) - Member role assignment
* [get_role_permissions](#get_role_permissions) - GetRolePermissions
* [list_scim_group_mappings](#list_scim_group_mappings) - ListScimGroupMappings
* [migrate_all_scim_group_mappings](#migrate_all_scim_group_mappings) - MigrateAllScimGroupMappings
* [revoke_object_access](#revoke_object_access) - RevokeObjectAccess

## assign_role_to_member

Member role assignment

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_AssignRoleToMember" method="post" path="/textql.rpc.public.rbac.RBACService/AssignRoleToMember" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.rbac_services.assign_role_to_member()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `member_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `role_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RBACServiceAssignRoleToMemberResponse](../../models/rbacserviceassignroletomemberresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_role_permissions

GetRolePermissions

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_GetRolePermissions" method="post" path="/textql.rpc.public.rbac.RBACService/GetRolePermissions" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.rbac_services.get_role_permissions()

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

**[models.RBACServiceGetRolePermissionsResponse](../../models/rbacservicegetrolepermissionsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_scim_group_mappings

ListScimGroupMappings

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_ListScimGroupMappings" method="post" path="/textql.rpc.public.rbac.RBACService/ListScimGroupMappings" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.rbac_services.list_scim_group_mappings(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                    | [models.TextqlRPCPublicRbacListScimGroupMappingsRequest](../../models/textqlrpcpublicrbaclistscimgroupmappingsrequest.md) | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |
| `connect_timeout_ms`                                                                                                      | *Optional[float]*                                                                                                         | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |

### Response

**[models.RBACServiceListScimGroupMappingsResponse](../../models/rbacservicelistscimgroupmappingsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## migrate_all_scim_group_mappings

MigrateAllScimGroupMappings

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_MigrateAllScimGroupMappings" method="post" path="/textql.rpc.public.rbac.RBACService/MigrateAllScimGroupMappings" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.rbac_services.migrate_all_scim_group_mappings(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                             | Type                                                                                                                                  | Required                                                                                                                              | Description                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                                | [models.TextqlRPCPublicRbacMigrateAllScimGroupMappingsRequest](../../models/textqlrpcpublicrbacmigrateallscimgroupmappingsrequest.md) | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `connect_timeout_ms`                                                                                                                  | *Optional[float]*                                                                                                                     | :heavy_minus_sign:                                                                                                                    | N/A                                                                                                                                   |
| `retries`                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                      | :heavy_minus_sign:                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                   |

### Response

**[models.RBACServiceMigrateAllScimGroupMappingsResponse](../../models/rbacservicemigrateallscimgroupmappingsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## revoke_object_access

RevokeObjectAccess

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_RevokeObjectAccess" method="post" path="/textql.rpc.public.rbac.RBACService/RevokeObjectAccess" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.rbac_services.revoke_object_access()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `object_type`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `object_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `member_id`                                                         | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `role_id`                                                           | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `group_id`                                                          | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RBACServiceRevokeObjectAccessResponse](../../models/rbacservicerevokeobjectaccessresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |