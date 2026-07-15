# TextqlRPCPublicObserveCustomTopicPerson

One owner of a topic's tagged chats, ranked by how many they own.


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `member_id`                                               | *Optional[str]*                                           | :heavy_minus_sign:                                        | N/A                                                       |
| `name`                                                    | *Optional[str]*                                           | :heavy_minus_sign:                                        | display name; falls back to the email, then the member id |
| `email`                                                   | *Optional[str]*                                           | :heavy_minus_sign:                                        | N/A                                                       |
| `thread_count`                                            | [Optional[models.ThreadCount]](../models/threadcount.md)  | :heavy_minus_sign:                                        | N/A                                                       |