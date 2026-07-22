from google.api import visibility_pb2 as _visibility_pb2
import paradigm_params_pb2 as _paradigm_params_pb2
import powerbi_selection_pb2 as _powerbi_selection_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Paradigm(_message.Message):
    __slots__ = ('type', 'version', 'options')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    type: _paradigm_params_pb2.ParadigmType
    version: int
    options: ParadigmOptions

    def __init__(self, type: _Optional[_Union[_paradigm_params_pb2.ParadigmType, str]]=..., version: _Optional[int]=..., options: _Optional[_Union[ParadigmOptions, _Mapping]]=...) -> None:
        ...

class ParadigmOptions(_message.Message):
    __slots__ = ('sql', 'research', 'ontology', 'basic', 'tableau', 'experimental', 'universal', 'public_demo', 'template')
    SQL_FIELD_NUMBER: _ClassVar[int]
    RESEARCH_FIELD_NUMBER: _ClassVar[int]
    ONTOLOGY_FIELD_NUMBER: _ClassVar[int]
    BASIC_FIELD_NUMBER: _ClassVar[int]
    TABLEAU_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENTAL_FIELD_NUMBER: _ClassVar[int]
    UNIVERSAL_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_DEMO_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    sql: SqlOptions
    research: ResearchOptions
    ontology: OntologyOptions
    basic: BasicOptions
    tableau: TableauOptions
    experimental: ExperimentalOptions
    universal: UniversalOptions
    public_demo: PublicDemoOptions
    template: TemplateOptions

    def __init__(self, sql: _Optional[_Union[SqlOptions, _Mapping]]=..., research: _Optional[_Union[ResearchOptions, _Mapping]]=..., ontology: _Optional[_Union[OntologyOptions, _Mapping]]=..., basic: _Optional[_Union[BasicOptions, _Mapping]]=..., tableau: _Optional[_Union[TableauOptions, _Mapping]]=..., experimental: _Optional[_Union[ExperimentalOptions, _Mapping]]=..., universal: _Optional[_Union[UniversalOptions, _Mapping]]=..., public_demo: _Optional[_Union[PublicDemoOptions, _Mapping]]=..., template: _Optional[_Union[TemplateOptions, _Mapping]]=...) -> None:
        ...

class SqlOptions(_message.Message):
    __slots__ = ('connector_ids',)
    CONNECTOR_IDS_FIELD_NUMBER: _ClassVar[int]
    connector_ids: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, connector_ids: _Optional[_Iterable[int]]=...) -> None:
        ...

class ResearchOptions(_message.Message):
    __slots__ = ('connector_ids', 'background_color', 'logo')
    CONNECTOR_IDS_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    connector_ids: _containers.RepeatedScalarFieldContainer[int]
    background_color: str
    logo: str

    def __init__(self, connector_ids: _Optional[_Iterable[int]]=..., background_color: _Optional[str]=..., logo: _Optional[str]=...) -> None:
        ...

class ExperimentalOptions(_message.Message):
    __slots__ = ('connector_ids', 'auto_approve_enabled')
    CONNECTOR_IDS_FIELD_NUMBER: _ClassVar[int]
    AUTO_APPROVE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    connector_ids: _containers.RepeatedScalarFieldContainer[int]
    auto_approve_enabled: bool

    def __init__(self, connector_ids: _Optional[_Iterable[int]]=..., auto_approve_enabled: bool=...) -> None:
        ...

class BasicOptions(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class OntologyOptions(_message.Message):
    __slots__ = ('connector_ids', 'ontology_ids')
    CONNECTOR_IDS_FIELD_NUMBER: _ClassVar[int]
    ONTOLOGY_IDS_FIELD_NUMBER: _ClassVar[int]
    connector_ids: _containers.RepeatedScalarFieldContainer[int]
    ontology_ids: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, connector_ids: _Optional[_Iterable[int]]=..., ontology_ids: _Optional[_Iterable[int]]=...) -> None:
        ...

class TableauOptions(_message.Message):
    __slots__ = ('dataset_id',)
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str

    def __init__(self, dataset_id: _Optional[str]=...) -> None:
        ...

class UniversalOptions(_message.Message):
    __slots__ = ('connector_ids', 'dataset_id', 'web_search_enabled', 'sql_enabled', 'ontology_enabled', 'ontology_editing_enabled', 'python_enabled', 'auto_approve_enabled', 'google_drive_enabled', 'powerbi_enabled', 'context_editing_enabled', 'form_editor_enabled', 'playbook_tools_enabled', 'microsoft365_enabled', 'feed_explorer_enabled', 'bash_enabled', 'javascript_enabled', 'feed_post_enabled', 'feed_comment_enabled', 'feed_engage_enabled', 'streamlit_enabled', 'compaction_disabled', 'gmail_enabled', 'chat_history_search_enabled', 'google_calendar_enabled', 'email_output_enabled', 'powerbi_selections', 'sms_mode', 'api_access_key_ids')
    CONNECTOR_IDS_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    WEB_SEARCH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SQL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ONTOLOGY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ONTOLOGY_EDITING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PYTHON_ENABLED_FIELD_NUMBER: _ClassVar[int]
    AUTO_APPROVE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_DRIVE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    POWERBI_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_EDITING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FORM_EDITOR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOK_TOOLS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MICROSOFT365_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FEED_EXPLORER_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BASH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    JAVASCRIPT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FEED_POST_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FEED_COMMENT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FEED_ENGAGE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    STREAMLIT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    COMPACTION_DISABLED_FIELD_NUMBER: _ClassVar[int]
    GMAIL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CHAT_HISTORY_SEARCH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_CALENDAR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    EMAIL_OUTPUT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    POWERBI_SELECTIONS_FIELD_NUMBER: _ClassVar[int]
    SMS_MODE_FIELD_NUMBER: _ClassVar[int]
    API_ACCESS_KEY_IDS_FIELD_NUMBER: _ClassVar[int]
    connector_ids: _containers.RepeatedScalarFieldContainer[int]
    dataset_id: str
    web_search_enabled: bool
    sql_enabled: bool
    ontology_enabled: bool
    ontology_editing_enabled: bool
    python_enabled: bool
    auto_approve_enabled: bool
    google_drive_enabled: bool
    powerbi_enabled: bool
    context_editing_enabled: bool
    form_editor_enabled: bool
    playbook_tools_enabled: bool
    microsoft365_enabled: bool
    feed_explorer_enabled: bool
    bash_enabled: bool
    javascript_enabled: bool
    feed_post_enabled: bool
    feed_comment_enabled: bool
    feed_engage_enabled: bool
    streamlit_enabled: bool
    compaction_disabled: bool
    gmail_enabled: bool
    chat_history_search_enabled: bool
    google_calendar_enabled: bool
    email_output_enabled: bool
    powerbi_selections: _containers.RepeatedCompositeFieldContainer[_powerbi_selection_pb2.PowerBISelection]
    sms_mode: bool
    api_access_key_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, connector_ids: _Optional[_Iterable[int]]=..., dataset_id: _Optional[str]=..., web_search_enabled: bool=..., sql_enabled: bool=..., ontology_enabled: bool=..., ontology_editing_enabled: bool=..., python_enabled: bool=..., auto_approve_enabled: bool=..., google_drive_enabled: bool=..., powerbi_enabled: bool=..., context_editing_enabled: bool=..., form_editor_enabled: bool=..., playbook_tools_enabled: bool=..., microsoft365_enabled: bool=..., feed_explorer_enabled: bool=..., bash_enabled: bool=..., javascript_enabled: bool=..., feed_post_enabled: bool=..., feed_comment_enabled: bool=..., feed_engage_enabled: bool=..., streamlit_enabled: bool=..., compaction_disabled: bool=..., gmail_enabled: bool=..., chat_history_search_enabled: bool=..., google_calendar_enabled: bool=..., email_output_enabled: bool=..., powerbi_selections: _Optional[_Iterable[_Union[_powerbi_selection_pb2.PowerBISelection, _Mapping]]]=..., sms_mode: bool=..., api_access_key_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class GoogleDriveOptions(_message.Message):
    __slots__ = ('connector_id',)
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    connector_id: int

    def __init__(self, connector_id: _Optional[int]=...) -> None:
        ...

class PublicDemoOptions(_message.Message):
    __slots__ = ('connector_id',)
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    connector_id: int

    def __init__(self, connector_id: _Optional[int]=...) -> None:
        ...

class TemplateOptions(_message.Message):
    __slots__ = ('capture_tools',)
    CAPTURE_TOOLS_FIELD_NUMBER: _ClassVar[int]
    capture_tools: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, capture_tools: _Optional[_Iterable[str]]=...) -> None:
        ...