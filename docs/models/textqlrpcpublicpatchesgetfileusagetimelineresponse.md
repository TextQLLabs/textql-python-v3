# TextqlRPCPublicPatchesGetFileUsageTimelineResponse


## Fields

| Field                                                                                                  | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `days`                                                                                                 | List[[models.TextqlRPCPublicPatchesDailyFileUsage](../models/textqlrpcpublicpatchesdailyfileusage.md)] | :heavy_minus_sign:                                                                                     | most recent pull or run (imports included) inside the window; unset when<br/> the file had no usage at all |