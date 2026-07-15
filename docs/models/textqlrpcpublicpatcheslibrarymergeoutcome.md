# TextqlRPCPublicPatchesLibraryMergeOutcome

## Example Usage

```python
from textql_sdk.models import TextqlRPCPublicPatchesLibraryMergeOutcome

# Open enum: unrecognized values are captured as UnrecognizedStr
value: TextqlRPCPublicPatchesLibraryMergeOutcome = "LIBRARY_MERGE_OUTCOME_UNSPECIFIED"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"LIBRARY_MERGE_OUTCOME_UNSPECIFIED"`
- `"LIBRARY_MERGE_OUTCOME_ALREADY_UP_TO_DATE"`
- `"LIBRARY_MERGE_OUTCOME_LOCAL_AHEAD"`
- `"LIBRARY_MERGE_OUTCOME_FAST_FORWARD"`
- `"LIBRARY_MERGE_OUTCOME_BOOTSTRAP_ADOPT"`
- `"LIBRARY_MERGE_OUTCOME_MERGE_REQUIRED"`
- `"LIBRARY_MERGE_OUTCOME_UNRELATED_HISTORIES"`
