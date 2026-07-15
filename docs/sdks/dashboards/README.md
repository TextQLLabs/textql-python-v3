# Dashboards

## Overview

### Available Operations

* [check_health](#check_health) - CheckDashboardHealth
* [create_dashboard](#create_dashboard) - CRUD operations
* [create_folder](#create_folder) - Folder management
* [delete](#delete) - DeleteDashboard
* [delete_folder](#delete_folder) - DeleteDashboardFolder
* [discard_changes](#discard_changes) - DiscardDashboardChanges
* [duplicate](#duplicate) - DuplicateDashboard
* [get](#get) - GetDashboard
* [get_version](#get_version) - GetDashboardVersion
* [get_dashboard_view_stats](#get_dashboard_view_stats) - View analytics
* [get_members_with_dashboards](#get_members_with_dashboards) - Member management
* [list_folders](#list_folders) - ListDashboardFolders
* [list_versions](#list_versions) - Version history
* [list](#list) - ListDashboards
* [move_to_folder](#move_to_folder) - MoveDashboardToFolder
* [preview_config](#preview_config) - Config-managed dashboards: render a `.dashboard` straight from a patch ref before  it merges (ADR-0022). Runs as the file's run_as, gated on the previewer being  authorized for it; persists nothing.
* [publish](#publish) - Publishing workflow
* [regenerate_screenshot](#regenerate_screenshot) - Screenshot management
* [restore_dashboard_version](#restore_dashboard_version) - RestoreDashboardVersion
* [run_scheduled_dashboard](#run_scheduled_dashboard) - RunScheduledDashboard
* [spawn](#spawn) - Dashboard execution
* [update_dashboard](#update_dashboard) - UpdateDashboard
* [update_dashboard_folder](#update_dashboard_folder) - UpdateDashboardFolder
* [update_dashboard_schedule](#update_dashboard_schedule) - Scheduling

## check_health

CheckDashboardHealth

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_CheckDashboardHealth" method="post" path="/textql.rpc.public.dashboard.DashboardService/CheckDashboardHealth" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.dashboards.check_health()

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

## create_dashboard

CRUD operations

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_CreateDashboard" method="post" path="/textql.rpc.public.dashboard.DashboardService/CreateDashboard" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.dashboards.create_dashboard()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                            | *Optional[float]*                                                                                               | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `name`                                                                                                          | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `description`                                                                                                   | *OptionalNullable[str]*                                                                                         | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `code`                                                                                                          | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `type`                                                                                                          | [Optional[models.TextqlRPCPublicDashboardDashboardType]](../../models/textqlrpcpublicdashboarddashboardtype.md) | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `html_url`                                                                                                      | *OptionalNullable[str]*                                                                                         | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `chat_id`                                                                                                       | *OptionalNullable[str]*                                                                                         | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `cell_id`                                                                                                       | *OptionalNullable[str]*                                                                                         | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `folder_id`                                                                                                     | *OptionalNullable[str]*                                                                                         | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.DashboardServiceCreateDashboardResponse](../../models/dashboardservicecreatedashboardresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## create_folder

Folder management

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_CreateDashboardFolder" method="post" path="/textql.rpc.public.dashboard.DashboardService/CreateDashboardFolder" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.dashboards.create_folder()

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

## delete

DeleteDashboard

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_DeleteDashboard" method="post" path="/textql.rpc.public.dashboard.DashboardService/DeleteDashboard" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.dashboards.delete()

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

## delete_folder

DeleteDashboardFolder

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_DeleteDashboardFolder" method="post" path="/textql.rpc.public.dashboard.DashboardService/DeleteDashboardFolder" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.dashboards.delete_folder()

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

## discard_changes

DiscardDashboardChanges

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_DiscardDashboardChanges" method="post" path="/textql.rpc.public.dashboard.DashboardService/DiscardDashboardChanges" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.dashboards.discard_changes()

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

## duplicate

DuplicateDashboard

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_DuplicateDashboard" method="post" path="/textql.rpc.public.dashboard.DashboardService/DuplicateDashboard" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.dashboards.duplicate()

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

## get

GetDashboard

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_GetDashboard" method="post" path="/textql.rpc.public.dashboard.DashboardService/GetDashboard" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.dashboards.get()

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
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.dashboards.get_version()

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
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.dashboards.get_dashboard_view_stats()

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

## get_members_with_dashboards

Member management

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_GetMembersWithDashboards" method="post" path="/textql.rpc.public.dashboard.DashboardService/GetMembersWithDashboards" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.dashboards.get_members_with_dashboards(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                                    | [models.TextqlRPCPublicDashboardGetMembersWithDashboardsRequest](../../models/textqlrpcpublicdashboardgetmemberswithdashboardsrequest.md) | :heavy_check_mark:                                                                                                                        | N/A                                                                                                                                       |
| `connect_timeout_ms`                                                                                                                      | *Optional[float]*                                                                                                                         | :heavy_minus_sign:                                                                                                                        | N/A                                                                                                                                       |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |

### Response

**[models.DashboardServiceGetMembersWithDashboardsResponse](../../models/dashboardservicegetmemberswithdashboardsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_folders

ListDashboardFolders

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_ListDashboardFolders" method="post" path="/textql.rpc.public.dashboard.DashboardService/ListDashboardFolders" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.dashboards.list_folders(body={})

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

## list_versions

Version history

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_ListDashboardVersions" method="post" path="/textql.rpc.public.dashboard.DashboardService/ListDashboardVersions" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.dashboards.list_versions()

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

## list

ListDashboards

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_ListDashboards" method="post" path="/textql.rpc.public.dashboard.DashboardService/ListDashboards" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.dashboards.list()

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
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.dashboards.move_to_folder()

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

## preview_config

Config-managed dashboards: render a `.dashboard` straight from a patch ref before
 it merges (ADR-0022). Runs as the file's run_as, gated on the previewer being
 authorized for it; persists nothing.

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_PreviewConfigDashboard" method="post" path="/textql.rpc.public.dashboard.DashboardService/PreviewConfigDashboard" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.dashboards.preview_config()

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

## publish

Publishing workflow

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_PublishDashboard" method="post" path="/textql.rpc.public.dashboard.DashboardService/PublishDashboard" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.dashboards.publish()

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
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.dashboards.regenerate_screenshot()

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

## restore_dashboard_version

RestoreDashboardVersion

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_RestoreDashboardVersion" method="post" path="/textql.rpc.public.dashboard.DashboardService/RestoreDashboardVersion" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.dashboards.restore_dashboard_version()

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

**[models.DashboardServiceRestoreDashboardVersionResponse](../../models/dashboardservicerestoredashboardversionresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## run_scheduled_dashboard

RunScheduledDashboard

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_RunScheduledDashboard" method="post" path="/textql.rpc.public.dashboard.DashboardService/RunScheduledDashboard" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.dashboards.run_scheduled_dashboard()

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

## spawn

Dashboard execution

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_SpawnDashboard" method="post" path="/textql.rpc.public.dashboard.DashboardService/SpawnDashboard" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.dashboards.spawn()

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

## update_dashboard

UpdateDashboard

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_UpdateDashboard" method="post" path="/textql.rpc.public.dashboard.DashboardService/UpdateDashboard" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.dashboards.update_dashboard()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                  | *Optional[float]*                                                                                                     | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `dashboard_id`                                                                                                        | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `name`                                                                                                                | *OptionalNullable[str]*                                                                                               | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `description`                                                                                                         | *OptionalNullable[str]*                                                                                               | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `code`                                                                                                                | *OptionalNullable[str]*                                                                                               | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `type`                                                                                                                | [Optional[models.TextqlRPCPublicDashboardDashboardType]](../../models/textqlrpcpublicdashboarddashboardtype.md)       | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `html_url`                                                                                                            | *OptionalNullable[str]*                                                                                               | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `data_sources`                                                                                                        | [Optional[models.TextqlRPCPublicDashboardDataSourcesPatch]](../../models/textqlrpcpublicdashboarddatasourcespatch.md) | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |

### Response

**[models.DashboardServiceUpdateDashboardResponse](../../models/dashboardserviceupdatedashboardresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## update_dashboard_folder

UpdateDashboardFolder

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_UpdateDashboardFolder" method="post" path="/textql.rpc.public.dashboard.DashboardService/UpdateDashboardFolder" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.dashboards.update_dashboard_folder()

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

## update_dashboard_schedule

Scheduling

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_UpdateDashboardSchedule" method="post" path="/textql.rpc.public.dashboard.DashboardService/UpdateDashboardSchedule" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.dashboards.update_dashboard_schedule()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                  | *Optional[float]*                                                                                     | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `dashboard_id`                                                                                        | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `schedule_enabled`                                                                                    | *Optional[bool]*                                                                                      | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `cron_string`                                                                                         | *OptionalNullable[str]*                                                                               | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `data_sources`                                                                                        | List[[models.TextqlRPCPublicDashboardDataSource](../../models/textqlrpcpublicdashboarddatasource.md)] | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.DashboardServiceUpdateDashboardScheduleResponse](../../models/dashboardserviceupdatedashboardscheduleresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |