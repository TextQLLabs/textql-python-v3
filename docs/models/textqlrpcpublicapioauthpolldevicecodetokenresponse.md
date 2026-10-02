# TextqlRPCPublicAPIOauthPollDeviceCodeTokenResponse


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `status`                                                        | *Optional[str]*                                                 | :heavy_minus_sign:                                              | "pending", "slow_down", "success", "expired", "denied", "error" |
| `display_name`                                                  | *Optional[str]*                                                 | :heavy_minus_sign:                                              | only on "success"                                               |
| `error_description`                                             | *Optional[str]*                                                 | :heavy_minus_sign:                                              | N/A                                                             |