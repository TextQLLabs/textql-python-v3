# TextqlRPCPublicAppListAppsRequest


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `search_term`                                           | *OptionalNullable[str]*                                 | :heavy_minus_sign:                                      | N/A                                                     |
| `limit`                                                 | *Optional[int]*                                         | :heavy_minus_sign:                                      | N/A                                                     |
| `offset`                                                | *Optional[int]*                                         | :heavy_minus_sign:                                      | N/A                                                     |
| `folder_id`                                             | *OptionalNullable[str]*                                 | :heavy_minus_sign:                                      | Filter by specific folder                               |
| `uncategorized_only`                                    | *OptionalNullable[bool]*                                | :heavy_minus_sign:                                      | Only show apps with no folder                           |
| `shared_with_me`                                        | *OptionalNullable[bool]*                                | :heavy_minus_sign:                                      | Only apps shared with the caller (not authored by them) |