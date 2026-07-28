# SettingsService

## Overview

### Available Operations

* [settings_service_check_member_status](#settings_service_check_member_status) - CheckMemberStatus
* [settings_service_delete_organization_member](#settings_service_delete_organization_member) - DeleteOrganizationMember
* [settings_service_invite_organization_member](#settings_service_invite_organization_member) - InviteOrganizationMember
* [settings_service_list_organization_members](#settings_service_list_organization_members) - ListOrganizationMembers
* [settings_service_update_organization_settings](#settings_service_update_organization_settings) - UpdateOrganizationSettings

## settings_service_check_member_status

CheckMemberStatus

### Example Usage

<!-- UsageSnippet language="python" operationID="SettingsService_CheckMemberStatus" method="post" path="/textql.rpc.public.settings.SettingsService/CheckMemberStatus" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.settings_service.settings_service_check_member_status()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `force_refresh`                                                     | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SettingsServiceCheckMemberStatusResponse](../../models/settingsservicecheckmemberstatusresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## settings_service_delete_organization_member

DeleteOrganizationMember

### Example Usage

<!-- UsageSnippet language="python" operationID="SettingsService_DeleteOrganizationMember" method="post" path="/textql.rpc.public.settings.SettingsService/DeleteOrganizationMember" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.settings_service.settings_service_delete_organization_member()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `org_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `member_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `hard_delete`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SettingsServiceDeleteOrganizationMemberResponse](../../models/settingsservicedeleteorganizationmemberresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## settings_service_invite_organization_member

InviteOrganizationMember

### Example Usage

<!-- UsageSnippet language="python" operationID="SettingsService_InviteOrganizationMember" method="post" path="/textql.rpc.public.settings.SettingsService/InviteOrganizationMember" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.settings_service.settings_service_invite_organization_member()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `org_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `email`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `role`                                                              | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SettingsServiceInviteOrganizationMemberResponse](../../models/settingsserviceinviteorganizationmemberresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## settings_service_list_organization_members

ListOrganizationMembers

### Example Usage

<!-- UsageSnippet language="python" operationID="SettingsService_ListOrganizationMembers" method="post" path="/textql.rpc.public.settings.SettingsService/ListOrganizationMembers" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.settings_service.settings_service_list_organization_members()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `org_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SettingsServiceListOrganizationMembersResponse](../../models/settingsservicelistorganizationmembersresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## settings_service_update_organization_settings

UpdateOrganizationSettings

### Example Usage

<!-- UsageSnippet language="python" operationID="SettingsService_UpdateOrganizationSettings" method="post" path="/textql.rpc.public.settings.SettingsService/UpdateOrganizationSettings" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.settings_service.settings_service_update_organization_settings()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                 | Type                                                                                                                                                                                                      | Required                                                                                                                                                                                                  | Description                                                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                                                                      | *Optional[float]*                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `org_id`                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `hide_example_connectors`                                                                                                                                                                                 | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `paradigm_params`                                                                                                                                                                                         | [Optional[models.TextqlRPCParadigmParamsParadigmParams]](../../models/textqlrpcparadigmparamsparadigmparams.md)                                                                                           | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `training_mode`                                                                                                                                                                                           | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `dashboards_enabled`                                                                                                                                                                                      | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `methodology_enabled`                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `feed_enabled`                                                                                                                                                                                            | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `observability_enabled`                                                                                                                                                                                   | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `notifications_enabled`                                                                                                                                                                                   | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `fast_mode_enabled`                                                                                                                                                                                       | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `max_thinking_enabled`                                                                                                                                                                                    | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `traces_enabled`                                                                                                                                                                                          | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `sandbox_observability_enabled`                                                                                                                                                                           | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `data_apps_enabled`                                                                                                                                                                                       | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `tool_restrictions`                                                                                                                                                                                       | [Optional[models.TextqlRPCParadigmParamsParadigmParams]](../../models/textqlrpcparadigmparamsparadigmparams.md)                                                                                           | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `subagents_enabled`                                                                                                                                                                                       | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `retries`                                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                                       |

### Response

**[models.SettingsServiceUpdateOrganizationSettingsResponse](../../models/settingsserviceupdateorganizationsettingsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |