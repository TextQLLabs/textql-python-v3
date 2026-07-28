# TextqlRPCPublicAppGetAppVersionRequest

Version history entry. Git-backed apps derive one per library commit (published_by/at
 carry the commit author/time); legacy rows are pre-existing publish-era snapshots.


## Fields

| Field                   | Type                    | Required                | Description             |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `app_id`                | *Optional[str]*         | :heavy_minus_sign:      | N/A                     |
| `version_number`        | *Optional[int]*         | :heavy_minus_sign:      | N/A                     |
| `commit_id`             | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     |