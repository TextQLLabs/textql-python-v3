# TextqlRPCPublicPatchesPatchCapabilities

PatchCapabilities describes which patch actions the calling member is
 permitted to perform. This is a read-only mirror of the authority checks in
 ApprovePatch and DenyPatch; computing it has no side effects and emits no
 audit log.


## Fields

| Field              | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `can_approve`      | *Optional[bool]*   | :heavy_minus_sign: | N/A                |
| `can_deny`         | *Optional[bool]*   | :heavy_minus_sign: | N/A                |
| `can_restore`      | *Optional[bool]*   | :heavy_minus_sign: | N/A                |
| `caller_approved`  | *Optional[bool]*   | :heavy_minus_sign: | N/A                |