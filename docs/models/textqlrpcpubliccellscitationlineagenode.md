# TextqlRPCPublicCellsCitationLineageNode

QuestionsCell is the agent's "ask the user structured questions" tool. It is a
 haltable cell: the agent pauses until the user submits or dismisses inline.
 On submit the answers go to the agent; on dismiss only the answered count does
 and the agent waits for the user's next message (the dismissal reason).


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `cell_id`                                                        | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `kind`                                                           | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `dataframe_name`                                                 | *OptionalNullable[str]*                                          | :heavy_minus_sign:                                               | prefill (pending) / summary (answered); sensitive values blanked |
| `connector_id`                                                   | *OptionalNullable[int]*                                          | :heavy_minus_sign:                                               | N/A                                                              |
| `tables`                                                         | List[*str*]                                                      | :heavy_minus_sign:                                               | N/A                                                              |
| `input_cell_ids`                                                 | List[*str*]                                                      | :heavy_minus_sign:                                               | N/A                                                              |