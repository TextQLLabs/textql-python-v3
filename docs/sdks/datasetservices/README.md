# DatasetServices

## Overview

### Available Operations

* [create_power_bi_dataset](#create_power_bi_dataset) - CreatePowerBIDataset
* [create_tableau_dataset](#create_tableau_dataset) - Create Tableau dataset from views/datasources
* [get_dataset_values](#get_dataset_values) - GetDatasetValues

## create_power_bi_dataset

CreatePowerBIDataset

### Example Usage

<!-- UsageSnippet language="python" operationID="DatasetService_CreatePowerBIDataset" method="post" path="/textql.rpc.public.dataset.DatasetService/CreatePowerBIDataset" -->
```python
from textql_sdk import TextQL
from textql_sdk.utils import parse_datetime


with TextQL() as text_ql:

    res = text_ql.dataset_services.create_power_bi_dataset(reports=[
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
from textql_sdk import TextQL
from textql_sdk.utils import parse_datetime


with TextQL() as text_ql:

    res = text_ql.dataset_services.create_tableau_dataset(views=[
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

## get_dataset_values

GetDatasetValues

### Example Usage

<!-- UsageSnippet language="python" operationID="DatasetService_GetDatasetValues" method="post" path="/textql.rpc.public.dataset.DatasetService/GetDatasetValues" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.dataset_services.get_dataset_values()

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