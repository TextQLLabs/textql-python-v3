# TextqlRPCPublicConnectorSupabaseMetadata

KdbMetadata configures a kdb+ (kx/q) connector. kdb+ speaks its own binary IPC
 protocol (not SQL), so queries are qSQL strings; see pkg/connectors/kdbipc.


## Fields

| Field                            | Type                             | Required                         | Description                      |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `host`                           | *Optional[str]*                  | :heavy_minus_sign:               | N/A                              |
| `port`                           | *Optional[int]*                  | :heavy_minus_sign:               | N/A                              |
| `user`                           | *Optional[str]*                  | :heavy_minus_sign:               | N/A                              |
| `password`                       | *Optional[str]*                  | :heavy_minus_sign:               | N/A                              |
| `database`                       | *Optional[str]*                  | :heavy_minus_sign:               | N/A                              |
| `schemas`                        | List[*str*]                      | :heavy_minus_sign:               | SSH tunnel / bastion host fields |
| `dialect`                        | *Optional[str]*                  | :heavy_minus_sign:               | N/A                              |
| `ssl_mode`                       | *Optional[bool]*                 | :heavy_minus_sign:               | N/A                              |