# TextqlRPCPublicPatchesValidateConfigResponse

ValidateConfigResponse: ok == true with no diagnostics means functionally valid
 against current org state — not a merge guarantee.


## Fields

| Field                                                                                                      | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `ok`                                                                                                       | *Optional[bool]*                                                                                           | :heavy_minus_sign:                                                                                         | N/A                                                                                                        |
| `diagnostics`                                                                                              | List[[models.TextqlRPCPublicPatchesConfigDiagnostic](../models/textqlrpcpublicpatchesconfigdiagnostic.md)] | :heavy_minus_sign:                                                                                         | N/A                                                                                                        |