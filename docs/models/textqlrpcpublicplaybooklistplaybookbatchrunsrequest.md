# TextqlRPCPublicPlaybookListPlaybookBatchRunsRequest

Request to list batch runs for a playbook


## Fields

| Field                               | Type                                | Required                            | Description                         |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| `playbook_id`                       | *Optional[str]*                     | :heavy_minus_sign:                  | UUID                                |
| `limit`                             | *OptionalNullable[int]*             | :heavy_minus_sign:                  | Max number of results (default: 50) |
| `offset`                            | *OptionalNullable[int]*             | :heavy_minus_sign:                  | Offset for pagination (default: 0)  |