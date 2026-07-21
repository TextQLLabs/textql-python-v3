# StreamChatEventData

One stream envelope: `result` carries the next cell, `error` reports a failure that ended the stream.


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `result`                                                                         | [Optional[models.TextqlRPCPublicChatCell]](../models/textqlrpcpublicchatcell.md) | :heavy_minus_sign:                                                               | N/A                                                                              |
| `error`                                                                          | [Optional[models.GoogleRPCStatus]](../models/googlerpcstatus.md)                 | :heavy_minus_sign:                                                               | N/A                                                                              |