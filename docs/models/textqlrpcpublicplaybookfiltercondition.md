# TextqlRPCPublicPlaybookFilterCondition

Filter condition for template data searches


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `field`                                                                    | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | JSON field name                                                            |
| `operator`                                                                 | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | "equals", "contains", "starts_with", "ends_with", "gt", "gte", "lt", "lte" |
| `value`                                                                    | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Value to filter by                                                         |