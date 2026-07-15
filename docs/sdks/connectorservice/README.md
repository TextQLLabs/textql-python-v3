# ConnectorService

## Overview

### Available Operations

* [create](#create) - CreateConnector
* [get_connector_cell_durations](#get_connector_cell_durations) - GetConnectorCellDurations
* [get_connector_stats](#get_connector_stats) - GetConnectorStats
* [get_table_preview](#get_table_preview) - GetTablePreview

## create

CreateConnector

### Example Usage

<!-- UsageSnippet language="python" operationID="ConnectorService_CreateConnector" method="post" path="/textql.rpc.public.connector.ConnectorService/CreateConnector" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.connector_service.create()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                       | Type                                                                                                                            | Required                                                                                                                        | Description                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                            | *Optional[float]*                                                                                                               | :heavy_minus_sign:                                                                                                              | N/A                                                                                                                             |
| `config`                                                                                                                        | [Optional[models.TextqlRPCPublicConnectorConnectorConfig]](../../models/textqlrpcpublicconnectorconnectorconfig.md)             | :heavy_minus_sign:                                                                                                              | N/A                                                                                                                             |
| `allow_sql_write_operations`                                                                                                    | *OptionalNullable[bool]*                                                                                                        | :heavy_minus_sign:                                                                                                              | N/A                                                                                                                             |
| `include_db_session_metadata`                                                                                                   | *OptionalNullable[bool]*                                                                                                        | :heavy_minus_sign:                                                                                                              | N/A                                                                                                                             |
| `access`                                                                                                                        | [Optional[models.TextqlRPCPublicConnectorConnectorAccessConfig]](../../models/textqlrpcpublicconnectorconnectoraccessconfig.md) | :heavy_minus_sign:                                                                                                              | N/A                                                                                                                             |
| `retries`                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                | :heavy_minus_sign:                                                                                                              | Configuration to override the default retry behavior of the client.                                                             |

### Response

**[models.ConnectorServiceCreateConnectorResponse](../../models/connectorservicecreateconnectorresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_connector_cell_durations

GetConnectorCellDurations

### Example Usage

<!-- UsageSnippet language="python" operationID="ConnectorService_GetConnectorCellDurations" method="post" path="/textql.rpc.public.connector.ConnectorService/GetConnectorCellDurations" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.connector_service.get_connector_cell_durations()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `connector_id`                                                      | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `days`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ConnectorServiceGetConnectorCellDurationsResponse](../../models/connectorservicegetconnectorcelldurationsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_connector_stats

GetConnectorStats

### Example Usage

<!-- UsageSnippet language="python" operationID="ConnectorService_GetConnectorStats" method="post" path="/textql.rpc.public.connector.ConnectorService/GetConnectorStats" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.connector_service.get_connector_stats()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `days`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | 0 = all-time                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ConnectorServiceGetConnectorStatsResponse](../../models/connectorservicegetconnectorstatsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_table_preview

GetTablePreview

### Example Usage

<!-- UsageSnippet language="python" operationID="ConnectorService_GetTablePreview" method="post" path="/textql.rpc.public.connector.ConnectorService/GetTablePreview" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.connector_service.get_table_preview()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `connector_id`                                                      | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `table_database`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `table_schema`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `table_name`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ConnectorServiceGetTablePreviewResponse](../../models/connectorservicegettablepreviewresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |