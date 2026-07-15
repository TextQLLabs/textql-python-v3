# TextqlRPCPublicAgentAgentRunDeliveryChannel


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `type`                                                                     | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | slack_channel \| teams_channel \| slack_dm \| teams_dm \| email \| feed_channel |
| `id`                                                                       | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | raw identifier (channel id, member id, aad id)                             |
| `label`                                                                    | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | resolved human-readable label (#channel, email address)                    |