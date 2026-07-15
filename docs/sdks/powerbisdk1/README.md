# Powerbi

## Overview

### Available Operations

* [generate_embed_token](#generate_embed_token) - GeneratePowerBIEmbedToken
* [get_dataset_preview](#get_dataset_preview) - GetPowerBIDatasetPreview
* [list_workspaces](#list_workspaces) - ListPowerBIWorkspaces

## generate_embed_token

GeneratePowerBIEmbedToken

### Example Usage

<!-- UsageSnippet language="python" operationID="PowerBIService_GeneratePowerBIEmbedToken" method="post" path="/textql.rpc.public.powerbi.PowerBIService/GeneratePowerBIEmbedToken" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.powerbi.generate_embed_token()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `connector_id`                                                      | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `workspace_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `report_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dataset_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PowerBIServiceGeneratePowerBIEmbedTokenResponse](../../models/powerbiservicegeneratepowerbiembedtokenresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_dataset_preview

GetPowerBIDatasetPreview

### Example Usage

<!-- UsageSnippet language="python" operationID="PowerBIService_GetPowerBIDatasetPreview" method="post" path="/textql.rpc.public.powerbi.PowerBIService/GetPowerBIDatasetPreview" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.powerbi.get_dataset_preview()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `connector_id`                                                      | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `workspace_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dataset_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dataset_name`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PowerBIServiceGetPowerBIDatasetPreviewResponse](../../models/powerbiservicegetpowerbidatasetpreviewresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_workspaces

ListPowerBIWorkspaces

### Example Usage

<!-- UsageSnippet language="python" operationID="PowerBIService_ListPowerBIWorkspaces" method="post" path="/textql.rpc.public.powerbi.PowerBIService/ListPowerBIWorkspaces" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.powerbi.list_workspaces()

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

**[models.PowerBIServiceListPowerBIWorkspacesResponse](../../models/powerbiservicelistpowerbiworkspacesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |