# TextqlRPCPublicCellsCitationLineageNode


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `cell_id`                                                 | *Optional[str]*                                           | :heavy_minus_sign:                                        | N/A                                                       |
| `kind`                                                    | *Optional[str]*                                           | :heavy_minus_sign:                                        | "sql" \| "python"                                         |
| `dataframe_name`                                          | *OptionalNullable[str]*                                   | :heavy_minus_sign:                                        | Produced dataframe name, if applicable                    |
| `connector_id`                                            | *OptionalNullable[int]*                                   | :heavy_minus_sign:                                        | SQL only: connector ID; display name resolves client-side |
| `tables`                                                  | List[*str*]                                               | :heavy_minus_sign:                                        | SQL only: referenced tables                               |
| `input_cell_ids`                                          | List[*str*]                                               | :heavy_minus_sign:                                        | upstream cell(s), for graph lineage                       |