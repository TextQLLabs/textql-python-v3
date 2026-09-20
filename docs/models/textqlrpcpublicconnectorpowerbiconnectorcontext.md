# TextqlRPCPublicConnectorPowerBIConnectorContext


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `report_ids`                                                        | List[*str*]                                                         | :heavy_minus_sign:                                                  | PowerBI report IDs                                                  |
| `dataset_ids`                                                       | List[*str*]                                                         | :heavy_minus_sign:                                                  | PowerBI dataset IDs (PowerBI datasets, not internal dataset_source) |
| `collection_ids`                                                    | List[*str*]                                                         | :heavy_minus_sign:                                                  | workspace dataset_source IDs (cache key, like Tableau collections)  |