# pylint: skip-file
# mypy: ignore-errors
# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
import datetime
from ..google.api import visibility_pb2 as _visibility_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ..public import chat_pb2 as _chat_pb2
from ..public import llm_model_pb2 as _llm_model_pb2
from ..public import paradigm_pb2 as _paradigm_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AgentViewerDeliveryRoute(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_VIEWER_DELIVERY_ROUTE_UNSPECIFIED: _ClassVar[AgentViewerDeliveryRoute]
    AGENT_VIEWER_DELIVERY_ROUTE_EMAIL: _ClassVar[AgentViewerDeliveryRoute]
    AGENT_VIEWER_DELIVERY_ROUTE_SLACK_DM: _ClassVar[AgentViewerDeliveryRoute]
    AGENT_VIEWER_DELIVERY_ROUTE_TEAMS_DM: _ClassVar[AgentViewerDeliveryRoute]

class AgentRunStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_RUN_STATUS_UNSPECIFIED: _ClassVar[AgentRunStatus]
    AGENT_RUN_STATUS_RUNNING: _ClassVar[AgentRunStatus]
    AGENT_RUN_STATUS_DONE: _ClassVar[AgentRunStatus]
    AGENT_RUN_STATUS_FAILED: _ClassVar[AgentRunStatus]
    AGENT_RUN_STATUS_CANCELLED: _ClassVar[AgentRunStatus]
AGENT_VIEWER_DELIVERY_ROUTE_UNSPECIFIED: AgentViewerDeliveryRoute
AGENT_VIEWER_DELIVERY_ROUTE_EMAIL: AgentViewerDeliveryRoute
AGENT_VIEWER_DELIVERY_ROUTE_SLACK_DM: AgentViewerDeliveryRoute
AGENT_VIEWER_DELIVERY_ROUTE_TEAMS_DM: AgentViewerDeliveryRoute
AGENT_RUN_STATUS_UNSPECIFIED: AgentRunStatus
AGENT_RUN_STATUS_RUNNING: AgentRunStatus
AGENT_RUN_STATUS_DONE: AgentRunStatus
AGENT_RUN_STATUS_FAILED: AgentRunStatus
AGENT_RUN_STATUS_CANCELLED: AgentRunStatus

class SlackAgentTrigger(_message.Message):
    __slots__ = ('trigger_id', 'is_active', 'team_id', 'allowed_channel_ids')
    TRIGGER_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
    trigger_id: str
    is_active: bool
    team_id: str
    allowed_channel_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, trigger_id: _Optional[str]=..., is_active: bool=..., team_id: _Optional[str]=..., allowed_channel_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class Agent(_message.Message):
    __slots__ = ('id', 'name', 'prompt', 'is_active', 'last_post_at', 'paradigm_options', 'post_count', 'comment_count', 'vote_count', 'member_id', 'member_name', 'last_chat_id', 'has_write_permission', 'slack_channel_id', 'slack_dm_user_ids', 'skip_org_default_channel', 'llm_model', 'fast_mode', 'is_stateful', 'posting_frequency_crons', 'email_output_enabled', 'email_recipient_member_ids', 'webhook_trigger_id', 'channel_ids', 'teams_channel_id', 'teams_dm_user_aad_ids', 'slack_trigger', 'profile_image_url', 'posting_frequency_cadences', 'callable_as_subagent', 'subagent_invoker_member_ids', 'subagent_invoker_role_ids', 'feed_enabled', 'viewer_delivery_routes', 'subagent_agent_ids', 'allow_ad_hoc_subagents')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    LAST_POST_AT_FIELD_NUMBER: _ClassVar[int]
    PARADIGM_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    POST_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    VOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    HAS_WRITE_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    SLACK_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    SLACK_DM_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    SKIP_ORG_DEFAULT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    LLM_MODEL_FIELD_NUMBER: _ClassVar[int]
    FAST_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_STATEFUL_FIELD_NUMBER: _ClassVar[int]
    POSTING_FREQUENCY_CRONS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_OUTPUT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    EMAIL_RECIPIENT_MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_TRIGGER_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
    TEAMS_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TEAMS_DM_USER_AAD_IDS_FIELD_NUMBER: _ClassVar[int]
    SLACK_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    PROFILE_IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    POSTING_FREQUENCY_CADENCES_FIELD_NUMBER: _ClassVar[int]
    CALLABLE_AS_SUBAGENT_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_INVOKER_MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_INVOKER_ROLE_IDS_FIELD_NUMBER: _ClassVar[int]
    FEED_ENABLED_FIELD_NUMBER: _ClassVar[int]
    VIEWER_DELIVERY_ROUTES_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_AGENT_IDS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_AD_HOC_SUBAGENTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    prompt: str
    is_active: bool
    last_post_at: _timestamp_pb2.Timestamp
    paradigm_options: _paradigm_pb2.ParadigmOptions
    post_count: int
    comment_count: int
    vote_count: int
    member_id: str
    member_name: str
    last_chat_id: str
    has_write_permission: bool
    slack_channel_id: str
    slack_dm_user_ids: _containers.RepeatedScalarFieldContainer[str]
    skip_org_default_channel: bool
    llm_model: _llm_model_pb2.LlmModel
    fast_mode: bool
    is_stateful: bool
    posting_frequency_crons: _containers.RepeatedScalarFieldContainer[str]
    email_output_enabled: bool
    email_recipient_member_ids: _containers.RepeatedScalarFieldContainer[str]
    webhook_trigger_id: str
    channel_ids: _containers.RepeatedScalarFieldContainer[str]
    teams_channel_id: str
    teams_dm_user_aad_ids: _containers.RepeatedScalarFieldContainer[str]
    slack_trigger: SlackAgentTrigger
    profile_image_url: str
    posting_frequency_cadences: _containers.RepeatedScalarFieldContainer[str]
    callable_as_subagent: bool
    subagent_invoker_member_ids: _containers.RepeatedScalarFieldContainer[str]
    subagent_invoker_role_ids: _containers.RepeatedScalarFieldContainer[str]
    feed_enabled: bool
    viewer_delivery_routes: _containers.RepeatedScalarFieldContainer[AgentViewerDeliveryRoute]
    subagent_agent_ids: _containers.RepeatedScalarFieldContainer[str]
    allow_ad_hoc_subagents: bool

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., prompt: _Optional[str]=..., is_active: bool=..., last_post_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., paradigm_options: _Optional[_Union[_paradigm_pb2.ParadigmOptions, _Mapping]]=..., post_count: _Optional[int]=..., comment_count: _Optional[int]=..., vote_count: _Optional[int]=..., member_id: _Optional[str]=..., member_name: _Optional[str]=..., last_chat_id: _Optional[str]=..., has_write_permission: bool=..., slack_channel_id: _Optional[str]=..., slack_dm_user_ids: _Optional[_Iterable[str]]=..., skip_org_default_channel: bool=..., llm_model: _Optional[_Union[_llm_model_pb2.LlmModel, str]]=..., fast_mode: bool=..., is_stateful: bool=..., posting_frequency_crons: _Optional[_Iterable[str]]=..., email_output_enabled: bool=..., email_recipient_member_ids: _Optional[_Iterable[str]]=..., webhook_trigger_id: _Optional[str]=..., channel_ids: _Optional[_Iterable[str]]=..., teams_channel_id: _Optional[str]=..., teams_dm_user_aad_ids: _Optional[_Iterable[str]]=..., slack_trigger: _Optional[_Union[SlackAgentTrigger, _Mapping]]=..., profile_image_url: _Optional[str]=..., posting_frequency_cadences: _Optional[_Iterable[str]]=..., callable_as_subagent: bool=..., subagent_invoker_member_ids: _Optional[_Iterable[str]]=..., subagent_invoker_role_ids: _Optional[_Iterable[str]]=..., feed_enabled: bool=..., viewer_delivery_routes: _Optional[_Iterable[_Union[AgentViewerDeliveryRoute, str]]]=..., subagent_agent_ids: _Optional[_Iterable[str]]=..., allow_ad_hoc_subagents: bool=...) -> None:
        ...

class UploadAgentAvatarRequest(_message.Message):
    __slots__ = ('agent_id', 'image_data', 'file_name')
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_DATA_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    image_data: bytes
    file_name: str

    def __init__(self, agent_id: _Optional[str]=..., image_data: _Optional[bytes]=..., file_name: _Optional[str]=...) -> None:
        ...

class UploadAgentAvatarResponse(_message.Message):
    __slots__ = ('profile_image_url',)
    PROFILE_IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    profile_image_url: str

    def __init__(self, profile_image_url: _Optional[str]=...) -> None:
        ...

class ResetAgentAvatarRequest(_message.Message):
    __slots__ = ('agent_id',)
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str

    def __init__(self, agent_id: _Optional[str]=...) -> None:
        ...

class ResetAgentAvatarResponse(_message.Message):
    __slots__ = ('profile_image_url',)
    PROFILE_IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    profile_image_url: str

    def __init__(self, profile_image_url: _Optional[str]=...) -> None:
        ...

class CreateAgentRequest(_message.Message):
    __slots__ = ('name', 'prompt', 'paradigm_options', 'source_suggestion_id', 'slack_channel_id', 'slack_dm_user_ids', 'skip_org_default_channel', 'llm_model', 'fast_mode', 'is_stateful', 'posting_frequency_crons', 'email_recipient_member_ids', 'channel_ids', 'teams_channel_id', 'teams_dm_user_aad_ids', 'slack_trigger', 'posting_frequency_cadences', 'callable_as_subagent', 'subagent_invoker_member_ids', 'subagent_invoker_role_ids', 'feed_enabled', 'subagent_agent_ids', 'allow_ad_hoc_subagents')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    PARADIGM_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SUGGESTION_ID_FIELD_NUMBER: _ClassVar[int]
    SLACK_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    SLACK_DM_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    SKIP_ORG_DEFAULT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    LLM_MODEL_FIELD_NUMBER: _ClassVar[int]
    FAST_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_STATEFUL_FIELD_NUMBER: _ClassVar[int]
    POSTING_FREQUENCY_CRONS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_RECIPIENT_MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
    TEAMS_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TEAMS_DM_USER_AAD_IDS_FIELD_NUMBER: _ClassVar[int]
    SLACK_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    POSTING_FREQUENCY_CADENCES_FIELD_NUMBER: _ClassVar[int]
    CALLABLE_AS_SUBAGENT_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_INVOKER_MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_INVOKER_ROLE_IDS_FIELD_NUMBER: _ClassVar[int]
    FEED_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_AGENT_IDS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_AD_HOC_SUBAGENTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    prompt: str
    paradigm_options: _paradigm_pb2.ParadigmOptions
    source_suggestion_id: str
    slack_channel_id: str
    slack_dm_user_ids: _containers.RepeatedScalarFieldContainer[str]
    skip_org_default_channel: bool
    llm_model: _llm_model_pb2.LlmModel
    fast_mode: bool
    is_stateful: bool
    posting_frequency_crons: _containers.RepeatedScalarFieldContainer[str]
    email_recipient_member_ids: _containers.RepeatedScalarFieldContainer[str]
    channel_ids: _containers.RepeatedScalarFieldContainer[str]
    teams_channel_id: str
    teams_dm_user_aad_ids: _containers.RepeatedScalarFieldContainer[str]
    slack_trigger: SlackAgentTrigger
    posting_frequency_cadences: _containers.RepeatedScalarFieldContainer[str]
    callable_as_subagent: bool
    subagent_invoker_member_ids: _containers.RepeatedScalarFieldContainer[str]
    subagent_invoker_role_ids: _containers.RepeatedScalarFieldContainer[str]
    feed_enabled: bool
    subagent_agent_ids: _containers.RepeatedScalarFieldContainer[str]
    allow_ad_hoc_subagents: bool

    def __init__(self, name: _Optional[str]=..., prompt: _Optional[str]=..., paradigm_options: _Optional[_Union[_paradigm_pb2.ParadigmOptions, _Mapping]]=..., source_suggestion_id: _Optional[str]=..., slack_channel_id: _Optional[str]=..., slack_dm_user_ids: _Optional[_Iterable[str]]=..., skip_org_default_channel: bool=..., llm_model: _Optional[_Union[_llm_model_pb2.LlmModel, str]]=..., fast_mode: bool=..., is_stateful: bool=..., posting_frequency_crons: _Optional[_Iterable[str]]=..., email_recipient_member_ids: _Optional[_Iterable[str]]=..., channel_ids: _Optional[_Iterable[str]]=..., teams_channel_id: _Optional[str]=..., teams_dm_user_aad_ids: _Optional[_Iterable[str]]=..., slack_trigger: _Optional[_Union[SlackAgentTrigger, _Mapping]]=..., posting_frequency_cadences: _Optional[_Iterable[str]]=..., callable_as_subagent: bool=..., subagent_invoker_member_ids: _Optional[_Iterable[str]]=..., subagent_invoker_role_ids: _Optional[_Iterable[str]]=..., feed_enabled: bool=..., subagent_agent_ids: _Optional[_Iterable[str]]=..., allow_ad_hoc_subagents: bool=...) -> None:
        ...

class CreateAgentResponse(_message.Message):
    __slots__ = ('agent', 'chat_id')
    AGENT_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    agent: Agent
    chat_id: str

    def __init__(self, agent: _Optional[_Union[Agent, _Mapping]]=..., chat_id: _Optional[str]=...) -> None:
        ...

class UpdateAgentRequest(_message.Message):
    __slots__ = ('agent_id', 'name', 'prompt', 'is_active', 'paradigm_options', 'slack_channel_id', 'slack_dm_user_ids', 'skip_org_default_channel', 'llm_model', 'fast_mode', 'is_stateful', 'posting_frequency_crons', 'email_recipient_member_ids', 'update_email_recipients', 'channel_ids', 'update_channel_ids', 'teams_channel_id', 'teams_dm_user_aad_ids', 'slack_trigger', 'posting_frequency_cadences', 'callable_as_subagent', 'subagent_invoker_member_ids', 'subagent_invoker_role_ids', 'update_subagent_invokers', 'feed_enabled', 'subagent_agent_ids', 'update_subagents', 'allow_ad_hoc_subagents')
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    PARADIGM_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SLACK_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    SLACK_DM_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    SKIP_ORG_DEFAULT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    LLM_MODEL_FIELD_NUMBER: _ClassVar[int]
    FAST_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_STATEFUL_FIELD_NUMBER: _ClassVar[int]
    POSTING_FREQUENCY_CRONS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_RECIPIENT_MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_EMAIL_RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
    TEAMS_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TEAMS_DM_USER_AAD_IDS_FIELD_NUMBER: _ClassVar[int]
    SLACK_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    POSTING_FREQUENCY_CADENCES_FIELD_NUMBER: _ClassVar[int]
    CALLABLE_AS_SUBAGENT_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_INVOKER_MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_INVOKER_ROLE_IDS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_SUBAGENT_INVOKERS_FIELD_NUMBER: _ClassVar[int]
    FEED_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_AGENT_IDS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_SUBAGENTS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_AD_HOC_SUBAGENTS_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    name: str
    prompt: str
    is_active: bool
    paradigm_options: _paradigm_pb2.ParadigmOptions
    slack_channel_id: str
    slack_dm_user_ids: _containers.RepeatedScalarFieldContainer[str]
    skip_org_default_channel: bool
    llm_model: _llm_model_pb2.LlmModel
    fast_mode: bool
    is_stateful: bool
    posting_frequency_crons: _containers.RepeatedScalarFieldContainer[str]
    email_recipient_member_ids: _containers.RepeatedScalarFieldContainer[str]
    update_email_recipients: bool
    channel_ids: _containers.RepeatedScalarFieldContainer[str]
    update_channel_ids: bool
    teams_channel_id: str
    teams_dm_user_aad_ids: _containers.RepeatedScalarFieldContainer[str]
    slack_trigger: SlackAgentTrigger
    posting_frequency_cadences: _containers.RepeatedScalarFieldContainer[str]
    callable_as_subagent: bool
    subagent_invoker_member_ids: _containers.RepeatedScalarFieldContainer[str]
    subagent_invoker_role_ids: _containers.RepeatedScalarFieldContainer[str]
    update_subagent_invokers: bool
    feed_enabled: bool
    subagent_agent_ids: _containers.RepeatedScalarFieldContainer[str]
    update_subagents: bool
    allow_ad_hoc_subagents: bool

    def __init__(self, agent_id: _Optional[str]=..., name: _Optional[str]=..., prompt: _Optional[str]=..., is_active: bool=..., paradigm_options: _Optional[_Union[_paradigm_pb2.ParadigmOptions, _Mapping]]=..., slack_channel_id: _Optional[str]=..., slack_dm_user_ids: _Optional[_Iterable[str]]=..., skip_org_default_channel: bool=..., llm_model: _Optional[_Union[_llm_model_pb2.LlmModel, str]]=..., fast_mode: bool=..., is_stateful: bool=..., posting_frequency_crons: _Optional[_Iterable[str]]=..., email_recipient_member_ids: _Optional[_Iterable[str]]=..., update_email_recipients: bool=..., channel_ids: _Optional[_Iterable[str]]=..., update_channel_ids: bool=..., teams_channel_id: _Optional[str]=..., teams_dm_user_aad_ids: _Optional[_Iterable[str]]=..., slack_trigger: _Optional[_Union[SlackAgentTrigger, _Mapping]]=..., posting_frequency_cadences: _Optional[_Iterable[str]]=..., callable_as_subagent: bool=..., subagent_invoker_member_ids: _Optional[_Iterable[str]]=..., subagent_invoker_role_ids: _Optional[_Iterable[str]]=..., update_subagent_invokers: bool=..., feed_enabled: bool=..., subagent_agent_ids: _Optional[_Iterable[str]]=..., update_subagents: bool=..., allow_ad_hoc_subagents: bool=...) -> None:
        ...

class UpdateAgentResponse(_message.Message):
    __slots__ = ('agent', 'chat_id')
    AGENT_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    agent: Agent
    chat_id: str

    def __init__(self, agent: _Optional[_Union[Agent, _Mapping]]=..., chat_id: _Optional[str]=...) -> None:
        ...

class ListAgentsRequest(_message.Message):
    __slots__ = ('include_inactive', 'include_all_org', 'days')
    INCLUDE_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ALL_ORG_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    include_inactive: bool
    include_all_org: bool
    days: int

    def __init__(self, include_inactive: bool=..., include_all_org: bool=..., days: _Optional[int]=...) -> None:
        ...

class ListAgentsResponse(_message.Message):
    __slots__ = ('agents',)
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    agents: _containers.RepeatedCompositeFieldContainer[Agent]

    def __init__(self, agents: _Optional[_Iterable[_Union[Agent, _Mapping]]]=...) -> None:
        ...

class GetAgentRequest(_message.Message):
    __slots__ = ('agent_id',)
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str

    def __init__(self, agent_id: _Optional[str]=...) -> None:
        ...

class GetAgentResponse(_message.Message):
    __slots__ = ('agent',)
    AGENT_FIELD_NUMBER: _ClassVar[int]
    agent: Agent

    def __init__(self, agent: _Optional[_Union[Agent, _Mapping]]=...) -> None:
        ...

class DeleteAgentRequest(_message.Message):
    __slots__ = ('agent_id',)
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str

    def __init__(self, agent_id: _Optional[str]=...) -> None:
        ...

class TriggerAgentRequest(_message.Message):
    __slots__ = ('agent_id',)
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str

    def __init__(self, agent_id: _Optional[str]=...) -> None:
        ...

class TriggerAgentResponse(_message.Message):
    __slots__ = ('chat_id',)
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str

    def __init__(self, chat_id: _Optional[str]=...) -> None:
        ...

class TriggerAgentCommentRequest(_message.Message):
    __slots__ = ('agent_id', 'post_id', 'mention_thing_id')
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    MENTION_THING_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    post_id: str
    mention_thing_id: str

    def __init__(self, agent_id: _Optional[str]=..., post_id: _Optional[str]=..., mention_thing_id: _Optional[str]=...) -> None:
        ...

class DuplicateAgentRequest(_message.Message):
    __slots__ = ('agent_id',)
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str

    def __init__(self, agent_id: _Optional[str]=...) -> None:
        ...

class DuplicateAgentResponse(_message.Message):
    __slots__ = ('agent',)
    AGENT_FIELD_NUMBER: _ClassVar[int]
    agent: Agent

    def __init__(self, agent: _Optional[_Union[Agent, _Mapping]]=...) -> None:
        ...

class SeedOrganizationRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class SeedOrganizationResponse(_message.Message):
    __slots__ = ('success', 'message')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str

    def __init__(self, success: bool=..., message: _Optional[str]=...) -> None:
        ...

class StreamAgentStatusRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class AgentStatusUpdate(_message.Message):
    __slots__ = ('agent_id', 'status', 'summary', 'post_id', 'mention_thing_id', 'chat_id')
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    MENTION_THING_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    status: AgentRunStatus
    summary: str
    post_id: str
    mention_thing_id: str
    chat_id: str

    def __init__(self, agent_id: _Optional[str]=..., status: _Optional[_Union[AgentRunStatus, str]]=..., summary: _Optional[str]=..., post_id: _Optional[str]=..., mention_thing_id: _Optional[str]=..., chat_id: _Optional[str]=...) -> None:
        ...

class ListAgentRunsRequest(_message.Message):
    __slots__ = ('agent_id', 'trigger_source', 'status', 'limit', 'offset')
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    trigger_source: str
    status: str
    limit: int
    offset: int

    def __init__(self, agent_id: _Optional[str]=..., trigger_source: _Optional[str]=..., status: _Optional[str]=..., limit: _Optional[int]=..., offset: _Optional[int]=...) -> None:
        ...

class AgentRunTriggerMetadata(_message.Message):
    __slots__ = ('auth_method', 'member_id', 'api_key_id', 'client_id', 'user_agent', 'ip', 'geo')
    AUTH_METHOD_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    API_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    GEO_FIELD_NUMBER: _ClassVar[int]
    auth_method: str
    member_id: str
    api_key_id: str
    client_id: str
    user_agent: str
    ip: str
    geo: AgentRunTriggerGeo

    def __init__(self, auth_method: _Optional[str]=..., member_id: _Optional[str]=..., api_key_id: _Optional[str]=..., client_id: _Optional[str]=..., user_agent: _Optional[str]=..., ip: _Optional[str]=..., geo: _Optional[_Union[AgentRunTriggerGeo, _Mapping]]=...) -> None:
        ...

class AgentRunTriggerGeo(_message.Message):
    __slots__ = ('city', 'region', 'country', 'country_code')
    CITY_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    city: str
    region: str
    country: str
    country_code: str

    def __init__(self, city: _Optional[str]=..., region: _Optional[str]=..., country: _Optional[str]=..., country_code: _Optional[str]=...) -> None:
        ...

class AgentRunToolCall(_message.Message):
    __slots__ = ('tool', 'summary', 'error', 'result_json', 'cell_id', 'duration_ms', 'started_at_ms')
    TOOL_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULT_JSON_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    tool: str
    summary: str
    error: str
    result_json: str
    cell_id: str
    duration_ms: int
    started_at_ms: int

    def __init__(self, tool: _Optional[str]=..., summary: _Optional[str]=..., error: _Optional[str]=..., result_json: _Optional[str]=..., cell_id: _Optional[str]=..., duration_ms: _Optional[int]=..., started_at_ms: _Optional[int]=...) -> None:
        ...

class AgentRunToolsSummary(_message.Message):
    __slots__ = ('total_calls', 'tool_counts', 'details')

    class ToolCountsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int

        def __init__(self, key: _Optional[str]=..., value: _Optional[int]=...) -> None:
            ...
    TOTAL_CALLS_FIELD_NUMBER: _ClassVar[int]
    TOOL_COUNTS_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    total_calls: int
    tool_counts: _containers.ScalarMap[str, int]
    details: _containers.RepeatedCompositeFieldContainer[AgentRunToolCall]

    def __init__(self, total_calls: _Optional[int]=..., tool_counts: _Optional[_Mapping[str, int]]=..., details: _Optional[_Iterable[_Union[AgentRunToolCall, _Mapping]]]=...) -> None:
        ...

class AgentRunDeliveryChannel(_message.Message):
    __slots__ = ('type', 'id', 'label')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    type: str
    id: str
    label: str

    def __init__(self, type: _Optional[str]=..., id: _Optional[str]=..., label: _Optional[str]=...) -> None:
        ...

class AgentRunDelivery(_message.Message):
    __slots__ = ('slack_channel_id', 'teams_channel_id', 'slack_dm_user_ids', 'teams_dm_user_aad_ids', 'email_recipient_member_ids', 'feed_channel_ids', 'channels')
    SLACK_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TEAMS_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    SLACK_DM_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    TEAMS_DM_USER_AAD_IDS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_RECIPIENT_MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    FEED_CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    slack_channel_id: str
    teams_channel_id: str
    slack_dm_user_ids: _containers.RepeatedScalarFieldContainer[str]
    teams_dm_user_aad_ids: _containers.RepeatedScalarFieldContainer[str]
    email_recipient_member_ids: _containers.RepeatedScalarFieldContainer[str]
    feed_channel_ids: _containers.RepeatedScalarFieldContainer[str]
    channels: _containers.RepeatedCompositeFieldContainer[AgentRunDeliveryChannel]

    def __init__(self, slack_channel_id: _Optional[str]=..., teams_channel_id: _Optional[str]=..., slack_dm_user_ids: _Optional[_Iterable[str]]=..., teams_dm_user_aad_ids: _Optional[_Iterable[str]]=..., email_recipient_member_ids: _Optional[_Iterable[str]]=..., feed_channel_ids: _Optional[_Iterable[str]]=..., channels: _Optional[_Iterable[_Union[AgentRunDeliveryChannel, _Mapping]]]=...) -> None:
        ...

class AgentRun(_message.Message):
    __slots__ = ('id', 'agent_id', 'trigger_source', 'status', 'chat_id', 'webhook_trigger_id', 'triggered_by_member_id', 'triggered_by_agent_id', 'error_kind', 'error_message', 'attempt', 'tool_calls_count', 'last_summary', 'created_at', 'started_at', 'finished_at', 'trigger_metadata', 'tools_summary', 'delivery', 'egress_summary', 'connector_ids', 'sandbox_mount_ms')
    ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_TRIGGER_ID_FIELD_NUMBER: _ClassVar[int]
    TRIGGERED_BY_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    TRIGGERED_BY_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_KIND_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALLS_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_METADATA_FIELD_NUMBER: _ClassVar[int]
    TOOLS_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_FIELD_NUMBER: _ClassVar[int]
    EGRESS_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_IDS_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_MOUNT_MS_FIELD_NUMBER: _ClassVar[int]
    id: str
    agent_id: str
    trigger_source: str
    status: str
    chat_id: str
    webhook_trigger_id: str
    triggered_by_member_id: str
    triggered_by_agent_id: str
    error_kind: str
    error_message: str
    attempt: int
    tool_calls_count: int
    last_summary: str
    created_at: _timestamp_pb2.Timestamp
    started_at: _timestamp_pb2.Timestamp
    finished_at: _timestamp_pb2.Timestamp
    trigger_metadata: AgentRunTriggerMetadata
    tools_summary: AgentRunToolsSummary
    delivery: AgentRunDelivery
    egress_summary: _chat_pb2.EgressSummary
    connector_ids: _containers.RepeatedScalarFieldContainer[int]
    sandbox_mount_ms: int

    def __init__(self, id: _Optional[str]=..., agent_id: _Optional[str]=..., trigger_source: _Optional[str]=..., status: _Optional[str]=..., chat_id: _Optional[str]=..., webhook_trigger_id: _Optional[str]=..., triggered_by_member_id: _Optional[str]=..., triggered_by_agent_id: _Optional[str]=..., error_kind: _Optional[str]=..., error_message: _Optional[str]=..., attempt: _Optional[int]=..., tool_calls_count: _Optional[int]=..., last_summary: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., trigger_metadata: _Optional[_Union[AgentRunTriggerMetadata, _Mapping]]=..., tools_summary: _Optional[_Union[AgentRunToolsSummary, _Mapping]]=..., delivery: _Optional[_Union[AgentRunDelivery, _Mapping]]=..., egress_summary: _Optional[_Union[_chat_pb2.EgressSummary, _Mapping]]=..., connector_ids: _Optional[_Iterable[int]]=..., sandbox_mount_ms: _Optional[int]=...) -> None:
        ...

class ListAgentRunsResponse(_message.Message):
    __slots__ = ('runs',)
    RUNS_FIELD_NUMBER: _ClassVar[int]
    runs: _containers.RepeatedCompositeFieldContainer[AgentRun]

    def __init__(self, runs: _Optional[_Iterable[_Union[AgentRun, _Mapping]]]=...) -> None:
        ...

class GetAgentRunRequest(_message.Message):
    __slots__ = ('run_id',)
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    run_id: str

    def __init__(self, run_id: _Optional[str]=...) -> None:
        ...

class GetAgentRunResponse(_message.Message):
    __slots__ = ('run',)
    RUN_FIELD_NUMBER: _ClassVar[int]
    run: AgentRun

    def __init__(self, run: _Optional[_Union[AgentRun, _Mapping]]=...) -> None:
        ...

class ListAgentRunsForThingRequest(_message.Message):
    __slots__ = ('thing_id', 'limit', 'offset', 'chat_id')
    THING_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    thing_id: str
    limit: int
    offset: int
    chat_id: str

    def __init__(self, thing_id: _Optional[str]=..., limit: _Optional[int]=..., offset: _Optional[int]=..., chat_id: _Optional[str]=...) -> None:
        ...

class ListAgentRunsForThingResponse(_message.Message):
    __slots__ = ('runs',)
    RUNS_FIELD_NUMBER: _ClassVar[int]
    runs: _containers.RepeatedCompositeFieldContainer[AgentRun]

    def __init__(self, runs: _Optional[_Iterable[_Union[AgentRun, _Mapping]]]=...) -> None:
        ...

class AgentDBColumn(_message.Message):
    __slots__ = ('name', 'type', 'nullable', 'primary_key')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NULLABLE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    nullable: bool
    primary_key: bool

    def __init__(self, name: _Optional[str]=..., type: _Optional[str]=..., nullable: bool=..., primary_key: bool=...) -> None:
        ...

class AgentDBTable(_message.Message):
    __slots__ = ('name', 'columns')
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    name: str
    columns: _containers.RepeatedCompositeFieldContainer[AgentDBColumn]

    def __init__(self, name: _Optional[str]=..., columns: _Optional[_Iterable[_Union[AgentDBColumn, _Mapping]]]=...) -> None:
        ...

class GetAgentDBSchemaRequest(_message.Message):
    __slots__ = ('agent_id',)
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str

    def __init__(self, agent_id: _Optional[str]=...) -> None:
        ...

class GetAgentDBSchemaResponse(_message.Message):
    __slots__ = ('tables', 'change_log_bytes')
    TABLES_FIELD_NUMBER: _ClassVar[int]
    CHANGE_LOG_BYTES_FIELD_NUMBER: _ClassVar[int]
    tables: _containers.RepeatedCompositeFieldContainer[AgentDBTable]
    change_log_bytes: int

    def __init__(self, tables: _Optional[_Iterable[_Union[AgentDBTable, _Mapping]]]=..., change_log_bytes: _Optional[int]=...) -> None:
        ...

class GetAgentDBTablePreviewRequest(_message.Message):
    __slots__ = ('agent_id', 'table_name', 'limit')
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    table_name: str
    limit: int

    def __init__(self, agent_id: _Optional[str]=..., table_name: _Optional[str]=..., limit: _Optional[int]=...) -> None:
        ...

class GetAgentDBTablePreviewResponse(_message.Message):
    __slots__ = ('arrow_data',)
    ARROW_DATA_FIELD_NUMBER: _ClassVar[int]
    arrow_data: bytes

    def __init__(self, arrow_data: _Optional[bytes]=...) -> None:
        ...