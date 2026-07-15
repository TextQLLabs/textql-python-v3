# Topics

## Overview

### Available Operations

* [refine_draft](#refine_draft) - Custom topics

## refine_draft

Custom topics

### Example Usage

<!-- UsageSnippet language="python" operationID="ObservabilityService_RefineTopicDraft" method="post" path="/textql.rpc.public.observe.ObservabilityService/RefineTopicDraft" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.topics.refine_draft()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `prompt`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `examples`                                                          | List[*str*]                                                         | :heavy_minus_sign:                                                  | example questions users ask                                         |
| `exclusions`                                                        | List[*str*]                                                         | :heavy_minus_sign:                                                  | "should NOT be tagged" phrases                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ObservabilityServiceRefineTopicDraftResponse](../../models/observabilityservicerefinetopicdraftresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |