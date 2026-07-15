# Datasets

## Overview

### Available Operations

* [create_folder](#create_folder) - CreateFolder
* [create_power_bi_dataset](#create_power_bi_dataset) - CreatePowerBIDataset
* [create_tableau_dataset](#create_tableau_dataset) - Create Tableau dataset from views/datasources
* [create_upload_presign_url](#create_upload_presign_url) - uploads
* [delete](#delete) - Delete a dataset (soft delete)
* [export](#export) - export dataset in "raw" format – original if dataset is uploaded, converted format otherwise (defaults to CSV)
* [fetch](#fetch) - GetDataset, GetDatasets only return metadata
* [get_stats](#get_stats) - GetDatasetStats
* [get_dataset_values](#get_dataset_values) - GetDatasetValues
* [get](#get) - GetDatasets
* [get_by_ids](#get_by_ids) - GetDatasetsByIds
* [get_folders](#get_folders) - for AR: CreateFolderACL, UpdateFolderACL, DeleteFolderACL
* [process_upload_presign_url](#process_upload_presign_url) - ProcessUploadPresignUrl
* [update_dataset](#update_dataset) - Update dataset metadata

## create_folder

CreateFolder

### Example Usage

<!-- UsageSnippet language="python" operationID="DatasetService_CreateFolder" method="post" path="/textql.rpc.public.dataset.DatasetService/CreateFolder" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.datasets.create_folder()

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

## create_power_bi_dataset

CreatePowerBIDataset

### Example Usage

<!-- UsageSnippet language="python" operationID="DatasetService_CreatePowerBIDataset" method="post" path="/textql.rpc.public.dataset.DatasetService/CreatePowerBIDataset" -->
```python
import os
from textql_sdk import Textql
from textql_sdk.utils import parse_datetime


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.datasets.create_power_bi_dataset(reports=[
        {
            "created_date": parse_datetime("2023-01-15T01:30:15.01Z"),
        },
    ], datasets=[
        {
            "created_date": parse_datetime("2023-01-15T01:30:15.01Z"),
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                      | *Optional[float]*                                                                                         | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `connector_id`                                                                                            | *Optional[int]*                                                                                           | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `name`                                                                                                    | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `folder_path`                                                                                             | List[*str*]                                                                                               | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `workspace_id`                                                                                            | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `workspace_name`                                                                                          | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `reports`                                                                                                 | List[[models.TextqlRPCPublicPowerbiPowerBIReport](../../models/textqlrpcpublicpowerbipowerbireport.md)]   | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `datasets`                                                                                                | List[[models.TextqlRPCPublicPowerbiPowerBIDataset](../../models/textqlrpcpublicpowerbipowerbidataset.md)] | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.DatasetServiceCreatePowerBIDatasetResponse](../../models/datasetservicecreatepowerbidatasetresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## create_tableau_dataset

Create Tableau dataset from views/datasources

### Example Usage

<!-- UsageSnippet language="python" operationID="DatasetService_CreateTableauDataset" method="post" path="/textql.rpc.public.dataset.DatasetService/CreateTableauDataset" -->
```python
import os
from textql_sdk import Textql
from textql_sdk.utils import parse_datetime


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.datasets.create_tableau_dataset(views=[
        {
            "created_at": parse_datetime("2023-01-15T01:30:15.01Z"),
            "updated_at": parse_datetime("2023-01-15T01:30:15.01Z"),
        },
    ], datasources=[
        {
            "created_at": parse_datetime("2023-01-15T01:30:15.01Z"),
            "updated_at": parse_datetime("2023-01-15T01:30:15.01Z"),
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                            | *Optional[float]*                                                                                               | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `connector_id`                                                                                                  | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `name`                                                                                                          | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `folder_path`                                                                                                   | List[*str*]                                                                                                     | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `project_id`                                                                                                    | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `project_name`                                                                                                  | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `views`                                                                                                         | List[[models.TextqlRPCPublicTableauTableauView](../../models/textqlrpcpublictableautableauview.md)]             | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `datasources`                                                                                                   | List[[models.TextqlRPCPublicTableauTableauDatasource](../../models/textqlrpcpublictableautableaudatasource.md)] | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.DatasetServiceCreateTableauDatasetResponse](../../models/datasetservicecreatetableaudatasetresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## create_upload_presign_url

uploads

### Example Usage

<!-- UsageSnippet language="python" operationID="DatasetService_CreateUploadPresignUrl" method="post" path="/textql.rpc.public.dataset.DatasetService/CreateUploadPresignUrl" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.datasets.create_upload_presign_url()

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
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.datasets.delete()

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
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.datasets.export()

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
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.datasets.fetch()

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
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.datasets.get_stats()

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

## get_dataset_values

GetDatasetValues

### Example Usage

<!-- UsageSnippet language="python" operationID="DatasetService_GetDatasetValues" method="post" path="/textql.rpc.public.dataset.DatasetService/GetDatasetValues" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.datasets.get_dataset_values()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dataset_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `version_id`                                                        | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | default to latest version                                           |
| `limit`                                                             | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | defaults to 10,000                                                  |
| `page`                                                              | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `sheet`                                                             | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | for multi-sheet excels                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DatasetServiceGetDatasetValuesResponse](../../models/datasetservicegetdatasetvaluesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get

GetDatasets

### Example Usage

<!-- UsageSnippet language="python" operationID="DatasetService_GetDatasets" method="post" path="/textql.rpc.public.dataset.DatasetService/GetDatasets" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.datasets.get()

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
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.datasets.get_by_ids()

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

## get_folders

for AR: CreateFolderACL, UpdateFolderACL, DeleteFolderACL

### Example Usage

<!-- UsageSnippet language="python" operationID="DatasetService_GetFolders" method="post" path="/textql.rpc.public.dataset.DatasetService/GetFolders" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.datasets.get_folders()

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

## process_upload_presign_url

for AR: CreateDatasetACL, UpdateDatasetACL, DeleteDatasetACL

### Example Usage

<!-- UsageSnippet language="python" operationID="DatasetService_ProcessUploadPresignUrl" method="post" path="/textql.rpc.public.dataset.DatasetService/ProcessUploadPresignUrl" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.datasets.process_upload_presign_url()

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

## update_dataset

Update dataset metadata

### Example Usage

<!-- UsageSnippet language="python" operationID="DatasetService_UpdateDataset" method="post" path="/textql.rpc.public.dataset.DatasetService/UpdateDataset" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.datasets.update_dataset()

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