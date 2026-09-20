# TextqlRPCPublicObserveGetChatTopicsResponse


## Fields

| Field                                                                                                     | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `topics_by_chat`                                                                                          | Dict[str, [models.TextqlRPCPublicObserveChatTopicList](../models/textqlrpcpublicobservechattopiclist.md)] | :heavy_minus_sign:                                                                                        | Keyed by chat id; chats with no tagged topics are absent.                                                 |