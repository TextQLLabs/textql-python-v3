# PowerBi

## Overview

### Available Operations

* [get_synced_items](#get_synced_items) - GetSyncedPowerBIItems
* [list_reports](#list_reports) - ListPowerBIReports

## get_synced_items

GetSyncedPowerBIItems

### Example Usage

<!-- UsageSnippet language="python" operationID="PowerBIService_GetSyncedPowerBIItems" method="post" path="/textql.rpc.public.powerbi.PowerBIService/GetSyncedPowerBIItems" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.power_bi.get_synced_items()

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

## list_reports

ListPowerBIReports

### Example Usage

<!-- UsageSnippet language="python" operationID="PowerBIService_ListPowerBIReports" method="post" path="/textql.rpc.public.powerbi.PowerBIService/ListPowerBIReports" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.power_bi.list_reports()

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