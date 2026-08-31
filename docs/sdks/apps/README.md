# Apps

## Overview

### Available Operations

* [heartbeat](#heartbeat) - AppHeartbeat
* [create_app](#create_app) - CreateApp
* [delete_app](#delete_app) - DeleteApp
* [duplicate](#duplicate) - Duplicates an app the caller can view into a new app they own,  named "Copy of <name>". Copies code/files/data sources/compute functions/  schedule; never carries over the source's data snapshot.
* [get](#get) - GetApp
* [get_db_schema](#get_db_schema) - Replaces the calling member's entire ordering; capped server-side.
* [get_db_table_preview](#get_db_table_preview) - View analytics: reads the engagement views recorded on app page load.
* [get_member_state](#get_member_state) - Per-member notification subscription to an app ("watch this app").
* [get_app_version](#get_app_version) - Overwrites the published tree's pinned _runtime/ana-1.js with the platform's current copy so host-driven affordances (comment hit-testing) work on older documents; never touches authored content or data. repinned=false for legacy pre-tree documents.
* [get_app_view_stats](#get_app_view_stats) - Keeps the viewed app's compute worker alive; first view spawns and pre-warms it (dashboard viewer-TTL parity).
* [get_members_with_apps](#get_members_with_apps) - GetMembersWithApps
* [invoke_compute_function](#invoke_compute_function) - InvokeAppComputeFunction
* [list_activity_since](#list_activity_since) - Favorite/unfavorite a library item (app or dashboard) for the calling member.  Per-member, per-org; favorited=false hard-deletes the row. Covers both primitives  since the merged library page pins apps and dashboards through one client.
* [list_versions](#list_versions) - Renders the live artifact in the production sandbox and returns browser diagnostics.  This is synchronous so callers can verify an app before sharing its URL.
* [list](#list) - ListApps
* [list_my_member_activity](#list_my_member_activity) - Watcher management: app owners/editors and org admins list the app's  subscribers and add/remove members (Upsert/Delete with member_id).
* [move_app_to_folder](#move_app_to_folder) - MoveAppToFolder
* [presence_heartbeat](#presence_heartbeat) - Ordering overlay for the sidebar Bookmarks section: one position list per  member covering favorites and thread bookmarks ('<kind>:<id>' keys).  Membership truth stays in library_favorite / chat bookmarks; this persists  only the drag-and-drop order.
* [record_member_activity](#record_member_activity) - RecordAppMemberActivity
* [refresh](#refresh) - Moves an app into a library folder (or to root when folder_id is empty).
* [restore_app_version](#restore_app_version) - Version history: git-backed, one version per save (plus legacy publish-era snapshots); authors can list and restore.
* [set_member_state](#set_member_state) - SetAppMemberState
* [set_favorite](#set_favorite) - Executes a declared compute function on a pooled sandbox worker; gated, org-scoped, rate-limited.
* [update](#update) - UpdateApp
* [verify_render](#verify_render) - Re-fetches data sources, rebuilds the document with a fresh snapshot, re-uploads.

## heartbeat

AppHeartbeat

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_AppHeartbeat" method="post" path="/textql.rpc.public.app.AppService/AppHeartbeat" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.apps.heartbeat()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | the resolved default after the change; unset when cleared           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceAppHeartbeatResponse](../../models/appserviceappheartbeatresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## create_app

CreateApp

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_CreateApp" method="post" path="/textql.rpc.public.app.AppService/CreateApp" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.apps.create_app()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                  | *Optional[float]*                                                                                     | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `name`                                                                                                | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `description`                                                                                         | *OptionalNullable[str]*                                                                               | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `code`                                                                                                | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `data_sources`                                                                                        | List[[models.TextqlRPCPublicDashboardDataSource](../../models/textqlrpcpublicdashboarddatasource.md)] | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `compute_functions`                                                                                   | List[[models.TextqlRPCPublicAppComputeFunction](../../models/textqlrpcpublicappcomputefunction.md)]   | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `files`                                                                                               | List[[models.TextqlRPCPublicAppAppFile](../../models/textqlrpcpublicappappfile.md)]                   | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `capabilities`                                                                                        | List[[models.TextqlRPCPublicAppCapability](../../models/textqlrpcpublicappcapability.md)]             | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `app_db_setup`                                                                                        | List[*str*]                                                                                           | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.AppServiceCreateAppResponse](../../models/appservicecreateappresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete_app

DeleteApp

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_DeleteApp" method="post" path="/textql.rpc.public.app.AppService/DeleteApp" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.apps.delete_app()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | full replacement for the calling member                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceDeleteAppResponse](../../models/appservicedeleteappresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## duplicate

Duplicates an app the caller can view into a new app they own,
 named "Copy of <name>". Copies code/files/data sources/compute functions/
 schedule; never carries over the source's data snapshot.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_DuplicateApp" method="post" path="/textql.rpc.public.app.AppService/DuplicateApp" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.apps.duplicate()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceDuplicateAppResponse](../../models/appserviceduplicateappresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get

GetApp

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_GetApp" method="post" path="/textql.rpc.public.app.AppService/GetApp" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.apps.get()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | signed /asset/apptree viewer URL for the published gallery tree     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceGetAppResponse](../../models/appservicegetappresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_db_schema

Replaces the calling member's entire ordering; capped server-side.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_GetAppDBSchema" method="post" path="/textql.rpc.public.app.AppService/GetAppDBSchema" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.apps.get_db_schema()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceGetAppDBSchemaResponse](../../models/appservicegetappdbschemaresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_db_table_preview

View analytics: reads the engagement views recorded on app page load.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_GetAppDBTablePreview" method="post" path="/textql.rpc.public.app.AppService/GetAppDBTablePreview" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.apps.get_db_table_preview()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | normalized relative path, forward slashes, no .. or leading /       |
| `table_name`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceGetAppDBTablePreviewResponse](../../models/appservicegetappdbtablepreviewresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_member_state

Per-member notification subscription to an app ("watch this app").

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_GetAppMemberState" method="post" path="/textql.rpc.public.app.AppService/GetAppMemberState" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.apps.get_member_state()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceGetAppMemberStateResponse](../../models/appservicegetappmemberstateresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_app_version

Overwrites the published tree's pinned _runtime/ana-1.js with the platform's current copy so host-driven affordances (comment hit-testing) work on older documents; never touches authored content or data. repinned=false for legacy pre-tree documents.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_GetAppVersion" method="post" path="/textql.rpc.public.app.AppService/GetAppVersion" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.apps.get_app_version()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                              | *Optional[float]*                                                                 | :heavy_minus_sign:                                                                | N/A                                                                               |
| `app_id`                                                                          | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | False when the document predates tree publishing and has no runtime to overwrite. |
| `version_number`                                                                  | *Optional[int]*                                                                   | :heavy_minus_sign:                                                                | N/A                                                                               |
| `commit_id`                                                                       | *OptionalNullable[str]*                                                           | :heavy_minus_sign:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.AppServiceGetAppVersionResponse](../../models/appservicegetappversionresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_app_view_stats

Keeps the viewed app's compute worker alive; first view spawns and pre-warms it (dashboard viewer-TTL parity).

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_GetAppViewStats" method="post" path="/textql.rpc.public.app.AppService/GetAppViewStats" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.apps.get_app_view_stats()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceGetAppViewStatsResponse](../../models/appservicegetappviewstatsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_members_with_apps

GetMembersWithApps

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_GetMembersWithApps" method="post" path="/textql.rpc.public.app.AppService/GetMembersWithApps" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.apps.get_members_with_apps(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                            | [models.TextqlRPCPublicAppGetMembersWithAppsRequest](../../models/textqlrpcpublicappgetmemberswithappsrequest.md) | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `connect_timeout_ms`                                                                                              | *Optional[float]*                                                                                                 | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[models.AppServiceGetMembersWithAppsResponse](../../models/appservicegetmemberswithappsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## invoke_compute_function

InvokeAppComputeFunction

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_InvokeAppComputeFunction" method="post" path="/textql.rpc.public.app.AppService/InvokeAppComputeFunction" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.apps.invoke_compute_function()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `function_name`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `params_json`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceInvokeAppComputeFunctionResponse](../../models/appserviceinvokeappcomputefunctionresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_activity_since

Favorite/unfavorite a library item (app or dashboard) for the calling member.
 Per-member, per-org; favorited=false hard-deletes the row. Covers both primitives
 since the merged library page pins apps and dashboards through one client.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_ListAppActivitySince" method="post" path="/textql.rpc.public.app.AppService/ListAppActivitySince" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.apps.list_activity_since()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `scope`                                                             | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `after_seq`                                                         | [Optional[models.AfterSeq]](../../models/afterseq.md)               | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | server clamps to 200; <=0 means default                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceListAppActivitySinceResponse](../../models/appservicelistappactivitysinceresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_versions

Renders the live artifact in the production sandbox and returns browser diagnostics.
 This is synchronous so callers can verify an app before sharing its URL.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_ListAppVersions" method="post" path="/textql.rpc.public.app.AppService/ListAppVersions" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.apps.list_versions()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceListAppVersionsResponse](../../models/appservicelistappversionsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list

ListApps

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_ListApps" method="post" path="/textql.rpc.public.app.AppService/ListApps" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.apps.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `search_term`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `folder_id`                                                         | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `uncategorized_only`                                                | *OptionalNullable[bool]*                                            | :heavy_minus_sign:                                                  | N/A                                                                 |
| `shared_with_me`                                                    | *OptionalNullable[bool]*                                            | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceListAppsResponse](../../models/appservicelistappsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_my_member_activity

Watcher management: app owners/editors and org admins list the app's
 subscribers and add/remove members (Upsert/Delete with member_id).

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_ListMyAppMemberActivity" method="post" path="/textql.rpc.public.app.AppService/ListMyAppMemberActivity" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.apps.list_my_member_activity()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `type`                                                              | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | server clamps to 200; <=0 means default                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceListMyAppMemberActivityResponse](../../models/appservicelistmyappmemberactivityresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## move_app_to_folder

MoveAppToFolder

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_MoveAppToFolder" method="post" path="/textql.rpc.public.app.AppService/MoveAppToFolder" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.apps.move_app_to_folder()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `folder_id`                                                         | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceMoveAppToFolderResponse](../../models/appservicemoveapptofolderresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## presence_heartbeat

Ordering overlay for the sidebar Bookmarks section: one position list per
 member covering favorites and thread bookmarks ('<kind>:<id>' keys).
 Membership truth stays in library_favorite / chat bookmarks; this persists
 only the drag-and-drop order.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_PresenceHeartbeat" method="post" path="/textql.rpc.public.app.AppService/PresenceHeartbeat" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.apps.presence_heartbeat()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `zone`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServicePresenceHeartbeatResponse](../../models/appservicepresenceheartbeatresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## record_member_activity

RecordAppMemberActivity

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_RecordAppMemberActivity" method="post" path="/textql.rpc.public.app.AppService/RecordAppMemberActivity" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.apps.record_member_activity()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `type`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `scope`                                                             | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `payload_json`                                                      | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | JSON object, usage payload authored by the app                      |
| `idem_key`                                                          | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | duplicate key returns the existing row, not an error                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceRecordAppMemberActivityResponse](../../models/appservicerecordappmemberactivityresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## refresh

Moves an app into a library folder (or to root when folder_id is empty).

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_RefreshApp" method="post" path="/textql.rpc.public.app.AppService/RefreshApp" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.apps.refresh()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceRefreshAppResponse](../../models/appservicerefreshappresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## restore_app_version

Version history: git-backed, one version per save (plus legacy publish-era snapshots); authors can list and restore.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_RestoreAppVersion" method="post" path="/textql.rpc.public.app.AppService/RestoreAppVersion" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.apps.restore_app_version()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `version_number`                                                    | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `commit_id`                                                         | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceRestoreAppVersionResponse](../../models/appservicerestoreappversionresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## set_member_state

SetAppMemberState

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_SetAppMemberState" method="post" path="/textql.rpc.public.app.AppService/SetAppMemberState" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.apps.set_member_state()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `value_json`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | whole-object JSON, last-write-wins, max 64KB                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceSetAppMemberStateResponse](../../models/appservicesetappmemberstateresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## set_favorite

Executes a declared compute function on a pooled sandbox worker; gated, org-scoped, rate-limited.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_SetFavorite" method="post" path="/textql.rpc.public.app.AppService/SetFavorite" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.apps.set_favorite()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `primitive_type`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `primitive_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `favorited`                                                         | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | "" = brand/default accent                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceSetFavoriteResponse](../../models/appservicesetfavoriteresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## update

UpdateApp

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_UpdateApp" method="post" path="/textql.rpc.public.app.AppService/UpdateApp" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.apps.update()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                    | *Optional[float]*                                                                                                       | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `app_id`                                                                                                                | *Optional[str]*                                                                                                         | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `name`                                                                                                                  | *OptionalNullable[str]*                                                                                                 | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `description`                                                                                                           | *OptionalNullable[str]*                                                                                                 | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `code`                                                                                                                  | *OptionalNullable[str]*                                                                                                 | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `data_sources`                                                                                                          | List[[models.TextqlRPCPublicDashboardDataSource](../../models/textqlrpcpublicdashboarddatasource.md)]                   | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `replace_data_sources`                                                                                                  | *OptionalNullable[bool]*                                                                                                | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `publish`                                                                                                               | *OptionalNullable[bool]*                                                                                                | :heavy_minus_sign:                                                                                                      | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible. |
| `staleness_window_seconds`                                                                                              | *OptionalNullable[int]*                                                                                                 | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `compute_functions`                                                                                                     | List[[models.TextqlRPCPublicAppComputeFunction](../../models/textqlrpcpublicappcomputefunction.md)]                     | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `replace_compute_functions`                                                                                             | *OptionalNullable[bool]*                                                                                                | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `files`                                                                                                                 | List[[models.TextqlRPCPublicAppAppFile](../../models/textqlrpcpublicappappfile.md)]                                     | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `replace_files`                                                                                                         | *OptionalNullable[bool]*                                                                                                | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `schedule_enabled`                                                                                                      | *OptionalNullable[bool]*                                                                                                | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `cron_string`                                                                                                           | *OptionalNullable[str]*                                                                                                 | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `capabilities`                                                                                                          | List[[models.TextqlRPCPublicAppCapability](../../models/textqlrpcpublicappcapability.md)]                               | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `replace_capabilities`                                                                                                  | *OptionalNullable[bool]*                                                                                                | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `app_db_setup`                                                                                                          | List[*str*]                                                                                                             | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `replace_app_db_setup`                                                                                                  | *OptionalNullable[bool]*                                                                                                | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |

### Response

**[models.AppServiceUpdateAppResponse](../../models/appserviceupdateappresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## verify_render

Re-fetches data sources, rebuilds the document with a fresh snapshot, re-uploads.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_VerifyAppRender" method="post" path="/textql.rpc.public.app.AppService/VerifyAppRender" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.apps.verify_render()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceVerifyAppRenderResponse](../../models/appserviceverifyapprenderresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |