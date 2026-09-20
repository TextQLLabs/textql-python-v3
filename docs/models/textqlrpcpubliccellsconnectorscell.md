# TextqlRPCPublicCellsConnectorsCell

ConnectorsCell is the agent-only "connectors" inspect tool. The frontend only
 shows that the tool ran (and a count); connector detail goes to the LLM, never
 to the browser, and never carries secrets.


## Fields

| Field              | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `action`           | *Optional[str]*    | :heavy_minus_sign: | list \| get        |
| `total_count`      | *Optional[int]*    | :heavy_minus_sign: | N/A                |