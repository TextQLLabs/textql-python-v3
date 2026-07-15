# TextqlRPCPublicAppSetFavoriteRequest


## Fields

| Field                                   | Type                                    | Required                                | Description                             |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| `primitive_type`                        | *Optional[str]*                         | :heavy_minus_sign:                      | 'app' \| 'dashboard'                    |
| `primitive_id`                          | *Optional[str]*                         | :heavy_minus_sign:                      | N/A                                     |
| `favorited`                             | *Optional[bool]*                        | :heavy_minus_sign:                      | true = pin, false = unpin (hard delete) |