# TextqlRPCPublicCellsOrgMemberRef

FormCell is the v2 form editor cell. It only references a form_v5 row by id;
 the frontend loads the full form via FormService (no chat-cell scanning). The
 cached fields let the inline chat cell render without a round-trip.


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `email`                                            | *Optional[str]*                                    | :heavy_minus_sign:                                 | list \| info \| create \| edit \| view \| update \| test |
| `name`                                             | *Optional[str]*                                    | :heavy_minus_sign:                                 | N/A                                                |