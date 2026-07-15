# Libraries

## Overview

### Available Operations

* [add_submodule](#add_submodule) - AddLibrarySubmodule
* [create_file_upload_url](#create_file_upload_url) - CreateLibraryFileUploadUrl
* [delete_approval_rule](#delete_approval_rule) - DeleteApprovalRule
* [delete_owners](#delete_owners) - DeleteLibraryOwners
* [get_codeowner_coverage](#get_codeowner_coverage) - GetCodeownerCoverage
* [get_effective_owners](#get_effective_owners) - GetEffectiveLibraryOwners
* [get_file_usage](#get_file_usage) - GetFileUsage
* [get_ana_config](#get_ana_config) - GetLibraryAnaConfig
* [get_file](#get_file) - GetLibraryFile
* [get_history_file_diff](#get_history_file_diff) - GetLibraryHistoryFileDiff
* [get_remote](#get_remote) - GetLibraryRemote
* [get_size_timeline](#get_size_timeline) - GetLibrarySizeTimeline
* [get_raw_patch](#get_raw_patch) - GetRawPatch
* [list_context_patch_auto_approve_rules](#list_context_patch_auto_approve_rules) - ListContextPatchAutoApproveRules
* [list_imports](#list_imports) - ListLibraryImports
* [list_skills](#list_skills) - Lists the skills under the library's flat skills/ root that the caller can  read (OWNERS-filtered). Returns display metadata only — never instruction  bodies — feeding the chat composer's `/` autocomplete.
* [recover](#recover) - RecoverLibrary
* [remove_library_submodule](#remove_library_submodule) - RemoveLibrarySubmodule
* [request_patch_review](#request_patch_review) - RequestPatchReview
* [restore_patch](#restore_patch) - RestorePatch
* [revert_patch](#revert_patch) - RevertPatch
* [update_approval_rule](#update_approval_rule) - UpdateApprovalRule
* [upsert_ana_config](#upsert_ana_config) - UpsertLibraryAnaConfig
* [upsert_owners](#upsert_owners) - UpsertLibraryOwners

## add_submodule

AddLibrarySubmodule

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_AddLibrarySubmodule" method="post" path="/textql.rpc.public.patches.LibraryService/AddLibrarySubmodule" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.libraries.add_submodule()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `url`                                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `path`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `branch`                                                            | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LibraryServiceAddLibrarySubmoduleResponse](../../models/libraryserviceaddlibrarysubmoduleresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## create_file_upload_url

CreateLibraryFileUploadUrl

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_CreateLibraryFileUploadUrl" method="post" path="/textql.rpc.public.patches.LibraryService/CreateLibraryFileUploadUrl" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.libraries.create_file_upload_url()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                             | Type                                                                                                                                                                  | Required                                                                                                                                                              | Description                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                                  | *Optional[float]*                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                    | N/A                                                                                                                                                                   |
| `path`                                                                                                                                                                | *Optional[str]*                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                    | N/A                                                                                                                                                                   |
| `mime_type`                                                                                                                                                           | *Optional[str]*                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                    | N/A                                                                                                                                                                   |
| `size_bytes`                                                                                                                                                          | [Optional[models.TextqlRPCPublicPatchesCreateLibraryFileUploadURLRequestSizeBytes]](../../models/textqlrpcpublicpatchescreatelibraryfileuploadurlrequestsizebytes.md) | :heavy_minus_sign:                                                                                                                                                    | N/A                                                                                                                                                                   |
| `retries`                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                      | :heavy_minus_sign:                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                   |

### Response

**[models.LibraryServiceCreateLibraryFileUploadURLResponse](../../models/libraryservicecreatelibraryfileuploadurlresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete_approval_rule

DeleteApprovalRule

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_DeleteApprovalRule" method="post" path="/textql.rpc.public.patches.LibraryService/DeleteApprovalRule" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.libraries.delete_approval_rule()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `id`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LibraryServiceDeleteApprovalRuleResponse](../../models/libraryservicedeleteapprovalruleresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete_owners

DeleteLibraryOwners

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_DeleteLibraryOwners" method="post" path="/textql.rpc.public.patches.LibraryService/DeleteLibraryOwners" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.libraries.delete_owners()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `path`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `role_ids`                                                          | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `commit_message`                                                    | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LibraryServiceDeleteLibraryOwnersResponse](../../models/libraryservicedeletelibraryownersresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_codeowner_coverage

GetCodeownerCoverage

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_GetCodeownerCoverage" method="post" path="/textql.rpc.public.patches.LibraryService/GetCodeownerCoverage" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.libraries.get_codeowner_coverage(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                     | Type                                                                                                                          | Required                                                                                                                      | Description                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                        | [models.TextqlRPCPublicPatchesGetCodeownerCoverageRequest](../../models/textqlrpcpublicpatchesgetcodeownercoveragerequest.md) | :heavy_check_mark:                                                                                                            | N/A                                                                                                                           |
| `connect_timeout_ms`                                                                                                          | *Optional[float]*                                                                                                             | :heavy_minus_sign:                                                                                                            | N/A                                                                                                                           |
| `retries`                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                              | :heavy_minus_sign:                                                                                                            | Configuration to override the default retry behavior of the client.                                                           |

### Response

**[models.LibraryServiceGetCodeownerCoverageResponse](../../models/libraryservicegetcodeownercoverageresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_effective_owners

GetEffectiveLibraryOwners

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_GetEffectiveLibraryOwners" method="post" path="/textql.rpc.public.patches.LibraryService/GetEffectiveLibraryOwners" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.libraries.get_effective_owners()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `path`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LibraryServiceGetEffectiveLibraryOwnersResponse](../../models/libraryservicegeteffectivelibraryownersresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_file_usage

GetFileUsage

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_GetFileUsage" method="post" path="/textql.rpc.public.patches.LibraryService/GetFileUsage" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.libraries.get_file_usage()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | *Optional[float]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `path_prefix`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `order`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [Optional[models.TextqlRPCPublicPatchesUsageOrderBy]](../../models/textqlrpcpublicpatchesusageorderby.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `observation_period`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | *Optional[timedelta]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | A Duration represents a signed, fixed-length span of time represented<br/> as a count of seconds and fractions of seconds at nanosecond<br/> resolution. It is independent of any calendar and concepts like "day"<br/> or "month". It is related to Timestamp in that the difference between<br/> two Timestamp values is a Duration and it can be added or subtracted<br/> from a Timestamp. Range is approximately +-10,000 years.<br/><br/> # Examples<br/><br/> Example 1: Compute Duration from two Timestamps in pseudo code.<br/><br/>     Timestamp start = ...;<br/>     Timestamp end = ...;<br/>     Duration duration = ...;<br/><br/>     duration.seconds = end.seconds - start.seconds;<br/>     duration.nanos = end.nanos - start.nanos;<br/><br/>     if (duration.seconds < 0 && duration.nanos > 0) {<br/>       duration.seconds += 1;<br/>       duration.nanos -= 1000000000;<br/>     } else if (duration.seconds > 0 && duration.nanos < 0) {<br/>       duration.seconds -= 1;<br/>       duration.nanos += 1000000000;<br/>     }<br/><br/> Example 2: Compute Timestamp from Timestamp + Duration in pseudo code.<br/><br/>     Timestamp start = ...;<br/>     Duration duration = ...;<br/>     Timestamp end = ...;<br/><br/>     end.seconds = start.seconds + duration.seconds;<br/>     end.nanos = start.nanos + duration.nanos;<br/><br/>     if (end.nanos < 0) {<br/>       end.seconds -= 1;<br/>       end.nanos += 1000000000;<br/>     } else if (end.nanos >= 1000000000) {<br/>       end.seconds += 1;<br/>       end.nanos -= 1000000000;<br/>     }<br/><br/> Example 3: Compute Duration from datetime.timedelta in Python.<br/><br/>     td = datetime.timedelta(days=3, minutes=10)<br/>     duration = Duration()<br/>     duration.FromTimedelta(td)<br/><br/> # JSON Mapping<br/><br/> In JSON format, the Duration type is encoded as a string rather than an<br/> object, where the string ends in the suffix "s" (indicating seconds) and<br/> is preceded by the number of seconds, with nanoseconds expressed as<br/> fractional seconds. For example, 3 seconds with 0 nanoseconds should be<br/> encoded in JSON format as "3s", while 3 seconds and 1 nanosecond should<br/> be expressed in JSON format as "3.000000001s", and 3 seconds and 1<br/> microsecond should be expressed in JSON format as "3.000001s". |
| `page_cursor`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `page_size`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | *OptionalNullable[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | default 100, capped at 100                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

### Response

**[models.LibraryServiceGetFileUsageResponse](../../models/libraryservicegetfileusageresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_ana_config

GetLibraryAnaConfig

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_GetLibraryAnaConfig" method="post" path="/textql.rpc.public.patches.LibraryService/GetLibraryAnaConfig" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.libraries.get_ana_config()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `path`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LibraryServiceGetLibraryAnaConfigResponse](../../models/libraryservicegetlibraryanaconfigresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_file

GetLibraryFile

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_GetLibraryFile" method="post" path="/textql.rpc.public.patches.LibraryService/GetLibraryFile" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.libraries.get_file()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `path`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LibraryServiceGetLibraryFileResponse](../../models/libraryservicegetlibraryfileresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_history_file_diff

GetLibraryHistoryFileDiff

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_GetLibraryHistoryFileDiff" method="post" path="/textql.rpc.public.patches.LibraryService/GetLibraryHistoryFileDiff" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.libraries.get_history_file_diff()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `commit_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `path`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LibraryServiceGetLibraryHistoryFileDiffResponse](../../models/libraryservicegetlibraryhistoryfilediffresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_remote

GetLibraryRemote

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_GetLibraryRemote" method="post" path="/textql.rpc.public.patches.LibraryService/GetLibraryRemote" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.libraries.get_remote(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                | [models.TextqlRPCPublicPatchesGetLibraryRemoteRequest](../../models/textqlrpcpublicpatchesgetlibraryremoterequest.md) | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `connect_timeout_ms`                                                                                                  | *Optional[float]*                                                                                                     | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |

### Response

**[models.LibraryServiceGetLibraryRemoteResponse](../../models/libraryservicegetlibraryremoteresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_size_timeline

GetLibrarySizeTimeline

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_GetLibrarySizeTimeline" method="post" path="/textql.rpc.public.patches.LibraryService/GetLibrarySizeTimeline" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.libraries.get_size_timeline()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | *Optional[float]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `observation_period`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | *Optional[timedelta]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | A Duration represents a signed, fixed-length span of time represented<br/> as a count of seconds and fractions of seconds at nanosecond<br/> resolution. It is independent of any calendar and concepts like "day"<br/> or "month". It is related to Timestamp in that the difference between<br/> two Timestamp values is a Duration and it can be added or subtracted<br/> from a Timestamp. Range is approximately +-10,000 years.<br/><br/> # Examples<br/><br/> Example 1: Compute Duration from two Timestamps in pseudo code.<br/><br/>     Timestamp start = ...;<br/>     Timestamp end = ...;<br/>     Duration duration = ...;<br/><br/>     duration.seconds = end.seconds - start.seconds;<br/>     duration.nanos = end.nanos - start.nanos;<br/><br/>     if (duration.seconds < 0 && duration.nanos > 0) {<br/>       duration.seconds += 1;<br/>       duration.nanos -= 1000000000;<br/>     } else if (duration.seconds > 0 && duration.nanos < 0) {<br/>       duration.seconds -= 1;<br/>       duration.nanos += 1000000000;<br/>     }<br/><br/> Example 2: Compute Timestamp from Timestamp + Duration in pseudo code.<br/><br/>     Timestamp start = ...;<br/>     Duration duration = ...;<br/>     Timestamp end = ...;<br/><br/>     end.seconds = start.seconds + duration.seconds;<br/>     end.nanos = start.nanos + duration.nanos;<br/><br/>     if (end.nanos < 0) {<br/>       end.seconds -= 1;<br/>       end.nanos += 1000000000;<br/>     } else if (end.nanos >= 1000000000) {<br/>       end.seconds += 1;<br/>       end.nanos -= 1000000000;<br/>     }<br/><br/> Example 3: Compute Duration from datetime.timedelta in Python.<br/><br/>     td = datetime.timedelta(days=3, minutes=10)<br/>     duration = Duration()<br/>     duration.FromTimedelta(td)<br/><br/> # JSON Mapping<br/><br/> In JSON format, the Duration type is encoded as a string rather than an<br/> object, where the string ends in the suffix "s" (indicating seconds) and<br/> is preceded by the number of seconds, with nanoseconds expressed as<br/> fractional seconds. For example, 3 seconds with 0 nanoseconds should be<br/> encoded in JSON format as "3s", while 3 seconds and 1 nanosecond should<br/> be expressed in JSON format as "3.000000001s", and 3 seconds and 1<br/> microsecond should be expressed in JSON format as "3.000001s". |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

### Response

**[models.LibraryServiceGetLibrarySizeTimelineResponse](../../models/libraryservicegetlibrarysizetimelineresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_raw_patch

GetRawPatch

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_GetRawPatch" method="post" path="/textql.rpc.public.patches.LibraryService/GetRawPatch" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.libraries.get_raw_patch()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `patch_number`                                                      | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LibraryServiceGetRawPatchResponse](../../models/libraryservicegetrawpatchresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_context_patch_auto_approve_rules

ListContextPatchAutoApproveRules

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_ListContextPatchAutoApproveRules" method="post" path="/textql.rpc.public.patches.LibraryService/ListContextPatchAutoApproveRules" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.libraries.list_context_patch_auto_approve_rules(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                             | Type                                                                                                                                                  | Required                                                                                                                                              | Description                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                                                | [models.TextqlRPCPublicPatchesListContextPatchAutoApproveRulesRequest](../../models/textqlrpcpublicpatcheslistcontextpatchautoapproverulesrequest.md) | :heavy_check_mark:                                                                                                                                    | N/A                                                                                                                                                   |
| `connect_timeout_ms`                                                                                                                                  | *Optional[float]*                                                                                                                                     | :heavy_minus_sign:                                                                                                                                    | N/A                                                                                                                                                   |
| `retries`                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                      | :heavy_minus_sign:                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                   |

### Response

**[models.LibraryServiceListContextPatchAutoApproveRulesResponse](../../models/libraryservicelistcontextpatchautoapproverulesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_imports

ListLibraryImports

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_ListLibraryImports" method="post" path="/textql.rpc.public.patches.LibraryService/ListLibraryImports" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.libraries.list_imports(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                    | [models.TextqlRPCPublicPatchesListLibraryImportsRequest](../../models/textqlrpcpublicpatcheslistlibraryimportsrequest.md) | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |
| `connect_timeout_ms`                                                                                                      | *Optional[float]*                                                                                                         | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |

### Response

**[models.LibraryServiceListLibraryImportsResponse](../../models/libraryservicelistlibraryimportsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_skills

Lists the skills under the library's flat skills/ root that the caller can
 read (OWNERS-filtered). Returns display metadata only — never instruction
 bodies — feeding the chat composer's `/` autocomplete.

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_ListSkills" method="post" path="/textql.rpc.public.patches.LibraryService/ListSkills" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.libraries.list_skills(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                    | [models.TextqlRPCPublicPatchesListSkillsRequest](../../models/textqlrpcpublicpatcheslistskillsrequest.md) | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `connect_timeout_ms`                                                                                      | *Optional[float]*                                                                                         | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.LibraryServiceListSkillsResponse](../../models/libraryservicelistskillsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## recover

RecoverLibrary

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_RecoverLibrary" method="post" path="/textql.rpc.public.patches.LibraryService/RecoverLibrary" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.libraries.recover()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                    | *Optional[float]*                                                                                                       | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `level`                                                                                                                 | [Optional[models.TextqlRPCPublicPatchesRecoverLibraryLevel]](../../models/textqlrpcpublicpatchesrecoverlibrarylevel.md) | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |

### Response

**[models.LibraryServiceRecoverLibraryResponse](../../models/libraryservicerecoverlibraryresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## remove_library_submodule

RemoveLibrarySubmodule

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_RemoveLibrarySubmodule" method="post" path="/textql.rpc.public.patches.LibraryService/RemoveLibrarySubmodule" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.libraries.remove_library_submodule()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `path`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LibraryServiceRemoveLibrarySubmoduleResponse](../../models/libraryserviceremovelibrarysubmoduleresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## request_patch_review

RequestPatchReview

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_RequestPatchReview" method="post" path="/textql.rpc.public.patches.LibraryService/RequestPatchReview" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.libraries.request_patch_review()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `patch_id`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `reviewer_member_id`                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LibraryServiceRequestPatchReviewResponse](../../models/libraryservicerequestpatchreviewresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## restore_patch

RestorePatch

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_RestorePatch" method="post" path="/textql.rpc.public.patches.LibraryService/RestorePatch" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.libraries.restore_patch()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `patch_id`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `expected_git_ref`                                                  | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LibraryServiceRestorePatchResponse](../../models/libraryservicerestorepatchresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## revert_patch

RevertPatch

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_RevertPatch" method="post" path="/textql.rpc.public.patches.LibraryService/RevertPatch" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.libraries.revert_patch()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `patch_id`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LibraryServiceRevertPatchResponse](../../models/libraryservicerevertpatchresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## update_approval_rule

UpdateApprovalRule

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_UpdateApprovalRule" method="post" path="/textql.rpc.public.patches.LibraryService/UpdateApprovalRule" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.libraries.update_approval_rule()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                | *Optional[float]*                                                                                                   | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `id`                                                                                                                | *Optional[str]*                                                                                                     | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `rule`                                                                                                              | [Optional[models.TextqlRPCPublicPatchesApprovalRuleInput]](../../models/textqlrpcpublicpatchesapprovalruleinput.md) | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |

### Response

**[models.LibraryServiceUpdateApprovalRuleResponse](../../models/libraryserviceupdateapprovalruleresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## upsert_ana_config

UpsertLibraryAnaConfig

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_UpsertLibraryAnaConfig" method="post" path="/textql.rpc.public.patches.LibraryService/UpsertLibraryAnaConfig" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.libraries.upsert_ana_config()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                        | *Optional[float]*                                                                                           | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `path`                                                                                                      | *Optional[str]*                                                                                             | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `auto_attach`                                                                                               | List[[models.TextqlRPCPublicPatchesAutoAttachEntry](../../models/textqlrpcpublicpatchesautoattachentry.md)] | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `commit_message`                                                                                            | *OptionalNullable[str]*                                                                                     | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `codeowners`                                                                                                | List[[models.TextqlRPCPublicPatchesCodeownerEntry](../../models/textqlrpcpublicpatchescodeownerentry.md)]   | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Response

**[models.LibraryServiceUpsertLibraryAnaConfigResponse](../../models/libraryserviceupsertlibraryanaconfigresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## upsert_owners

UpsertLibraryOwners

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_UpsertLibraryOwners" method="post" path="/textql.rpc.public.patches.LibraryService/UpsertLibraryOwners" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.libraries.upsert_owners()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                            | *Optional[float]*                                                                                               | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `path`                                                                                                          | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `role_ids`                                                                                                      | List[*str*]                                                                                                     | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `permissions`                                                                                                   | List[[models.TextqlRPCPublicPatchesLibraryPermission](../../models/textqlrpcpublicpatcheslibrarypermission.md)] | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `commit_message`                                                                                                | *OptionalNullable[str]*                                                                                         | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.LibraryServiceUpsertLibraryOwnersResponse](../../models/libraryserviceupsertlibraryownersresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |