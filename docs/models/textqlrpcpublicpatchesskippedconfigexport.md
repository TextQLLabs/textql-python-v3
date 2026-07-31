# TextqlRPCPublicPatchesSkippedConfigExport

SaveAllObjectsAsConfig is the bulk SaveObjectAsConfig: it renders every
 object of the type the caller can read (and that has no config history) into
 ONE open patch. Objects the config format cannot express are skipped with a
 per-object reason rather than failing the batch.


## Fields

| Field              | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `object_id`        | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `object_name`      | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `reason`           | *Optional[str]*    | :heavy_minus_sign: | N/A                |