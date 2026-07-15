# TextqlRPCPublicDatasetGetDatasetValuesRequest


## Fields

| Field                     | Type                      | Required                  | Description               |
| ------------------------- | ------------------------- | ------------------------- | ------------------------- |
| `dataset_id`              | *Optional[str]*           | :heavy_minus_sign:        | N/A                       |
| `version_id`              | *OptionalNullable[int]*   | :heavy_minus_sign:        | default to latest version |
| `limit`                   | *OptionalNullable[int]*   | :heavy_minus_sign:        | defaults to 10,000        |
| `page`                    | *OptionalNullable[int]*   | :heavy_minus_sign:        | N/A                       |
| `sheet`                   | *OptionalNullable[int]*   | :heavy_minus_sign:        | for multi-sheet excels    |