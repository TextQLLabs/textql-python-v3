# Dashboards

## Overview

### Available Operations

* [create_folder](#create_folder) - Folder management
* [delete_folder](#delete_folder) - DeleteDashboardFolder
* [duplicate](#duplicate) - DuplicateDashboard
* [list_folders](#list_folders) - ListDashboardFolders
* [list](#list) - ListDashboards
* [move_to_folder](#move_to_folder) - MoveDashboardToFolder
* [publish](#publish) - Publishing workflow
* [regenerate_screenshot](#regenerate_screenshot) - Screenshot management
* [run_scheduled_dashboard](#run_scheduled_dashboard) - RunScheduledDashboard

## create_folder

Folder management

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_CreateDashboardFolder" method="post" path="/textql.rpc.public.dashboard.DashboardService/CreateDashboardFolder" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dashboards.create_folder()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `name`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `parent_id`                                                         | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DashboardServiceCreateDashboardFolderResponse](../../models/dashboardservicecreatedashboardfolderresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete_folder

DeleteDashboardFolder

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_DeleteDashboardFolder" method="post" path="/textql.rpc.public.dashboard.DashboardService/DeleteDashboardFolder" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dashboards.delete_folder()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `folder_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DashboardServiceDeleteDashboardFolderResponse](../../models/dashboardservicedeletedashboardfolderresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## duplicate

DuplicateDashboard

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_DuplicateDashboard" method="post" path="/textql.rpc.public.dashboard.DashboardService/DuplicateDashboard" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dashboards.duplicate()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                        | *Optional[float]*                                                           | :heavy_minus_sign:                                                          | N/A                                                                         |
| `dashboard_id`                                                              | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | N/A                                                                         |
| `name`                                                                      | *OptionalNullable[str]*                                                     | :heavy_minus_sign:                                                          | Optional new name for the duplicate (defaults to "Copy of [original name]") |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.DashboardServiceDuplicateDashboardResponse](../../models/dashboardserviceduplicatedashboardresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_folders

ListDashboardFolders

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_ListDashboardFolders" method="post" path="/textql.rpc.public.dashboard.DashboardService/ListDashboardFolders" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dashboards.list_folders(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                         | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                            | [models.TextqlRPCPublicDashboardListDashboardFoldersRequest](../../models/textqlrpcpublicdashboardlistdashboardfoldersrequest.md) | :heavy_check_mark:                                                                                                                | N/A                                                                                                                               |
| `connect_timeout_ms`                                                                                                              | *Optional[float]*                                                                                                                 | :heavy_minus_sign:                                                                                                                | N/A                                                                                                                               |
| `retries`                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                  | :heavy_minus_sign:                                                                                                                | Configuration to override the default retry behavior of the client.                                                               |

### Response

**[models.DashboardServiceListDashboardFoldersResponse](../../models/dashboardservicelistdashboardfoldersresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list

ListDashboards

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_ListDashboards" method="post" path="/textql.rpc.public.dashboard.DashboardService/ListDashboards" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dashboards.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                      | *Optional[float]*                                                                                                         | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `search_term`                                                                                                             | *OptionalNullable[str]*                                                                                                   | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `my_dashboards_only`                                                                                                      | *OptionalNullable[bool]*                                                                                                  | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `sort_by`                                                                                                                 | [Optional[models.TextqlRPCPublicDashboardDashboardSortField]](../../models/textqlrpcpublicdashboarddashboardsortfield.md) | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `sort_direction`                                                                                                          | [Optional[models.TextqlRPCPublicCommonSortDirection]](../../models/textqlrpcpubliccommonsortdirection.md)                 | :heavy_minus_sign:                                                                                                        | Common enum for sort direction used across multiple services                                                              |
| `limit`                                                                                                                   | *Optional[int]*                                                                                                           | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `offset`                                                                                                                  | *Optional[int]*                                                                                                           | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `folder_id`                                                                                                               | *OptionalNullable[str]*                                                                                                   | :heavy_minus_sign:                                                                                                        | Filter by specific folder                                                                                                 |
| `uncategorized_only`                                                                                                      | *OptionalNullable[bool]*                                                                                                  | :heavy_minus_sign:                                                                                                        | Only show dashboards with no folder                                                                                       |
| `creator_member_id`                                                                                                       | *OptionalNullable[str]*                                                                                                   | :heavy_minus_sign:                                                                                                        | Filter by specific creator member ID (single-select; superseded by creator_member_ids when non-empty)                     |
| `shared_with_me`                                                                                                          | *OptionalNullable[bool]*                                                                                                  | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `creator_member_ids`                                                                                                      | List[*str*]                                                                                                               | :heavy_minus_sign:                                                                                                        | Multi-select creator filter (union). Supersedes creator_member_id when non-empty.                                         |
| `status_filter`                                                                                                           | [Optional[models.TextqlRPCPublicDashboardDashboardStatus]](../../models/textqlrpcpublicdashboarddashboardstatus.md)       | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |

### Response

**[models.DashboardServiceListDashboardsResponse](../../models/dashboardservicelistdashboardsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## move_to_folder

MoveDashboardToFolder

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_MoveDashboardToFolder" method="post" path="/textql.rpc.public.dashboard.DashboardService/MoveDashboardToFolder" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dashboards.move_to_folder()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dashboard_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `folder_id`                                                         | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | null/empty = move to root (uncategorized)                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DashboardServiceMoveDashboardToFolderResponse](../../models/dashboardservicemovedashboardtofolderresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## publish

Publishing workflow

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_PublishDashboard" method="post" path="/textql.rpc.public.dashboard.DashboardService/PublishDashboard" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dashboards.publish()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dashboard_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `label`                                                             | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Optional version label/description                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DashboardServicePublishDashboardResponse](../../models/dashboardservicepublishdashboardresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## regenerate_screenshot

Screenshot management

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_RegenerateScreenshot" method="post" path="/textql.rpc.public.dashboard.DashboardService/RegenerateScreenshot" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dashboards.regenerate_screenshot()

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

**[models.DashboardServiceRegenerateScreenshotResponse](../../models/dashboardserviceregeneratescreenshotresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## run_scheduled_dashboard

RunScheduledDashboard

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_RunScheduledDashboard" method="post" path="/textql.rpc.public.dashboard.DashboardService/RunScheduledDashboard" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dashboards.run_scheduled_dashboard()

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

**[models.DashboardServiceRunScheduledDashboardResponse](../../models/dashboardservicerunscheduleddashboardresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |