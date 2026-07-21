# StreamChatEvent

A successful response.(streaming responses)


## Fields

| Field                                                                                                 | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `data`                                                                                                | [models.StreamChatEventData](../models/streamchateventdata.md)                                        | :heavy_check_mark:                                                                                    | One stream envelope: `result` carries the next cell, `error` reports a failure that ended the stream. |