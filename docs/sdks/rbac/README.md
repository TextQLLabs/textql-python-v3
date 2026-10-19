# Rbac

## Overview

### Available Operations

* [approve_access_request](#approve_access_request) - ApproveAccessRequest
* [assign_permission_to_role](#assign_permission_to_role) - AssignPermissionToRole
* [assign_role_to_member](#assign_role_to_member) - Member role assignment
* [create_api_key](#create_api_key) - API Key management
* [create_personal_api_key](#create_personal_api_key) - Create an API key owned by the calling member. Requires no permission.
* [create_role](#create_role) - Role management
* [create_import_upload](#create_import_upload) - CreateRolePermissionsUploadUrl
* [create_service_account](#create_service_account) - Service account management
* [create_service_account_api_key](#create_service_account_api_key) - Create an API key owned by a service account. Requires organization:write.
* [delete_role](#delete_role) - DeleteRole
* [delete_service_account](#delete_service_account) - DeleteServiceAccount
* [export_roles](#export_roles) - ExportRolePermissions
* [generate_share_link](#generate_share_link) - GenerateShareLink
* [get_current_member_roles_and_permissions](#get_current_member_roles_and_permissions) - Get current member roles and permissions
* [get_embed_user_api_key](#get_embed_user_api_key) - GetEmbedUserApiKey
* [get_member_roles](#get_member_roles) - GetMemberRoles
* [get_object_access](#get_object_access) - GetObjectAccess
* [get_role](#get_role) - GetRole
* [get_role_permissions](#get_role_permissions) - GetRolePermissions
* [has_object_access](#has_object_access) - HasObjectAccess
* [import_roles](#import_roles) - ImportRolePermissions
* [list_access_requests](#list_access_requests) - ListAccessRequests
* [list_api_keys](#list_api_keys) - ListApiKeys
* [list_permissions](#list_permissions) - Permission management
* [list_roles](#list_roles) - ListRoles
* [list_service_accounts](#list_service_accounts) - ListServiceAccounts
* [parse_role_import](#parse_role_import) - Parse a CSV or XLSX file into an editable draft without creating roles.  Unknown names and values are preserved for correction; import validates them.
* [reject_access_request](#reject_access_request) - RejectAccessRequest
* [remove_permission_from_role](#remove_permission_from_role) - RemovePermissionFromRole
* [remove_role_from_member](#remove_role_from_member) - RemoveRoleFromMember
* [request_access](#request_access) - Access request management
* [revoke_api_key](#revoke_api_key) - RevokeApiKey
* [revoke_object_access](#revoke_object_access) - RevokeObjectAccess
* [rotate_api_key](#rotate_api_key) - RotateApiKey
* [set_role_permissions](#set_role_permissions) - Bulk add/remove permissions on a role in one call, producing a single audit entry for the whole edit.
* [share_object](#share_object) - Object sharing and access control
* [share_object_with_role](#share_object_with_role) - ShareObjectWithRole
* [update_object_access](#update_object_access) - UpdateObjectAccess
* [update_object_visibility](#update_object_visibility) - UpdateObjectVisibility
* [update_role](#update_role) - UpdateRole
* [who_am_i](#who_am_i) - Describe what a key is allowed to do.

## approve_access_request

ApproveAccessRequest

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_ApproveAccessRequest" method="post" path="/textql.rpc.public.rbac.RBACService/ApproveAccessRequest" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.approve_access_request()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `request_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RBACServiceApproveAccessRequestResponse](../../models/rbacserviceapproveaccessrequestresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

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

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                    | *Optional[float]*                                                                                       | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `role_name`                                                                                             | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | Exact, case-sensitive role name, unique within the caller's organization.<br/> Supply role_name or role_id. |
| `permission`                                                                                            | [Optional[models.TextqlRPCPublicRbacPermissionSpec]](../../models/textqlrpcpublicrbacpermissionspec.md) | :heavy_minus_sign:                                                                                      | A single RBAC permission. Select a resource and one of its supported actions.                           |
| `role_id`                                                                                               | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | Existing role ID. Prefer role_name; if both are supplied they must match.                               |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

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

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                                         | *Optional[float]*                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `member_email`                                                                                                                                                               | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | Email within the caller's organization; case-insensitive, with outer whitespace ignored.<br/> Use instead of member_id; if both are supplied they must identify the same member. |
| `role_name`                                                                                                                                                                  | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | Exact, case-sensitive role name, unique within the caller's organization.<br/> Supply role_name or role_id.                                                                  |
| `member_id`                                                                                                                                                                  | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `role_id`                                                                                                                                                                    | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | Existing role ID. Prefer role_name; if both are supplied they must match.                                                                                                    |
| `retries`                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                             | :heavy_minus_sign:                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                          |

### Response

**[models.RBACServiceAssignRoleToMemberResponse](../../models/rbacserviceassignroletomemberresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## create_api_key

API Key management

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

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                | Type                                                                                                                                                                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                                                                                                                                                                                                                                                                     | *Optional[float]*                                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                       | N/A                                                                                                                                                                                                                                                                                                                                                                                                      |
| `target_member_email`                                                                                                                                                                                                                                                                                                                                                                                    | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                       | Email within the caller's organization; case-insensitive, with outer whitespace ignored.<br/> Use instead of target_member_id; if both are supplied they must identify the same member.                                                                                                                                                                                                                  |
| `assumed_role_names`                                                                                                                                                                                                                                                                                                                                                                                     | List[*str*]                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                       | Exact, case-sensitive role names in the caller's organization.<br/> Merged with legacy assumed_roles IDs and deduplicated. The existing<br/> member-role and calling API-key scope restrictions apply to both forms.                                                                                                                                                                                     |
| `expiry_seconds`                                                                                                                                                                                                                                                                                                                                                                                         | *OptionalNullable[int]*                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                       | N/A                                                                                                                                                                                                                                                                                                                                                                                                      |
| `assumed_roles`                                                                                                                                                                                                                                                                                                                                                                                          | List[*str*]                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                       | Role IDs (UUIDs) to scope the new API key to. The service validates that<br/> each ID exists in the caller's org. Non-admin callers may only specify<br/> roles they already hold; assumed-role API key callers may only specify<br/> a subset of their current assumed roles.<br/> Legacy role IDs. Prefer assumed_role_names.                                                                          |
| `inherit_all_roles`                                                                                                                                                                                                                                                                                                                                                                                      | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                       | When true, the API key inherits all of the creating member's roles<br/> (no assumed-role scoping). Callers must set this explicitly when<br/> both role lists are empty; otherwise the request is rejected to prevent<br/> accidentally creating over-privileged keys.                                                                                                                                   |
| `name`                                                                                                                                                                                                                                                                                                                                                                                                   | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                       | Optional display name for the API key.                                                                                                                                                                                                                                                                                                                                                                   |
| `target_member_id`                                                                                                                                                                                                                                                                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                       | Optional owner override for the new API key.<br/> If unset, the API key is created for the calling member.<br/> If set, the API key is created for this member ID (target principal):<br/> service-account targets require the caller to hold organization:write;<br/> human targets require api_access_key:delegate, and the key is bounded<br/> by the target member's roles with superadmin elevation always<br/> suppressed. |
| `client_id`                                                                                                                                                                                                                                                                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                       | Optional client metadata stored on the API key as client_id.<br/> Prefer a JSON object string when using structured client attributes.                                                                                                                                                                                                                                                                   |
| `suppress_superadmin`                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                       | When true, requests authenticated with this key skip the<br/> @textql.com-email superadmin elevation branch. Only meaningful<br/> when paired with assumed_roles so a textql admin can preview a<br/> role's experience without superadmin permissions bleeding through.                                                                                                                                 |
| `full_member_access`                                                                                                                                                                                                                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                       | N/A                                                                                                                                                                                                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                      |

### Response

**[models.RBACServiceCreateAPIKeyResponse](../../models/rbacservicecreateapikeyresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## create_personal_api_key

Create an API key owned by the calling member. Requires no permission.

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_CreatePersonalApiKey" method="post" path="/textql.rpc.public.rbac.RBACService/CreatePersonalApiKey" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.create_personal_api_key()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                    | Type                                                                                                                                                                                                         | Required                                                                                                                                                                                                     | Description                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `connect_timeout_ms`                                                                                                                                                                                         | *Optional[float]*                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                           | N/A                                                                                                                                                                                                          |
| `assumed_role_names`                                                                                                                                                                                         | List[*str*]                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                           | Exact, case-sensitive role names in the caller's organization.<br/> Merged with legacy assumed_roles IDs and deduplicated. The existing<br/> member-role and calling API-key scope restrictions apply to both forms. |
| `name`                                                                                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                           | N/A                                                                                                                                                                                                          |
| `expiry_seconds`                                                                                                                                                                                             | *OptionalNullable[int]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                           | N/A                                                                                                                                                                                                          |
| `assumed_roles`                                                                                                                                                                                              | List[*str*]                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                           | Bounded by the roles the caller holds.<br/> Legacy role IDs. Prefer assumed_role_names.                                                                                                                      |
| `inherit_all_roles`                                                                                                                                                                                          | *OptionalNullable[bool]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                           | Required when both role lists are empty, so omission cannot mint a wide key.                                                                                                                                 |
| `client_id`                                                                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                           | N/A                                                                                                                                                                                                          |
| `full_member_access`                                                                                                                                                                                         | *Optional[bool]*                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                           | Also reach the owner's own items; otherwise the key sees only what the<br/> assumed roles can see.                                                                                                           |
| `suppress_superadmin`                                                                                                                                                                                        | *Optional[bool]*                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                           | Drop @textql.com superadmin elevation. No-op for non-superadmins.                                                                                                                                            |
| `retries`                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                          |

### Response

**[models.RBACServiceCreatePersonalAPIKeyResponse](../../models/rbacservicecreatepersonalapikeyresponse.md)**

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
| `color`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `icon`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RBACServiceCreateRoleResponse](../../models/rbacservicecreateroleresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## create_import_upload

CreateRolePermissionsUploadUrl

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_CreateRolePermissionsUploadUrl" method="post" path="/textql.rpc.public.rbac.RBACService/CreateRolePermissionsUploadUrl" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.create_import_upload()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `file_name`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `size_bytes`                                                        | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RBACServiceCreateRolePermissionsUploadURLResponse](../../models/rbacservicecreaterolepermissionsuploadurlresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## create_service_account

Service account management

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

| Parameter                                                                                                                                                                          | Type                                                                                                                                                                               | Required                                                                                                                                                                           | Description                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                                               | *Optional[float]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                 | N/A                                                                                                                                                                                |
| `owner_member_email`                                                                                                                                                               | *OptionalNullable[str]*                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                 | Email within the caller's organization; case-insensitive, with outer whitespace ignored.<br/> Use instead of owner_member_id; if both are supplied they must identify the same member. |
| `name`                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                 | N/A                                                                                                                                                                                |
| `description`                                                                                                                                                                      | *OptionalNullable[str]*                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                 | N/A                                                                                                                                                                                |
| `owner_member_id`                                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                 | N/A                                                                                                                                                                                |
| `role_names`                                                                                                                                                                       | List[*str*]                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                 | Exact, case-sensitive role names in the caller's organization.<br/> Merged with legacy role_ids and deduplicated; bounded by caller authority.                                     |
| `role_ids`                                                                                                                                                                         | List[*str*]                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                 | Legacy role IDs. Prefer role_names.                                                                                                                                                |
| `retries`                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                |

### Response

**[models.RBACServiceCreateServiceAccountResponse](../../models/rbacservicecreateserviceaccountresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## create_service_account_api_key

Create an API key owned by a service account. Requires organization:write.

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_CreateServiceAccountApiKey" method="post" path="/textql.rpc.public.rbac.RBACService/CreateServiceAccountApiKey" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.create_service_account_api_key()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                    | Type                                                                                                                                                                                                         | Required                                                                                                                                                                                                     | Description                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `connect_timeout_ms`                                                                                                                                                                                         | *Optional[float]*                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                           | N/A                                                                                                                                                                                                          |
| `service_account_email`                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                           | Email within the caller's organization; case-insensitive, with outer whitespace ignored.<br/> Use instead of service_account_member_id; if both are supplied they must identify the same member.             |
| `assumed_role_names`                                                                                                                                                                                         | List[*str*]                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                           | Exact, case-sensitive role names in the caller's organization.<br/> Merged with legacy assumed_roles IDs and deduplicated. The existing<br/> member-role and calling API-key scope restrictions apply to both forms. |
| `service_account_member_id`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                           | N/A                                                                                                                                                                                                          |
| `name`                                                                                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                           | N/A                                                                                                                                                                                                          |
| `expiry_seconds`                                                                                                                                                                                             | *OptionalNullable[int]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                           | N/A                                                                                                                                                                                                          |
| `assumed_roles`                                                                                                                                                                                              | List[*str*]                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                           | Bounded by the service account's own roles; org admins get no bypass here.<br/> Legacy role IDs. Prefer assumed_role_names.                                                                                  |
| `inherit_all_roles`                                                                                                                                                                                          | *OptionalNullable[bool]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                           | Required when both role lists are empty, so omission cannot mint a wide key.                                                                                                                                 |
| `client_id`                                                                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                           | N/A                                                                                                                                                                                                          |
| `full_member_access`                                                                                                                                                                                         | *Optional[bool]*                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                           | Also reach the service account's own items.                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                          |

### Response

**[models.RBACServiceCreateServiceAccountAPIKeyResponse](../../models/rbacservicecreateserviceaccountapikeyresponse.md)**

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

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                    | *Optional[float]*                                                                                       | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `role_name`                                                                                             | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | Exact, case-sensitive role name, unique within the caller's organization.<br/> Supply role_name or role_id. |
| `role_id`                                                                                               | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | Existing role ID. Prefer role_name; if both are supplied they must match.                               |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

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

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                                         | *Optional[float]*                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `member_email`                                                                                                                                                               | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | Email within the caller's organization; case-insensitive, with outer whitespace ignored.<br/> Use instead of member_id; if both are supplied they must identify the same member. |
| `member_id`                                                                                                                                                                  | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `retries`                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                             | :heavy_minus_sign:                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                          |

### Response

**[models.RBACServiceDeleteServiceAccountResponse](../../models/rbacservicedeleteserviceaccountresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## export_roles

ExportRolePermissions

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_ExportRolePermissions" method="post" path="/textql.rpc.public.rbac.RBACService/ExportRolePermissions" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.export_roles()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                         | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                              | *Optional[float]*                                                                                                                 | :heavy_minus_sign:                                                                                                                | N/A                                                                                                                               |
| `format_`                                                                                                                         | [Optional[models.TextqlRPCPublicRbacRolePermissionsExportFormat]](../../models/textqlrpcpublicrbacrolepermissionsexportformat.md) | :heavy_minus_sign:                                                                                                                | N/A                                                                                                                               |
| `retries`                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                  | :heavy_minus_sign:                                                                                                                | Configuration to override the default retry behavior of the client.                                                               |

### Response

**[models.RBACServiceExportRolePermissionsResponse](../../models/rbacserviceexportrolepermissionsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## generate_share_link

GenerateShareLink

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_GenerateShareLink" method="post" path="/textql.rpc.public.rbac.RBACService/GenerateShareLink" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.generate_share_link()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `object_type`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `object_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RBACServiceGenerateShareLinkResponse](../../models/rbacservicegeneratesharelinkresponse.md)**

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

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                                         | *Optional[float]*                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `member_email`                                                                                                                                                               | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | Email within the caller's organization; case-insensitive, with outer whitespace ignored.<br/> Use instead of member_id; if both are supplied they must identify the same member. |
| `member_id`                                                                                                                                                                  | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `retries`                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                             | :heavy_minus_sign:                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                          |

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

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                             | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | N/A                                                                                                                                                              |
| `member_emails`                                                                                                                                                  | List[*str*]                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                               | Emails within the caller's organization; case-insensitive, with outer whitespace ignored.<br/> Merged with member_ids and deduplicated. Unknown emails are rejected. |
| `member_ids`                                                                                                                                                     | List[*str*]                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                               | N/A                                                                                                                                                              |
| `retries`                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                              |

### Response

**[models.RBACServiceGetMemberRolesResponse](../../models/rbacservicegetmemberrolesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_object_access

GetObjectAccess

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_GetObjectAccess" method="post" path="/textql.rpc.public.rbac.RBACService/GetObjectAccess" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.get_object_access()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `object_type`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `object_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RBACServiceGetObjectAccessResponse](../../models/rbacservicegetobjectaccessresponse.md)**

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

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                    | *Optional[float]*                                                                                       | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `role_name`                                                                                             | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | Exact, case-sensitive role name, unique within the caller's organization.<br/> Supply role_name or role_id. |
| `role_id`                                                                                               | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | Existing role ID. Prefer role_name; if both are supplied they must match.                               |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

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

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                    | *Optional[float]*                                                                                       | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `role_name`                                                                                             | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | Exact, case-sensitive role name, unique within the caller's organization.<br/> Supply role_name or role_id. |
| `role_id`                                                                                               | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | Existing role ID. Prefer role_name; if both are supplied they must match.                               |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.RBACServiceGetRolePermissionsResponse](../../models/rbacservicegetrolepermissionsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## has_object_access

HasObjectAccess

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_HasObjectAccess" method="post" path="/textql.rpc.public.rbac.RBACService/HasObjectAccess" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.has_object_access()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                                         | *Optional[float]*                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `member_email`                                                                                                                                                               | *OptionalNullable[str]*                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                           | Email within the caller's organization; case-insensitive, with outer whitespace ignored.<br/> Use instead of member_id; if both are supplied they must identify the same member. |
| `role_name`                                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                           | Exact, case-sensitive role name in the caller's organization.<br/> To target a role, supply role_name or role_id; if both are supplied they must match.                      |
| `object_type`                                                                                                                                                                | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `object_id`                                                                                                                                                                  | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `member_id`                                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `role_id`                                                                                                                                                                    | *OptionalNullable[str]*                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                           | Legacy role ID. Prefer role_name.                                                                                                                                            |
| `retries`                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                             | :heavy_minus_sign:                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                          |

### Response

**[models.RBACServiceHasObjectAccessResponse](../../models/rbacservicehasobjectaccessresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## import_roles

ImportRolePermissions

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_ImportRolePermissions" method="post" path="/textql.rpc.public.rbac.RBACService/ImportRolePermissions" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.import_roles()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                             | Type                                                                                                                                                  | Required                                                                                                                                              | Description                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                  | *Optional[float]*                                                                                                                                     | :heavy_minus_sign:                                                                                                                                    | N/A                                                                                                                                                   |
| `data`                                                                                                                                                | *Optional[str]*                                                                                                                                       | :heavy_minus_sign:                                                                                                                                    | Legacy CSV input. Prefer draft to approve an edited parsing response.<br/> Supply exactly one of data or draft. All values are validated before creation. |
| `draft`                                                                                                                                               | [Optional[models.TextqlRPCPublicRbacRolePermissionsImportDraft]](../../models/textqlrpcpublicrbacrolepermissionsimportdraft.md)                       | :heavy_minus_sign:                                                                                                                                    | N/A                                                                                                                                                   |
| `retries`                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                      | :heavy_minus_sign:                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                   |

### Response

**[models.RBACServiceImportRolePermissionsResponse](../../models/rbacserviceimportrolepermissionsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_access_requests

ListAccessRequests

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_ListAccessRequests" method="post" path="/textql.rpc.public.rbac.RBACService/ListAccessRequests" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.list_access_requests()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `object_type`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `object_id`                                                         | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `status`                                                            | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | pending, approved, rejected                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RBACServiceListAccessRequestsResponse](../../models/rbacservicelistaccessrequestsresponse.md)**

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

| Parameter                                                                                                                                                                                    | Type                                                                                                                                                                                         | Required                                                                                                                                                                                     | Description                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                                                         | *Optional[float]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                           | N/A                                                                                                                                                                                          |
| `service_account_email`                                                                                                                                                                      | *OptionalNullable[str]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                           | Email within the caller's organization; case-insensitive, with outer whitespace ignored.<br/> Use instead of service_account_member_id; if both are supplied they must identify the same member. |
| `scope`                                                                                                                                                                                      | [Optional[models.TextqlRPCPublicRbacAPIKeyScope]](../../models/textqlrpcpublicrbacapikeyscope.md)                                                                                            | :heavy_minus_sign:                                                                                                                                                                           | N/A                                                                                                                                                                                          |
| `service_account_member_id`                                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                           | N/A                                                                                                                                                                                          |
| `include_revoked`                                                                                                                                                                            | *OptionalNullable[bool]*                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                           | N/A                                                                                                                                                                                          |
| `search_term`                                                                                                                                                                                | *OptionalNullable[str]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                           | N/A                                                                                                                                                                                          |
| `sort_by`                                                                                                                                                                                    | [Optional[models.TextqlRPCPublicRbacAPIKeySortField]](../../models/textqlrpcpublicrbacapikeysortfield.md)                                                                                    | :heavy_minus_sign:                                                                                                                                                                           | N/A                                                                                                                                                                                          |
| `sort_direction`                                                                                                                                                                             | [Optional[models.TextqlRPCPublicCommonSortDirection]](../../models/textqlrpcpubliccommonsortdirection.md)                                                                                    | :heavy_minus_sign:                                                                                                                                                                           | Common enum for sort direction used across multiple services                                                                                                                                 |
| `page_size`                                                                                                                                                                                  | *OptionalNullable[int]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                           | N/A                                                                                                                                                                                          |
| `page_token`                                                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                           | N/A                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                          |

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
| `page_size`                                                         | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page_token`                                                        | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RBACServiceListServiceAccountsResponse](../../models/rbacservicelistserviceaccountsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## parse_role_import

Parse a CSV or XLSX file into an editable draft without creating roles.
 Unknown names and values are preserved for correction; import validates them.

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_ParseRolePermissionsImport" method="post" path="/textql.rpc.public.rbac.RBACService/ParseRolePermissionsImport" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.parse_role_import()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                      | *Optional[float]*                                                         | :heavy_minus_sign:                                                        | N/A                                                                       |
| `file_url`                                                                | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | Presigned download URL for a CSV or XLSX file, up to 1 MiB and 100 roles. |
| `file_key`                                                                | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.RBACServiceParseRolePermissionsImportResponse](../../models/rbacserviceparserolepermissionsimportresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## reject_access_request

RejectAccessRequest

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_RejectAccessRequest" method="post" path="/textql.rpc.public.rbac.RBACService/RejectAccessRequest" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.reject_access_request()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `request_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `rejection_reason`                                                  | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RBACServiceRejectAccessRequestResponse](../../models/rbacservicerejectaccessrequestresponse.md)**

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

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                    | *Optional[float]*                                                                                       | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `role_name`                                                                                             | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | Exact, case-sensitive role name, unique within the caller's organization.<br/> Supply role_name or role_id. |
| `permission`                                                                                            | [Optional[models.TextqlRPCPublicRbacPermissionSpec]](../../models/textqlrpcpublicrbacpermissionspec.md) | :heavy_minus_sign:                                                                                      | A single RBAC permission. Select a resource and one of its supported actions.                           |
| `role_id`                                                                                               | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | Existing role ID. Prefer role_name; if both are supplied they must match.                               |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

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

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                                         | *Optional[float]*                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `member_email`                                                                                                                                                               | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | Email within the caller's organization; case-insensitive, with outer whitespace ignored.<br/> Use instead of member_id; if both are supplied they must identify the same member. |
| `role_name`                                                                                                                                                                  | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | Exact, case-sensitive role name, unique within the caller's organization.<br/> Supply role_name or role_id.                                                                  |
| `member_id`                                                                                                                                                                  | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `role_id`                                                                                                                                                                    | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | Existing role ID. Prefer role_name; if both are supplied they must match.                                                                                                    |
| `retries`                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                             | :heavy_minus_sign:                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                          |

### Response

**[models.RBACServiceRemoveRoleFromMemberResponse](../../models/rbacserviceremoverolefrommemberresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## request_access

Access request management

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_RequestAccess" method="post" path="/textql.rpc.public.rbac.RBACService/RequestAccess" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.request_access()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `object_type`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `object_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `requested_access_type`                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | owner, editor, viewer                                               |
| `justification`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `request_message`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RBACServiceRequestAccessResponse](../../models/rbacservicerequestaccessresponse.md)**

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

## revoke_object_access

RevokeObjectAccess

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_RevokeObjectAccess" method="post" path="/textql.rpc.public.rbac.RBACService/RevokeObjectAccess" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.revoke_object_access()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                                         | *Optional[float]*                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `member_email`                                                                                                                                                               | *OptionalNullable[str]*                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                           | Email within the caller's organization; case-insensitive, with outer whitespace ignored.<br/> Use instead of member_id; if both are supplied they must identify the same member. |
| `role_name`                                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                           | Exact, case-sensitive role name in the caller's organization.<br/> To target a role, supply role_name or role_id; if both are supplied they must match.                      |
| `object_type`                                                                                                                                                                | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `object_id`                                                                                                                                                                  | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `member_id`                                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `role_id`                                                                                                                                                                    | *OptionalNullable[str]*                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                           | Legacy role ID. Prefer role_name.                                                                                                                                            |
| `retries`                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                             | :heavy_minus_sign:                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                          |

### Response

**[models.RBACServiceRevokeObjectAccessResponse](../../models/rbacservicerevokeobjectaccessresponse.md)**

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

## set_role_permissions

Bulk add/remove permissions on a role in one call, producing a single audit entry for the whole edit.

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_SetRolePermissions" method="post" path="/textql.rpc.public.rbac.RBACService/SetRolePermissions" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.set_role_permissions()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                            | *Optional[float]*                                                                                               | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `role_name`                                                                                                     | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | Exact, case-sensitive role name, unique within the caller's organization.<br/> Supply role_name or role_id.     |
| `add_permissions`                                                                                               | List[[models.TextqlRPCPublicRbacPermissionSpec](../../models/textqlrpcpublicrbacpermissionspec.md)]             | :heavy_minus_sign:                                                                                              | Permissions to add. Duplicates are ignored; a permission cannot be both<br/> added and removed in the same request. |
| `remove_permissions`                                                                                            | List[[models.TextqlRPCPublicRbacPermissionSpec](../../models/textqlrpcpublicrbacpermissionspec.md)]             | :heavy_minus_sign:                                                                                              | Permissions to remove.                                                                                          |
| `role_id`                                                                                                       | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | Existing role ID. Prefer role_name; if both are supplied they must match.                                       |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.RBACServiceSetRolePermissionsResponse](../../models/rbacservicesetrolepermissionsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## share_object

Object sharing and access control

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_ShareObject" method="post" path="/textql.rpc.public.rbac.RBACService/ShareObject" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.share_object()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                                         | *Optional[float]*                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `member_email`                                                                                                                                                               | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | Email within the caller's organization; case-insensitive, with outer whitespace ignored.<br/> Use instead of member_id; if both are supplied they must identify the same member. |
| `object_type`                                                                                                                                                                | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `object_id`                                                                                                                                                                  | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `member_id`                                                                                                                                                                  | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `access_type`                                                                                                                                                                | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | owner, editor, viewer                                                                                                                                                        |
| `is_public`                                                                                                                                                                  | *Optional[bool]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `retries`                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                             | :heavy_minus_sign:                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                          |

### Response

**[models.RBACServiceShareObjectResponse](../../models/rbacserviceshareobjectresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## share_object_with_role

ShareObjectWithRole

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_ShareObjectWithRole" method="post" path="/textql.rpc.public.rbac.RBACService/ShareObjectWithRole" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.share_object_with_role()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                         | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                              | *Optional[float]*                                                                                                                 | :heavy_minus_sign:                                                                                                                | N/A                                                                                                                               |
| `role_name`                                                                                                                       | *Optional[str]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | Exact, case-sensitive role name in the caller's organization.<br/> Supply role_name or role_id; if both are supplied they must match. |
| `object_type`                                                                                                                     | *Optional[str]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | N/A                                                                                                                               |
| `object_id`                                                                                                                       | *Optional[str]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | N/A                                                                                                                               |
| `role_id`                                                                                                                         | *Optional[str]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | Legacy role ID. Prefer role_name.                                                                                                 |
| `access_type`                                                                                                                     | *Optional[str]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | owner, editor, viewer                                                                                                             |
| `is_public`                                                                                                                       | *Optional[bool]*                                                                                                                  | :heavy_minus_sign:                                                                                                                | N/A                                                                                                                               |
| `retries`                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                  | :heavy_minus_sign:                                                                                                                | Configuration to override the default retry behavior of the client.                                                               |

### Response

**[models.RBACServiceShareObjectWithRoleResponse](../../models/rbacserviceshareobjectwithroleresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## update_object_access

UpdateObjectAccess

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_UpdateObjectAccess" method="post" path="/textql.rpc.public.rbac.RBACService/UpdateObjectAccess" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.update_object_access()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `access_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `access_type`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | owner, editor, viewer                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RBACServiceUpdateObjectAccessResponse](../../models/rbacserviceupdateobjectaccessresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## update_object_visibility

UpdateObjectVisibility

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_UpdateObjectVisibility" method="post" path="/textql.rpc.public.rbac.RBACService/UpdateObjectVisibility" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.update_object_visibility()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `object_type`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `object_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `is_public`                                                         | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RBACServiceUpdateObjectVisibilityResponse](../../models/rbacserviceupdateobjectvisibilityresponse.md)**

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
| `role_name`                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                        | Exact, case-sensitive role name, unique within the caller's organization.<br/> Supply role_name or role_id. For updates, name is the new name.                                                            |
| `name`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `description`                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `allowed_models`                                                                                                                                                                                          | List[[models.TextqlRPCPublicChatLlmModel](../../models/textqlrpcpublicchatllmmodel.md)]                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `default_model`                                                                                                                                                                                           | [Optional[models.TextqlRPCPublicChatLlmModel]](../../models/textqlrpcpublicchatllmmodel.md)                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `allow_model_choice`                                                                                                                                                                                      | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `clear_allowed_model_ids`                                                                                                                                                                                 | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Clears allowed_models back to "all models allowed". Needed because proto3<br/> cannot distinguish an empty repeated field from an absent one.                                                             |
| `color`                                                                                                                                                                                                   | *OptionalNullable[str]*                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                        | Omitted preserves the existing value; empty resets to the default.                                                                                                                                        |
| `icon`                                                                                                                                                                                                    | *OptionalNullable[str]*                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `role_id`                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                        | Existing role ID. Prefer role_name; if both are supplied they must match.                                                                                                                                 |
| `retries`                                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                                       |

### Response

**[models.RBACServiceUpdateRoleResponse](../../models/rbacserviceupdateroleresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## who_am_i

Describe what a key is allowed to do.

### Example Usage

<!-- UsageSnippet language="python" operationID="RBACService_WhoAmI" method="post" path="/textql.rpc.public.rbac.RBACService/WhoAmI" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.rbac.who_am_i(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `body`                                                                                      | [models.TextqlRPCPublicRbacWhoAmIRequest](../../models/textqlrpcpublicrbacwhoamirequest.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `connect_timeout_ms`                                                                        | *Optional[float]*                                                                           | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.RBACServiceWhoAmIResponse](../../models/rbacservicewhoamiresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |