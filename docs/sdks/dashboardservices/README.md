# DashboardServices

## Overview

### Available Operations

* [check_health](#check_health) - CheckDashboardHealth
* [delete](#delete) - DeleteDashboard
* [discard_changes](#discard_changes) - DiscardDashboardChanges
* [get](#get) - GetDashboard
* [get_version](#get_version) - GetDashboardVersion
* [get_dashboard_view_stats](#get_dashboard_view_stats) - View analytics
* [list_versions](#list_versions) - Version history
* [preview_config](#preview_config) - Config-managed dashboards: render a `.dashboard` straight from a patch ref before  it merges (ADR-0022). Runs as the file's run_as, gated on the previewer being  authorized for it; persists nothing.
* [spawn](#spawn) - Dashboard execution
* [update_dashboard_folder](#update_dashboard_folder) - UpdateDashboardFolder

## check_health

CheckDashboardHealth

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_CheckDashboardHealth" method="post" path="/textql.rpc.public.dashboard.DashboardService/CheckDashboardHealth" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dashboard_services.check_health()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dashboard_ids`                                                     | List[*str*]                                                         | :heavy_minus_sign:                                                  | Batch check multiple dashboards                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DashboardServiceCheckDashboardHealthResponse](../../models/dashboardservicecheckdashboardhealthresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete

DeleteDashboard

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_DeleteDashboard" method="post" path="/textql.rpc.public.dashboard.DashboardService/DeleteDashboard" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dashboard_services.delete()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dashboard_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DashboardServiceDeleteDashboardResponse](../../models/dashboardservicedeletedashboardresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## discard_changes

DiscardDashboardChanges

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_DiscardDashboardChanges" method="post" path="/textql.rpc.public.dashboard.DashboardService/DiscardDashboardChanges" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dashboard_services.discard_changes()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dashboard_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DashboardServiceDiscardDashboardChangesResponse](../../models/dashboardservicediscarddashboardchangesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get

GetDashboard

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_GetDashboard" method="post" path="/textql.rpc.public.dashboard.DashboardService/GetDashboard" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dashboard_services.get()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dashboard_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DashboardServiceGetDashboardResponse](../../models/dashboardservicegetdashboardresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_version

GetDashboardVersion

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_GetDashboardVersion" method="post" path="/textql.rpc.public.dashboard.DashboardService/GetDashboardVersion" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dashboard_services.get_version()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dashboard_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `version_number`                                                    | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DashboardServiceGetDashboardVersionResponse](../../models/dashboardservicegetdashboardversionresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_dashboard_view_stats

View analytics

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_GetDashboardViewStats" method="post" path="/textql.rpc.public.dashboard.DashboardService/GetDashboardViewStats" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dashboard_services.get_dashboard_view_stats()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dashboard_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DashboardServiceGetDashboardViewStatsResponse](../../models/dashboardservicegetdashboardviewstatsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_versions

Version history

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_ListDashboardVersions" method="post" path="/textql.rpc.public.dashboard.DashboardService/ListDashboardVersions" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dashboard_services.list_versions()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dashboard_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DashboardServiceListDashboardVersionsResponse](../../models/dashboardservicelistdashboardversionsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## preview_config

Config-managed dashboards: render a `.dashboard` straight from a patch ref before
 it merges (ADR-0022). Runs as the file's run_as, gated on the previewer being
 authorized for it; persists nothing.

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_PreviewConfigDashboard" method="post" path="/textql.rpc.public.dashboard.DashboardService/PreviewConfigDashboard" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dashboard_services.preview_config()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `patch_ref`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | git ref of the patch to preview from                                |
| `dashboard_path`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Library path of the .dashboard file                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DashboardServicePreviewConfigDashboardResponse](../../models/dashboardservicepreviewconfigdashboardresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## spawn

Dashboard execution

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_SpawnDashboard" method="post" path="/textql.rpc.public.dashboard.DashboardService/SpawnDashboard" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dashboard_services.spawn()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                          | *Optional[float]*                                                             | :heavy_minus_sign:                                                            | N/A                                                                           |
| `dashboard_id`                                                                | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | N/A                                                                           |
| `force_restart`                                                               | *Optional[bool]*                                                              | :heavy_minus_sign:                                                            | Force restart even if already running                                         |
| `refresh_data_only`                                                           | *Optional[bool]*                                                              | :heavy_minus_sign:                                                            | Re-fetch data sources and reload without restarting the app                   |
| `refresh_source_names`                                                        | List[*str*]                                                                   | :heavy_minus_sign:                                                            | If non-empty with refresh_data_only, only refresh these sources by name       |
| `refresh_code_only`                                                           | *Optional[bool]*                                                              | :heavy_minus_sign:                                                            | Update code in-place via Streamlit's runOnSave without restarting the process |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.DashboardServiceSpawnDashboardResponse](../../models/dashboardservicespawndashboardresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## update_dashboard_folder

UpdateDashboardFolder

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_UpdateDashboardFolder" method="post" path="/textql.rpc.public.dashboard.DashboardService/UpdateDashboardFolder" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dashboard_services.update_dashboard_folder()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `folder_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `name`                                                              | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `parent_id`                                                         | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Move folder to different parent (empty string = move to root)       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DashboardServiceUpdateDashboardFolderResponse](../../models/dashboardserviceupdatedashboardfolderresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |