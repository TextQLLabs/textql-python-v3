# TextqlRPCPublicObserveMemberSignalTrendPoint

One (member, week) bucket of signal quality. Weeks with no signals and no
 analyzed threads are omitted; the client zero-fills the axis.


## Fields

| Field                                   | Type                                    | Required                                | Description                             |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| `member_id`                             | *Optional[str]*                         | :heavy_minus_sign:                      | N/A                                     |
| `bucket_start`                          | *Optional[str]*                         | :heavy_minus_sign:                      | YYYY-MM-DD, week start                  |
| `positive`                              | *Optional[int]*                         | :heavy_minus_sign:                      | N/A                                     |
| `negative`                              | *Optional[int]*                         | :heavy_minus_sign:                      | N/A                                     |
| `analyzed`                              | *Optional[int]*                         | :heavy_minus_sign:                      | distinct analyzed threads in the bucket |