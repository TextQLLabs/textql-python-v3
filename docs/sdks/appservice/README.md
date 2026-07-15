# AppService

## Overview

AppService manages data apps: the generative app execution primitive.
 An app is agent-authored single-file HTML/JS/CSS executing in a CSP sandbox,
 fed a snapshot of its declared data sources. First-class resource, not a dashboard.

### Available Operations

* [heartbeat](#heartbeat) - Viewer heartbeat: keeps a warm compute worker alive while the app is open so its  billed lifetime tracks the view session (mirrors a dashboard's viewer TTL). No-op  when the app has no warm worker; never spawns one.
* [get_app_version](#get_app_version) - GetAppVersion
* [get_app_view_stats](#get_app_view_stats) - View analytics: reads the engagement views recorded on app page load.
* [move_app_to_folder](#move_app_to_folder) - Moves an app into a library folder (or to root when folder_id is empty).
* [restore_app_version](#restore_app_version) - RestoreAppVersion

## heartbeat

Viewer heartbeat: keeps a warm compute worker alive while the app is open so its
 billed lifetime tracks the view session (mirrors a dashboard's viewer TTL). No-op
 when the app has no warm worker; never spawns one.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_AppHeartbeat" method="post" path="/textql.rpc.public.app.AppService/AppHeartbeat" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.app_service.heartbeat()

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

## get_app_version

GetAppVersion

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_GetAppVersion" method="post" path="/textql.rpc.public.app.AppService/GetAppVersion" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.app_service.get_app_version()

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
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.app_service.get_app_view_stats()

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

## move_app_to_folder

Moves an app into a library folder (or to root when folder_id is empty).

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_MoveAppToFolder" method="post" path="/textql.rpc.public.app.AppService/MoveAppToFolder" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.app_service.move_app_to_folder()

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

## restore_app_version

RestoreAppVersion

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_RestoreAppVersion" method="post" path="/textql.rpc.public.app.AppService/RestoreAppVersion" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.app_service.restore_app_version()

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