# PowerbiDatasets

## Overview

### Available Operations

* [list](#list) - ListPowerBIDatasets

## list

ListPowerBIDatasets

### Example Usage

<!-- UsageSnippet language="python" operationID="PowerBIService_ListPowerBIDatasets" method="post" path="/textql.rpc.public.powerbi.PowerBIService/ListPowerBIDatasets" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.powerbi_datasets.list()

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