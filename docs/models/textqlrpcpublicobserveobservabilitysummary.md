# TextqlRPCPublicObserveObservabilitySummary


## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `total_runs`                                  | *Optional[int]*                               | :heavy_minus_sign:                            | Totals                                        |
| `total_threads`                               | *Optional[int]*                               | :heavy_minus_sign:                            | N/A                                           |
| `total_playbooks`                             | *Optional[int]*                               | :heavy_minus_sign:                            | N/A                                           |
| `total_warnings`                              | *Optional[int]*                               | :heavy_minus_sign:                            | N/A                                           |
| `warn_rate_pct`                               | *Optional[int]*                               | :heavy_minus_sign:                            | N/A                                           |
| `runs_delta_pct`                              | *Optional[int]*                               | :heavy_minus_sign:                            | Deltas (percentage change vs previous period) |
| `threads_delta_pct`                           | *Optional[int]*                               | :heavy_minus_sign:                            | N/A                                           |
| `playbooks_delta_pct`                         | *Optional[int]*                               | :heavy_minus_sign:                            | N/A                                           |
| `warnings_delta_pct`                          | *Optional[int]*                               | :heavy_minus_sign:                            | N/A                                           |
| `runs_sparkline`                              | List[*int*]                                   | :heavy_minus_sign:                            | Sparklines (14 daily values, oldest first)    |
| `threads_sparkline`                           | List[*int*]                                   | :heavy_minus_sign:                            | N/A                                           |
| `playbooks_sparkline`                         | List[*int*]                                   | :heavy_minus_sign:                            | N/A                                           |
| `warnings_sparkline`                          | List[*int*]                                   | :heavy_minus_sign:                            | N/A                                           |
| `total_feed_agents`                           | *Optional[int]*                               | :heavy_minus_sign:                            | Feed agents                                   |
| `feed_agents_delta_pct`                       | *Optional[int]*                               | :heavy_minus_sign:                            | N/A                                           |
| `feed_agents_sparkline`                       | List[*int*]                                   | :heavy_minus_sign:                            | N/A                                           |
| `total_slack`                                 | *Optional[int]*                               | :heavy_minus_sign:                            | Slack chats                                   |
| `slack_delta_pct`                             | *Optional[int]*                               | :heavy_minus_sign:                            | N/A                                           |
| `slack_sparkline`                             | List[*int*]                                   | :heavy_minus_sign:                            | N/A                                           |
| `total_teams`                                 | *Optional[int]*                               | :heavy_minus_sign:                            | Teams chats                                   |
| `teams_delta_pct`                             | *Optional[int]*                               | :heavy_minus_sign:                            | N/A                                           |
| `teams_sparkline`                             | List[*int*]                                   | :heavy_minus_sign:                            | N/A                                           |