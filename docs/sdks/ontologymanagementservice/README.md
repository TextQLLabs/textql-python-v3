# OntologyManagementService

## Overview

### Available Operations

* [ontology_management_service_add_ontology_submodule](#ontology_management_service_add_ontology_submodule) - AddOntologySubmodule
* [ontology_management_service_approve_patch](#ontology_management_service_approve_patch) - ApprovePatch
* [ontology_management_service_configure_ontology_remote](#ontology_management_service_configure_ontology_remote) - ConfigureOntologyRemote
* [ontology_management_service_create_approval_rule](#ontology_management_service_create_approval_rule) - CreateApprovalRule
* [ontology_management_service_create_context_patch_auto_approve_rule](#ontology_management_service_create_context_patch_auto_approve_rule) - CreateContextPatchAutoApproveRule
* [ontology_management_service_create_ontology_directory](#ontology_management_service_create_ontology_directory) - CreateOntologyDirectory
* [ontology_management_service_create_ontology_file_upload_url](#ontology_management_service_create_ontology_file_upload_url) - CreateOntologyFileUploadUrl
* [ontology_management_service_delete_approval_rule](#ontology_management_service_delete_approval_rule) - DeleteApprovalRule
* [ontology_management_service_delete_context_patch_auto_approve_rule](#ontology_management_service_delete_context_patch_auto_approve_rule) - DeleteContextPatchAutoApproveRule
* [ontology_management_service_delete_ontology_directory](#ontology_management_service_delete_ontology_directory) - DeleteOntologyDirectory
* [ontology_management_service_delete_ontology_file](#ontology_management_service_delete_ontology_file) - DeleteOntologyFile
* [ontology_management_service_delete_ontology_owners](#ontology_management_service_delete_ontology_owners) - DeleteOntologyOwners
* [ontology_management_service_deny_patch](#ontology_management_service_deny_patch) - DenyPatch
* [ontology_management_service_exchange_ontology_github_code](#ontology_management_service_exchange_ontology_github_code) - ExchangeOntologyGithubCode
* [ontology_management_service_finalize_ontology_file_upload](#ontology_management_service_finalize_ontology_file_upload) - FinalizeOntologyFileUpload
* [ontology_management_service_get_codeowner_coverage](#ontology_management_service_get_codeowner_coverage) - GetCodeownerCoverage
* [ontology_management_service_get_config_export_capabilities](#ontology_management_service_get_config_export_capabilities) - GetConfigExportCapabilities
* [ontology_management_service_get_effective_ontology_owners](#ontology_management_service_get_effective_ontology_owners) - GetEffectiveOntologyOwners
* [ontology_management_service_get_file_usage](#ontology_management_service_get_file_usage) - GetFileUsage
* [ontology_management_service_get_file_usage_timeline](#ontology_management_service_get_file_usage_timeline) - GetFileUsageTimeline
* [ontology_management_service_get_ontology_ana_config](#ontology_management_service_get_ontology_ana_config) - GetOntologyAnaConfig
* [ontology_management_service_get_ontology_file](#ontology_management_service_get_ontology_file) - GetOntologyFile
* [ontology_management_service_get_ontology_github_o_auth_url](#ontology_management_service_get_ontology_github_o_auth_url) - GetOntologyGithubOAuthURL
* [ontology_management_service_get_ontology_history_file_diff](#ontology_management_service_get_ontology_history_file_diff) - GetOntologyHistoryFileDiff
* [ontology_management_service_get_ontology_owners](#ontology_management_service_get_ontology_owners) - GetOntologyOwners
* [ontology_management_service_get_ontology_remote](#ontology_management_service_get_ontology_remote) - GetOntologyRemote
* [ontology_management_service_get_ontology_size_timeline](#ontology_management_service_get_ontology_size_timeline) - GetOntologySizeTimeline
* [ontology_management_service_get_ontology_sync_conflicts](#ontology_management_service_get_ontology_sync_conflicts) - GetOntologySyncConflicts
* [ontology_management_service_get_ontology_usage_summary](#ontology_management_service_get_ontology_usage_summary) - GetOntologyUsageSummary
* [ontology_management_service_get_patch](#ontology_management_service_get_patch) - GetPatch
* [ontology_management_service_get_patch_by_number](#ontology_management_service_get_patch_by_number) - GetPatchByNumber
* [ontology_management_service_get_patch_capabilities](#ontology_management_service_get_patch_capabilities) - GetPatchCapabilities
* [ontology_management_service_get_raw_patch](#ontology_management_service_get_raw_patch) - GetRawPatch
* [ontology_management_service_get_usage_details_for_file](#ontology_management_service_get_usage_details_for_file) - GetUsageDetailsForFile
* [ontology_management_service_list_approval_rules](#ontology_management_service_list_approval_rules) - ListApprovalRules
* [ontology_management_service_list_chats_for_file](#ontology_management_service_list_chats_for_file) - ListChatsForFile
* [ontology_management_service_list_context_patch_auto_approve_rules](#ontology_management_service_list_context_patch_auto_approve_rules) - ListContextPatchAutoApproveRules
* [ontology_management_service_list_golden_files](#ontology_management_service_list_golden_files) - ListGoldenFiles
* [ontology_management_service_list_ontology_entries](#ontology_management_service_list_ontology_entries) - ListOntologyEntries
* [ontology_management_service_list_ontology_history](#ontology_management_service_list_ontology_history) - ListOntologyHistory
* [ontology_management_service_list_ontology_imports](#ontology_management_service_list_ontology_imports) - ListOntologyImports
* [ontology_management_service_list_ontology_submodules](#ontology_management_service_list_ontology_submodules) - ListOntologySubmodules
* [ontology_management_service_list_ontology_sync_runs](#ontology_management_service_list_ontology_sync_runs) - ListOntologySyncRuns
* [ontology_management_service_list_patch_objects](#ontology_management_service_list_patch_objects) - ListPatchObjects parses the config objects present at a patch's git ref and  returns each object's Library path, resolved display name, and granular type  (e.g. "playbook", "dashboard/streamlit", "dashboard/dash"). Parse-only: it  reuses the snapshot-at-ref + parse steps the preview path performs before  spawning — no sandbox spawn, no run_as authorization, no persistence. The  frontend uses the dashboard subtype to decide previewability (streamlit/dash).
* [ontology_management_service_list_patch_reviewers](#ontology_management_service_list_patch_reviewers) - ListPatchReviewers
* [ontology_management_service_list_patches](#ontology_management_service_list_patches) - ListPatches
* [ontology_management_service_list_skills](#ontology_management_service_list_skills) - Lists the skills under the ontology's flat skills/ root that the caller can  read (OWNERS-filtered). Returns display metadata only — never instruction  bodies — feeding the chat composer's `/` autocomplete.
* [ontology_management_service_plan_ontology_merge](#ontology_management_service_plan_ontology_merge) - PlanOntologyMerge
* [ontology_management_service_preview_ontology_pull_from_remote](#ontology_management_service_preview_ontology_pull_from_remote) - PreviewOntologyPullFromRemote
* [ontology_management_service_pull_ontology_from_remote](#ontology_management_service_pull_ontology_from_remote) - PullOntologyFromRemote
* [ontology_management_service_push_ontology_to_remote](#ontology_management_service_push_ontology_to_remote) - PushOntologyToRemote
* [ontology_management_service_recover_ontology](#ontology_management_service_recover_ontology) - RecoverOntology
* [ontology_management_service_remove_ontology_remote](#ontology_management_service_remove_ontology_remote) - RemoveOntologyRemote
* [ontology_management_service_remove_ontology_submodule](#ontology_management_service_remove_ontology_submodule) - RemoveOntologySubmodule
* [ontology_management_service_rename_ontology_file](#ontology_management_service_rename_ontology_file) - RenameOntologyFile
* [ontology_management_service_request_patch_review](#ontology_management_service_request_patch_review) - RequestPatchReview
* [ontology_management_service_resolve_ontology_sync_conflict](#ontology_management_service_resolve_ontology_sync_conflict) - ResolveOntologySyncConflict
* [ontology_management_service_restore_patch](#ontology_management_service_restore_patch) - RestorePatch
* [ontology_management_service_revert_patch](#ontology_management_service_revert_patch) - RevertPatch
* [ontology_management_service_save_all_objects_as_config](#ontology_management_service_save_all_objects_as_config) - SaveAllObjectsAsConfig
* [ontology_management_service_save_object_as_config](#ontology_management_service_save_object_as_config) - SaveObjectAsConfig
* [ontology_management_service_set_ontology_file_golden](#ontology_management_service_set_ontology_file_golden) - SetOntologyFileGolden
* [ontology_management_service_trigger_config_drift_reconcile](#ontology_management_service_trigger_config_drift_reconcile) - TriggerConfigDriftReconcile forces an immediate config-sync catch-up for the  caller's org: if the Ontology repo's live HEAD differs from the last  reconciled commit, it enqueues a reconcile (otherwise no-op). The on-demand  equivalent of waiting for the periodic drift scan.
* [ontology_management_service_update_approval_rule](#ontology_management_service_update_approval_rule) - UpdateApprovalRule
* [ontology_management_service_update_context_patch_auto_approve_rule](#ontology_management_service_update_context_patch_auto_approve_rule) - UpdateContextPatchAutoApproveRule
* [ontology_management_service_update_ontology_sync_config](#ontology_management_service_update_ontology_sync_config) - UpdateOntologySyncConfig
* [ontology_management_service_upsert_ontology_ana_config](#ontology_management_service_upsert_ontology_ana_config) - UpsertOntologyAnaConfig
* [ontology_management_service_upsert_ontology_file](#ontology_management_service_upsert_ontology_file) - UpsertOntologyFile
* [ontology_management_service_upsert_ontology_owners](#ontology_management_service_upsert_ontology_owners) - UpsertOntologyOwners
* [ontology_management_service_validate_config](#ontology_management_service_validate_config) - Read-only functional validation of a proposed config: parse + dependency  resolution/reachability, no authorization and no persistence. "ok" means  functionally valid, not "guaranteed to merge" — the merge gate re-checks  authorization at approve time.

## ontology_management_service_add_ontology_submodule

AddOntologySubmodule

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_AddOntologySubmodule" method="post" path="/textql.rpc.public.patches.OntologyManagementService/AddOntologySubmodule" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_add_ontology_submodule()

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

**[models.OntologyManagementServiceAddOntologySubmoduleResponse](../../models/ontologymanagementserviceaddontologysubmoduleresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_approve_patch

ApprovePatch

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_ApprovePatch" method="post" path="/textql.rpc.public.patches.OntologyManagementService/ApprovePatch" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_approve_patch()

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

**[models.OntologyManagementServiceApprovePatchResponse](../../models/ontologymanagementserviceapprovepatchresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_configure_ontology_remote

ConfigureOntologyRemote

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_ConfigureOntologyRemote" method="post" path="/textql.rpc.public.patches.OntologyManagementService/ConfigureOntologyRemote" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_configure_ontology_remote()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `remote_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `auth_type`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `token`                                                             | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `ssh_private_key`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `ssh_key_password`                                                  | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `default_branch`                                                    | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `github_app_id`                                                     | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `github_app_installation_id`                                        | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `github_app_private_key`                                            | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `signing_key_type`                                                  | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `signing_key`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `push_mode`                                                         | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `use_hosted_github_app`                                             | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OntologyManagementServiceConfigureOntologyRemoteResponse](../../models/ontologymanagementserviceconfigureontologyremoteresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_create_approval_rule

CreateApprovalRule

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_CreateApprovalRule" method="post" path="/textql.rpc.public.patches.OntologyManagementService/CreateApprovalRule" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_create_approval_rule()

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

**[models.OntologyManagementServiceCreateApprovalRuleResponse](../../models/ontologymanagementservicecreateapprovalruleresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_create_context_patch_auto_approve_rule

CreateContextPatchAutoApproveRule

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_CreateContextPatchAutoApproveRule" method="post" path="/textql.rpc.public.patches.OntologyManagementService/CreateContextPatchAutoApproveRule" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_create_context_patch_auto_approve_rule()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                         | Type                                                                                                                                              | Required                                                                                                                                          | Description                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                              | *Optional[float]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                | N/A                                                                                                                                               |
| `rule`                                                                                                                                            | [Optional[models.TextqlRPCPublicPatchesContextPatchAutoApproveRuleInput]](../../models/textqlrpcpublicpatchescontextpatchautoapproveruleinput.md) | :heavy_minus_sign:                                                                                                                                | N/A                                                                                                                                               |
| `retries`                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                  | :heavy_minus_sign:                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                               |

### Response

**[models.OntologyManagementServiceCreateContextPatchAutoApproveRuleResponse](../../models/ontologymanagementservicecreatecontextpatchautoapproveruleresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_create_ontology_directory

CreateOntologyDirectory

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_CreateOntologyDirectory" method="post" path="/textql.rpc.public.patches.OntologyManagementService/CreateOntologyDirectory" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_create_ontology_directory()

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

**[models.OntologyManagementServiceCreateOntologyDirectoryResponse](../../models/ontologymanagementservicecreateontologydirectoryresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_create_ontology_file_upload_url

CreateOntologyFileUploadUrl

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_CreateOntologyFileUploadUrl" method="post" path="/textql.rpc.public.patches.OntologyManagementService/CreateOntologyFileUploadUrl" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_create_ontology_file_upload_url()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                                    | *Optional[float]*                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                      | N/A                                                                                                                                                                     |
| `path`                                                                                                                                                                  | *Optional[str]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | N/A                                                                                                                                                                     |
| `mime_type`                                                                                                                                                             | *Optional[str]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | N/A                                                                                                                                                                     |
| `size_bytes`                                                                                                                                                            | [Optional[models.TextqlRPCPublicPatchesCreateOntologyFileUploadURLRequestSizeBytes]](../../models/textqlrpcpublicpatchescreateontologyfileuploadurlrequestsizebytes.md) | :heavy_minus_sign:                                                                                                                                                      | N/A                                                                                                                                                                     |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.OntologyManagementServiceCreateOntologyFileUploadURLResponse](../../models/ontologymanagementservicecreateontologyfileuploadurlresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_delete_approval_rule

DeleteApprovalRule

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_DeleteApprovalRule" method="post" path="/textql.rpc.public.patches.OntologyManagementService/DeleteApprovalRule" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_delete_approval_rule()

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

**[models.OntologyManagementServiceDeleteApprovalRuleResponse](../../models/ontologymanagementservicedeleteapprovalruleresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_delete_context_patch_auto_approve_rule

DeleteContextPatchAutoApproveRule

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_DeleteContextPatchAutoApproveRule" method="post" path="/textql.rpc.public.patches.OntologyManagementService/DeleteContextPatchAutoApproveRule" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_delete_context_patch_auto_approve_rule()

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

**[models.OntologyManagementServiceDeleteContextPatchAutoApproveRuleResponse](../../models/ontologymanagementservicedeletecontextpatchautoapproveruleresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_delete_ontology_directory

DeleteOntologyDirectory

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_DeleteOntologyDirectory" method="post" path="/textql.rpc.public.patches.OntologyManagementService/DeleteOntologyDirectory" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_delete_ontology_directory()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                                                                                                                        | *Optional[float]*                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                         |
| `path`                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                         |
| `commit_message`                                                                                                                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                         |
| `recursive`                                                                                                                                                                                                                                                 | *Optional[bool]*                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                          | When true, delete the directory and all of its contents (files and<br/> subdirectories) in a single atomic commit. The caller must have write<br/> access to every nested subdirectory. When false (default), the directory<br/> must be empty of non-reserved entries. |
| `retries`                                                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                                                         |

### Response

**[models.OntologyManagementServiceDeleteOntologyDirectoryResponse](../../models/ontologymanagementservicedeleteontologydirectoryresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_delete_ontology_file

DeleteOntologyFile

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_DeleteOntologyFile" method="post" path="/textql.rpc.public.patches.OntologyManagementService/DeleteOntologyFile" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_delete_ontology_file()

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

**[models.OntologyManagementServiceDeleteOntologyFileResponse](../../models/ontologymanagementservicedeleteontologyfileresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_delete_ontology_owners

DeleteOntologyOwners

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_DeleteOntologyOwners" method="post" path="/textql.rpc.public.patches.OntologyManagementService/DeleteOntologyOwners" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_delete_ontology_owners()

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

**[models.OntologyManagementServiceDeleteOntologyOwnersResponse](../../models/ontologymanagementservicedeleteontologyownersresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_deny_patch

DenyPatch

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_DenyPatch" method="post" path="/textql.rpc.public.patches.OntologyManagementService/DenyPatch" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_deny_patch()

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

**[models.OntologyManagementServiceDenyPatchResponse](../../models/ontologymanagementservicedenypatchresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_exchange_ontology_github_code

ExchangeOntologyGithubCode

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_ExchangeOntologyGithubCode" method="post" path="/textql.rpc.public.patches.OntologyManagementService/ExchangeOntologyGithubCode" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_exchange_ontology_github_code()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `code`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `state`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `code_verifier`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OntologyManagementServiceExchangeOntologyGithubCodeResponse](../../models/ontologymanagementserviceexchangeontologygithubcoderesponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_finalize_ontology_file_upload

FinalizeOntologyFileUpload

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_FinalizeOntologyFileUpload" method="post" path="/textql.rpc.public.patches.OntologyManagementService/FinalizeOntologyFileUpload" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_finalize_ontology_file_upload()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `path`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `upload_key`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `commit_message`                                                    | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OntologyManagementServiceFinalizeOntologyFileUploadResponse](../../models/ontologymanagementservicefinalizeontologyfileuploadresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_get_codeowner_coverage

GetCodeownerCoverage

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_GetCodeownerCoverage" method="post" path="/textql.rpc.public.patches.OntologyManagementService/GetCodeownerCoverage" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_get_codeowner_coverage(body={})

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

**[models.OntologyManagementServiceGetCodeownerCoverageResponse](../../models/ontologymanagementservicegetcodeownercoverageresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_get_config_export_capabilities

GetConfigExportCapabilities

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_GetConfigExportCapabilities" method="post" path="/textql.rpc.public.patches.OntologyManagementService/GetConfigExportCapabilities" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_get_config_export_capabilities(body={})

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

**[models.OntologyManagementServiceGetConfigExportCapabilitiesResponse](../../models/ontologymanagementservicegetconfigexportcapabilitiesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_get_effective_ontology_owners

GetEffectiveOntologyOwners

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_GetEffectiveOntologyOwners" method="post" path="/textql.rpc.public.patches.OntologyManagementService/GetEffectiveOntologyOwners" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_get_effective_ontology_owners()

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

**[models.OntologyManagementServiceGetEffectiveOntologyOwnersResponse](../../models/ontologymanagementservicegeteffectiveontologyownersresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_get_file_usage

GetFileUsage

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_GetFileUsage" method="post" path="/textql.rpc.public.patches.OntologyManagementService/GetFileUsage" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_get_file_usage()

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
| `page_size`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | *OptionalNullable[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

### Response

**[models.OntologyManagementServiceGetFileUsageResponse](../../models/ontologymanagementservicegetfileusageresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_get_file_usage_timeline

GetFileUsageTimeline

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_GetFileUsageTimeline" method="post" path="/textql.rpc.public.patches.OntologyManagementService/GetFileUsageTimeline" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_get_file_usage_timeline()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | *Optional[float]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `path_prefix`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `observation_period`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | *Optional[timedelta]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | A Duration represents a signed, fixed-length span of time represented<br/> as a count of seconds and fractions of seconds at nanosecond<br/> resolution. It is independent of any calendar and concepts like "day"<br/> or "month". It is related to Timestamp in that the difference between<br/> two Timestamp values is a Duration and it can be added or subtracted<br/> from a Timestamp. Range is approximately +-10,000 years.<br/><br/> # Examples<br/><br/> Example 1: Compute Duration from two Timestamps in pseudo code.<br/><br/>     Timestamp start = ...;<br/>     Timestamp end = ...;<br/>     Duration duration = ...;<br/><br/>     duration.seconds = end.seconds - start.seconds;<br/>     duration.nanos = end.nanos - start.nanos;<br/><br/>     if (duration.seconds < 0 && duration.nanos > 0) {<br/>       duration.seconds += 1;<br/>       duration.nanos -= 1000000000;<br/>     } else if (duration.seconds > 0 && duration.nanos < 0) {<br/>       duration.seconds -= 1;<br/>       duration.nanos += 1000000000;<br/>     }<br/><br/> Example 2: Compute Timestamp from Timestamp + Duration in pseudo code.<br/><br/>     Timestamp start = ...;<br/>     Duration duration = ...;<br/>     Timestamp end = ...;<br/><br/>     end.seconds = start.seconds + duration.seconds;<br/>     end.nanos = start.nanos + duration.nanos;<br/><br/>     if (end.nanos < 0) {<br/>       end.seconds -= 1;<br/>       end.nanos += 1000000000;<br/>     } else if (end.nanos >= 1000000000) {<br/>       end.seconds += 1;<br/>       end.nanos -= 1000000000;<br/>     }<br/><br/> Example 3: Compute Duration from datetime.timedelta in Python.<br/><br/>     td = datetime.timedelta(days=3, minutes=10)<br/>     duration = Duration()<br/>     duration.FromTimedelta(td)<br/><br/> # JSON Mapping<br/><br/> In JSON format, the Duration type is encoded as a string rather than an<br/> object, where the string ends in the suffix "s" (indicating seconds) and<br/> is preceded by the number of seconds, with nanoseconds expressed as<br/> fractional seconds. For example, 3 seconds with 0 nanoseconds should be<br/> encoded in JSON format as "3s", while 3 seconds and 1 nanosecond should<br/> be expressed in JSON format as "3.000000001s", and 3 seconds and 1<br/> microsecond should be expressed in JSON format as "3.000001s". |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

### Response

**[models.OntologyManagementServiceGetFileUsageTimelineResponse](../../models/ontologymanagementservicegetfileusagetimelineresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_get_ontology_ana_config

GetOntologyAnaConfig

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_GetOntologyAnaConfig" method="post" path="/textql.rpc.public.patches.OntologyManagementService/GetOntologyAnaConfig" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_get_ontology_ana_config()

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

**[models.OntologyManagementServiceGetOntologyAnaConfigResponse](../../models/ontologymanagementservicegetontologyanaconfigresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_get_ontology_file

GetOntologyFile

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_GetOntologyFile" method="post" path="/textql.rpc.public.patches.OntologyManagementService/GetOntologyFile" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_get_ontology_file()

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

**[models.OntologyManagementServiceGetOntologyFileResponse](../../models/ontologymanagementservicegetontologyfileresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_get_ontology_github_o_auth_url

GetOntologyGithubOAuthURL

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_GetOntologyGithubOAuthURL" method="post" path="/textql.rpc.public.patches.OntologyManagementService/GetOntologyGithubOAuthURL" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_get_ontology_github_o_auth_url()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `state`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `code_challenge`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OntologyManagementServiceGetOntologyGithubOAuthURLResponse](../../models/ontologymanagementservicegetontologygithuboauthurlresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_get_ontology_history_file_diff

GetOntologyHistoryFileDiff

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_GetOntologyHistoryFileDiff" method="post" path="/textql.rpc.public.patches.OntologyManagementService/GetOntologyHistoryFileDiff" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_get_ontology_history_file_diff()

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

**[models.OntologyManagementServiceGetOntologyHistoryFileDiffResponse](../../models/ontologymanagementservicegetontologyhistoryfilediffresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_get_ontology_owners

GetOntologyOwners

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_GetOntologyOwners" method="post" path="/textql.rpc.public.patches.OntologyManagementService/GetOntologyOwners" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_get_ontology_owners()

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

**[models.OntologyManagementServiceGetOntologyOwnersResponse](../../models/ontologymanagementservicegetontologyownersresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_get_ontology_remote

GetOntologyRemote

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_GetOntologyRemote" method="post" path="/textql.rpc.public.patches.OntologyManagementService/GetOntologyRemote" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_get_ontology_remote(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                  | [models.TextqlRPCPublicPatchesGetOntologyRemoteRequest](../../models/textqlrpcpublicpatchesgetontologyremoterequest.md) | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `connect_timeout_ms`                                                                                                    | *Optional[float]*                                                                                                       | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |

### Response

**[models.OntologyManagementServiceGetOntologyRemoteResponse](../../models/ontologymanagementservicegetontologyremoteresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_get_ontology_size_timeline

GetOntologySizeTimeline

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_GetOntologySizeTimeline" method="post" path="/textql.rpc.public.patches.OntologyManagementService/GetOntologySizeTimeline" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_get_ontology_size_timeline()

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

**[models.OntologyManagementServiceGetOntologySizeTimelineResponse](../../models/ontologymanagementservicegetontologysizetimelineresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_get_ontology_sync_conflicts

GetOntologySyncConflicts

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_GetOntologySyncConflicts" method="post" path="/textql.rpc.public.patches.OntologyManagementService/GetOntologySyncConflicts" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_get_ontology_sync_conflicts(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                             | Type                                                                                                                                  | Required                                                                                                                              | Description                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                                | [models.TextqlRPCPublicPatchesGetOntologySyncConflictsRequest](../../models/textqlrpcpublicpatchesgetontologysyncconflictsrequest.md) | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `connect_timeout_ms`                                                                                                                  | *Optional[float]*                                                                                                                     | :heavy_minus_sign:                                                                                                                    | N/A                                                                                                                                   |
| `retries`                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                      | :heavy_minus_sign:                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                   |

### Response

**[models.OntologyManagementServiceGetOntologySyncConflictsResponse](../../models/ontologymanagementservicegetontologysyncconflictsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_get_ontology_usage_summary

GetOntologyUsageSummary

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_GetOntologyUsageSummary" method="post" path="/textql.rpc.public.patches.OntologyManagementService/GetOntologyUsageSummary" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_get_ontology_usage_summary()

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

**[models.OntologyManagementServiceGetOntologyUsageSummaryResponse](../../models/ontologymanagementservicegetontologyusagesummaryresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_get_patch

GetPatch

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_GetPatch" method="post" path="/textql.rpc.public.patches.OntologyManagementService/GetPatch" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_get_patch()

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

**[models.OntologyManagementServiceGetPatchResponse](../../models/ontologymanagementservicegetpatchresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_get_patch_by_number

GetPatchByNumber

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_GetPatchByNumber" method="post" path="/textql.rpc.public.patches.OntologyManagementService/GetPatchByNumber" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_get_patch_by_number()

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

**[models.OntologyManagementServiceGetPatchByNumberResponse](../../models/ontologymanagementservicegetpatchbynumberresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_get_patch_capabilities

GetPatchCapabilities

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_GetPatchCapabilities" method="post" path="/textql.rpc.public.patches.OntologyManagementService/GetPatchCapabilities" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_get_patch_capabilities()

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

**[models.OntologyManagementServiceGetPatchCapabilitiesResponse](../../models/ontologymanagementservicegetpatchcapabilitiesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_get_raw_patch

GetRawPatch

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_GetRawPatch" method="post" path="/textql.rpc.public.patches.OntologyManagementService/GetRawPatch" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_get_raw_patch()

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

**[models.OntologyManagementServiceGetRawPatchResponse](../../models/ontologymanagementservicegetrawpatchresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_get_usage_details_for_file

GetUsageDetailsForFile

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_GetUsageDetailsForFile" method="post" path="/textql.rpc.public.patches.OntologyManagementService/GetUsageDetailsForFile" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_get_usage_details_for_file()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | *Optional[float]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `file_path`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `observation_period`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | *Optional[timedelta]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | A Duration represents a signed, fixed-length span of time represented<br/> as a count of seconds and fractions of seconds at nanosecond<br/> resolution. It is independent of any calendar and concepts like "day"<br/> or "month". It is related to Timestamp in that the difference between<br/> two Timestamp values is a Duration and it can be added or subtracted<br/> from a Timestamp. Range is approximately +-10,000 years.<br/><br/> # Examples<br/><br/> Example 1: Compute Duration from two Timestamps in pseudo code.<br/><br/>     Timestamp start = ...;<br/>     Timestamp end = ...;<br/>     Duration duration = ...;<br/><br/>     duration.seconds = end.seconds - start.seconds;<br/>     duration.nanos = end.nanos - start.nanos;<br/><br/>     if (duration.seconds < 0 && duration.nanos > 0) {<br/>       duration.seconds += 1;<br/>       duration.nanos -= 1000000000;<br/>     } else if (duration.seconds > 0 && duration.nanos < 0) {<br/>       duration.seconds -= 1;<br/>       duration.nanos += 1000000000;<br/>     }<br/><br/> Example 2: Compute Timestamp from Timestamp + Duration in pseudo code.<br/><br/>     Timestamp start = ...;<br/>     Duration duration = ...;<br/>     Timestamp end = ...;<br/><br/>     end.seconds = start.seconds + duration.seconds;<br/>     end.nanos = start.nanos + duration.nanos;<br/><br/>     if (end.nanos < 0) {<br/>       end.seconds -= 1;<br/>       end.nanos += 1000000000;<br/>     } else if (end.nanos >= 1000000000) {<br/>       end.seconds += 1;<br/>       end.nanos -= 1000000000;<br/>     }<br/><br/> Example 3: Compute Duration from datetime.timedelta in Python.<br/><br/>     td = datetime.timedelta(days=3, minutes=10)<br/>     duration = Duration()<br/>     duration.FromTimedelta(td)<br/><br/> # JSON Mapping<br/><br/> In JSON format, the Duration type is encoded as a string rather than an<br/> object, where the string ends in the suffix "s" (indicating seconds) and<br/> is preceded by the number of seconds, with nanoseconds expressed as<br/> fractional seconds. For example, 3 seconds with 0 nanoseconds should be<br/> encoded in JSON format as "3s", while 3 seconds and 1 nanosecond should<br/> be expressed in JSON format as "3.000000001s", and 3 seconds and 1<br/> microsecond should be expressed in JSON format as "3.000001s". |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

### Response

**[models.OntologyManagementServiceGetUsageDetailsForFileResponse](../../models/ontologymanagementservicegetusagedetailsforfileresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_list_approval_rules

ListApprovalRules

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_ListApprovalRules" method="post" path="/textql.rpc.public.patches.OntologyManagementService/ListApprovalRules" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_list_approval_rules(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                  | [models.TextqlRPCPublicPatchesListApprovalRulesRequest](../../models/textqlrpcpublicpatcheslistapprovalrulesrequest.md) | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `connect_timeout_ms`                                                                                                    | *Optional[float]*                                                                                                       | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |

### Response

**[models.OntologyManagementServiceListApprovalRulesResponse](../../models/ontologymanagementservicelistapprovalrulesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_list_chats_for_file

ListChatsForFile

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_ListChatsForFile" method="post" path="/textql.rpc.public.patches.OntologyManagementService/ListChatsForFile" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_list_chats_for_file()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | *Optional[float]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `file_path`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `observation_period`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | *Optional[timedelta]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | A Duration represents a signed, fixed-length span of time represented<br/> as a count of seconds and fractions of seconds at nanosecond<br/> resolution. It is independent of any calendar and concepts like "day"<br/> or "month". It is related to Timestamp in that the difference between<br/> two Timestamp values is a Duration and it can be added or subtracted<br/> from a Timestamp. Range is approximately +-10,000 years.<br/><br/> # Examples<br/><br/> Example 1: Compute Duration from two Timestamps in pseudo code.<br/><br/>     Timestamp start = ...;<br/>     Timestamp end = ...;<br/>     Duration duration = ...;<br/><br/>     duration.seconds = end.seconds - start.seconds;<br/>     duration.nanos = end.nanos - start.nanos;<br/><br/>     if (duration.seconds < 0 && duration.nanos > 0) {<br/>       duration.seconds += 1;<br/>       duration.nanos -= 1000000000;<br/>     } else if (duration.seconds > 0 && duration.nanos < 0) {<br/>       duration.seconds -= 1;<br/>       duration.nanos += 1000000000;<br/>     }<br/><br/> Example 2: Compute Timestamp from Timestamp + Duration in pseudo code.<br/><br/>     Timestamp start = ...;<br/>     Duration duration = ...;<br/>     Timestamp end = ...;<br/><br/>     end.seconds = start.seconds + duration.seconds;<br/>     end.nanos = start.nanos + duration.nanos;<br/><br/>     if (end.nanos < 0) {<br/>       end.seconds -= 1;<br/>       end.nanos += 1000000000;<br/>     } else if (end.nanos >= 1000000000) {<br/>       end.seconds += 1;<br/>       end.nanos -= 1000000000;<br/>     }<br/><br/> Example 3: Compute Duration from datetime.timedelta in Python.<br/><br/>     td = datetime.timedelta(days=3, minutes=10)<br/>     duration = Duration()<br/>     duration.FromTimedelta(td)<br/><br/> # JSON Mapping<br/><br/> In JSON format, the Duration type is encoded as a string rather than an<br/> object, where the string ends in the suffix "s" (indicating seconds) and<br/> is preceded by the number of seconds, with nanoseconds expressed as<br/> fractional seconds. For example, 3 seconds with 0 nanoseconds should be<br/> encoded in JSON format as "3s", while 3 seconds and 1 nanosecond should<br/> be expressed in JSON format as "3.000000001s", and 3 seconds and 1<br/> microsecond should be expressed in JSON format as "3.000001s". |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *OptionalNullable[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

### Response

**[models.OntologyManagementServiceListChatsForFileResponse](../../models/ontologymanagementservicelistchatsforfileresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_list_context_patch_auto_approve_rules

ListContextPatchAutoApproveRules

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_ListContextPatchAutoApproveRules" method="post" path="/textql.rpc.public.patches.OntologyManagementService/ListContextPatchAutoApproveRules" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_list_context_patch_auto_approve_rules(body={})

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

**[models.OntologyManagementServiceListContextPatchAutoApproveRulesResponse](../../models/ontologymanagementservicelistcontextpatchautoapproverulesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_list_golden_files

ListGoldenFiles

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_ListGoldenFiles" method="post" path="/textql.rpc.public.patches.OntologyManagementService/ListGoldenFiles" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_list_golden_files(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                              | [models.TextqlRPCPublicPatchesListGoldenFilesRequest](../../models/textqlrpcpublicpatcheslistgoldenfilesrequest.md) | :heavy_check_mark:                                                                                                  | N/A                                                                                                                 |
| `connect_timeout_ms`                                                                                                | *Optional[float]*                                                                                                   | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |

### Response

**[models.OntologyManagementServiceListGoldenFilesResponse](../../models/ontologymanagementservicelistgoldenfilesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_list_ontology_entries

ListOntologyEntries

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_ListOntologyEntries" method="post" path="/textql.rpc.public.patches.OntologyManagementService/ListOntologyEntries" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_list_ontology_entries()

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

**[models.OntologyManagementServiceListOntologyEntriesResponse](../../models/ontologymanagementservicelistontologyentriesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_list_ontology_history

ListOntologyHistory

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_ListOntologyHistory" method="post" path="/textql.rpc.public.patches.OntologyManagementService/ListOntologyHistory" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_list_ontology_history()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page_size`                                                         | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page_token`                                                        | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `path`                                                              | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OntologyManagementServiceListOntologyHistoryResponse](../../models/ontologymanagementservicelistontologyhistoryresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_list_ontology_imports

ListOntologyImports

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_ListOntologyImports" method="post" path="/textql.rpc.public.patches.OntologyManagementService/ListOntologyImports" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_list_ontology_imports(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                      | [models.TextqlRPCPublicPatchesListOntologyImportsRequest](../../models/textqlrpcpublicpatcheslistontologyimportsrequest.md) | :heavy_check_mark:                                                                                                          | N/A                                                                                                                         |
| `connect_timeout_ms`                                                                                                        | *Optional[float]*                                                                                                           | :heavy_minus_sign:                                                                                                          | N/A                                                                                                                         |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |

### Response

**[models.OntologyManagementServiceListOntologyImportsResponse](../../models/ontologymanagementservicelistontologyimportsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_list_ontology_submodules

ListOntologySubmodules

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_ListOntologySubmodules" method="post" path="/textql.rpc.public.patches.OntologyManagementService/ListOntologySubmodules" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_list_ontology_submodules(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                         | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                            | [models.TextqlRPCPublicPatchesListOntologySubmodulesRequest](../../models/textqlrpcpublicpatcheslistontologysubmodulesrequest.md) | :heavy_check_mark:                                                                                                                | N/A                                                                                                                               |
| `connect_timeout_ms`                                                                                                              | *Optional[float]*                                                                                                                 | :heavy_minus_sign:                                                                                                                | N/A                                                                                                                               |
| `retries`                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                  | :heavy_minus_sign:                                                                                                                | Configuration to override the default retry behavior of the client.                                                               |

### Response

**[models.OntologyManagementServiceListOntologySubmodulesResponse](../../models/ontologymanagementservicelistontologysubmodulesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_list_ontology_sync_runs

ListOntologySyncRuns

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_ListOntologySyncRuns" method="post" path="/textql.rpc.public.patches.OntologyManagementService/ListOntologySyncRuns" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_list_ontology_sync_runs()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page_size`                                                         | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page_token`                                                        | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OntologyManagementServiceListOntologySyncRunsResponse](../../models/ontologymanagementservicelistontologysyncrunsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_list_patch_objects

ListPatchObjects parses the config objects present at a patch's git ref and
 returns each object's Library path, resolved display name, and granular type
 (e.g. "playbook", "dashboard/streamlit", "dashboard/dash"). Parse-only: it
 reuses the snapshot-at-ref + parse steps the preview path performs before
 spawning — no sandbox spawn, no run_as authorization, no persistence. The
 frontend uses the dashboard subtype to decide previewability (streamlit/dash).

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_ListPatchObjects" method="post" path="/textql.rpc.public.patches.OntologyManagementService/ListPatchObjects" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_list_patch_objects()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `patch_ref`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | git ref of the patch to inspect                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OntologyManagementServiceListPatchObjectsResponse](../../models/ontologymanagementservicelistpatchobjectsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_list_patch_reviewers

ListPatchReviewers

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_ListPatchReviewers" method="post" path="/textql.rpc.public.patches.OntologyManagementService/ListPatchReviewers" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_list_patch_reviewers()

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

**[models.OntologyManagementServiceListPatchReviewersResponse](../../models/ontologymanagementservicelistpatchreviewersresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_list_patches

ListPatches

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_ListPatches" method="post" path="/textql.rpc.public.patches.OntologyManagementService/ListPatches" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_list_patches()

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

**[models.OntologyManagementServiceListPatchesResponse](../../models/ontologymanagementservicelistpatchesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_list_skills

Lists the skills under the ontology's flat skills/ root that the caller can
 read (OWNERS-filtered). Returns display metadata only — never instruction
 bodies — feeding the chat composer's `/` autocomplete.

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_ListSkills" method="post" path="/textql.rpc.public.patches.OntologyManagementService/ListSkills" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_list_skills(body={})

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

**[models.OntologyManagementServiceListSkillsResponse](../../models/ontologymanagementservicelistskillsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_plan_ontology_merge

PlanOntologyMerge

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_PlanOntologyMerge" method="post" path="/textql.rpc.public.patches.OntologyManagementService/PlanOntologyMerge" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_plan_ontology_merge(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                  | [models.TextqlRPCPublicPatchesPlanOntologyMergeRequest](../../models/textqlrpcpublicpatchesplanontologymergerequest.md) | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `connect_timeout_ms`                                                                                                    | *Optional[float]*                                                                                                       | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |

### Response

**[models.OntologyManagementServicePlanOntologyMergeResponse](../../models/ontologymanagementserviceplanontologymergeresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_preview_ontology_pull_from_remote

PreviewOntologyPullFromRemote

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_PreviewOntologyPullFromRemote" method="post" path="/textql.rpc.public.patches.OntologyManagementService/PreviewOntologyPullFromRemote" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_preview_ontology_pull_from_remote(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                       | Type                                                                                                                                            | Required                                                                                                                                        | Description                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                                          | [models.TextqlRPCPublicPatchesPreviewOntologyPullFromRemoteRequest](../../models/textqlrpcpublicpatchespreviewontologypullfromremoterequest.md) | :heavy_check_mark:                                                                                                                              | N/A                                                                                                                                             |
| `connect_timeout_ms`                                                                                                                            | *Optional[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                              | N/A                                                                                                                                             |
| `retries`                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                | :heavy_minus_sign:                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                             |

### Response

**[models.OntologyManagementServicePreviewOntologyPullFromRemoteResponse](../../models/ontologymanagementservicepreviewontologypullfromremoteresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_pull_ontology_from_remote

PullOntologyFromRemote

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_PullOntologyFromRemote" method="post" path="/textql.rpc.public.patches.OntologyManagementService/PullOntologyFromRemote" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_pull_ontology_from_remote()

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

**[models.OntologyManagementServicePullOntologyFromRemoteResponse](../../models/ontologymanagementservicepullontologyfromremoteresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_push_ontology_to_remote

PushOntologyToRemote

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_PushOntologyToRemote" method="post" path="/textql.rpc.public.patches.OntologyManagementService/PushOntologyToRemote" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_push_ontology_to_remote(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                     | Type                                                                                                                          | Required                                                                                                                      | Description                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                        | [models.TextqlRPCPublicPatchesPushOntologyToRemoteRequest](../../models/textqlrpcpublicpatchespushontologytoremoterequest.md) | :heavy_check_mark:                                                                                                            | N/A                                                                                                                           |
| `connect_timeout_ms`                                                                                                          | *Optional[float]*                                                                                                             | :heavy_minus_sign:                                                                                                            | N/A                                                                                                                           |
| `retries`                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                              | :heavy_minus_sign:                                                                                                            | Configuration to override the default retry behavior of the client.                                                           |

### Response

**[models.OntologyManagementServicePushOntologyToRemoteResponse](../../models/ontologymanagementservicepushontologytoremoteresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_recover_ontology

RecoverOntology

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_RecoverOntology" method="post" path="/textql.rpc.public.patches.OntologyManagementService/RecoverOntology" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_recover_ontology()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                      | *Optional[float]*                                                                                                         | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `level`                                                                                                                   | [Optional[models.TextqlRPCPublicPatchesRecoverOntologyLevel]](../../models/textqlrpcpublicpatchesrecoverontologylevel.md) | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |

### Response

**[models.OntologyManagementServiceRecoverOntologyResponse](../../models/ontologymanagementservicerecoverontologyresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_remove_ontology_remote

RemoveOntologyRemote

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_RemoveOntologyRemote" method="post" path="/textql.rpc.public.patches.OntologyManagementService/RemoveOntologyRemote" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_remove_ontology_remote(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                     | Type                                                                                                                          | Required                                                                                                                      | Description                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                        | [models.TextqlRPCPublicPatchesRemoveOntologyRemoteRequest](../../models/textqlrpcpublicpatchesremoveontologyremoterequest.md) | :heavy_check_mark:                                                                                                            | N/A                                                                                                                           |
| `connect_timeout_ms`                                                                                                          | *Optional[float]*                                                                                                             | :heavy_minus_sign:                                                                                                            | N/A                                                                                                                           |
| `retries`                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                              | :heavy_minus_sign:                                                                                                            | Configuration to override the default retry behavior of the client.                                                           |

### Response

**[models.OntologyManagementServiceRemoveOntologyRemoteResponse](../../models/ontologymanagementserviceremoveontologyremoteresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_remove_ontology_submodule

RemoveOntologySubmodule

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_RemoveOntologySubmodule" method="post" path="/textql.rpc.public.patches.OntologyManagementService/RemoveOntologySubmodule" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_remove_ontology_submodule()

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

**[models.OntologyManagementServiceRemoveOntologySubmoduleResponse](../../models/ontologymanagementserviceremoveontologysubmoduleresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_rename_ontology_file

RenameOntologyFile

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_RenameOntologyFile" method="post" path="/textql.rpc.public.patches.OntologyManagementService/RenameOntologyFile" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_rename_ontology_file()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `old_path`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `new_path`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `commit_message`                                                    | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OntologyManagementServiceRenameOntologyFileResponse](../../models/ontologymanagementservicerenameontologyfileresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_request_patch_review

RequestPatchReview

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_RequestPatchReview" method="post" path="/textql.rpc.public.patches.OntologyManagementService/RequestPatchReview" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_request_patch_review()

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

**[models.OntologyManagementServiceRequestPatchReviewResponse](../../models/ontologymanagementservicerequestpatchreviewresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_resolve_ontology_sync_conflict

ResolveOntologySyncConflict

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_ResolveOntologySyncConflict" method="post" path="/textql.rpc.public.patches.OntologyManagementService/ResolveOntologySyncConflict" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_resolve_ontology_sync_conflict()

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

**[models.OntologyManagementServiceResolveOntologySyncConflictResponse](../../models/ontologymanagementserviceresolveontologysyncconflictresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_restore_patch

RestorePatch

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_RestorePatch" method="post" path="/textql.rpc.public.patches.OntologyManagementService/RestorePatch" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_restore_patch()

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

**[models.OntologyManagementServiceRestorePatchResponse](../../models/ontologymanagementservicerestorepatchresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_revert_patch

RevertPatch

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_RevertPatch" method="post" path="/textql.rpc.public.patches.OntologyManagementService/RevertPatch" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_revert_patch()

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

**[models.OntologyManagementServiceRevertPatchResponse](../../models/ontologymanagementservicerevertpatchresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_save_all_objects_as_config

SaveAllObjectsAsConfig

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_SaveAllObjectsAsConfig" method="post" path="/textql.rpc.public.patches.OntologyManagementService/SaveAllObjectsAsConfig" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_save_all_objects_as_config()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `object_type`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OntologyManagementServiceSaveAllObjectsAsConfigResponse](../../models/ontologymanagementservicesaveallobjectsasconfigresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_save_object_as_config

SaveObjectAsConfig

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_SaveObjectAsConfig" method="post" path="/textql.rpc.public.patches.OntologyManagementService/SaveObjectAsConfig" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_save_object_as_config()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `object_type`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `object_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OntologyManagementServiceSaveObjectAsConfigResponse](../../models/ontologymanagementservicesaveobjectasconfigresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_set_ontology_file_golden

SetOntologyFileGolden

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_SetOntologyFileGolden" method="post" path="/textql.rpc.public.patches.OntologyManagementService/SetOntologyFileGolden" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_set_ontology_file_golden()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `path`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `golden`                                                            | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | true = certify, false = retire                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OntologyManagementServiceSetOntologyFileGoldenResponse](../../models/ontologymanagementservicesetontologyfilegoldenresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_trigger_config_drift_reconcile

TriggerConfigDriftReconcile forces an immediate config-sync catch-up for the
 caller's org: if the Ontology repo's live HEAD differs from the last
 reconciled commit, it enqueues a reconcile (otherwise no-op). The on-demand
 equivalent of waiting for the periodic drift scan.

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_TriggerConfigDriftReconcile" method="post" path="/textql.rpc.public.patches.OntologyManagementService/TriggerConfigDriftReconcile" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_trigger_config_drift_reconcile(body={})

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

**[models.OntologyManagementServiceTriggerConfigDriftReconcileResponse](../../models/ontologymanagementservicetriggerconfigdriftreconcileresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_update_approval_rule

UpdateApprovalRule

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_UpdateApprovalRule" method="post" path="/textql.rpc.public.patches.OntologyManagementService/UpdateApprovalRule" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_update_approval_rule()

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

**[models.OntologyManagementServiceUpdateApprovalRuleResponse](../../models/ontologymanagementserviceupdateapprovalruleresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_update_context_patch_auto_approve_rule

UpdateContextPatchAutoApproveRule

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_UpdateContextPatchAutoApproveRule" method="post" path="/textql.rpc.public.patches.OntologyManagementService/UpdateContextPatchAutoApproveRule" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_update_context_patch_auto_approve_rule()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                         | Type                                                                                                                                              | Required                                                                                                                                          | Description                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                              | *Optional[float]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                | N/A                                                                                                                                               |
| `id`                                                                                                                                              | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | N/A                                                                                                                                               |
| `rule`                                                                                                                                            | [Optional[models.TextqlRPCPublicPatchesContextPatchAutoApproveRuleInput]](../../models/textqlrpcpublicpatchescontextpatchautoapproveruleinput.md) | :heavy_minus_sign:                                                                                                                                | N/A                                                                                                                                               |
| `retries`                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                  | :heavy_minus_sign:                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                               |

### Response

**[models.OntologyManagementServiceUpdateContextPatchAutoApproveRuleResponse](../../models/ontologymanagementserviceupdatecontextpatchautoapproveruleresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_update_ontology_sync_config

UpdateOntologySyncConfig

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_UpdateOntologySyncConfig" method="post" path="/textql.rpc.public.patches.OntologyManagementService/UpdateOntologySyncConfig" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_update_ontology_sync_config()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `sync_enabled`                                                      | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `sync_interval_minutes`                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `push_mode`                                                         | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OntologyManagementServiceUpdateOntologySyncConfigResponse](../../models/ontologymanagementserviceupdateontologysyncconfigresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_upsert_ontology_ana_config

UpsertOntologyAnaConfig

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_UpsertOntologyAnaConfig" method="post" path="/textql.rpc.public.patches.OntologyManagementService/UpsertOntologyAnaConfig" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_upsert_ontology_ana_config()

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

**[models.OntologyManagementServiceUpsertOntologyAnaConfigResponse](../../models/ontologymanagementserviceupsertontologyanaconfigresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_upsert_ontology_file

UpsertOntologyFile

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_UpsertOntologyFile" method="post" path="/textql.rpc.public.patches.OntologyManagementService/UpsertOntologyFile" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_upsert_ontology_file()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `path`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `content`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `commit_message`                                                    | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OntologyManagementServiceUpsertOntologyFileResponse](../../models/ontologymanagementserviceupsertontologyfileresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_upsert_ontology_owners

UpsertOntologyOwners

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_UpsertOntologyOwners" method="post" path="/textql.rpc.public.patches.OntologyManagementService/UpsertOntologyOwners" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_upsert_ontology_owners()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                              | *Optional[float]*                                                                                                 | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `path`                                                                                                            | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `role_ids`                                                                                                        | List[*str*]                                                                                                       | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `permissions`                                                                                                     | List[[models.TextqlRPCPublicPatchesOntologyPermission](../../models/textqlrpcpublicpatchesontologypermission.md)] | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `commit_message`                                                                                                  | *OptionalNullable[str]*                                                                                           | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[models.OntologyManagementServiceUpsertOntologyOwnersResponse](../../models/ontologymanagementserviceupsertontologyownersresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## ontology_management_service_validate_config

Read-only functional validation of a proposed config: parse + dependency
 resolution/reachability, no authorization and no persistence. "ok" means
 functionally valid, not "guaranteed to merge" — the merge gate re-checks
 authorization at approve time.

### Example Usage

<!-- UsageSnippet language="python" operationID="OntologyManagementService_ValidateConfig" method="post" path="/textql.rpc.public.patches.OntologyManagementService/ValidateConfig" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.ontology_management_service.ontology_management_service_validate_config()

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

**[models.OntologyManagementServiceValidateConfigResponse](../../models/ontologymanagementservicevalidateconfigresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |