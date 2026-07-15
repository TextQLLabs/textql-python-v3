# Tableaus

## Overview

### Available Operations

* [list_workbooks](#list_workbooks) - List Tableau workbooks

## list_workbooks

List Tableau workbooks

### Example Usage

<!-- UsageSnippet language="python" operationID="TableauService_ListTableauWorkbooks" method="post" path="/textql.rpc.public.tableau.TableauService/ListTableauWorkbooks" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.tableaus.list_workbooks()

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