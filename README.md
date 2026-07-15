# textql

Developer-friendly & type-safe Python SDK specifically catered to leverage *textql* API.

[![Built by Speakeasy](https://img.shields.io/badge/Built_by-SPEAKEASY-374151?style=for-the-badge&labelColor=f3f4f6)](https://www.speakeasy.com/?utm_source=textql&utm_campaign=python)
[![License: MIT](https://img.shields.io/badge/LICENSE_//_MIT-3b5bdb?style=for-the-badge&labelColor=eff6ff)](https://opensource.org/licenses/MIT)


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/textql/home). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary

TextQL API: TextQL public API. Generated from protobuf service definitions; internal
endpoints are excluded via google.api.visibility / file_visibility.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [textql](#textql)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add git+<UNSET>.git
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+<UNSET>.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+<UNSET>.git
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from textql-sdk python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "textql-sdk",
# ]
# ///

from textql_sdk import TextQL

sdk = TextQL(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.agent_services.create()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from textql_sdk import TextQL

async def main():

    async with TextQL() as text_ql:

        res = await text_ql.agent_services.create_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [Agents](docs/sdks/agents/README.md)

* [delete](docs/sdks/agents/README.md#delete) - DeleteAgent
* [list_runs](docs/sdks/agents/README.md#list_runs) - ListAgentRuns
* [list](docs/sdks/agents/README.md#list) - ListAgents
* [reset_agent_avatar](docs/sdks/agents/README.md#reset_agent_avatar) - ResetAgentAvatar
* [update](docs/sdks/agents/README.md#update) - UpdateAgent

### [AgentService](docs/sdks/agentservice/README.md)

* [duplicate](docs/sdks/agentservice/README.md#duplicate) - DuplicateAgent
* [trigger_agent](docs/sdks/agentservice/README.md#trigger_agent) - TriggerAgent

### [AgentServices](docs/sdks/agentservices/README.md)

* [create](docs/sdks/agentservices/README.md#create) - CreateAgent
* [get_agent](docs/sdks/agentservices/README.md#get_agent) - GetAgent
* [get_run](docs/sdks/agentservices/README.md#get_run) - GetAgentRun
* [upload_agent_avatar](docs/sdks/agentservices/README.md#upload_agent_avatar) - UploadAgentAvatar

### [Apps](docs/sdks/apps/README.md)

* [duplicate](docs/sdks/apps/README.md#duplicate) - Duplicates an app the caller can view into a new draft app they own,  named "Copy of <name>". Copies code/files/data sources/compute functions/  schedule; never carries over the source's published state or data snapshot.
* [get](docs/sdks/apps/README.md#get) - GetApp
* [get_component_gallery_url](docs/sdks/apps/README.md#get_component_gallery_url) - Staff-only (superadmin gated in-handler): publishes the embedded component  gallery as an app tree and returns its signed viewer URL.
* [get_members_with_apps](docs/sdks/apps/README.md#get_members_with_apps) - GetMembersWithApps
* [invoke_compute_function](docs/sdks/apps/README.md#invoke_compute_function) - Executes a declared compute function on a pooled sandbox worker; gated, org-scoped, rate-limited.
* [list_versions](docs/sdks/apps/README.md#list_versions) - Version history: a snapshot is recorded on each publish; authors can list and restore.
* [list](docs/sdks/apps/README.md#list) - ListApps
* [set_favorite](docs/sdks/apps/README.md#set_favorite) - Favorite/unfavorite a library item (app or dashboard) for the calling member.  Per-member, per-org; favorited=false hard-deletes the row. Covers both primitives  since the merged library page pins apps and dashboards through one client.

### [AppService](docs/sdks/appservice/README.md)

* [heartbeat](docs/sdks/appservice/README.md#heartbeat) - Viewer heartbeat: keeps a warm compute worker alive while the app is open so its  billed lifetime tracks the view session (mirrors a dashboard's viewer TTL). No-op  when the app has no warm worker; never spawns one.
* [get_app_version](docs/sdks/appservice/README.md#get_app_version) - GetAppVersion
* [get_app_view_stats](docs/sdks/appservice/README.md#get_app_view_stats) - View analytics: reads the engagement views recorded on app page load.
* [move_app_to_folder](docs/sdks/appservice/README.md#move_app_to_folder) - Moves an app into a library folder (or to root when folder_id is empty).
* [restore_app_version](docs/sdks/appservice/README.md#restore_app_version) - RestoreAppVersion

### [AppServices](docs/sdks/appservices/README.md)

* [create_app](docs/sdks/appservices/README.md#create_app) - CreateApp
* [delete_app](docs/sdks/appservices/README.md#delete_app) - DeleteApp
* [refresh](docs/sdks/appservices/README.md#refresh) - Re-fetches data sources, rebuilds the document with a fresh snapshot, re-uploads.
* [update](docs/sdks/appservices/README.md#update) - UpdateApp

### [AuditLogs](docs/sdks/auditlogs/README.md)

* [configure_otlp_export](docs/sdks/auditlogs/README.md#configure_otlp_export) - ConfigureOtlpExport
* [delete_otlp_export_config](docs/sdks/auditlogs/README.md#delete_otlp_export_config) - DeleteOtlpExportConfig
* [delete_s3_export_config](docs/sdks/auditlogs/README.md#delete_s3_export_config) - DeleteS3ExportConfig
* [get_otlp_export_config](docs/sdks/auditlogs/README.md#get_otlp_export_config) - GetOtlpExportConfig
* [list](docs/sdks/auditlogs/README.md#list) - ListAuditLogs
* [test_s3_export_connection](docs/sdks/auditlogs/README.md#test_s3_export_connection) - TestS3ExportConnection
* [trigger_otlp_export](docs/sdks/auditlogs/README.md#trigger_otlp_export) - TriggerOtlpExport

### [AuditLogService](docs/sdks/auditlogservice/README.md)

* [configure_s3_export](docs/sdks/auditlogservice/README.md#configure_s3_export) - ConfigureS3Export
* [get_s3_export_config](docs/sdks/auditlogservice/README.md#get_s3_export_config) - GetS3ExportConfig
* [test_otlp_export_connection](docs/sdks/auditlogservice/README.md#test_otlp_export_connection) - TestOtlpExportConnection
* [trigger_s3_export](docs/sdks/auditlogservice/README.md#trigger_s3_export) - TriggerS3Export

### [Channels](docs/sdks/channels/README.md)

* [list](docs/sdks/channels/README.md#list) - ListChannels

### [Chat](docs/sdks/chat/README.md)

* [approve_context_prompt_change](docs/sdks/chat/README.md#approve_context_prompt_change) - ApproveContextPromptChange
* [cancel_stream](docs/sdks/chat/README.md#cancel_stream) - CancelStream
* [get_history](docs/sdks/chat/README.md#get_history) - GetChatHistory
* [rate_cell](docs/sdks/chat/README.md#rate_cell) - RateChatCell appends a row to cell_rating for every click; thumbs-down also upserts a user_thumbs_down thread_warning.

### [Chats](docs/sdks/chats/README.md)

* [attach_agent](docs/sdks/chats/README.md#attach_agent) - External API users
* [bookmark](docs/sdks/chats/README.md#bookmark) - BookmarkChat
* [check_health](docs/sdks/chats/README.md#check_health) - CheckHealth
* [delete](docs/sdks/chats/README.md#delete) - DeleteChat
* [dismiss_questions](docs/sdks/chats/README.md#dismiss_questions) - DismissQuestions
* [get_api_answer](docs/sdks/chats/README.md#get_api_answer) - GetAPIChatAnswer
* [get](docs/sdks/chats/README.md#get) - GetChat
* [get_artifacts_summary](docs/sdks/chats/README.md#get_artifacts_summary) - GetChatArtifactsSummary
* [get_chat_execution_timing](docs/sdks/chats/README.md#get_chat_execution_timing) - GetChatExecutionTiming
* [get_all](docs/sdks/chats/README.md#get_all) - GetChats
* [get_completion_parameters_batch](docs/sdks/chats/README.md#get_completion_parameters_batch) - GetCompletionParametersBatch
* [get_llm_usage](docs/sdks/chats/README.md#get_llm_usage) - GetLlmUsage
* [get_members_with_chats](docs/sdks/chats/README.md#get_members_with_chats) - List distinct chat creators the user can access
* [query_one_shot](docs/sdks/chats/README.md#query_one_shot) - QueryOneShot
* [reject_ontology_change](docs/sdks/chats/README.md#reject_ontology_change) - RejectOntologyChange
* [run](docs/sdks/chats/README.md#run) - RunChat
* [submit_context_prompt_change](docs/sdks/chats/README.md#submit_context_prompt_change) - SubmitContextPromptChange
* [submit_questions](docs/sdks/chats/README.md#submit_questions) - Resolve a halted questions cell. Submit hands the answers to the agent and  resumes it; Dismiss hands over only the answered count and does NOT resume  (the user's next message becomes the dismissal reason).
* [unbookmark](docs/sdks/chats/README.md#unbookmark) - UnbookmarkChat
* [update](docs/sdks/chats/README.md#update) - UpdateChat

### [ChatService](docs/sdks/chatservice/README.md)

* [attach_dataset](docs/sdks/chatservice/README.md#attach_dataset) - AttachDataset
* [check_streamlit_health](docs/sdks/chatservice/README.md#check_streamlit_health) - CheckStreamlitHealth
* [create_chat](docs/sdks/chatservice/README.md#create_chat) - CreateChat
* [get_completion_parameters](docs/sdks/chatservice/README.md#get_completion_parameters) - GetCompletionParameters
* [poll_events](docs/sdks/chatservice/README.md#poll_events) - PollChatEvents

### [ChatServices](docs/sdks/chatservices/README.md)

* [approve_ontology_change](docs/sdks/chatservices/README.md#approve_ontology_change) - Resolve a halted ask_approval form cell. Submit runs the form's submission  and continues the agent with the outcome; Reject discards it (passive, no  run); Dismiss treats it as a change request (no run, next message says what  to change). All three set the cell's outcome, like the other approve/deny cells.
* [attach_app](docs/sdks/chatservices/README.md#attach_app) - AttachApp
* [attach_dashboard](docs/sdks/chatservices/README.md#attach_dashboard) - AttachDashboard
* [check_permissions](docs/sdks/chatservices/README.md#check_permissions) - CheckChatPermissions
* [duplicate_chat](docs/sdks/chatservices/README.md#duplicate_chat) - DuplicateChat
* [get_artifact](docs/sdks/chatservices/README.md#get_artifact) - GetArtifact
* [get_playbook_chats](docs/sdks/chatservices/README.md#get_playbook_chats) - GetPlaybookChats
* [reject_context_prompt_change](docs/sdks/chatservices/README.md#reject_context_prompt_change) - RejectContextPromptChange
* [send](docs/sdks/chatservices/README.md#send) - SendMessage

### [Connector](docs/sdks/connector/README.md)

* [get_dashboards](docs/sdks/connector/README.md#get_dashboards) - GetConnectorDashboards

### [Connectors](docs/sdks/connectors/README.md)

* [delete](docs/sdks/connectors/README.md#delete) - DeleteConnector
* [get](docs/sdks/connectors/README.md#get) - GetConnector
* [get_chats](docs/sdks/connectors/README.md#get_chats) - GetConnectorChats
* [get_usage](docs/sdks/connectors/README.md#get_usage) - GetConnectorUsage
* [list_tables](docs/sdks/connectors/README.md#list_tables) - ListConnectorTables
* [test](docs/sdks/connectors/README.md#test) - TestConnector

### [ConnectorService](docs/sdks/connectorservice/README.md)

* [create](docs/sdks/connectorservice/README.md#create) - CreateConnector
* [get_connector_cell_durations](docs/sdks/connectorservice/README.md#get_connector_cell_durations) - GetConnectorCellDurations
* [get_connector_stats](docs/sdks/connectorservice/README.md#get_connector_stats) - GetConnectorStats
* [get_table_preview](docs/sdks/connectorservice/README.md#get_table_preview) - GetTablePreview

### [ConnectorServices](docs/sdks/connectorservices/README.md)

* [duplicate_connector](docs/sdks/connectorservices/README.md#duplicate_connector) - DuplicateConnector
* [execute_query](docs/sdks/connectorservices/README.md#execute_query) - ExecuteQuery
* [get_connectors](docs/sdks/connectorservices/README.md#get_connectors) - GetConnectors
* [get_example_queries](docs/sdks/connectorservices/README.md#get_example_queries) - GetExampleQueries
* [list_query_templates](docs/sdks/connectorservices/README.md#list_query_templates) - ListQueryTemplates
* [update](docs/sdks/connectorservices/README.md#update) - UpdateConnector

### [Dashboards](docs/sdks/dashboards/README.md)

* [create_folder](docs/sdks/dashboards/README.md#create_folder) - Folder management
* [delete_folder](docs/sdks/dashboards/README.md#delete_folder) - DeleteDashboardFolder
* [duplicate](docs/sdks/dashboards/README.md#duplicate) - DuplicateDashboard
* [list_folders](docs/sdks/dashboards/README.md#list_folders) - ListDashboardFolders
* [list](docs/sdks/dashboards/README.md#list) - ListDashboards
* [move_to_folder](docs/sdks/dashboards/README.md#move_to_folder) - MoveDashboardToFolder
* [publish](docs/sdks/dashboards/README.md#publish) - Publishing workflow
* [regenerate_screenshot](docs/sdks/dashboards/README.md#regenerate_screenshot) - Screenshot management
* [run_scheduled_dashboard](docs/sdks/dashboards/README.md#run_scheduled_dashboard) - RunScheduledDashboard

### [DashboardService](docs/sdks/dashboardservice/README.md)

* [create_dashboard](docs/sdks/dashboardservice/README.md#create_dashboard) - CRUD operations
* [get_members_with_dashboards](docs/sdks/dashboardservice/README.md#get_members_with_dashboards) - Member management
* [restore_dashboard_version](docs/sdks/dashboardservice/README.md#restore_dashboard_version) - RestoreDashboardVersion
* [update_dashboard](docs/sdks/dashboardservice/README.md#update_dashboard) - UpdateDashboard
* [update_dashboard_schedule](docs/sdks/dashboardservice/README.md#update_dashboard_schedule) - Scheduling

### [DashboardServices](docs/sdks/dashboardservices/README.md)

* [check_health](docs/sdks/dashboardservices/README.md#check_health) - CheckDashboardHealth
* [delete](docs/sdks/dashboardservices/README.md#delete) - DeleteDashboard
* [discard_changes](docs/sdks/dashboardservices/README.md#discard_changes) - DiscardDashboardChanges
* [get](docs/sdks/dashboardservices/README.md#get) - GetDashboard
* [get_version](docs/sdks/dashboardservices/README.md#get_version) - GetDashboardVersion
* [get_dashboard_view_stats](docs/sdks/dashboardservices/README.md#get_dashboard_view_stats) - View analytics
* [list_versions](docs/sdks/dashboardservices/README.md#list_versions) - Version history
* [preview_config](docs/sdks/dashboardservices/README.md#preview_config) - Config-managed dashboards: render a `.dashboard` straight from a patch ref before  it merges (ADR-0022). Runs as the file's run_as, gated on the previewer being  authorized for it; persists nothing.
* [spawn](docs/sdks/dashboardservices/README.md#spawn) - Dashboard execution
* [update_dashboard_folder](docs/sdks/dashboardservices/README.md#update_dashboard_folder) - UpdateDashboardFolder

### [Datasets](docs/sdks/datasets/README.md)

* [create_upload_presign_url](docs/sdks/datasets/README.md#create_upload_presign_url) - uploads
* [delete](docs/sdks/datasets/README.md#delete) - Delete a dataset (soft delete)
* [export](docs/sdks/datasets/README.md#export) - export dataset in "raw" format – original if dataset is uploaded, converted format otherwise (defaults to CSV)
* [fetch](docs/sdks/datasets/README.md#fetch) - GetDataset, GetDatasets only return metadata
* [get_stats](docs/sdks/datasets/README.md#get_stats) - GetDatasetStats
* [get](docs/sdks/datasets/README.md#get) - GetDatasets
* [get_by_ids](docs/sdks/datasets/README.md#get_by_ids) - GetDatasetsByIds
* [process_upload_presign_url](docs/sdks/datasets/README.md#process_upload_presign_url) - ProcessUploadPresignUrl

### [DatasetService](docs/sdks/datasetservice/README.md)

* [create_folder](docs/sdks/datasetservice/README.md#create_folder) - CreateFolder
* [get_folders](docs/sdks/datasetservice/README.md#get_folders) - for AR: CreateFolderACL, UpdateFolderACL, DeleteFolderACL
* [update_dataset](docs/sdks/datasetservice/README.md#update_dataset) - Update dataset metadata

### [DatasetServices](docs/sdks/datasetservices/README.md)

* [create_power_bi_dataset](docs/sdks/datasetservices/README.md#create_power_bi_dataset) - CreatePowerBIDataset
* [create_tableau_dataset](docs/sdks/datasetservices/README.md#create_tableau_dataset) - Create Tableau dataset from views/datasources
* [get_dataset_values](docs/sdks/datasetservices/README.md#get_dataset_values) - GetDatasetValues

### [Libraries](docs/sdks/libraries/README.md)

* [add_submodule](docs/sdks/libraries/README.md#add_submodule) - AddLibrarySubmodule
* [create_file_upload_url](docs/sdks/libraries/README.md#create_file_upload_url) - CreateLibraryFileUploadUrl
* [delete_approval_rule](docs/sdks/libraries/README.md#delete_approval_rule) - DeleteApprovalRule
* [delete_owners](docs/sdks/libraries/README.md#delete_owners) - DeleteLibraryOwners
* [get_codeowner_coverage](docs/sdks/libraries/README.md#get_codeowner_coverage) - GetCodeownerCoverage
* [get_effective_owners](docs/sdks/libraries/README.md#get_effective_owners) - GetEffectiveLibraryOwners
* [get_file_usage](docs/sdks/libraries/README.md#get_file_usage) - GetFileUsage
* [get_ana_config](docs/sdks/libraries/README.md#get_ana_config) - GetLibraryAnaConfig
* [get_file](docs/sdks/libraries/README.md#get_file) - GetLibraryFile
* [get_history_file_diff](docs/sdks/libraries/README.md#get_history_file_diff) - GetLibraryHistoryFileDiff
* [get_remote](docs/sdks/libraries/README.md#get_remote) - GetLibraryRemote
* [get_size_timeline](docs/sdks/libraries/README.md#get_size_timeline) - GetLibrarySizeTimeline
* [get_raw_patch](docs/sdks/libraries/README.md#get_raw_patch) - GetRawPatch
* [list_context_patch_auto_approve_rules](docs/sdks/libraries/README.md#list_context_patch_auto_approve_rules) - ListContextPatchAutoApproveRules
* [list_imports](docs/sdks/libraries/README.md#list_imports) - ListLibraryImports
* [list_skills](docs/sdks/libraries/README.md#list_skills) - Lists the skills under the library's flat skills/ root that the caller can  read (OWNERS-filtered). Returns display metadata only — never instruction  bodies — feeding the chat composer's `/` autocomplete.
* [recover](docs/sdks/libraries/README.md#recover) - RecoverLibrary
* [remove_library_submodule](docs/sdks/libraries/README.md#remove_library_submodule) - RemoveLibrarySubmodule
* [request_patch_review](docs/sdks/libraries/README.md#request_patch_review) - RequestPatchReview
* [restore_patch](docs/sdks/libraries/README.md#restore_patch) - RestorePatch
* [revert_patch](docs/sdks/libraries/README.md#revert_patch) - RevertPatch
* [update_approval_rule](docs/sdks/libraries/README.md#update_approval_rule) - UpdateApprovalRule
* [upsert_ana_config](docs/sdks/libraries/README.md#upsert_ana_config) - UpsertLibraryAnaConfig
* [upsert_owners](docs/sdks/libraries/README.md#upsert_owners) - UpsertLibraryOwners

### [Library](docs/sdks/library/README.md)

* [exchange_github_code](docs/sdks/library/README.md#exchange_github_code) - ExchangeLibraryGithubCode
* [finalize_file_upload](docs/sdks/library/README.md#finalize_file_upload) - FinalizeLibraryFileUpload
* [get_usage_details_for_file](docs/sdks/library/README.md#get_usage_details_for_file) - GetUsageDetailsForFile
* [plan_merge](docs/sdks/library/README.md#plan_merge) - PlanLibraryMerge
* [rename_file](docs/sdks/library/README.md#rename_file) - RenameLibraryFile

### [LibraryService](docs/sdks/libraryservice/README.md)

* [approve_patch](docs/sdks/libraryservice/README.md#approve_patch) - ApprovePatch
* [create_approval_rule](docs/sdks/libraryservice/README.md#create_approval_rule) - CreateApprovalRule
* [create_library_directory](docs/sdks/libraryservice/README.md#create_library_directory) - CreateLibraryDirectory
* [delete_context_patch_auto_approve_rule](docs/sdks/libraryservice/README.md#delete_context_patch_auto_approve_rule) - DeleteContextPatchAutoApproveRule
* [deny_patch](docs/sdks/libraryservice/README.md#deny_patch) - DenyPatch
* [get_config_export_capabilities](docs/sdks/libraryservice/README.md#get_config_export_capabilities) - GetConfigExportCapabilities
* [get_patch](docs/sdks/libraryservice/README.md#get_patch) - GetPatch
* [get_patch_by_number](docs/sdks/libraryservice/README.md#get_patch_by_number) - GetPatchByNumber
* [get_patch_capabilities](docs/sdks/libraryservice/README.md#get_patch_capabilities) - GetPatchCapabilities
* [list_library_entries](docs/sdks/libraryservice/README.md#list_library_entries) - ListLibraryEntries
* [list_library_submodules](docs/sdks/libraryservice/README.md#list_library_submodules) - ListLibrarySubmodules
* [list_patches](docs/sdks/libraryservice/README.md#list_patches) - ListPatches
* [migrate_legacy_context](docs/sdks/libraryservice/README.md#migrate_legacy_context) - MigrateLegacyContextToLibrary
* [migrate_ontology](docs/sdks/libraryservice/README.md#migrate_ontology) - MigrateOntologyToLibrary
* [pull_from_remote](docs/sdks/libraryservice/README.md#pull_from_remote) - PullLibraryFromRemote
* [remove_remote](docs/sdks/libraryservice/README.md#remove_remote) - RemoveLibraryRemote
* [resolve_sync_conflict](docs/sdks/libraryservice/README.md#resolve_sync_conflict) - ResolveLibrarySyncConflict
* [trigger_config_drift_reconcile](docs/sdks/libraryservice/README.md#trigger_config_drift_reconcile) - TriggerConfigDriftReconcile forces an immediate config-sync catch-up for the  caller's org: if the Library repo's live HEAD differs from the last  reconciled commit, it enqueues a reconcile (otherwise no-op). The on-demand  equivalent of waiting for the periodic drift scan.
* [update_library_sync_config](docs/sdks/libraryservice/README.md#update_library_sync_config) - UpdateLibrarySyncConfig

### [LibraryServices](docs/sdks/libraryservices/README.md)

* [configure_library_remote](docs/sdks/libraryservices/README.md#configure_library_remote) - ConfigureLibraryRemote
* [create_context_patch_auto_approve_rule](docs/sdks/libraryservices/README.md#create_context_patch_auto_approve_rule) - CreateContextPatchAutoApproveRule
* [delete_library_directory](docs/sdks/libraryservices/README.md#delete_library_directory) - DeleteLibraryDirectory
* [delete_library_file](docs/sdks/libraryservices/README.md#delete_library_file) - DeleteLibraryFile
* [get_file_usage_timeline](docs/sdks/libraryservices/README.md#get_file_usage_timeline) - GetFileUsageTimeline
* [get_library_github_o_auth_url](docs/sdks/libraryservices/README.md#get_library_github_o_auth_url) - GetLibraryGithubOAuthURL
* [get_migration_status](docs/sdks/libraryservices/README.md#get_migration_status) - GetLibraryMigrationStatus
* [get_library_owners](docs/sdks/libraryservices/README.md#get_library_owners) - GetLibraryOwners
* [get_library_sync_conflicts](docs/sdks/libraryservices/README.md#get_library_sync_conflicts) - GetLibrarySyncConflicts
* [get_ontology_usage_summary](docs/sdks/libraryservices/README.md#get_ontology_usage_summary) - GetOntologyUsageSummary
* [list_approval_rules](docs/sdks/libraryservices/README.md#list_approval_rules) - ListApprovalRules
* [list_chats_for_file](docs/sdks/libraryservices/README.md#list_chats_for_file) - ListChatsForFile
* [list_library_history](docs/sdks/libraryservices/README.md#list_library_history) - ListLibraryHistory
* [list_library_sync_runs](docs/sdks/libraryservices/README.md#list_library_sync_runs) - ListLibrarySyncRuns
* [list_patch_reviewers](docs/sdks/libraryservices/README.md#list_patch_reviewers) - ListPatchReviewers
* [preview_library_pull_from_remote](docs/sdks/libraryservices/README.md#preview_library_pull_from_remote) - PreviewLibraryPullFromRemote
* [push_library_to_remote](docs/sdks/libraryservices/README.md#push_library_to_remote) - PushLibraryToRemote
* [save_all_objects_as_config](docs/sdks/libraryservices/README.md#save_all_objects_as_config) - SaveAllObjectsAsConfig
* [save_as_config](docs/sdks/libraryservices/README.md#save_as_config) - SaveObjectAsConfig
* [update_context_patch_auto_approve_rule](docs/sdks/libraryservices/README.md#update_context_patch_auto_approve_rule) - UpdateContextPatchAutoApproveRule
* [upsert_library_file](docs/sdks/libraryservices/README.md#upsert_library_file) - UpsertLibraryFile
* [validate_config](docs/sdks/libraryservices/README.md#validate_config) - Read-only functional validation of a proposed config: parse + dependency  resolution/reachability, no authorization and no persistence. "ok" means  functionally valid, not "guaranteed to merge" — the merge gate re-checks  authorization at approve time.

### [Mcp](docs/sdks/mcp/README.md)

* [initiate_o_auth_flow](docs/sdks/mcp/README.md#initiate_o_auth_flow) - InitiateOAuthFlow
* [toggle_server](docs/sdks/mcp/README.md#toggle_server) - ToggleMCPServer

### [Mcps](docs/sdks/mcps/README.md)

* [clear_o_auth_token](docs/sdks/mcps/README.md#clear_o_auth_token) - ClearOAuthToken
* [get_servers](docs/sdks/mcps/README.md#get_servers) - GetMCPServers

### [McpServers](docs/sdks/mcpservers/README.md)

* [delete](docs/sdks/mcpservers/README.md#delete) - DeleteMCPServer

### [McpService](docs/sdks/mcpservice/README.md)

* [handle_o_auth_callback](docs/sdks/mcpservice/README.md#handle_o_auth_callback) - HandleOAuthCallback

### [McpServices](docs/sdks/mcpservices/README.md)

* [upsert_mcp_servers](docs/sdks/mcpservices/README.md#upsert_mcp_servers) - UpsertMCPServers

### [MetricsExports](docs/sdks/metricsexports/README.md)

* [configure](docs/sdks/metricsexports/README.md#configure) - ConfigureMetricsExport
* [test_connection](docs/sdks/metricsexports/README.md#test_connection) - TestMetricsExportConnection

### [MetricsExportService](docs/sdks/metricsexportservice/README.md)

* [delete_config](docs/sdks/metricsexportservice/README.md#delete_config) - DeleteMetricsExportConfig

### [MetricsExportServices](docs/sdks/metricsexportservices/README.md)

* [get_metrics_export_config](docs/sdks/metricsexportservices/README.md#get_metrics_export_config) - GetMetricsExportConfig
* [trigger_push](docs/sdks/metricsexportservices/README.md#trigger_push) - TriggerMetricsPush

### [Observabilities](docs/sdks/observabilities/README.md)

* [get_access_method_stats](docs/sdks/observabilities/README.md#get_access_method_stats) - GetAccessMethodStats

### [Observability](docs/sdks/observability/README.md)

* [backfill_custom_topic](docs/sdks/observability/README.md#backfill_custom_topic) - BackfillCustomTopic
* [backfill_thread_warnings](docs/sdks/observability/README.md#backfill_thread_warnings) - BackfillThreadWarnings
* [create_custom_topic](docs/sdks/observability/README.md#create_custom_topic) - CreateCustomTopic
* [deactivate_custom_topic](docs/sdks/observability/README.md#deactivate_custom_topic) - DeactivateCustomTopic
* [fix_warning](docs/sdks/observability/README.md#fix_warning) - FixWarning
* [get_active_people_stats](docs/sdks/observability/README.md#get_active_people_stats) - GetActivePeopleStats
* [get_active_people_trend](docs/sdks/observability/README.md#get_active_people_trend) - GetActivePeopleTrend
* [get_backfill_status](docs/sdks/observability/README.md#get_backfill_status) - GetBackfillStatus
* [get_billing_stats](docs/sdks/observability/README.md#get_billing_stats) - GetBillingStats
* [get_chat_topics](docs/sdks/observability/README.md#get_chat_topics) - GetChatTopics
* [get_check_record_fix](docs/sdks/observability/README.md#get_check_record_fix) - GetCheckRecordFix
* [get_custom_topic](docs/sdks/observability/README.md#get_custom_topic) - GetCustomTopic
* [get_custom_topic_threads](docs/sdks/observability/README.md#get_custom_topic_threads) - GetCustomTopicThreads
* [update_custom_topic](docs/sdks/observability/README.md#update_custom_topic) - UpdateCustomTopic

### [ObservabilityService](docs/sdks/observabilityservice/README.md)

* [activate_custom_topic](docs/sdks/observabilityservice/README.md#activate_custom_topic) - ActivateCustomTopic
* [get_backfill_preview](docs/sdks/observabilityservice/README.md#get_backfill_preview) - GetBackfillPreview
* [get_engagement_spectrum](docs/sdks/observabilityservice/README.md#get_engagement_spectrum) - GetEngagementSpectrum
* [get_observability_stats](docs/sdks/observabilityservice/README.md#get_observability_stats) - GetObservabilityStats
* [get_thread_warnings](docs/sdks/observabilityservice/README.md#get_thread_warnings) - GetThreadWarnings

### [ObservabilityServices](docs/sdks/observabilityservices/README.md)

* [delete_custom_topic](docs/sdks/observabilityservices/README.md#delete_custom_topic) - DeleteCustomTopic
* [export_csv](docs/sdks/observabilityservices/README.md#export_csv) - ExportObservabilityCsv
* [fix_check_record](docs/sdks/observabilityservices/README.md#fix_check_record) - FixCheckRecord
* [get_chat_source_stats](docs/sdks/observabilityservices/README.md#get_chat_source_stats) - GetChatSourceStats
* [get_custom_topic_people](docs/sdks/observabilityservices/README.md#get_custom_topic_people) - GetCustomTopicPeople
* [get_member_activity](docs/sdks/observabilityservices/README.md#get_member_activity) - GetMemberActivity
* [list_custom_topics](docs/sdks/observabilityservices/README.md#list_custom_topics) - ListCustomTopics
* [set_topic_tag_feedback](docs/sdks/observabilityservices/README.md#set_topic_tag_feedback) - SetTopicTagFeedback

### [Playbooks](docs/sdks/playbooks/README.md)

* [attach_dashboard](docs/sdks/playbooks/README.md#attach_dashboard) - AttachDashboard
* [attach_dataset](docs/sdks/playbooks/README.md#attach_dataset) - AttachDataset
* [deactivate](docs/sdks/playbooks/README.md#deactivate) - DeactivatePlaybook
* [delete](docs/sdks/playbooks/README.md#delete) - DeletePlaybook
* [deploy](docs/sdks/playbooks/README.md#deploy) - DeployPlaybook
* [favorite_report](docs/sdks/playbooks/README.md#favorite_report) - Favorite report management
* [get_chat_reports_summary](docs/sdks/playbooks/README.md#get_chat_reports_summary) - Lightweight endpoint for chat report drawer - returns summaries without full blocks
* [get_members_with](docs/sdks/playbooks/README.md#get_members_with) - GetMembersWithPlaybooks
* [fetch](docs/sdks/playbooks/README.md#fetch) - GetPlaybook
* [get_extended_qn](docs/sdks/playbooks/README.md#get_extended_qn) - Playbook Extended quant.new operations
* [get_reports](docs/sdks/playbooks/README.md#get_reports) - GetPlaybookReports
* [get](docs/sdks/playbooks/README.md#get) - GetPlaybooks
* [get_qn_playbook](docs/sdks/playbooks/README.md#get_qn_playbook) - GetQNPlaybook
* [get_reports_with_filters](docs/sdks/playbooks/README.md#get_reports_with_filters) - GetReportsWithFilters
* [list_all_teams_channel_context_playbooks](docs/sdks/playbooks/README.md#list_all_teams_channel_context_playbooks) - ListAllTeamsChannelContextPlaybooks
* [list_batch_runs](docs/sdks/playbooks/README.md#list_batch_runs) - List batch runs for a playbook
* [list_slack_channels_for_context](docs/sdks/playbooks/README.md#list_slack_channels_for_context) - List Slack channel IDs where the given playbook is set as the context
* [mark_report_as_read](docs/sdks/playbooks/README.md#mark_report_as_read) - Report read tracking
* [preview_slack_report](docs/sdks/playbooks/README.md#preview_slack_report) - PreviewSlackReport
* [run](docs/sdks/playbooks/README.md#run) - RunPlaybook
* [set_teams_channel_context](docs/sdks/playbooks/README.md#set_teams_channel_context) - SetTeamsChannelContextPlaybook
* [subscribe](docs/sdks/playbooks/README.md#subscribe) - SubscribeToPlaybook
* [unset_teams_channel_context](docs/sdks/playbooks/README.md#unset_teams_channel_context) - UnsetTeamsChannelContextPlaybook
* [unsubscribe](docs/sdks/playbooks/README.md#unsubscribe) - UnsubscribeFromPlaybook
* [update_extended_qn](docs/sdks/playbooks/README.md#update_extended_qn) - UpdatePlaybookExtendedQn

### [PlaybookService](docs/sdks/playbookservice/README.md)

* [cancel_template_execution](docs/sdks/playbookservice/README.md#cancel_template_execution) - Cancel template execution for a specific template header
* [duplicate](docs/sdks/playbookservice/README.md#duplicate) - DuplicatePlaybook
* [get_active_subscribed_count](docs/sdks/playbookservice/README.md#get_active_subscribed_count) - GetActiveSubscribedPlaybooksCount
* [get_playbook_reports_batch](docs/sdks/playbookservice/README.md#get_playbook_reports_batch) - Get reports for multiple template data IDs in a single batch request
* [get_playbooks_previews](docs/sdks/playbookservice/README.md#get_playbooks_previews) - GetPlaybooksPreviews
* [get_report_by_id](docs/sdks/playbookservice/README.md#get_report_by_id) - Get a single report by ID
* [list_teams_channels_for_context_playbook](docs/sdks/playbookservice/README.md#list_teams_channels_for_context_playbook) - ListTeamsChannelsForContextPlaybook
* [remove_dataset](docs/sdks/playbookservice/README.md#remove_dataset) - RemoveDataset
* [unset_slack_channel_context_playbook](docs/sdks/playbookservice/README.md#unset_slack_channel_context_playbook) - Unset the context playbook for a Slack channel. This clears any association  so that messages in this channel no longer use a specific playbook context.
* [update](docs/sdks/playbookservice/README.md#update) - UpdatePlaybook

### [PlaybookServices](docs/sdks/playbookservices/README.md)

* [create_playbook](docs/sdks/playbookservices/README.md#create_playbook) - CreatePlaybook
* [demo_playbook](docs/sdks/playbookservices/README.md#demo_playbook) - DemoPlaybook
* [get_batch_run](docs/sdks/playbookservices/README.md#get_batch_run) - Get a specific batch run
* [get_playbook_lineage](docs/sdks/playbookservices/README.md#get_playbook_lineage) - GetPlaybookLineage
* [list_slack_channel_context_playbooks](docs/sdks/playbookservices/README.md#list_slack_channel_context_playbooks) - List all Slack channels context playbook mappings for the organization
* [remove_dashboard](docs/sdks/playbookservices/README.md#remove_dashboard) - RemoveDashboard
* [set_slack_channel_context_playbook](docs/sdks/playbookservices/README.md#set_slack_channel_context_playbook) - Set the context playbook for a Slack channel. This associates the given  playbook to a Slack channel so that Slack messages in that channel use the  playbook's context by default.

### [Powerbi](docs/sdks/powerbisdk1/README.md)

* [generate_embed_token](docs/sdks/powerbisdk1/README.md#generate_embed_token) - GeneratePowerBIEmbedToken
* [get_dataset_preview](docs/sdks/powerbisdk1/README.md#get_dataset_preview) - GetPowerBIDatasetPreview
* [list_workspaces](docs/sdks/powerbisdk1/README.md#list_workspaces) - ListPowerBIWorkspaces

### [PowerBi](docs/sdks/powerbisdk2/README.md)

* [get_synced_items](docs/sdks/powerbisdk2/README.md#get_synced_items) - GetSyncedPowerBIItems
* [list_reports](docs/sdks/powerbisdk2/README.md#list_reports) - ListPowerBIReports

### [PowerbiDatasets](docs/sdks/powerbidatasets/README.md)

* [list](docs/sdks/powerbidatasets/README.md#list) - ListPowerBIDatasets

### [PowerBiService](docs/sdks/powerbiservice/README.md)

* [test_connection](docs/sdks/powerbiservice/README.md#test_connection) - TestPowerBIConnection

### [PowerBiServices](docs/sdks/powerbiservices/README.md)

* [export_report_image](docs/sdks/powerbiservices/README.md#export_report_image) - ExportPowerBIReportImage
* [unsync_items](docs/sdks/powerbiservices/README.md#unsync_items) - UnsyncPowerBIItems
* [sync_power_bi_items](docs/sdks/powerbiservices/README.md#sync_power_bi_items) - SyncPowerBIItems

### [Rbac](docs/sdks/rbac/README.md)

* [add_group_member](docs/sdks/rbac/README.md#add_group_member) - AddGroupMember
* [approve_access_request](docs/sdks/rbac/README.md#approve_access_request) - ApproveAccessRequest
* [assign_permission_to_role](docs/sdks/rbac/README.md#assign_permission_to_role) - AssignPermissionToRole
* [create_group](docs/sdks/rbac/README.md#create_group) - CreateGroup
* [create_service_account](docs/sdks/rbac/README.md#create_service_account) - Service account management
* [delete_group](docs/sdks/rbac/README.md#delete_group) - DeleteGroup
* [delete_role](docs/sdks/rbac/README.md#delete_role) - DeleteRole
* [delete_service_account](docs/sdks/rbac/README.md#delete_service_account) - DeleteServiceAccount
* [generate_share_link](docs/sdks/rbac/README.md#generate_share_link) - GenerateShareLink
* [get_current_member_roles_and_permissions](docs/sdks/rbac/README.md#get_current_member_roles_and_permissions) - Get current member roles and permissions
* [get_embed_user_api_key](docs/sdks/rbac/README.md#get_embed_user_api_key) - GetEmbedUserApiKey
* [get_group](docs/sdks/rbac/README.md#get_group) - GetGroup
* [get_member_groups](docs/sdks/rbac/README.md#get_member_groups) - GetMemberGroups
* [get_member_roles](docs/sdks/rbac/README.md#get_member_roles) - GetMemberRoles
* [get_object_access](docs/sdks/rbac/README.md#get_object_access) - GetObjectAccess
* [has_object_access](docs/sdks/rbac/README.md#has_object_access) - HasObjectAccess
* [list_group_connectors](docs/sdks/rbac/README.md#list_group_connectors) - ListGroupConnectors
* [list_permissions](docs/sdks/rbac/README.md#list_permissions) - Permission management
* [list_roles](docs/sdks/rbac/README.md#list_roles) - ListRoles
* [migrate_scim_group_mapping_to_group](docs/sdks/rbac/README.md#migrate_scim_group_mapping_to_group) - MigrateScimGroupMappingToGroup
* [reject_access_request](docs/sdks/rbac/README.md#reject_access_request) - RejectAccessRequest
* [remove_group_member](docs/sdks/rbac/README.md#remove_group_member) - RemoveGroupMember
* [remove_permission_from_role](docs/sdks/rbac/README.md#remove_permission_from_role) - RemovePermissionFromRole
* [request_access](docs/sdks/rbac/README.md#request_access) - Access request management
* [revert_scim_group_mapping_to_role](docs/sdks/rbac/README.md#revert_scim_group_mapping_to_role) - RevertScimGroupMappingToRole
* [revoke_api_key](docs/sdks/rbac/README.md#revoke_api_key) - RevokeApiKey
* [share_with_group](docs/sdks/rbac/README.md#share_with_group) - ShareObjectWithGroup
* [share_object_with_role](docs/sdks/rbac/README.md#share_object_with_role) - ShareObjectWithRole
* [update_group](docs/sdks/rbac/README.md#update_group) - UpdateGroup
* [update_object_visibility](docs/sdks/rbac/README.md#update_object_visibility) - UpdateObjectVisibility
* [update_role](docs/sdks/rbac/README.md#update_role) - UpdateRole

### [Rbacs](docs/sdks/rbacs/README.md)

* [get_role](docs/sdks/rbacs/README.md#get_role) - GetRole

### [RbacService](docs/sdks/rbacservice/README.md)

* [convert_role_to_group](docs/sdks/rbacservice/README.md#convert_role_to_group) - ConvertRoleToGroup
* [create_api_key](docs/sdks/rbacservice/README.md#create_api_key) - API Key management
* [create_role](docs/sdks/rbacservice/README.md#create_role) - Role management
* [list_access_requests](docs/sdks/rbacservice/README.md#list_access_requests) - ListAccessRequests
* [list_api_keys](docs/sdks/rbacservice/README.md#list_api_keys) - ListApiKeys
* [list_groups](docs/sdks/rbacservice/README.md#list_groups) - ListGroups
* [list_service_accounts](docs/sdks/rbacservice/README.md#list_service_accounts) - ListServiceAccounts
* [remove_role_from_member](docs/sdks/rbacservice/README.md#remove_role_from_member) - RemoveRoleFromMember
* [rotate_api_key](docs/sdks/rbacservice/README.md#rotate_api_key) - RotateApiKey
* [share_object](docs/sdks/rbacservice/README.md#share_object) - Object sharing and access control
* [update_object_access](docs/sdks/rbacservice/README.md#update_object_access) - UpdateObjectAccess

### [RbacServices](docs/sdks/rbacservices/README.md)

* [assign_role_to_member](docs/sdks/rbacservices/README.md#assign_role_to_member) - Member role assignment
* [get_role_permissions](docs/sdks/rbacservices/README.md#get_role_permissions) - GetRolePermissions
* [list_scim_group_mappings](docs/sdks/rbacservices/README.md#list_scim_group_mappings) - ListScimGroupMappings
* [migrate_all_scim_group_mappings](docs/sdks/rbacservices/README.md#migrate_all_scim_group_mappings) - MigrateAllScimGroupMappings
* [revoke_object_access](docs/sdks/rbacservices/README.md#revoke_object_access) - RevokeObjectAccess

### [SandboxAdmin](docs/sdks/sandboxadmin/README.md)

* [stop](docs/sdks/sandboxadmin/README.md#stop) - StopSandbox

### [SandboxAdmins](docs/sdks/sandboxadmins/README.md)

* [get_sandbox](docs/sdks/sandboxadmins/README.md#get_sandbox) - GetSandbox

### [SandboxAdminService](docs/sdks/sandboxadminservice/README.md)

* [list_sandbox_files](docs/sdks/sandboxadminservice/README.md#list_sandbox_files) - Live filesystem of a running sandbox. Both are NO-OP (read-only) and only  return data while the worker is alive; available=false otherwise.
* [restart_sandbox](docs/sdks/sandboxadminservice/README.md#restart_sandbox) - Restart a stopped/reaped sandbox by re-acquiring a worker for the same  sandbox_id, preserving the original owner. Same scoping as StopSandbox  (owner, or sandbox:write_private for org-wide).

### [SandboxAdminServices](docs/sdks/sandboxadminservices/README.md)

* [list_sandbox_egress](docs/sdks/sandboxadminservices/README.md#list_sandbox_egress) - Outbound HTTP(S) calls a sandbox made (the egress ledger). Durable — reads  the recorded table, so it works for stopped sandboxes too.
* [list_sandbox_spend](docs/sdks/sandboxadminservices/README.md#list_sandbox_spend) - Per-lease compute usage for a sandbox, computed from lease durations × the  compute rate. Durable (reads the lease table), so it works for stopped  sandboxes. This is usage (ACUs), not the invoiced dollar amount.

### [Sandboxes](docs/sdks/sandboxes/README.md)

* [list_executions](docs/sdks/sandboxes/README.md#list_executions) - ListSandboxExecutions
* [list](docs/sdks/sandboxes/README.md#list) - ListSandboxes
* [read_file](docs/sdks/sandboxes/README.md#read_file) - ReadSandboxFile

### [SandboxQueryService](docs/sdks/sandboxqueryservice/README.md)

* [execute_query](docs/sdks/sandboxqueryservice/README.md#execute_query) - ExecuteQuery

### [ScimService](docs/sdks/scimservice/README.md)

* [create_scim_token](docs/sdks/scimservice/README.md#create_scim_token) - CreateScimToken
* [list_scim_o_auth_clients](docs/sdks/scimservice/README.md#list_scim_o_auth_clients) - ListScimOAuthClients
* [revoke_o_auth_client](docs/sdks/scimservice/README.md#revoke_o_auth_client) - RevokeScimOAuthClient
* [revoke_scim_token](docs/sdks/scimservice/README.md#revoke_scim_token) - RevokeScimToken

### [ScimServices](docs/sdks/scimservices/README.md)

* [create_o_auth_client](docs/sdks/scimservices/README.md#create_o_auth_client) - CreateScimOAuthClient

### [ScimTokens](docs/sdks/scimtokens/README.md)

* [list](docs/sdks/scimtokens/README.md#list) - ListScimTokens

### [Secrets](docs/sdks/secrets/README.md)

* [create_api_revision](docs/sdks/secrets/README.md#create_api_revision) - CreateApiRevision
* [delete_api_revision](docs/sdks/secrets/README.md#delete_api_revision) - DeleteApiRevision
* [get_members_with_secrets](docs/sdks/secrets/README.md#get_members_with_secrets) - GetMembersWithSecrets
* [list_api_providers](docs/sdks/secrets/README.md#list_api_providers) - ListApiProviders
* [update](docs/sdks/secrets/README.md#update) - UpdateSecret
* [upsert_api_access_key](docs/sdks/secrets/README.md#upsert_api_access_key) - UpsertApiAccessKey

### [SecretService](docs/sdks/secretservice/README.md)

* [get_api_access_key](docs/sdks/secretservice/README.md#get_api_access_key) - GetApiAccessKey
* [migrate_secret_to_api_connector](docs/sdks/secretservice/README.md#migrate_secret_to_api_connector) - MigrateSecretToApiConnector

### [SecretServices](docs/sdks/secretservices/README.md)

* [delete_api_access_key](docs/sdks/secretservices/README.md#delete_api_access_key) - DeleteApiAccessKey
* [delete_secret](docs/sdks/secretservices/README.md#delete_secret) - DeleteSecret
* [list_api_access_keys](docs/sdks/secretservices/README.md#list_api_access_keys) - ListApiAccessKeys
* [list_secrets](docs/sdks/secretservices/README.md#list_secrets) - ListSecrets
* [put_secret](docs/sdks/secretservices/README.md#put_secret) - PutSecret
* [test_api_access_key](docs/sdks/secretservices/README.md#test_api_access_key) - TestApiAccessKey

### [Slack](docs/sdks/slack/README.md)

* [create_uuid](docs/sdks/slack/README.md#create_uuid) - CreateSlackUuid
* [delete_installation](docs/sdks/slack/README.md#delete_installation) - DeleteInstallation
* [handle_o_auth_callback](docs/sdks/slack/README.md#handle_o_auth_callback) - HandleSlackOAuthCallback
* [sync_workspace](docs/sdks/slack/README.md#sync_workspace) - SyncWorkspace

### [SlackService](docs/sdks/slackservice/README.md)

* [list_channels](docs/sdks/slackservice/README.md#list_channels) - ListChannels
* [list_installations](docs/sdks/slackservice/README.md#list_installations) - ListInstallations

### [SlackServices](docs/sdks/slackservices/README.md)

* [get_current_user](docs/sdks/slackservices/README.md#get_current_user) - GetCurrentUser
* [list_users](docs/sdks/slackservices/README.md#list_users) - ListUsers

### [Tableau](docs/sdks/tableausdk/README.md)

* [generate_embed_token](docs/sdks/tableausdk/README.md#generate_embed_token) - Generate JWT token for embedding views
* [get_starred_items](docs/sdks/tableausdk/README.md#get_starred_items) - GetStarredTableauItems
* [list_projects](docs/sdks/tableausdk/README.md#list_projects) - List Tableau projects
* [list_views](docs/sdks/tableausdk/README.md#list_views) - List Tableau views
* [star_item](docs/sdks/tableausdk/README.md#star_item) - Star/unstar items

### [Tableaus](docs/sdks/tableaus/README.md)

* [list_workbooks](docs/sdks/tableaus/README.md#list_workbooks) - List Tableau workbooks

### [TableauService](docs/sdks/tableauservice/README.md)

* [refresh_collection](docs/sdks/tableauservice/README.md#refresh_collection) - RefreshTableauCollection
* [test_tableau_connection](docs/sdks/tableauservice/README.md#test_tableau_connection) - Test a Tableau connection

### [TableauServices](docs/sdks/tableauservices/README.md)

* [get_collection_thumbnail](docs/sdks/tableauservices/README.md#get_collection_thumbnail) - Get collection thumbnail (first view image)
* [get_connected_app_status](docs/sdks/tableauservices/README.md#get_connected_app_status) - GetConnectedAppStatus
* [list_tableau_datasources](docs/sdks/tableauservices/README.md#list_tableau_datasources) - List Tableau datasources
* [reset_connected_app](docs/sdks/tableauservices/README.md#reset_connected_app) - ResetConnectedApp
* [unstar_tableau_item](docs/sdks/tableauservices/README.md#unstar_tableau_item) - UnstarTableauItem

### [Teams](docs/sdks/teams/README.md)

* [create_uuid](docs/sdks/teams/README.md#create_uuid) - CreateTeamsUuid
* [delete_installation](docs/sdks/teams/README.md#delete_installation) - DeleteInstallation
* [get_current_user](docs/sdks/teams/README.md#get_current_user) - GetCurrentUser
* [handle_o_auth_callback](docs/sdks/teams/README.md#handle_o_auth_callback) - HandleTeamsOAuthCallback
* [list_installations](docs/sdks/teams/README.md#list_installations) - ListInstallations
* [sync_workspace](docs/sdks/teams/README.md#sync_workspace) - SyncWorkspace

### [TeamsService](docs/sdks/teamsservice/README.md)

* [list_users](docs/sdks/teamsservice/README.md#list_users) - ListUsers

### [Topics](docs/sdks/topics/README.md)

* [refine_draft](docs/sdks/topics/README.md#refine_draft) - Custom topics

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from textql_sdk import TextQL
from textql_sdk.utils import BackoffStrategy, RetryConfig


with TextQL() as text_ql:

    res = text_ql.agent_services.create(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from textql_sdk import TextQL
from textql_sdk.utils import BackoffStrategy, RetryConfig


with TextQL(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
) as text_ql:

    res = text_ql.agent_services.create()

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`TextqlError`](./src/textql_sdk/errors/textqlerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                            |
| ------------------ | ---------------- | ------------------------------------------------------ |
| `err.message`      | `str`            | Error message                                          |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                     |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                  |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned. |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                      |

### Example
```python
from textql_sdk import TextQL, errors


with TextQL() as text_ql:
    res = None
    try:

        res = text_ql.agent_services.create()

        # Handle response
        print(res)


    except errors.TextqlError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

```

### Error Classes
**Primary error:**
* [`TextqlError`](./src/textql_sdk/errors/textqlerror.py): The base class for HTTP error responses.

<details><summary>Less common errors (5)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`TextqlError`](./src/textql_sdk/errors/textqlerror.py)**:
* [`ResponseValidationError`](./src/textql_sdk/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from textql_sdk import TextQL


with TextQL(
    server_url="https://app.textql.com",
) as text_ql:

    res = text_ql.agent_services.create()

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from textql_sdk import TextQL
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = TextQL(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from textql_sdk import TextQL
from textql_sdk.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = TextQL(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `TextQL` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from textql_sdk import TextQL
def main():

    with TextQL() as text_ql:
        # Rest of application here...


# Or when using async:
async def amain():

    async with TextQL() as text_ql:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from textql_sdk import TextQL
import logging

logging.basicConfig(level=logging.DEBUG)
s = TextQL(debug_logger=logging.getLogger("textql_sdk"))
```

You can also enable a default debug logger by setting an environment variable `TEXTQL_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=textql&utm_campaign=python)
