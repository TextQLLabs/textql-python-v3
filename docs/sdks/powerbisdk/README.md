# Powerbi

## Overview

### Available Operations

* [export_report_image](#export_report_image) - ExportPowerBIReportImage
* [generate_embed_token](#generate_embed_token) - GeneratePowerBIEmbedToken
* [get_dataset_preview](#get_dataset_preview) - GetPowerBIDatasetPreview
* [get_synced_items](#get_synced_items) - GetSyncedPowerBIItems
* [list](#list) - ListPowerBIDatasets
* [list_reports](#list_reports) - ListPowerBIReports
* [list_workspaces](#list_workspaces) - ListPowerBIWorkspaces
* [sync_power_bi_items](#sync_power_bi_items) - SyncPowerBIItems
* [test_connection](#test_connection) - TestPowerBIConnection
* [unsync_items](#unsync_items) - UnsyncPowerBIItems

## export_report_image

ExportPowerBIReportImage

### Example Usage

<!-- UsageSnippet language="python" operationID="PowerBIService_ExportPowerBIReportImage" method="post" path="/textql.rpc.public.powerbi.PowerBIService/ExportPowerBIReportImage" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.powerbi.export_report_image()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `connector_id`                                                      | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `workspace_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `report_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PowerBIServiceExportPowerBIReportImageResponse](../../models/powerbiserviceexportpowerbireportimageresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## generate_embed_token

GeneratePowerBIEmbedToken

### Example Usage

<!-- UsageSnippet language="python" operationID="PowerBIService_GeneratePowerBIEmbedToken" method="post" path="/textql.rpc.public.powerbi.PowerBIService/GeneratePowerBIEmbedToken" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.powerbi.generate_embed_token()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `connector_id`                                                      | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `workspace_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `report_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dataset_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PowerBIServiceGeneratePowerBIEmbedTokenResponse](../../models/powerbiservicegeneratepowerbiembedtokenresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_dataset_preview

GetPowerBIDatasetPreview

### Example Usage

<!-- UsageSnippet language="python" operationID="PowerBIService_GetPowerBIDatasetPreview" method="post" path="/textql.rpc.public.powerbi.PowerBIService/GetPowerBIDatasetPreview" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.powerbi.get_dataset_preview()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `connector_id`                                                      | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `workspace_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dataset_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dataset_name`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PowerBIServiceGetPowerBIDatasetPreviewResponse](../../models/powerbiservicegetpowerbidatasetpreviewresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_synced_items

GetSyncedPowerBIItems

### Example Usage

<!-- UsageSnippet language="python" operationID="PowerBIService_GetSyncedPowerBIItems" method="post" path="/textql.rpc.public.powerbi.PowerBIService/GetSyncedPowerBIItems" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.powerbi.get_synced_items()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `connector_id`                                                      | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PowerBIServiceGetSyncedPowerBIItemsResponse](../../models/powerbiservicegetsyncedpowerbiitemsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list

ListPowerBIDatasets

### Example Usage

<!-- UsageSnippet language="python" operationID="PowerBIService_ListPowerBIDatasets" method="post" path="/textql.rpc.public.powerbi.PowerBIService/ListPowerBIDatasets" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.powerbi.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `connector_id`                                                      | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `workspace_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PowerBIServiceListPowerBIDatasetsResponse](../../models/powerbiservicelistpowerbidatasetsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_reports

ListPowerBIReports

### Example Usage

<!-- UsageSnippet language="python" operationID="PowerBIService_ListPowerBIReports" method="post" path="/textql.rpc.public.powerbi.PowerBIService/ListPowerBIReports" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.powerbi.list_reports()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `connector_id`                                                      | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `workspace_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PowerBIServiceListPowerBIReportsResponse](../../models/powerbiservicelistpowerbireportsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_workspaces

ListPowerBIWorkspaces

### Example Usage

<!-- UsageSnippet language="python" operationID="PowerBIService_ListPowerBIWorkspaces" method="post" path="/textql.rpc.public.powerbi.PowerBIService/ListPowerBIWorkspaces" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.powerbi.list_workspaces()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `connector_id`                                                      | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PowerBIServiceListPowerBIWorkspacesResponse](../../models/powerbiservicelistpowerbiworkspacesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## sync_power_bi_items

SyncPowerBIItems

### Example Usage

<!-- UsageSnippet language="python" operationID="PowerBIService_SyncPowerBIItems" method="post" path="/textql.rpc.public.powerbi.PowerBIService/SyncPowerBIItems" -->
```python
from textql_sdk import Textql
from textql_sdk.utils import parse_datetime


with Textql() as textql:

    res = textql.powerbi.sync_power_bi_items(reports=[
        {
            "created_date": parse_datetime("2023-01-15T01:30:15.01Z"),
        },
    ], datasets=[
        {
            "created_date": parse_datetime("2023-01-15T01:30:15.01Z"),
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                      | *Optional[float]*                                                                                         | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `connector_id`                                                                                            | *Optional[int]*                                                                                           | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `workspace_id`                                                                                            | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `workspace_name`                                                                                          | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `reports`                                                                                                 | List[[models.TextqlRPCPublicPowerbiPowerBIReport](../../models/textqlrpcpublicpowerbipowerbireport.md)]   | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `datasets`                                                                                                | List[[models.TextqlRPCPublicPowerbiPowerBIDataset](../../models/textqlrpcpublicpowerbipowerbidataset.md)] | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.PowerBIServiceSyncPowerBIItemsResponse](../../models/powerbiservicesyncpowerbiitemsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## test_connection

TestPowerBIConnection

### Example Usage

<!-- UsageSnippet language="python" operationID="PowerBIService_TestPowerBIConnection" method="post" path="/textql.rpc.public.powerbi.PowerBIService/TestPowerBIConnection" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.powerbi.test_connection()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `connector_id`                                                      | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `tenant_id`                                                         | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `client_id`                                                         | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `client_secret`                                                     | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PowerBIServiceTestPowerBIConnectionResponse](../../models/powerbiservicetestpowerbiconnectionresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## unsync_items

UnsyncPowerBIItems

### Example Usage

<!-- UsageSnippet language="python" operationID="PowerBIService_UnsyncPowerBIItems" method="post" path="/textql.rpc.public.powerbi.PowerBIService/UnsyncPowerBIItems" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.powerbi.unsync_items()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `connector_id`                                                      | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `report_ids`                                                        | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dataset_ids`                                                       | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PowerBIServiceUnsyncPowerBIItemsResponse](../../models/powerbiserviceunsyncpowerbiitemsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |