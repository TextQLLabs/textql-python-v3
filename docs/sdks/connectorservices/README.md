# ConnectorServices

## Overview

### Available Operations

* [duplicate_connector](#duplicate_connector) - DuplicateConnector
* [execute_query](#execute_query) - ExecuteQuery
* [get_connectors](#get_connectors) - GetConnectors
* [get_example_queries](#get_example_queries) - GetExampleQueries
* [list_query_templates](#list_query_templates) - ListQueryTemplates
* [update](#update) - UpdateConnector

## duplicate_connector

DuplicateConnector

### Example Usage

<!-- UsageSnippet language="python" operationID="ConnectorService_DuplicateConnector" method="post" path="/textql.rpc.public.connector.ConnectorService/DuplicateConnector" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.connector_services.duplicate_connector()

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

    res = text_ql.connector_services.execute_query()

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

## get_connectors

GetConnectors

### Example Usage

<!-- UsageSnippet language="python" operationID="ConnectorService_GetConnectors" method="post" path="/textql.rpc.public.connector.ConnectorService/GetConnectors" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.connector_services.get_connectors(body={})

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

    res = text_ql.connector_services.get_example_queries()

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

## list_query_templates

ListQueryTemplates

### Example Usage

<!-- UsageSnippet language="python" operationID="ConnectorService_ListQueryTemplates" method="post" path="/textql.rpc.public.connector.ConnectorService/ListQueryTemplates" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.connector_services.list_query_templates()

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

## update

UpdateConnector

### Example Usage

<!-- UsageSnippet language="python" operationID="ConnectorService_UpdateConnector" method="post" path="/textql.rpc.public.connector.ConnectorService/UpdateConnector" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.connector_services.update()

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