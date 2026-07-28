# TextqlRPCPublicAppListAppVersionsResponse

AppFile is one non-entry file of a multi-file app tree; code remains the entry index.html.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `versions`                                                                             | List[[models.TextqlRPCPublicAppAppVersion](../models/textqlrpcpublicappappversion.md)] | :heavy_minus_sign:                                                                     | normalized relative path, forward slashes, no .. or leading /                          |
| `total_count`                                                                          | *Optional[int]*                                                                        | :heavy_minus_sign:                                                                     | N/A                                                                                    |