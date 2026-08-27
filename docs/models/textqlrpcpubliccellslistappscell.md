# TextqlRPCPublicCellsListAppsCell

create_design_system tool: authors/edits an org Data App design system.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `search_term`                                                                        | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | create \| edit                                                                       |
| `app_id`                                                                             | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | N/A                                                                                  |
| `total_count`                                                                        | *Optional[int]*                                                                      | :heavy_minus_sign:                                                                   | N/A                                                                                  |
| `error_message`                                                                      | *OptionalNullable[str]*                                                              | :heavy_minus_sign:                                                                   | in-product viewer route                                                              |
| `apps`                                                                               | List[[models.TextqlRPCPublicCellsAppInfo](../models/textqlrpcpubliccellsappinfo.md)] | :heavy_minus_sign:                                                                   | N/A                                                                                  |