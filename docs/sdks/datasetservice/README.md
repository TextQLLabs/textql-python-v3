# DatasetService

## Overview

### Available Operations

* [create_folder](#create_folder) - CreateFolder
* [get_folders](#get_folders) - for AR: CreateFolderACL, UpdateFolderACL, DeleteFolderACL
* [update_dataset](#update_dataset) - Update dataset metadata

## create_folder

CreateFolder

### Example Usage

<!-- UsageSnippet language="python" operationID="DatasetService_CreateFolder" method="post" path="/textql.rpc.public.dataset.DatasetService/CreateFolder" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dataset_service.create_folder()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `parent_path`                                                       | List[*str*]                                                         | :heavy_minus_sign:                                                  | parent folders must already exist                                   |
| `name`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DatasetServiceCreateFolderResponse](../../models/datasetservicecreatefolderresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_folders

for AR: CreateFolderACL, UpdateFolderACL, DeleteFolderACL

### Example Usage

<!-- UsageSnippet language="python" operationID="DatasetService_GetFolders" method="post" path="/textql.rpc.public.dataset.DatasetService/GetFolders" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dataset_service.get_folders()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `path`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DatasetServiceGetFoldersResponse](../../models/datasetservicegetfoldersresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## update_dataset

Update dataset metadata

### Example Usage

<!-- UsageSnippet language="python" operationID="DatasetService_UpdateDataset" method="post" path="/textql.rpc.public.dataset.DatasetService/UpdateDataset" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dataset_service.update_dataset()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dataset_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `name`                                                              | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Add other updatable fields as needed                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DatasetServiceUpdateDatasetResponse](../../models/datasetserviceupdatedatasetresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |