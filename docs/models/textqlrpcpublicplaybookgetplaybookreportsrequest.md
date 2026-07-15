# TextqlRPCPublicPlaybookGetPlaybookReportsRequest


## Fields

| Field                              | Type                               | Required                           | Description                        |
| ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- |
| `playbook_id`                      | *Optional[str]*                    | :heavy_minus_sign:                 | UUID                               |
| `limit`                            | *Optional[int]*                    | :heavy_minus_sign:                 | N/A                                |
| `offset`                           | *Optional[int]*                    | :heavy_minus_sign:                 | N/A                                |
| `chat_id`                          | *OptionalNullable[str]*            | :heavy_minus_sign:                 | UUID                               |
| `template_data_id`                 | *OptionalNullable[str]*            | :heavy_minus_sign:                 | UUID                               |
| `batch_run_id`                     | *OptionalNullable[str]*            | :heavy_minus_sign:                 | UUID - filter reports by batch run |