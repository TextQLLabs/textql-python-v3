# TextqlRPCPublicCellsEmailRecipient

ConnectorsCell is the agent-only "connectors" inspect tool. The frontend only
 shows that the tool ran (and a count); connector detail goes to the LLM, never
 to the browser, and never carries secrets.


## Fields

| Field                   | Type                    | Required                | Description             |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `address`               | *Optional[str]*         | :heavy_minus_sign:      | list \| get             |
| `class_`                | *Optional[str]*         | :heavy_minus_sign:      | N/A                     |
| `member_id`             | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     |
| `display_name`          | *OptionalNullable[str]* | :heavy_minus_sign:      | N/A                     |