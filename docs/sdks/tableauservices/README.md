# TableauServices

## Overview

### Available Operations

* [get_collection_thumbnail](#get_collection_thumbnail) - Get collection thumbnail (first view image)
* [get_connected_app_status](#get_connected_app_status) - GetConnectedAppStatus
* [list_tableau_datasources](#list_tableau_datasources) - List Tableau datasources
* [reset_connected_app](#reset_connected_app) - ResetConnectedApp
* [unstar_tableau_item](#unstar_tableau_item) - UnstarTableauItem

## get_collection_thumbnail

Get collection thumbnail (first view image)

### Example Usage

<!-- UsageSnippet language="python" operationID="TableauService_GetCollectionThumbnail" method="post" path="/textql.rpc.public.tableau.TableauService/GetCollectionThumbnail" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.tableau_services.get_collection_thumbnail()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dataset_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TableauServiceGetCollectionThumbnailResponse](../../models/tableauservicegetcollectionthumbnailresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_connected_app_status

GetConnectedAppStatus

### Example Usage

<!-- UsageSnippet language="python" operationID="TableauService_GetConnectedAppStatus" method="post" path="/textql.rpc.public.tableau.TableauService/GetConnectedAppStatus" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.tableau_services.get_connected_app_status()

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

**[models.TableauServiceGetConnectedAppStatusResponse](../../models/tableauservicegetconnectedappstatusresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_tableau_datasources

List Tableau datasources

### Example Usage

<!-- UsageSnippet language="python" operationID="TableauService_ListTableauDatasources" method="post" path="/textql.rpc.public.tableau.TableauService/ListTableauDatasources" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.tableau_services.list_tableau_datasources(body={
        "project_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                         | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                            | [models.TextqlRPCPublicTableauListTableauDatasourcesRequest](../../models/textqlrpcpublictableaulisttableaudatasourcesrequest.md) | :heavy_check_mark:                                                                                                                | N/A                                                                                                                               |
| `connect_timeout_ms`                                                                                                              | *Optional[float]*                                                                                                                 | :heavy_minus_sign:                                                                                                                | N/A                                                                                                                               |
| `retries`                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                  | :heavy_minus_sign:                                                                                                                | Configuration to override the default retry behavior of the client.                                                               |

### Response

**[models.TableauServiceListTableauDatasourcesResponse](../../models/tableauservicelisttableaudatasourcesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## reset_connected_app

ResetConnectedApp

### Example Usage

<!-- UsageSnippet language="python" operationID="TableauService_ResetConnectedApp" method="post" path="/textql.rpc.public.tableau.TableauService/ResetConnectedApp" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.tableau_services.reset_connected_app()

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

**[models.TableauServiceResetConnectedAppResponse](../../models/tableauserviceresetconnectedappresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## unstar_tableau_item

UnstarTableauItem

### Example Usage

<!-- UsageSnippet language="python" operationID="TableauService_UnstarTableauItem" method="post" path="/textql.rpc.public.tableau.TableauService/UnstarTableauItem" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.tableau_services.unstar_tableau_item()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                            | *Optional[float]*                                                                                               | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `connector_id`                                                                                                  | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `item_type`                                                                                                     | [Optional[models.TextqlRPCPublicTableauTableauItemType]](../../models/textqlrpcpublictableautableauitemtype.md) | :heavy_minus_sign:                                                                                              | Starred items                                                                                                   |
| `item_id`                                                                                                       | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.TableauServiceUnstarTableauItemResponse](../../models/tableauserviceunstartableauitemresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |