# TextqlRPCPublicDashboardLibraryTQLSource

References a .tql file stored in the Context Library. The file is rendered
 to SQL at fetch time and executed against the provided connector. Template
 parameter values are JSON-encoded in `params_json` (e.g. {"region":"EU"}).


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `tql_path`                                                        | *Optional[str]*                                                   | :heavy_minus_sign:                                                | path to the .tql file in the Context Library (must end in .tql)   |
| `connector_id`                                                    | *Optional[int]*                                                   | :heavy_minus_sign:                                                | SQL connector to execute the rendered query against               |
| `params_json`                                                     | *Optional[str]*                                                   | :heavy_minus_sign:                                                | JSON object mapping parameter names to values; "" means no params |