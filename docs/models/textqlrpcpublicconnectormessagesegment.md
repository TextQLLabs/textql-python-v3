# TextqlRPCPublicConnectorMessageSegment

A segment of an example query message - either plain text or a styled feature word


## Fields

| Field                                                                                                    | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `content`                                                                                                | *Optional[str]*                                                                                          | :heavy_minus_sign:                                                                                       | The text content of this segment                                                                         |
| `feature_type`                                                                                           | [Optional[models.TextqlRPCPublicConnectorFeatureType]](../models/textqlrpcpublicconnectorfeaturetype.md) | :heavy_minus_sign:                                                                                       | Feature types for nudge queries - identifies which feature a query promotes                              |