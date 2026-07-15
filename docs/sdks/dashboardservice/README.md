# DashboardService

## Overview

### Available Operations

* [create_dashboard](#create_dashboard) - CRUD operations
* [get_members_with_dashboards](#get_members_with_dashboards) - Member management
* [restore_dashboard_version](#restore_dashboard_version) - RestoreDashboardVersion
* [update_dashboard](#update_dashboard) - UpdateDashboard
* [update_dashboard_schedule](#update_dashboard_schedule) - Scheduling

## create_dashboard

CRUD operations

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_CreateDashboard" method="post" path="/textql.rpc.public.dashboard.DashboardService/CreateDashboard" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dashboard_service.create_dashboard()

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

## get_members_with_dashboards

Member management

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_GetMembersWithDashboards" method="post" path="/textql.rpc.public.dashboard.DashboardService/GetMembersWithDashboards" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dashboard_service.get_members_with_dashboards(body={})

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

## restore_dashboard_version

RestoreDashboardVersion

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_RestoreDashboardVersion" method="post" path="/textql.rpc.public.dashboard.DashboardService/RestoreDashboardVersion" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dashboard_service.restore_dashboard_version()

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

## update_dashboard

UpdateDashboard

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_UpdateDashboard" method="post" path="/textql.rpc.public.dashboard.DashboardService/UpdateDashboard" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dashboard_service.update_dashboard()

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

## update_dashboard_schedule

Scheduling

### Example Usage

<!-- UsageSnippet language="python" operationID="DashboardService_UpdateDashboardSchedule" method="post" path="/textql.rpc.public.dashboard.DashboardService/UpdateDashboardSchedule" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dashboard_service.update_dashboard_schedule()

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