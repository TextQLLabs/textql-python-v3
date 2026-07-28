# pylint: skip-file
# mypy: ignore-errors
import datetime
from ..google.api import visibility_pb2 as _visibility_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ..public import apps_pb2 as _apps_pb2
from ..public import cells_pb2 as _cells_pb2
from ..public import dashboard_pb2 as _dashboard_pb2
from ..public import dataset_pb2 as _dataset_pb2
from ..public import identity_pb2 as _identity_pb2
from ..public import llm_model_pb2 as _llm_model_pb2
from ..public import paradigm_pb2 as _paradigm_pb2
from ..public import warnings_pb2 as _warnings_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CellLifecycle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LIFECYCLE_UNKNOWN: _ClassVar[CellLifecycle]
    LIFECYCLE_CREATING: _ClassVar[CellLifecycle]
    LIFECYCLE_CREATED: _ClassVar[CellLifecycle]
    LIFECYCLE_EXECUTING: _ClassVar[CellLifecycle]
    LIFECYCLE_EXECUTED: _ClassVar[CellLifecycle]
    LIFECYCLE_HALTED: _ClassVar[CellLifecycle]
    LIFECYCLE_HANDOFF_PENDING: _ClassVar[CellLifecycle]

class ChatSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHAT_SOURCE_UNKNOWN: _ClassVar[ChatSource]
    CHAT_SOURCE_THREAD: _ClassVar[ChatSource]
    CHAT_SOURCE_PLAYBOOK: _ClassVar[ChatSource]
    CHAT_SOURCE_TEMPLATE: _ClassVar[ChatSource]
    CHAT_SOURCE_SLACK: _ClassVar[ChatSource]
    CHAT_SOURCE_AGENT: _ClassVar[ChatSource]
    CHAT_SOURCE_FEED: _ClassVar[ChatSource]
    CHAT_SOURCE_TEAMS: _ClassVar[ChatSource]
    CHAT_SOURCE_SMS: _ClassVar[ChatSource]
    CHAT_SOURCE_MCP: _ClassVar[ChatSource]
    CHAT_SOURCE_SYSTEM: _ClassVar[ChatSource]

class Methodology(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    METHODOLOGY_UNKNOWN: _ClassVar[Methodology]
    METHODOLOGY_ADAPTIVE: _ClassVar[Methodology]
    METHODOLOGY_PRESCRIPTIVE: _ClassVar[Methodology]
    METHODOLOGY_THOROUGH: _ClassVar[Methodology]
    METHODOLOGY_CAREFUL: _ClassVar[Methodology]
    METHODOLOGY_ONTOLOGY_BUILDING: _ClassVar[Methodology]

class CellRating(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CELL_RATING_UNSPECIFIED: _ClassVar[CellRating]
    CELL_RATING_NONE: _ClassVar[CellRating]
    CELL_RATING_UP: _ClassVar[CellRating]
    CELL_RATING_DOWN: _ClassVar[CellRating]

class ChatSortField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHAT_SORT_FIELD_UNKNOWN: _ClassVar[ChatSortField]
    CHAT_SORT_FIELD_NAME: _ClassVar[ChatSortField]
    CHAT_SORT_FIELD_CREATED_AT: _ClassVar[ChatSortField]
    CHAT_SORT_FIELD_UPDATED_AT: _ClassVar[ChatSortField]

class ChatSortDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHAT_SORT_DIRECTION_UNKNOWN: _ClassVar[ChatSortDirection]
    CHAT_SORT_DIRECTION_ASC: _ClassVar[ChatSortDirection]
    CHAT_SORT_DIRECTION_DESC: _ClassVar[ChatSortDirection]

class HealthStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATUS_UNKNOWN: _ClassVar[HealthStatus]
    STATUS_HEALTHY: _ClassVar[HealthStatus]
    STATUS_MINOR: _ClassVar[HealthStatus]
    STATUS_MAJOR: _ClassVar[HealthStatus]
    STATUS_CRITICAL: _ClassVar[HealthStatus]

class StreamlitHealthStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STREAMLIT_HEALTH_STATUS_NOT_RUNNING: _ClassVar[StreamlitHealthStatus]
    STREAMLIT_HEALTH_STATUS_HEALTHY: _ClassVar[StreamlitHealthStatus]
    STREAMLIT_HEALTH_STATUS_STARTING: _ClassVar[StreamlitHealthStatus]
    STREAMLIT_HEALTH_STATUS_FAILED: _ClassVar[StreamlitHealthStatus]
    STREAMLIT_HEALTH_STATUS_UPDATING: _ClassVar[StreamlitHealthStatus]

class ArtifactType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ARTIFACT_TYPE_UNKNOWN: _ClassVar[ArtifactType]
    ARTIFACT_TYPE_IMAGE: _ClassVar[ArtifactType]
    ARTIFACT_TYPE_CSV: _ClassVar[ArtifactType]
    ARTIFACT_TYPE_PDF: _ClassVar[ArtifactType]
    ARTIFACT_TYPE_HTML: _ClassVar[ArtifactType]
    ARTIFACT_TYPE_TEXT: _ClassVar[ArtifactType]
    ARTIFACT_TYPE_STREAMLIT: _ClassVar[ArtifactType]
    ARTIFACT_TYPE_DASHBOARD: _ClassVar[ArtifactType]
    ARTIFACT_TYPE_FORM: _ClassVar[ArtifactType]
    ARTIFACT_TYPE_REPORT: _ClassVar[ArtifactType]
    ARTIFACT_TYPE_AGENT: _ClassVar[ArtifactType]
    ARTIFACT_TYPE_HTML_CHART: _ClassVar[ArtifactType]
    ARTIFACT_TYPE_APP: _ClassVar[ArtifactType]
LIFECYCLE_UNKNOWN: CellLifecycle
LIFECYCLE_CREATING: CellLifecycle
LIFECYCLE_CREATED: CellLifecycle
LIFECYCLE_EXECUTING: CellLifecycle
LIFECYCLE_EXECUTED: CellLifecycle
LIFECYCLE_HALTED: CellLifecycle
LIFECYCLE_HANDOFF_PENDING: CellLifecycle
CHAT_SOURCE_UNKNOWN: ChatSource
CHAT_SOURCE_THREAD: ChatSource
CHAT_SOURCE_PLAYBOOK: ChatSource
CHAT_SOURCE_TEMPLATE: ChatSource
CHAT_SOURCE_SLACK: ChatSource
CHAT_SOURCE_AGENT: ChatSource
CHAT_SOURCE_FEED: ChatSource
CHAT_SOURCE_TEAMS: ChatSource
CHAT_SOURCE_SMS: ChatSource
CHAT_SOURCE_MCP: ChatSource
CHAT_SOURCE_SYSTEM: ChatSource
METHODOLOGY_UNKNOWN: Methodology
METHODOLOGY_ADAPTIVE: Methodology
METHODOLOGY_PRESCRIPTIVE: Methodology
METHODOLOGY_THOROUGH: Methodology
METHODOLOGY_CAREFUL: Methodology
METHODOLOGY_ONTOLOGY_BUILDING: Methodology
CELL_RATING_UNSPECIFIED: CellRating
CELL_RATING_NONE: CellRating
CELL_RATING_UP: CellRating
CELL_RATING_DOWN: CellRating
CHAT_SORT_FIELD_UNKNOWN: ChatSortField
CHAT_SORT_FIELD_NAME: ChatSortField
CHAT_SORT_FIELD_CREATED_AT: ChatSortField
CHAT_SORT_FIELD_UPDATED_AT: ChatSortField
CHAT_SORT_DIRECTION_UNKNOWN: ChatSortDirection
CHAT_SORT_DIRECTION_ASC: ChatSortDirection
CHAT_SORT_DIRECTION_DESC: ChatSortDirection
STATUS_UNKNOWN: HealthStatus
STATUS_HEALTHY: HealthStatus
STATUS_MINOR: HealthStatus
STATUS_MAJOR: HealthStatus
STATUS_CRITICAL: HealthStatus
STREAMLIT_HEALTH_STATUS_NOT_RUNNING: StreamlitHealthStatus
STREAMLIT_HEALTH_STATUS_HEALTHY: StreamlitHealthStatus
STREAMLIT_HEALTH_STATUS_STARTING: StreamlitHealthStatus
STREAMLIT_HEALTH_STATUS_FAILED: StreamlitHealthStatus
STREAMLIT_HEALTH_STATUS_UPDATING: StreamlitHealthStatus
ARTIFACT_TYPE_UNKNOWN: ArtifactType
ARTIFACT_TYPE_IMAGE: ArtifactType
ARTIFACT_TYPE_CSV: ArtifactType
ARTIFACT_TYPE_PDF: ArtifactType
ARTIFACT_TYPE_HTML: ArtifactType
ARTIFACT_TYPE_TEXT: ArtifactType
ARTIFACT_TYPE_STREAMLIT: ArtifactType
ARTIFACT_TYPE_DASHBOARD: ArtifactType
ARTIFACT_TYPE_FORM: ArtifactType
ARTIFACT_TYPE_REPORT: ArtifactType
ARTIFACT_TYPE_AGENT: ArtifactType
ARTIFACT_TYPE_HTML_CHART: ArtifactType
ARTIFACT_TYPE_APP: ArtifactType

class AttachAgentToChatRequest(_message.Message):
    __slots__ = ('chat_id', 'agent_id')
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    agent_id: str

    def __init__(self, chat_id: _Optional[str]=..., agent_id: _Optional[str]=...) -> None:
        ...

class AttachAgentToChatResponse(_message.Message):
    __slots__ = ('chat',)
    CHAT_FIELD_NUMBER: _ClassVar[int]
    chat: Chat

    def __init__(self, chat: _Optional[_Union[Chat, _Mapping]]=...) -> None:
        ...

class Chat(_message.Message):
    __slots__ = ('id', 'paradigm', 'model', 'timestamp', 'org_id', 'member_id', 'summary', 'playbook_id', 'research', 'creator_email', 'api_key_client_id', 'updated_at', 'is_bookmarked', 'preferred_provider', 'template_data_id', 'batch_run_id', 'preview', 'dashboard_mode', 'source', 'methodology', 'is_running', 'is_unread', 'vllm_model_id', 'fast_mode', 'agent_id', 'agent_name', 'agent_profile_image_url', 'max_thinking')
    ID_FIELD_NUMBER: _ClassVar[int]
    PARADIGM_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    RESEARCH_FIELD_NUMBER: _ClassVar[int]
    CREATOR_EMAIL_FIELD_NUMBER: _ClassVar[int]
    API_KEY_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_BOOKMARKED_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_DATA_ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_MODE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    METHODOLOGY_FIELD_NUMBER: _ClassVar[int]
    IS_RUNNING_FIELD_NUMBER: _ClassVar[int]
    IS_UNREAD_FIELD_NUMBER: _ClassVar[int]
    VLLM_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    FAST_MODE_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    AGENT_PROFILE_IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    MAX_THINKING_FIELD_NUMBER: _ClassVar[int]
    id: str
    paradigm: _paradigm_pb2.Paradigm
    model: _llm_model_pb2.LlmModel
    timestamp: _timestamp_pb2.Timestamp
    org_id: str
    member_id: str
    summary: str
    playbook_id: str
    research: bool
    creator_email: str
    api_key_client_id: str
    updated_at: _timestamp_pb2.Timestamp
    is_bookmarked: bool
    preferred_provider: str
    template_data_id: str
    batch_run_id: str
    preview: str
    dashboard_mode: bool
    source: ChatSource
    methodology: Methodology
    is_running: bool
    is_unread: bool
    vllm_model_id: str
    fast_mode: bool
    agent_id: str
    agent_name: str
    agent_profile_image_url: str
    max_thinking: bool

    def __init__(self, id: _Optional[str]=..., paradigm: _Optional[_Union[_paradigm_pb2.Paradigm, _Mapping]]=..., model: _Optional[_Union[_llm_model_pb2.LlmModel, str]]=..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., org_id: _Optional[str]=..., member_id: _Optional[str]=..., summary: _Optional[str]=..., playbook_id: _Optional[str]=..., research: bool=..., creator_email: _Optional[str]=..., api_key_client_id: _Optional[str]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., is_bookmarked: bool=..., preferred_provider: _Optional[str]=..., template_data_id: _Optional[str]=..., batch_run_id: _Optional[str]=..., preview: _Optional[str]=..., dashboard_mode: bool=..., source: _Optional[_Union[ChatSource, str]]=..., methodology: _Optional[_Union[Methodology, str]]=..., is_running: bool=..., is_unread: bool=..., vllm_model_id: _Optional[str]=..., fast_mode: bool=..., agent_id: _Optional[str]=..., agent_name: _Optional[str]=..., agent_profile_image_url: _Optional[str]=..., max_thinking: bool=...) -> None:
        ...

class Cell(_message.Message):
    __slots__ = ('id', 'timestamp', 'complete', 'generated', 'lifecycle', 'tool_call_id', 'exec_error', 'sender_member_id', 'md_cell', 'py_cell', 'sql_cell', 'ans_cell', 'document_cell', 'ws_cell', 'report_cell', 'tabular_file_cell', 'status_cell', 'metrics_cell', 'summary_cell', 'tableau_cell', 'tableau_sql_cell', 'context_prompt_editor_cell', 'ontology_editor_cell', 'image_cell', 'text_cell', 'mcp_tool_cell', 'preview_cell', 'playbook_editor_cell', 'streamlit_cell', 'dashboard_cell', 'google_drive_content_cell', 'google_drive_search_cell', 'powerbi_cell', 'powerbi_dax_cell', 'form_editor_cell', 'tableau_search_fields_cell', 'report_history_cell', 'microsoft365_email_search_cell', 'microsoft365_email_content_cell', 'microsoft365_calendar_cell', 'feed_explorer_cell', 'bash_cell', 'javascript_cell', 'feed_post_cell', 'feed_comment_cell', 'feed_engage_cell', 'ontology_search_metrics_cell', 'ontology_open_object_cell', 'compaction_cell', 'gmail_email_search_cell', 'gmail_email_content_cell', 'list_dashboards_cell', 'list_users_cell', 'google_calendar_search_cell', 'feed_create_cell', 'ontology_query_cell', 'email_cell', 'patch_cell', 'linkedin_search_cell', 'use_skill_cell', 'form_cell', 'connectors_cell', 'questions_cell', 'app_cell', 'list_apps_cell', 'thinking_cell', 'tool_summary', 'duration_ms')
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_FIELD_NUMBER: _ClassVar[int]
    GENERATED_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    EXEC_ERROR_FIELD_NUMBER: _ClassVar[int]
    SENDER_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MD_CELL_FIELD_NUMBER: _ClassVar[int]
    PY_CELL_FIELD_NUMBER: _ClassVar[int]
    SQL_CELL_FIELD_NUMBER: _ClassVar[int]
    ANS_CELL_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_CELL_FIELD_NUMBER: _ClassVar[int]
    WS_CELL_FIELD_NUMBER: _ClassVar[int]
    REPORT_CELL_FIELD_NUMBER: _ClassVar[int]
    TABULAR_FILE_CELL_FIELD_NUMBER: _ClassVar[int]
    STATUS_CELL_FIELD_NUMBER: _ClassVar[int]
    METRICS_CELL_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_CELL_FIELD_NUMBER: _ClassVar[int]
    TABLEAU_CELL_FIELD_NUMBER: _ClassVar[int]
    TABLEAU_SQL_CELL_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_PROMPT_EDITOR_CELL_FIELD_NUMBER: _ClassVar[int]
    ONTOLOGY_EDITOR_CELL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_CELL_FIELD_NUMBER: _ClassVar[int]
    TEXT_CELL_FIELD_NUMBER: _ClassVar[int]
    MCP_TOOL_CELL_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_CELL_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOK_EDITOR_CELL_FIELD_NUMBER: _ClassVar[int]
    STREAMLIT_CELL_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_CELL_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_DRIVE_CONTENT_CELL_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_DRIVE_SEARCH_CELL_FIELD_NUMBER: _ClassVar[int]
    POWERBI_CELL_FIELD_NUMBER: _ClassVar[int]
    POWERBI_DAX_CELL_FIELD_NUMBER: _ClassVar[int]
    FORM_EDITOR_CELL_FIELD_NUMBER: _ClassVar[int]
    TABLEAU_SEARCH_FIELDS_CELL_FIELD_NUMBER: _ClassVar[int]
    REPORT_HISTORY_CELL_FIELD_NUMBER: _ClassVar[int]
    MICROSOFT365_EMAIL_SEARCH_CELL_FIELD_NUMBER: _ClassVar[int]
    MICROSOFT365_EMAIL_CONTENT_CELL_FIELD_NUMBER: _ClassVar[int]
    MICROSOFT365_CALENDAR_CELL_FIELD_NUMBER: _ClassVar[int]
    FEED_EXPLORER_CELL_FIELD_NUMBER: _ClassVar[int]
    BASH_CELL_FIELD_NUMBER: _ClassVar[int]
    JAVASCRIPT_CELL_FIELD_NUMBER: _ClassVar[int]
    FEED_POST_CELL_FIELD_NUMBER: _ClassVar[int]
    FEED_COMMENT_CELL_FIELD_NUMBER: _ClassVar[int]
    FEED_ENGAGE_CELL_FIELD_NUMBER: _ClassVar[int]
    ONTOLOGY_SEARCH_METRICS_CELL_FIELD_NUMBER: _ClassVar[int]
    ONTOLOGY_OPEN_OBJECT_CELL_FIELD_NUMBER: _ClassVar[int]
    COMPACTION_CELL_FIELD_NUMBER: _ClassVar[int]
    GMAIL_EMAIL_SEARCH_CELL_FIELD_NUMBER: _ClassVar[int]
    GMAIL_EMAIL_CONTENT_CELL_FIELD_NUMBER: _ClassVar[int]
    LIST_DASHBOARDS_CELL_FIELD_NUMBER: _ClassVar[int]
    LIST_USERS_CELL_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_CALENDAR_SEARCH_CELL_FIELD_NUMBER: _ClassVar[int]
    FEED_CREATE_CELL_FIELD_NUMBER: _ClassVar[int]
    ONTOLOGY_QUERY_CELL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_CELL_FIELD_NUMBER: _ClassVar[int]
    PATCH_CELL_FIELD_NUMBER: _ClassVar[int]
    LINKEDIN_SEARCH_CELL_FIELD_NUMBER: _ClassVar[int]
    USE_SKILL_CELL_FIELD_NUMBER: _ClassVar[int]
    FORM_CELL_FIELD_NUMBER: _ClassVar[int]
    CONNECTORS_CELL_FIELD_NUMBER: _ClassVar[int]
    QUESTIONS_CELL_FIELD_NUMBER: _ClassVar[int]
    APP_CELL_FIELD_NUMBER: _ClassVar[int]
    LIST_APPS_CELL_FIELD_NUMBER: _ClassVar[int]
    THINKING_CELL_FIELD_NUMBER: _ClassVar[int]
    TOOL_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    id: str
    timestamp: _timestamp_pb2.Timestamp
    complete: bool
    generated: bool
    lifecycle: CellLifecycle
    tool_call_id: str
    exec_error: str
    sender_member_id: str
    md_cell: _cells_pb2.MarkdownCell
    py_cell: _cells_pb2.PythonCell
    sql_cell: _cells_pb2.SQLCell
    ans_cell: _cells_pb2.AnswerCell
    document_cell: _cells_pb2.DocumentCell
    ws_cell: _cells_pb2.WebSearchCell
    report_cell: _cells_pb2.ReportCell
    tabular_file_cell: _cells_pb2.TabularFileCell
    status_cell: _cells_pb2.StatusCell
    metrics_cell: _cells_pb2.MetricsCell
    summary_cell: _cells_pb2.SummaryCell
    tableau_cell: _cells_pb2.TableauCell
    tableau_sql_cell: _cells_pb2.TableauSQLCell
    context_prompt_editor_cell: _cells_pb2.ContextPromptEditorCell
    ontology_editor_cell: _cells_pb2.OntologyEditorCell
    image_cell: _cells_pb2.ImageCell
    text_cell: _cells_pb2.TextCell
    mcp_tool_cell: _cells_pb2.MCPToolCell
    preview_cell: _cells_pb2.PreviewCell
    playbook_editor_cell: _cells_pb2.PlaybookEditorCell
    streamlit_cell: _cells_pb2.StreamlitCell
    dashboard_cell: _cells_pb2.DashboardCell
    google_drive_content_cell: _cells_pb2.GoogleDriveContentCell
    google_drive_search_cell: _cells_pb2.GoogleDriveSearchCell
    powerbi_cell: _cells_pb2.PowerBICell
    powerbi_dax_cell: _cells_pb2.PowerBIDAXCell
    form_editor_cell: _cells_pb2.FormEditorCell
    tableau_search_fields_cell: _cells_pb2.TableauSearchFieldsCell
    report_history_cell: _cells_pb2.ReportHistoryCell
    microsoft365_email_search_cell: _cells_pb2.Microsoft365EmailSearchCell
    microsoft365_email_content_cell: _cells_pb2.Microsoft365EmailContentCell
    microsoft365_calendar_cell: _cells_pb2.Microsoft365CalendarCell
    feed_explorer_cell: _cells_pb2.FeedExplorerCell
    bash_cell: _cells_pb2.BashCell
    javascript_cell: _cells_pb2.JavaScriptCell
    feed_post_cell: _cells_pb2.FeedPostCell
    feed_comment_cell: _cells_pb2.FeedCommentCell
    feed_engage_cell: _cells_pb2.FeedEngageCell
    ontology_search_metrics_cell: _cells_pb2.OntologySearchMetricsCell
    ontology_open_object_cell: _cells_pb2.OntologyOpenObjectCell
    compaction_cell: _cells_pb2.CompactionCell
    gmail_email_search_cell: _cells_pb2.GmailEmailSearchCell
    gmail_email_content_cell: _cells_pb2.GmailEmailContentCell
    list_dashboards_cell: _cells_pb2.ListDashboardsCell
    list_users_cell: _cells_pb2.ListUsersCell
    google_calendar_search_cell: _cells_pb2.GoogleCalendarSearchCell
    feed_create_cell: _cells_pb2.FeedCreateCell
    ontology_query_cell: _cells_pb2.OntologyQueryCell
    email_cell: _cells_pb2.EmailCell
    patch_cell: _cells_pb2.PatchCell
    linkedin_search_cell: _cells_pb2.LinkedinSearchCell
    use_skill_cell: _cells_pb2.UseSkillCell
    form_cell: _cells_pb2.FormCell
    connectors_cell: _cells_pb2.ConnectorsCell
    questions_cell: _cells_pb2.QuestionsCell
    app_cell: _cells_pb2.AppCell
    list_apps_cell: _cells_pb2.ListAppsCell
    thinking_cell: _cells_pb2.ThinkingCell
    tool_summary: str
    duration_ms: int

    def __init__(self, id: _Optional[str]=..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., complete: bool=..., generated: bool=..., lifecycle: _Optional[_Union[CellLifecycle, str]]=..., tool_call_id: _Optional[str]=..., exec_error: _Optional[str]=..., sender_member_id: _Optional[str]=..., md_cell: _Optional[_Union[_cells_pb2.MarkdownCell, _Mapping]]=..., py_cell: _Optional[_Union[_cells_pb2.PythonCell, _Mapping]]=..., sql_cell: _Optional[_Union[_cells_pb2.SQLCell, _Mapping]]=..., ans_cell: _Optional[_Union[_cells_pb2.AnswerCell, _Mapping]]=..., document_cell: _Optional[_Union[_cells_pb2.DocumentCell, _Mapping]]=..., ws_cell: _Optional[_Union[_cells_pb2.WebSearchCell, _Mapping]]=..., report_cell: _Optional[_Union[_cells_pb2.ReportCell, _Mapping]]=..., tabular_file_cell: _Optional[_Union[_cells_pb2.TabularFileCell, _Mapping]]=..., status_cell: _Optional[_Union[_cells_pb2.StatusCell, _Mapping]]=..., metrics_cell: _Optional[_Union[_cells_pb2.MetricsCell, _Mapping]]=..., summary_cell: _Optional[_Union[_cells_pb2.SummaryCell, _Mapping]]=..., tableau_cell: _Optional[_Union[_cells_pb2.TableauCell, _Mapping]]=..., tableau_sql_cell: _Optional[_Union[_cells_pb2.TableauSQLCell, _Mapping]]=..., context_prompt_editor_cell: _Optional[_Union[_cells_pb2.ContextPromptEditorCell, _Mapping]]=..., ontology_editor_cell: _Optional[_Union[_cells_pb2.OntologyEditorCell, _Mapping]]=..., image_cell: _Optional[_Union[_cells_pb2.ImageCell, _Mapping]]=..., text_cell: _Optional[_Union[_cells_pb2.TextCell, _Mapping]]=..., mcp_tool_cell: _Optional[_Union[_cells_pb2.MCPToolCell, _Mapping]]=..., preview_cell: _Optional[_Union[_cells_pb2.PreviewCell, _Mapping]]=..., playbook_editor_cell: _Optional[_Union[_cells_pb2.PlaybookEditorCell, _Mapping]]=..., streamlit_cell: _Optional[_Union[_cells_pb2.StreamlitCell, _Mapping]]=..., dashboard_cell: _Optional[_Union[_cells_pb2.DashboardCell, _Mapping]]=..., google_drive_content_cell: _Optional[_Union[_cells_pb2.GoogleDriveContentCell, _Mapping]]=..., google_drive_search_cell: _Optional[_Union[_cells_pb2.GoogleDriveSearchCell, _Mapping]]=..., powerbi_cell: _Optional[_Union[_cells_pb2.PowerBICell, _Mapping]]=..., powerbi_dax_cell: _Optional[_Union[_cells_pb2.PowerBIDAXCell, _Mapping]]=..., form_editor_cell: _Optional[_Union[_cells_pb2.FormEditorCell, _Mapping]]=..., tableau_search_fields_cell: _Optional[_Union[_cells_pb2.TableauSearchFieldsCell, _Mapping]]=..., report_history_cell: _Optional[_Union[_cells_pb2.ReportHistoryCell, _Mapping]]=..., microsoft365_email_search_cell: _Optional[_Union[_cells_pb2.Microsoft365EmailSearchCell, _Mapping]]=..., microsoft365_email_content_cell: _Optional[_Union[_cells_pb2.Microsoft365EmailContentCell, _Mapping]]=..., microsoft365_calendar_cell: _Optional[_Union[_cells_pb2.Microsoft365CalendarCell, _Mapping]]=..., feed_explorer_cell: _Optional[_Union[_cells_pb2.FeedExplorerCell, _Mapping]]=..., bash_cell: _Optional[_Union[_cells_pb2.BashCell, _Mapping]]=..., javascript_cell: _Optional[_Union[_cells_pb2.JavaScriptCell, _Mapping]]=..., feed_post_cell: _Optional[_Union[_cells_pb2.FeedPostCell, _Mapping]]=..., feed_comment_cell: _Optional[_Union[_cells_pb2.FeedCommentCell, _Mapping]]=..., feed_engage_cell: _Optional[_Union[_cells_pb2.FeedEngageCell, _Mapping]]=..., ontology_search_metrics_cell: _Optional[_Union[_cells_pb2.OntologySearchMetricsCell, _Mapping]]=..., ontology_open_object_cell: _Optional[_Union[_cells_pb2.OntologyOpenObjectCell, _Mapping]]=..., compaction_cell: _Optional[_Union[_cells_pb2.CompactionCell, _Mapping]]=..., gmail_email_search_cell: _Optional[_Union[_cells_pb2.GmailEmailSearchCell, _Mapping]]=..., gmail_email_content_cell: _Optional[_Union[_cells_pb2.GmailEmailContentCell, _Mapping]]=..., list_dashboards_cell: _Optional[_Union[_cells_pb2.ListDashboardsCell, _Mapping]]=..., list_users_cell: _Optional[_Union[_cells_pb2.ListUsersCell, _Mapping]]=..., google_calendar_search_cell: _Optional[_Union[_cells_pb2.GoogleCalendarSearchCell, _Mapping]]=..., feed_create_cell: _Optional[_Union[_cells_pb2.FeedCreateCell, _Mapping]]=..., ontology_query_cell: _Optional[_Union[_cells_pb2.OntologyQueryCell, _Mapping]]=..., email_cell: _Optional[_Union[_cells_pb2.EmailCell, _Mapping]]=..., patch_cell: _Optional[_Union[_cells_pb2.PatchCell, _Mapping]]=..., linkedin_search_cell: _Optional[_Union[_cells_pb2.LinkedinSearchCell, _Mapping]]=..., use_skill_cell: _Optional[_Union[_cells_pb2.UseSkillCell, _Mapping]]=..., form_cell: _Optional[_Union[_cells_pb2.FormCell, _Mapping]]=..., connectors_cell: _Optional[_Union[_cells_pb2.ConnectorsCell, _Mapping]]=..., questions_cell: _Optional[_Union[_cells_pb2.QuestionsCell, _Mapping]]=..., app_cell: _Optional[_Union[_cells_pb2.AppCell, _Mapping]]=..., list_apps_cell: _Optional[_Union[_cells_pb2.ListAppsCell, _Mapping]]=..., thinking_cell: _Optional[_Union[_cells_pb2.ThinkingCell, _Mapping]]=..., tool_summary: _Optional[str]=..., duration_ms: _Optional[int]=...) -> None:
        ...

class LlmCompletionParameters(_message.Message):
    __slots__ = ('started_at', 'completed_at', 'member_id', 'llm_model', 'llm_provider', 'system_messages', 'messages', 'tools', 'tool_choice', 'thinking', 'max_tokens', 'temperature', 'stop_sequences', 'service_tier', 'custom_settings')
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    LLM_MODEL_FIELD_NUMBER: _ClassVar[int]
    LLM_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    TOOL_CHOICE_FIELD_NUMBER: _ClassVar[int]
    THINKING_FIELD_NUMBER: _ClassVar[int]
    MAX_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    STOP_SEQUENCES_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TIER_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    started_at: _timestamp_pb2.Timestamp
    completed_at: _timestamp_pb2.Timestamp
    member_id: str
    llm_model: str
    llm_provider: str
    system_messages: _containers.RepeatedScalarFieldContainer[str]
    messages: _containers.RepeatedScalarFieldContainer[str]
    tools: _containers.RepeatedScalarFieldContainer[str]
    tool_choice: str
    thinking: str
    max_tokens: int
    temperature: float
    stop_sequences: _containers.RepeatedScalarFieldContainer[str]
    service_tier: str
    custom_settings: str

    def __init__(self, started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., completed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., member_id: _Optional[str]=..., llm_model: _Optional[str]=..., llm_provider: _Optional[str]=..., system_messages: _Optional[_Iterable[str]]=..., messages: _Optional[_Iterable[str]]=..., tools: _Optional[_Iterable[str]]=..., tool_choice: _Optional[str]=..., thinking: _Optional[str]=..., max_tokens: _Optional[int]=..., temperature: _Optional[float]=..., stop_sequences: _Optional[_Iterable[str]]=..., service_tier: _Optional[str]=..., custom_settings: _Optional[str]=...) -> None:
        ...

class CreateRequest(_message.Message):
    __slots__ = ('paradigm', 'model', 'message', 'playbook_id', 'research', 'dashboard_mode', 'methodology', 'vllm_model_id', 'fast_mode', 'max_thinking')
    PARADIGM_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    RESEARCH_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_MODE_FIELD_NUMBER: _ClassVar[int]
    METHODOLOGY_FIELD_NUMBER: _ClassVar[int]
    VLLM_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    FAST_MODE_FIELD_NUMBER: _ClassVar[int]
    MAX_THINKING_FIELD_NUMBER: _ClassVar[int]
    paradigm: _paradigm_pb2.Paradigm
    model: _llm_model_pb2.LlmModel
    message: str
    playbook_id: str
    research: bool
    dashboard_mode: bool
    methodology: Methodology
    vllm_model_id: str
    fast_mode: bool
    max_thinking: bool

    def __init__(self, paradigm: _Optional[_Union[_paradigm_pb2.Paradigm, _Mapping]]=..., model: _Optional[_Union[_llm_model_pb2.LlmModel, str]]=..., message: _Optional[str]=..., playbook_id: _Optional[str]=..., research: bool=..., dashboard_mode: bool=..., methodology: _Optional[_Union[Methodology, str]]=..., vllm_model_id: _Optional[str]=..., fast_mode: bool=..., max_thinking: bool=...) -> None:
        ...

class CreateResponse(_message.Message):
    __slots__ = ('chat',)
    CHAT_FIELD_NUMBER: _ClassVar[int]
    chat: Chat

    def __init__(self, chat: _Optional[_Union[Chat, _Mapping]]=...) -> None:
        ...

class UpdateChatRequest(_message.Message):
    __slots__ = ('chat_id', 'research', 'summary', 'dashboard_mode', 'methodology', 'fast_mode', 'max_thinking')
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    RESEARCH_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_MODE_FIELD_NUMBER: _ClassVar[int]
    METHODOLOGY_FIELD_NUMBER: _ClassVar[int]
    FAST_MODE_FIELD_NUMBER: _ClassVar[int]
    MAX_THINKING_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    research: bool
    summary: str
    dashboard_mode: bool
    methodology: Methodology
    fast_mode: bool
    max_thinking: bool

    def __init__(self, chat_id: _Optional[str]=..., research: bool=..., summary: _Optional[str]=..., dashboard_mode: bool=..., methodology: _Optional[_Union[Methodology, str]]=..., fast_mode: bool=..., max_thinking: bool=...) -> None:
        ...

class UpdateChatResponse(_message.Message):
    __slots__ = ('chat',)
    CHAT_FIELD_NUMBER: _ClassVar[int]
    chat: Chat

    def __init__(self, chat: _Optional[_Union[Chat, _Mapping]]=...) -> None:
        ...

class DeleteChatRequest(_message.Message):
    __slots__ = ('chat_id',)
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str

    def __init__(self, chat_id: _Optional[str]=...) -> None:
        ...

class RunChatRequest(_message.Message):
    __slots__ = ('chat_id', 'latest_complete_cell_id', 'research', 'model', 'fast_mode', 'max_thinking')
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    LATEST_COMPLETE_CELL_ID_FIELD_NUMBER: _ClassVar[int]
    RESEARCH_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    FAST_MODE_FIELD_NUMBER: _ClassVar[int]
    MAX_THINKING_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    latest_complete_cell_id: str
    research: bool
    model: _llm_model_pb2.LlmModel
    fast_mode: bool
    max_thinking: bool

    def __init__(self, chat_id: _Optional[str]=..., latest_complete_cell_id: _Optional[str]=..., research: bool=..., model: _Optional[_Union[_llm_model_pb2.LlmModel, str]]=..., fast_mode: bool=..., max_thinking: bool=...) -> None:
        ...

class RunChatResponse(_message.Message):
    __slots__ = ('cells',)
    CELLS_FIELD_NUMBER: _ClassVar[int]
    cells: _containers.RepeatedCompositeFieldContainer[Cell]

    def __init__(self, cells: _Optional[_Iterable[_Union[Cell, _Mapping]]]=...) -> None:
        ...

class CancelStreamRequest(_message.Message):
    __slots__ = ('chat_id',)
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str

    def __init__(self, chat_id: _Optional[str]=...) -> None:
        ...

class CancelStreamResponse(_message.Message):
    __slots__ = ('exists',)
    EXISTS_FIELD_NUMBER: _ClassVar[int]
    exists: bool

    def __init__(self, exists: bool=...) -> None:
        ...

class RateChatCellRequest(_message.Message):
    __slots__ = ('chat_id', 'cell_id', 'rating', 'reason')
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    cell_id: str
    rating: CellRating
    reason: str

    def __init__(self, chat_id: _Optional[str]=..., cell_id: _Optional[str]=..., rating: _Optional[_Union[CellRating, str]]=..., reason: _Optional[str]=...) -> None:
        ...

class SendRequest(_message.Message):
    __slots__ = ('chat_id', 'message', 'image_urls', 'message_id', 'steering')
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URLS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    STEERING_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    message: str
    image_urls: _containers.RepeatedScalarFieldContainer[str]
    message_id: str
    steering: bool

    def __init__(self, chat_id: _Optional[str]=..., message: _Optional[str]=..., image_urls: _Optional[_Iterable[str]]=..., message_id: _Optional[str]=..., steering: bool=...) -> None:
        ...

class SendResponse(_message.Message):
    __slots__ = ('cell_id',)
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    cell_id: str

    def __init__(self, cell_id: _Optional[str]=...) -> None:
        ...

class WatchChatRequest(_message.Message):
    __slots__ = ('chat_id', 'latest_complete_cell_id', 'resume_cursor')
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    LATEST_COMPLETE_CELL_ID_FIELD_NUMBER: _ClassVar[int]
    RESUME_CURSOR_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    latest_complete_cell_id: str
    resume_cursor: str

    def __init__(self, chat_id: _Optional[str]=..., latest_complete_cell_id: _Optional[str]=..., resume_cursor: _Optional[str]=...) -> None:
        ...

class WatchChatEvent(_message.Message):
    __slots__ = ('opened', 'cell', 'run_complete', 'run_error', 'handoff_pending', 'run_started', 'heartbeat', 'cursor')
    OPENED_FIELD_NUMBER: _ClassVar[int]
    CELL_FIELD_NUMBER: _ClassVar[int]
    RUN_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    RUN_ERROR_FIELD_NUMBER: _ClassVar[int]
    HANDOFF_PENDING_FIELD_NUMBER: _ClassVar[int]
    RUN_STARTED_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    opened: WatchOpenedEvent
    cell: Cell
    run_complete: WatchRunCompleteEvent
    run_error: WatchRunErrorEvent
    handoff_pending: WatchHandoffPendingEvent
    run_started: WatchRunStartedEvent
    heartbeat: WatchHeartbeatEvent
    cursor: str

    def __init__(self, opened: _Optional[_Union[WatchOpenedEvent, _Mapping]]=..., cell: _Optional[_Union[Cell, _Mapping]]=..., run_complete: _Optional[_Union[WatchRunCompleteEvent, _Mapping]]=..., run_error: _Optional[_Union[WatchRunErrorEvent, _Mapping]]=..., handoff_pending: _Optional[_Union[WatchHandoffPendingEvent, _Mapping]]=..., run_started: _Optional[_Union[WatchRunStartedEvent, _Mapping]]=..., heartbeat: _Optional[_Union[WatchHeartbeatEvent, _Mapping]]=..., cursor: _Optional[str]=...) -> None:
        ...

class WatchOpenedEvent(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WatchHeartbeatEvent(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WatchRunStartedEvent(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WatchRunCompleteEvent(_message.Message):
    __slots__ = ('final_cell_id',)
    FINAL_CELL_ID_FIELD_NUMBER: _ClassVar[int]
    final_cell_id: str

    def __init__(self, final_cell_id: _Optional[str]=...) -> None:
        ...

class WatchRunErrorEvent(_message.Message):
    __slots__ = ('error', 'code')
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    error: str
    code: str

    def __init__(self, error: _Optional[str]=..., code: _Optional[str]=...) -> None:
        ...

class PollChatEventsRequest(_message.Message):
    __slots__ = ('chat_id', 'resume_cursor', 'min_generation')
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    RESUME_CURSOR_FIELD_NUMBER: _ClassVar[int]
    MIN_GENERATION_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    resume_cursor: str
    min_generation: int

    def __init__(self, chat_id: _Optional[str]=..., resume_cursor: _Optional[str]=..., min_generation: _Optional[int]=...) -> None:
        ...

class PollChatEventsResponse(_message.Message):
    __slots__ = ('events', 'cursor', 'running', 'generation')
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    RUNNING_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[WatchChatEvent]
    cursor: str
    running: bool
    generation: int

    def __init__(self, events: _Optional[_Iterable[_Union[WatchChatEvent, _Mapping]]]=..., cursor: _Optional[str]=..., running: bool=..., generation: _Optional[int]=...) -> None:
        ...

class WatchHandoffPendingEvent(_message.Message):
    __slots__ = ('handoff_marker',)
    HANDOFF_MARKER_FIELD_NUMBER: _ClassVar[int]
    handoff_marker: str

    def __init__(self, handoff_marker: _Optional[str]=...) -> None:
        ...

class AttachDatasetRequest(_message.Message):
    __slots__ = ('chat_id', 'dataset_id')
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    dataset_id: str

    def __init__(self, chat_id: _Optional[str]=..., dataset_id: _Optional[str]=...) -> None:
        ...

class AttachDatasetResponse(_message.Message):
    __slots__ = ('cell', 'dataset')
    CELL_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    cell: Cell
    dataset: _dataset_pb2.Dataset

    def __init__(self, cell: _Optional[_Union[Cell, _Mapping]]=..., dataset: _Optional[_Union[_dataset_pb2.Dataset, _Mapping]]=...) -> None:
        ...

class AttachDashboardRequest(_message.Message):
    __slots__ = ('chat_id', 'dashboard_id')
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    dashboard_id: str

    def __init__(self, chat_id: _Optional[str]=..., dashboard_id: _Optional[str]=...) -> None:
        ...

class AttachDashboardResponse(_message.Message):
    __slots__ = ('cell', 'dashboard')
    CELL_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    cell: Cell
    dashboard: _dashboard_pb2.Dashboard

    def __init__(self, cell: _Optional[_Union[Cell, _Mapping]]=..., dashboard: _Optional[_Union[_dashboard_pb2.Dashboard, _Mapping]]=...) -> None:
        ...

class AttachAppRequest(_message.Message):
    __slots__ = ('chat_id', 'app_id')
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    app_id: str

    def __init__(self, chat_id: _Optional[str]=..., app_id: _Optional[str]=...) -> None:
        ...

class AttachAppResponse(_message.Message):
    __slots__ = ('cell', 'app')
    CELL_FIELD_NUMBER: _ClassVar[int]
    APP_FIELD_NUMBER: _ClassVar[int]
    cell: Cell
    app: _apps_pb2.App

    def __init__(self, cell: _Optional[_Union[Cell, _Mapping]]=..., app: _Optional[_Union[_apps_pb2.App, _Mapping]]=...) -> None:
        ...

class HistoryRequest(_message.Message):
    __slots__ = ('chat_id', 'limit', 'skip')
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    limit: int
    skip: int

    def __init__(self, chat_id: _Optional[str]=..., limit: _Optional[int]=..., skip: _Optional[int]=...) -> None:
        ...

class HistoryResponse(_message.Message):
    __slots__ = ('cells', 'has_more')
    CELLS_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    cells: _containers.RepeatedCompositeFieldContainer[Cell]
    has_more: bool

    def __init__(self, cells: _Optional[_Iterable[_Union[Cell, _Mapping]]]=..., has_more: bool=...) -> None:
        ...

class GetAPIChatAnswerRequest(_message.Message):
    __slots__ = ('chat_id',)
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str

    def __init__(self, chat_id: _Optional[str]=...) -> None:
        ...

class GetAPIChatAnswerResponse(_message.Message):
    __slots__ = ('answer', 'complete', 'error')
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    answer: str
    complete: bool
    error: str

    def __init__(self, answer: _Optional[str]=..., complete: bool=..., error: _Optional[str]=...) -> None:
        ...

class GetChatsRequest(_message.Message):
    __slots__ = ('member_only', 'search_term', 'limit', 'offset', 'creator_member_id', 'sort_by', 'sort_direction', 'bookmarked_only', 'created_after', 'created_before', 'exclude_batch_runs', 'exclude_unused_playbooks', 'source', 'has_thread_warning', 'creator_member_ids', 'shared_with_me', 'exclude_feed', 'sources', 'thread_warning_types', 'topic_ids', 'connector_ids')
    MEMBER_ONLY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_TERM_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    CREATOR_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    SORT_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    BOOKMARKED_ONLY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AFTER_FIELD_NUMBER: _ClassVar[int]
    CREATED_BEFORE_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_BATCH_RUNS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_UNUSED_PLAYBOOKS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    HAS_THREAD_WARNING_FIELD_NUMBER: _ClassVar[int]
    CREATOR_MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    SHARED_WITH_ME_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_FEED_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    THREAD_WARNING_TYPES_FIELD_NUMBER: _ClassVar[int]
    TOPIC_IDS_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_IDS_FIELD_NUMBER: _ClassVar[int]
    member_only: bool
    search_term: str
    limit: int
    offset: int
    creator_member_id: str
    sort_by: ChatSortField
    sort_direction: ChatSortDirection
    bookmarked_only: bool
    created_after: _timestamp_pb2.Timestamp
    created_before: _timestamp_pb2.Timestamp
    exclude_batch_runs: bool
    exclude_unused_playbooks: bool
    source: ChatSource
    has_thread_warning: bool
    creator_member_ids: _containers.RepeatedScalarFieldContainer[str]
    shared_with_me: bool
    exclude_feed: bool
    sources: _containers.RepeatedScalarFieldContainer[ChatSource]
    thread_warning_types: _containers.RepeatedScalarFieldContainer[_warnings_pb2.ThreadWarningType]
    topic_ids: _containers.RepeatedScalarFieldContainer[str]
    connector_ids: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, member_only: bool=..., search_term: _Optional[str]=..., limit: _Optional[int]=..., offset: _Optional[int]=..., creator_member_id: _Optional[str]=..., sort_by: _Optional[_Union[ChatSortField, str]]=..., sort_direction: _Optional[_Union[ChatSortDirection, str]]=..., bookmarked_only: bool=..., created_after: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., created_before: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., exclude_batch_runs: bool=..., exclude_unused_playbooks: bool=..., source: _Optional[_Union[ChatSource, str]]=..., has_thread_warning: bool=..., creator_member_ids: _Optional[_Iterable[str]]=..., shared_with_me: bool=..., exclude_feed: bool=..., sources: _Optional[_Iterable[_Union[ChatSource, str]]]=..., thread_warning_types: _Optional[_Iterable[_Union[_warnings_pb2.ThreadWarningType, str]]]=..., topic_ids: _Optional[_Iterable[str]]=..., connector_ids: _Optional[_Iterable[int]]=...) -> None:
        ...

class GetChatsResponse(_message.Message):
    __slots__ = ('chats', 'total_count')
    CHATS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    chats: _containers.RepeatedCompositeFieldContainer[Chat]
    total_count: int

    def __init__(self, chats: _Optional[_Iterable[_Union[Chat, _Mapping]]]=..., total_count: _Optional[int]=...) -> None:
        ...

class GetChatRequest(_message.Message):
    __slots__ = ('chat_id',)
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str

    def __init__(self, chat_id: _Optional[str]=...) -> None:
        ...

class ChatMessage(_message.Message):
    __slots__ = ('role', 'content', 'created_at')
    ROLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    role: str
    content: str
    created_at: _timestamp_pb2.Timestamp

    def __init__(self, role: _Optional[str]=..., content: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GetChatResponse(_message.Message):
    __slots__ = ('chat', 'messages', 'assets')
    CHAT_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    chat: Chat
    messages: _containers.RepeatedCompositeFieldContainer[ChatMessage]
    assets: _containers.RepeatedCompositeFieldContainer[_cells_pb2.PreviewCell]

    def __init__(self, chat: _Optional[_Union[Chat, _Mapping]]=..., messages: _Optional[_Iterable[_Union[ChatMessage, _Mapping]]]=..., assets: _Optional[_Iterable[_Union[_cells_pb2.PreviewCell, _Mapping]]]=...) -> None:
        ...

class DuplicateChatRequest(_message.Message):
    __slots__ = ('chat_id', 'only_if_different_owner')
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    ONLY_IF_DIFFERENT_OWNER_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    only_if_different_owner: bool

    def __init__(self, chat_id: _Optional[str]=..., only_if_different_owner: bool=...) -> None:
        ...

class DuplicateChatResponse(_message.Message):
    __slots__ = ('chat',)
    CHAT_FIELD_NUMBER: _ClassVar[int]
    chat: Chat

    def __init__(self, chat: _Optional[_Union[Chat, _Mapping]]=...) -> None:
        ...

class GetPlaybookChatsRequest(_message.Message):
    __slots__ = ('playbook_id', 'limit', 'skip')
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str
    limit: int
    skip: int

    def __init__(self, playbook_id: _Optional[str]=..., limit: _Optional[int]=..., skip: _Optional[int]=...) -> None:
        ...

class GetPlaybookChatsResponse(_message.Message):
    __slots__ = ('chats',)
    CHATS_FIELD_NUMBER: _ClassVar[int]
    chats: _containers.RepeatedCompositeFieldContainer[Chat]

    def __init__(self, chats: _Optional[_Iterable[_Union[Chat, _Mapping]]]=...) -> None:
        ...

class GetCompletionParametersRequest(_message.Message):
    __slots__ = ('chat_id', 'cell_id')
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    cell_id: str

    def __init__(self, chat_id: _Optional[str]=..., cell_id: _Optional[str]=...) -> None:
        ...

class CheckChatPermissionsRequest(_message.Message):
    __slots__ = ('chat_id',)
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str

    def __init__(self, chat_id: _Optional[str]=...) -> None:
        ...

class CheckChatPermissionsResponse(_message.Message):
    __slots__ = ('has_write_permission', 'has_read_permission', 'connector_id', 'ontology_id', 'connector_ids', 'ontology_ids')
    HAS_WRITE_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    HAS_READ_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    ONTOLOGY_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_IDS_FIELD_NUMBER: _ClassVar[int]
    ONTOLOGY_IDS_FIELD_NUMBER: _ClassVar[int]
    has_write_permission: bool
    has_read_permission: bool
    connector_id: int
    ontology_id: int
    connector_ids: _containers.RepeatedScalarFieldContainer[int]
    ontology_ids: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, has_write_permission: bool=..., has_read_permission: bool=..., connector_id: _Optional[int]=..., ontology_id: _Optional[int]=..., connector_ids: _Optional[_Iterable[int]]=..., ontology_ids: _Optional[_Iterable[int]]=...) -> None:
        ...

class GetCompletionParametersResponse(_message.Message):
    __slots__ = ('params',)
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: LlmCompletionParameters

    def __init__(self, params: _Optional[_Union[LlmCompletionParameters, _Mapping]]=...) -> None:
        ...

class GetCompletionParametersBatchRequest(_message.Message):
    __slots__ = ('chat_id', 'cell_ids')
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    CELL_IDS_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    cell_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, chat_id: _Optional[str]=..., cell_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetCompletionParametersBatchResponse(_message.Message):
    __slots__ = ('params_by_cell_id',)

    class ParamsByCellIdEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: LlmCompletionParameters

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[LlmCompletionParameters, _Mapping]]=...) -> None:
            ...
    PARAMS_BY_CELL_ID_FIELD_NUMBER: _ClassVar[int]
    params_by_cell_id: _containers.MessageMap[str, LlmCompletionParameters]

    def __init__(self, params_by_cell_id: _Optional[_Mapping[str, LlmCompletionParameters]]=...) -> None:
        ...

class ChatExecutionTiming(_message.Message):
    __slots__ = ('cell_type', 'cell_count', 'total_ms', 'warehouse_ms', 'egress_ms', 'overhead_ms')
    CELL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MS_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_MS_FIELD_NUMBER: _ClassVar[int]
    EGRESS_MS_FIELD_NUMBER: _ClassVar[int]
    OVERHEAD_MS_FIELD_NUMBER: _ClassVar[int]
    cell_type: str
    cell_count: int
    total_ms: int
    warehouse_ms: int
    egress_ms: int
    overhead_ms: int

    def __init__(self, cell_type: _Optional[str]=..., cell_count: _Optional[int]=..., total_ms: _Optional[int]=..., warehouse_ms: _Optional[int]=..., egress_ms: _Optional[int]=..., overhead_ms: _Optional[int]=...) -> None:
        ...

class GetChatExecutionTimingRequest(_message.Message):
    __slots__ = ('chat_id',)
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str

    def __init__(self, chat_id: _Optional[str]=...) -> None:
        ...

class CellExecutionTiming(_message.Message):
    __slots__ = ('cell_id', 'total_ms', 'warehouse_ms')
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MS_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_MS_FIELD_NUMBER: _ClassVar[int]
    cell_id: str
    total_ms: int
    warehouse_ms: int

    def __init__(self, cell_id: _Optional[str]=..., total_ms: _Optional[int]=..., warehouse_ms: _Optional[int]=...) -> None:
        ...

class GetChatExecutionTimingResponse(_message.Message):
    __slots__ = ('by_type', 'total_execution_ms', 'total_warehouse_ms', 'total_egress_ms', 'total_overhead_ms', 'by_cell', 'sandbox_mount_ms')
    BY_TYPE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_EXECUTION_MS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_WAREHOUSE_MS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_EGRESS_MS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_OVERHEAD_MS_FIELD_NUMBER: _ClassVar[int]
    BY_CELL_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_MOUNT_MS_FIELD_NUMBER: _ClassVar[int]
    by_type: _containers.RepeatedCompositeFieldContainer[ChatExecutionTiming]
    total_execution_ms: int
    total_warehouse_ms: int
    total_egress_ms: int
    total_overhead_ms: int
    by_cell: _containers.RepeatedCompositeFieldContainer[CellExecutionTiming]
    sandbox_mount_ms: int

    def __init__(self, by_type: _Optional[_Iterable[_Union[ChatExecutionTiming, _Mapping]]]=..., total_execution_ms: _Optional[int]=..., total_warehouse_ms: _Optional[int]=..., total_egress_ms: _Optional[int]=..., total_overhead_ms: _Optional[int]=..., by_cell: _Optional[_Iterable[_Union[CellExecutionTiming, _Mapping]]]=..., sandbox_mount_ms: _Optional[int]=...) -> None:
        ...

class CheckHealthRequest(_message.Message):
    __slots__ = ('model', 'functional')
    MODEL_FIELD_NUMBER: _ClassVar[int]
    FUNCTIONAL_FIELD_NUMBER: _ClassVar[int]
    model: _llm_model_pb2.LlmModel
    functional: bool

    def __init__(self, model: _Optional[_Union[_llm_model_pb2.LlmModel, str]]=..., functional: bool=...) -> None:
        ...

class CheckHealthResponse(_message.Message):
    __slots__ = ('llm_status', 'web_status', 'ontology_status', 'valkey_status', 'tableau_status', 'sandbox_status', 'llm_execution_status', 'sandbox_execution_status', 'console_status')
    LLM_STATUS_FIELD_NUMBER: _ClassVar[int]
    WEB_STATUS_FIELD_NUMBER: _ClassVar[int]
    ONTOLOGY_STATUS_FIELD_NUMBER: _ClassVar[int]
    VALKEY_STATUS_FIELD_NUMBER: _ClassVar[int]
    TABLEAU_STATUS_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_STATUS_FIELD_NUMBER: _ClassVar[int]
    LLM_EXECUTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_EXECUTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    CONSOLE_STATUS_FIELD_NUMBER: _ClassVar[int]
    llm_status: HealthStatus
    web_status: HealthStatus
    ontology_status: HealthStatus
    valkey_status: HealthStatus
    tableau_status: HealthStatus
    sandbox_status: HealthStatus
    llm_execution_status: HealthStatus
    sandbox_execution_status: HealthStatus
    console_status: HealthStatus

    def __init__(self, llm_status: _Optional[_Union[HealthStatus, str]]=..., web_status: _Optional[_Union[HealthStatus, str]]=..., ontology_status: _Optional[_Union[HealthStatus, str]]=..., valkey_status: _Optional[_Union[HealthStatus, str]]=..., tableau_status: _Optional[_Union[HealthStatus, str]]=..., sandbox_status: _Optional[_Union[HealthStatus, str]]=..., llm_execution_status: _Optional[_Union[HealthStatus, str]]=..., sandbox_execution_status: _Optional[_Union[HealthStatus, str]]=..., console_status: _Optional[_Union[HealthStatus, str]]=...) -> None:
        ...

class LlmUsage(_message.Message):
    __slots__ = ('input_tokens', 'cache_creation_input_tokens', 'cache_read_input_tokens', 'output_tokens', 'model_name', 'timestamp')
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_CREATION_INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_READ_INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    input_tokens: int
    cache_creation_input_tokens: int
    cache_read_input_tokens: int
    output_tokens: int
    model_name: str
    timestamp: _timestamp_pb2.Timestamp

    def __init__(self, input_tokens: _Optional[int]=..., cache_creation_input_tokens: _Optional[int]=..., cache_read_input_tokens: _Optional[int]=..., output_tokens: _Optional[int]=..., model_name: _Optional[str]=..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GetLlmUsageRequest(_message.Message):
    __slots__ = ('chat_id', 'include_costs')
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_COSTS_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    include_costs: bool

    def __init__(self, chat_id: _Optional[str]=..., include_costs: bool=...) -> None:
        ...

class GetLlmUsageResponse(_message.Message):
    __slots__ = ('usage', 'context_window_used', 'estimated_cost', 'estimated_compute_cost', 'sandbox_id', 'estimated_compute_acus', 'estimated_llm_acus')
    USAGE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_WINDOW_USED_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_COST_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_COMPUTE_COST_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_ID_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_COMPUTE_ACUS_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_LLM_ACUS_FIELD_NUMBER: _ClassVar[int]
    usage: _containers.RepeatedCompositeFieldContainer[LlmUsage]
    context_window_used: float
    estimated_cost: float
    estimated_compute_cost: float
    sandbox_id: str
    estimated_compute_acus: float
    estimated_llm_acus: float

    def __init__(self, usage: _Optional[_Iterable[_Union[LlmUsage, _Mapping]]]=..., context_window_used: _Optional[float]=..., estimated_cost: _Optional[float]=..., estimated_compute_cost: _Optional[float]=..., sandbox_id: _Optional[str]=..., estimated_compute_acus: _Optional[float]=..., estimated_llm_acus: _Optional[float]=...) -> None:
        ...

class ApproveContextPromptChangeRequest(_message.Message):
    __slots__ = ('cell_id', 'edited_context')
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    EDITED_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    cell_id: str
    edited_context: str

    def __init__(self, cell_id: _Optional[str]=..., edited_context: _Optional[str]=...) -> None:
        ...

class ApproveContextPromptChangeResponse(_message.Message):
    __slots__ = ('success', 'message', 'status', 'resumed', 'resume_error')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RESUMED_FIELD_NUMBER: _ClassVar[int]
    RESUME_ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    status: _cells_pb2.ContextPromptChangeStatus
    resumed: bool
    resume_error: str

    def __init__(self, success: bool=..., message: _Optional[str]=..., status: _Optional[_Union[_cells_pb2.ContextPromptChangeStatus, str]]=..., resumed: bool=..., resume_error: _Optional[str]=...) -> None:
        ...

class RejectContextPromptChangeRequest(_message.Message):
    __slots__ = ('cell_id',)
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    cell_id: str

    def __init__(self, cell_id: _Optional[str]=...) -> None:
        ...

class RejectContextPromptChangeResponse(_message.Message):
    __slots__ = ('success', 'message', 'status', 'resumed', 'resume_error')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RESUMED_FIELD_NUMBER: _ClassVar[int]
    RESUME_ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    status: _cells_pb2.ContextPromptChangeStatus
    resumed: bool
    resume_error: str

    def __init__(self, success: bool=..., message: _Optional[str]=..., status: _Optional[_Union[_cells_pb2.ContextPromptChangeStatus, str]]=..., resumed: bool=..., resume_error: _Optional[str]=...) -> None:
        ...

class SubmitContextPromptChangeRequest(_message.Message):
    __slots__ = ('cell_id', 'edited_context')
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    EDITED_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    cell_id: str
    edited_context: str

    def __init__(self, cell_id: _Optional[str]=..., edited_context: _Optional[str]=...) -> None:
        ...

class SubmitContextPromptChangeResponse(_message.Message):
    __slots__ = ('success', 'message', 'status', 'resumed', 'resume_error')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RESUMED_FIELD_NUMBER: _ClassVar[int]
    RESUME_ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    status: _cells_pb2.ContextPromptChangeStatus
    resumed: bool
    resume_error: str

    def __init__(self, success: bool=..., message: _Optional[str]=..., status: _Optional[_Union[_cells_pb2.ContextPromptChangeStatus, str]]=..., resumed: bool=..., resume_error: _Optional[str]=...) -> None:
        ...

class SubmitQuestionsRequest(_message.Message):
    __slots__ = ('cell_id', 'answers')
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    ANSWERS_FIELD_NUMBER: _ClassVar[int]
    cell_id: str
    answers: _containers.RepeatedCompositeFieldContainer[_cells_pb2.QuestionAnswer]

    def __init__(self, cell_id: _Optional[str]=..., answers: _Optional[_Iterable[_Union[_cells_pb2.QuestionAnswer, _Mapping]]]=...) -> None:
        ...

class SubmitQuestionsResponse(_message.Message):
    __slots__ = ('success', 'status', 'resumed', 'resume_error')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RESUMED_FIELD_NUMBER: _ClassVar[int]
    RESUME_ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    status: _cells_pb2.QuestionsStatus
    resumed: bool
    resume_error: str

    def __init__(self, success: bool=..., status: _Optional[_Union[_cells_pb2.QuestionsStatus, str]]=..., resumed: bool=..., resume_error: _Optional[str]=...) -> None:
        ...

class DismissQuestionsRequest(_message.Message):
    __slots__ = ('cell_id', 'answers')
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    ANSWERS_FIELD_NUMBER: _ClassVar[int]
    cell_id: str
    answers: _containers.RepeatedCompositeFieldContainer[_cells_pb2.QuestionAnswer]

    def __init__(self, cell_id: _Optional[str]=..., answers: _Optional[_Iterable[_Union[_cells_pb2.QuestionAnswer, _Mapping]]]=...) -> None:
        ...

class DismissQuestionsResponse(_message.Message):
    __slots__ = ('success', 'status')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    status: _cells_pb2.QuestionsStatus

    def __init__(self, success: bool=..., status: _Optional[_Union[_cells_pb2.QuestionsStatus, str]]=...) -> None:
        ...

class SubmitFormApprovalRequest(_message.Message):
    __slots__ = ('cell_id',)
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    cell_id: str

    def __init__(self, cell_id: _Optional[str]=...) -> None:
        ...

class SubmitFormApprovalResponse(_message.Message):
    __slots__ = ('success', 'outcome', 'error', 'resumed', 'resume_error')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESUMED_FIELD_NUMBER: _ClassVar[int]
    RESUME_ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    outcome: str
    error: str
    resumed: bool
    resume_error: str

    def __init__(self, success: bool=..., outcome: _Optional[str]=..., error: _Optional[str]=..., resumed: bool=..., resume_error: _Optional[str]=...) -> None:
        ...

class RejectFormApprovalRequest(_message.Message):
    __slots__ = ('cell_id',)
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    cell_id: str

    def __init__(self, cell_id: _Optional[str]=...) -> None:
        ...

class RejectFormApprovalResponse(_message.Message):
    __slots__ = ('success', 'resumed', 'resume_error')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    RESUMED_FIELD_NUMBER: _ClassVar[int]
    RESUME_ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    resumed: bool
    resume_error: str

    def __init__(self, success: bool=..., resumed: bool=..., resume_error: _Optional[str]=...) -> None:
        ...

class DismissFormApprovalRequest(_message.Message):
    __slots__ = ('cell_id',)
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    cell_id: str

    def __init__(self, cell_id: _Optional[str]=...) -> None:
        ...

class DismissFormApprovalResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class GetCellAuthStatusRequest(_message.Message):
    __slots__ = ('cell_id', 'chat_id')
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    cell_id: str
    chat_id: str

    def __init__(self, cell_id: _Optional[str]=..., chat_id: _Optional[str]=...) -> None:
        ...

class GetCellAuthStatusResponse(_message.Message):
    __slots__ = ('lifecycle', 'can_continue')
    LIFECYCLE_FIELD_NUMBER: _ClassVar[int]
    CAN_CONTINUE_FIELD_NUMBER: _ClassVar[int]
    lifecycle: CellLifecycle
    can_continue: bool

    def __init__(self, lifecycle: _Optional[_Union[CellLifecycle, str]]=..., can_continue: bool=...) -> None:
        ...

class GrantSandboxOAuthPermissionRequest(_message.Message):
    __slots__ = ('cell_id', 'api_access_key_id')
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    API_ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    cell_id: str
    api_access_key_id: str

    def __init__(self, cell_id: _Optional[str]=..., api_access_key_id: _Optional[str]=...) -> None:
        ...

class GrantSandboxOAuthPermissionResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ResumeChatAfterAuthRequest(_message.Message):
    __slots__ = ('cell_id',)
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    cell_id: str

    def __init__(self, cell_id: _Optional[str]=...) -> None:
        ...

class ResumeChatAfterAuthResponse(_message.Message):
    __slots__ = ('success', 'sql_cell', 'python_cell', 'powerbi_dax_cell', 'resumed', 'resume_error')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    SQL_CELL_FIELD_NUMBER: _ClassVar[int]
    PYTHON_CELL_FIELD_NUMBER: _ClassVar[int]
    POWERBI_DAX_CELL_FIELD_NUMBER: _ClassVar[int]
    RESUMED_FIELD_NUMBER: _ClassVar[int]
    RESUME_ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    sql_cell: _cells_pb2.SQLCell
    python_cell: _cells_pb2.PythonCell
    powerbi_dax_cell: _cells_pb2.PowerBIDAXCell
    resumed: bool
    resume_error: str

    def __init__(self, success: bool=..., sql_cell: _Optional[_Union[_cells_pb2.SQLCell, _Mapping]]=..., python_cell: _Optional[_Union[_cells_pb2.PythonCell, _Mapping]]=..., powerbi_dax_cell: _Optional[_Union[_cells_pb2.PowerBIDAXCell, _Mapping]]=..., resumed: bool=..., resume_error: _Optional[str]=...) -> None:
        ...

class ApproveOntologyChangeRequest(_message.Message):
    __slots__ = ('cell_id',)
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    cell_id: str

    def __init__(self, cell_id: _Optional[str]=...) -> None:
        ...

class ApproveOntologyChangeResponse(_message.Message):
    __slots__ = ('success', 'message', 'resumed', 'resume_error')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESUMED_FIELD_NUMBER: _ClassVar[int]
    RESUME_ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    resumed: bool
    resume_error: str

    def __init__(self, success: bool=..., message: _Optional[str]=..., resumed: bool=..., resume_error: _Optional[str]=...) -> None:
        ...

class RejectOntologyChangeRequest(_message.Message):
    __slots__ = ('cell_id',)
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    cell_id: str

    def __init__(self, cell_id: _Optional[str]=...) -> None:
        ...

class RejectOntologyChangeResponse(_message.Message):
    __slots__ = ('success', 'message', 'resumed', 'resume_error')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESUMED_FIELD_NUMBER: _ClassVar[int]
    RESUME_ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    resumed: bool
    resume_error: str

    def __init__(self, success: bool=..., message: _Optional[str]=..., resumed: bool=..., resume_error: _Optional[str]=...) -> None:
        ...

class GetMembersWithChatsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetMembersWithChatsResponse(_message.Message):
    __slots__ = ('members',)
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    members: _containers.RepeatedCompositeFieldContainer[_identity_pb2.MemberPreview]

    def __init__(self, members: _Optional[_Iterable[_Union[_identity_pb2.MemberPreview, _Mapping]]]=...) -> None:
        ...

class CheckStreamlitHealthRequest(_message.Message):
    __slots__ = ('chat_id', 'cell_id')
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    cell_id: str

    def __init__(self, chat_id: _Optional[str]=..., cell_id: _Optional[str]=...) -> None:
        ...

class CheckStreamlitHealthResponse(_message.Message):
    __slots__ = ('status', 'cell', 'embed_url', 'streamlit_url')
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CELL_FIELD_NUMBER: _ClassVar[int]
    EMBED_URL_FIELD_NUMBER: _ClassVar[int]
    STREAMLIT_URL_FIELD_NUMBER: _ClassVar[int]
    status: StreamlitHealthStatus
    cell: Cell
    embed_url: str
    streamlit_url: str

    def __init__(self, status: _Optional[_Union[StreamlitHealthStatus, str]]=..., cell: _Optional[_Union[Cell, _Mapping]]=..., embed_url: _Optional[str]=..., streamlit_url: _Optional[str]=...) -> None:
        ...

class UpdateFormStatusRequest(_message.Message):
    __slots__ = ('form_id', 'status')
    FORM_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    form_id: str
    status: _cells_pb2.EditableFormStatus

    def __init__(self, form_id: _Optional[str]=..., status: _Optional[_Union[_cells_pb2.EditableFormStatus, str]]=...) -> None:
        ...

class UpdateFormStatusResponse(_message.Message):
    __slots__ = ('form',)
    FORM_FIELD_NUMBER: _ClassVar[int]
    form: _cells_pb2.EditableForm

    def __init__(self, form: _Optional[_Union[_cells_pb2.EditableForm, _Mapping]]=...) -> None:
        ...

class UpdateFormFieldsRequest(_message.Message):
    __slots__ = ('form_id', 'fields')
    FORM_ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    form_id: str
    fields: _struct_pb2.Struct

    def __init__(self, form_id: _Optional[str]=..., fields: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...

class UpdateFormFieldsResponse(_message.Message):
    __slots__ = ('form',)
    FORM_FIELD_NUMBER: _ClassVar[int]
    form: _cells_pb2.EditableForm

    def __init__(self, form: _Optional[_Union[_cells_pb2.EditableForm, _Mapping]]=...) -> None:
        ...

class UpdateFormValidationErrorRequest(_message.Message):
    __slots__ = ('form_id', 'validation_error')
    FORM_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    form_id: str
    validation_error: str

    def __init__(self, form_id: _Optional[str]=..., validation_error: _Optional[str]=...) -> None:
        ...

class UpdateFormValidationErrorResponse(_message.Message):
    __slots__ = ('form',)
    FORM_FIELD_NUMBER: _ClassVar[int]
    form: _cells_pb2.EditableForm

    def __init__(self, form: _Optional[_Union[_cells_pb2.EditableForm, _Mapping]]=...) -> None:
        ...

class GetCellRequest(_message.Message):
    __slots__ = ('cell_id',)
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    cell_id: str

    def __init__(self, cell_id: _Optional[str]=...) -> None:
        ...

class GetCellResponse(_message.Message):
    __slots__ = ('cell',)
    CELL_FIELD_NUMBER: _ClassVar[int]
    cell: Cell

    def __init__(self, cell: _Optional[_Union[Cell, _Mapping]]=...) -> None:
        ...

class SetFormSubmitResultRequest(_message.Message):
    __slots__ = ('form_id', 'submit_error', 'submit_result', 'status')
    FORM_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_ERROR_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_RESULT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    form_id: str
    submit_error: str
    submit_result: str
    status: _cells_pb2.EditableFormStatus

    def __init__(self, form_id: _Optional[str]=..., submit_error: _Optional[str]=..., submit_result: _Optional[str]=..., status: _Optional[_Union[_cells_pb2.EditableFormStatus, str]]=...) -> None:
        ...

class SetFormSubmitResultResponse(_message.Message):
    __slots__ = ('form',)
    FORM_FIELD_NUMBER: _ClassVar[int]
    form: _cells_pb2.EditableForm

    def __init__(self, form: _Optional[_Union[_cells_pb2.EditableForm, _Mapping]]=...) -> None:
        ...

class QueryOneShotRequest(_message.Message):
    __slots__ = ('question', 'paradigm', 'model', 'chat_id')
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    PARADIGM_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    question: str
    paradigm: _paradigm_pb2.Paradigm
    model: _llm_model_pb2.LlmModel
    chat_id: str

    def __init__(self, question: _Optional[str]=..., paradigm: _Optional[_Union[_paradigm_pb2.Paradigm, _Mapping]]=..., model: _Optional[_Union[_llm_model_pb2.LlmModel, str]]=..., chat_id: _Optional[str]=...) -> None:
        ...

class QueryOneShotResponse(_message.Message):
    __slots__ = ('chat_id', 'answer', 'cells')
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    CELLS_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    answer: str
    cells: _containers.RepeatedCompositeFieldContainer[Cell]

    def __init__(self, chat_id: _Optional[str]=..., answer: _Optional[str]=..., cells: _Optional[_Iterable[_Union[Cell, _Mapping]]]=...) -> None:
        ...

class BookmarkChatRequest(_message.Message):
    __slots__ = ('chat_id',)
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str

    def __init__(self, chat_id: _Optional[str]=...) -> None:
        ...

class UnbookmarkChatRequest(_message.Message):
    __slots__ = ('chat_id',)
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str

    def __init__(self, chat_id: _Optional[str]=...) -> None:
        ...

class ArtifactSummary(_message.Message):
    __slots__ = ('id', 'name', 'type', 'created_at', 'thumbnail_url')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    type: ArtifactType
    created_at: _timestamp_pb2.Timestamp
    thumbnail_url: str

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., type: _Optional[_Union[ArtifactType, str]]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., thumbnail_url: _Optional[str]=...) -> None:
        ...

class GetChatArtifactsSummaryRequest(_message.Message):
    __slots__ = ('chat_id',)
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str

    def __init__(self, chat_id: _Optional[str]=...) -> None:
        ...

class GetChatArtifactsSummaryResponse(_message.Message):
    __slots__ = ('artifacts',)
    ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    artifacts: _containers.RepeatedCompositeFieldContainer[ArtifactSummary]

    def __init__(self, artifacts: _Optional[_Iterable[_Union[ArtifactSummary, _Mapping]]]=...) -> None:
        ...

class GetArtifactRequest(_message.Message):
    __slots__ = ('artifact_id', 'chat_id')
    ARTIFACT_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    artifact_id: str
    chat_id: str

    def __init__(self, artifact_id: _Optional[str]=..., chat_id: _Optional[str]=...) -> None:
        ...

class GetArtifactResponse(_message.Message):
    __slots__ = ('id', 'name', 'file', 'streamlit', 'dashboard', 'form')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    STREAMLIT_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    FORM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    file: FileArtifactData
    streamlit: StreamlitArtifactData
    dashboard: DashboardArtifactData
    form: FormArtifactData

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., file: _Optional[_Union[FileArtifactData, _Mapping]]=..., streamlit: _Optional[_Union[StreamlitArtifactData, _Mapping]]=..., dashboard: _Optional[_Union[DashboardArtifactData, _Mapping]]=..., form: _Optional[_Union[FormArtifactData, _Mapping]]=...) -> None:
        ...

class FileArtifactData(_message.Message):
    __slots__ = ('url', 'type')
    URL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    url: str
    type: ArtifactType

    def __init__(self, url: _Optional[str]=..., type: _Optional[_Union[ArtifactType, str]]=...) -> None:
        ...

class StreamlitArtifactData(_message.Message):
    __slots__ = ('embed_url',)
    EMBED_URL_FIELD_NUMBER: _ClassVar[int]
    embed_url: str

    def __init__(self, embed_url: _Optional[str]=...) -> None:
        ...

class DashboardArtifactData(_message.Message):
    __slots__ = ('dashboard_id',)
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str

    def __init__(self, dashboard_id: _Optional[str]=...) -> None:
        ...

class FormArtifactData(_message.Message):
    __slots__ = ('form_id',)
    FORM_ID_FIELD_NUMBER: _ClassVar[int]
    form_id: str

    def __init__(self, form_id: _Optional[str]=...) -> None:
        ...

class MarkChatReadRequest(_message.Message):
    __slots__ = ('chat_id',)
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str

    def __init__(self, chat_id: _Optional[str]=...) -> None:
        ...

class MarkChatReadResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MarkChatUnreadRequest(_message.Message):
    __slots__ = ('chat_id',)
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str

    def __init__(self, chat_id: _Optional[str]=...) -> None:
        ...

class MarkChatUnreadResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class EgressCall(_message.Message):
    __slots__ = ('id', 'method', 'scheme', 'host', 'path', 'status_code', 'outcome', 'duration_ms', 'request_bytes', 'response_bytes', 'api_access_key_id', 'occurred_at', 'cell_id', 'interpretation')
    ID_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    SCHEME_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_BYTES_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_BYTES_FIELD_NUMBER: _ClassVar[int]
    API_ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    INTERPRETATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    method: str
    scheme: str
    host: str
    path: str
    status_code: int
    outcome: str
    duration_ms: int
    request_bytes: int
    response_bytes: int
    api_access_key_id: str
    occurred_at: _timestamp_pb2.Timestamp
    cell_id: str
    interpretation: str

    def __init__(self, id: _Optional[str]=..., method: _Optional[str]=..., scheme: _Optional[str]=..., host: _Optional[str]=..., path: _Optional[str]=..., status_code: _Optional[int]=..., outcome: _Optional[str]=..., duration_ms: _Optional[int]=..., request_bytes: _Optional[int]=..., response_bytes: _Optional[int]=..., api_access_key_id: _Optional[str]=..., occurred_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., cell_id: _Optional[str]=..., interpretation: _Optional[str]=...) -> None:
        ...

class EgressSummary(_message.Message):
    __slots__ = ('total_calls', 'outcome_counts', 'calls')

    class OutcomeCountsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int

        def __init__(self, key: _Optional[str]=..., value: _Optional[int]=...) -> None:
            ...
    TOTAL_CALLS_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_COUNTS_FIELD_NUMBER: _ClassVar[int]
    CALLS_FIELD_NUMBER: _ClassVar[int]
    total_calls: int
    outcome_counts: _containers.ScalarMap[str, int]
    calls: _containers.RepeatedCompositeFieldContainer[EgressCall]

    def __init__(self, total_calls: _Optional[int]=..., outcome_counts: _Optional[_Mapping[str, int]]=..., calls: _Optional[_Iterable[_Union[EgressCall, _Mapping]]]=...) -> None:
        ...