# TextqlRPCPublicConnectorMicrosoft365Metadata


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `tenant_id`                                                    | *Optional[str]*                                                | :heavy_minus_sign:                                             | N/A                                                            |
| `client_id`                                                    | *Optional[str]*                                                | :heavy_minus_sign:                                             | N/A                                                            |
| `client_secret`                                                | *Optional[str]*                                                | :heavy_minus_sign:                                             | N/A                                                            |
| `access_token`                                                 | *Optional[str]*                                                | :heavy_minus_sign:                                             | N/A                                                            |
| `refresh_token`                                                | *Optional[str]*                                                | :heavy_minus_sign:                                             | N/A                                                            |
| `member_id`                                                    | *Optional[str]*                                                | :heavy_minus_sign:                                             | N/A                                                            |
| `token_expiry`                                                 | *Optional[str]*                                                | :heavy_minus_sign:                                             | ISO 8601 timestamp                                             |
| `metadata_only`                                                | *Optional[bool]*                                               | :heavy_minus_sign:                                             | When true, only email metadata is accessible (no body content) |
| `scopes`                                                       | List[*str*]                                                    | :heavy_minus_sign:                                             | N/A                                                            |