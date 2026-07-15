# TextqlRPCPublicDashboardPreviewConfigDashboardRequest

PreviewConfigDashboard renders a config-managed dashboard from a patch ref before
 merge (ADR-0022). The previewing member + org come from auth context.


## Fields

| Field                                | Type                                 | Required                             | Description                          |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `patch_ref`                          | *Optional[str]*                      | :heavy_minus_sign:                   | git ref of the patch to preview from |
| `dashboard_path`                     | *Optional[str]*                      | :heavy_minus_sign:                   | Library path of the .dashboard file  |