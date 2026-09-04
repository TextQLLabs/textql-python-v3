# TextqlRPCPublicConnectorListQueryTemplatesRequest


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `connector_id`                                 | *Optional[int]*                                | :heavy_minus_sign:                             | N/A                                            |
| `limit`                                        | *Optional[int]*                                | :heavy_minus_sign:                             | Display name (e.g., "Explore Data")            |
| `offset`                                       | *Optional[int]*                                | :heavy_minus_sign:                             | Query text to send (plain text, no formatting) |
| `days`                                         | *Optional[int]*                                | :heavy_minus_sign:                             | True if requires multiple connectors           |