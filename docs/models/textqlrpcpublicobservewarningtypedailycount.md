# TextqlRPCPublicObserveWarningTypeDailyCount

WarningTypeDailyCount is one (day, warning type) bucket for the warning
 breakdown-over-time chart. Derived from thread_warning joined to each chat's
 created_at.


## Fields

| Field                                                                                                      | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `date_`                                                                                                    | *Optional[str]*                                                                                            | :heavy_minus_sign:                                                                                         | YYYY-MM-DD                                                                                                 |
| `warning_type`                                                                                             | [Optional[models.TextqlRPCPublicChatThreadWarningType]](../models/textqlrpcpublicchatthreadwarningtype.md) | :heavy_minus_sign:                                                                                         | ThreadWarningType is the canonical set of thread warning types                                             |
| `total`                                                                                                    | *Optional[int]*                                                                                            | :heavy_minus_sign:                                                                                         | N/A                                                                                                        |