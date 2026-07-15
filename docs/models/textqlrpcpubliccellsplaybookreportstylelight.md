# TextqlRPCPublicCellsPlaybookReportStyleLight

Playbook report output style - matches parseReportStyle in playbook_helpers.go
 REPORT_STYLE_EXECUTIVE = "Executive_Report" or "Executive"
 REPORT_STYLE_VERBOSE = "Verbose" or "Thorough"
 REPORT_STYLE_CONCISE = "Concise" or "Brief"

## Example Usage

```python
from textql_sdk.models import TextqlRPCPublicCellsPlaybookReportStyleLight

# Open enum: unrecognized values are captured as UnrecognizedStr
value: TextqlRPCPublicCellsPlaybookReportStyleLight = "REPORT_STYLE_LIGHT_UNKNOWN"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"REPORT_STYLE_LIGHT_UNKNOWN"`
- `"REPORT_STYLE_LIGHT_EXECUTIVE"`
- `"REPORT_STYLE_LIGHT_VERBOSE"`
- `"REPORT_STYLE_LIGHT_CONCISE"`
