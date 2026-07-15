# Apps

## Overview

### Available Operations

* [duplicate](#duplicate) - Duplicates an app the caller can view into a new draft app they own,  named "Copy of <name>". Copies code/files/data sources/compute functions/  schedule; never carries over the source's published state or data snapshot.
* [get](#get) - GetApp
* [get_component_gallery_url](#get_component_gallery_url) - Staff-only (superadmin gated in-handler): publishes the embedded component  gallery as an app tree and returns its signed viewer URL.
* [get_members_with_apps](#get_members_with_apps) - GetMembersWithApps
* [invoke_compute_function](#invoke_compute_function) - Executes a declared compute function on a pooled sandbox worker; gated, org-scoped, rate-limited.
* [list_versions](#list_versions) - Version history: a snapshot is recorded on each publish; authors can list and restore.
* [list](#list) - ListApps
* [set_favorite](#set_favorite) - Favorite/unfavorite a library item (app or dashboard) for the calling member.  Per-member, per-org; favorited=false hard-deletes the row. Covers both primitives  since the merged library page pins apps and dashboards through one client.

## duplicate

Duplicates an app the caller can view into a new draft app they own,
 named "Copy of <name>". Copies code/files/data sources/compute functions/
 schedule; never carries over the source's published state or data snapshot.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_DuplicateApp" method="post" path="/textql.rpc.public.app.AppService/DuplicateApp" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.apps.duplicate()

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
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.apps.get()

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

## get_component_gallery_url

Staff-only (superadmin gated in-handler): publishes the embedded component
 gallery as an app tree and returns its signed viewer URL.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_GetComponentGalleryUrl" method="post" path="/textql.rpc.public.app.AppService/GetComponentGalleryUrl" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.apps.get_component_gallery_url()

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
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.apps.get_members_with_apps(body={})

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
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.apps.invoke_compute_function()

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
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.apps.list_versions()

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
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.apps.list()

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

## set_favorite

Favorite/unfavorite a library item (app or dashboard) for the calling member.
 Per-member, per-org; favorited=false hard-deletes the row. Covers both primitives
 since the merged library page pins apps and dashboards through one client.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_SetFavorite" method="post" path="/textql.rpc.public.app.AppService/SetFavorite" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.apps.set_favorite()

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