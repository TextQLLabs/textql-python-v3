# MetricsExportServices

## Overview

### Available Operations

* [get_metrics_export_config](#get_metrics_export_config) - GetMetricsExportConfig
* [trigger_push](#trigger_push) - TriggerMetricsPush

## get_metrics_export_config

GetMetricsExportConfig

### Example Usage

<!-- UsageSnippet language="python" operationID="MetricsExportService_GetMetricsExportConfig" method="post" path="/textql.rpc.public.metrics_export.MetricsExportService/GetMetricsExportConfig" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.metrics_export_services.get_metrics_export_config(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                                        | [models.TextqlRPCPublicMetricsExportGetMetricsExportConfigRequest](../../models/textqlrpcpublicmetricsexportgetmetricsexportconfigrequest.md) | :heavy_check_mark:                                                                                                                            | N/A                                                                                                                                           |
| `connect_timeout_ms`                                                                                                                          | *Optional[float]*                                                                                                                             | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |

### Response

**[models.MetricsExportServiceGetMetricsExportConfigResponse](../../models/metricsexportservicegetmetricsexportconfigresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## trigger_push

TriggerMetricsPush

### Example Usage

<!-- UsageSnippet language="python" operationID="MetricsExportService_TriggerMetricsPush" method="post" path="/textql.rpc.public.metrics_export.MetricsExportService/TriggerMetricsPush" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.metrics_export_services.trigger_push(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                             | Type                                                                                                                                  | Required                                                                                                                              | Description                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                                | [models.TextqlRPCPublicMetricsExportTriggerMetricsPushRequest](../../models/textqlrpcpublicmetricsexporttriggermetricspushrequest.md) | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `connect_timeout_ms`                                                                                                                  | *Optional[float]*                                                                                                                     | :heavy_minus_sign:                                                                                                                    | N/A                                                                                                                                   |
| `retries`                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                      | :heavy_minus_sign:                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                   |

### Response

**[models.MetricsExportServiceTriggerMetricsPushResponse](../../models/metricsexportservicetriggermetricspushresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |