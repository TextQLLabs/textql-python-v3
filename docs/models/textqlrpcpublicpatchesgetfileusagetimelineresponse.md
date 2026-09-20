# TextqlRPCPublicPatchesGetFileUsageTimelineResponse


## Fields

| Field                                                                                                  | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `days`                                                                                                 | List[[models.TextqlRPCPublicPatchesDailyFileUsage](../models/textqlrpcpublicpatchesdailyfileusage.md)] | :heavy_minus_sign:                                                                                     | one entry per UTC day in the window, oldest first; idle days zero-filled                               |