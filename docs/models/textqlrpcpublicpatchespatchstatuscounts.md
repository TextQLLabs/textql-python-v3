# TextqlRPCPublicPatchesPatchStatusCounts

PatchCapabilities describes which patch actions the calling member is
 permitted to perform. This is a read-only mirror of the authority checks in
 ApprovePatch and DenyPatch; computing it has no side effects and emits no
 audit log.


## Fields

| Field              | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `open`             | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `draft_mine`       | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `approved`         | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `denied`           | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `open_mine`        | *Optional[int]*    | :heavy_minus_sign: | N/A                |