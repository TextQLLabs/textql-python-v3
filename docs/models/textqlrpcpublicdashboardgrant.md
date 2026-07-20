# TextqlRPCPublicDashboardGrant

Grant is an author allowlist gating a data source or compute function. A viewer whose
 effective role names intersect roles, or whose member id is listed in members, may call it.
 Absent grant = org-visible (today's behavior); an empty grant object is invalid.


## Fields

| Field               | Type                | Required            | Description         |
| ------------------- | ------------------- | ------------------- | ------------------- |
| `roles`             | List[*str*]         | :heavy_minus_sign:  | org role names      |
| `members`           | List[*str*]         | :heavy_minus_sign:  | explicit member ids |