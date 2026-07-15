# TextqlRPCPublicObserveMemberBillingStat


## Fields

| Field                                     | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `member_id`                               | *Optional[str]*                           | :heavy_minus_sign:                        | N/A                                       |
| `member_name`                             | *Optional[str]*                           | :heavy_minus_sign:                        | N/A                                       |
| `email`                                   | *Optional[str]*                           | :heavy_minus_sign:                        | N/A                                       |
| `total_acu`                               | *Optional[float]*                         | :heavy_minus_sign:                        | N/A                                       |
| `acu_by_category`                         | Dict[str, *float*]                        | :heavy_minus_sign:                        | llm_tokens, compute_hours, cell_execution |
| `acu_by_source`                           | Dict[str, *float*]                        | :heavy_minus_sign:                        | chat, feed, observability                 |
| `profile_image_url`                       | *Optional[str]*                           | :heavy_minus_sign:                        | N/A                                       |
| `thread_count`                            | *Optional[int]*                           | :heavy_minus_sign:                        | N/A                                       |
| `playbook_count`                          | *Optional[int]*                           | :heavy_minus_sign:                        | N/A                                       |
| `dashboard_count`                         | *Optional[int]*                           | :heavy_minus_sign:                        | N/A                                       |
| `agent_count`                             | *Optional[int]*                           | :heavy_minus_sign:                        | N/A                                       |
| `is_former_member`                        | *Optional[bool]*                          | :heavy_minus_sign:                        | N/A                                       |