# TextqlRPCPublicConnectorMongoDBMetadata


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `host`                                                        | *Optional[str]*                                               | :heavy_minus_sign:                                            | N/A                                                           |
| `port`                                                        | *Optional[int]*                                               | :heavy_minus_sign:                                            | N/A                                                           |
| `user`                                                        | *Optional[str]*                                               | :heavy_minus_sign:                                            | N/A                                                           |
| `password`                                                    | *Optional[str]*                                               | :heavy_minus_sign:                                            | N/A                                                           |
| `database`                                                    | *Optional[str]*                                               | :heavy_minus_sign:                                            | default database to query                                     |
| `auth_source`                                                 | *Optional[str]*                                               | :heavy_minus_sign:                                            | authSource (e.g. "admin"); defaults to database when empty    |
| `tls`                                                         | *Optional[bool]*                                              | :heavy_minus_sign:                                            | N/A                                                           |
| `srv`                                                         | *Optional[bool]*                                              | :heavy_minus_sign:                                            | mongodb+srv connection (Atlas) — host is the cluster DNS name |