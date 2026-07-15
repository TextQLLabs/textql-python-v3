# Connectors

## Overview

### Available Operations

* [create](#create) - CreateConnector
* [delete](#delete) - DeleteConnector
* [duplicate_connector](#duplicate_connector) - DuplicateConnector
* [execute_query](#execute_query) - ExecuteQuery
* [get](#get) - GetConnector
* [get_connector_cell_durations](#get_connector_cell_durations) - GetConnectorCellDurations
* [get_chats](#get_chats) - GetConnectorChats
* [get_dashboards](#get_dashboards) - GetConnectorDashboards
* [get_connector_stats](#get_connector_stats) - GetConnectorStats
* [get_usage](#get_usage) - GetConnectorUsage
* [get_connectors](#get_connectors) - GetConnectors
* [get_example_queries](#get_example_queries) - GetExampleQueries
* [get_table_preview](#get_table_preview) - GetTablePreview
* [list_tables](#list_tables) - ListConnectorTables
* [list_query_templates](#list_query_templates) - ListQueryTemplates
* [test](#test) - TestConnector
* [update](#update) - UpdateConnector

## create

CreateConnector

### Example Usage

<!-- UsageSnippet language="python" operationID="ConnectorService_CreateConnector" method="post" path="/textql.rpc.public.connector.ConnectorService/CreateConnector" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.connectors.create()

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

## delete

DeleteConnector

### Example Usage

<!-- UsageSnippet language="python" operationID="ConnectorService_DeleteConnector" method="post" path="/textql.rpc.public.connector.ConnectorService/DeleteConnector" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.connectors.delete()

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

**[models.ConnectorServiceDeleteConnectorResponse](../../models/connectorservicedeleteconnectorresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## duplicate_connector

DuplicateConnector

### Example Usage

<!-- UsageSnippet language="python" operationID="ConnectorService_DuplicateConnector" method="post" path="/textql.rpc.public.connector.ConnectorService/DuplicateConnector" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.connectors.duplicate_connector()

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

**[models.ConnectorServiceDuplicateConnectorResponse](../../models/connectorserviceduplicateconnectorresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## execute_query

ExecuteQuery

### Example Usage

<!-- UsageSnippet language="python" operationID="ConnectorService_ExecuteQuery" method="post" path="/textql.rpc.public.connector.ConnectorService/ExecuteQuery" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.connectors.execute_query()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `connector_id`                                                      | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `query`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ConnectorServiceExecuteQueryResponse](../../models/connectorserviceexecutequeryresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get

GetConnector

### Example Usage

<!-- UsageSnippet language="python" operationID="ConnectorService_GetConnector" method="post" path="/textql.rpc.public.connector.ConnectorService/GetConnector" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.connectors.get()

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

**[models.ConnectorServiceGetConnectorResponse](../../models/connectorservicegetconnectorresponse.md)**

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

    res = text_ql.connectors.get_connector_cell_durations()

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

## get_chats

GetConnectorChats

### Example Usage

<!-- UsageSnippet language="python" operationID="ConnectorService_GetConnectorChats" method="post" path="/textql.rpc.public.connector.ConnectorService/GetConnectorChats" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.connectors.get_chats()

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

**[models.ConnectorServiceGetConnectorChatsResponse](../../models/connectorservicegetconnectorchatsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_dashboards

GetConnectorDashboards

### Example Usage

<!-- UsageSnippet language="python" operationID="ConnectorService_GetConnectorDashboards" method="post" path="/textql.rpc.public.connector.ConnectorService/GetConnectorDashboards" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.connectors.get_dashboards()

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

## get_connector_stats

GetConnectorStats

### Example Usage

<!-- UsageSnippet language="python" operationID="ConnectorService_GetConnectorStats" method="post" path="/textql.rpc.public.connector.ConnectorService/GetConnectorStats" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.connectors.get_connector_stats()

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

## get_usage

GetConnectorUsage

### Example Usage

<!-- UsageSnippet language="python" operationID="ConnectorService_GetConnectorUsage" method="post" path="/textql.rpc.public.connector.ConnectorService/GetConnectorUsage" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.connectors.get_usage()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `connector_id`                                                      | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `days`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ConnectorServiceGetConnectorUsageResponse](../../models/connectorservicegetconnectorusageresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_connectors

GetConnectors

### Example Usage

<!-- UsageSnippet language="python" operationID="ConnectorService_GetConnectors" method="post" path="/textql.rpc.public.connector.ConnectorService/GetConnectors" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.connectors.get_connectors(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                              | [models.TextqlRPCPublicConnectorGetConnectorsRequest](../../models/textqlrpcpublicconnectorgetconnectorsrequest.md) | :heavy_check_mark:                                                                                                  | N/A                                                                                                                 |
| `connect_timeout_ms`                                                                                                | *Optional[float]*                                                                                                   | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |

### Response

**[models.ConnectorServiceGetConnectorsResponse](../../models/connectorservicegetconnectorsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_example_queries

GetExampleQueries

### Example Usage

<!-- UsageSnippet language="python" operationID="ConnectorService_GetExampleQueries" method="post" path="/textql.rpc.public.connector.ConnectorService/GetExampleQueries" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.connectors.get_example_queries()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                              | *Optional[float]*                                                                                                 | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `connector_contexts`                                                                                              | List[[models.TextqlRPCPublicConnectorConnectorContext](../../models/textqlrpcpublicconnectorconnectorcontext.md)] | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `feature_filter`                                                                                                  | [Optional[models.TextqlRPCPublicConnectorFeatureType]](../../models/textqlrpcpublicconnectorfeaturetype.md)       | :heavy_minus_sign:                                                                                                | Feature types for nudge queries - identifies which feature a query promotes                                       |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[models.ConnectorServiceGetExampleQueriesResponse](../../models/connectorservicegetexamplequeriesresponse.md)**

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

    res = text_ql.connectors.get_table_preview()

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

## list_tables

ListConnectorTables

### Example Usage

<!-- UsageSnippet language="python" operationID="ConnectorService_ListConnectorTables" method="post" path="/textql.rpc.public.connector.ConnectorService/ListConnectorTables" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.connectors.list_tables()

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

**[models.ConnectorServiceListConnectorTablesResponse](../../models/connectorservicelistconnectortablesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_query_templates

ListQueryTemplates

### Example Usage

<!-- UsageSnippet language="python" operationID="ConnectorService_ListQueryTemplates" method="post" path="/textql.rpc.public.connector.ConnectorService/ListQueryTemplates" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.connectors.list_query_templates()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `connector_id`                                                      | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `days`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Optional lookback window in days; 0 or unset means all-time.        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ConnectorServiceListQueryTemplatesResponse](../../models/connectorservicelistquerytemplatesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## test

TestConnector

### Example Usage

<!-- UsageSnippet language="python" operationID="ConnectorService_TestConnector" method="post" path="/textql.rpc.public.connector.ConnectorService/TestConnector" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.connectors.test()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                                                                                        | *Optional[float]*                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                         |
| `config`                                                                                                                                                                                                                    | [Optional[models.TextqlRPCPublicConnectorConnectorConfig]](../../models/textqlrpcpublicconnectorconnectorconfig.md)                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                         |
| `connector_id`                                                                                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                          | Optional: If provided, confidential fields will be preserved from the existing connector<br/> when the corresponding field in config is empty. This allows testing updates without<br/> requiring the user to re-enter credentials. |
| `retries`                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                         |

### Response

**[models.ConnectorServiceTestConnectorResponse](../../models/connectorservicetestconnectorresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## update

UpdateConnector

### Example Usage

<!-- UsageSnippet language="python" operationID="ConnectorService_UpdateConnector" method="post" path="/textql.rpc.public.connector.ConnectorService/UpdateConnector" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.connectors.update()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                | *Optional[float]*                                                                                                   | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `connector_id`                                                                                                      | *Optional[int]*                                                                                                     | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `config`                                                                                                            | [Optional[models.TextqlRPCPublicConnectorConnectorConfig]](../../models/textqlrpcpublicconnectorconnectorconfig.md) | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `allow_sql_write_operations`                                                                                        | *OptionalNullable[bool]*                                                                                            | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `include_db_session_metadata`                                                                                       | *OptionalNullable[bool]*                                                                                            | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |

### Response

**[models.ConnectorServiceUpdateConnectorResponse](../../models/connectorserviceupdateconnectorresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |