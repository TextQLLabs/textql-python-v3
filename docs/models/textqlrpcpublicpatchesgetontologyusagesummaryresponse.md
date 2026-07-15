# TextqlRPCPublicPatchesGetOntologyUsageSummaryResponse

Aggregate ontology-usage health for the window — the roll-ups the Ontology
 Health hero needs without paging every file to the client. pulled_files,
 avg_hit_rate, and error_files are Postgres aggregates over the pull/run data;
 total_files, dead_files, and reclaimable_tokens come from the current git
 tree diffed against the set of pulled paths (a dead file is one present in
 the ontology but never pulled in the window).


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `total_files`                                                        | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `pulled_files`                                                       | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `dead_files`                                                         | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `avg_hit_rate`                                                       | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | 0..1, averaged over pulled files                                     |
| `error_files`                                                        | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | files with at least one errored pull in the window                   |
| `reclaimable_tokens`                                                 | [Optional[models.ReclaimableTokens]](../models/reclaimabletokens.md) | :heavy_minus_sign:                                                   | estimated tokens held by dead files (~size/4)                        |