# TextqlRPCPublicPatchesGetPatchRequest

GetConfigExportCapabilities tells the UI whether to offer "Save as config":
 which object types currently have a working exporter (registered AND its
 dependencies — e.g. the ontology parser — reachable), and whether the caller
 holds the permission SaveObjectAsConfig requires. Authn-only: the response
 carries the authorization answer instead of failing the call.


## Fields

| Field                   | Type                    | Required                | Description             |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `patch_id`              | *Optional[str]*         | :heavy_minus_sign:      | N/A                     |
| `revision`              | *OptionalNullable[int]* | :heavy_minus_sign:      | N/A                     |