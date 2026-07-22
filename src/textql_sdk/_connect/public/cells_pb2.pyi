import datetime
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
import paradigm_params_pb2 as _paradigm_params_pb2
from public import connector_pb2 as _connector_pb2
from public import dashboard_pb2 as _dashboard_pb2
from public import dataframe_pb2 as _dataframe_pb2
from public import dataset_pb2 as _dataset_pb2
from public import llm_model_pb2 as _llm_model_pb2
from public import ontology_pb2 as _ontology_pb2
from public import paradigm_pb2 as _paradigm_pb2
from public import patches_pb2 as _patches_pb2
from public import report_pb2 as _report_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DashboardAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DASHBOARD_ACTION_UNKNOWN: _ClassVar[DashboardAction]
    DASHBOARD_ACTION_CREATE: _ClassVar[DashboardAction]
    DASHBOARD_ACTION_UPDATE: _ClassVar[DashboardAction]
    DASHBOARD_ACTION_PUBLISH: _ClassVar[DashboardAction]

class WebSearchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TYPE_UNKNOWN: _ClassVar[WebSearchType]
    TYPE_RESEARCH: _ClassVar[WebSearchType]
    TYPE_QUESTION: _ClassVar[WebSearchType]
    TYPE_CONTENTS: _ClassVar[WebSearchType]

class DateRange(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RANGE_UNKNOWN: _ClassVar[DateRange]
    RANGE_ALL: _ClassVar[DateRange]
    RANGE_PAST_DAY: _ClassVar[DateRange]
    RANGE_PAST_WEEK: _ClassVar[DateRange]
    RANGE_PAST_MONTH: _ClassVar[DateRange]
    RANGE_PAST_YEAR: _ClassVar[DateRange]

class ContextPromptEditorAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTION_UNKNOWN: _ClassVar[ContextPromptEditorAction]
    ACTION_GET: _ClassVar[ContextPromptEditorAction]
    ACTION_PROPOSE: _ClassVar[ContextPromptEditorAction]
    ACTION_CREATE: _ClassVar[ContextPromptEditorAction]

class ContextPromptChangeStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATUS_UNKNOWN: _ClassVar[ContextPromptChangeStatus]
    STATUS_DRAFT: _ClassVar[ContextPromptChangeStatus]
    STATUS_PENDING: _ClassVar[ContextPromptChangeStatus]
    STATUS_REJECTED: _ClassVar[ContextPromptChangeStatus]
    STATUS_APPLIED: _ClassVar[ContextPromptChangeStatus]

class OntologyEditorAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ONTOLOGY_ACTION_UNKNOWN: _ClassVar[OntologyEditorAction]
    ONTOLOGY_ACTION_LIST: _ClassVar[OntologyEditorAction]
    ONTOLOGY_ACTION_OBJECT: _ClassVar[OntologyEditorAction]
    ONTOLOGY_ACTION_LINK: _ClassVar[OntologyEditorAction]
    ONTOLOGY_ACTION_ATTRIBUTE: _ClassVar[OntologyEditorAction]
    ONTOLOGY_ACTION_METRIC: _ClassVar[OntologyEditorAction]

class OntologyEditorListType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LIST_TYPE_UNKNOWN: _ClassVar[OntologyEditorListType]
    LIST_TYPE_OBJECTS: _ClassVar[OntologyEditorListType]
    LIST_TYPE_LINKS: _ClassVar[OntologyEditorListType]
    LIST_TYPE_ATTRIBUTES: _ClassVar[OntologyEditorListType]
    LIST_TYPE_METRICS: _ClassVar[OntologyEditorListType]

class OntologyEditorOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERATION_UNKNOWN: _ClassVar[OntologyEditorOperation]
    OPERATION_CREATE: _ClassVar[OntologyEditorOperation]
    OPERATION_UPDATE: _ClassVar[OntologyEditorOperation]
    OPERATION_DELETE: _ClassVar[OntologyEditorOperation]

class OntologyEditorStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ONTOLOGY_STATUS_UNKNOWN: _ClassVar[OntologyEditorStatus]
    ONTOLOGY_STATUS_DRAFT: _ClassVar[OntologyEditorStatus]
    ONTOLOGY_STATUS_APPLIED: _ClassVar[OntologyEditorStatus]
    ONTOLOGY_STATUS_REJECTED: _ClassVar[OntologyEditorStatus]
    ONTOLOGY_STATUS_ERROR: _ClassVar[OntologyEditorStatus]

class PlaybookEditorAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PLAYBOOK_ACTION_UNKNOWN: _ClassVar[PlaybookEditorAction]
    PLAYBOOK_ACTION_LIST: _ClassVar[PlaybookEditorAction]
    PLAYBOOK_ACTION_GET: _ClassVar[PlaybookEditorAction]
    PLAYBOOK_ACTION_CREATE: _ClassVar[PlaybookEditorAction]
    PLAYBOOK_ACTION_UPDATE: _ClassVar[PlaybookEditorAction]
    PLAYBOOK_ACTION_RUN: _ClassVar[PlaybookEditorAction]

class FormEditorAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FORM_EDITOR_ACTION_UNKNOWN: _ClassVar[FormEditorAction]
    FORM_EDITOR_ACTION_INFO: _ClassVar[FormEditorAction]
    FORM_EDITOR_ACTION_VIEW: _ClassVar[FormEditorAction]
    FORM_EDITOR_ACTION_CREATE: _ClassVar[FormEditorAction]
    FORM_EDITOR_ACTION_UPDATE: _ClassVar[FormEditorAction]

class EditableFormStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EDITABLE_FORM_STATUS_UNKNOWN: _ClassVar[EditableFormStatus]
    EDITABLE_FORM_STATUS_DRAFT: _ClassVar[EditableFormStatus]
    EDITABLE_FORM_STATUS_MODIFIED: _ClassVar[EditableFormStatus]
    EDITABLE_FORM_STATUS_SUBMITTING: _ClassVar[EditableFormStatus]
    EDITABLE_FORM_STATUS_SUBMITTED: _ClassVar[EditableFormStatus]
    EDITABLE_FORM_STATUS_REJECTED: _ClassVar[EditableFormStatus]

class PlaybookStatusLight(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PLAYBOOK_STATUS_UNKNOWN: _ClassVar[PlaybookStatusLight]
    PLAYBOOK_STATUS_ACTIVE: _ClassVar[PlaybookStatusLight]
    PLAYBOOK_STATUS_INACTIVE: _ClassVar[PlaybookStatusLight]

class PlaybookReportStyleLight(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPORT_STYLE_LIGHT_UNKNOWN: _ClassVar[PlaybookReportStyleLight]
    REPORT_STYLE_LIGHT_EXECUTIVE: _ClassVar[PlaybookReportStyleLight]
    REPORT_STYLE_LIGHT_VERBOSE: _ClassVar[PlaybookReportStyleLight]
    REPORT_STYLE_LIGHT_CONCISE: _ClassVar[PlaybookReportStyleLight]

class FeedAgentAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FEED_AGENT_ACTION_UNKNOWN: _ClassVar[FeedAgentAction]
    FEED_AGENT_ACTION_CREATE: _ClassVar[FeedAgentAction]
    FEED_AGENT_ACTION_UPDATE: _ClassVar[FeedAgentAction]

class QuestionsStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUESTIONS_STATUS_UNKNOWN: _ClassVar[QuestionsStatus]
    QUESTIONS_STATUS_PENDING: _ClassVar[QuestionsStatus]
    QUESTIONS_STATUS_ANSWERED: _ClassVar[QuestionsStatus]
    QUESTIONS_STATUS_DISMISSED: _ClassVar[QuestionsStatus]

class QuestionKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUESTION_KIND_UNKNOWN: _ClassVar[QuestionKind]
    QUESTION_KIND_CHOICE: _ClassVar[QuestionKind]
    QUESTION_KIND_MULTICHOICE: _ClassVar[QuestionKind]
    QUESTION_KIND_INPUTS: _ClassVar[QuestionKind]

class QuestionInputKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUESTION_INPUT_KIND_UNKNOWN: _ClassVar[QuestionInputKind]
    QUESTION_INPUT_KIND_TEXT: _ClassVar[QuestionInputKind]
    QUESTION_INPUT_KIND_FORMFIELD: _ClassVar[QuestionInputKind]
    QUESTION_INPUT_KIND_MULTILINE: _ClassVar[QuestionInputKind]
DASHBOARD_ACTION_UNKNOWN: DashboardAction
DASHBOARD_ACTION_CREATE: DashboardAction
DASHBOARD_ACTION_UPDATE: DashboardAction
DASHBOARD_ACTION_PUBLISH: DashboardAction
TYPE_UNKNOWN: WebSearchType
TYPE_RESEARCH: WebSearchType
TYPE_QUESTION: WebSearchType
TYPE_CONTENTS: WebSearchType
RANGE_UNKNOWN: DateRange
RANGE_ALL: DateRange
RANGE_PAST_DAY: DateRange
RANGE_PAST_WEEK: DateRange
RANGE_PAST_MONTH: DateRange
RANGE_PAST_YEAR: DateRange
ACTION_UNKNOWN: ContextPromptEditorAction
ACTION_GET: ContextPromptEditorAction
ACTION_PROPOSE: ContextPromptEditorAction
ACTION_CREATE: ContextPromptEditorAction
STATUS_UNKNOWN: ContextPromptChangeStatus
STATUS_DRAFT: ContextPromptChangeStatus
STATUS_PENDING: ContextPromptChangeStatus
STATUS_REJECTED: ContextPromptChangeStatus
STATUS_APPLIED: ContextPromptChangeStatus
ONTOLOGY_ACTION_UNKNOWN: OntologyEditorAction
ONTOLOGY_ACTION_LIST: OntologyEditorAction
ONTOLOGY_ACTION_OBJECT: OntologyEditorAction
ONTOLOGY_ACTION_LINK: OntologyEditorAction
ONTOLOGY_ACTION_ATTRIBUTE: OntologyEditorAction
ONTOLOGY_ACTION_METRIC: OntologyEditorAction
LIST_TYPE_UNKNOWN: OntologyEditorListType
LIST_TYPE_OBJECTS: OntologyEditorListType
LIST_TYPE_LINKS: OntologyEditorListType
LIST_TYPE_ATTRIBUTES: OntologyEditorListType
LIST_TYPE_METRICS: OntologyEditorListType
OPERATION_UNKNOWN: OntologyEditorOperation
OPERATION_CREATE: OntologyEditorOperation
OPERATION_UPDATE: OntologyEditorOperation
OPERATION_DELETE: OntologyEditorOperation
ONTOLOGY_STATUS_UNKNOWN: OntologyEditorStatus
ONTOLOGY_STATUS_DRAFT: OntologyEditorStatus
ONTOLOGY_STATUS_APPLIED: OntologyEditorStatus
ONTOLOGY_STATUS_REJECTED: OntologyEditorStatus
ONTOLOGY_STATUS_ERROR: OntologyEditorStatus
PLAYBOOK_ACTION_UNKNOWN: PlaybookEditorAction
PLAYBOOK_ACTION_LIST: PlaybookEditorAction
PLAYBOOK_ACTION_GET: PlaybookEditorAction
PLAYBOOK_ACTION_CREATE: PlaybookEditorAction
PLAYBOOK_ACTION_UPDATE: PlaybookEditorAction
PLAYBOOK_ACTION_RUN: PlaybookEditorAction
FORM_EDITOR_ACTION_UNKNOWN: FormEditorAction
FORM_EDITOR_ACTION_INFO: FormEditorAction
FORM_EDITOR_ACTION_VIEW: FormEditorAction
FORM_EDITOR_ACTION_CREATE: FormEditorAction
FORM_EDITOR_ACTION_UPDATE: FormEditorAction
EDITABLE_FORM_STATUS_UNKNOWN: EditableFormStatus
EDITABLE_FORM_STATUS_DRAFT: EditableFormStatus
EDITABLE_FORM_STATUS_MODIFIED: EditableFormStatus
EDITABLE_FORM_STATUS_SUBMITTING: EditableFormStatus
EDITABLE_FORM_STATUS_SUBMITTED: EditableFormStatus
EDITABLE_FORM_STATUS_REJECTED: EditableFormStatus
PLAYBOOK_STATUS_UNKNOWN: PlaybookStatusLight
PLAYBOOK_STATUS_ACTIVE: PlaybookStatusLight
PLAYBOOK_STATUS_INACTIVE: PlaybookStatusLight
REPORT_STYLE_LIGHT_UNKNOWN: PlaybookReportStyleLight
REPORT_STYLE_LIGHT_EXECUTIVE: PlaybookReportStyleLight
REPORT_STYLE_LIGHT_VERBOSE: PlaybookReportStyleLight
REPORT_STYLE_LIGHT_CONCISE: PlaybookReportStyleLight
FEED_AGENT_ACTION_UNKNOWN: FeedAgentAction
FEED_AGENT_ACTION_CREATE: FeedAgentAction
FEED_AGENT_ACTION_UPDATE: FeedAgentAction
QUESTIONS_STATUS_UNKNOWN: QuestionsStatus
QUESTIONS_STATUS_PENDING: QuestionsStatus
QUESTIONS_STATUS_ANSWERED: QuestionsStatus
QUESTIONS_STATUS_DISMISSED: QuestionsStatus
QUESTION_KIND_UNKNOWN: QuestionKind
QUESTION_KIND_CHOICE: QuestionKind
QUESTION_KIND_MULTICHOICE: QuestionKind
QUESTION_KIND_INPUTS: QuestionKind
QUESTION_INPUT_KIND_UNKNOWN: QuestionInputKind
QUESTION_INPUT_KIND_TEXT: QuestionInputKind
QUESTION_INPUT_KIND_FORMFIELD: QuestionInputKind
QUESTION_INPUT_KIND_MULTILINE: QuestionInputKind

class MarkdownCell(_message.Message):
    __slots__ = ('content', 'rendered_html', 'citations')
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    RENDERED_HTML_FIELD_NUMBER: _ClassVar[int]
    CITATIONS_FIELD_NUMBER: _ClassVar[int]
    content: str
    rendered_html: str
    citations: _containers.RepeatedCompositeFieldContainer[Citation]

    def __init__(self, content: _Optional[str]=..., rendered_html: _Optional[str]=..., citations: _Optional[_Iterable[_Union[Citation, _Mapping]]]=...) -> None:
        ...

class SQLCell(_message.Message):
    __slots__ = ('query', 'connector_id', 'dataframe', 'dataframe_preview', 'auth_required', 'auth_connector_name', 'auth_locator', 'auth_client_id', 'auth_role', 'auth_completed', 'auth_connector_type', 'auth_workspace_url', 'execution_time_ms', 'agent_memory')
    QUERY_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    DATAFRAME_FIELD_NUMBER: _ClassVar[int]
    DATAFRAME_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    AUTH_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    AUTH_CONNECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTH_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    AUTH_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    AUTH_ROLE_FIELD_NUMBER: _ClassVar[int]
    AUTH_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    AUTH_CONNECTOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUTH_WORKSPACE_URL_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    AGENT_MEMORY_FIELD_NUMBER: _ClassVar[int]
    query: str
    connector_id: int
    dataframe: _dataframe_pb2.DataFrameWithInfo
    dataframe_preview: str
    auth_required: bool
    auth_connector_name: str
    auth_locator: str
    auth_client_id: str
    auth_role: str
    auth_completed: bool
    auth_connector_type: _connector_pb2.ConnectorType
    auth_workspace_url: str
    execution_time_ms: int
    agent_memory: bool

    def __init__(self, query: _Optional[str]=..., connector_id: _Optional[int]=..., dataframe: _Optional[_Union[_dataframe_pb2.DataFrameWithInfo, _Mapping]]=..., dataframe_preview: _Optional[str]=..., auth_required: bool=..., auth_connector_name: _Optional[str]=..., auth_locator: _Optional[str]=..., auth_client_id: _Optional[str]=..., auth_role: _Optional[str]=..., auth_completed: bool=..., auth_connector_type: _Optional[_Union[_connector_pb2.ConnectorType, str]]=..., auth_workspace_url: _Optional[str]=..., execution_time_ms: _Optional[int]=..., agent_memory: bool=...) -> None:
        ...

class PythonCell(_message.Message):
    __slots__ = ('code', 'output', 'dataframe_info', 'dataframe_preview', 'images', 'files', 'html_screenshots', 'charts', 'auth_required', 'auth_api_access_key_id', 'auth_provider_name', 'auth_completed', 'auth_member', 'auth_permission_required', 'auth_grant_type', 'execution_time_ms')
    CODE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    DATAFRAME_INFO_FIELD_NUMBER: _ClassVar[int]
    DATAFRAME_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    HTML_SCREENSHOTS_FIELD_NUMBER: _ClassVar[int]
    CHARTS_FIELD_NUMBER: _ClassVar[int]
    AUTH_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    AUTH_API_ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    AUTH_PROVIDER_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTH_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    AUTH_MEMBER_FIELD_NUMBER: _ClassVar[int]
    AUTH_PERMISSION_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    AUTH_GRANT_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    code: str
    output: _containers.RepeatedScalarFieldContainer[str]
    dataframe_info: _containers.RepeatedCompositeFieldContainer[_dataframe_pb2.DataFrameInfo]
    dataframe_preview: _containers.RepeatedScalarFieldContainer[str]
    images: _containers.RepeatedCompositeFieldContainer[ImageReference]
    files: _containers.RepeatedCompositeFieldContainer[FileReference]
    html_screenshots: _containers.RepeatedCompositeFieldContainer[ImageReference]
    charts: _containers.RepeatedCompositeFieldContainer[ChartReference]
    auth_required: bool
    auth_api_access_key_id: str
    auth_provider_name: str
    auth_completed: bool
    auth_member: str
    auth_permission_required: bool
    auth_grant_type: str
    execution_time_ms: int

    def __init__(self, code: _Optional[str]=..., output: _Optional[_Iterable[str]]=..., dataframe_info: _Optional[_Iterable[_Union[_dataframe_pb2.DataFrameInfo, _Mapping]]]=..., dataframe_preview: _Optional[_Iterable[str]]=..., images: _Optional[_Iterable[_Union[ImageReference, _Mapping]]]=..., files: _Optional[_Iterable[_Union[FileReference, _Mapping]]]=..., html_screenshots: _Optional[_Iterable[_Union[ImageReference, _Mapping]]]=..., charts: _Optional[_Iterable[_Union[ChartReference, _Mapping]]]=..., auth_required: bool=..., auth_api_access_key_id: _Optional[str]=..., auth_provider_name: _Optional[str]=..., auth_completed: bool=..., auth_member: _Optional[str]=..., auth_permission_required: bool=..., auth_grant_type: _Optional[str]=..., execution_time_ms: _Optional[int]=...) -> None:
        ...

class StreamlitCell(_message.Message):
    __slots__ = ('code', 'url', 'error_message', 'screenshot_url', 'execution_time_ms')
    CODE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SCREENSHOT_URL_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    code: str
    url: str
    error_message: str
    screenshot_url: str
    execution_time_ms: int

    def __init__(self, code: _Optional[str]=..., url: _Optional[str]=..., error_message: _Optional[str]=..., screenshot_url: _Optional[str]=..., execution_time_ms: _Optional[int]=...) -> None:
        ...

class SqlQueryInput(_message.Message):
    __slots__ = ('name', 'query', 'connector_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    query: str
    connector_id: int

    def __init__(self, name: _Optional[str]=..., query: _Optional[str]=..., connector_id: _Optional[int]=...) -> None:
        ...

class DashboardCell(_message.Message):
    __slots__ = ('name', 'dashboard_id', 'code', 'data_sources', 'error_message', 'screenshot_url', 'last_run_at', 'action', 'type', 'updated_at')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCES_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SCREENSHOT_URL_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_AT_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    name: str
    dashboard_id: str
    code: str
    data_sources: _containers.RepeatedCompositeFieldContainer[_dashboard_pb2.DataSource]
    error_message: str
    screenshot_url: str
    last_run_at: str
    action: DashboardAction
    type: str
    updated_at: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., dashboard_id: _Optional[str]=..., code: _Optional[str]=..., data_sources: _Optional[_Iterable[_Union[_dashboard_pb2.DataSource, _Mapping]]]=..., error_message: _Optional[str]=..., screenshot_url: _Optional[str]=..., last_run_at: _Optional[str]=..., action: _Optional[_Union[DashboardAction, str]]=..., type: _Optional[str]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CompactionCell(_message.Message):
    __slots__ = ('content', 'executed_python', 'python_cells')
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    EXECUTED_PYTHON_FIELD_NUMBER: _ClassVar[int]
    PYTHON_CELLS_FIELD_NUMBER: _ClassVar[int]
    content: str
    executed_python: bool
    python_cells: _containers.RepeatedCompositeFieldContainer[PythonCell]

    def __init__(self, content: _Optional[str]=..., executed_python: bool=..., python_cells: _Optional[_Iterable[_Union[PythonCell, _Mapping]]]=...) -> None:
        ...

class ThinkingCell(_message.Message):
    __slots__ = ('content', 'redacted')
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    REDACTED_FIELD_NUMBER: _ClassVar[int]
    content: str
    redacted: bool

    def __init__(self, content: _Optional[str]=..., redacted: bool=...) -> None:
        ...

class MetricsCell(_message.Message):
    __slots__ = ('query', 'dataset', 'ontology_id', 'dataframe', 'dataframe_preview', 'generated_sql', 'query_id', 'error_message')
    QUERY_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    ONTOLOGY_ID_FIELD_NUMBER: _ClassVar[int]
    DATAFRAME_FIELD_NUMBER: _ClassVar[int]
    DATAFRAME_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    GENERATED_SQL_FIELD_NUMBER: _ClassVar[int]
    QUERY_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    query: str
    dataset: str
    ontology_id: int
    dataframe: _dataframe_pb2.DataFrameWithInfo
    dataframe_preview: str
    generated_sql: str
    query_id: str
    error_message: str

    def __init__(self, query: _Optional[str]=..., dataset: _Optional[str]=..., ontology_id: _Optional[int]=..., dataframe: _Optional[_Union[_dataframe_pb2.DataFrameWithInfo, _Mapping]]=..., dataframe_preview: _Optional[str]=..., generated_sql: _Optional[str]=..., query_id: _Optional[str]=..., error_message: _Optional[str]=...) -> None:
        ...

class OntologyMetricSearchMatch(_message.Message):
    __slots__ = ('metric_id', 'metric_name', 'metric_description', 'metric_aggregation', 'object_id', 'object_name')
    METRIC_ID_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METRIC_AGGREGATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    metric_id: str
    metric_name: str
    metric_description: str
    metric_aggregation: str
    object_id: str
    object_name: str

    def __init__(self, metric_id: _Optional[str]=..., metric_name: _Optional[str]=..., metric_description: _Optional[str]=..., metric_aggregation: _Optional[str]=..., object_id: _Optional[str]=..., object_name: _Optional[str]=...) -> None:
        ...

class OntologySearchMetricsCell(_message.Message):
    __slots__ = ('query', 'ontology_id', 'match_count', 'returned_count', 'truncated', 'matches')
    QUERY_FIELD_NUMBER: _ClassVar[int]
    ONTOLOGY_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_COUNT_FIELD_NUMBER: _ClassVar[int]
    RETURNED_COUNT_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    MATCHES_FIELD_NUMBER: _ClassVar[int]
    query: str
    ontology_id: int
    match_count: int
    returned_count: int
    truncated: bool
    matches: _containers.RepeatedCompositeFieldContainer[OntologyMetricSearchMatch]

    def __init__(self, query: _Optional[str]=..., ontology_id: _Optional[int]=..., match_count: _Optional[int]=..., returned_count: _Optional[int]=..., truncated: bool=..., matches: _Optional[_Iterable[_Union[OntologyMetricSearchMatch, _Mapping]]]=...) -> None:
        ...

class OntologyObjectDimensionLite(_message.Message):
    __slots__ = ('dimension_id', 'dimension_name', 'dimension_description', 'dimension_type')
    DIMENSION_ID_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_NAME_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    dimension_id: str
    dimension_name: str
    dimension_description: str
    dimension_type: str

    def __init__(self, dimension_id: _Optional[str]=..., dimension_name: _Optional[str]=..., dimension_description: _Optional[str]=..., dimension_type: _Optional[str]=...) -> None:
        ...

class OntologyObjectMetricLite(_message.Message):
    __slots__ = ('metric_id', 'metric_name', 'metric_description', 'metric_aggregation')
    METRIC_ID_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METRIC_AGGREGATION_FIELD_NUMBER: _ClassVar[int]
    metric_id: str
    metric_name: str
    metric_description: str
    metric_aggregation: str

    def __init__(self, metric_id: _Optional[str]=..., metric_name: _Optional[str]=..., metric_description: _Optional[str]=..., metric_aggregation: _Optional[str]=...) -> None:
        ...

class OntologyOpenObjectCell(_message.Message):
    __slots__ = ('requested_object', 'ontology_id', 'object_id', 'object_name', 'object_description', 'dimension_count', 'dimension_returned_count', 'metric_count', 'metric_returned_count', 'dimensions_truncated', 'metrics_truncated', 'dimensions', 'metrics')
    REQUESTED_OBJECT_FIELD_NUMBER: _ClassVar[int]
    ONTOLOGY_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_COUNT_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_RETURNED_COUNT_FIELD_NUMBER: _ClassVar[int]
    METRIC_COUNT_FIELD_NUMBER: _ClassVar[int]
    METRIC_RETURNED_COUNT_FIELD_NUMBER: _ClassVar[int]
    DIMENSIONS_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    METRICS_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    requested_object: str
    ontology_id: int
    object_id: str
    object_name: str
    object_description: str
    dimension_count: int
    dimension_returned_count: int
    metric_count: int
    metric_returned_count: int
    dimensions_truncated: bool
    metrics_truncated: bool
    dimensions: _containers.RepeatedCompositeFieldContainer[OntologyObjectDimensionLite]
    metrics: _containers.RepeatedCompositeFieldContainer[OntologyObjectMetricLite]

    def __init__(self, requested_object: _Optional[str]=..., ontology_id: _Optional[int]=..., object_id: _Optional[str]=..., object_name: _Optional[str]=..., object_description: _Optional[str]=..., dimension_count: _Optional[int]=..., dimension_returned_count: _Optional[int]=..., metric_count: _Optional[int]=..., metric_returned_count: _Optional[int]=..., dimensions_truncated: bool=..., metrics_truncated: bool=..., dimensions: _Optional[_Iterable[_Union[OntologyObjectDimensionLite, _Mapping]]]=..., metrics: _Optional[_Iterable[_Union[OntologyObjectMetricLite, _Mapping]]]=...) -> None:
        ...

class ImageReference(_message.Message):
    __slots__ = ('name', 'url')
    NAME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    name: str
    url: str

    def __init__(self, name: _Optional[str]=..., url: _Optional[str]=...) -> None:
        ...

class ChartReference(_message.Message):
    __slots__ = ('name', 'url', 'html_url', 'png_url', 'title', 'spec_url')
    NAME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    HTML_URL_FIELD_NUMBER: _ClassVar[int]
    PNG_URL_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SPEC_URL_FIELD_NUMBER: _ClassVar[int]
    name: str
    url: str
    html_url: str
    png_url: str
    title: str
    spec_url: str

    def __init__(self, name: _Optional[str]=..., url: _Optional[str]=..., html_url: _Optional[str]=..., png_url: _Optional[str]=..., title: _Optional[str]=..., spec_url: _Optional[str]=...) -> None:
        ...

class FileReference(_message.Message):
    __slots__ = ('name', 'url', 'file_type')
    NAME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    url: str
    file_type: str

    def __init__(self, name: _Optional[str]=..., url: _Optional[str]=..., file_type: _Optional[str]=...) -> None:
        ...

class SQLReference(_message.Message):
    __slots__ = ('tool_id',)
    TOOL_ID_FIELD_NUMBER: _ClassVar[int]
    tool_id: str

    def __init__(self, tool_id: _Optional[str]=...) -> None:
        ...

class AnswerCell(_message.Message):
    __slots__ = ('content', 'images', 'sql')
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    SQL_FIELD_NUMBER: _ClassVar[int]
    content: str
    images: _containers.RepeatedCompositeFieldContainer[ImageReference]
    sql: _containers.RepeatedCompositeFieldContainer[SQLReference]

    def __init__(self, content: _Optional[str]=..., images: _Optional[_Iterable[_Union[ImageReference, _Mapping]]]=..., sql: _Optional[_Iterable[_Union[SQLReference, _Mapping]]]=...) -> None:
        ...

class DocumentCell(_message.Message):
    __slots__ = ('name', 'url', 'preview', 'dataset_source_id', 'page_count')
    NAME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_FIELD_NUMBER: _ClassVar[int]
    DATASET_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    url: str
    preview: str
    dataset_source_id: str
    page_count: int

    def __init__(self, name: _Optional[str]=..., url: _Optional[str]=..., preview: _Optional[str]=..., dataset_source_id: _Optional[str]=..., page_count: _Optional[int]=...) -> None:
        ...

class TabularFileCell(_message.Message):
    __slots__ = ('file_name', 'category', 'dataframes', 'dataset_source_id', 'preview_available')
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    DATAFRAMES_FIELD_NUMBER: _ClassVar[int]
    DATASET_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    category: _dataset_pb2.TabularFileCategory
    dataframes: _containers.RepeatedCompositeFieldContainer[_dataframe_pb2.DataFrameInfo]
    dataset_source_id: str
    preview_available: bool

    def __init__(self, file_name: _Optional[str]=..., category: _Optional[_Union[_dataset_pb2.TabularFileCategory, str]]=..., dataframes: _Optional[_Iterable[_Union[_dataframe_pb2.DataFrameInfo, _Mapping]]]=..., dataset_source_id: _Optional[str]=..., preview_available: bool=...) -> None:
        ...

class ImageCell(_message.Message):
    __slots__ = ('name', 'url', 'mime_type', 'width', 'height', 'size_bytes', 'dataset_source_id', 'alt_text', 'caption')
    NAME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DATASET_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    ALT_TEXT_FIELD_NUMBER: _ClassVar[int]
    CAPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    url: str
    mime_type: str
    width: int
    height: int
    size_bytes: int
    dataset_source_id: str
    alt_text: str
    caption: str

    def __init__(self, name: _Optional[str]=..., url: _Optional[str]=..., mime_type: _Optional[str]=..., width: _Optional[int]=..., height: _Optional[int]=..., size_bytes: _Optional[int]=..., dataset_source_id: _Optional[str]=..., alt_text: _Optional[str]=..., caption: _Optional[str]=...) -> None:
        ...

class TextCell(_message.Message):
    __slots__ = ('file_name', 'content', 'mime_type', 'size_bytes', 'dataset_source_id', 'line_count')
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DATASET_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    LINE_COUNT_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    content: str
    mime_type: str
    size_bytes: int
    dataset_source_id: str
    line_count: int

    def __init__(self, file_name: _Optional[str]=..., content: _Optional[str]=..., mime_type: _Optional[str]=..., size_bytes: _Optional[int]=..., dataset_source_id: _Optional[str]=..., line_count: _Optional[int]=...) -> None:
        ...

class ExaSearchResult(_message.Message):
    __slots__ = ('title', 'url', 'text', 'author', 'published_date', 'favicon', 'image', 'score', 'highlights', 'highlight_scores', 'summary')
    TITLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_DATE_FIELD_NUMBER: _ClassVar[int]
    FAVICON_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    HIGHLIGHTS_FIELD_NUMBER: _ClassVar[int]
    HIGHLIGHT_SCORES_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    title: str
    url: str
    text: str
    author: str
    published_date: str
    favicon: str
    image: str
    score: float
    highlights: _containers.RepeatedScalarFieldContainer[str]
    highlight_scores: _containers.RepeatedScalarFieldContainer[float]
    summary: str

    def __init__(self, title: _Optional[str]=..., url: _Optional[str]=..., text: _Optional[str]=..., author: _Optional[str]=..., published_date: _Optional[str]=..., favicon: _Optional[str]=..., image: _Optional[str]=..., score: _Optional[float]=..., highlights: _Optional[_Iterable[str]]=..., highlight_scores: _Optional[_Iterable[float]]=..., summary: _Optional[str]=...) -> None:
        ...

class WebSearchCell(_message.Message):
    __slots__ = ('query', 'search_type', 'date_range', 'answer', 'exa_results', 'cost_dollars', 'execution_time_ms')
    QUERY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATE_RANGE_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    EXA_RESULTS_FIELD_NUMBER: _ClassVar[int]
    COST_DOLLARS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    query: str
    search_type: WebSearchType
    date_range: DateRange
    answer: str
    exa_results: _containers.RepeatedCompositeFieldContainer[ExaSearchResult]
    cost_dollars: float
    execution_time_ms: int

    def __init__(self, query: _Optional[str]=..., search_type: _Optional[_Union[WebSearchType, str]]=..., date_range: _Optional[_Union[DateRange, str]]=..., answer: _Optional[str]=..., exa_results: _Optional[_Iterable[_Union[ExaSearchResult, _Mapping]]]=..., cost_dollars: _Optional[float]=..., execution_time_ms: _Optional[int]=...) -> None:
        ...

class LinkedinSearchCell(_message.Message):
    __slots__ = ('query', 'exa_results', 'cost_dollars', 'execution_time_ms')
    QUERY_FIELD_NUMBER: _ClassVar[int]
    EXA_RESULTS_FIELD_NUMBER: _ClassVar[int]
    COST_DOLLARS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    query: str
    exa_results: _containers.RepeatedCompositeFieldContainer[ExaSearchResult]
    cost_dollars: float
    execution_time_ms: int

    def __init__(self, query: _Optional[str]=..., exa_results: _Optional[_Iterable[_Union[ExaSearchResult, _Mapping]]]=..., cost_dollars: _Optional[float]=..., execution_time_ms: _Optional[int]=...) -> None:
        ...

class ReportCell(_message.Message):
    __slots__ = ('subject', 'summary', 'blocks', 'html_preview', 'chat_id', 'report_id')
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    HTML_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    REPORT_ID_FIELD_NUMBER: _ClassVar[int]
    subject: str
    summary: str
    blocks: _containers.RepeatedCompositeFieldContainer[_report_pb2.ReportBlock]
    html_preview: str
    chat_id: str
    report_id: str

    def __init__(self, subject: _Optional[str]=..., summary: _Optional[str]=..., blocks: _Optional[_Iterable[_Union[_report_pb2.ReportBlock, _Mapping]]]=..., html_preview: _Optional[str]=..., chat_id: _Optional[str]=..., report_id: _Optional[str]=...) -> None:
        ...

class FeedExplorerCell(_message.Message):
    __slots__ = ('operation', 'post_id', 'filter', 'limit', 'result', 'channel_id')
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    operation: str
    post_id: str
    filter: str
    limit: int
    result: str
    channel_id: str

    def __init__(self, operation: _Optional[str]=..., post_id: _Optional[str]=..., filter: _Optional[str]=..., limit: _Optional[int]=..., result: _Optional[str]=..., channel_id: _Optional[str]=...) -> None:
        ...

class SummaryCell(_message.Message):
    __slots__ = ('summary',)
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    summary: str

    def __init__(self, summary: _Optional[str]=...) -> None:
        ...

class StatusCell(_message.Message):
    __slots__ = ('status',)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str

    def __init__(self, status: _Optional[str]=...) -> None:
        ...

class TableauCell(_message.Message):
    __slots__ = ('dataset_id', 'message_blocks')
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    message_blocks: _containers.RepeatedCompositeFieldContainer[TableauMessageBlock]

    def __init__(self, dataset_id: _Optional[str]=..., message_blocks: _Optional[_Iterable[_Union[TableauMessageBlock, _Mapping]]]=...) -> None:
        ...

class TableauMessageBlock(_message.Message):
    __slots__ = ('content', 'image_base64', 'pdf_base64')
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_BASE64_FIELD_NUMBER: _ClassVar[int]
    PDF_BASE64_FIELD_NUMBER: _ClassVar[int]
    content: str
    image_base64: str
    pdf_base64: str

    def __init__(self, content: _Optional[str]=..., image_base64: _Optional[str]=..., pdf_base64: _Optional[str]=...) -> None:
        ...

class TableauSQLCell(_message.Message):
    __slots__ = ('tableau_datasource_luid', 'query', 'dataframe', 'dataframe_preview')
    TABLEAU_DATASOURCE_LUID_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    DATAFRAME_FIELD_NUMBER: _ClassVar[int]
    DATAFRAME_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    tableau_datasource_luid: str
    query: str
    dataframe: _dataframe_pb2.DataFrameWithInfo
    dataframe_preview: str

    def __init__(self, tableau_datasource_luid: _Optional[str]=..., query: _Optional[str]=..., dataframe: _Optional[_Union[_dataframe_pb2.DataFrameWithInfo, _Mapping]]=..., dataframe_preview: _Optional[str]=...) -> None:
        ...

class TableauSearchFieldsCell(_message.Message):
    __slots__ = ('search_term', 'result_text')
    SEARCH_TERM_FIELD_NUMBER: _ClassVar[int]
    RESULT_TEXT_FIELD_NUMBER: _ClassVar[int]
    search_term: str
    result_text: str

    def __init__(self, search_term: _Optional[str]=..., result_text: _Optional[str]=...) -> None:
        ...

class PowerBIMessageBlock(_message.Message):
    __slots__ = ('content', 'image_base64')
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_BASE64_FIELD_NUMBER: _ClassVar[int]
    content: str
    image_base64: str

    def __init__(self, content: _Optional[str]=..., image_base64: _Optional[str]=...) -> None:
        ...

class PowerBICell(_message.Message):
    __slots__ = ('dataset_id', 'report_ids', 'powerbi_dataset_ids', 'message_blocks')
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    REPORT_IDS_FIELD_NUMBER: _ClassVar[int]
    POWERBI_DATASET_IDS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    report_ids: _containers.RepeatedScalarFieldContainer[str]
    powerbi_dataset_ids: _containers.RepeatedScalarFieldContainer[str]
    message_blocks: _containers.RepeatedCompositeFieldContainer[PowerBIMessageBlock]

    def __init__(self, dataset_id: _Optional[str]=..., report_ids: _Optional[_Iterable[str]]=..., powerbi_dataset_ids: _Optional[_Iterable[str]]=..., message_blocks: _Optional[_Iterable[_Union[PowerBIMessageBlock, _Mapping]]]=...) -> None:
        ...

class PowerBIDAXCell(_message.Message):
    __slots__ = ('dataset_id', 'dax_query', 'dataframe', 'dataframe_preview', 'auth_required', 'auth_connector_name', 'auth_connector_id', 'auth_tenant_id', 'auth_client_id', 'auth_completed')
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    DAX_QUERY_FIELD_NUMBER: _ClassVar[int]
    DATAFRAME_FIELD_NUMBER: _ClassVar[int]
    DATAFRAME_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    AUTH_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    AUTH_CONNECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTH_CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    AUTH_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    AUTH_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    AUTH_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    dax_query: str
    dataframe: _dataframe_pb2.DataFrameWithInfo
    dataframe_preview: str
    auth_required: bool
    auth_connector_name: str
    auth_connector_id: int
    auth_tenant_id: str
    auth_client_id: str
    auth_completed: bool

    def __init__(self, dataset_id: _Optional[str]=..., dax_query: _Optional[str]=..., dataframe: _Optional[_Union[_dataframe_pb2.DataFrameWithInfo, _Mapping]]=..., dataframe_preview: _Optional[str]=..., auth_required: bool=..., auth_connector_name: _Optional[str]=..., auth_connector_id: _Optional[int]=..., auth_tenant_id: _Optional[str]=..., auth_client_id: _Optional[str]=..., auth_completed: bool=...) -> None:
        ...

class ContextPromptEditorEditPair(_message.Message):
    __slots__ = ('old_string', 'new_string')
    OLD_STRING_FIELD_NUMBER: _ClassVar[int]
    NEW_STRING_FIELD_NUMBER: _ClassVar[int]
    old_string: str
    new_string: str

    def __init__(self, old_string: _Optional[str]=..., new_string: _Optional[str]=...) -> None:
        ...

class ContextPromptEditorCell(_message.Message):
    __slots__ = ('action', 'current_context', 'proposed_context', 'diff', 'status', 'error_message', 'context_id')
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PROPOSED_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DIFF_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_ID_FIELD_NUMBER: _ClassVar[int]
    action: ContextPromptEditorAction
    current_context: str
    proposed_context: str
    diff: str
    status: ContextPromptChangeStatus
    error_message: str
    context_id: str

    def __init__(self, action: _Optional[_Union[ContextPromptEditorAction, str]]=..., current_context: _Optional[str]=..., proposed_context: _Optional[str]=..., diff: _Optional[str]=..., status: _Optional[_Union[ContextPromptChangeStatus, str]]=..., error_message: _Optional[str]=..., context_id: _Optional[str]=...) -> None:
        ...

class OntologyEditorListFilter(_message.Message):
    __slots__ = ('object_id',)
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    object_id: str

    def __init__(self, object_id: _Optional[str]=...) -> None:
        ...

class OntologyEditorCell(_message.Message):
    __slots__ = ('action', 'list_type', 'operation', 'status', 'list_filter', 'list_count', 'list_objects', 'list_attributes', 'list_relations', 'list_metrics', 'created_object', 'created_attributes', 'updated_object', 'deleted_object', 'created_attribute', 'updated_attribute', 'deleted_attribute', 'created_link', 'updated_link', 'deleted_link', 'created_metric', 'updated_metric', 'deleted_metric')
    ACTION_FIELD_NUMBER: _ClassVar[int]
    LIST_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LIST_FILTER_FIELD_NUMBER: _ClassVar[int]
    LIST_COUNT_FIELD_NUMBER: _ClassVar[int]
    LIST_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    LIST_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    LIST_RELATIONS_FIELD_NUMBER: _ClassVar[int]
    LIST_METRICS_FIELD_NUMBER: _ClassVar[int]
    CREATED_OBJECT_FIELD_NUMBER: _ClassVar[int]
    CREATED_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    UPDATED_OBJECT_FIELD_NUMBER: _ClassVar[int]
    DELETED_OBJECT_FIELD_NUMBER: _ClassVar[int]
    CREATED_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    DELETED_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    CREATED_LINK_FIELD_NUMBER: _ClassVar[int]
    UPDATED_LINK_FIELD_NUMBER: _ClassVar[int]
    DELETED_LINK_FIELD_NUMBER: _ClassVar[int]
    CREATED_METRIC_FIELD_NUMBER: _ClassVar[int]
    UPDATED_METRIC_FIELD_NUMBER: _ClassVar[int]
    DELETED_METRIC_FIELD_NUMBER: _ClassVar[int]
    action: OntologyEditorAction
    list_type: OntologyEditorListType
    operation: OntologyEditorOperation
    status: OntologyEditorStatus
    list_filter: OntologyEditorListFilter
    list_count: int
    list_objects: _containers.RepeatedCompositeFieldContainer[_ontology_pb2.OntologyObject]
    list_attributes: _containers.RepeatedCompositeFieldContainer[_ontology_pb2.OntologyAttribute]
    list_relations: _containers.RepeatedCompositeFieldContainer[_ontology_pb2.OntologyRelation]
    list_metrics: _containers.RepeatedCompositeFieldContainer[_ontology_pb2.OntologyMetric]
    created_object: _ontology_pb2.OntologyObject
    created_attributes: _containers.RepeatedCompositeFieldContainer[_ontology_pb2.OntologyAttribute]
    updated_object: _ontology_pb2.OntologyObject
    deleted_object: _ontology_pb2.OntologyObject
    created_attribute: _ontology_pb2.OntologyAttribute
    updated_attribute: _ontology_pb2.OntologyAttribute
    deleted_attribute: _ontology_pb2.OntologyAttribute
    created_link: _ontology_pb2.OntologyRelation
    updated_link: _ontology_pb2.OntologyRelation
    deleted_link: _ontology_pb2.OntologyRelation
    created_metric: _ontology_pb2.OntologyMetric
    updated_metric: _ontology_pb2.OntologyMetric
    deleted_metric: _ontology_pb2.OntologyMetric

    def __init__(self, action: _Optional[_Union[OntologyEditorAction, str]]=..., list_type: _Optional[_Union[OntologyEditorListType, str]]=..., operation: _Optional[_Union[OntologyEditorOperation, str]]=..., status: _Optional[_Union[OntologyEditorStatus, str]]=..., list_filter: _Optional[_Union[OntologyEditorListFilter, _Mapping]]=..., list_count: _Optional[int]=..., list_objects: _Optional[_Iterable[_Union[_ontology_pb2.OntologyObject, _Mapping]]]=..., list_attributes: _Optional[_Iterable[_Union[_ontology_pb2.OntologyAttribute, _Mapping]]]=..., list_relations: _Optional[_Iterable[_Union[_ontology_pb2.OntologyRelation, _Mapping]]]=..., list_metrics: _Optional[_Iterable[_Union[_ontology_pb2.OntologyMetric, _Mapping]]]=..., created_object: _Optional[_Union[_ontology_pb2.OntologyObject, _Mapping]]=..., created_attributes: _Optional[_Iterable[_Union[_ontology_pb2.OntologyAttribute, _Mapping]]]=..., updated_object: _Optional[_Union[_ontology_pb2.OntologyObject, _Mapping]]=..., deleted_object: _Optional[_Union[_ontology_pb2.OntologyObject, _Mapping]]=..., created_attribute: _Optional[_Union[_ontology_pb2.OntologyAttribute, _Mapping]]=..., updated_attribute: _Optional[_Union[_ontology_pb2.OntologyAttribute, _Mapping]]=..., deleted_attribute: _Optional[_Union[_ontology_pb2.OntologyAttribute, _Mapping]]=..., created_link: _Optional[_Union[_ontology_pb2.OntologyRelation, _Mapping]]=..., updated_link: _Optional[_Union[_ontology_pb2.OntologyRelation, _Mapping]]=..., deleted_link: _Optional[_Union[_ontology_pb2.OntologyRelation, _Mapping]]=..., created_metric: _Optional[_Union[_ontology_pb2.OntologyMetric, _Mapping]]=..., updated_metric: _Optional[_Union[_ontology_pb2.OntologyMetric, _Mapping]]=..., deleted_metric: _Optional[_Union[_ontology_pb2.OntologyMetric, _Mapping]]=...) -> None:
        ...

class MCPToolCell(_message.Message):
    __slots__ = ('server_name', 'tool_name', 'arguments_json', 'content_json', 'is_error', 'error_message', 'execution_time_ms')
    SERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_JSON_FIELD_NUMBER: _ClassVar[int]
    CONTENT_JSON_FIELD_NUMBER: _ClassVar[int]
    IS_ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    server_name: str
    tool_name: str
    arguments_json: str
    content_json: str
    is_error: bool
    error_message: str
    execution_time_ms: int

    def __init__(self, server_name: _Optional[str]=..., tool_name: _Optional[str]=..., arguments_json: _Optional[str]=..., content_json: _Optional[str]=..., is_error: bool=..., error_message: _Optional[str]=..., execution_time_ms: _Optional[int]=...) -> None:
        ...

class UseSkillCell(_message.Message):
    __slots__ = ('trigger', 'name', 'ok')
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OK_FIELD_NUMBER: _ClassVar[int]
    trigger: str
    name: str
    ok: bool

    def __init__(self, trigger: _Optional[str]=..., name: _Optional[str]=..., ok: bool=...) -> None:
        ...

class OntologyQueryParam(_message.Message):
    __slots__ = ('name', 'type', 'nullable', 'description', 'default_value')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NULLABLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    nullable: bool
    description: str
    default_value: str

    def __init__(self, name: _Optional[str]=..., type: _Optional[str]=..., nullable: bool=..., description: _Optional[str]=..., default_value: _Optional[str]=...) -> None:
        ...

class OntologyQueryCell(_message.Message):
    __slots__ = ('action', 'path', 'params_json', 'connector_id', 'declared_params', 'sql', 'used_connector_id', 'dataframe', 'dataframe_preview', 'auth_required', 'auth_connector_name', 'auth_locator', 'auth_client_id', 'auth_role', 'auth_completed', 'auth_connector_type', 'auth_workspace_url')
    ACTION_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    PARAMS_JSON_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    DECLARED_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SQL_FIELD_NUMBER: _ClassVar[int]
    USED_CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    DATAFRAME_FIELD_NUMBER: _ClassVar[int]
    DATAFRAME_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    AUTH_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    AUTH_CONNECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTH_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    AUTH_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    AUTH_ROLE_FIELD_NUMBER: _ClassVar[int]
    AUTH_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    AUTH_CONNECTOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUTH_WORKSPACE_URL_FIELD_NUMBER: _ClassVar[int]
    action: str
    path: str
    params_json: str
    connector_id: int
    declared_params: _containers.RepeatedCompositeFieldContainer[OntologyQueryParam]
    sql: str
    used_connector_id: int
    dataframe: _dataframe_pb2.DataFrameWithInfo
    dataframe_preview: str
    auth_required: bool
    auth_connector_name: str
    auth_locator: str
    auth_client_id: str
    auth_role: str
    auth_completed: bool
    auth_connector_type: _connector_pb2.ConnectorType
    auth_workspace_url: str

    def __init__(self, action: _Optional[str]=..., path: _Optional[str]=..., params_json: _Optional[str]=..., connector_id: _Optional[int]=..., declared_params: _Optional[_Iterable[_Union[OntologyQueryParam, _Mapping]]]=..., sql: _Optional[str]=..., used_connector_id: _Optional[int]=..., dataframe: _Optional[_Union[_dataframe_pb2.DataFrameWithInfo, _Mapping]]=..., dataframe_preview: _Optional[str]=..., auth_required: bool=..., auth_connector_name: _Optional[str]=..., auth_locator: _Optional[str]=..., auth_client_id: _Optional[str]=..., auth_role: _Optional[str]=..., auth_completed: bool=..., auth_connector_type: _Optional[_Union[_connector_pb2.ConnectorType, str]]=..., auth_workspace_url: _Optional[str]=...) -> None:
        ...

class PreviewCell(_message.Message):
    __slots__ = ('target', 'preview_type', 'name', 'url', 'content', 'error')
    TARGET_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    target: str
    preview_type: str
    name: str
    url: str
    content: str
    error: str

    def __init__(self, target: _Optional[str]=..., preview_type: _Optional[str]=..., name: _Optional[str]=..., url: _Optional[str]=..., content: _Optional[str]=..., error: _Optional[str]=...) -> None:
        ...

class FormEditorCell(_message.Message):
    __slots__ = ('action', 'form_snapshot', 'form', 'form_id')
    ACTION_FIELD_NUMBER: _ClassVar[int]
    FORM_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    FORM_FIELD_NUMBER: _ClassVar[int]
    FORM_ID_FIELD_NUMBER: _ClassVar[int]
    action: FormEditorAction
    form_snapshot: EditableForm
    form: EditableForm
    form_id: str

    def __init__(self, action: _Optional[_Union[FormEditorAction, str]]=..., form_snapshot: _Optional[_Union[EditableForm, _Mapping]]=..., form: _Optional[_Union[EditableForm, _Mapping]]=..., form_id: _Optional[str]=...) -> None:
        ...

class FormCell(_message.Message):
    __slots__ = ('action', 'form_id', 'form_type', 'status', 'test_status', 'name', 'approval_outcome', 'test_message')
    ACTION_FIELD_NUMBER: _ClassVar[int]
    FORM_ID_FIELD_NUMBER: _ClassVar[int]
    FORM_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TEST_STATUS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_OUTCOME_FIELD_NUMBER: _ClassVar[int]
    TEST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    action: str
    form_id: str
    form_type: str
    status: str
    test_status: str
    name: str
    approval_outcome: str
    test_message: str

    def __init__(self, action: _Optional[str]=..., form_id: _Optional[str]=..., form_type: _Optional[str]=..., status: _Optional[str]=..., test_status: _Optional[str]=..., name: _Optional[str]=..., approval_outcome: _Optional[str]=..., test_message: _Optional[str]=...) -> None:
        ...

class EditableForm(_message.Message):
    __slots__ = ('form_name', 'fields', 'status', 'id', 'submit_error', 'submit_result', 'validation_error')
    FORM_NAME_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_ERROR_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_RESULT_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    form_name: str
    fields: _struct_pb2.Struct
    status: EditableFormStatus
    id: str
    submit_error: str
    submit_result: str
    validation_error: str

    def __init__(self, form_name: _Optional[str]=..., fields: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., status: _Optional[_Union[EditableFormStatus, str]]=..., id: _Optional[str]=..., submit_error: _Optional[str]=..., submit_result: _Optional[str]=..., validation_error: _Optional[str]=...) -> None:
        ...

class ConnectorRef(_message.Message):
    __slots__ = ('id', 'name', 'type')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    type: str

    def __init__(self, id: _Optional[int]=..., name: _Optional[str]=..., type: _Optional[str]=...) -> None:
        ...

class OrgMemberRef(_message.Message):
    __slots__ = ('email', 'name')
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    email: str
    name: str

    def __init__(self, email: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class SlackChannelRef(_message.Message):
    __slots__ = ('channel_id', 'name')
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    name: str

    def __init__(self, channel_id: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class SlackUserRef(_message.Message):
    __slots__ = ('user_id', 'name')
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    name: str

    def __init__(self, user_id: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class TeamsChannelRef(_message.Message):
    __slots__ = ('channel_id', 'name')
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    name: str

    def __init__(self, channel_id: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class TeamsUserRef(_message.Message):
    __slots__ = ('user_aad_id', 'name')
    USER_AAD_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    user_aad_id: str
    name: str

    def __init__(self, user_aad_id: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class FieldChange(_message.Message):
    __slots__ = ('field_name', 'old_value', 'new_value')
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    OLD_VALUE_FIELD_NUMBER: _ClassVar[int]
    NEW_VALUE_FIELD_NUMBER: _ClassVar[int]
    field_name: str
    old_value: str
    new_value: str

    def __init__(self, field_name: _Optional[str]=..., old_value: _Optional[str]=..., new_value: _Optional[str]=...) -> None:
        ...

class PlaybookInfo(_message.Message):
    __slots__ = ('id', 'name', 'prompt', 'owner_id', 'owner_email', 'created_at', 'updated_at', 'cron_string', 'datasets', 'email_addresses', 'slack_channel_id', 'tagged_slack_user_ids', 'status', 'connector_id', 'paradigm_type', 'report_output_style', 'is_subscribed', 'connector_ids', 'teams_channel_id', 'tagged_teams_user_aad_ids')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CRON_STRING_FIELD_NUMBER: _ClassVar[int]
    DATASETS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    SLACK_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TAGGED_SLACK_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    PARADIGM_TYPE_FIELD_NUMBER: _ClassVar[int]
    REPORT_OUTPUT_STYLE_FIELD_NUMBER: _ClassVar[int]
    IS_SUBSCRIBED_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_IDS_FIELD_NUMBER: _ClassVar[int]
    TEAMS_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TAGGED_TEAMS_USER_AAD_IDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    prompt: str
    owner_id: str
    owner_email: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    cron_string: str
    datasets: _containers.RepeatedCompositeFieldContainer[_dataset_pb2.Dataset]
    email_addresses: _containers.RepeatedScalarFieldContainer[str]
    slack_channel_id: str
    tagged_slack_user_ids: _containers.RepeatedScalarFieldContainer[str]
    status: PlaybookStatusLight
    connector_id: int
    paradigm_type: _paradigm_params_pb2.ParadigmType
    report_output_style: PlaybookReportStyleLight
    is_subscribed: bool
    connector_ids: _containers.RepeatedScalarFieldContainer[int]
    teams_channel_id: str
    tagged_teams_user_aad_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., prompt: _Optional[str]=..., owner_id: _Optional[str]=..., owner_email: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., cron_string: _Optional[str]=..., datasets: _Optional[_Iterable[_Union[_dataset_pb2.Dataset, _Mapping]]]=..., email_addresses: _Optional[_Iterable[str]]=..., slack_channel_id: _Optional[str]=..., tagged_slack_user_ids: _Optional[_Iterable[str]]=..., status: _Optional[_Union[PlaybookStatusLight, str]]=..., connector_id: _Optional[int]=..., paradigm_type: _Optional[_Union[_paradigm_params_pb2.ParadigmType, str]]=..., report_output_style: _Optional[_Union[PlaybookReportStyleLight, str]]=..., is_subscribed: bool=..., connector_ids: _Optional[_Iterable[int]]=..., teams_channel_id: _Optional[str]=..., tagged_teams_user_aad_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class PlaybookEditorCell(_message.Message):
    __slots__ = ('action', 'playbooks', 'error_message', 'total_count', 'slack_channels', 'slack_users', 'connectors', 'org_members', 'has_slack', 'field_changes', 'teams_channels', 'teams_users', 'has_teams')
    ACTION_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOKS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    SLACK_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    SLACK_USERS_FIELD_NUMBER: _ClassVar[int]
    CONNECTORS_FIELD_NUMBER: _ClassVar[int]
    ORG_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    HAS_SLACK_FIELD_NUMBER: _ClassVar[int]
    FIELD_CHANGES_FIELD_NUMBER: _ClassVar[int]
    TEAMS_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    TEAMS_USERS_FIELD_NUMBER: _ClassVar[int]
    HAS_TEAMS_FIELD_NUMBER: _ClassVar[int]
    action: PlaybookEditorAction
    playbooks: _containers.RepeatedCompositeFieldContainer[PlaybookInfo]
    error_message: str
    total_count: int
    slack_channels: _containers.RepeatedCompositeFieldContainer[SlackChannelRef]
    slack_users: _containers.RepeatedCompositeFieldContainer[SlackUserRef]
    connectors: _containers.RepeatedCompositeFieldContainer[ConnectorRef]
    org_members: _containers.RepeatedCompositeFieldContainer[OrgMemberRef]
    has_slack: bool
    field_changes: _containers.RepeatedCompositeFieldContainer[FieldChange]
    teams_channels: _containers.RepeatedCompositeFieldContainer[TeamsChannelRef]
    teams_users: _containers.RepeatedCompositeFieldContainer[TeamsUserRef]
    has_teams: bool

    def __init__(self, action: _Optional[_Union[PlaybookEditorAction, str]]=..., playbooks: _Optional[_Iterable[_Union[PlaybookInfo, _Mapping]]]=..., error_message: _Optional[str]=..., total_count: _Optional[int]=..., slack_channels: _Optional[_Iterable[_Union[SlackChannelRef, _Mapping]]]=..., slack_users: _Optional[_Iterable[_Union[SlackUserRef, _Mapping]]]=..., connectors: _Optional[_Iterable[_Union[ConnectorRef, _Mapping]]]=..., org_members: _Optional[_Iterable[_Union[OrgMemberRef, _Mapping]]]=..., has_slack: bool=..., field_changes: _Optional[_Iterable[_Union[FieldChange, _Mapping]]]=..., teams_channels: _Optional[_Iterable[_Union[TeamsChannelRef, _Mapping]]]=..., teams_users: _Optional[_Iterable[_Union[TeamsUserRef, _Mapping]]]=..., has_teams: bool=...) -> None:
        ...

class GoogleDriveFile(_message.Message):
    __slots__ = ('id', 'name', 'mime_type', 'size', 'modified_time', 'web_view_link')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_TIME_FIELD_NUMBER: _ClassVar[int]
    WEB_VIEW_LINK_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    mime_type: str
    size: int
    modified_time: str
    web_view_link: str

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., mime_type: _Optional[str]=..., size: _Optional[int]=..., modified_time: _Optional[str]=..., web_view_link: _Optional[str]=...) -> None:
        ...

class GoogleDriveSearchCell(_message.Message):
    __slots__ = ('files', 'dataframe_preview', 'error_message', 'file_count')
    FILES_FIELD_NUMBER: _ClassVar[int]
    DATAFRAME_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FILE_COUNT_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[GoogleDriveFile]
    dataframe_preview: str
    error_message: str
    file_count: int

    def __init__(self, files: _Optional[_Iterable[_Union[GoogleDriveFile, _Mapping]]]=..., dataframe_preview: _Optional[str]=..., error_message: _Optional[str]=..., file_count: _Optional[int]=...) -> None:
        ...

class GoogleDriveContentCell(_message.Message):
    __slots__ = ('file_name', 'content_type', 'content', 'file_id', 'error_message')
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    content_type: str
    content: str
    file_id: str
    error_message: str

    def __init__(self, file_name: _Optional[str]=..., content_type: _Optional[str]=..., content: _Optional[str]=..., file_id: _Optional[str]=..., error_message: _Optional[str]=...) -> None:
        ...

class Microsoft365EmailSearchCell(_message.Message):
    __slots__ = ('email_count', 'email_summary', 'synthetic_tool_use_id')
    EMAIL_COUNT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SYNTHETIC_TOOL_USE_ID_FIELD_NUMBER: _ClassVar[int]
    email_count: int
    email_summary: str
    synthetic_tool_use_id: str

    def __init__(self, email_count: _Optional[int]=..., email_summary: _Optional[str]=..., synthetic_tool_use_id: _Optional[str]=...) -> None:
        ...

class Microsoft365EmailContentCell(_message.Message):
    __slots__ = ('email_id', 'subject', 'sender', 'synthetic_tool_use_id')
    EMAIL_ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    SYNTHETIC_TOOL_USE_ID_FIELD_NUMBER: _ClassVar[int]
    email_id: str
    subject: str
    sender: str
    synthetic_tool_use_id: str

    def __init__(self, email_id: _Optional[str]=..., subject: _Optional[str]=..., sender: _Optional[str]=..., synthetic_tool_use_id: _Optional[str]=...) -> None:
        ...

class Microsoft365CalendarCell(_message.Message):
    __slots__ = ('event_count', 'event_summary', 'synthetic_tool_use_id')
    EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    EVENT_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SYNTHETIC_TOOL_USE_ID_FIELD_NUMBER: _ClassVar[int]
    event_count: int
    event_summary: str
    synthetic_tool_use_id: str

    def __init__(self, event_count: _Optional[int]=..., event_summary: _Optional[str]=..., synthetic_tool_use_id: _Optional[str]=...) -> None:
        ...

class GmailEmailSearchCell(_message.Message):
    __slots__ = ('email_count', 'email_summary', 'synthetic_tool_use_id')
    EMAIL_COUNT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SYNTHETIC_TOOL_USE_ID_FIELD_NUMBER: _ClassVar[int]
    email_count: int
    email_summary: str
    synthetic_tool_use_id: str

    def __init__(self, email_count: _Optional[int]=..., email_summary: _Optional[str]=..., synthetic_tool_use_id: _Optional[str]=...) -> None:
        ...

class GoogleCalendarSearchCell(_message.Message):
    __slots__ = ('event_count', 'event_summary', 'synthetic_tool_use_id')
    EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    EVENT_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SYNTHETIC_TOOL_USE_ID_FIELD_NUMBER: _ClassVar[int]
    event_count: int
    event_summary: str
    synthetic_tool_use_id: str

    def __init__(self, event_count: _Optional[int]=..., event_summary: _Optional[str]=..., synthetic_tool_use_id: _Optional[str]=...) -> None:
        ...

class GmailEmailContentCell(_message.Message):
    __slots__ = ('email_id', 'subject', 'sender', 'synthetic_tool_use_id')
    EMAIL_ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    SYNTHETIC_TOOL_USE_ID_FIELD_NUMBER: _ClassVar[int]
    email_id: str
    subject: str
    sender: str
    synthetic_tool_use_id: str

    def __init__(self, email_id: _Optional[str]=..., subject: _Optional[str]=..., sender: _Optional[str]=..., synthetic_tool_use_id: _Optional[str]=...) -> None:
        ...

class PreviewCellRef(_message.Message):
    __slots__ = ('target', 'preview_type', 'name', 'url')
    TARGET_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    target: str
    preview_type: str
    name: str
    url: str

    def __init__(self, target: _Optional[str]=..., preview_type: _Optional[str]=..., name: _Optional[str]=..., url: _Optional[str]=...) -> None:
        ...

class ReportHistoryInfo(_message.Message):
    __slots__ = ('id', 'chat_id', 'cell_id', 'created_at', 'subject', 'summary', 'blocks', 'read_at', 'preview_cells', 'html_preview')
    ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    READ_AT_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_CELLS_FIELD_NUMBER: _ClassVar[int]
    HTML_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    id: str
    chat_id: str
    cell_id: str
    created_at: _timestamp_pb2.Timestamp
    subject: str
    summary: str
    blocks: _containers.RepeatedCompositeFieldContainer[_report_pb2.ReportBlock]
    read_at: _timestamp_pb2.Timestamp
    preview_cells: _containers.RepeatedCompositeFieldContainer[PreviewCellRef]
    html_preview: str

    def __init__(self, id: _Optional[str]=..., chat_id: _Optional[str]=..., cell_id: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., subject: _Optional[str]=..., summary: _Optional[str]=..., blocks: _Optional[_Iterable[_Union[_report_pb2.ReportBlock, _Mapping]]]=..., read_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., preview_cells: _Optional[_Iterable[_Union[PreviewCellRef, _Mapping]]]=..., html_preview: _Optional[str]=...) -> None:
        ...

class ReportHistoryCell(_message.Message):
    __slots__ = ('reports', 'total_count', 'error_message')
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    reports: _containers.RepeatedCompositeFieldContainer[ReportHistoryInfo]
    total_count: int
    error_message: str

    def __init__(self, reports: _Optional[_Iterable[_Union[ReportHistoryInfo, _Mapping]]]=..., total_count: _Optional[int]=..., error_message: _Optional[str]=...) -> None:
        ...

class BashCell(_message.Message):
    __slots__ = ('script', 'stdout', 'stderr', 'exit_code')
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    STDOUT_FIELD_NUMBER: _ClassVar[int]
    STDERR_FIELD_NUMBER: _ClassVar[int]
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    script: str
    stdout: str
    stderr: str
    exit_code: int

    def __init__(self, script: _Optional[str]=..., stdout: _Optional[str]=..., stderr: _Optional[str]=..., exit_code: _Optional[int]=...) -> None:
        ...

class JavaScriptCell(_message.Message):
    __slots__ = ('code', 'title', 'files', 'images', 'stdout')
    CODE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    STDOUT_FIELD_NUMBER: _ClassVar[int]
    code: str
    title: str
    files: _containers.RepeatedCompositeFieldContainer[FileReference]
    images: _containers.RepeatedCompositeFieldContainer[ImageReference]
    stdout: str

    def __init__(self, code: _Optional[str]=..., title: _Optional[str]=..., files: _Optional[_Iterable[_Union[FileReference, _Mapping]]]=..., images: _Optional[_Iterable[_Union[ImageReference, _Mapping]]]=..., stdout: _Optional[str]=...) -> None:
        ...

class FeedPostCell(_message.Message):
    __slots__ = ('title', 'content', 'image_urls', 'dashboard_ids', 'report_ids', 'chat_ids', 'post_id', 'post_url', 'timestamp', 'error', 'mentioned_member_ids', 'mentioned_agent_ids')
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URLS_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_IDS_FIELD_NUMBER: _ClassVar[int]
    REPORT_IDS_FIELD_NUMBER: _ClassVar[int]
    CHAT_IDS_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    POST_URL_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MENTIONED_MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    MENTIONED_AGENT_IDS_FIELD_NUMBER: _ClassVar[int]
    title: str
    content: str
    image_urls: _containers.RepeatedScalarFieldContainer[str]
    dashboard_ids: _containers.RepeatedScalarFieldContainer[str]
    report_ids: _containers.RepeatedScalarFieldContainer[str]
    chat_ids: _containers.RepeatedScalarFieldContainer[str]
    post_id: str
    post_url: str
    timestamp: str
    error: str
    mentioned_member_ids: _containers.RepeatedScalarFieldContainer[str]
    mentioned_agent_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, title: _Optional[str]=..., content: _Optional[str]=..., image_urls: _Optional[_Iterable[str]]=..., dashboard_ids: _Optional[_Iterable[str]]=..., report_ids: _Optional[_Iterable[str]]=..., chat_ids: _Optional[_Iterable[str]]=..., post_id: _Optional[str]=..., post_url: _Optional[str]=..., timestamp: _Optional[str]=..., error: _Optional[str]=..., mentioned_member_ids: _Optional[_Iterable[str]]=..., mentioned_agent_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class FeedCommentCell(_message.Message):
    __slots__ = ('post_id', 'content', 'comment_id', 'comment_url', 'timestamp', 'error', 'post_title', 'post_author', 'post_upvote_count', 'post_downvote_count')
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_URL_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    POST_TITLE_FIELD_NUMBER: _ClassVar[int]
    POST_AUTHOR_FIELD_NUMBER: _ClassVar[int]
    POST_UPVOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    POST_DOWNVOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    content: str
    comment_id: str
    comment_url: str
    timestamp: str
    error: str
    post_title: str
    post_author: str
    post_upvote_count: int
    post_downvote_count: int

    def __init__(self, post_id: _Optional[str]=..., content: _Optional[str]=..., comment_id: _Optional[str]=..., comment_url: _Optional[str]=..., timestamp: _Optional[str]=..., error: _Optional[str]=..., post_title: _Optional[str]=..., post_author: _Optional[str]=..., post_upvote_count: _Optional[int]=..., post_downvote_count: _Optional[int]=...) -> None:
        ...

class FeedEngageCell(_message.Message):
    __slots__ = ('thing_id', 'vote_type', 'upvote_count', 'downvote_count', 'timestamp', 'error', 'url', 'thing_title')
    THING_ID_FIELD_NUMBER: _ClassVar[int]
    VOTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    UPVOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    DOWNVOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    THING_TITLE_FIELD_NUMBER: _ClassVar[int]
    thing_id: str
    vote_type: str
    upvote_count: int
    downvote_count: int
    timestamp: str
    error: str
    url: str
    thing_title: str

    def __init__(self, thing_id: _Optional[str]=..., vote_type: _Optional[str]=..., upvote_count: _Optional[int]=..., downvote_count: _Optional[int]=..., timestamp: _Optional[str]=..., error: _Optional[str]=..., url: _Optional[str]=..., thing_title: _Optional[str]=...) -> None:
        ...

class DashboardInfo(_message.Message):
    __slots__ = ('id', 'name', 'description', 'status', 'creator_id', 'created_at', 'updated_at', 'refreshed_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATOR_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    REFRESHED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    status: str
    creator_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    refreshed_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., description: _Optional[str]=..., status: _Optional[str]=..., creator_id: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., refreshed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListDashboardsCell(_message.Message):
    __slots__ = ('search_term', 'dashboard_id', 'total_count', 'sandbox_available', 'error_message', 'dashboards')
    SEARCH_TERM_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DASHBOARDS_FIELD_NUMBER: _ClassVar[int]
    search_term: str
    dashboard_id: str
    total_count: int
    sandbox_available: bool
    error_message: str
    dashboards: _containers.RepeatedCompositeFieldContainer[DashboardInfo]

    def __init__(self, search_term: _Optional[str]=..., dashboard_id: _Optional[str]=..., total_count: _Optional[int]=..., sandbox_available: bool=..., error_message: _Optional[str]=..., dashboards: _Optional[_Iterable[_Union[DashboardInfo, _Mapping]]]=...) -> None:
        ...

class AgentInfo(_message.Message):
    __slots__ = ('id', 'name', 'avatar_url', 'type', 'email')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_URL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    avatar_url: str
    type: str
    email: str

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., avatar_url: _Optional[str]=..., type: _Optional[str]=..., email: _Optional[str]=...) -> None:
        ...

class ListUsersCell(_message.Message):
    __slots__ = ('search_term', 'user_type', 'total_count', 'sandbox_available', 'error_message', 'agents')
    SEARCH_TERM_FIELD_NUMBER: _ClassVar[int]
    USER_TYPE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    search_term: str
    user_type: str
    total_count: int
    sandbox_available: bool
    error_message: str
    agents: _containers.RepeatedCompositeFieldContainer[AgentInfo]

    def __init__(self, search_term: _Optional[str]=..., user_type: _Optional[str]=..., total_count: _Optional[int]=..., sandbox_available: bool=..., error_message: _Optional[str]=..., agents: _Optional[_Iterable[_Union[AgentInfo, _Mapping]]]=...) -> None:
        ...

class ConnectorsCell(_message.Message):
    __slots__ = ('action', 'total_count')
    ACTION_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    action: str
    total_count: int

    def __init__(self, action: _Optional[str]=..., total_count: _Optional[int]=...) -> None:
        ...

class FeedAgentInfo(_message.Message):
    __slots__ = ('id', 'name', 'prompt', 'is_active', 'created_at', 'paradigm_options', 'connector_ids', 'llm_model', 'fast_mode', 'posting_frequency_crons')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    PARADIGM_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_IDS_FIELD_NUMBER: _ClassVar[int]
    LLM_MODEL_FIELD_NUMBER: _ClassVar[int]
    FAST_MODE_FIELD_NUMBER: _ClassVar[int]
    POSTING_FREQUENCY_CRONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    prompt: str
    is_active: bool
    created_at: _timestamp_pb2.Timestamp
    paradigm_options: _paradigm_pb2.ParadigmOptions
    connector_ids: _containers.RepeatedScalarFieldContainer[int]
    llm_model: _llm_model_pb2.LlmModel
    fast_mode: bool
    posting_frequency_crons: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., prompt: _Optional[str]=..., is_active: bool=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., paradigm_options: _Optional[_Union[_paradigm_pb2.ParadigmOptions, _Mapping]]=..., connector_ids: _Optional[_Iterable[int]]=..., llm_model: _Optional[_Union[_llm_model_pb2.LlmModel, str]]=..., fast_mode: bool=..., posting_frequency_crons: _Optional[_Iterable[str]]=...) -> None:
        ...

class FeedCreateCell(_message.Message):
    __slots__ = ('action', 'agent', 'error_message', 'updated_fields', 'field_changes', 'connectors')
    ACTION_FIELD_NUMBER: _ClassVar[int]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_CHANGES_FIELD_NUMBER: _ClassVar[int]
    CONNECTORS_FIELD_NUMBER: _ClassVar[int]
    action: FeedAgentAction
    agent: FeedAgentInfo
    error_message: str
    updated_fields: _containers.RepeatedScalarFieldContainer[str]
    field_changes: _containers.RepeatedCompositeFieldContainer[FieldChange]
    connectors: _containers.RepeatedCompositeFieldContainer[ConnectorRef]

    def __init__(self, action: _Optional[_Union[FeedAgentAction, str]]=..., agent: _Optional[_Union[FeedAgentInfo, _Mapping]]=..., error_message: _Optional[str]=..., updated_fields: _Optional[_Iterable[str]]=..., field_changes: _Optional[_Iterable[_Union[FieldChange, _Mapping]]]=..., connectors: _Optional[_Iterable[_Union[ConnectorRef, _Mapping]]]=...) -> None:
        ...

class EmailRecipient(_message.Message):
    __slots__ = ('address', 'member_id', 'display_name')
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    address: str
    member_id: str
    display_name: str

    def __init__(self, address: _Optional[str]=..., member_id: _Optional[str]=..., display_name: _Optional[str]=..., **kwargs) -> None:
        ...

class EmailCell(_message.Message):
    __slots__ = ('to', 'subject', 'body', 'recipients', 'status', 'sent_at', 'message_id', 'error_message', 'error_class', 'sent_count', 'rendered_body_html')
    TO_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CLASS_FIELD_NUMBER: _ClassVar[int]
    SENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    RENDERED_BODY_HTML_FIELD_NUMBER: _ClassVar[int]
    to: _containers.RepeatedScalarFieldContainer[str]
    subject: str
    body: str
    recipients: _containers.RepeatedCompositeFieldContainer[EmailRecipient]
    status: str
    sent_at: str
    message_id: str
    error_message: str
    error_class: str
    sent_count: int
    rendered_body_html: str

    def __init__(self, to: _Optional[_Iterable[str]]=..., subject: _Optional[str]=..., body: _Optional[str]=..., recipients: _Optional[_Iterable[_Union[EmailRecipient, _Mapping]]]=..., status: _Optional[str]=..., sent_at: _Optional[str]=..., message_id: _Optional[str]=..., error_message: _Optional[str]=..., error_class: _Optional[str]=..., sent_count: _Optional[int]=..., rendered_body_html: _Optional[str]=...) -> None:
        ...

class PatchCell(_message.Message):
    __slots__ = ('title', 'description', 'number', 'has_conflicts', 'conflict_view', 'status', 'diffs', 'patch_id', 'git_ref', 'auto_approved', 'auto_approved_rule_directory')
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    HAS_CONFLICTS_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_VIEW_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DIFFS_FIELD_NUMBER: _ClassVar[int]
    PATCH_ID_FIELD_NUMBER: _ClassVar[int]
    GIT_REF_FIELD_NUMBER: _ClassVar[int]
    AUTO_APPROVED_FIELD_NUMBER: _ClassVar[int]
    AUTO_APPROVED_RULE_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    number: int
    has_conflicts: bool
    conflict_view: str
    status: _patches_pb2.PatchStatus
    diffs: _containers.RepeatedCompositeFieldContainer[_patches_pb2.PatchDiff]
    patch_id: str
    git_ref: str
    auto_approved: bool
    auto_approved_rule_directory: str

    def __init__(self, title: _Optional[str]=..., description: _Optional[str]=..., number: _Optional[int]=..., has_conflicts: bool=..., conflict_view: _Optional[str]=..., status: _Optional[_Union[_patches_pb2.PatchStatus, str]]=..., diffs: _Optional[_Iterable[_Union[_patches_pb2.PatchDiff, _Mapping]]]=..., patch_id: _Optional[str]=..., git_ref: _Optional[str]=..., auto_approved: bool=..., auto_approved_rule_directory: _Optional[str]=...) -> None:
        ...

class QuestionOption(_message.Message):
    __slots__ = ('name', 'description', 'explanation')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    explanation: str

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., explanation: _Optional[str]=...) -> None:
        ...

class QuestionInput(_message.Message):
    __slots__ = ('kind', 'label', 'explanation', 'sensitive', 'form_path_label')
    KIND_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    FORM_PATH_LABEL_FIELD_NUMBER: _ClassVar[int]
    kind: QuestionInputKind
    label: str
    explanation: str
    sensitive: bool
    form_path_label: str

    def __init__(self, kind: _Optional[_Union[QuestionInputKind, str]]=..., label: _Optional[str]=..., explanation: _Optional[str]=..., sensitive: bool=..., form_path_label: _Optional[str]=...) -> None:
        ...

class QuestionSpec(_message.Message):
    __slots__ = ('question', 'explanation', 'kind', 'options', 'allow_custom', 'inputs')
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_CUSTOM_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    question: str
    explanation: str
    kind: QuestionKind
    options: _containers.RepeatedCompositeFieldContainer[QuestionOption]
    allow_custom: bool
    inputs: _containers.RepeatedCompositeFieldContainer[QuestionInput]

    def __init__(self, question: _Optional[str]=..., explanation: _Optional[str]=..., kind: _Optional[_Union[QuestionKind, str]]=..., options: _Optional[_Iterable[_Union[QuestionOption, _Mapping]]]=..., allow_custom: bool=..., inputs: _Optional[_Iterable[_Union[QuestionInput, _Mapping]]]=...) -> None:
        ...

class QuestionAnswer(_message.Message):
    __slots__ = ('selected', 'custom', 'inputs', 'provided')
    SELECTED_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    PROVIDED_FIELD_NUMBER: _ClassVar[int]
    selected: _containers.RepeatedScalarFieldContainer[str]
    custom: str
    inputs: _containers.RepeatedScalarFieldContainer[str]
    provided: _containers.RepeatedScalarFieldContainer[bool]

    def __init__(self, selected: _Optional[_Iterable[str]]=..., custom: _Optional[str]=..., inputs: _Optional[_Iterable[str]]=..., provided: _Optional[_Iterable[bool]]=...) -> None:
        ...

class QuestionsCell(_message.Message):
    __slots__ = ('status', 'questions', 'answers', 'answered_count')
    STATUS_FIELD_NUMBER: _ClassVar[int]
    QUESTIONS_FIELD_NUMBER: _ClassVar[int]
    ANSWERS_FIELD_NUMBER: _ClassVar[int]
    ANSWERED_COUNT_FIELD_NUMBER: _ClassVar[int]
    status: QuestionsStatus
    questions: _containers.RepeatedCompositeFieldContainer[QuestionSpec]
    answers: _containers.RepeatedCompositeFieldContainer[QuestionAnswer]
    answered_count: int

    def __init__(self, status: _Optional[_Union[QuestionsStatus, str]]=..., questions: _Optional[_Iterable[_Union[QuestionSpec, _Mapping]]]=..., answers: _Optional[_Iterable[_Union[QuestionAnswer, _Mapping]]]=..., answered_count: _Optional[int]=...) -> None:
        ...

class Citation(_message.Message):
    __slots__ = ('id', 'claim', 'source_cell_id', 'source_ref', 'source_locator', 'anchor', 'quoted_text', 'rationale', 'lineage')
    ID_FIELD_NUMBER: _ClassVar[int]
    CLAIM_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CELL_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_REF_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_FIELD_NUMBER: _ClassVar[int]
    QUOTED_TEXT_FIELD_NUMBER: _ClassVar[int]
    RATIONALE_FIELD_NUMBER: _ClassVar[int]
    LINEAGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    claim: str
    source_cell_id: str
    source_ref: str
    source_locator: str
    anchor: str
    quoted_text: str
    rationale: str
    lineage: _containers.RepeatedCompositeFieldContainer[CitationLineageNode]

    def __init__(self, id: _Optional[str]=..., claim: _Optional[str]=..., source_cell_id: _Optional[str]=..., source_ref: _Optional[str]=..., source_locator: _Optional[str]=..., anchor: _Optional[str]=..., quoted_text: _Optional[str]=..., rationale: _Optional[str]=..., lineage: _Optional[_Iterable[_Union[CitationLineageNode, _Mapping]]]=...) -> None:
        ...

class CitationLineageNode(_message.Message):
    __slots__ = ('cell_id', 'kind', 'dataframe_name', 'connector_id', 'tables', 'input_cell_ids')
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    DATAFRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    TABLES_FIELD_NUMBER: _ClassVar[int]
    INPUT_CELL_IDS_FIELD_NUMBER: _ClassVar[int]
    cell_id: str
    kind: str
    dataframe_name: str
    connector_id: int
    tables: _containers.RepeatedScalarFieldContainer[str]
    input_cell_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, cell_id: _Optional[str]=..., kind: _Optional[str]=..., dataframe_name: _Optional[str]=..., connector_id: _Optional[int]=..., tables: _Optional[_Iterable[str]]=..., input_cell_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class AppCell(_message.Message):
    __slots__ = ('action', 'app_id', 'name', 'error_message', 'screenshot_url', 'last_run_at', 'build_line_count', 'build_file_count')
    ACTION_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SCREENSHOT_URL_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_AT_FIELD_NUMBER: _ClassVar[int]
    BUILD_LINE_COUNT_FIELD_NUMBER: _ClassVar[int]
    BUILD_FILE_COUNT_FIELD_NUMBER: _ClassVar[int]
    action: str
    app_id: str
    name: str
    error_message: str
    screenshot_url: str
    last_run_at: str
    build_line_count: int
    build_file_count: int

    def __init__(self, action: _Optional[str]=..., app_id: _Optional[str]=..., name: _Optional[str]=..., error_message: _Optional[str]=..., screenshot_url: _Optional[str]=..., last_run_at: _Optional[str]=..., build_line_count: _Optional[int]=..., build_file_count: _Optional[int]=...) -> None:
        ...

class AppInfo(_message.Message):
    __slots__ = ('id', 'name', 'description', 'status', 'creator_id', 'created_at', 'updated_at', 'refreshed_at', 'published_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATOR_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    REFRESHED_AT_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    status: str
    creator_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    refreshed_at: _timestamp_pb2.Timestamp
    published_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., description: _Optional[str]=..., status: _Optional[str]=..., creator_id: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., refreshed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., published_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListAppsCell(_message.Message):
    __slots__ = ('search_term', 'app_id', 'total_count', 'error_message', 'apps')
    SEARCH_TERM_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    APPS_FIELD_NUMBER: _ClassVar[int]
    search_term: str
    app_id: str
    total_count: int
    error_message: str
    apps: _containers.RepeatedCompositeFieldContainer[AppInfo]

    def __init__(self, search_term: _Optional[str]=..., app_id: _Optional[str]=..., total_count: _Optional[int]=..., error_message: _Optional[str]=..., apps: _Optional[_Iterable[_Union[AppInfo, _Mapping]]]=...) -> None:
        ...