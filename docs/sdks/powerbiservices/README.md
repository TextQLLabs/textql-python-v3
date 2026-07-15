# PowerBiServices

## Overview

### Available Operations

* [export_report_image](#export_report_image) - ExportPowerBIReportImage
* [unsync_items](#unsync_items) - UnsyncPowerBIItems
* [sync_power_bi_items](#sync_power_bi_items) - SyncPowerBIItems

## export_report_image

ExportPowerBIReportImage

### Example Usage

<!-- UsageSnippet language="python" operationID="PowerBIService_ExportPowerBIReportImage" method="post" path="/textql.rpc.public.powerbi.PowerBIService/ExportPowerBIReportImage" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.power_bi_services.export_report_image()

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

## unsync_items

UnsyncPowerBIItems

### Example Usage

<!-- UsageSnippet language="python" operationID="PowerBIService_UnsyncPowerBIItems" method="post" path="/textql.rpc.public.powerbi.PowerBIService/UnsyncPowerBIItems" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.power_bi_services.unsync_items()

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

## sync_power_bi_items

SyncPowerBIItems

### Example Usage

<!-- UsageSnippet language="python" operationID="PowerBIService_SyncPowerBIItems" method="post" path="/textql.rpc.public.powerbi.PowerBIService/SyncPowerBIItems" -->
```python
from textql_sdk import TextQL
from textql_sdk.utils import parse_datetime


with TextQL() as text_ql:

    res = text_ql.power_bi_services.sync_power_bi_items(reports=[
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