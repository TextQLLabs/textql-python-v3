# TextqlRPCPublicCellsAppCell


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `action`                                                  | *Optional[str]*                                           | :heavy_minus_sign:                                        | N/A                                                       |
| `app_id`                                                  | *Optional[str]*                                           | :heavy_minus_sign:                                        | "sql" \| "python"                                         |
| `name`                                                    | *Optional[str]*                                           | :heavy_minus_sign:                                        | Produced dataframe name, if applicable                    |
| `error_message`                                           | *OptionalNullable[str]*                                   | :heavy_minus_sign:                                        | SQL only: connector ID; display name resolves client-side |
| `screenshot_url`                                          | *OptionalNullable[str]*                                   | :heavy_minus_sign:                                        | SQL only: referenced tables                               |
| `last_run_at`                                             | *OptionalNullable[str]*                                   | :heavy_minus_sign:                                        | upstream cell(s), for graph lineage                       |
| `build_line_count`                                        | *OptionalNullable[int]*                                   | :heavy_minus_sign:                                        | N/A                                                       |
| `build_file_count`                                        | *OptionalNullable[int]*                                   | :heavy_minus_sign:                                        | N/A                                                       |