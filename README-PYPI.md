# textql

Developer-friendly & type-safe Python SDK specifically catered to leverage *textql* API.
[![License: MIT](https://img.shields.io/badge/LICENSE_//_MIT-3b5bdb?style=for-the-badge&labelColor=eff6ff)](https://opensource.org/licenses/MIT)

<!-- Start Summary [summary] -->
## Summary

TextQL API: TextQL public API. Generated from protobuf service definitions; internal
endpoints are excluded via google.api.visibility / file_visibility.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [textql](https://github.com/TextQLLabs/textql-python-v3/blob/master/#textql)
  * [SDK Installation](https://github.com/TextQLLabs/textql-python-v3/blob/master/#sdk-installation)
  * [IDE Support](https://github.com/TextQLLabs/textql-python-v3/blob/master/#ide-support)
  * [SDK Example Usage](https://github.com/TextQLLabs/textql-python-v3/blob/master/#sdk-example-usage)
  * [Authentication](https://github.com/TextQLLabs/textql-python-v3/blob/master/#authentication)
  * [Available Resources and Operations](https://github.com/TextQLLabs/textql-python-v3/blob/master/#available-resources-and-operations)
  * [Retries](https://github.com/TextQLLabs/textql-python-v3/blob/master/#retries)
  * [Error Handling](https://github.com/TextQLLabs/textql-python-v3/blob/master/#error-handling)
  * [Server Selection](https://github.com/TextQLLabs/textql-python-v3/blob/master/#server-selection)
  * [Custom HTTP Client](https://github.com/TextQLLabs/textql-python-v3/blob/master/#custom-http-client)
  * [Resource Management](https://github.com/TextQLLabs/textql-python-v3/blob/master/#resource-management)
  * [Debugging](https://github.com/TextQLLabs/textql-python-v3/blob/master/#debugging)
* [Development](https://github.com/TextQLLabs/textql-python-v3/blob/master/#development)
  * [Maturity](https://github.com/TextQLLabs/textql-python-v3/blob/master/#maturity)
  * [Contributions](https://github.com/TextQLLabs/textql-python-v3/blob/master/#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add textql-sdk
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install textql-sdk
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add textql-sdk
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

from textql_sdk import Textql

sdk = Textql(
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
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.agents.create()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
import os
from textql_sdk import Textql

async def main():

    async with Textql(
        api_key=os.getenv("TEXTQL_API_KEY", ""),
    ) as textql:

        res = await textql.agents.create_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name      | Type   | Scheme  | Environment Variable |
| --------- | ------ | ------- | -------------------- |
| `api_key` | apiKey | API key | `TEXTQL_API_KEY`     |

To authenticate with the API the `api_key` parameter must be set when initializing the SDK client instance. For example:
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.agents.create()

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [Agents](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/agents/README.md)

* [create](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/agents/README.md#create) - CreateAgent
* [delete](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/agents/README.md#delete) - DeleteAgent
* [duplicate](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/agents/README.md#duplicate) - DuplicateAgent
* [get_agent](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/agents/README.md#get_agent) - GetAgent
* [get_db_schema](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/agents/README.md#get_db_schema) - GetAgentDBSchema
* [get_db_table_preview](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/agents/README.md#get_db_table_preview) - GetAgentDBTablePreview
* [get_run](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/agents/README.md#get_run) - GetAgentRun
* [list_runs](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/agents/README.md#list_runs) - ListAgentRuns
* [list](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/agents/README.md#list) - ListAgents
* [reset_agent_avatar](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/agents/README.md#reset_agent_avatar) - ResetAgentAvatar
* [trigger_agent](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/agents/README.md#trigger_agent) - TriggerAgent
* [update](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/agents/README.md#update) - UpdateAgent
* [upload_agent_avatar](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/agents/README.md#upload_agent_avatar) - UploadAgentAvatar

### [Apps](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/apps/README.md)

* [heartbeat](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/apps/README.md#heartbeat) - Keeps the viewed app's compute worker alive; first view spawns and pre-warms it (dashboard viewer-TTL parity).
* [create_app](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/apps/README.md#create_app) - CreateApp
* [delete_app](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/apps/README.md#delete_app) - DeleteApp
* [duplicate](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/apps/README.md#duplicate) - Duplicates an app the caller can view into a new app they own,  named "Copy of <name>". Copies code/files/data sources/compute functions/  schedule; never carries over the source's data snapshot.
* [get](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/apps/README.md#get) - GetApp
* [get_db_schema](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/apps/README.md#get_db_schema) - GetAppDBSchema
* [get_db_table_preview](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/apps/README.md#get_db_table_preview) - Cross-member live activity: rows from every member of the app after a seq,  each carrying member_id + display_name (resolved server-side; never email).
* [get_member_state](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/apps/README.md#get_member_state) - Ordering overlay for the sidebar Bookmarks section: one position list per  member covering favorites and thread bookmarks ('<kind>:<id>' keys).  Membership truth stays in library_favorite / chat bookmarks; this persists  only the drag-and-drop order.
* [get_app_version](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/apps/README.md#get_app_version) - GetAppVersion
* [get_app_view_stats](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/apps/README.md#get_app_view_stats) - Lists the calling member's favorited library items (apps, dashboards,  agents) for the sidebar Pinned section: id, type, name, preview screenshot.
* [get_members_with_apps](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/apps/README.md#get_members_with_apps) - GetMembersWithApps
* [invoke_compute_function](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/apps/README.md#invoke_compute_function) - Executes a declared compute function on a pooled sandbox worker; gated, org-scoped, rate-limited.
* [list_activity_since](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/apps/README.md#list_activity_since) - Per-member app state: one JSON blob per (app, member) so apps remember  settings/progress. Member always resolved server-side from auth context;  per-member persistence, so viewers with read access can save their own state.
* [list_versions](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/apps/README.md#list_versions) - Version history: git-backed, one version per save (plus legacy publish-era snapshots); authors can list and restore.
* [list](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/apps/README.md#list) - ListApps
* [list_my_member_activity](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/apps/README.md#list_my_member_activity) - Staff-only (superadmin gated in-handler): publishes the embedded component  gallery as an app tree and returns its signed viewer URL.
* [move_app_to_folder](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/apps/README.md#move_app_to_folder) - Moves an app into a library folder (or to root when folder_id is empty).
* [presence_heartbeat](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/apps/README.md#presence_heartbeat) - Append-only per-member activity log. Listing is own rows only; no  cross-member reads in this release.
* [record_member_activity](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/apps/README.md#record_member_activity) - View analytics: reads the engagement views recorded on app page load.
* [refresh](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/apps/README.md#refresh) - Re-fetches data sources, rebuilds the document with a fresh snapshot, re-uploads.
* [restore_app_version](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/apps/README.md#restore_app_version) - RestoreAppVersion
* [set_member_state](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/apps/README.md#set_member_state) - Replaces the calling member's entire ordering; capped server-side.
* [set_favorite](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/apps/README.md#set_favorite) - Favorite/unfavorite a library item (app or dashboard) for the calling member.  Per-member, per-org; favorited=false hard-deletes the row. Covers both primitives  since the merged library page pins apps and dashboards through one client.
* [update](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/apps/README.md#update) - UpdateApp

### [AuditLogs](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/auditlogs/README.md)

* [configure_otlp_export](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/auditlogs/README.md#configure_otlp_export) - ConfigureOtlpExport
* [configure_s3_export](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/auditlogs/README.md#configure_s3_export) - ConfigureS3Export
* [delete_otlp_export_config](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/auditlogs/README.md#delete_otlp_export_config) - DeleteOtlpExportConfig
* [delete_s3_export_config](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/auditlogs/README.md#delete_s3_export_config) - DeleteS3ExportConfig
* [get_otlp_export_config](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/auditlogs/README.md#get_otlp_export_config) - GetOtlpExportConfig
* [get_s3_export_config](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/auditlogs/README.md#get_s3_export_config) - GetS3ExportConfig
* [list](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/auditlogs/README.md#list) - ListAuditLogs
* [test_otlp_export_connection](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/auditlogs/README.md#test_otlp_export_connection) - TestOtlpExportConnection
* [test_s3_export_connection](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/auditlogs/README.md#test_s3_export_connection) - TestS3ExportConnection
* [trigger_otlp_export](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/auditlogs/README.md#trigger_otlp_export) - TriggerOtlpExport
* [trigger_s3_export](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/auditlogs/README.md#trigger_s3_export) - TriggerS3Export

### [Chats](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md)

* [approve_context_prompt_change](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#approve_context_prompt_change) - ApproveContextPromptChange
* [approve_ontology_change](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#approve_ontology_change) - ApproveOntologyChange
* [attach_agent](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#attach_agent) - AttachAgentToChat
* [attach_app](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#attach_app) - AttachApp
* [attach_dashboard](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#attach_dashboard) - AttachDashboard
* [attach_dataset](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#attach_dataset) - RateChatCell appends a row to cell_rating for every click; thumbs-down also upserts a user_thumbs_down thread_warning.
* [bookmark](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#bookmark) - BookmarkChat
* [cancel_stream](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#cancel_stream) - CancelStream
* [check_permissions](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#check_permissions) - CheckChatPermissions
* [check_health](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#check_health) - CheckHealth
* [check_streamlit_health](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#check_streamlit_health) - CheckStreamlitHealth
* [create_chat](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#create_chat) - CreateChat
* [delete](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#delete) - DeleteChat
* [dismiss_questions](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#dismiss_questions) - Resolve a halted questions cell. Submit hands the answers to the agent and  resumes it; Dismiss hands over only the answered count and does NOT resume  (the user's next message becomes the dismissal reason).
* [duplicate_chat](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#duplicate_chat) - DuplicateChat
* [get_api_answer](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#get_api_answer) - GetAPIChatAnswer
* [get_artifact](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#get_artifact) - GetArtifact
* [get](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#get) - GetChat
* [get_artifacts_summary](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#get_artifacts_summary) - GetChatArtifactsSummary
* [get_chat_execution_timing](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#get_chat_execution_timing) - GetChatExecutionTiming
* [get_history](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#get_history) - GetChatHistory
* [get_all](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#get_all) - GetChats
* [get_completion_parameters](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#get_completion_parameters) - List distinct chat creators the user can access
* [get_completion_parameters_batch](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#get_completion_parameters_batch) - GetCompletionParametersBatch
* [get_llm_usage](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#get_llm_usage) - GetLlmUsage
* [get_members_with_chats](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#get_members_with_chats) - GetMembersWithChats
* [get_playbook_chats](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#get_playbook_chats) - GetPlaybookChats
* [poll_events](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#poll_events) - PollChatEvents
* [query_one_shot](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#query_one_shot) - QueryOneShot
* [rate_cell](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#rate_cell) - RateChatCell
* [reject_context_prompt_change](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#reject_context_prompt_change) - RejectContextPromptChange
* [reject_ontology_change](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#reject_ontology_change) - Resolve a halted ask_approval form cell. Submit runs the form's submission  and continues the agent with the outcome; Reject discards it (passive, no  run); Dismiss treats it as a change request (no run, next message says what  to change). All three set the cell's outcome, like the other approve/deny cells.
* [run](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#run) - RunChat
* [send](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#send) - SendMessage
* [submit_context_prompt_change](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#submit_context_prompt_change) - SubmitContextPromptChange
* [submit_questions](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#submit_questions) - SubmitQuestions
* [unbookmark](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#unbookmark) - UnbookmarkChat
* [update](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/chats/README.md#update) - UpdateChat

### [Connectors](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/connectors/README.md)

* [create](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/connectors/README.md#create) - CreateConnector
* [delete](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/connectors/README.md#delete) - DeleteConnector
* [duplicate_connector](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/connectors/README.md#duplicate_connector) - DuplicateConnector
* [execute_query](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/connectors/README.md#execute_query) - ExecuteQuery
* [get](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/connectors/README.md#get) - GetConnector
* [get_connector_cell_durations](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/connectors/README.md#get_connector_cell_durations) - GetConnectorCellDurations
* [get_chats](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/connectors/README.md#get_chats) - GetConnectorChats
* [get_dashboards](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/connectors/README.md#get_dashboards) - GetConnectorDashboards
* [get_connector_stats](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/connectors/README.md#get_connector_stats) - GetConnectorStats
* [get_usage](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/connectors/README.md#get_usage) - GetConnectorUsage
* [get_connectors](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/connectors/README.md#get_connectors) - GetConnectors
* [get_example_queries](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/connectors/README.md#get_example_queries) - GetExampleQueries
* [get_table_preview](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/connectors/README.md#get_table_preview) - GetTablePreview
* [list_tables](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/connectors/README.md#list_tables) - ListConnectorTables
* [list_query_templates](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/connectors/README.md#list_query_templates) - ListQueryTemplates
* [test](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/connectors/README.md#test) - TestConnector
* [update](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/connectors/README.md#update) - UpdateConnector

### [Dashboards](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/dashboards/README.md)

* [check_health](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/dashboards/README.md#check_health) - CheckDashboardHealth
* [create_dashboard](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/dashboards/README.md#create_dashboard) - CRUD operations
* [create_folder](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/dashboards/README.md#create_folder) - Folder management
* [delete](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/dashboards/README.md#delete) - DeleteDashboard
* [delete_folder](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/dashboards/README.md#delete_folder) - DeleteDashboardFolder
* [discard_changes](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/dashboards/README.md#discard_changes) - DiscardDashboardChanges
* [duplicate](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/dashboards/README.md#duplicate) - DuplicateDashboard
* [get](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/dashboards/README.md#get) - GetDashboard
* [get_version](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/dashboards/README.md#get_version) - GetDashboardVersion
* [get_dashboard_view_stats](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/dashboards/README.md#get_dashboard_view_stats) - View analytics
* [get_members_with_dashboards](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/dashboards/README.md#get_members_with_dashboards) - Member management
* [list_folders](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/dashboards/README.md#list_folders) - ListDashboardFolders
* [list_versions](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/dashboards/README.md#list_versions) - Version history
* [list](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/dashboards/README.md#list) - ListDashboards
* [move_to_folder](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/dashboards/README.md#move_to_folder) - MoveDashboardToFolder
* [preview_config](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/dashboards/README.md#preview_config) - Config-managed dashboards: render a `.dashboard` straight from a patch ref before  it merges (ADR-0022). Runs as the file's run_as, gated on the previewer being  authorized for it; persists nothing.
* [publish](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/dashboards/README.md#publish) - Publishing workflow
* [regenerate_screenshot](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/dashboards/README.md#regenerate_screenshot) - Screenshot management
* [restore_dashboard_version](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/dashboards/README.md#restore_dashboard_version) - RestoreDashboardVersion
* [run_scheduled_dashboard](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/dashboards/README.md#run_scheduled_dashboard) - RunScheduledDashboard
* [spawn](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/dashboards/README.md#spawn) - Dashboard execution
* [update_dashboard](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/dashboards/README.md#update_dashboard) - UpdateDashboard
* [update_dashboard_folder](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/dashboards/README.md#update_dashboard_folder) - UpdateDashboardFolder
* [update_dashboard_schedule](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/dashboards/README.md#update_dashboard_schedule) - Scheduling

### [Datasets](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/datasets/README.md)

* [create_folder](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/datasets/README.md#create_folder) - CreateFolder
* [create_power_bi_dataset](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/datasets/README.md#create_power_bi_dataset) - CreatePowerBIDataset
* [create_tableau_dataset](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/datasets/README.md#create_tableau_dataset) - Create Tableau dataset from views/datasources
* [create_upload_presign_url](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/datasets/README.md#create_upload_presign_url) - uploads
* [delete](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/datasets/README.md#delete) - Delete a dataset (soft delete)
* [export](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/datasets/README.md#export) - export dataset in "raw" format – original if dataset is uploaded, converted format otherwise (defaults to CSV)
* [fetch](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/datasets/README.md#fetch) - GetDataset, GetDatasets only return metadata
* [get_stats](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/datasets/README.md#get_stats) - GetDatasetStats
* [get_dataset_values](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/datasets/README.md#get_dataset_values) - GetDatasetValues
* [get](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/datasets/README.md#get) - GetDatasets
* [get_by_ids](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/datasets/README.md#get_by_ids) - GetDatasetsByIds
* [get_folders](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/datasets/README.md#get_folders) - for AR: CreateFolderACL, UpdateFolderACL, DeleteFolderACL
* [process_upload_presign_url](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/datasets/README.md#process_upload_presign_url) - ProcessUploadPresignUrl
* [update_dataset](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/datasets/README.md#update_dataset) - Update dataset metadata

### [Mcp](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/mcp/README.md)

* [clear_o_auth_token](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/mcp/README.md#clear_o_auth_token) - ClearOAuthToken
* [delete](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/mcp/README.md#delete) - DeleteMCPServer
* [get_servers](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/mcp/README.md#get_servers) - GetMCPServers
* [handle_o_auth_callback](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/mcp/README.md#handle_o_auth_callback) - HandleOAuthCallback
* [initiate_o_auth_flow](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/mcp/README.md#initiate_o_auth_flow) - InitiateOAuthFlow
* [toggle_server](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/mcp/README.md#toggle_server) - ToggleMCPServer
* [upsert_mcp_servers](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/mcp/README.md#upsert_mcp_servers) - UpsertMCPServers

### [MetricsExports](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/metricsexports/README.md)

* [configure](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/metricsexports/README.md#configure) - ConfigureMetricsExport
* [delete_config](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/metricsexports/README.md#delete_config) - DeleteMetricsExportConfig
* [get_metrics_export_config](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/metricsexports/README.md#get_metrics_export_config) - GetMetricsExportConfig
* [test_connection](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/metricsexports/README.md#test_connection) - TestMetricsExportConnection
* [trigger_push](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/metricsexports/README.md#trigger_push) - TriggerMetricsPush

### [Observability](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md)

* [activate_custom_topic](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#activate_custom_topic) - ActivateCustomTopic
* [backfill_custom_topic](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#backfill_custom_topic) - BackfillCustomTopic
* [backfill_thread_warnings](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#backfill_thread_warnings) - BackfillThreadWarnings
* [create_custom_topic](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#create_custom_topic) - Custom topics
* [deactivate_custom_topic](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#deactivate_custom_topic) - DeactivateCustomTopic
* [delete_custom_topic](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#delete_custom_topic) - DeleteCustomTopic
* [export_csv](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#export_csv) - ExportObservabilityCsv
* [fix_check_record](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#fix_check_record) - FixCheckRecord
* [fix_warning](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#fix_warning) - FixWarning
* [get_access_method_stats](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#get_access_method_stats) - GetAccessMethodStats
* [get_active_people_stats](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#get_active_people_stats) - GetActivePeopleStats
* [get_active_people_trend](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#get_active_people_trend) - GetActivePeopleTrend
* [get_backfill_preview](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#get_backfill_preview) - GetBackfillPreview
* [get_backfill_status](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#get_backfill_status) - GetBackfillStatus
* [get_billing_stats](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#get_billing_stats) - GetBillingStats
* [get_chat_source_stats](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#get_chat_source_stats) - GetChatSourceStats
* [get_chat_topics](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#get_chat_topics) - GetChatTopics
* [get_check_record_fix](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#get_check_record_fix) - GetCheckRecordFix
* [get_custom_topic](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#get_custom_topic) - GetCustomTopic
* [get_custom_topic_people](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#get_custom_topic_people) - GetCustomTopicPeople
* [get_custom_topic_threads](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#get_custom_topic_threads) - GetCustomTopicThreads
* [get_engagement_spectrum](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#get_engagement_spectrum) - GetEngagementSpectrum
* [get_member_activity](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#get_member_activity) - GetMemberActivity
* [get_member_signal_trend](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#get_member_signal_trend) - GetMemberSignalTrend
* [get_observability_stats](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#get_observability_stats) - GetObservabilityStats
* [get_thread_warnings](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#get_thread_warnings) - GetThreadWarnings
* [list_custom_topics](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#list_custom_topics) - ListCustomTopics
* [refine_draft](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#refine_draft) - RefineTopicDraft
* [set_topic_tag_feedback](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#set_topic_tag_feedback) - SetTopicTagFeedback
* [update_custom_topic](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/observability/README.md#update_custom_topic) - UpdateCustomTopic

### [Ontology](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md)

* [add_submodule](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#add_submodule) - AddOntologySubmodule
* [approve_patch](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#approve_patch) - ApprovePatch
* [configure_remote](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#configure_remote) - ConfigureOntologyRemote
* [create_approval_rule](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#create_approval_rule) - CreateApprovalRule
* [create_context_patch_auto_approve_rule](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#create_context_patch_auto_approve_rule) - CreateContextPatchAutoApproveRule
* [create_directory](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#create_directory) - CreateOntologyDirectory
* [create_file_upload_url](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#create_file_upload_url) - CreateOntologyFileUploadUrl
* [delete_approval_rule](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#delete_approval_rule) - DeleteApprovalRule
* [delete_context_patch_auto_approve_rule](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#delete_context_patch_auto_approve_rule) - DeleteContextPatchAutoApproveRule
* [delete_directory](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#delete_directory) - DeleteOntologyDirectory
* [delete_file](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#delete_file) - DeleteOntologyFile
* [delete_owners](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#delete_owners) - DeleteOntologyOwners
* [deny_patch](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#deny_patch) - DenyPatch
* [exchange_github_code](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#exchange_github_code) - ExchangeOntologyGithubCode
* [finalize_file_upload](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#finalize_file_upload) - FinalizeOntologyFileUpload
* [get_codeowner_coverage](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#get_codeowner_coverage) - GetCodeownerCoverage
* [get_config_export_capabilities](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#get_config_export_capabilities) - GetConfigExportCapabilities
* [get_effective_owners](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#get_effective_owners) - GetEffectiveOntologyOwners
* [get_file_usage](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#get_file_usage) - GetFileUsage
* [get_file_usage_timeline](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#get_file_usage_timeline) - GetFileUsageTimeline
* [get_ana_config](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#get_ana_config) - GetOntologyAnaConfig
* [get_file](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#get_file) - GetOntologyFile
* [get_github_o_auth_url](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#get_github_o_auth_url) - GetOntologyGithubOAuthURL
* [get_history_file_diff](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#get_history_file_diff) - GetOntologyHistoryFileDiff
* [get_owners](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#get_owners) - GetOntologyOwners
* [get_remote](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#get_remote) - GetOntologyRemote
* [get_size_timeline](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#get_size_timeline) - GetOntologySizeTimeline
* [get_sync_conflicts](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#get_sync_conflicts) - GetOntologySyncConflicts
* [get_usage_summary](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#get_usage_summary) - GetOntologyUsageSummary
* [get_patch](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#get_patch) - GetPatch
* [get_patch_by_number](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#get_patch_by_number) - GetPatchByNumber
* [get_patch_capabilities](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#get_patch_capabilities) - GetPatchCapabilities
* [get_raw_patch](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#get_raw_patch) - GetRawPatch
* [get_usage_details_for_file](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#get_usage_details_for_file) - GetUsageDetailsForFile
* [list_approval_rules](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#list_approval_rules) - ListApprovalRules
* [list_chats_for_file](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#list_chats_for_file) - ListChatsForFile
* [list_context_patch_auto_approve_rules](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#list_context_patch_auto_approve_rules) - ListContextPatchAutoApproveRules
* [list_golden_files](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#list_golden_files) - ListGoldenFiles
* [list_entries](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#list_entries) - ListOntologyEntries
* [list_history](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#list_history) - ListOntologyHistory
* [list_imports](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#list_imports) - ListOntologyImports
* [list_submodules](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#list_submodules) - ListOntologySubmodules
* [list_sync_runs](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#list_sync_runs) - ListOntologySyncRuns
* [list_patch_objects](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#list_patch_objects) - ListPatchObjects parses the config objects present at a patch's git ref and  returns each object's Library path, resolved display name, and granular type  (e.g. "playbook", "dashboard/streamlit", "dashboard/dash"). Parse-only: it  reuses the snapshot-at-ref + parse steps the preview path performs before  spawning — no sandbox spawn, no run_as authorization, no persistence. The  frontend uses the dashboard subtype to decide previewability (streamlit/dash).
* [list_patch_reviewers](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#list_patch_reviewers) - ListPatchReviewers
* [list_patches](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#list_patches) - ListPatches
* [list_skills](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#list_skills) - Lists the skills under the ontology's flat skills/ root that the caller can  read (OWNERS-filtered). Returns display metadata only — never instruction  bodies — feeding the chat composer's `/` autocomplete.
* [plan_merge](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#plan_merge) - PlanOntologyMerge
* [preview_pull_from_remote](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#preview_pull_from_remote) - TriggerConfigDriftReconcile forces an immediate config-sync catch-up for the  caller's org: if the Ontology repo's live HEAD differs from the last  reconciled commit, it enqueues a reconcile (otherwise no-op). The on-demand  equivalent of waiting for the periodic drift scan.
* [pull_from_remote](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#pull_from_remote) - PullOntologyFromRemote
* [push_to_remote](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#push_to_remote) - PushOntologyToRemote
* [recover](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#recover) - RecoverOntology
* [remove_remote](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#remove_remote) - RemoveOntologyRemote
* [remove_submodule](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#remove_submodule) - RemoveOntologySubmodule
* [rename_file](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#rename_file) - RenameOntologyFile
* [request_patch_review](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#request_patch_review) - RequestPatchReview
* [resolve_sync_conflict](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#resolve_sync_conflict) - ResolveOntologySyncConflict
* [restore_patch](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#restore_patch) - RestorePatch
* [revert_patch](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#revert_patch) - RevertPatch
* [save_all_objects_as_config](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#save_all_objects_as_config) - SaveAllObjectsAsConfig
* [save_object_as_config](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#save_object_as_config) - SaveObjectAsConfig
* [set_file_golden](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#set_file_golden) - SetOntologyFileGolden
* [trigger_config_drift_reconcile](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#trigger_config_drift_reconcile) - TriggerConfigDriftReconcile
* [update_approval_rule](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#update_approval_rule) - UpdateApprovalRule
* [update_context_patch_auto_approve_rule](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#update_context_patch_auto_approve_rule) - UpdateContextPatchAutoApproveRule
* [update_sync_config](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#update_sync_config) - UpdateOntologySyncConfig
* [upsert_ana_config](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#upsert_ana_config) - UpsertOntologyAnaConfig
* [upsert_file](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#upsert_file) - UpsertOntologyFile
* [upsert_owners](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#upsert_owners) - UpsertOntologyOwners
* [validate_config](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/ontology/README.md#validate_config) - Read-only functional validation of a proposed config: parse + dependency  resolution/reachability, no authorization and no persistence. "ok" means  functionally valid, not "guaranteed to merge" — the merge gate re-checks  authorization at approve time.

### [Playbooks](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md)

* [attach_dashboard](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#attach_dashboard) - AttachDashboard
* [attach_dataset](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#attach_dataset) - AttachDataset
* [cancel_template_execution](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#cancel_template_execution) - Cancel template execution for a specific template header
* [create_playbook](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#create_playbook) - CreatePlaybook
* [deactivate](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#deactivate) - DeactivatePlaybook
* [delete](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#delete) - DeletePlaybook
* [demo_playbook](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#demo_playbook) - DemoPlaybook
* [deploy](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#deploy) - DeployPlaybook
* [duplicate](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#duplicate) - DuplicatePlaybook
* [favorite_report](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#favorite_report) - Favorite report management
* [get_active_subscribed_count](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#get_active_subscribed_count) - GetActiveSubscribedPlaybooksCount
* [get_chat_reports_summary](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#get_chat_reports_summary) - Lightweight endpoint for chat report drawer - returns summaries without full blocks
* [get_members_with](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#get_members_with) - GetMembersWithPlaybooks
* [fetch](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#fetch) - GetPlaybook
* [get_batch_run](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#get_batch_run) - Get a specific batch run
* [get_playbook_lineage](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#get_playbook_lineage) - GetPlaybookLineage
* [get_reports](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#get_reports) - GetPlaybookReports
* [get_playbook_reports_batch](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#get_playbook_reports_batch) - Get reports for multiple template data IDs in a single batch request
* [get](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#get) - GetPlaybooks
* [get_playbooks_previews](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#get_playbooks_previews) - GetPlaybooksPreviews
* [get_report_by_id](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#get_report_by_id) - Get a single report by ID
* [get_reports_with_filters](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#get_reports_with_filters) - GetReportsWithFilters
* [list_slack_channel_context_playbooks](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#list_slack_channel_context_playbooks) - List all Slack channels context playbook mappings for the organization
* [list_all_teams_channel_context_playbooks](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#list_all_teams_channel_context_playbooks) - ListAllTeamsChannelContextPlaybooks
* [list_batch_runs](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#list_batch_runs) - List batch runs for a playbook
* [list_slack_channels_for_context](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#list_slack_channels_for_context) - List Slack channel IDs where the given playbook is set as the context
* [list_teams_channels_for_context_playbook](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#list_teams_channels_for_context_playbook) - ListTeamsChannelsForContextPlaybook
* [mark_report_as_read](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#mark_report_as_read) - Report read tracking
* [preview_slack_report](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#preview_slack_report) - PreviewSlackReport
* [remove_dashboard](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#remove_dashboard) - RemoveDashboard
* [remove_dataset](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#remove_dataset) - RemoveDataset
* [run](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#run) - RunPlaybook
* [set_slack_channel_context_playbook](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#set_slack_channel_context_playbook) - Set the context playbook for a Slack channel. This associates the given  playbook to a Slack channel so that Slack messages in that channel use the  playbook's context by default.
* [set_teams_channel_context](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#set_teams_channel_context) - SetTeamsChannelContextPlaybook
* [subscribe](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#subscribe) - SubscribeToPlaybook
* [unset_slack_channel_context_playbook](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#unset_slack_channel_context_playbook) - Unset the context playbook for a Slack channel. This clears any association  so that messages in this channel no longer use a specific playbook context.
* [unset_teams_channel_context](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#unset_teams_channel_context) - UnsetTeamsChannelContextPlaybook
* [unsubscribe](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#unsubscribe) - UnsubscribeFromPlaybook
* [update](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/playbooks/README.md#update) - UpdatePlaybook

### [Powerbi](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/powerbisdk/README.md)

* [export_report_image](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/powerbisdk/README.md#export_report_image) - ExportPowerBIReportImage
* [generate_embed_token](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/powerbisdk/README.md#generate_embed_token) - GeneratePowerBIEmbedToken
* [get_dataset_preview](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/powerbisdk/README.md#get_dataset_preview) - GetPowerBIDatasetPreview
* [get_synced_items](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/powerbisdk/README.md#get_synced_items) - GetSyncedPowerBIItems
* [list](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/powerbisdk/README.md#list) - ListPowerBIDatasets
* [list_reports](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/powerbisdk/README.md#list_reports) - ListPowerBIReports
* [list_workspaces](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/powerbisdk/README.md#list_workspaces) - ListPowerBIWorkspaces
* [sync_power_bi_items](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/powerbisdk/README.md#sync_power_bi_items) - SyncPowerBIItems
* [test_connection](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/powerbisdk/README.md#test_connection) - TestPowerBIConnection
* [unsync_items](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/powerbisdk/README.md#unsync_items) - UnsyncPowerBIItems

### [Rbac](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/rbac/README.md)

* [assign_permission_to_role](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/rbac/README.md#assign_permission_to_role) - AssignPermissionToRole
* [assign_role_to_member](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/rbac/README.md#assign_role_to_member) - Member role assignment
* [create_api_key](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/rbac/README.md#create_api_key) - Group management. Internal only.
* [create_role](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/rbac/README.md#create_role) - Role management
* [create_service_account](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/rbac/README.md#create_service_account) - CreateServiceAccount
* [delete_role](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/rbac/README.md#delete_role) - DeleteRole
* [delete_service_account](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/rbac/README.md#delete_service_account) - DeleteServiceAccount
* [get_current_member_roles_and_permissions](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/rbac/README.md#get_current_member_roles_and_permissions) - Get current member roles and permissions
* [get_embed_user_api_key](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/rbac/README.md#get_embed_user_api_key) - GetEmbedUserApiKey
* [get_member_roles](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/rbac/README.md#get_member_roles) - GetMemberRoles
* [get_role](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/rbac/README.md#get_role) - GetRole
* [get_role_permissions](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/rbac/README.md#get_role_permissions) - GetRolePermissions
* [list_api_keys](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/rbac/README.md#list_api_keys) - ListApiKeys
* [list_permissions](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/rbac/README.md#list_permissions) - Permission management
* [list_roles](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/rbac/README.md#list_roles) - ListRoles
* [list_service_accounts](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/rbac/README.md#list_service_accounts) - ListServiceAccounts
* [remove_permission_from_role](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/rbac/README.md#remove_permission_from_role) - RemovePermissionFromRole
* [remove_role_from_member](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/rbac/README.md#remove_role_from_member) - RemoveRoleFromMember
* [revoke_api_key](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/rbac/README.md#revoke_api_key) - RevokeApiKey
* [rotate_api_key](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/rbac/README.md#rotate_api_key) - RotateApiKey
* [set_role_permissions](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/rbac/README.md#set_role_permissions) - Bulk add/remove permissions on a role in one call, producing a single audit entry for the whole edit.
* [update_role](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/rbac/README.md#update_role) - UpdateRole
* [who_am_i](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/rbac/README.md#who_am_i) - Describe what a key is allowed to do.

### [Sandbox](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/sandbox/README.md)

* [execute_query](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/sandbox/README.md#execute_query) - ExecuteQuery

### [SandboxAdmin](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/sandboxadmin/README.md)

* [get_sandbox](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/sandboxadmin/README.md#get_sandbox) - GetSandbox
* [list_sandbox_egress](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/sandboxadmin/README.md#list_sandbox_egress) - Outbound HTTP(S) calls a sandbox made (the egress ledger). Durable — reads  the recorded table, so it works for stopped sandboxes too.
* [list_executions](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/sandboxadmin/README.md#list_executions) - ListSandboxExecutions
* [list_sandbox_files](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/sandboxadmin/README.md#list_sandbox_files) - Live filesystem of a running sandbox. Both are NO-OP (read-only) and only  return data while the worker is alive; available=false otherwise.
* [list_sandbox_spend](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/sandboxadmin/README.md#list_sandbox_spend) - Per-lease compute usage for a sandbox, computed from lease durations × the  compute rate. Durable (reads the lease table), so it works for stopped  sandboxes. This is usage (ACUs), not the invoiced dollar amount.
* [list](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/sandboxadmin/README.md#list) - ListSandboxes
* [read_file](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/sandboxadmin/README.md#read_file) - ReadSandboxFile
* [restart_sandbox](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/sandboxadmin/README.md#restart_sandbox) - Restart a stopped/reaped sandbox by re-acquiring a worker for the same  sandbox_id, preserving the original owner. Same scoping as StopSandbox  (owner, or sandbox:write_private for org-wide).
* [stop](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/sandboxadmin/README.md#stop) - StopSandbox

### [SandboxCapabilities](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/sandboxcapabilities/README.md)

* [execute_write](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/sandboxcapabilities/README.md#execute_write) - ExecuteWrite
* [poll_ask](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/sandboxcapabilities/README.md#poll_ask) - PollAsk
* [put_asset](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/sandboxcapabilities/README.md#put_asset) - PutAsset
* [send_notify](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/sandboxcapabilities/README.md#send_notify) - SendNotify
* [start_ask](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/sandboxcapabilities/README.md#start_ask) - StartAsk
* [state_op](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/sandboxcapabilities/README.md#state_op) - StateOp

### [Scim](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/scim/README.md)

* [create_o_auth_client](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/scim/README.md#create_o_auth_client) - CreateScimOAuthClient
* [create_scim_token](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/scim/README.md#create_scim_token) - CreateScimToken
* [list_scim_o_auth_clients](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/scim/README.md#list_scim_o_auth_clients) - ListScimOAuthClients
* [list](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/scim/README.md#list) - ListScimTokens
* [revoke_o_auth_client](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/scim/README.md#revoke_o_auth_client) - RevokeScimOAuthClient
* [revoke_scim_token](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/scim/README.md#revoke_scim_token) - RevokeScimToken

### [Secrets](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/secrets/README.md)

* [delete_secret](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/secrets/README.md#delete_secret) - DeleteSecret
* [get_members_with_secrets](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/secrets/README.md#get_members_with_secrets) - GetMembersWithSecrets
* [list_secrets](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/secrets/README.md#list_secrets) - ListSecrets
* [put_secret](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/secrets/README.md#put_secret) - PutSecret
* [update](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/secrets/README.md#update) - UpdateSecret

### [Settings](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/settings/README.md)

* [check_member_status](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/settings/README.md#check_member_status) - CheckMemberStatus
* [delete_member](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/settings/README.md#delete_member) - DeleteOrganizationMember
* [invite_member](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/settings/README.md#invite_member) - InviteOrganizationMember
* [list_members](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/settings/README.md#list_members) - ListOrganizationMembers
* [update](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/settings/README.md#update) - UpdateOrganizationSettings

### [Slack](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/slack/README.md)

* [create_uuid](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/slack/README.md#create_uuid) - CreateSlackUuid
* [delete_installation](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/slack/README.md#delete_installation) - DeleteInstallation
* [get_current_user](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/slack/README.md#get_current_user) - GetCurrentUser
* [handle_o_auth_callback](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/slack/README.md#handle_o_auth_callback) - HandleSlackOAuthCallback
* [list_channels](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/slack/README.md#list_channels) - ListChannels
* [list_installations](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/slack/README.md#list_installations) - ListInstallations
* [list_users](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/slack/README.md#list_users) - ListUsers
* [sync_workspace](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/slack/README.md#sync_workspace) - SyncWorkspace

### [Tableau](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/tableausdk/README.md)

* [generate_embed_token](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/tableausdk/README.md#generate_embed_token) - Generate JWT token for embedding views
* [get_collection_thumbnail](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/tableausdk/README.md#get_collection_thumbnail) - Get collection thumbnail (first view image)
* [get_connected_app_status](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/tableausdk/README.md#get_connected_app_status) - GetConnectedAppStatus
* [get_starred_items](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/tableausdk/README.md#get_starred_items) - GetStarredTableauItems
* [list_tableau_datasources](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/tableausdk/README.md#list_tableau_datasources) - List Tableau datasources
* [list_projects](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/tableausdk/README.md#list_projects) - List Tableau projects
* [list_views](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/tableausdk/README.md#list_views) - List Tableau views
* [list_workbooks](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/tableausdk/README.md#list_workbooks) - List Tableau workbooks
* [refresh_collection](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/tableausdk/README.md#refresh_collection) - RefreshTableauCollection
* [reset_connected_app](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/tableausdk/README.md#reset_connected_app) - ResetConnectedApp
* [star_item](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/tableausdk/README.md#star_item) - Star/unstar items
* [test_tableau_connection](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/tableausdk/README.md#test_tableau_connection) - Test a Tableau connection
* [unstar_tableau_item](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/tableausdk/README.md#unstar_tableau_item) - UnstarTableauItem

### [Teams](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/teams/README.md)

* [create_uuid](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/teams/README.md#create_uuid) - CreateTeamsUuid
* [delete_installation](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/teams/README.md#delete_installation) - DeleteInstallation
* [get_current_user](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/teams/README.md#get_current_user) - GetCurrentUser
* [handle_o_auth_callback](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/teams/README.md#handle_o_auth_callback) - HandleTeamsOAuthCallback
* [list](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/teams/README.md#list) - ListChannels
* [list_installations](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/teams/README.md#list_installations) - ListInstallations
* [list_users](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/teams/README.md#list_users) - ListUsers
* [sync_workspace](https://github.com/TextQLLabs/textql-python-v3/blob/master/docs/sdks/teams/README.md#sync_workspace) - SyncWorkspace

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
import os
from textql_sdk import Textql
from textql_sdk.utils import BackoffStrategy, RetryConfig


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.agents.create(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
import os
from textql_sdk import Textql
from textql_sdk.utils import BackoffStrategy, RetryConfig


with Textql(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.agents.create()

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`TextqlError`](https://github.com/TextQLLabs/textql-python-v3/blob/master/./src/textql_sdk/errors/textqlerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                            |
| ------------------ | ---------------- | ------------------------------------------------------ |
| `err.message`      | `str`            | Error message                                          |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                     |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                  |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned. |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                      |

### Example
```python
import os
from textql_sdk import Textql, errors


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:
    res = None
    try:

        res = textql.agents.create()

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
* [`TextqlError`](https://github.com/TextQLLabs/textql-python-v3/blob/master/./src/textql_sdk/errors/textqlerror.py): The base class for HTTP error responses.

<details><summary>Less common errors (5)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`TextqlError`](https://github.com/TextQLLabs/textql-python-v3/blob/master/./src/textql_sdk/errors/textqlerror.py)**:
* [`ResponseValidationError`](https://github.com/TextQLLabs/textql-python-v3/blob/master/./src/textql_sdk/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import os
from textql_sdk import Textql


with Textql(
    server_url="https://app.textql.com",
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.agents.create()

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
from textql_sdk import Textql
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Textql(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from textql_sdk import Textql
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

s = Textql(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Textql` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
import os
from textql_sdk import Textql
def main():

    with Textql(
        api_key=os.getenv("TEXTQL_API_KEY", ""),
    ) as textql:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Textql(
        api_key=os.getenv("TEXTQL_API_KEY", ""),
    ) as textql:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from textql_sdk import Textql
import logging

logging.basicConfig(level=logging.DEBUG)
s = Textql(debug_logger=logging.getLogger("textql_sdk"))
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
