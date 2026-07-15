# MetricsExports

## Overview

### Available Operations

* [configure](#configure) - ConfigureMetricsExport
* [delete_config](#delete_config) - DeleteMetricsExportConfig
* [get_metrics_export_config](#get_metrics_export_config) - GetMetricsExportConfig
* [test_connection](#test_connection) - TestMetricsExportConnection
* [trigger_push](#trigger_push) - TriggerMetricsPush

## configure

ConfigureMetricsExport

### Example Usage

<!-- UsageSnippet language="python" operationID="MetricsExportService_ConfigureMetricsExport" method="post" path="/textql.rpc.public.metrics_export.MetricsExportService/ConfigureMetricsExport" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.metrics_exports.configure()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `prometheus_enabled`                                                | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `otlp_enabled`                                                      | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `otlp_endpoint`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `otlp_headers`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `otlp_protocol`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `push_interval_seconds`                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MetricsExportServiceConfigureMetricsExportResponse](../../models/metricsexportserviceconfiguremetricsexportresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete_config

DeleteMetricsExportConfig

### Example Usage

<!-- UsageSnippet language="python" operationID="MetricsExportService_DeleteMetricsExportConfig" method="post" path="/textql.rpc.public.metrics_export.MetricsExportService/DeleteMetricsExportConfig" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.metrics_exports.delete_config(body={})

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

## get_metrics_export_config

GetMetricsExportConfig

### Example Usage

<!-- UsageSnippet language="python" operationID="MetricsExportService_GetMetricsExportConfig" method="post" path="/textql.rpc.public.metrics_export.MetricsExportService/GetMetricsExportConfig" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.metrics_exports.get_metrics_export_config(body={})

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

## test_connection

TestMetricsExportConnection

### Example Usage

<!-- UsageSnippet language="python" operationID="MetricsExportService_TestMetricsExportConnection" method="post" path="/textql.rpc.public.metrics_export.MetricsExportService/TestMetricsExportConnection" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.metrics_exports.test_connection()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `otlp_endpoint`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `otlp_headers`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `otlp_protocol`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MetricsExportServiceTestMetricsExportConnectionResponse](../../models/metricsexportservicetestmetricsexportconnectionresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## trigger_push

TriggerMetricsPush

### Example Usage

<!-- UsageSnippet language="python" operationID="MetricsExportService_TriggerMetricsPush" method="post" path="/textql.rpc.public.metrics_export.MetricsExportService/TriggerMetricsPush" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.metrics_exports.trigger_push(body={})

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