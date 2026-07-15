# MetricsExportService

## Overview

### Available Operations

* [delete_config](#delete_config) - DeleteMetricsExportConfig

## delete_config

DeleteMetricsExportConfig

### Example Usage

<!-- UsageSnippet language="python" operationID="MetricsExportService_DeleteMetricsExportConfig" method="post" path="/textql.rpc.public.metrics_export.MetricsExportService/DeleteMetricsExportConfig" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.metrics_export_service.delete_config(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                           | Type                                                                                                                                                | Required                                                                                                                                            | Description                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                                              | [models.TextqlRPCPublicMetricsExportDeleteMetricsExportConfigRequest](../../models/textqlrpcpublicmetricsexportdeletemetricsexportconfigrequest.md) | :heavy_check_mark:                                                                                                                                  | N/A                                                                                                                                                 |
| `connect_timeout_ms`                                                                                                                                | *Optional[float]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                  | N/A                                                                                                                                                 |
| `retries`                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                    | :heavy_minus_sign:                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                 |

### Response

**[models.MetricsExportServiceDeleteMetricsExportConfigResponse](../../models/metricsexportservicedeletemetricsexportconfigresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |