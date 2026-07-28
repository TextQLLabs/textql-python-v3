# pylint: skip-file
# mypy: ignore-errors
# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
import datetime
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from .. import paradigm_params_pb2 as _paradigm_params_pb2
from ..public import cells_pb2 as _cells_pb2
from ..public import common_pb2 as _common_pb2
from ..public import config_source_pb2 as _config_source_pb2
from ..public import dashboard_pb2 as _dashboard_pb2
from ..public import dataset_pb2 as _dataset_pb2
from ..public import identity_pb2 as _identity_pb2
from ..public import llm_model_pb2 as _llm_model_pb2
from ..public import paradigm_pb2 as _paradigm_pb2
from ..public import report_pb2 as _report_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PlaybookStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATUS_UNKNOWN: _ClassVar[PlaybookStatus]
    STATUS_ACTIVE: _ClassVar[PlaybookStatus]
    STATUS_INACTIVE: _ClassVar[PlaybookStatus]
    STATUS_EMPTY: _ClassVar[PlaybookStatus]
    ALL_PLAYBOOKS: _ClassVar[PlaybookStatus]

class TemplateDataExecutionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXECUTION_STATUS_UNKNOWN: _ClassVar[TemplateDataExecutionStatus]
    EXECUTION_STATUS_IDLE: _ClassVar[TemplateDataExecutionStatus]
    EXECUTION_STATUS_QUEUED: _ClassVar[TemplateDataExecutionStatus]
    EXECUTION_STATUS_RUNNING: _ClassVar[TemplateDataExecutionStatus]
    EXECUTION_STATUS_COMPLETED: _ClassVar[TemplateDataExecutionStatus]
    EXECUTION_STATUS_FAILED: _ClassVar[TemplateDataExecutionStatus]
    EXECUTION_STATUS_CANCELLED: _ClassVar[TemplateDataExecutionStatus]

class PlaybookTriggerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRIGGER_TYPE_UNKNOWN: _ClassVar[PlaybookTriggerType]
    TRIGGER_TYPE_CRON: _ClassVar[PlaybookTriggerType]
    TRIGGER_TYPE_WEBHOOK: _ClassVar[PlaybookTriggerType]

class PlaybookSortField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SORT_FIELD_UNKNOWN: _ClassVar[PlaybookSortField]
    SORT_FIELD_NAME: _ClassVar[PlaybookSortField]
    SORT_FIELD_CREATED_AT: _ClassVar[PlaybookSortField]
    SORT_FIELD_UPDATED_AT: _ClassVar[PlaybookSortField]
    SORT_FIELD_SCHEDULE: _ClassVar[PlaybookSortField]

class PlaybookReportStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPORT_STYLE_UNKNOWN: _ClassVar[PlaybookReportStyle]
    EXECUTIVE_REPORT: _ClassVar[PlaybookReportStyle]
    VERBOSE: _ClassVar[PlaybookReportStyle]
    CONCISE: _ClassVar[PlaybookReportStyle]

class ChatAccessMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHAT_ACCESS_MODE_INHERIT: _ClassVar[ChatAccessMode]
    CHAT_ACCESS_MODE_CUSTOM: _ClassVar[ChatAccessMode]
STATUS_UNKNOWN: PlaybookStatus
STATUS_ACTIVE: PlaybookStatus
STATUS_INACTIVE: PlaybookStatus
STATUS_EMPTY: PlaybookStatus
ALL_PLAYBOOKS: PlaybookStatus
EXECUTION_STATUS_UNKNOWN: TemplateDataExecutionStatus
EXECUTION_STATUS_IDLE: TemplateDataExecutionStatus
EXECUTION_STATUS_QUEUED: TemplateDataExecutionStatus
EXECUTION_STATUS_RUNNING: TemplateDataExecutionStatus
EXECUTION_STATUS_COMPLETED: TemplateDataExecutionStatus
EXECUTION_STATUS_FAILED: TemplateDataExecutionStatus
EXECUTION_STATUS_CANCELLED: TemplateDataExecutionStatus
TRIGGER_TYPE_UNKNOWN: PlaybookTriggerType
TRIGGER_TYPE_CRON: PlaybookTriggerType
TRIGGER_TYPE_WEBHOOK: PlaybookTriggerType
SORT_FIELD_UNKNOWN: PlaybookSortField
SORT_FIELD_NAME: PlaybookSortField
SORT_FIELD_CREATED_AT: PlaybookSortField
SORT_FIELD_UPDATED_AT: PlaybookSortField
SORT_FIELD_SCHEDULE: PlaybookSortField
REPORT_STYLE_UNKNOWN: PlaybookReportStyle
EXECUTIVE_REPORT: PlaybookReportStyle
VERBOSE: PlaybookReportStyle
CONCISE: PlaybookReportStyle
CHAT_ACCESS_MODE_INHERIT: ChatAccessMode
CHAT_ACCESS_MODE_CUSTOM: ChatAccessMode

class ChatAccessOverride(_message.Message):
    __slots__ = ('member_id', 'role_id', 'access_type')
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    role_id: str
    access_type: str

    def __init__(self, member_id: _Optional[str]=..., role_id: _Optional[str]=..., access_type: _Optional[str]=...) -> None:
        ...

class ChatAccessOverrideList(_message.Message):
    __slots__ = ('items',)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ChatAccessOverride]

    def __init__(self, items: _Optional[_Iterable[_Union[ChatAccessOverride, _Mapping]]]=...) -> None:
        ...

class FilterCondition(_message.Message):
    __slots__ = ('field', 'operator', 'value')
    FIELD_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    field: str
    operator: str
    value: str

    def __init__(self, field: _Optional[str]=..., operator: _Optional[str]=..., value: _Optional[str]=...) -> None:
        ...

class Playbook(_message.Message):
    __slots__ = ('id', 'org_id', 'member_id', 'connector_id', 'name', 'prompt', 'created_at', 'updated_at', 'status', 'trigger_type', 'cron_string', 'dataset_ids', 'reference_report_id', 'latest_chat_id', 'email_addresses', 'slack_channel_id', 'tagged_slack_user_ids', 'llm_model', 'paradigm_options', 'paradigm_type', 'is_running', 'owner', 'has_write_permission', 'is_subscribed', 'report_output_style', 'template_header_id', 'selected_template_data_ids', 'max_concurrent_templates', 'auto_optimize_concurrency', 'connector_ids', 'template_data_filters', 'parent_playbook_id', 'origin_playbook_id', 'duplicated_by_member_id', 'duplicated_at', 'chat_access_mode', 'chat_access_overrides', 'chat_is_public', 'dashboard_ids', 'recipient_email_column', 'teams_channel_id', 'tagged_teams_user_aad_ids', 'config_source', 'api_access_key_ids')
    ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_TYPE_FIELD_NUMBER: _ClassVar[int]
    CRON_STRING_FIELD_NUMBER: _ClassVar[int]
    DATASET_IDS_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_REPORT_ID_FIELD_NUMBER: _ClassVar[int]
    LATEST_CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    SLACK_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TAGGED_SLACK_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    LLM_MODEL_FIELD_NUMBER: _ClassVar[int]
    PARADIGM_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PARADIGM_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_RUNNING_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    HAS_WRITE_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    IS_SUBSCRIBED_FIELD_NUMBER: _ClassVar[int]
    REPORT_OUTPUT_STYLE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_HEADER_ID_FIELD_NUMBER: _ClassVar[int]
    SELECTED_TEMPLATE_DATA_IDS_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    AUTO_OPTIMIZE_CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_IDS_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_DATA_FILTERS_FIELD_NUMBER: _ClassVar[int]
    PARENT_PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    DUPLICATED_BY_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    DUPLICATED_AT_FIELD_NUMBER: _ClassVar[int]
    CHAT_ACCESS_MODE_FIELD_NUMBER: _ClassVar[int]
    CHAT_ACCESS_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    CHAT_IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_IDS_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_EMAIL_COLUMN_FIELD_NUMBER: _ClassVar[int]
    TEAMS_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TAGGED_TEAMS_USER_AAD_IDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_SOURCE_FIELD_NUMBER: _ClassVar[int]
    API_ACCESS_KEY_IDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    org_id: str
    member_id: str
    connector_id: int
    name: str
    prompt: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    status: PlaybookStatus
    trigger_type: PlaybookTriggerType
    cron_string: str
    dataset_ids: _containers.RepeatedScalarFieldContainer[str]
    reference_report_id: str
    latest_chat_id: str
    email_addresses: _containers.RepeatedScalarFieldContainer[str]
    slack_channel_id: str
    tagged_slack_user_ids: _containers.RepeatedScalarFieldContainer[str]
    llm_model: _llm_model_pb2.LlmModel
    paradigm_options: _paradigm_pb2.ParadigmOptions
    paradigm_type: _paradigm_params_pb2.ParadigmType
    is_running: bool
    owner: _identity_pb2.MemberPreview
    has_write_permission: bool
    is_subscribed: bool
    report_output_style: PlaybookReportStyle
    template_header_id: str
    selected_template_data_ids: _containers.RepeatedScalarFieldContainer[str]
    max_concurrent_templates: int
    auto_optimize_concurrency: bool
    connector_ids: _containers.RepeatedScalarFieldContainer[int]
    template_data_filters: _containers.RepeatedCompositeFieldContainer[FilterCondition]
    parent_playbook_id: str
    origin_playbook_id: str
    duplicated_by_member_id: str
    duplicated_at: _timestamp_pb2.Timestamp
    chat_access_mode: ChatAccessMode
    chat_access_overrides: _containers.RepeatedCompositeFieldContainer[ChatAccessOverride]
    chat_is_public: bool
    dashboard_ids: _containers.RepeatedScalarFieldContainer[str]
    recipient_email_column: str
    teams_channel_id: str
    tagged_teams_user_aad_ids: _containers.RepeatedScalarFieldContainer[str]
    config_source: _config_source_pb2.ConfigSource
    api_access_key_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, id: _Optional[str]=..., org_id: _Optional[str]=..., member_id: _Optional[str]=..., connector_id: _Optional[int]=..., name: _Optional[str]=..., prompt: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., status: _Optional[_Union[PlaybookStatus, str]]=..., trigger_type: _Optional[_Union[PlaybookTriggerType, str]]=..., cron_string: _Optional[str]=..., dataset_ids: _Optional[_Iterable[str]]=..., reference_report_id: _Optional[str]=..., latest_chat_id: _Optional[str]=..., email_addresses: _Optional[_Iterable[str]]=..., slack_channel_id: _Optional[str]=..., tagged_slack_user_ids: _Optional[_Iterable[str]]=..., llm_model: _Optional[_Union[_llm_model_pb2.LlmModel, str]]=..., paradigm_options: _Optional[_Union[_paradigm_pb2.ParadigmOptions, _Mapping]]=..., paradigm_type: _Optional[_Union[_paradigm_params_pb2.ParadigmType, str]]=..., is_running: bool=..., owner: _Optional[_Union[_identity_pb2.MemberPreview, _Mapping]]=..., has_write_permission: bool=..., is_subscribed: bool=..., report_output_style: _Optional[_Union[PlaybookReportStyle, str]]=..., template_header_id: _Optional[str]=..., selected_template_data_ids: _Optional[_Iterable[str]]=..., max_concurrent_templates: _Optional[int]=..., auto_optimize_concurrency: bool=..., connector_ids: _Optional[_Iterable[int]]=..., template_data_filters: _Optional[_Iterable[_Union[FilterCondition, _Mapping]]]=..., parent_playbook_id: _Optional[str]=..., origin_playbook_id: _Optional[str]=..., duplicated_by_member_id: _Optional[str]=..., duplicated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., chat_access_mode: _Optional[_Union[ChatAccessMode, str]]=..., chat_access_overrides: _Optional[_Iterable[_Union[ChatAccessOverride, _Mapping]]]=..., chat_is_public: bool=..., dashboard_ids: _Optional[_Iterable[str]]=..., recipient_email_column: _Optional[str]=..., teams_channel_id: _Optional[str]=..., tagged_teams_user_aad_ids: _Optional[_Iterable[str]]=..., config_source: _Optional[_Union[_config_source_pb2.ConfigSource, _Mapping]]=..., api_access_key_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreatePlaybookRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CreatePlaybookResponse(_message.Message):
    __slots__ = ('playbook',)
    PLAYBOOK_FIELD_NUMBER: _ClassVar[int]
    playbook: Playbook

    def __init__(self, playbook: _Optional[_Union[Playbook, _Mapping]]=...) -> None:
        ...

class GetPlaybookRequest(_message.Message):
    __slots__ = ('playbook_id', 'limit', 'offset')
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str
    limit: int
    offset: int

    def __init__(self, playbook_id: _Optional[str]=..., limit: _Optional[int]=..., offset: _Optional[int]=...) -> None:
        ...

class GetPlaybookResponse(_message.Message):
    __slots__ = ('playbook', 'reports', 'total_reports_count')
    PLAYBOOK_FIELD_NUMBER: _ClassVar[int]
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_REPORTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    playbook: Playbook
    reports: _containers.RepeatedCompositeFieldContainer[PlaybookReport]
    total_reports_count: int

    def __init__(self, playbook: _Optional[_Union[Playbook, _Mapping]]=..., reports: _Optional[_Iterable[_Union[PlaybookReport, _Mapping]]]=..., total_reports_count: _Optional[int]=...) -> None:
        ...

class GetPlaybooksRequest(_message.Message):
    __slots__ = ('member_only', 'limit', 'offset', 'search_term', 'status_filter', 'creator_member_id', 'sort_by', 'sort_direction', 'subscribed_first', 'only_subscribed', 'shared_with_me', 'include_shared_drafts', 'statuses', 'creator_member_ids')
    MEMBER_ONLY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SEARCH_TERM_FIELD_NUMBER: _ClassVar[int]
    STATUS_FILTER_FIELD_NUMBER: _ClassVar[int]
    CREATOR_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    SORT_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBED_FIRST_FIELD_NUMBER: _ClassVar[int]
    ONLY_SUBSCRIBED_FIELD_NUMBER: _ClassVar[int]
    SHARED_WITH_ME_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SHARED_DRAFTS_FIELD_NUMBER: _ClassVar[int]
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    CREATOR_MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    member_only: bool
    limit: int
    offset: int
    search_term: str
    status_filter: PlaybookStatus
    creator_member_id: str
    sort_by: PlaybookSortField
    sort_direction: _common_pb2.SortDirection
    subscribed_first: bool
    only_subscribed: bool
    shared_with_me: bool
    include_shared_drafts: bool
    statuses: _containers.RepeatedScalarFieldContainer[PlaybookStatus]
    creator_member_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, member_only: bool=..., limit: _Optional[int]=..., offset: _Optional[int]=..., search_term: _Optional[str]=..., status_filter: _Optional[_Union[PlaybookStatus, str]]=..., creator_member_id: _Optional[str]=..., sort_by: _Optional[_Union[PlaybookSortField, str]]=..., sort_direction: _Optional[_Union[_common_pb2.SortDirection, str]]=..., subscribed_first: bool=..., only_subscribed: bool=..., shared_with_me: bool=..., include_shared_drafts: bool=..., statuses: _Optional[_Iterable[_Union[PlaybookStatus, str]]]=..., creator_member_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetPlaybooksResponse(_message.Message):
    __slots__ = ('playbooks', 'total_count')
    PLAYBOOKS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    playbooks: _containers.RepeatedCompositeFieldContainer[Playbook]
    total_count: int

    def __init__(self, playbooks: _Optional[_Iterable[_Union[Playbook, _Mapping]]]=..., total_count: _Optional[int]=...) -> None:
        ...

class StringList(_message.Message):
    __slots__ = ('items',)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, items: _Optional[_Iterable[str]]=...) -> None:
        ...

class Int32List(_message.Message):
    __slots__ = ('items',)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, items: _Optional[_Iterable[int]]=...) -> None:
        ...

class FilterConditionList(_message.Message):
    __slots__ = ('items',)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[FilterCondition]

    def __init__(self, items: _Optional[_Iterable[_Union[FilterCondition, _Mapping]]]=...) -> None:
        ...

class UpdatePlaybookRequest(_message.Message):
    __slots__ = ('playbook_id', 'name', 'prompt', 'status', 'trigger_type', 'cron_string', 'dataset_ids', 'connector_id', 'reference_report_id', 'paradigm_options', 'paradigm_type', 'email_addresses', 'slack_channel_id', 'tagged_slack_user_ids', 'report_output_style', 'template_header_id', 'selected_template_data_ids', 'max_concurrent_templates', 'auto_optimize_concurrency', 'connector_ids', 'template_data_filters', 'llm_model', 'chat_access_mode', 'chat_access_overrides', 'chat_is_public', 'dashboard_ids', 'recipient_email_column', 'teams_channel_id', 'tagged_teams_user_aad_ids', 'api_access_key_ids')
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_TYPE_FIELD_NUMBER: _ClassVar[int]
    CRON_STRING_FIELD_NUMBER: _ClassVar[int]
    DATASET_IDS_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_REPORT_ID_FIELD_NUMBER: _ClassVar[int]
    PARADIGM_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PARADIGM_TYPE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    SLACK_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TAGGED_SLACK_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    REPORT_OUTPUT_STYLE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_HEADER_ID_FIELD_NUMBER: _ClassVar[int]
    SELECTED_TEMPLATE_DATA_IDS_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    AUTO_OPTIMIZE_CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_IDS_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_DATA_FILTERS_FIELD_NUMBER: _ClassVar[int]
    LLM_MODEL_FIELD_NUMBER: _ClassVar[int]
    CHAT_ACCESS_MODE_FIELD_NUMBER: _ClassVar[int]
    CHAT_ACCESS_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    CHAT_IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_IDS_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_EMAIL_COLUMN_FIELD_NUMBER: _ClassVar[int]
    TEAMS_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TAGGED_TEAMS_USER_AAD_IDS_FIELD_NUMBER: _ClassVar[int]
    API_ACCESS_KEY_IDS_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str
    name: str
    prompt: str
    status: PlaybookStatus
    trigger_type: PlaybookTriggerType
    cron_string: str
    dataset_ids: StringList
    connector_id: int
    reference_report_id: str
    paradigm_options: _paradigm_pb2.ParadigmOptions
    paradigm_type: _paradigm_params_pb2.ParadigmType
    email_addresses: StringList
    slack_channel_id: str
    tagged_slack_user_ids: StringList
    report_output_style: PlaybookReportStyle
    template_header_id: str
    selected_template_data_ids: StringList
    max_concurrent_templates: int
    auto_optimize_concurrency: bool
    connector_ids: Int32List
    template_data_filters: FilterConditionList
    llm_model: _llm_model_pb2.LlmModel
    chat_access_mode: ChatAccessMode
    chat_access_overrides: ChatAccessOverrideList
    chat_is_public: bool
    dashboard_ids: StringList
    recipient_email_column: str
    teams_channel_id: str
    tagged_teams_user_aad_ids: StringList
    api_access_key_ids: StringList

    def __init__(self, playbook_id: _Optional[str]=..., name: _Optional[str]=..., prompt: _Optional[str]=..., status: _Optional[_Union[PlaybookStatus, str]]=..., trigger_type: _Optional[_Union[PlaybookTriggerType, str]]=..., cron_string: _Optional[str]=..., dataset_ids: _Optional[_Union[StringList, _Mapping]]=..., connector_id: _Optional[int]=..., reference_report_id: _Optional[str]=..., paradigm_options: _Optional[_Union[_paradigm_pb2.ParadigmOptions, _Mapping]]=..., paradigm_type: _Optional[_Union[_paradigm_params_pb2.ParadigmType, str]]=..., email_addresses: _Optional[_Union[StringList, _Mapping]]=..., slack_channel_id: _Optional[str]=..., tagged_slack_user_ids: _Optional[_Union[StringList, _Mapping]]=..., report_output_style: _Optional[_Union[PlaybookReportStyle, str]]=..., template_header_id: _Optional[str]=..., selected_template_data_ids: _Optional[_Union[StringList, _Mapping]]=..., max_concurrent_templates: _Optional[int]=..., auto_optimize_concurrency: bool=..., connector_ids: _Optional[_Union[Int32List, _Mapping]]=..., template_data_filters: _Optional[_Union[FilterConditionList, _Mapping]]=..., llm_model: _Optional[_Union[_llm_model_pb2.LlmModel, str]]=..., chat_access_mode: _Optional[_Union[ChatAccessMode, str]]=..., chat_access_overrides: _Optional[_Union[ChatAccessOverrideList, _Mapping]]=..., chat_is_public: bool=..., dashboard_ids: _Optional[_Union[StringList, _Mapping]]=..., recipient_email_column: _Optional[str]=..., teams_channel_id: _Optional[str]=..., tagged_teams_user_aad_ids: _Optional[_Union[StringList, _Mapping]]=..., api_access_key_ids: _Optional[_Union[StringList, _Mapping]]=...) -> None:
        ...

class UpdatePlaybookResponse(_message.Message):
    __slots__ = ('playbook',)
    PLAYBOOK_FIELD_NUMBER: _ClassVar[int]
    playbook: Playbook

    def __init__(self, playbook: _Optional[_Union[Playbook, _Mapping]]=...) -> None:
        ...

class DeletePlaybookRequest(_message.Message):
    __slots__ = ('playbook_id',)
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str

    def __init__(self, playbook_id: _Optional[str]=...) -> None:
        ...

class DeletePlaybookResponse(_message.Message):
    __slots__ = ('playbook_id', 'deleted_at')
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str
    deleted_at: _timestamp_pb2.Timestamp

    def __init__(self, playbook_id: _Optional[str]=..., deleted_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class DeployPlaybookRequest(_message.Message):
    __slots__ = ('playbook_id',)
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str

    def __init__(self, playbook_id: _Optional[str]=...) -> None:
        ...

class DeployPlaybookResponse(_message.Message):
    __slots__ = ('playbook_id', 'deployed_at')
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_AT_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str
    deployed_at: _timestamp_pb2.Timestamp

    def __init__(self, playbook_id: _Optional[str]=..., deployed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class DeactivatePlaybookRequest(_message.Message):
    __slots__ = ('playbook_id',)
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str

    def __init__(self, playbook_id: _Optional[str]=...) -> None:
        ...

class PlaybookAttachDatasetRequest(_message.Message):
    __slots__ = ('playbook_id', 'dataset_id')
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str
    dataset_id: str

    def __init__(self, playbook_id: _Optional[str]=..., dataset_id: _Optional[str]=...) -> None:
        ...

class PlaybookAttachDatasetResponse(_message.Message):
    __slots__ = ('dataset',)
    DATASET_FIELD_NUMBER: _ClassVar[int]
    dataset: _dataset_pb2.Dataset

    def __init__(self, dataset: _Optional[_Union[_dataset_pb2.Dataset, _Mapping]]=...) -> None:
        ...

class PlaybookRemoveDatasetRequest(_message.Message):
    __slots__ = ('playbook_id', 'dataset_id')
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str
    dataset_id: str

    def __init__(self, playbook_id: _Optional[str]=..., dataset_id: _Optional[str]=...) -> None:
        ...

class PlaybookRemoveDatasetResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class PlaybookAttachDashboardRequest(_message.Message):
    __slots__ = ('playbook_id', 'dashboard_id')
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str
    dashboard_id: str

    def __init__(self, playbook_id: _Optional[str]=..., dashboard_id: _Optional[str]=...) -> None:
        ...

class PlaybookAttachDashboardResponse(_message.Message):
    __slots__ = ('dashboard',)
    DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    dashboard: _dashboard_pb2.Dashboard

    def __init__(self, dashboard: _Optional[_Union[_dashboard_pb2.Dashboard, _Mapping]]=...) -> None:
        ...

class PlaybookRemoveDashboardRequest(_message.Message):
    __slots__ = ('playbook_id', 'dashboard_id')
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str
    dashboard_id: str

    def __init__(self, playbook_id: _Optional[str]=..., dashboard_id: _Optional[str]=...) -> None:
        ...

class PlaybookRemoveDashboardResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class GetPlaybookReportsRequest(_message.Message):
    __slots__ = ('playbook_id', 'limit', 'offset', 'chat_id', 'template_data_id', 'batch_run_id')
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_DATA_ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str
    limit: int
    offset: int
    chat_id: str
    template_data_id: str
    batch_run_id: str

    def __init__(self, playbook_id: _Optional[str]=..., limit: _Optional[int]=..., offset: _Optional[int]=..., chat_id: _Optional[str]=..., template_data_id: _Optional[str]=..., batch_run_id: _Optional[str]=...) -> None:
        ...

class PlaybookReport(_message.Message):
    __slots__ = ('id', 'chat_id', 'cell_id', 'created_at', 'subject', 'summary', 'blocks', 'html_preview', 'playbook_id', 'read_at', 'playbook_template_data_id')
    ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    HTML_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    READ_AT_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOK_TEMPLATE_DATA_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    chat_id: str
    cell_id: str
    created_at: _timestamp_pb2.Timestamp
    subject: str
    summary: str
    blocks: _containers.RepeatedCompositeFieldContainer[_report_pb2.ReportBlock]
    html_preview: str
    playbook_id: str
    read_at: _timestamp_pb2.Timestamp
    playbook_template_data_id: str

    def __init__(self, id: _Optional[str]=..., chat_id: _Optional[str]=..., cell_id: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., subject: _Optional[str]=..., summary: _Optional[str]=..., blocks: _Optional[_Iterable[_Union[_report_pb2.ReportBlock, _Mapping]]]=..., html_preview: _Optional[str]=..., playbook_id: _Optional[str]=..., read_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., playbook_template_data_id: _Optional[str]=...) -> None:
        ...

class GetPlaybookReportsResponse(_message.Message):
    __slots__ = ('reports', 'total_count')
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    reports: _containers.RepeatedCompositeFieldContainer[PlaybookReport]
    total_count: int

    def __init__(self, reports: _Optional[_Iterable[_Union[PlaybookReport, _Mapping]]]=..., total_count: _Optional[int]=...) -> None:
        ...

class GetPlaybookReportsBatchRequest(_message.Message):
    __slots__ = ('playbook_id', 'template_data_ids', 'limit_per_template', 'batch_run_id')
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_DATA_IDS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_PER_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    BATCH_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str
    template_data_ids: _containers.RepeatedScalarFieldContainer[str]
    limit_per_template: int
    batch_run_id: str

    def __init__(self, playbook_id: _Optional[str]=..., template_data_ids: _Optional[_Iterable[str]]=..., limit_per_template: _Optional[int]=..., batch_run_id: _Optional[str]=...) -> None:
        ...

class TemplateDataReports(_message.Message):
    __slots__ = ('template_data_id', 'reports', 'total_count', 'preview_cells')
    TEMPLATE_DATA_ID_FIELD_NUMBER: _ClassVar[int]
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_CELLS_FIELD_NUMBER: _ClassVar[int]
    template_data_id: str
    reports: _containers.RepeatedCompositeFieldContainer[PlaybookReport]
    total_count: int
    preview_cells: _containers.RepeatedCompositeFieldContainer[_cells_pb2.PreviewCellRef]

    def __init__(self, template_data_id: _Optional[str]=..., reports: _Optional[_Iterable[_Union[PlaybookReport, _Mapping]]]=..., total_count: _Optional[int]=..., preview_cells: _Optional[_Iterable[_Union[_cells_pb2.PreviewCellRef, _Mapping]]]=...) -> None:
        ...

class GetPlaybookReportsBatchResponse(_message.Message):
    __slots__ = ('template_data_reports',)
    TEMPLATE_DATA_REPORTS_FIELD_NUMBER: _ClassVar[int]
    template_data_reports: _containers.RepeatedCompositeFieldContainer[TemplateDataReports]

    def __init__(self, template_data_reports: _Optional[_Iterable[_Union[TemplateDataReports, _Mapping]]]=...) -> None:
        ...

class PreviewSlackReportRequest(_message.Message):
    __slots__ = ('playbook_id', 'cell', 'chat_id', 'slack_channel_id')
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    CELL_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    SLACK_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str
    cell: _cells_pb2.ReportCell
    chat_id: str
    slack_channel_id: str

    def __init__(self, playbook_id: _Optional[str]=..., cell: _Optional[_Union[_cells_pb2.ReportCell, _Mapping]]=..., chat_id: _Optional[str]=..., slack_channel_id: _Optional[str]=...) -> None:
        ...

class PreviewSlackReportResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class RunPlaybookRequest(_message.Message):
    __slots__ = ('playbook_id', 'dry_run', 'template_id')
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str
    dry_run: bool
    template_id: str

    def __init__(self, playbook_id: _Optional[str]=..., dry_run: bool=..., template_id: _Optional[str]=...) -> None:
        ...

class RunPlaybookResponse(_message.Message):
    __slots__ = ('chat_id',)
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str

    def __init__(self, chat_id: _Optional[str]=...) -> None:
        ...

class DemoPlaybookRequest(_message.Message):
    __slots__ = ('chat_id', 'person_name', 'job_title', 'target_email')
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    PERSON_NAME_FIELD_NUMBER: _ClassVar[int]
    JOB_TITLE_FIELD_NUMBER: _ClassVar[int]
    TARGET_EMAIL_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    person_name: str
    job_title: str
    target_email: str

    def __init__(self, chat_id: _Optional[str]=..., person_name: _Optional[str]=..., job_title: _Optional[str]=..., target_email: _Optional[str]=...) -> None:
        ...

class DemoPlaybookResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetMembersWithPlaybooksRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetMembersWithPlaybooksResponse(_message.Message):
    __slots__ = ('members',)
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    members: _containers.RepeatedCompositeFieldContainer[_identity_pb2.MemberPreview]

    def __init__(self, members: _Optional[_Iterable[_Union[_identity_pb2.MemberPreview, _Mapping]]]=...) -> None:
        ...

class DuplicatePlaybookRequest(_message.Message):
    __slots__ = ('playbook_id',)
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str

    def __init__(self, playbook_id: _Optional[str]=...) -> None:
        ...

class DuplicatePlaybookResponse(_message.Message):
    __slots__ = ('playbook',)
    PLAYBOOK_FIELD_NUMBER: _ClassVar[int]
    playbook: Playbook

    def __init__(self, playbook: _Optional[_Union[Playbook, _Mapping]]=...) -> None:
        ...

class GetPlaybookLineageRequest(_message.Message):
    __slots__ = ('playbook_id',)
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str

    def __init__(self, playbook_id: _Optional[str]=...) -> None:
        ...

class PlaybookLineageNode(_message.Message):
    __slots__ = ('playbook_id', 'name', 'status', 'duplicated_at', 'duplicated_by')
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DUPLICATED_AT_FIELD_NUMBER: _ClassVar[int]
    DUPLICATED_BY_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str
    name: str
    status: PlaybookStatus
    duplicated_at: _timestamp_pb2.Timestamp
    duplicated_by: _identity_pb2.MemberPreview

    def __init__(self, playbook_id: _Optional[str]=..., name: _Optional[str]=..., status: _Optional[_Union[PlaybookStatus, str]]=..., duplicated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., duplicated_by: _Optional[_Union[_identity_pb2.MemberPreview, _Mapping]]=...) -> None:
        ...

class GetPlaybookLineageResponse(_message.Message):
    __slots__ = ('parent', 'duplicates', 'origin_playbook_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DUPLICATES_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    parent: PlaybookLineageNode
    duplicates: _containers.RepeatedCompositeFieldContainer[PlaybookLineageNode]
    origin_playbook_id: str

    def __init__(self, parent: _Optional[_Union[PlaybookLineageNode, _Mapping]]=..., duplicates: _Optional[_Iterable[_Union[PlaybookLineageNode, _Mapping]]]=..., origin_playbook_id: _Optional[str]=...) -> None:
        ...

class ReportFilters(_message.Message):
    __slots__ = ('playbook_ids', 'search_term', 'start_time', 'end_time', 'sort_by', 'sort_direction', 'limit', 'offset', 'only_subscribed', 'include_header', 'include_with_header', 'chat_id')
    PLAYBOOK_IDS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_TERM_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    SORT_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ONLY_SUBSCRIBED_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_HEADER_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_WITH_HEADER_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    playbook_ids: _containers.RepeatedScalarFieldContainer[str]
    search_term: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    sort_by: str
    sort_direction: _common_pb2.SortDirection
    limit: int
    offset: int
    only_subscribed: bool
    include_header: bool
    include_with_header: bool
    chat_id: str

    def __init__(self, playbook_ids: _Optional[_Iterable[str]]=..., search_term: _Optional[str]=..., start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., sort_by: _Optional[str]=..., sort_direction: _Optional[_Union[_common_pb2.SortDirection, str]]=..., limit: _Optional[int]=..., offset: _Optional[int]=..., only_subscribed: bool=..., include_header: bool=..., include_with_header: bool=..., chat_id: _Optional[str]=...) -> None:
        ...

class GetReportsWithFiltersRequest(_message.Message):
    __slots__ = ('filters',)
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    filters: ReportFilters

    def __init__(self, filters: _Optional[_Union[ReportFilters, _Mapping]]=...) -> None:
        ...

class GetReportsWithFiltersResponse(_message.Message):
    __slots__ = ('reports', 'reports_with_header', 'total_count', 'unread_count')
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    REPORTS_WITH_HEADER_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    reports: _containers.RepeatedCompositeFieldContainer[PlaybookReport]
    reports_with_header: _containers.RepeatedCompositeFieldContainer[PlaybookReport]
    total_count: int
    unread_count: int

    def __init__(self, reports: _Optional[_Iterable[_Union[PlaybookReport, _Mapping]]]=..., reports_with_header: _Optional[_Iterable[_Union[PlaybookReport, _Mapping]]]=..., total_count: _Optional[int]=..., unread_count: _Optional[int]=...) -> None:
        ...

class ChatReportSummary(_message.Message):
    __slots__ = ('id', 'chat_id', 'subject', 'summary', 'created_at', 'hero_image_url')
    ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    HERO_IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    chat_id: str
    subject: str
    summary: str
    created_at: _timestamp_pb2.Timestamp
    hero_image_url: str

    def __init__(self, id: _Optional[str]=..., chat_id: _Optional[str]=..., subject: _Optional[str]=..., summary: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., hero_image_url: _Optional[str]=...) -> None:
        ...

class GetChatReportsSummaryRequest(_message.Message):
    __slots__ = ('chat_id',)
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str

    def __init__(self, chat_id: _Optional[str]=...) -> None:
        ...

class GetChatReportsSummaryResponse(_message.Message):
    __slots__ = ('reports',)
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    reports: _containers.RepeatedCompositeFieldContainer[ChatReportSummary]

    def __init__(self, reports: _Optional[_Iterable[_Union[ChatReportSummary, _Mapping]]]=...) -> None:
        ...

class GetReportByIdRequest(_message.Message):
    __slots__ = ('report_id',)
    REPORT_ID_FIELD_NUMBER: _ClassVar[int]
    report_id: str

    def __init__(self, report_id: _Optional[str]=...) -> None:
        ...

class GetReportByIdResponse(_message.Message):
    __slots__ = ('report',)
    REPORT_FIELD_NUMBER: _ClassVar[int]
    report: PlaybookReport

    def __init__(self, report: _Optional[_Union[PlaybookReport, _Mapping]]=...) -> None:
        ...

class GetPlaybookReportsWithFiltersRequest(_message.Message):
    __slots__ = ('filters',)
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    filters: ReportFilters

    def __init__(self, filters: _Optional[_Union[ReportFilters, _Mapping]]=...) -> None:
        ...

class GetPlaybookReportsWithFiltersResponse(_message.Message):
    __slots__ = ('reports', 'total_count')
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    reports: _containers.RepeatedCompositeFieldContainer[PlaybookReport]
    total_count: int

    def __init__(self, reports: _Optional[_Iterable[_Union[PlaybookReport, _Mapping]]]=..., total_count: _Optional[int]=...) -> None:
        ...

class PlaybookPreview(_message.Message):
    __slots__ = ('id', 'name', 'status', 'created_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    status: PlaybookStatus
    created_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., status: _Optional[_Union[PlaybookStatus, str]]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GetPlaybooksPreviewsRequest(_message.Message):
    __slots__ = ('only_subscribed', 'status_filter')
    ONLY_SUBSCRIBED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FILTER_FIELD_NUMBER: _ClassVar[int]
    only_subscribed: bool
    status_filter: PlaybookStatus

    def __init__(self, only_subscribed: bool=..., status_filter: _Optional[_Union[PlaybookStatus, str]]=...) -> None:
        ...

class GetPlaybooksPreviewsResponse(_message.Message):
    __slots__ = ('playbooks',)
    PLAYBOOKS_FIELD_NUMBER: _ClassVar[int]
    playbooks: _containers.RepeatedCompositeFieldContainer[PlaybookPreview]

    def __init__(self, playbooks: _Optional[_Iterable[_Union[PlaybookPreview, _Mapping]]]=...) -> None:
        ...

class SubscribeToPlaybookRequest(_message.Message):
    __slots__ = ('playbook_id',)
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str

    def __init__(self, playbook_id: _Optional[str]=...) -> None:
        ...

class SubscribeToPlaybookResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class UnsubscribeFromPlaybookRequest(_message.Message):
    __slots__ = ('playbook_id',)
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str

    def __init__(self, playbook_id: _Optional[str]=...) -> None:
        ...

class UnsubscribeFromPlaybookResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class GetActiveSubscribedPlaybooksCountRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetActiveSubscribedPlaybooksCountResponse(_message.Message):
    __slots__ = ('count',)
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int

    def __init__(self, count: _Optional[int]=...) -> None:
        ...

class MarkReportAsReadRequest(_message.Message):
    __slots__ = ('report_id',)
    REPORT_ID_FIELD_NUMBER: _ClassVar[int]
    report_id: str

    def __init__(self, report_id: _Optional[str]=...) -> None:
        ...

class MarkReportAsReadResponse(_message.Message):
    __slots__ = ('success', 'read_at')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    READ_AT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    read_at: _timestamp_pb2.Timestamp

    def __init__(self, success: bool=..., read_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class FavoriteReportRequest(_message.Message):
    __slots__ = ('playbook_id', 'report_id')
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    REPORT_ID_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str
    report_id: str

    def __init__(self, playbook_id: _Optional[str]=..., report_id: _Optional[str]=...) -> None:
        ...

class FavoriteReportResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class SetSlackChannelContextPlaybookRequest(_message.Message):
    __slots__ = ('playbook_id', 'slack_channel_id')
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    SLACK_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str
    slack_channel_id: str

    def __init__(self, playbook_id: _Optional[str]=..., slack_channel_id: _Optional[str]=...) -> None:
        ...

class SetSlackChannelContextPlaybookResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class UnsetSlackChannelContextPlaybookRequest(_message.Message):
    __slots__ = ('slack_channel_id',)
    SLACK_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    slack_channel_id: str

    def __init__(self, slack_channel_id: _Optional[str]=...) -> None:
        ...

class UnsetSlackChannelContextPlaybookResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class ListSlackChannelsForContextPlaybookRequest(_message.Message):
    __slots__ = ('playbook_id',)
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str

    def __init__(self, playbook_id: _Optional[str]=...) -> None:
        ...

class ListSlackChannelsForContextPlaybookResponse(_message.Message):
    __slots__ = ('slack_channel_ids',)
    SLACK_CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
    slack_channel_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, slack_channel_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class SlackChannelPlaybookMapping(_message.Message):
    __slots__ = ('playbook_id', 'slack_channel_id')
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    SLACK_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str
    slack_channel_id: str

    def __init__(self, playbook_id: _Optional[str]=..., slack_channel_id: _Optional[str]=...) -> None:
        ...

class ListAllSlackChannelContextPlaybooksRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListAllSlackChannelContextPlaybooksResponse(_message.Message):
    __slots__ = ('mappings',)
    MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    mappings: _containers.RepeatedCompositeFieldContainer[SlackChannelPlaybookMapping]

    def __init__(self, mappings: _Optional[_Iterable[_Union[SlackChannelPlaybookMapping, _Mapping]]]=...) -> None:
        ...

class SetTeamsChannelContextPlaybookRequest(_message.Message):
    __slots__ = ('playbook_id', 'teams_channel_id')
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    TEAMS_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str
    teams_channel_id: str

    def __init__(self, playbook_id: _Optional[str]=..., teams_channel_id: _Optional[str]=...) -> None:
        ...

class SetTeamsChannelContextPlaybookResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class UnsetTeamsChannelContextPlaybookRequest(_message.Message):
    __slots__ = ('teams_channel_id',)
    TEAMS_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    teams_channel_id: str

    def __init__(self, teams_channel_id: _Optional[str]=...) -> None:
        ...

class UnsetTeamsChannelContextPlaybookResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class ListTeamsChannelsForContextPlaybookRequest(_message.Message):
    __slots__ = ('playbook_id',)
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str

    def __init__(self, playbook_id: _Optional[str]=...) -> None:
        ...

class ListTeamsChannelsForContextPlaybookResponse(_message.Message):
    __slots__ = ('teams_channel_ids',)
    TEAMS_CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
    teams_channel_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, teams_channel_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class TeamsChannelPlaybookMapping(_message.Message):
    __slots__ = ('playbook_id', 'teams_channel_id')
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    TEAMS_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str
    teams_channel_id: str

    def __init__(self, playbook_id: _Optional[str]=..., teams_channel_id: _Optional[str]=...) -> None:
        ...

class ListAllTeamsChannelContextPlaybooksRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListAllTeamsChannelContextPlaybooksResponse(_message.Message):
    __slots__ = ('mappings',)
    MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    mappings: _containers.RepeatedCompositeFieldContainer[TeamsChannelPlaybookMapping]

    def __init__(self, mappings: _Optional[_Iterable[_Union[TeamsChannelPlaybookMapping, _Mapping]]]=...) -> None:
        ...

class StreamTemplateDataStatusRequest(_message.Message):
    __slots__ = ('template_header_id', 'playbook_id')
    TEMPLATE_HEADER_ID_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    template_header_id: str
    playbook_id: str

    def __init__(self, template_header_id: _Optional[str]=..., playbook_id: _Optional[str]=...) -> None:
        ...

class TemplateDataStatusUpdate(_message.Message):
    __slots__ = ('template_data_id', 'execution_status', 'last_execution_started_at', 'last_execution_completed_at', 'last_execution_error', 'chat_id')
    TEMPLATE_DATA_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_EXECUTION_STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_EXECUTION_COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_EXECUTION_ERROR_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    template_data_id: str
    execution_status: TemplateDataExecutionStatus
    last_execution_started_at: _timestamp_pb2.Timestamp
    last_execution_completed_at: _timestamp_pb2.Timestamp
    last_execution_error: str
    chat_id: str

    def __init__(self, template_data_id: _Optional[str]=..., execution_status: _Optional[_Union[TemplateDataExecutionStatus, str]]=..., last_execution_started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., last_execution_completed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., last_execution_error: _Optional[str]=..., chat_id: _Optional[str]=...) -> None:
        ...

class CancelTemplateExecutionRequest(_message.Message):
    __slots__ = ('template_header_id', 'playbook_id')
    TEMPLATE_HEADER_ID_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    template_header_id: str
    playbook_id: str

    def __init__(self, template_header_id: _Optional[str]=..., playbook_id: _Optional[str]=...) -> None:
        ...

class CancelTemplateExecutionResponse(_message.Message):
    __slots__ = ('success', 'cancelled_count')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_COUNT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    cancelled_count: int

    def __init__(self, success: bool=..., cancelled_count: _Optional[int]=...) -> None:
        ...

class PlaybookBatchRun(_message.Message):
    __slots__ = ('id', 'playbook_id', 'template_header_id', 'template_data_ids', 'created_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_HEADER_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_DATA_IDS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    playbook_id: str
    template_header_id: str
    template_data_ids: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., playbook_id: _Optional[str]=..., template_header_id: _Optional[str]=..., template_data_ids: _Optional[_Iterable[str]]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GetPlaybookBatchRunRequest(_message.Message):
    __slots__ = ('batch_run_id',)
    BATCH_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    batch_run_id: str

    def __init__(self, batch_run_id: _Optional[str]=...) -> None:
        ...

class GetPlaybookBatchRunResponse(_message.Message):
    __slots__ = ('batch_run',)
    BATCH_RUN_FIELD_NUMBER: _ClassVar[int]
    batch_run: PlaybookBatchRun

    def __init__(self, batch_run: _Optional[_Union[PlaybookBatchRun, _Mapping]]=...) -> None:
        ...

class ListPlaybookBatchRunsRequest(_message.Message):
    __slots__ = ('playbook_id', 'limit', 'offset')
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str
    limit: int
    offset: int

    def __init__(self, playbook_id: _Optional[str]=..., limit: _Optional[int]=..., offset: _Optional[int]=...) -> None:
        ...

class ListPlaybookBatchRunsResponse(_message.Message):
    __slots__ = ('batch_runs', 'total_count')
    BATCH_RUNS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    batch_runs: _containers.RepeatedCompositeFieldContainer[PlaybookBatchRun]
    total_count: int

    def __init__(self, batch_runs: _Optional[_Iterable[_Union[PlaybookBatchRun, _Mapping]]]=..., total_count: _Optional[int]=...) -> None:
        ...