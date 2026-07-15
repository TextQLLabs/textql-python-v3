# TextqlRPCPublicPlaybookGetPlaybookReportsBatchRequest

Batch request to get reports for multiple template data IDs efficiently


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `playbook_id`                                             | *Optional[str]*                                           | :heavy_minus_sign:                                        | UUID                                                      |
| `template_data_ids`                                       | List[*str*]                                               | :heavy_minus_sign:                                        | List of template data UUIDs to fetch reports for          |
| `limit_per_template`                                      | *Optional[int]*                                           | :heavy_minus_sign:                                        | Max reports to return per template_data_id (default: 100) |
| `batch_run_id`                                            | *OptionalNullable[str]*                                   | :heavy_minus_sign:                                        | UUID - filter reports and artifacts by batch run          |