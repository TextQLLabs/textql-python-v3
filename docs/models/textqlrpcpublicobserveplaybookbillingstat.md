# TextqlRPCPublicObservePlaybookBillingStat


## Fields

| Field                                     | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `playbook_id`                             | *Optional[str]*                           | :heavy_minus_sign:                        | N/A                                       |
| `playbook_name`                           | *Optional[str]*                           | :heavy_minus_sign:                        | N/A                                       |
| `owner_id`                                | *Optional[str]*                           | :heavy_minus_sign:                        | N/A                                       |
| `owner_name`                              | *Optional[str]*                           | :heavy_minus_sign:                        | N/A                                       |
| `total_acu`                               | *Optional[float]*                         | :heavy_minus_sign:                        | llm_tokens, compute_hours, cell_execution |
| `llm_acu`                                 | *Optional[float]*                         | :heavy_minus_sign:                        | chat, feed, observability                 |
| `compute_acu`                             | *Optional[float]*                         | :heavy_minus_sign:                        | N/A                                       |
| `run_count`                               | *Optional[int]*                           | :heavy_minus_sign:                        | N/A                                       |
| `daily_run_counts`                        | List[*int*]                               | :heavy_minus_sign:                        | N/A                                       |
| `is_active`                               | *Optional[bool]*                          | :heavy_minus_sign:                        | N/A                                       |