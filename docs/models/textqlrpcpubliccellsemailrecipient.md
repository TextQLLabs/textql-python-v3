# TextqlRPCPublicCellsEmailRecipient

EmailRecipient is one resolved recipient of an EmailCell. The frontend
 renders these as chips; the backend uses the resolution to enforce the
 internal-only policy at cell creation time.


## Fields

| Field                              | Type                               | Required                           | Description                        |
| ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- |
| `address`                          | *Optional[str]*                    | :heavy_minus_sign:                 | N/A                                |
| `class_`                           | *Optional[str]*                    | :heavy_minus_sign:                 | "internal" or "external"           |
| `member_id`                        | *OptionalNullable[str]*            | :heavy_minus_sign:                 | populated when class == "internal" |
| `display_name`                     | *OptionalNullable[str]*            | :heavy_minus_sign:                 | N/A                                |