# ObservabilityService

## Overview

### Available Operations

* [observability_service_get_member_signal_trend](#observability_service_get_member_signal_trend) - GetMemberSignalTrend

## observability_service_get_member_signal_trend

GetMemberSignalTrend

### Example Usage

<!-- UsageSnippet language="python" operationID="ObservabilityService_GetMemberSignalTrend" method="post" path="/textql.rpc.public.observe.ObservabilityService/GetMemberSignalTrend" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.observability_service.observability_service_get_member_signal_trend()

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

**[models.ObservabilityServiceGetMemberSignalTrendResponse](../../models/observabilityservicegetmembersignaltrendresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |