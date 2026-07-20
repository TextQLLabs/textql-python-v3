# TextqlRPCPublicAppRecordAppMemberActivityRequest

Per-member activity log


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `app_id`                                             | *Optional[str]*                                      | :heavy_minus_sign:                                   | N/A                                                  |
| `type`                                               | *Optional[str]*                                      | :heavy_minus_sign:                                   | N/A                                                  |
| `scope`                                              | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | N/A                                                  |
| `payload_json`                                       | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | JSON object, usage payload authored by the app       |
| `idem_key`                                           | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | duplicate key returns the existing row, not an error |