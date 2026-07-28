# TextqlRPCPublicObserveUsageHeatmapPoint

UsageHeatmapPoint is one (weekday, hour) bucket of chat volume, in the
 timezone requested via GetObservabilityStatsRequest.timezone.


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `dow`                                           | *Optional[int]*                                 | :heavy_minus_sign:                              | 0=Sunday .. 6=Saturday (Postgres/JS convention) |
| `hour`                                          | *Optional[int]*                                 | :heavy_minus_sign:                              | 0-23                                            |
| `total`                                         | *Optional[int]*                                 | :heavy_minus_sign:                              | N/A                                             |