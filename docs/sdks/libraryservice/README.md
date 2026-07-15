# LibraryService

## Overview

### Available Operations

* [approve_patch](#approve_patch) - ApprovePatch
* [create_approval_rule](#create_approval_rule) - CreateApprovalRule
* [create_library_directory](#create_library_directory) - CreateLibraryDirectory
* [delete_context_patch_auto_approve_rule](#delete_context_patch_auto_approve_rule) - DeleteContextPatchAutoApproveRule
* [deny_patch](#deny_patch) - DenyPatch
* [get_config_export_capabilities](#get_config_export_capabilities) - GetConfigExportCapabilities
* [get_patch](#get_patch) - GetPatch
* [get_patch_by_number](#get_patch_by_number) - GetPatchByNumber
* [get_patch_capabilities](#get_patch_capabilities) - GetPatchCapabilities
* [list_library_entries](#list_library_entries) - ListLibraryEntries
* [list_library_submodules](#list_library_submodules) - ListLibrarySubmodules
* [list_patches](#list_patches) - ListPatches
* [migrate_legacy_context](#migrate_legacy_context) - MigrateLegacyContextToLibrary
* [migrate_ontology](#migrate_ontology) - MigrateOntologyToLibrary
* [pull_from_remote](#pull_from_remote) - PullLibraryFromRemote
* [remove_remote](#remove_remote) - RemoveLibraryRemote
* [resolve_sync_conflict](#resolve_sync_conflict) - ResolveLibrarySyncConflict
* [trigger_config_drift_reconcile](#trigger_config_drift_reconcile) - TriggerConfigDriftReconcile forces an immediate config-sync catch-up for the  caller's org: if the Library repo's live HEAD differs from the last  reconciled commit, it enqueues a reconcile (otherwise no-op). The on-demand  equivalent of waiting for the periodic drift scan.
* [update_library_sync_config](#update_library_sync_config) - UpdateLibrarySyncConfig

## approve_patch

ApprovePatch

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_ApprovePatch" method="post" path="/textql.rpc.public.patches.LibraryService/ApprovePatch" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.library_service.approve_patch()

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

**[models.LibraryServiceApprovePatchResponse](../../models/libraryserviceapprovepatchresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## create_approval_rule

CreateApprovalRule

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_CreateApprovalRule" method="post" path="/textql.rpc.public.patches.LibraryService/CreateApprovalRule" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.library_service.create_approval_rule()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                | *Optional[float]*                                                                                                   | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `rule`                                                                                                              | [Optional[models.TextqlRPCPublicPatchesApprovalRuleInput]](../../models/textqlrpcpublicpatchesapprovalruleinput.md) | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |

### Response

**[models.LibraryServiceCreateApprovalRuleResponse](../../models/libraryservicecreateapprovalruleresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## create_library_directory

CreateLibraryDirectory

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_CreateLibraryDirectory" method="post" path="/textql.rpc.public.patches.LibraryService/CreateLibraryDirectory" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.library_service.create_library_directory()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `path`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `commit_message`                                                    | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LibraryServiceCreateLibraryDirectoryResponse](../../models/libraryservicecreatelibrarydirectoryresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete_context_patch_auto_approve_rule

DeleteContextPatchAutoApproveRule

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_DeleteContextPatchAutoApproveRule" method="post" path="/textql.rpc.public.patches.LibraryService/DeleteContextPatchAutoApproveRule" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.library_service.delete_context_patch_auto_approve_rule()

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

**[models.LibraryServiceDeleteContextPatchAutoApproveRuleResponse](../../models/libraryservicedeletecontextpatchautoapproveruleresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## deny_patch

DenyPatch

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_DenyPatch" method="post" path="/textql.rpc.public.patches.LibraryService/DenyPatch" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.library_service.deny_patch()

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

**[models.LibraryServiceDenyPatchResponse](../../models/libraryservicedenypatchresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_config_export_capabilities

GetConfigExportCapabilities

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_GetConfigExportCapabilities" method="post" path="/textql.rpc.public.patches.LibraryService/GetConfigExportCapabilities" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.library_service.get_config_export_capabilities(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                   | Type                                                                                                                                        | Required                                                                                                                                    | Description                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                                      | [models.TextqlRPCPublicPatchesGetConfigExportCapabilitiesRequest](../../models/textqlrpcpublicpatchesgetconfigexportcapabilitiesrequest.md) | :heavy_check_mark:                                                                                                                          | N/A                                                                                                                                         |
| `connect_timeout_ms`                                                                                                                        | *Optional[float]*                                                                                                                           | :heavy_minus_sign:                                                                                                                          | N/A                                                                                                                                         |
| `retries`                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                            | :heavy_minus_sign:                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                         |

### Response

**[models.LibraryServiceGetConfigExportCapabilitiesResponse](../../models/libraryservicegetconfigexportcapabilitiesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_patch

GetPatch

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_GetPatch" method="post" path="/textql.rpc.public.patches.LibraryService/GetPatch" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.library_service.get_patch()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `patch_id`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `revision`                                                          | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LibraryServiceGetPatchResponse](../../models/libraryservicegetpatchresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_patch_by_number

GetPatchByNumber

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_GetPatchByNumber" method="post" path="/textql.rpc.public.patches.LibraryService/GetPatchByNumber" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.library_service.get_patch_by_number()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `number`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LibraryServiceGetPatchByNumberResponse](../../models/libraryservicegetpatchbynumberresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_patch_capabilities

GetPatchCapabilities

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_GetPatchCapabilities" method="post" path="/textql.rpc.public.patches.LibraryService/GetPatchCapabilities" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.library_service.get_patch_capabilities()

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

**[models.LibraryServiceGetPatchCapabilitiesResponse](../../models/libraryservicegetpatchcapabilitiesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_library_entries

ListLibraryEntries

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_ListLibraryEntries" method="post" path="/textql.rpc.public.patches.LibraryService/ListLibraryEntries" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.library_service.list_library_entries()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `path`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `recursive`                                                         | *OptionalNullable[bool]*                                            | :heavy_minus_sign:                                                  | N/A                                                                 |
| `include_debug_files`                                               | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | when true, reserved files like OWNERS are included                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LibraryServiceListLibraryEntriesResponse](../../models/libraryservicelistlibraryentriesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_library_submodules

ListLibrarySubmodules

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_ListLibrarySubmodules" method="post" path="/textql.rpc.public.patches.LibraryService/ListLibrarySubmodules" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.library_service.list_library_submodules(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                       | Type                                                                                                                            | Required                                                                                                                        | Description                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                          | [models.TextqlRPCPublicPatchesListLibrarySubmodulesRequest](../../models/textqlrpcpublicpatcheslistlibrarysubmodulesrequest.md) | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `connect_timeout_ms`                                                                                                            | *Optional[float]*                                                                                                               | :heavy_minus_sign:                                                                                                              | N/A                                                                                                                             |
| `retries`                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                | :heavy_minus_sign:                                                                                                              | Configuration to override the default retry behavior of the client.                                                             |

### Response

**[models.LibraryServiceListLibrarySubmodulesResponse](../../models/libraryservicelistlibrarysubmodulesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_patches

ListPatches

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_ListPatches" method="post" path="/textql.rpc.public.patches.LibraryService/ListPatches" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.library_service.list_patches()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                | *Optional[float]*                                                                                   | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `page_size`                                                                                         | *OptionalNullable[int]*                                                                             | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `page_token`                                                                                        | *OptionalNullable[str]*                                                                             | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `statuses`                                                                                          | List[[models.TextqlRPCPublicPatchesPatchStatus](../../models/textqlrpcpublicpatchespatchstatus.md)] | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `include_auto_approved`                                                                             | *OptionalNullable[bool]*                                                                            | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.LibraryServiceListPatchesResponse](../../models/libraryservicelistpatchesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## migrate_legacy_context

MigrateLegacyContextToLibrary

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_MigrateLegacyContextToLibrary" method="post" path="/textql.rpc.public.patches.LibraryService/MigrateLegacyContextToLibrary" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.library_service.migrate_legacy_context()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dry_run`                                                           | *OptionalNullable[bool]*                                            | :heavy_minus_sign:                                                  | N/A                                                                 |
| `include_inactive`                                                  | *OptionalNullable[bool]*                                            | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LibraryServiceMigrateLegacyContextToLibraryResponse](../../models/libraryservicemigratelegacycontexttolibraryresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## migrate_ontology

MigrateOntologyToLibrary

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_MigrateOntologyToLibrary" method="post" path="/textql.rpc.public.patches.LibraryService/MigrateOntologyToLibrary" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.library_service.migrate_ontology()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `ontology_ids`                                                      | List[*int*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dry_run`                                                           | *OptionalNullable[bool]*                                            | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LibraryServiceMigrateOntologyToLibraryResponse](../../models/libraryservicemigrateontologytolibraryresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## pull_from_remote

PullLibraryFromRemote

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_PullLibraryFromRemote" method="post" path="/textql.rpc.public.patches.LibraryService/PullLibraryFromRemote" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.library_service.pull_from_remote()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `acknowledge_unrelated_histories`                                   | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `expected_local_head_hash`                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `expected_remote_head_hash`                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LibraryServicePullLibraryFromRemoteResponse](../../models/libraryservicepulllibraryfromremoteresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## remove_remote

RemoveLibraryRemote

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_RemoveLibraryRemote" method="post" path="/textql.rpc.public.patches.LibraryService/RemoveLibraryRemote" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.library_service.remove_remote(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                      | [models.TextqlRPCPublicPatchesRemoveLibraryRemoteRequest](../../models/textqlrpcpublicpatchesremovelibraryremoterequest.md) | :heavy_check_mark:                                                                                                          | N/A                                                                                                                         |
| `connect_timeout_ms`                                                                                                        | *Optional[float]*                                                                                                           | :heavy_minus_sign:                                                                                                          | N/A                                                                                                                         |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |

### Response

**[models.LibraryServiceRemoveLibraryRemoteResponse](../../models/libraryserviceremovelibraryremoteresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## resolve_sync_conflict

ResolveLibrarySyncConflict

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_ResolveLibrarySyncConflict" method="post" path="/textql.rpc.public.patches.LibraryService/ResolveLibrarySyncConflict" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.library_service.resolve_sync_conflict()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `conflict_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `resolved_content`                                                  | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LibraryServiceResolveLibrarySyncConflictResponse](../../models/libraryserviceresolvelibrarysyncconflictresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## trigger_config_drift_reconcile

TriggerConfigDriftReconcile forces an immediate config-sync catch-up for the
 caller's org: if the Library repo's live HEAD differs from the last
 reconciled commit, it enqueues a reconcile (otherwise no-op). The on-demand
 equivalent of waiting for the periodic drift scan.

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_TriggerConfigDriftReconcile" method="post" path="/textql.rpc.public.patches.LibraryService/TriggerConfigDriftReconcile" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.library_service.trigger_config_drift_reconcile(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                   | Type                                                                                                                                        | Required                                                                                                                                    | Description                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                                      | [models.TextqlRPCPublicPatchesTriggerConfigDriftReconcileRequest](../../models/textqlrpcpublicpatchestriggerconfigdriftreconcilerequest.md) | :heavy_check_mark:                                                                                                                          | N/A                                                                                                                                         |
| `connect_timeout_ms`                                                                                                                        | *Optional[float]*                                                                                                                           | :heavy_minus_sign:                                                                                                                          | N/A                                                                                                                                         |
| `retries`                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                            | :heavy_minus_sign:                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                         |

### Response

**[models.LibraryServiceTriggerConfigDriftReconcileResponse](../../models/libraryservicetriggerconfigdriftreconcileresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## update_library_sync_config

UpdateLibrarySyncConfig

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_UpdateLibrarySyncConfig" method="post" path="/textql.rpc.public.patches.LibraryService/UpdateLibrarySyncConfig" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.library_service.update_library_sync_config()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `sync_enabled`                                                      | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `sync_interval_minutes`                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LibraryServiceUpdateLibrarySyncConfigResponse](../../models/libraryserviceupdatelibrarysyncconfigresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |