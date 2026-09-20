# TextqlRPCPublicCellsUseSkillCell

UseSkillCell is the client projection of a `use_skill` auto-invoke. It
 deliberately carries no body field: the skill's instructions are LLM-facing
 prompt scaffolding (see compute/pkg/chat/cells/use_skill.go), never sent to
 the transcript. The frontend renders provenance only ("Using skill /trigger").


## Fields

| Field              | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `trigger`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `name`             | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `ok`               | *Optional[bool]*   | :heavy_minus_sign: | N/A                |