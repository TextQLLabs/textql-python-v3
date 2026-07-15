# Connectors

## Overview

### Available Operations

* [delete](#delete) - DeleteConnector
* [get](#get) - GetConnector
* [get_chats](#get_chats) - GetConnectorChats
* [get_usage](#get_usage) - GetConnectorUsage
* [list_tables](#list_tables) - ListConnectorTables
* [test](#test) - TestConnector

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