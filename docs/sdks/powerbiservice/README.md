# PowerBiService

## Overview

### Available Operations

* [test_connection](#test_connection) - TestPowerBIConnection

## test_connection

TestPowerBIConnection

### Example Usage

<!-- UsageSnippet language="python" operationID="PowerBIService_TestPowerBIConnection" method="post" path="/textql.rpc.public.powerbi.PowerBIService/TestPowerBIConnection" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.power_bi_service.test_connection()

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