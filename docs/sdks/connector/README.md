# Connector

## Overview

### Available Operations

* [get_dashboards](#get_dashboards) - GetConnectorDashboards

## get_dashboards

GetConnectorDashboards

### Example Usage

<!-- UsageSnippet language="python" operationID="ConnectorService_GetConnectorDashboards" method="post" path="/textql.rpc.public.connector.ConnectorService/GetConnectorDashboards" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.connector.get_dashboards()

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

**[models.ConnectorServiceGetConnectorDashboardsResponse](../../models/connectorservicegetconnectordashboardsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |