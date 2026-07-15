# TableauService

## Overview

### Available Operations

* [refresh_collection](#refresh_collection) - RefreshTableauCollection
* [test_tableau_connection](#test_tableau_connection) - Test a Tableau connection

## refresh_collection

RefreshTableauCollection

### Example Usage

<!-- UsageSnippet language="python" operationID="TableauService_RefreshTableauCollection" method="post" path="/textql.rpc.public.tableau.TableauService/RefreshTableauCollection" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.tableau_service.refresh_collection()

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

## test_tableau_connection

Test a Tableau connection

### Example Usage

<!-- UsageSnippet language="python" operationID="TableauService_TestTableauConnection" method="post" path="/textql.rpc.public.tableau.TableauService/TestTableauConnection" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.tableau_service.test_tableau_connection()

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