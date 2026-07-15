# TextqlRPCPowerbiSelectionPowerBISelection

PowerBISelection captures a chosen PowerBI workspace (and optionally the
 specific reports/datasets within it) for attaching to a chat. Field shape
 mirrors textql.rpc.public.paradigm.PowerBISelection; kept in a standalone
 package so it can be shared by paradigm_params without an import cycle
 (public/paradigm.proto already imports paradigm_params.proto).


## Fields

| Field              | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `workspace_id`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `report_ids`       | List[*str*]        | :heavy_minus_sign: | N/A                |
| `dataset_ids`      | List[*str*]        | :heavy_minus_sign: | N/A                |
| `workspace_name`   | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `connector_id`     | *Optional[int]*    | :heavy_minus_sign: | N/A                |