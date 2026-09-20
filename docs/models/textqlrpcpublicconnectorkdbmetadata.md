# TextqlRPCPublicConnectorKdbMetadata

KdbMetadata configures a kdb+ (kx/q) connector. kdb+ speaks its own binary IPC
 protocol (not SQL), so queries are qSQL strings; see pkg/connectors/kdbipc.


## Fields

| Field                            | Type                             | Required                         | Description                      |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `host`                           | *Optional[str]*                  | :heavy_minus_sign:               | N/A                              |
| `port`                           | *Optional[int]*                  | :heavy_minus_sign:               | N/A                              |
| `user`                           | *Optional[str]*                  | :heavy_minus_sign:               | N/A                              |
| `password`                       | *Optional[str]*                  | :heavy_minus_sign:               | N/A                              |
| `tls`                            | *Optional[bool]*                 | :heavy_minus_sign:               | N/A                              |
| `ssh_tunnel_enabled`             | *Optional[bool]*                 | :heavy_minus_sign:               | SSH tunnel / bastion host fields |
| `ssh_host`                       | *Optional[str]*                  | :heavy_minus_sign:               | N/A                              |
| `ssh_port`                       | *Optional[int]*                  | :heavy_minus_sign:               | N/A                              |
| `ssh_user`                       | *Optional[str]*                  | :heavy_minus_sign:               | N/A                              |
| `ssh_private_key`                | *Optional[str]*                  | :heavy_minus_sign:               | N/A                              |
| `ssh_host_public_key`            | *Optional[str]*                  | :heavy_minus_sign:               | N/A                              |