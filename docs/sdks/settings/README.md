# Settings

## Overview

### Available Operations

* [check_member_status](#check_member_status) - CheckMemberStatus
* [delete_member](#delete_member) - DeleteOrganizationMember
* [get](#get) - GetOrganizationSettings
* [invite_member](#invite_member) - InviteOrganizationMember
* [list_members](#list_members) - ListOrganizationMembers
* [update_models](#update_models) - UpdateOrganizationModelSettings
* [update](#update) - UpdateOrganizationSettings

## check_member_status

CheckMemberStatus

### Example Usage

<!-- UsageSnippet language="python" operationID="SettingsService_CheckMemberStatus" method="post" path="/textql.rpc.public.settings.SettingsService/CheckMemberStatus" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.settings.check_member_status()

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

## delete_member

DeleteOrganizationMember

### Example Usage

<!-- UsageSnippet language="python" operationID="SettingsService_DeleteOrganizationMember" method="post" path="/textql.rpc.public.settings.SettingsService/DeleteOrganizationMember" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.settings.delete_member()

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

## get

GetOrganizationSettings

### Example Usage

<!-- UsageSnippet language="python" operationID="SettingsService_GetOrganizationSettings" method="post" path="/textql.rpc.public.settings.SettingsService/GetOrganizationSettings" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.settings.get(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                             | Type                                                                                                                                  | Required                                                                                                                              | Description                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                                | [models.TextqlRPCPublicSettingsGetOrganizationSettingsRequest](../../models/textqlrpcpublicsettingsgetorganizationsettingsrequest.md) | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `connect_timeout_ms`                                                                                                                  | *Optional[float]*                                                                                                                     | :heavy_minus_sign:                                                                                                                    | N/A                                                                                                                                   |
| `retries`                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                      | :heavy_minus_sign:                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                   |

### Response

**[models.SettingsServiceGetOrganizationSettingsResponse](../../models/settingsservicegetorganizationsettingsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## invite_member

InviteOrganizationMember

### Example Usage

<!-- UsageSnippet language="python" operationID="SettingsService_InviteOrganizationMember" method="post" path="/textql.rpc.public.settings.SettingsService/InviteOrganizationMember" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.settings.invite_member()

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

## list_members

ListOrganizationMembers

### Example Usage

<!-- UsageSnippet language="python" operationID="SettingsService_ListOrganizationMembers" method="post" path="/textql.rpc.public.settings.SettingsService/ListOrganizationMembers" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.settings.list_members()

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

## update_models

UpdateOrganizationModelSettings

### Example Usage

<!-- UsageSnippet language="python" operationID="SettingsService_UpdateOrganizationModelSettings" method="post" path="/textql.rpc.public.settings.SettingsService/UpdateOrganizationModelSettings" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.settings.update_models()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                        | *Optional[float]*                                                                           | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `default_model`                                                                             | [Optional[models.TextqlRPCPublicChatLlmModel]](../../models/textqlrpcpublicchatllmmodel.md) | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `enabled_models`                                                                            | List[[models.TextqlRPCPublicChatLlmModel](../../models/textqlrpcpublicchatllmmodel.md)]     | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `clear_enabled_models`                                                                      | *Optional[bool]*                                                                            | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `restricted_models`                                                                         | List[[models.TextqlRPCPublicChatLlmModel](../../models/textqlrpcpublicchatllmmodel.md)]     | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `clear_restricted_models`                                                                   | *Optional[bool]*                                                                            | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `restricted_families`                                                                       | List[*str*]                                                                                 | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `clear_restricted_families`                                                                 | *Optional[bool]*                                                                            | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.SettingsServiceUpdateOrganizationModelSettingsResponse](../../models/settingsserviceupdateorganizationmodelsettingsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## update

UpdateOrganizationSettings

### Example Usage

<!-- UsageSnippet language="python" operationID="SettingsService_UpdateOrganizationSettings" method="post" path="/textql.rpc.public.settings.SettingsService/UpdateOrganizationSettings" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.settings.update()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                 | Type                                                                                                                                                                                                      | Required                                                                                                                                                                                                  | Description                                                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                                                                      | *Optional[float]*                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `org_id`                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `secrets_enabled`                                                                                                                                                                                         | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `hide_example_connectors`                                                                                                                                                                                 | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `paradigm_params`                                                                                                                                                                                         | [Optional[models.TextqlRPCParadigmParamsParadigmParams]](../../models/textqlrpcparadigmparamsparadigmparams.md)                                                                                           | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `default_paradigm_mode`                                                                                                                                                                                   | [Optional[models.TextqlRPCParadigmParamsParadigmType]](../../models/textqlrpcparadigmparamsparadigmtype.md)                                                                                               | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `default_connector_ids`                                                                                                                                                                                   | List[*int*]                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `training_mode`                                                                                                                                                                                           | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `dashboards_enabled`                                                                                                                                                                                      | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `methodology_enabled`                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `feed_enabled`                                                                                                                                                                                            | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `context_v3_enabled`                                                                                                                                                                                      | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `clear_enabled_model_ids`                                                                                                                                                                                 | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `clear_restricted_model_ids`                                                                                                                                                                              | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `enabled_models`                                                                                                                                                                                          | List[[models.TextqlRPCPublicChatLlmModel](../../models/textqlrpcpublicchatllmmodel.md)]                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `restricted_models`                                                                                                                                                                                       | List[[models.TextqlRPCPublicChatLlmModel](../../models/textqlrpcpublicchatllmmodel.md)]                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `default_model`                                                                                                                                                                                           | [Optional[models.TextqlRPCPublicChatLlmModel]](../../models/textqlrpcpublicchatllmmodel.md)                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `observability_enabled`                                                                                                                                                                                   | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `notifications_enabled`                                                                                                                                                                                   | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `hide_api_connectors`                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `fast_mode_enabled`                                                                                                                                                                                       | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `max_thinking_enabled`                                                                                                                                                                                    | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `clear_default_connector_ids`                                                                                                                                                                             | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `default_dashboard_output`                                                                                                                                                                                | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `default_methodology`                                                                                                                                                                                     | [Optional[models.TextqlRPCPublicChatMethodology]](../../models/textqlrpcpublicchatmethodology.md)                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `traces_enabled`                                                                                                                                                                                          | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `sandbox_observability_enabled`                                                                                                                                                                           | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `data_apps_enabled`                                                                                                                                                                                       | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `issues_enabled`                                                                                                                                                                                          | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `spend_transparency_enabled`                                                                                                                                                                              | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `sharing_disabled`                                                                                                                                                                                        | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `tool_restrictions`                                                                                                                                                                                       | [Optional[models.TextqlRPCParadigmParamsParadigmParams]](../../models/textqlrpcparadigmparamsparadigmparams.md)                                                                                           | :heavy_minus_sign:                                                                                                                                                                                        | N/A                                                                                                                                                                                                       |
| `subagents_enabled`                                                                                                                                                                                       | *Optional[bool]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Wrapper message for `bool`.<br/><br/> The JSON representation for `BoolValue` is JSON `true` and `false`.<br/><br/> Not recommended for use in new APIs, but still useful for legacy APIs and<br/> has no plan to be removed. |
| `retries`                                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                                       |

### Response

**[models.SettingsServiceUpdateOrganizationSettingsResponse](../../models/settingsserviceupdateorganizationsettingsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |