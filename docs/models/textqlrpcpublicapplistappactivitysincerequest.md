# TextqlRPCPublicAppListAppActivitySinceRequest


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `app_id`                                           | *Optional[str]*                                    | :heavy_minus_sign:                                 | N/A                                                |
| `scope`                                            | *OptionalNullable[str]*                            | :heavy_minus_sign:                                 | N/A                                                |
| `after_seq`                                        | [Optional[models.AfterSeq]](../models/afterseq.md) | :heavy_minus_sign:                                 | N/A                                                |
| `limit`                                            | *Optional[int]*                                    | :heavy_minus_sign:                                 | server clamps to 200; <=0 means default            |