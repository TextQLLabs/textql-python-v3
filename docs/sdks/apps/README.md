# Apps

## Overview

### Available Operations

* [heartbeat](#heartbeat) - Viewer heartbeat: keeps a warm compute worker alive while the app is open so its  billed lifetime tracks the view session (mirrors a dashboard's viewer TTL). No-op  when the app has no warm worker; never spawns one.
* [create_app](#create_app) - CreateApp
* [delete_app](#delete_app) - DeleteApp
* [duplicate](#duplicate) - Duplicates an app the caller can view into a new draft app they own,  named "Copy of <name>". Copies code/files/data sources/compute functions/  schedule; never carries over the source's published state or data snapshot.
* [get](#get) - GetApp
* [get_app_version](#get_app_version) - GetAppVersion
* [get_app_view_stats](#get_app_view_stats) - View analytics: reads the engagement views recorded on app page load.
* [get_component_gallery_url](#get_component_gallery_url) - Staff-only (superadmin gated in-handler): publishes the embedded component  gallery as an app tree and returns its signed viewer URL.
* [get_members_with_apps](#get_members_with_apps) - GetMembersWithApps
* [invoke_compute_function](#invoke_compute_function) - Executes a declared compute function on a pooled sandbox worker; gated, org-scoped, rate-limited.
* [list_versions](#list_versions) - Version history: a snapshot is recorded on each publish; authors can list and restore.
* [list](#list) - ListApps
* [move_app_to_folder](#move_app_to_folder) - Moves an app into a library folder (or to root when folder_id is empty).
* [refresh](#refresh) - Re-fetches data sources, rebuilds the document with a fresh snapshot, re-uploads.
* [restore_app_version](#restore_app_version) - RestoreAppVersion
* [set_favorite](#set_favorite) - Favorite/unfavorite a library item (app or dashboard) for the calling member.  Per-member, per-org; favorited=false hard-deletes the row. Covers both primitives  since the merged library page pins apps and dashboards through one client.
* [update](#update) - UpdateApp

## heartbeat

Viewer heartbeat: keeps a warm compute worker alive while the app is open so its
 billed lifetime tracks the view session (mirrors a dashboard's viewer TTL). No-op
 when the app has no warm worker; never spawns one.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_AppHeartbeat" method="post" path="/textql.rpc.public.app.AppService/AppHeartbeat" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.apps.heartbeat()

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
from textql_sdk import Textql


with Textql() as textql:

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
from textql_sdk import Textql


with Textql() as textql:

    res = textql.apps.delete_app()

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

**[models.AppServiceDeleteAppResponse](../../models/appservicedeleteappresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## duplicate

Duplicates an app the caller can view into a new draft app they own,
 named "Copy of <name>". Copies code/files/data sources/compute functions/
 schedule; never carries over the source's published state or data snapshot.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_DuplicateApp" method="post" path="/textql.rpc.public.app.AppService/DuplicateApp" -->
```python
from textql_sdk import Textql


with Textql() as textql:

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
from textql_sdk import Textql


with Textql() as textql:

    res = textql.apps.get()

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

**[models.AppServiceGetAppResponse](../../models/appservicegetappresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_app_version

GetAppVersion

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_GetAppVersion" method="post" path="/textql.rpc.public.app.AppService/GetAppVersion" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.apps.get_app_version()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `version_number`                                                    | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceGetAppVersionResponse](../../models/appservicegetappversionresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_app_view_stats

View analytics: reads the engagement views recorded on app page load.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_GetAppViewStats" method="post" path="/textql.rpc.public.app.AppService/GetAppViewStats" -->
```python
from textql_sdk import Textql


with Textql() as textql:

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

## get_component_gallery_url

Staff-only (superadmin gated in-handler): publishes the embedded component
 gallery as an app tree and returns its signed viewer URL.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_GetComponentGalleryUrl" method="post" path="/textql.rpc.public.app.AppService/GetComponentGalleryUrl" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.apps.get_component_gallery_url()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `runtime_version`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | optional; empty = current default vendor set                        |
| `accent_hex`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | optional; empty = default indigo #6366f1                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceGetComponentGalleryURLResponse](../../models/appservicegetcomponentgalleryurlresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_members_with_apps

GetMembersWithApps

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_GetMembersWithApps" method="post" path="/textql.rpc.public.app.AppService/GetMembersWithApps" -->
```python
from textql_sdk import Textql


with Textql() as textql:

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

Executes a declared compute function on a pooled sandbox worker; gated, org-scoped, rate-limited.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_InvokeAppComputeFunction" method="post" path="/textql.rpc.public.app.AppService/InvokeAppComputeFunction" -->
```python
from textql_sdk import Textql


with Textql() as textql:

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
| `params_json`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | JSON object, keys map to function kwargs                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceInvokeAppComputeFunctionResponse](../../models/appserviceinvokeappcomputefunctionresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_versions

Version history: a snapshot is recorded on each publish; authors can list and restore.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_ListAppVersions" method="post" path="/textql.rpc.public.app.AppService/ListAppVersions" -->
```python
from textql_sdk import Textql


with Textql() as textql:

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
from textql_sdk import Textql


with Textql() as textql:

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
| `folder_id`                                                         | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Filter by specific folder                                           |
| `uncategorized_only`                                                | *OptionalNullable[bool]*                                            | :heavy_minus_sign:                                                  | Only show apps with no folder                                       |
| `shared_with_me`                                                    | *OptionalNullable[bool]*                                            | :heavy_minus_sign:                                                  | Only apps shared with the caller (not authored by them)             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceListAppsResponse](../../models/appservicelistappsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## move_app_to_folder

Moves an app into a library folder (or to root when folder_id is empty).

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_MoveAppToFolder" method="post" path="/textql.rpc.public.app.AppService/MoveAppToFolder" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.apps.move_app_to_folder()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `folder_id`                                                         | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | null/empty = move to root (uncategorized)                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceMoveAppToFolderResponse](../../models/appservicemoveapptofolderresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## refresh

Re-fetches data sources, rebuilds the document with a fresh snapshot, re-uploads.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_RefreshApp" method="post" path="/textql.rpc.public.app.AppService/RefreshApp" -->
```python
from textql_sdk import Textql


with Textql() as textql:

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

RestoreAppVersion

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_RestoreAppVersion" method="post" path="/textql.rpc.public.app.AppService/RestoreAppVersion" -->
```python
from textql_sdk import Textql


with Textql() as textql:

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
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceRestoreAppVersionResponse](../../models/appservicerestoreappversionresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## set_favorite

Favorite/unfavorite a library item (app or dashboard) for the calling member.
 Per-member, per-org; favorited=false hard-deletes the row. Covers both primitives
 since the merged library page pins apps and dashboards through one client.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_SetFavorite" method="post" path="/textql.rpc.public.app.AppService/SetFavorite" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.apps.set_favorite()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `primitive_type`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | 'app' \| 'dashboard'                                                |
| `primitive_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `favorited`                                                         | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | true = pin, false = unpin (hard delete)                             |
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
from textql_sdk import Textql


with Textql() as textql:

    res = textql.apps.update()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                  | *Optional[float]*                                                                                     | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `app_id`                                                                                              | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `name`                                                                                                | *OptionalNullable[str]*                                                                               | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `description`                                                                                         | *OptionalNullable[str]*                                                                               | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `code`                                                                                                | *OptionalNullable[str]*                                                                               | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `data_sources`                                                                                        | List[[models.TextqlRPCPublicDashboardDataSource](../../models/textqlrpcpublicdashboarddatasource.md)] | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `replace_data_sources`                                                                                | *OptionalNullable[bool]*                                                                              | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `publish`                                                                                             | *OptionalNullable[bool]*                                                                              | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `staleness_seconds`                                                                                   | *OptionalNullable[int]*                                                                               | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `compute_functions`                                                                                   | List[[models.TextqlRPCPublicAppComputeFunction](../../models/textqlrpcpublicappcomputefunction.md)]   | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `replace_compute_functions`                                                                           | *OptionalNullable[bool]*                                                                              | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `files`                                                                                               | List[[models.TextqlRPCPublicAppAppFile](../../models/textqlrpcpublicappappfile.md)]                   | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `replace_files`                                                                                       | *OptionalNullable[bool]*                                                                              | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `schedule_enabled`                                                                                    | *OptionalNullable[bool]*                                                                              | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `cron_string`                                                                                         | *OptionalNullable[str]*                                                                               | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.AppServiceUpdateAppResponse](../../models/appserviceupdateappresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |