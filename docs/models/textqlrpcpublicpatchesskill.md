# TextqlRPCPublicPatchesSkill

Skill is the display metadata for one library skill. Intentionally carries no
 instruction body: bodies are inlined server-side at chat time and never sent
 to the client.


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `trigger`                                        | *Optional[str]*                                  | :heavy_minus_sign:                               | directory basename — the /<trigger> a user types |
| `name`                                           | *Optional[str]*                                  | :heavy_minus_sign:                               | frontmatter display name (may be empty)          |
| `description`                                    | *Optional[str]*                                  | :heavy_minus_sign:                               | frontmatter description (may be empty)           |
| `path`                                           | *Optional[str]*                                  | :heavy_minus_sign:                               | library-relative path, e.g. "skills/forecast"    |