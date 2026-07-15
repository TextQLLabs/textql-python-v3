# Tableau

## Overview

### Available Operations

* [generate_embed_token](#generate_embed_token) - Generate JWT token for embedding views
* [get_collection_thumbnail](#get_collection_thumbnail) - Get collection thumbnail (first view image)
* [get_connected_app_status](#get_connected_app_status) - GetConnectedAppStatus
* [get_starred_items](#get_starred_items) - GetStarredTableauItems
* [list_tableau_datasources](#list_tableau_datasources) - List Tableau datasources
* [list_projects](#list_projects) - List Tableau projects
* [list_views](#list_views) - List Tableau views
* [list_workbooks](#list_workbooks) - List Tableau workbooks
* [refresh_collection](#refresh_collection) - RefreshTableauCollection
* [reset_connected_app](#reset_connected_app) - ResetConnectedApp
* [star_item](#star_item) - Star/unstar items
* [test_tableau_connection](#test_tableau_connection) - Test a Tableau connection
* [unstar_tableau_item](#unstar_tableau_item) - UnstarTableauItem

## generate_embed_token

Generate JWT token for embedding views

### Example Usage

<!-- UsageSnippet language="python" operationID="TableauService_GenerateEmbedToken" method="post" path="/textql.rpc.public.tableau.TableauService/GenerateEmbedToken" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.tableau.generate_embed_token()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `connector_id`                                                      | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `view_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TableauServiceGenerateEmbedTokenResponse](../../models/tableauservicegenerateembedtokenresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_collection_thumbnail

Get collection thumbnail (first view image)

### Example Usage

<!-- UsageSnippet language="python" operationID="TableauService_GetCollectionThumbnail" method="post" path="/textql.rpc.public.tableau.TableauService/GetCollectionThumbnail" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.tableau.get_collection_thumbnail()

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

    res = text_ql.tableau.get_connected_app_status()

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

## get_starred_items

GetStarredTableauItems

### Example Usage

<!-- UsageSnippet language="python" operationID="TableauService_GetStarredTableauItems" method="post" path="/textql.rpc.public.tableau.TableauService/GetStarredTableauItems" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.tableau.get_starred_items()

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

**[models.TableauServiceGetStarredTableauItemsResponse](../../models/tableauservicegetstarredtableauitemsresponse.md)**

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

    res = text_ql.tableau.list_tableau_datasources(body={
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

## list_projects

List Tableau projects

### Example Usage

<!-- UsageSnippet language="python" operationID="TableauService_ListTableauProjects" method="post" path="/textql.rpc.public.tableau.TableauService/ListTableauProjects" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.tableau.list_projects()

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

**[models.TableauServiceListTableauProjectsResponse](../../models/tableauservicelisttableauprojectsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_views

List Tableau views

### Example Usage

<!-- UsageSnippet language="python" operationID="TableauService_ListTableauViews" method="post" path="/textql.rpc.public.tableau.TableauService/ListTableauViews" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.tableau.list_views()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `connector_id`                                                      | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `workbook_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `workbook_name`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TableauServiceListTableauViewsResponse](../../models/tableauservicelisttableauviewsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_workbooks

List Tableau workbooks

### Example Usage

<!-- UsageSnippet language="python" operationID="TableauService_ListTableauWorkbooks" method="post" path="/textql.rpc.public.tableau.TableauService/ListTableauWorkbooks" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.tableau.list_workbooks()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `connector_id`                                                      | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `project_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `project_name`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TableauServiceListTableauWorkbooksResponse](../../models/tableauservicelisttableauworkbooksresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## refresh_collection

RefreshTableauCollection

### Example Usage

<!-- UsageSnippet language="python" operationID="TableauService_RefreshTableauCollection" method="post" path="/textql.rpc.public.tableau.TableauService/RefreshTableauCollection" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.tableau.refresh_collection()

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

**[models.TableauServiceRefreshTableauCollectionResponse](../../models/tableauservicerefreshtableaucollectionresponse.md)**

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

    res = text_ql.tableau.reset_connected_app()

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

## star_item

Star/unstar items

### Example Usage

<!-- UsageSnippet language="python" operationID="TableauService_StarTableauItem" method="post" path="/textql.rpc.public.tableau.TableauService/StarTableauItem" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.tableau.star_item()

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
| `item_name`                                                                                                     | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.TableauServiceStarTableauItemResponse](../../models/tableauservicestartableauitemresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## test_tableau_connection

Test a Tableau connection

### Example Usage

<!-- UsageSnippet language="python" operationID="TableauService_TestTableauConnection" method="post" path="/textql.rpc.public.tableau.TableauService/TestTableauConnection" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.tableau.test_tableau_connection()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `connector_id`                                                      | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `server_url`                                                        | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `site_name`                                                         | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `pat_name`                                                          | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `pat_secret`                                                        | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TableauServiceTestTableauConnectionResponse](../../models/tableauservicetesttableauconnectionresponse.md)**

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

    res = text_ql.tableau.unstar_tableau_item()

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