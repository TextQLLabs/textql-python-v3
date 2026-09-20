# TextqlRPCPublicObserveGetCustomTopicThreadsRequest


## Fields

| Field                                      | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `topic_id`                                 | *Optional[str]*                            | :heavy_minus_sign:                         | N/A                                        |
| `verdict`                                  | *Optional[str]*                            | :heavy_minus_sign:                         | 'tagged' (default) \| 'excluded_manual'    |
| `page_token`                               | *Optional[str]*                            | :heavy_minus_sign:                         | N/A                                        |
| `page_size`                                | *Optional[int]*                            | :heavy_minus_sign:                         | N/A                                        |
| `member_id`                                | *Optional[str]*                            | :heavy_minus_sign:                         | only threads owned by this member when set |