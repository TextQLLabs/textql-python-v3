# TextqlRPCPublicAppGetAppVersionRequest


## Fields

| Field                                                                             | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `app_id`                                                                          | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | False when the document predates tree publishing and has no runtime to overwrite. |
| `version_number`                                                                  | *Optional[int]*                                                                   | :heavy_minus_sign:                                                                | N/A                                                                               |
| `commit_id`                                                                       | *OptionalNullable[str]*                                                           | :heavy_minus_sign:                                                                | N/A                                                                               |