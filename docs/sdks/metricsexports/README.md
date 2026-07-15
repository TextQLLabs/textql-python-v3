# MetricsExports

## Overview

### Available Operations

* [configure](#configure) - ConfigureMetricsExport
* [test_connection](#test_connection) - TestMetricsExportConnection

## configure

ConfigureMetricsExport

### Example Usage

<!-- UsageSnippet language="python" operationID="MetricsExportService_ConfigureMetricsExport" method="post" path="/textql.rpc.public.metrics_export.MetricsExportService/ConfigureMetricsExport" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.metrics_exports.configure()

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

## test_connection

TestMetricsExportConnection

### Example Usage

<!-- UsageSnippet language="python" operationID="MetricsExportService_TestMetricsExportConnection" method="post" path="/textql.rpc.public.metrics_export.MetricsExportService/TestMetricsExportConnection" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.metrics_exports.test_connection()

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