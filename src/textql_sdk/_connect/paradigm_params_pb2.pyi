# pylint: skip-file
# mypy: ignore-errors
# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
from .google.api import visibility_pb2 as _visibility_pb2
from . import powerbi_selection_pb2 as _powerbi_selection_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ParadigmType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TYPE_UNKNOWN: _ClassVar[ParadigmType]
    TYPE_SQL: _ClassVar[ParadigmType]
    TYPE_RESEARCH: _ClassVar[ParadigmType]
    TYPE_ONTOLOGY: _ClassVar[ParadigmType]
    TYPE_BASIC: _ClassVar[ParadigmType]
    TYPE_TABLEAU: _ClassVar[ParadigmType]
    TYPE_EXPERIMENTAL: _ClassVar[ParadigmType]
    TYPE_UNIVERSAL: _ClassVar[ParadigmType]
    TYPE_PUBLIC_DEMO: _ClassVar[ParadigmType]
    TYPE_SUMMARY: _ClassVar[ParadigmType]
    TYPE_OBSERVABILITY: _ClassVar[ParadigmType]
    TYPE_TEMPLATE: _ClassVar[ParadigmType]
    TYPE_MINIMALIST: _ClassVar[ParadigmType]
    TYPE_TOPICS: _ClassVar[ParadigmType]
TYPE_UNKNOWN: ParadigmType
TYPE_SQL: ParadigmType
TYPE_RESEARCH: ParadigmType
TYPE_ONTOLOGY: ParadigmType
TYPE_BASIC: ParadigmType
TYPE_TABLEAU: ParadigmType
TYPE_EXPERIMENTAL: ParadigmType
TYPE_UNIVERSAL: ParadigmType
TYPE_PUBLIC_DEMO: ParadigmType
TYPE_SUMMARY: ParadigmType
TYPE_OBSERVABILITY: ParadigmType
TYPE_TEMPLATE: ParadigmType
TYPE_MINIMALIST: ParadigmType
TYPE_TOPICS: ParadigmType

class ParadigmParams(_message.Message):
    __slots__ = ('web_search_enabled', 'sql_enabled', 'ontology_enabled', 'ontology_editing_enabled', 'python_enabled', 'powerbi_enabled', 'google_drive_enabled', 'auto_approve_enabled', 'context_editing_enabled', 'form_editor_enabled', 'tableau_enabled', 'file_upload_enabled', 'multiple_connector_mode', 'playbook_tools_enabled', 'microsoft_365_enabled', 'bash_enabled', 'javascript_enabled', 'model_switching_enabled', 'feed_explorer_enabled', 'feed_post_enabled', 'feed_comment_enabled', 'feed_engage_enabled', 'compaction_disabled', 'gmail_enabled', 'chat_history_search_enabled', 'google_calendar_enabled', 'parallel_tools_enabled', 'email_output_enabled', 'questions_tool_enabled', 'powerbi_selections', 'dataset_id')
    WEB_SEARCH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SQL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ONTOLOGY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ONTOLOGY_EDITING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PYTHON_ENABLED_FIELD_NUMBER: _ClassVar[int]
    POWERBI_ENABLED_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_DRIVE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    AUTO_APPROVE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_EDITING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FORM_EDITOR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TABLEAU_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FILE_UPLOAD_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MULTIPLE_CONNECTOR_MODE_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOK_TOOLS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MICROSOFT_365_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BASH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    JAVASCRIPT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MODEL_SWITCHING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FEED_EXPLORER_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FEED_POST_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FEED_COMMENT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FEED_ENGAGE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    COMPACTION_DISABLED_FIELD_NUMBER: _ClassVar[int]
    GMAIL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CHAT_HISTORY_SEARCH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_CALENDAR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_TOOLS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    EMAIL_OUTPUT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    QUESTIONS_TOOL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    POWERBI_SELECTIONS_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    web_search_enabled: bool
    sql_enabled: bool
    ontology_enabled: bool
    ontology_editing_enabled: bool
    python_enabled: bool
    powerbi_enabled: bool
    google_drive_enabled: bool
    auto_approve_enabled: bool
    context_editing_enabled: bool
    form_editor_enabled: bool
    tableau_enabled: bool
    file_upload_enabled: bool
    multiple_connector_mode: bool
    playbook_tools_enabled: bool
    microsoft_365_enabled: bool
    bash_enabled: bool
    javascript_enabled: bool
    model_switching_enabled: bool
    feed_explorer_enabled: bool
    feed_post_enabled: bool
    feed_comment_enabled: bool
    feed_engage_enabled: bool
    compaction_disabled: bool
    gmail_enabled: bool
    chat_history_search_enabled: bool
    google_calendar_enabled: bool
    parallel_tools_enabled: bool
    email_output_enabled: bool
    questions_tool_enabled: bool
    powerbi_selections: _containers.RepeatedCompositeFieldContainer[_powerbi_selection_pb2.PowerBISelection]
    dataset_id: str

    def __init__(self, web_search_enabled: bool=..., sql_enabled: bool=..., ontology_enabled: bool=..., ontology_editing_enabled: bool=..., python_enabled: bool=..., powerbi_enabled: bool=..., google_drive_enabled: bool=..., auto_approve_enabled: bool=..., context_editing_enabled: bool=..., form_editor_enabled: bool=..., tableau_enabled: bool=..., file_upload_enabled: bool=..., multiple_connector_mode: bool=..., playbook_tools_enabled: bool=..., microsoft_365_enabled: bool=..., bash_enabled: bool=..., javascript_enabled: bool=..., model_switching_enabled: bool=..., feed_explorer_enabled: bool=..., feed_post_enabled: bool=..., feed_comment_enabled: bool=..., feed_engage_enabled: bool=..., compaction_disabled: bool=..., gmail_enabled: bool=..., chat_history_search_enabled: bool=..., google_calendar_enabled: bool=..., parallel_tools_enabled: bool=..., email_output_enabled: bool=..., questions_tool_enabled: bool=..., powerbi_selections: _Optional[_Iterable[_Union[_powerbi_selection_pb2.PowerBISelection, _Mapping]]]=..., dataset_id: _Optional[str]=...) -> None:
        ...