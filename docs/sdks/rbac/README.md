# Rbac

## Overview

### Available Operations

* [assign_permission_to_role](#assign_permission_to_role) - AssignPermissionToRole
* [assign_role_to_member](#assign_role_to_member) - Member role assignment
* [create_api_key](#create_api_key) - Group management. Internal only.
* [create_role](#create_role) - Role management
* [create_service_account](#create_service_account) - CreateServiceAccount
* [delete_role](#delete_role) - DeleteRole
* [delete_service_account](#delete_service_account) - DeleteServiceAccount
* [get_current_member_roles_and_permissions](#get_current_member_roles_and_permissions) - Get current member roles and permissions
* [get_embed_user_api_key](#get_embed_user_api_key) - GetEmbedUserApiKey
* [get_member_roles](#get_member_roles) - GetMemberRoles
* [get_role](#get_role) - GetRole
* [get_role_permissions](#get_role_permissions) - GetRolePermissions
* [list_api_keys](#list_api_keys) - ListApiKeys
* [list_permissions](#list_permissions) - Permission management
* [list_roles](#list_roles) - ListRoles
* [list_service_accounts](#list_service_accounts) - ListServiceAccounts
* [remove_permission_from_role](#remove_permission_from_role) - RemovePermissionFromRole
* [remove_role_from_member](#remove_role_from_member) - RemoveRoleFromMember
* [revoke_api_key](#revoke_api_key) - RevokeApiKey
* [rotate_api_key](#rotate_api_key) - RotateApiKey
* [update_role](#update_role) - UpdateRole

## assign_permission_to_role

AssignPermissionToRole

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_AssignPermissionToRole" method="post" path="/textql.rpc.public.rbac.RBACService/AssignPermissionToRole" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.assign_permission_to_role()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `role_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `permission_id`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RBACServiceAssignPermissionToRoleResponse](../../models/rbacserviceassignpermissiontoroleresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## assign_role_to_member

Member role assignment

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_AssignRoleToMember" method="post" path="/textql.rpc.public.rbac.RBACService/AssignRoleToMember" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.assign_role_to_member()

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

## create_api_key

Group management. Internal only.

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_CreateApiKey" method="post" path="/textql.rpc.public.rbac.RBACService/CreateApiKey" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.create_api_key()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `expiry_seconds`                                                    | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `assumed_roles`                                                     | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `inherit_all_roles`                                                 | *OptionalNullable[bool]*                                            | :heavy_minus_sign:                                                  | N/A                                                                 |
| `name`                                                              | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `target_member_id`                                                  | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `client_id`                                                         | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `suppress_superadmin`                                               | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RBACServiceCreateAPIKeyResponse](../../models/rbacservicecreateapikeyresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## create_role

Role management

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_CreateRole" method="post" path="/textql.rpc.public.rbac.RBACService/CreateRole" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.create_role()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `name`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `description`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RBACServiceCreateRoleResponse](../../models/rbacservicecreateroleresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## create_service_account

CreateServiceAccount

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_CreateServiceAccount" method="post" path="/textql.rpc.public.rbac.RBACService/CreateServiceAccount" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.create_service_account()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `name`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `description`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `owner_member_id`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `role_ids`                                                          | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RBACServiceCreateServiceAccountResponse](../../models/rbacservicecreateserviceaccountresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete_role

DeleteRole

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_DeleteRole" method="post" path="/textql.rpc.public.rbac.RBACService/DeleteRole" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.delete_role()

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

**[models.RBACServiceDeleteRoleResponse](../../models/rbacservicedeleteroleresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete_service_account

DeleteServiceAccount

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_DeleteServiceAccount" method="post" path="/textql.rpc.public.rbac.RBACService/DeleteServiceAccount" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.delete_service_account()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `member_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RBACServiceDeleteServiceAccountResponse](../../models/rbacservicedeleteserviceaccountresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_current_member_roles_and_permissions

Get current member roles and permissions

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_GetCurrentMemberRolesAndPermissions" method="post" path="/textql.rpc.public.rbac.RBACService/GetCurrentMemberRolesAndPermissions" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.get_current_member_roles_and_permissions(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                             | Type                                                                                                                                                  | Required                                                                                                                                              | Description                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                                                | [models.TextqlRPCPublicRbacGetCurrentMemberRolesAndPermissionsRequest](../../models/textqlrpcpublicrbacgetcurrentmemberrolesandpermissionsrequest.md) | :heavy_check_mark:                                                                                                                                    | N/A                                                                                                                                                   |
| `connect_timeout_ms`                                                                                                                                  | *Optional[float]*                                                                                                                                     | :heavy_minus_sign:                                                                                                                                    | N/A                                                                                                                                                   |
| `retries`                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                      | :heavy_minus_sign:                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                   |

### Response

**[models.RBACServiceGetCurrentMemberRolesAndPermissionsResponse](../../models/rbacservicegetcurrentmemberrolesandpermissionsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_embed_user_api_key

GetEmbedUserApiKey

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_GetEmbedUserApiKey" method="post" path="/textql.rpc.public.rbac.RBACService/GetEmbedUserApiKey" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.get_embed_user_api_key()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `member_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RBACServiceGetEmbedUserAPIKeyResponse](../../models/rbacservicegetembeduserapikeyresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_member_roles

GetMemberRoles

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_GetMemberRoles" method="post" path="/textql.rpc.public.rbac.RBACService/GetMemberRoles" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.get_member_roles()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `member_ids`                                                        | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RBACServiceGetMemberRolesResponse](../../models/rbacservicegetmemberrolesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_role

GetRole

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_GetRole" method="post" path="/textql.rpc.public.rbac.RBACService/GetRole" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.get_role()

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

## get_role_permissions

GetRolePermissions

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_GetRolePermissions" method="post" path="/textql.rpc.public.rbac.RBACService/GetRolePermissions" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.get_role_permissions()

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

## list_api_keys

ListApiKeys

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_ListApiKeys" method="post" path="/textql.rpc.public.rbac.RBACService/ListApiKeys" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.list_api_keys()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                      | *Optional[float]*                                                                                         | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `scope`                                                                                                   | [Optional[models.TextqlRPCPublicRbacAPIKeyScope]](../../models/textqlrpcpublicrbacapikeyscope.md)         | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `service_account_member_id`                                                                               | *OptionalNullable[str]*                                                                                   | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `include_revoked`                                                                                         | *OptionalNullable[bool]*                                                                                  | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `search_term`                                                                                             | *OptionalNullable[str]*                                                                                   | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `sort_by`                                                                                                 | [Optional[models.TextqlRPCPublicRbacAPIKeySortField]](../../models/textqlrpcpublicrbacapikeysortfield.md) | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `sort_direction`                                                                                          | [Optional[models.TextqlRPCPublicCommonSortDirection]](../../models/textqlrpcpubliccommonsortdirection.md) | :heavy_minus_sign:                                                                                        | Common enum for sort direction used across multiple services                                              |
| `page_size`                                                                                               | *OptionalNullable[int]*                                                                                   | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `page_token`                                                                                              | *OptionalNullable[str]*                                                                                   | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.RBACServiceListAPIKeysResponse](../../models/rbacservicelistapikeysresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_permissions

Permission management

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_ListPermissions" method="post" path="/textql.rpc.public.rbac.RBACService/ListPermissions" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.list_permissions(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                        | [models.TextqlRPCPublicRbacListPermissionsRequest](../../models/textqlrpcpublicrbaclistpermissionsrequest.md) | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `connect_timeout_ms`                                                                                          | *Optional[float]*                                                                                             | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.RBACServiceListPermissionsResponse](../../models/rbacservicelistpermissionsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_roles

ListRoles

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_ListRoles" method="post" path="/textql.rpc.public.rbac.RBACService/ListRoles" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.list_roles(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `body`                                                                                            | [models.TextqlRPCPublicRbacListRolesRequest](../../models/textqlrpcpublicrbaclistrolesrequest.md) | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `connect_timeout_ms`                                                                              | *Optional[float]*                                                                                 | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.RBACServiceListRolesResponse](../../models/rbacservicelistrolesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_service_accounts

ListServiceAccounts

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_ListServiceAccounts" method="post" path="/textql.rpc.public.rbac.RBACService/ListServiceAccounts" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.list_service_accounts()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `search_term`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page_size`                                                         | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | owner, editor, viewer                                               |
| `page_token`                                                        | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RBACServiceListServiceAccountsResponse](../../models/rbacservicelistserviceaccountsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## remove_permission_from_role

RemovePermissionFromRole

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_RemovePermissionFromRole" method="post" path="/textql.rpc.public.rbac.RBACService/RemovePermissionFromRole" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.remove_permission_from_role()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `role_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `permission_id`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RBACServiceRemovePermissionFromRoleResponse](../../models/rbacserviceremovepermissionfromroleresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## remove_role_from_member

RemoveRoleFromMember

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_RemoveRoleFromMember" method="post" path="/textql.rpc.public.rbac.RBACService/RemoveRoleFromMember" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.remove_role_from_member()

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

**[models.RBACServiceRemoveRoleFromMemberResponse](../../models/rbacserviceremoverolefrommemberresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## revoke_api_key

RevokeApiKey

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_RevokeApiKey" method="post" path="/textql.rpc.public.rbac.RBACService/RevokeApiKey" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.revoke_api_key()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `api_key_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RBACServiceRevokeAPIKeyResponse](../../models/rbacservicerevokeapikeyresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## rotate_api_key

RotateApiKey

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_RotateApiKey" method="post" path="/textql.rpc.public.rbac.RBACService/RotateApiKey" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.rotate_api_key()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `api_key_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RBACServiceRotateAPIKeyResponse](../../models/rbacservicerotateapikeyresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## update_role

UpdateRole

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_UpdateRole" method="post" path="/textql.rpc.public.rbac.RBACService/UpdateRole" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.update_role()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                 | Type                                                                                                                                                                                                      | Required                                                                                                                                                                                                  | Description                                                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                                                                      | *Optional[float]*                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `role_id`                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `name`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `description`                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `default_model_id`                                                                                                                                                                                        | *Optional[float]*                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `int32`.<br/><br/> The JSON representation for `Int32Value` is JSON number.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `allowed_model_ids`                                                                                                                                                                                       | List[*int*]                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `allow_model_choice`                                                                                                                                                                                      | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `clear_allowed_model_ids`                                                                                                                                                                                 | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `retries`                                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                                       |

### Response

**[models.RBACServiceUpdateRoleResponse](../../models/rbacserviceupdateroleresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |