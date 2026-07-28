# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
# pylint: skip-file
# mypy: ignore-errors
from .. import auth_pb2 as _auth_pb2
from ..google.api import visibility_pb2 as _visibility_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from .. import paradigm_params_pb2 as _paradigm_params_pb2
from ..public import chat_pb2 as _chat_pb2
from ..public import options_pb2 as _options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class UpdateOrganizationSettingsRequest(_message.Message):
    __slots__ = ('org_id', 'organization_name', 'require_attached', 'inject_whole_ontology_disable_search', 'secrets_enabled', 'email_polling_enabled', 'disable_emojis', 'warning', 'chat_v5_cutover', 'public_preview', 'console_access', 'brand_name', 'default_llm_model', 'preferred_provider', 'hide_example_connectors', 'paradigm_params', 'default_paradigm_mode', 'default_connector_ids', 'add_allowed_email_domains', 'remove_allowed_email_domains', 'training_mode', 'dashboards_enabled', 'billing_admin_id', 'methodology_enabled', 'allow_all_api_access', 'feed_enabled', 'context_v3_enabled', 'bash_enabled', 'default_routing_enabled', 'enabled_model_ids', 'restricted_model_ids', 'restricted_families', 'clear_enabled_model_ids', 'clear_restricted_model_ids', 'clear_restricted_families', 'discoverable', 'observability_enabled', 'notifications_enabled', 'client_db_override_enabled', 'context_review_required', 'google_connector_enabled', 'clear_logo_url', 'hide_api_connectors', 'fast_mode_enabled', 'max_thinking_enabled', 'clear_default_connector_ids', 'sandbox_state_retention_days', 'asset_url_expiry', 'email_output_enabled', 'default_playbook_private', 'default_dashboard_output', 'default_methodology', 'scim_new_group_default_role_type', 'groups_feature_enabled', 'show_textql_usage', 'traces_enabled', 'allow_llm_data_retention', 'sox_db_session_metadata_enabled', 'sms_enabled', 'scim_assign_default_role', 'migration_banner_dismissed', 'config_migrations_enabled', 'sandbox_observability_enabled', 'data_apps_enabled', 'issues_enabled', 'config_objects_enabled', 'config_objects_playbooks_enabled', 'config_objects_dashboards_enabled', 'config_autofix_enabled', 'spend_transparency_enabled', 'sharing_disabled')
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_ATTACHED_FIELD_NUMBER: _ClassVar[int]
    INJECT_WHOLE_ONTOLOGY_DISABLE_SEARCH_FIELD_NUMBER: _ClassVar[int]
    SECRETS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    EMAIL_POLLING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DISABLE_EMOJIS_FIELD_NUMBER: _ClassVar[int]
    WARNING_FIELD_NUMBER: _ClassVar[int]
    CHAT_V5_CUTOVER_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    CONSOLE_ACCESS_FIELD_NUMBER: _ClassVar[int]
    BRAND_NAME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LLM_MODEL_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    HIDE_EXAMPLE_CONNECTORS_FIELD_NUMBER: _ClassVar[int]
    PARADIGM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PARADIGM_MODE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CONNECTOR_IDS_FIELD_NUMBER: _ClassVar[int]
    ADD_ALLOWED_EMAIL_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_ALLOWED_EMAIL_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    TRAINING_MODE_FIELD_NUMBER: _ClassVar[int]
    DASHBOARDS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BILLING_ADMIN_ID_FIELD_NUMBER: _ClassVar[int]
    METHODOLOGY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ALLOW_ALL_API_ACCESS_FIELD_NUMBER: _ClassVar[int]
    FEED_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_V3_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BASH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ROUTING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ENABLED_MODEL_IDS_FIELD_NUMBER: _ClassVar[int]
    RESTRICTED_MODEL_IDS_FIELD_NUMBER: _ClassVar[int]
    RESTRICTED_FAMILIES_FIELD_NUMBER: _ClassVar[int]
    CLEAR_ENABLED_MODEL_IDS_FIELD_NUMBER: _ClassVar[int]
    CLEAR_RESTRICTED_MODEL_IDS_FIELD_NUMBER: _ClassVar[int]
    CLEAR_RESTRICTED_FAMILIES_FIELD_NUMBER: _ClassVar[int]
    DISCOVERABLE_FIELD_NUMBER: _ClassVar[int]
    OBSERVABILITY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CLIENT_DB_OVERRIDE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_REVIEW_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_CONNECTOR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CLEAR_LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    HIDE_API_CONNECTORS_FIELD_NUMBER: _ClassVar[int]
    FAST_MODE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MAX_THINKING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CLEAR_DEFAULT_CONNECTOR_IDS_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_STATE_RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    ASSET_URL_EXPIRY_FIELD_NUMBER: _ClassVar[int]
    EMAIL_OUTPUT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PLAYBOOK_PRIVATE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DASHBOARD_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_METHODOLOGY_FIELD_NUMBER: _ClassVar[int]
    SCIM_NEW_GROUP_DEFAULT_ROLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FEATURE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SHOW_TEXTQL_USAGE_FIELD_NUMBER: _ClassVar[int]
    TRACES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ALLOW_LLM_DATA_RETENTION_FIELD_NUMBER: _ClassVar[int]
    SOX_DB_SESSION_METADATA_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SMS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SCIM_ASSIGN_DEFAULT_ROLE_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_BANNER_DISMISSED_FIELD_NUMBER: _ClassVar[int]
    CONFIG_MIGRATIONS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_OBSERVABILITY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DATA_APPS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ISSUES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CONFIG_OBJECTS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CONFIG_OBJECTS_PLAYBOOKS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CONFIG_OBJECTS_DASHBOARDS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CONFIG_AUTOFIX_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SPEND_TRANSPARENCY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SHARING_DISABLED_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    organization_name: str
    require_attached: _wrappers_pb2.BoolValue
    inject_whole_ontology_disable_search: _wrappers_pb2.BoolValue
    secrets_enabled: _wrappers_pb2.BoolValue
    email_polling_enabled: _wrappers_pb2.BoolValue
    disable_emojis: _wrappers_pb2.BoolValue
    warning: _wrappers_pb2.StringValue
    chat_v5_cutover: _wrappers_pb2.BoolValue
    public_preview: _wrappers_pb2.BoolValue
    console_access: _wrappers_pb2.BoolValue
    brand_name: _wrappers_pb2.StringValue
    default_llm_model: _wrappers_pb2.Int32Value
    preferred_provider: _wrappers_pb2.StringValue
    hide_example_connectors: _wrappers_pb2.BoolValue
    paradigm_params: _paradigm_params_pb2.ParadigmParams
    default_paradigm_mode: _paradigm_params_pb2.ParadigmType
    default_connector_ids: _containers.RepeatedScalarFieldContainer[int]
    add_allowed_email_domains: _containers.RepeatedScalarFieldContainer[str]
    remove_allowed_email_domains: _containers.RepeatedScalarFieldContainer[str]
    training_mode: _wrappers_pb2.BoolValue
    dashboards_enabled: _wrappers_pb2.BoolValue
    billing_admin_id: _wrappers_pb2.StringValue
    methodology_enabled: _wrappers_pb2.BoolValue
    allow_all_api_access: _wrappers_pb2.BoolValue
    feed_enabled: _wrappers_pb2.BoolValue
    context_v3_enabled: _wrappers_pb2.BoolValue
    bash_enabled: _wrappers_pb2.BoolValue
    default_routing_enabled: _wrappers_pb2.BoolValue
    enabled_model_ids: _containers.RepeatedScalarFieldContainer[int]
    restricted_model_ids: _containers.RepeatedScalarFieldContainer[int]
    restricted_families: _containers.RepeatedScalarFieldContainer[str]
    clear_enabled_model_ids: bool
    clear_restricted_model_ids: bool
    clear_restricted_families: bool
    discoverable: _wrappers_pb2.BoolValue
    observability_enabled: _wrappers_pb2.BoolValue
    notifications_enabled: _wrappers_pb2.BoolValue
    client_db_override_enabled: _wrappers_pb2.BoolValue
    context_review_required: _wrappers_pb2.BoolValue
    google_connector_enabled: _wrappers_pb2.BoolValue
    clear_logo_url: bool
    hide_api_connectors: _wrappers_pb2.BoolValue
    fast_mode_enabled: _wrappers_pb2.BoolValue
    max_thinking_enabled: _wrappers_pb2.BoolValue
    clear_default_connector_ids: bool
    sandbox_state_retention_days: _wrappers_pb2.Int32Value
    asset_url_expiry: _auth_pb2.AssetUrlExpiry
    email_output_enabled: _wrappers_pb2.BoolValue
    default_playbook_private: _wrappers_pb2.BoolValue
    default_dashboard_output: _wrappers_pb2.BoolValue
    default_methodology: _chat_pb2.Methodology
    scim_new_group_default_role_type: _wrappers_pb2.StringValue
    groups_feature_enabled: _wrappers_pb2.BoolValue
    show_textql_usage: _wrappers_pb2.BoolValue
    traces_enabled: _wrappers_pb2.BoolValue
    allow_llm_data_retention: _wrappers_pb2.BoolValue
    sox_db_session_metadata_enabled: _wrappers_pb2.BoolValue
    sms_enabled: _wrappers_pb2.BoolValue
    scim_assign_default_role: _wrappers_pb2.BoolValue
    migration_banner_dismissed: _wrappers_pb2.BoolValue
    config_migrations_enabled: _wrappers_pb2.BoolValue
    sandbox_observability_enabled: _wrappers_pb2.BoolValue
    data_apps_enabled: _wrappers_pb2.BoolValue
    issues_enabled: _wrappers_pb2.BoolValue
    config_objects_enabled: _wrappers_pb2.BoolValue
    config_objects_playbooks_enabled: _wrappers_pb2.BoolValue
    config_objects_dashboards_enabled: _wrappers_pb2.BoolValue
    config_autofix_enabled: _wrappers_pb2.BoolValue
    spend_transparency_enabled: _wrappers_pb2.BoolValue
    sharing_disabled: _wrappers_pb2.BoolValue

    def __init__(self, org_id: _Optional[str]=..., organization_name: _Optional[str]=..., require_attached: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., inject_whole_ontology_disable_search: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., secrets_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., email_polling_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., disable_emojis: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., warning: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]]=..., chat_v5_cutover: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., public_preview: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., console_access: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., brand_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]]=..., default_llm_model: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., preferred_provider: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]]=..., hide_example_connectors: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., paradigm_params: _Optional[_Union[_paradigm_params_pb2.ParadigmParams, _Mapping]]=..., default_paradigm_mode: _Optional[_Union[_paradigm_params_pb2.ParadigmType, str]]=..., default_connector_ids: _Optional[_Iterable[int]]=..., add_allowed_email_domains: _Optional[_Iterable[str]]=..., remove_allowed_email_domains: _Optional[_Iterable[str]]=..., training_mode: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., dashboards_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., billing_admin_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]]=..., methodology_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., allow_all_api_access: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., feed_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., context_v3_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., bash_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., default_routing_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., enabled_model_ids: _Optional[_Iterable[int]]=..., restricted_model_ids: _Optional[_Iterable[int]]=..., restricted_families: _Optional[_Iterable[str]]=..., clear_enabled_model_ids: bool=..., clear_restricted_model_ids: bool=..., clear_restricted_families: bool=..., discoverable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., observability_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., notifications_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., client_db_override_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., context_review_required: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., google_connector_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., clear_logo_url: bool=..., hide_api_connectors: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., fast_mode_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., max_thinking_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., clear_default_connector_ids: bool=..., sandbox_state_retention_days: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., asset_url_expiry: _Optional[_Union[_auth_pb2.AssetUrlExpiry, str]]=..., email_output_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., default_playbook_private: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., default_dashboard_output: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., default_methodology: _Optional[_Union[_chat_pb2.Methodology, str]]=..., scim_new_group_default_role_type: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]]=..., groups_feature_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., show_textql_usage: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., traces_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., allow_llm_data_retention: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., sox_db_session_metadata_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., sms_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., scim_assign_default_role: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., migration_banner_dismissed: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., config_migrations_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., sandbox_observability_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., data_apps_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., issues_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., config_objects_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., config_objects_playbooks_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., config_objects_dashboards_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., config_autofix_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., spend_transparency_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., sharing_disabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=...) -> None:
        ...

class UpdateOrganizationSettingsResponse(_message.Message):
    __slots__ = ('organization',)
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    organization: _auth_pb2.Organization

    def __init__(self, organization: _Optional[_Union[_auth_pb2.Organization, _Mapping]]=...) -> None:
        ...

class ListOrganizationMembersRequest(_message.Message):
    __slots__ = ('org_id',)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str

    def __init__(self, org_id: _Optional[str]=...) -> None:
        ...

class ListOrganizationMembersResponse(_message.Message):
    __slots__ = ('members',)
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    members: _containers.RepeatedCompositeFieldContainer[_auth_pb2.Member]

    def __init__(self, members: _Optional[_Iterable[_Union[_auth_pb2.Member, _Mapping]]]=...) -> None:
        ...

class InviteOrganizationMemberRequest(_message.Message):
    __slots__ = ('org_id', 'email', 'role')
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    email: str
    role: str

    def __init__(self, org_id: _Optional[str]=..., email: _Optional[str]=..., role: _Optional[str]=...) -> None:
        ...

class InviteOrganizationMemberResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class DeleteOrganizationMemberRequest(_message.Message):
    __slots__ = ('org_id', 'member_id', 'hard_delete')
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    HARD_DELETE_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    member_id: str
    hard_delete: bool

    def __init__(self, org_id: _Optional[str]=..., member_id: _Optional[str]=..., hard_delete: bool=...) -> None:
        ...

class DeleteOrganizationMemberResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class DeleteOrganizationRequest(_message.Message):
    __slots__ = ('org_id',)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str

    def __init__(self, org_id: _Optional[str]=...) -> None:
        ...

class DeleteOrganizationResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class UpdateCurrentMemberProfileRequest(_message.Message):
    __slots__ = ('preferred_first_name', 'preferred_last_name', 'show_code', 'steering')
    PREFERRED_FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    SHOW_CODE_FIELD_NUMBER: _ClassVar[int]
    STEERING_FIELD_NUMBER: _ClassVar[int]
    preferred_first_name: _wrappers_pb2.StringValue
    preferred_last_name: _wrappers_pb2.StringValue
    show_code: _wrappers_pb2.BoolValue
    steering: _wrappers_pb2.BoolValue

    def __init__(self, preferred_first_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]]=..., preferred_last_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]]=..., show_code: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., steering: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=...) -> None:
        ...

class UpdateCurrentMemberProfileResponse(_message.Message):
    __slots__ = ('member',)
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: _auth_pb2.Member

    def __init__(self, member: _Optional[_Union[_auth_pb2.Member, _Mapping]]=...) -> None:
        ...

class CheckMemberStatusRequest(_message.Message):
    __slots__ = ('force_refresh',)
    FORCE_REFRESH_FIELD_NUMBER: _ClassVar[int]
    force_refresh: bool

    def __init__(self, force_refresh: bool=...) -> None:
        ...

class CheckMemberStatusResponse(_message.Message):
    __slots__ = ('is_suspended', 'console_access', 'is_suspended_manual', 'is_suspended_overage', 'is_suspended_usage', 'is_suspended_member_usage', 'suspension_message', 'suspended_cost_centers', 'is_suspended_org_limit')
    IS_SUSPENDED_FIELD_NUMBER: _ClassVar[int]
    CONSOLE_ACCESS_FIELD_NUMBER: _ClassVar[int]
    IS_SUSPENDED_MANUAL_FIELD_NUMBER: _ClassVar[int]
    IS_SUSPENDED_OVERAGE_FIELD_NUMBER: _ClassVar[int]
    IS_SUSPENDED_USAGE_FIELD_NUMBER: _ClassVar[int]
    IS_SUSPENDED_MEMBER_USAGE_FIELD_NUMBER: _ClassVar[int]
    SUSPENSION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SUSPENDED_COST_CENTERS_FIELD_NUMBER: _ClassVar[int]
    IS_SUSPENDED_ORG_LIMIT_FIELD_NUMBER: _ClassVar[int]
    is_suspended: bool
    console_access: bool
    is_suspended_manual: bool
    is_suspended_overage: bool
    is_suspended_usage: bool
    is_suspended_member_usage: bool
    suspension_message: str
    suspended_cost_centers: _containers.RepeatedScalarFieldContainer[str]
    is_suspended_org_limit: bool

    def __init__(self, is_suspended: bool=..., console_access: bool=..., is_suspended_manual: bool=..., is_suspended_overage: bool=..., is_suspended_usage: bool=..., is_suspended_member_usage: bool=..., suspension_message: _Optional[str]=..., suspended_cost_centers: _Optional[_Iterable[str]]=..., is_suspended_org_limit: bool=...) -> None:
        ...

class ModelDeprecationInfo(_message.Message):
    __slots__ = ('deprecated_model', 'successor_model', 'deprecated_model_name', 'successor_model_name', 'deprecation_date')
    DEPRECATED_MODEL_FIELD_NUMBER: _ClassVar[int]
    SUCCESSOR_MODEL_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    SUCCESSOR_MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    DEPRECATION_DATE_FIELD_NUMBER: _ClassVar[int]
    deprecated_model: int
    successor_model: int
    deprecated_model_name: str
    successor_model_name: str
    deprecation_date: str

    def __init__(self, deprecated_model: _Optional[int]=..., successor_model: _Optional[int]=..., deprecated_model_name: _Optional[str]=..., successor_model_name: _Optional[str]=..., deprecation_date: _Optional[str]=...) -> None:
        ...

class GetModelDeprecationsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetModelDeprecationsResponse(_message.Message):
    __slots__ = ('deprecations',)
    DEPRECATIONS_FIELD_NUMBER: _ClassVar[int]
    deprecations: _containers.RepeatedCompositeFieldContainer[ModelDeprecationInfo]

    def __init__(self, deprecations: _Optional[_Iterable[_Union[ModelDeprecationInfo, _Mapping]]]=...) -> None:
        ...