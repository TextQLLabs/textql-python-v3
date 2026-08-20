# TextqlRPCPublicSandboxQuerySandboxExecuteBashResponse


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `stdout`                                                    | *Optional[str]*                                             | :heavy_minus_sign:                                          | N/A                                                         |
| `stderr`                                                    | *Optional[str]*                                             | :heavy_minus_sign:                                          | N/A                                                         |
| `exit_code`                                                 | *Optional[int]*                                             | :heavy_minus_sign:                                          | N/A                                                         |
| `error`                                                     | *Optional[str]*                                             | :heavy_minus_sign:                                          | non-empty on execution-level failure (timeout, spawn error) |
| `refreshed_token`                                           | *OptionalNullable[str]*                                     | :heavy_minus_sign:                                          | N/A                                                         |