# TextqlRPCPublicCellsFeedExplorerCell


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `operation`                                     | *Optional[str]*                                 | :heavy_minus_sign:                              | "get_feed", "get_post", "get_comments"          |
| `post_id`                                       | *OptionalNullable[str]*                         | :heavy_minus_sign:                              | N/A                                             |
| `filter_`                                       | *OptionalNullable[str]*                         | :heavy_minus_sign:                              | N/A                                             |
| `limit`                                         | *OptionalNullable[int]*                         | :heavy_minus_sign:                              | N/A                                             |
| `result`                                        | *Optional[str]*                                 | :heavy_minus_sign:                              | JSON-serialized result                          |
| `channel_id`                                    | *OptionalNullable[str]*                         | :heavy_minus_sign:                              | when set, get results for specific feed channel |