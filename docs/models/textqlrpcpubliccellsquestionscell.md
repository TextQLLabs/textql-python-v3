# TextqlRPCPublicCellsQuestionsCell

QuestionsCell is the agent's "ask the user structured questions" tool. It is a
 haltable cell: the agent pauses until the user submits or dismisses inline.
 On submit the answers go to the agent; on dismiss only the answered count does
 and the agent waits for the user's next message (the dismissal reason).


## Fields

| Field                                                                                                    | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `status`                                                                                                 | [Optional[models.TextqlRPCPublicCellsQuestionsStatus]](../models/textqlrpcpubliccellsquestionsstatus.md) | :heavy_minus_sign:                                                                                       | N/A                                                                                                      |
| `questions`                                                                                              | List[[models.TextqlRPCPublicCellsQuestionSpec](../models/textqlrpcpubliccellsquestionspec.md)]           | :heavy_minus_sign:                                                                                       | N/A                                                                                                      |
| `answers`                                                                                                | List[[models.TextqlRPCPublicCellsQuestionAnswer](../models/textqlrpcpubliccellsquestionanswer.md)]       | :heavy_minus_sign:                                                                                       | prefill (pending) / summary (answered); sensitive values blanked                                         |
| `answered_count`                                                                                         | *Optional[int]*                                                                                          | :heavy_minus_sign:                                                                                       | N/A                                                                                                      |