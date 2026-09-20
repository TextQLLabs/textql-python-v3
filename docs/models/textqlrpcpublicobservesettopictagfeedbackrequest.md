# TextqlRPCPublicObserveSetTopicTagFeedbackRequest


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `topic_id`                                       | *Optional[str]*                                  | :heavy_minus_sign:                               | N/A                                              |
| `chat_id`                                        | *Optional[str]*                                  | :heavy_minus_sign:                               | N/A                                              |
| `excluded`                                       | *Optional[bool]*                                 | :heavy_minus_sign:                               | false restores verdict='tagged'                  |
| `reason`                                         | *Optional[str]*                                  | :heavy_minus_sign:                               | optional; fed to the judge as a negative example |