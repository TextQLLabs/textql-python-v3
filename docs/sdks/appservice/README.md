# AppService

## Overview

AppService manages data apps: the generative app execution primitive.
 An app is agent-authored single-file HTML/JS/CSS executing in a CSP sandbox,
 fed a snapshot of its declared data sources. First-class resource, not a dashboard.

### Available Operations

* [app_service_get_app_db_schema](#app_service_get_app_db_schema) - Server stream of live activity batches + presence snapshots, driven by  Valkey nudges over the app_activity:{app_id} channel; Postgres stays SSoT.
* [app_service_get_app_db_table_preview](#app_service_get_app_db_table_preview) - Presence heartbeat: sets a short-TTL Valkey key for the member and nudges  the app's stream. Presence never touches Postgres and never exposes emails.
* [app_service_get_app_member_state](#app_service_get_app_member_state) - View analytics: reads the engagement views recorded on app page load.
* [app_service_list_app_activity_since](#app_service_list_app_activity_since) - Append-only per-member activity log. Listing is own rows only; no  cross-member reads in this release.
* [app_service_list_my_app_member_activity](#app_service_list_my_app_member_activity) - ListMyAppMemberActivity
* [app_service_presence_heartbeat](#app_service_presence_heartbeat) - Cross-member live activity: rows from every member of the app after a seq,  each carrying member_id + display_name (resolved server-side; never email).
* [app_service_record_app_member_activity](#app_service_record_app_member_activity) - Per-member app state: one JSON blob per (app, member) so apps remember  settings/progress. Member always resolved server-side from auth context;  per-member persistence, so viewers with read access can save their own state.
* [app_service_set_app_member_state](#app_service_set_app_member_state) - Staff-only (superadmin gated in-handler): publishes the embedded component  gallery as an app tree and returns its signed viewer URL.

## app_service_get_app_db_schema

Server stream of live activity batches + presence snapshots, driven by
 Valkey nudges over the app_activity:{app_id} channel; Postgres stays SSoT.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_GetAppDBSchema" method="post" path="/textql.rpc.public.app.AppService/GetAppDBSchema" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.app_service.app_service_get_app_db_schema()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceGetAppDBSchemaResponse](../../models/appservicegetappdbschemaresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## app_service_get_app_db_table_preview

Presence heartbeat: sets a short-TTL Valkey key for the member and nudges
 the app's stream. Presence never touches Postgres and never exposes emails.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_GetAppDBTablePreview" method="post" path="/textql.rpc.public.app.AppService/GetAppDBTablePreview" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.app_service.app_service_get_app_db_table_preview()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `table_name`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceGetAppDBTablePreviewResponse](../../models/appservicegetappdbtablepreviewresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## app_service_get_app_member_state

View analytics: reads the engagement views recorded on app page load.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_GetAppMemberState" method="post" path="/textql.rpc.public.app.AppService/GetAppMemberState" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.app_service.app_service_get_app_member_state()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceGetAppMemberStateResponse](../../models/appservicegetappmemberstateresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## app_service_list_app_activity_since

Append-only per-member activity log. Listing is own rows only; no
 cross-member reads in this release.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_ListAppActivitySince" method="post" path="/textql.rpc.public.app.AppService/ListAppActivitySince" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.app_service.app_service_list_app_activity_since()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `scope`                                                             | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `after_seq`                                                         | [Optional[models.AfterSeq]](../../models/afterseq.md)               | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | server clamps to 200; <=0 means default                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceListAppActivitySinceResponse](../../models/appservicelistappactivitysinceresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## app_service_list_my_app_member_activity

ListMyAppMemberActivity

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_ListMyAppMemberActivity" method="post" path="/textql.rpc.public.app.AppService/ListMyAppMemberActivity" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.app_service.app_service_list_my_app_member_activity()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `type`                                                              | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | server clamps to 200; <=0 means default                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceListMyAppMemberActivityResponse](../../models/appservicelistmyappmemberactivityresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## app_service_presence_heartbeat

Cross-member live activity: rows from every member of the app after a seq,
 each carrying member_id + display_name (resolved server-side; never email).

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_PresenceHeartbeat" method="post" path="/textql.rpc.public.app.AppService/PresenceHeartbeat" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.app_service.app_service_presence_heartbeat()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `zone`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServicePresenceHeartbeatResponse](../../models/appservicepresenceheartbeatresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## app_service_record_app_member_activity

Per-member app state: one JSON blob per (app, member) so apps remember
 settings/progress. Member always resolved server-side from auth context;
 per-member persistence, so viewers with read access can save their own state.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_RecordAppMemberActivity" method="post" path="/textql.rpc.public.app.AppService/RecordAppMemberActivity" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.app_service.app_service_record_app_member_activity()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `type`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `scope`                                                             | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `payload_json`                                                      | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | JSON object, usage payload authored by the app                      |
| `idem_key`                                                          | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | duplicate key returns the existing row, not an error                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceRecordAppMemberActivityResponse](../../models/appservicerecordappmemberactivityresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## app_service_set_app_member_state

Staff-only (superadmin gated in-handler): publishes the embedded component
 gallery as an app tree and returns its signed viewer URL.

### Example Usage

<!-- UsageSnippet language="python" operationID="AppService_SetAppMemberState" method="post" path="/textql.rpc.public.app.AppService/SetAppMemberState" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.app_service.app_service_set_app_member_state()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `value_json`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | whole-object JSON, last-write-wins, max 64KB                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AppServiceSetAppMemberStateResponse](../../models/appservicesetappmemberstateresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |