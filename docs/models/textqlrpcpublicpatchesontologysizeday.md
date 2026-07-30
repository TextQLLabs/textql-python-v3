# TextqlRPCPublicPatchesOntologySizeDay

FileChatUsage is one chat that retrieved a ontology file inside the
 observation window. Only pulls attributed to a chat are listed — background
 or sandbox reads carry no chat id and are excluded.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `date_`                                                                                | [Optional[models.TextqlRPCPublicPatchesDate]](../models/textqlrpcpublicpatchesdate.md) | :heavy_minus_sign:                                                                     | N/A                                                                                    |
| `total_bytes`                                                                          | [Optional[models.TotalBytes]](../models/totalbytes.md)                                 | :heavy_minus_sign:                                                                     | empty for untitled chats                                                               |
| `file_count`                                                                           | *Optional[int]*                                                                        | :heavy_minus_sign:                                                                     | N/A                                                                                    |