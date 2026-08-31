# TextqlRPCPublicCellsQuestionOption

EmailCell is the agent's "send an email" output. It is an executable cell:
 the LLM emits the input (to/subject/body) and the framework executes the
 send, mutating the result fields. The cell renders as a transcript ("Email
 sent to maya@acme.com at 2:14pm") with the body visible after the fact.


## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `name`                                        | *Optional[str]*                               | :heavy_minus_sign:                            | Inputs (set by the LLM at cell creation time) |
| `description`                                 | *OptionalNullable[str]*                       | :heavy_minus_sign:                            | N/A                                           |
| `explanation`                                 | *OptionalNullable[str]*                       | :heavy_minus_sign:                            | markdown — rendered to HTML at send time      |