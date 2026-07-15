# Datasets

## Overview

### Available Operations

* [create_upload_presign_url](#create_upload_presign_url) - uploads
* [delete](#delete) - Delete a dataset (soft delete)
* [export](#export) - export dataset in "raw" format – original if dataset is uploaded, converted format otherwise (defaults to CSV)
* [fetch](#fetch) - GetDataset, GetDatasets only return metadata
* [get_stats](#get_stats) - GetDatasetStats
* [get](#get) - GetDatasets
* [get_by_ids](#get_by_ids) - GetDatasetsByIds
* [process_upload_presign_url](#process_upload_presign_url) - ProcessUploadPresignUrl

## create_upload_presign_url

uploads

### Example Usage

<!-- UsageSnippet language="python" operationID="DatasetService_CreateUploadPresignUrl" method="post" path="/textql.rpc.public.dataset.DatasetService/CreateUploadPresignUrl" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.datasets.create_upload_presign_url()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                    | *Optional[float]*                                                                                       | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `type`                                                                                                  | [Optional[models.TextqlRPCPublicDatasetDatasetType]](../../models/textqlrpcpublicdatasetdatasettype.md) | :heavy_minus_sign:                                                                                      | never change the names or numbers of existing dataset types!                                            |
| `file_name`                                                                                             | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `folder_path`                                                                                           | List[*str*]                                                                                             | :heavy_minus_sign:                                                                                      | if this dataset lives in a folder                                                                       |
| `ephemeral`                                                                                             | *Optional[bool]*                                                                                        | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `expires_in_days`                                                                                       | *OptionalNullable[int]*                                                                                 | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.DatasetServiceCreateUploadPresignURLResponse](../../models/datasetservicecreateuploadpresignurlresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete

Delete a dataset (soft delete)

### Example Usage

<!-- UsageSnippet language="python" operationID="DatasetService_DeleteDataset" method="post" path="/textql.rpc.public.dataset.DatasetService/DeleteDataset" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.datasets.delete()

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

**[models.DatasetServiceDeleteDatasetResponse](../../models/datasetservicedeletedatasetresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## export

export dataset in "raw" format – original if dataset is uploaded, converted format otherwise (defaults to CSV)

### Example Usage

<!-- UsageSnippet language="python" operationID="DatasetService_ExportDataset" method="post" path="/textql.rpc.public.dataset.DatasetService/ExportDataset" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.datasets.export()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                      | *Optional[float]*                                                                                         | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `dataset_id`                                                                                              | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `preferred_format`                                                                                        | [Optional[models.TextqlRPCPublicDatasetExportFormat]](../../models/textqlrpcpublicdatasetexportformat.md) | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `version_id`                                                                                              | *OptionalNullable[int]*                                                                                   | :heavy_minus_sign:                                                                                        | default to latest version                                                                                 |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.DatasetServiceExportDatasetResponse](../../models/datasetserviceexportdatasetresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## fetch

GetDataset, GetDatasets only return metadata

### Example Usage

<!-- UsageSnippet language="python" operationID="DatasetService_GetDataset" method="post" path="/textql.rpc.public.dataset.DatasetService/GetDataset" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.datasets.fetch()

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

**[models.DatasetServiceGetDatasetResponse](../../models/datasetservicegetdatasetresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_stats

GetDatasetStats

### Example Usage

<!-- UsageSnippet language="python" operationID="DatasetService_GetDatasetStats" method="post" path="/textql.rpc.public.dataset.DatasetService/GetDatasetStats" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.datasets.get_stats()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dataset_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `version_id`                                                        | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DatasetServiceGetDatasetStatsResponse](../../models/datasetservicegetdatasetstatsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get

GetDatasets

### Example Usage

<!-- UsageSnippet language="python" operationID="DatasetService_GetDatasets" method="post" path="/textql.rpc.public.dataset.DatasetService/GetDatasets" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.datasets.get()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                      | *Optional[float]*                                                                                         | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `types`                                                                                                   | List[[models.TextqlRPCPublicDatasetDatasetType](../../models/textqlrpcpublicdatasetdatasettype.md)]       | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `owner_only`                                                                                              | *Optional[bool]*                                                                                          | :heavy_minus_sign:                                                                                        | only include datasets where the user is the owner                                                         |
| `include_subfolders`                                                                                      | *Optional[bool]*                                                                                          | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `path`                                                                                                    | *OptionalNullable[str]*                                                                                   | :heavy_minus_sign:                                                                                        | defaults to path /                                                                                        |
| `search_param`                                                                                            | *OptionalNullable[str]*                                                                                   | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `sort`                                                                                                    | [Optional[models.TextqlRPCPublicDatasetDatasetsSort]](../../models/textqlrpcpublicdatasetdatasetssort.md) | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `limit`                                                                                                   | *OptionalNullable[int]*                                                                                   | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `cursor`                                                                                                  | *OptionalNullable[str]*                                                                                   | :heavy_minus_sign:                                                                                        | cursor-based pagination. cursor is the id of the last record returned                                     |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.DatasetServiceGetDatasetsResponse](../../models/datasetservicegetdatasetsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_by_ids

GetDatasetsByIds

### Example Usage

<!-- UsageSnippet language="python" operationID="DatasetService_GetDatasetsByIds" method="post" path="/textql.rpc.public.dataset.DatasetService/GetDatasetsByIds" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.datasets.get_by_ids()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dataset_ids`                                                       | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DatasetServiceGetDatasetsByIdsResponse](../../models/datasetservicegetdatasetsbyidsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## process_upload_presign_url

for AR: CreateDatasetACL, UpdateDatasetACL, DeleteDatasetACL

### Example Usage

<!-- UsageSnippet language="python" operationID="DatasetService_ProcessUploadPresignUrl" method="post" path="/textql.rpc.public.dataset.DatasetService/ProcessUploadPresignUrl" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.datasets.process_upload_presign_url()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dataset_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dataset_version`                                                   | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DatasetServiceProcessUploadPresignURLResponse](../../models/datasetserviceprocessuploadpresignurlresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |