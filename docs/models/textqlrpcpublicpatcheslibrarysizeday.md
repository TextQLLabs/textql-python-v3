# TextqlRPCPublicPatchesLibrarySizeDay

LibrarySizeDay is the library's total content size as of the end of one UTC
 day, sampled from git history (the last commit on or before that day).


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `date_`                                                                                | [Optional[models.TextqlRPCPublicPatchesDate]](../models/textqlrpcpublicpatchesdate.md) | :heavy_minus_sign:                                                                     | copied from google.type.Date; not available in buf's google/protobuf/*                 |
| `total_bytes`                                                                          | [Optional[models.TotalBytes]](../models/totalbytes.md)                                 | :heavy_minus_sign:                                                                     | N/A                                                                                    |
| `file_count`                                                                           | *Optional[int]*                                                                        | :heavy_minus_sign:                                                                     | N/A                                                                                    |