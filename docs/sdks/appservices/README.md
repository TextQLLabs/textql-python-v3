# AppServices

## Overview

### Available Operations

* [create_app](#create_app) - CreateApp
* [delete_app](#delete_app) - DeleteApp
* [refresh](#refresh) - Re-fetches data sources, rebuilds the document with a fresh snapshot, re-uploads.
* [update](#update) - UpdateApp

## create_app

CreateApp

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_CreateApp" method="post" path="/textql.rpc.public.app.AppService/CreateApp" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.app_services.create_app()

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
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.app_services.delete_app()

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

## refresh

Re-fetches data sources, rebuilds the document with a fresh snapshot, re-uploads.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_RefreshApp" method="post" path="/textql.rpc.public.app.AppService/RefreshApp" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.app_services.refresh()

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

## update

UpdateApp

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_UpdateApp" method="post" path="/textql.rpc.public.app.AppService/UpdateApp" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.app_services.update()

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