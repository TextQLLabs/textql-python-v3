# Tableau

## Overview

### Available Operations

* [generate_embed_token](#generate_embed_token) - Generate JWT token for embedding views
* [get_starred_items](#get_starred_items) - GetStarredTableauItems
* [list_projects](#list_projects) - List Tableau projects
* [list_views](#list_views) - List Tableau views
* [star_item](#star_item) - Star/unstar items

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