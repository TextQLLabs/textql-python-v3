# TextqlRPCPublicPatchesOntologyMergeOutcome

## Example Usage

```python
from textql_sdk.models import TextqlRPCPublicPatchesOntologyMergeOutcome

# Open enum: unrecognized values are captured as UnrecognizedStr
value: TextqlRPCPublicPatchesOntologyMergeOutcome = "ONTOLOGY_MERGE_OUTCOME_UNSPECIFIED"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"ONTOLOGY_MERGE_OUTCOME_UNSPECIFIED"`
- `"ONTOLOGY_MERGE_OUTCOME_ALREADY_UP_TO_DATE"`
- `"ONTOLOGY_MERGE_OUTCOME_LOCAL_AHEAD"`
- `"ONTOLOGY_MERGE_OUTCOME_FAST_FORWARD"`
- `"ONTOLOGY_MERGE_OUTCOME_BOOTSTRAP_ADOPT"`
- `"ONTOLOGY_MERGE_OUTCOME_MERGE_REQUIRED"`
- `"ONTOLOGY_MERGE_OUTCOME_UNRELATED_HISTORIES"`
