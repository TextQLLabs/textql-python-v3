# ObservabilityService

## Overview

### Available Operations

* [activate_custom_topic](#activate_custom_topic) - ActivateCustomTopic
* [get_backfill_preview](#get_backfill_preview) - GetBackfillPreview
* [get_engagement_spectrum](#get_engagement_spectrum) - GetEngagementSpectrum
* [get_observability_stats](#get_observability_stats) - GetObservabilityStats
* [get_thread_warnings](#get_thread_warnings) - GetThreadWarnings

## activate_custom_topic

ActivateCustomTopic

### Example Usage

<!-- UsageSnippet language="python" operationID="ObservabilityService_ActivateCustomTopic" method="post" path="/textql.rpc.public.observe.ObservabilityService/ActivateCustomTopic" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.observability_service.activate_custom_topic()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `topic_id`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ObservabilityServiceActivateCustomTopicResponse](../../models/observabilityserviceactivatecustomtopicresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_backfill_preview

GetBackfillPreview

### Example Usage

<!-- UsageSnippet language="python" operationID="ObservabilityService_GetBackfillPreview" method="post" path="/textql.rpc.public.observe.ObservabilityService/GetBackfillPreview" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.observability_service.get_backfill_preview()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `days`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `org_id`                                                            | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `redo_all_threads`                                                  | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ObservabilityServiceGetBackfillPreviewResponse](../../models/observabilityservicegetbackfillpreviewresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_engagement_spectrum

GetEngagementSpectrum

### Example Usage

<!-- UsageSnippet language="python" operationID="ObservabilityService_GetEngagementSpectrum" method="post" path="/textql.rpc.public.observe.ObservabilityService/GetEngagementSpectrum" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.observability_service.get_engagement_spectrum()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `days`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ObservabilityServiceGetEngagementSpectrumResponse](../../models/observabilityservicegetengagementspectrumresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_observability_stats

GetObservabilityStats

### Example Usage

<!-- UsageSnippet language="python" operationID="ObservabilityService_GetObservabilityStats" method="post" path="/textql.rpc.public.observe.ObservabilityService/GetObservabilityStats" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.observability_service.get_observability_stats()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `days`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | time window: 7, 14, 30, 90                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ObservabilityServiceGetObservabilityStatsResponse](../../models/observabilityservicegetobservabilitystatsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_thread_warnings

GetThreadWarnings

### Example Usage

<!-- UsageSnippet language="python" operationID="ObservabilityService_GetThreadWarnings" method="post" path="/textql.rpc.public.observe.ObservabilityService/GetThreadWarnings" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.observability_service.get_thread_warnings()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `chat_ids`                                                          | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ObservabilityServiceGetThreadWarningsResponse](../../models/observabilityservicegetthreadwarningsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |