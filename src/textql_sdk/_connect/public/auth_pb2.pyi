import datetime
import auth_pb2 as _auth_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
import paradigm_params_pb2 as _paradigm_params_pb2
from public import chat_pb2 as _chat_pb2
from public import options_pb2 as _options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class UpdateDefaultConnectorRequest(_message.Message):
    __slots__ = ('connector_ids', 'paradigm_params', 'clear_paradigm_params', 'default_methodology', 'default_llm_model', 'default_fast_mode')
    CONNECTOR_IDS_FIELD_NUMBER: _ClassVar[int]
    PARADIGM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CLEAR_PARADIGM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_METHODOLOGY_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LLM_MODEL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FAST_MODE_FIELD_NUMBER: _ClassVar[int]
    connector_ids: _containers.RepeatedScalarFieldContainer[int]
    paradigm_params: _paradigm_params_pb2.ParadigmParams
    clear_paradigm_params: bool
    default_methodology: _chat_pb2.Methodology
    default_llm_model: int
    default_fast_mode: bool

    def __init__(self, connector_ids: _Optional[_Iterable[int]]=..., paradigm_params: _Optional[_Union[_paradigm_params_pb2.ParadigmParams, _Mapping]]=..., clear_paradigm_params: bool=..., default_methodology: _Optional[_Union[_chat_pb2.Methodology, str]]=..., default_llm_model: _Optional[int]=..., default_fast_mode: bool=...) -> None:
        ...

class UpdateDefaultConnectorResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class LoginEmailStartRequest(_message.Message):
    __slots__ = ('email', 'custom_callback_url', 'custom_subject', 'custom_body_html', 'custom_sender_name', 'autojoin_token', 'oauth_resume')
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CALLBACK_URL_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_SUBJECT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_BODY_HTML_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_SENDER_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTOJOIN_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OAUTH_RESUME_FIELD_NUMBER: _ClassVar[int]
    email: str
    custom_callback_url: str
    custom_subject: str
    custom_body_html: str
    custom_sender_name: str
    autojoin_token: str
    oauth_resume: str

    def __init__(self, email: _Optional[str]=..., custom_callback_url: _Optional[str]=..., custom_subject: _Optional[str]=..., custom_body_html: _Optional[str]=..., custom_sender_name: _Optional[str]=..., autojoin_token: _Optional[str]=..., oauth_resume: _Optional[str]=...) -> None:
        ...

class LoginEmailStartResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ValidateIntermediaryTokenRequest(_message.Message):
    __slots__ = ('intermediary_token',)
    INTERMEDIARY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    intermediary_token: str

    def __init__(self, intermediary_token: _Optional[str]=...) -> None:
        ...

class ValidateIntermediaryTokenResponse(_message.Message):
    __slots__ = ('organizations', 'provider_id')
    ORGANIZATIONS_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    organizations: _containers.RepeatedCompositeFieldContainer[_auth_pb2.Organization]
    provider_id: str

    def __init__(self, organizations: _Optional[_Iterable[_Union[_auth_pb2.Organization, _Mapping]]]=..., provider_id: _Optional[str]=...) -> None:
        ...

class ValidateLongTermTokenRequest(_message.Message):
    __slots__ = ('long_term_access_token',)
    LONG_TERM_ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    long_term_access_token: str

    def __init__(self, long_term_access_token: _Optional[str]=...) -> None:
        ...

class ValidateLongTermTokenResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ExchangeIntermediaryTokenRequest(_message.Message):
    __slots__ = ('intermediary_token', 'organization_id')
    INTERMEDIARY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    intermediary_token: str
    organization_id: str

    def __init__(self, intermediary_token: _Optional[str]=..., organization_id: _Optional[str]=...) -> None:
        ...

class GetOIDCAuthUrlRequest(_message.Message):
    __slots__ = ('provider_id', 'oauth_resume')
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    OAUTH_RESUME_FIELD_NUMBER: _ClassVar[int]
    provider_id: str
    oauth_resume: str

    def __init__(self, provider_id: _Optional[str]=..., oauth_resume: _Optional[str]=...) -> None:
        ...

class GetOIDCAuthUrlResponse(_message.Message):
    __slots__ = ('auth_url',)
    AUTH_URL_FIELD_NUMBER: _ClassVar[int]
    auth_url: str

    def __init__(self, auth_url: _Optional[str]=...) -> None:
        ...

class HandleOIDCCallbackRequest(_message.Message):
    __slots__ = ('code', 'state')
    CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    code: str
    state: str

    def __init__(self, code: _Optional[str]=..., state: _Optional[str]=...) -> None:
        ...

class HandleOIDCCallbackResponse(_message.Message):
    __slots__ = ('success', 'intermediary_token', 'error', 'provider_id', 'oauth_resume')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    INTERMEDIARY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    OAUTH_RESUME_FIELD_NUMBER: _ClassVar[int]
    success: bool
    intermediary_token: str
    error: str
    provider_id: str
    oauth_resume: str

    def __init__(self, success: bool=..., intermediary_token: _Optional[str]=..., error: _Optional[str]=..., provider_id: _Optional[str]=..., oauth_resume: _Optional[str]=...) -> None:
        ...

class LogoutRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class LogoutResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class CreateSSOOrganizationRequest(_message.Message):
    __slots__ = ('name', 'icon', 'oidc_issuer', 'oidc_client_id', 'oidc_client_secret')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    OIDC_ISSUER_FIELD_NUMBER: _ClassVar[int]
    OIDC_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    OIDC_CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    name: str
    icon: str
    oidc_issuer: str
    oidc_client_id: str
    oidc_client_secret: str

    def __init__(self, name: _Optional[str]=..., icon: _Optional[str]=..., oidc_issuer: _Optional[str]=..., oidc_client_id: _Optional[str]=..., oidc_client_secret: _Optional[str]=...) -> None:
        ...

class CreateSSOOrganizationResponse(_message.Message):
    __slots__ = ('success', 'organization', 'error')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    organization: _auth_pb2.Organization
    error: str

    def __init__(self, success: bool=..., organization: _Optional[_Union[_auth_pb2.Organization, _Mapping]]=..., error: _Optional[str]=...) -> None:
        ...

class ListOrganizationsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListOrganizationsResponse(_message.Message):
    __slots__ = ('organizations',)
    ORGANIZATIONS_FIELD_NUMBER: _ClassVar[int]
    organizations: _containers.RepeatedCompositeFieldContainer[_auth_pb2.Organization]

    def __init__(self, organizations: _Optional[_Iterable[_Union[_auth_pb2.Organization, _Mapping]]]=...) -> None:
        ...

class GetMemberRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetMemberResponse(_message.Message):
    __slots__ = ('member',)
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: _auth_pb2.Member

    def __init__(self, member: _Optional[_Union[_auth_pb2.Member, _Mapping]]=...) -> None:
        ...

class ExchangeSessionRequest(_message.Message):
    __slots__ = ('organization_id',)
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    organization_id: str

    def __init__(self, organization_id: _Optional[str]=...) -> None:
        ...

class ExchangeSessionResponse(_message.Message):
    __slots__ = ('member', 'warnings')
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    member: _auth_pb2.Member
    warnings: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, member: _Optional[_Union[_auth_pb2.Member, _Mapping]]=..., warnings: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetOrganizationRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetOrganizationResponse(_message.Message):
    __slots__ = ('organization',)
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    organization: _auth_pb2.Organization

    def __init__(self, organization: _Optional[_Union[_auth_pb2.Organization, _Mapping]]=...) -> None:
        ...

class GetMemberInOrgByIdRequest(_message.Message):
    __slots__ = ('member_id', 'org_id')
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    org_id: str

    def __init__(self, member_id: _Optional[str]=..., org_id: _Optional[str]=...) -> None:
        ...

class GetMemberInOrgByIdResponse(_message.Message):
    __slots__ = ('member',)
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: _auth_pb2.Member

    def __init__(self, member: _Optional[_Union[_auth_pb2.Member, _Mapping]]=...) -> None:
        ...

class GetOIDCConfigRequest(_message.Message):
    __slots__ = ('organization_id',)
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    organization_id: str

    def __init__(self, organization_id: _Optional[str]=...) -> None:
        ...

class GetOIDCConfigResponse(_message.Message):
    __slots__ = ('config',)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: _auth_pb2.OIDCConfig

    def __init__(self, config: _Optional[_Union[_auth_pb2.OIDCConfig, _Mapping]]=...) -> None:
        ...

class SaveOIDCConfigRequest(_message.Message):
    __slots__ = ('config',)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: _auth_pb2.OIDCConfig

    def __init__(self, config: _Optional[_Union[_auth_pb2.OIDCConfig, _Mapping]]=...) -> None:
        ...

class SaveOIDCConfigResponse(_message.Message):
    __slots__ = ('success', 'message')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str

    def __init__(self, success: bool=..., message: _Optional[str]=...) -> None:
        ...

class CheckDomainForOIDCRequest(_message.Message):
    __slots__ = ('email_domain',)
    EMAIL_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    email_domain: str

    def __init__(self, email_domain: _Optional[str]=...) -> None:
        ...

class OIDCProviderInfo(_message.Message):
    __slots__ = ('provider_id', 'display_name', 'issuer_url', 'org_count')
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ISSUER_URL_FIELD_NUMBER: _ClassVar[int]
    ORG_COUNT_FIELD_NUMBER: _ClassVar[int]
    provider_id: str
    display_name: str
    issuer_url: str
    org_count: int

    def __init__(self, provider_id: _Optional[str]=..., display_name: _Optional[str]=..., issuer_url: _Optional[str]=..., org_count: _Optional[int]=...) -> None:
        ...

class CheckDomainForOIDCResponse(_message.Message):
    __slots__ = ('use_oidc', 'providers')
    USE_OIDC_FIELD_NUMBER: _ClassVar[int]
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    use_oidc: bool
    providers: _containers.RepeatedCompositeFieldContainer[OIDCProviderInfo]

    def __init__(self, use_oidc: bool=..., providers: _Optional[_Iterable[_Union[OIDCProviderInfo, _Mapping]]]=...) -> None:
        ...

class GetGoogleOAuthUrlRequest(_message.Message):
    __slots__ = ('oauth_resume',)
    OAUTH_RESUME_FIELD_NUMBER: _ClassVar[int]
    oauth_resume: str

    def __init__(self, oauth_resume: _Optional[str]=...) -> None:
        ...

class GetGoogleOAuthUrlResponse(_message.Message):
    __slots__ = ('auth_url',)
    AUTH_URL_FIELD_NUMBER: _ClassVar[int]
    auth_url: str

    def __init__(self, auth_url: _Optional[str]=...) -> None:
        ...

class HandleGoogleOAuthCallbackRequest(_message.Message):
    __slots__ = ('code', 'state')
    CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    code: str
    state: str

    def __init__(self, code: _Optional[str]=..., state: _Optional[str]=...) -> None:
        ...

class HandleGoogleOAuthCallbackResponse(_message.Message):
    __slots__ = ('success', 'intermediary_token', 'error', 'oauth_resume')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    INTERMEDIARY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    OAUTH_RESUME_FIELD_NUMBER: _ClassVar[int]
    success: bool
    intermediary_token: str
    error: str
    oauth_resume: str

    def __init__(self, success: bool=..., intermediary_token: _Optional[str]=..., error: _Optional[str]=..., oauth_resume: _Optional[str]=...) -> None:
        ...

class UpdateOrgThemeRequest(_message.Message):
    __slots__ = ('org_id', 'theme')
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    THEME_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    theme: _auth_pb2.Theme

    def __init__(self, org_id: _Optional[str]=..., theme: _Optional[_Union[_auth_pb2.Theme, _Mapping]]=...) -> None:
        ...

class UpdateOrgThemeResponse(_message.Message):
    __slots__ = ('organization',)
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    organization: _auth_pb2.Organization

    def __init__(self, organization: _Optional[_Union[_auth_pb2.Organization, _Mapping]]=...) -> None:
        ...

class UpdateOrgToolRestrictionsRequest(_message.Message):
    __slots__ = ('org_id', 'tool_restrictions')
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    tool_restrictions: _paradigm_params_pb2.ParadigmParams

    def __init__(self, org_id: _Optional[str]=..., tool_restrictions: _Optional[_Union[_paradigm_params_pb2.ParadigmParams, _Mapping]]=...) -> None:
        ...

class UpdateOrgToolRestrictionsResponse(_message.Message):
    __slots__ = ('organization',)
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    organization: _auth_pb2.Organization

    def __init__(self, organization: _Optional[_Union[_auth_pb2.Organization, _Mapping]]=...) -> None:
        ...

class CreateLogoUploadPresignUrlRequest(_message.Message):
    __slots__ = ('org_id', 'file_name')
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    file_name: str

    def __init__(self, org_id: _Optional[str]=..., file_name: _Optional[str]=...) -> None:
        ...

class CreateLogoUploadPresignUrlResponse(_message.Message):
    __slots__ = ('upload_id', 'presign_url')
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    PRESIGN_URL_FIELD_NUMBER: _ClassVar[int]
    upload_id: str
    presign_url: str

    def __init__(self, upload_id: _Optional[str]=..., presign_url: _Optional[str]=...) -> None:
        ...

class ProcessLogoUploadPresignUrlRequest(_message.Message):
    __slots__ = ('org_id', 'upload_id', 'update_theme', 'update_org_logo')
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_THEME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ORG_LOGO_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    upload_id: str
    update_theme: bool
    update_org_logo: bool

    def __init__(self, org_id: _Optional[str]=..., upload_id: _Optional[str]=..., update_theme: bool=..., update_org_logo: bool=...) -> None:
        ...

class ProcessLogoUploadPresignUrlResponse(_message.Message):
    __slots__ = ('logo_url', 'organization')
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    logo_url: str
    organization: _auth_pb2.Organization

    def __init__(self, logo_url: _Optional[str]=..., organization: _Optional[_Union[_auth_pb2.Organization, _Mapping]]=...) -> None:
        ...

class UploadMemberImageRequest(_message.Message):
    __slots__ = ('member_id', 'image_data', 'file_name')
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_DATA_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    image_data: bytes
    file_name: str

    def __init__(self, member_id: _Optional[str]=..., image_data: _Optional[bytes]=..., file_name: _Optional[str]=...) -> None:
        ...

class UploadMemberImageResponse(_message.Message):
    __slots__ = ('image_url',)
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    image_url: str

    def __init__(self, image_url: _Optional[str]=...) -> None:
        ...

class GenerateMagicLinkForUserRequest(_message.Message):
    __slots__ = ('email',)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str

    def __init__(self, email: _Optional[str]=...) -> None:
        ...

class GenerateMagicLinkForUserResponse(_message.Message):
    __slots__ = ('magic_link',)
    MAGIC_LINK_FIELD_NUMBER: _ClassVar[int]
    magic_link: str

    def __init__(self, magic_link: _Optional[str]=...) -> None:
        ...

class GetConsoleAuthTokenRequest(_message.Message):
    __slots__ = ('debug_level',)
    DEBUG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    debug_level: int

    def __init__(self, debug_level: _Optional[int]=...) -> None:
        ...

class GetConsoleAuthTokenResponse(_message.Message):
    __slots__ = ('intermediary_token', 'console_url')
    INTERMEDIARY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CONSOLE_URL_FIELD_NUMBER: _ClassVar[int]
    intermediary_token: str
    console_url: str

    def __init__(self, intermediary_token: _Optional[str]=..., console_url: _Optional[str]=...) -> None:
        ...

class OIDCProvider(_message.Message):
    __slots__ = ('provider_id', 'display_name', 'issuer_url', 'client_id', 'client_secret', 'scopes', 'provider_type', 'attribute_mapping', 'created_at', 'updated_at', 'env_configured')
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ISSUER_URL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_MAPPING_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    ENV_CONFIGURED_FIELD_NUMBER: _ClassVar[int]
    provider_id: str
    display_name: str
    issuer_url: str
    client_id: str
    client_secret: str
    scopes: _containers.RepeatedScalarFieldContainer[str]
    provider_type: str
    attribute_mapping: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    env_configured: bool

    def __init__(self, provider_id: _Optional[str]=..., display_name: _Optional[str]=..., issuer_url: _Optional[str]=..., client_id: _Optional[str]=..., client_secret: _Optional[str]=..., scopes: _Optional[_Iterable[str]]=..., provider_type: _Optional[str]=..., attribute_mapping: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., env_configured: bool=...) -> None:
        ...

class OIDCProviderWithOrgs(_message.Message):
    __slots__ = ('provider', 'org_count')
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    ORG_COUNT_FIELD_NUMBER: _ClassVar[int]
    provider: OIDCProvider
    org_count: int

    def __init__(self, provider: _Optional[_Union[OIDCProvider, _Mapping]]=..., org_count: _Optional[int]=...) -> None:
        ...

class ListOIDCProvidersRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListOIDCProvidersResponse(_message.Message):
    __slots__ = ('providers',)
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    providers: _containers.RepeatedCompositeFieldContainer[OIDCProviderWithOrgs]

    def __init__(self, providers: _Optional[_Iterable[_Union[OIDCProviderWithOrgs, _Mapping]]]=...) -> None:
        ...

class CreateOIDCProviderRequest(_message.Message):
    __slots__ = ('display_name', 'issuer_url', 'client_id', 'client_secret', 'scopes', 'provider_type', 'attribute_mapping')
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ISSUER_URL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_MAPPING_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    issuer_url: str
    client_id: str
    client_secret: str
    scopes: _containers.RepeatedScalarFieldContainer[str]
    provider_type: str
    attribute_mapping: str

    def __init__(self, display_name: _Optional[str]=..., issuer_url: _Optional[str]=..., client_id: _Optional[str]=..., client_secret: _Optional[str]=..., scopes: _Optional[_Iterable[str]]=..., provider_type: _Optional[str]=..., attribute_mapping: _Optional[str]=...) -> None:
        ...

class CreateOIDCProviderResponse(_message.Message):
    __slots__ = ('success', 'provider_id', 'error', 'is_duplicate', 'existing_provider')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    IS_DUPLICATE_FIELD_NUMBER: _ClassVar[int]
    EXISTING_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    success: bool
    provider_id: str
    error: str
    is_duplicate: bool
    existing_provider: OIDCProvider

    def __init__(self, success: bool=..., provider_id: _Optional[str]=..., error: _Optional[str]=..., is_duplicate: bool=..., existing_provider: _Optional[_Union[OIDCProvider, _Mapping]]=...) -> None:
        ...

class UpdateOIDCProviderRequest(_message.Message):
    __slots__ = ('provider_id', 'display_name', 'issuer_url', 'client_id', 'client_secret', 'scopes', 'provider_type', 'attribute_mapping')
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ISSUER_URL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_MAPPING_FIELD_NUMBER: _ClassVar[int]
    provider_id: str
    display_name: str
    issuer_url: str
    client_id: str
    client_secret: str
    scopes: _containers.RepeatedScalarFieldContainer[str]
    provider_type: str
    attribute_mapping: str

    def __init__(self, provider_id: _Optional[str]=..., display_name: _Optional[str]=..., issuer_url: _Optional[str]=..., client_id: _Optional[str]=..., client_secret: _Optional[str]=..., scopes: _Optional[_Iterable[str]]=..., provider_type: _Optional[str]=..., attribute_mapping: _Optional[str]=...) -> None:
        ...

class UpdateOIDCProviderResponse(_message.Message):
    __slots__ = ('success', 'error')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: str

    def __init__(self, success: bool=..., error: _Optional[str]=...) -> None:
        ...

class DeleteOIDCProviderRequest(_message.Message):
    __slots__ = ('provider_id',)
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    provider_id: str

    def __init__(self, provider_id: _Optional[str]=...) -> None:
        ...

class DeleteOIDCProviderResponse(_message.Message):
    __slots__ = ('success', 'error')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: str

    def __init__(self, success: bool=..., error: _Optional[str]=...) -> None:
        ...

class AddOrgOIDCProviderRequest(_message.Message):
    __slots__ = ('org_id', 'provider_id')
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    provider_id: str

    def __init__(self, org_id: _Optional[str]=..., provider_id: _Optional[str]=...) -> None:
        ...

class AddOrgOIDCProviderResponse(_message.Message):
    __slots__ = ('success', 'error')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: str

    def __init__(self, success: bool=..., error: _Optional[str]=...) -> None:
        ...

class RemoveOrgOIDCProviderRequest(_message.Message):
    __slots__ = ('org_id', 'provider_id')
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    provider_id: str

    def __init__(self, org_id: _Optional[str]=..., provider_id: _Optional[str]=...) -> None:
        ...

class RemoveOrgOIDCProviderResponse(_message.Message):
    __slots__ = ('success', 'error')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: str

    def __init__(self, success: bool=..., error: _Optional[str]=...) -> None:
        ...

class UpdateOrgOIDCProvidersRequest(_message.Message):
    __slots__ = ('org_id', 'provider_ids')
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_IDS_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    provider_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, org_id: _Optional[str]=..., provider_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class UpdateOrgOIDCProvidersResponse(_message.Message):
    __slots__ = ('success', 'error')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: str

    def __init__(self, success: bool=..., error: _Optional[str]=...) -> None:
        ...

class GetOrgOIDCProvidersRequest(_message.Message):
    __slots__ = ('org_id',)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str

    def __init__(self, org_id: _Optional[str]=...) -> None:
        ...

class GetOrgOIDCProvidersResponse(_message.Message):
    __slots__ = ('providers',)
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    providers: _containers.RepeatedCompositeFieldContainer[OIDCProvider]

    def __init__(self, providers: _Optional[_Iterable[_Union[OIDCProvider, _Mapping]]]=...) -> None:
        ...

class CreateOrganizationRequest(_message.Message):
    __slots__ = ('intermediary_token', 'organization_name')
    INTERMEDIARY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
    intermediary_token: str
    organization_name: str

    def __init__(self, intermediary_token: _Optional[str]=..., organization_name: _Optional[str]=...) -> None:
        ...

class CreateOrganizationResponse(_message.Message):
    __slots__ = ('success', 'error', 'organization')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: str
    organization: _auth_pb2.Organization

    def __init__(self, success: bool=..., error: _Optional[str]=..., organization: _Optional[_Union[_auth_pb2.Organization, _Mapping]]=...) -> None:
        ...

class CreateSiblingOrganizationRequest(_message.Message):
    __slots__ = ('source_org_id', 'new_org_name')
    SOURCE_ORG_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_ORG_NAME_FIELD_NUMBER: _ClassVar[int]
    source_org_id: str
    new_org_name: str

    def __init__(self, source_org_id: _Optional[str]=..., new_org_name: _Optional[str]=...) -> None:
        ...

class CreateSiblingOrganizationResponse(_message.Message):
    __slots__ = ('success', 'error', 'new_org_id', 'new_organization')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NEW_ORG_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: str
    new_org_id: str
    new_organization: _auth_pb2.Organization

    def __init__(self, success: bool=..., error: _Optional[str]=..., new_org_id: _Optional[str]=..., new_organization: _Optional[_Union[_auth_pb2.Organization, _Mapping]]=...) -> None:
        ...

class VerifyApiKeyRequest(_message.Message):
    __slots__ = ('api_key_base64', 'required_resource', 'required_action')
    API_KEY_BASE64_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ACTION_FIELD_NUMBER: _ClassVar[int]
    api_key_base64: str
    required_resource: str
    required_action: str

    def __init__(self, api_key_base64: _Optional[str]=..., required_resource: _Optional[str]=..., required_action: _Optional[str]=...) -> None:
        ...

class VerifyApiKeyResponse(_message.Message):
    __slots__ = ('valid', 'member_id', 'organization_id', 'client_id')
    VALID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    valid: bool
    member_id: str
    organization_id: str
    client_id: str

    def __init__(self, valid: bool=..., member_id: _Optional[str]=..., organization_id: _Optional[str]=..., client_id: _Optional[str]=...) -> None:
        ...

class OrgOAuthClient(_message.Message):
    __slots__ = ('client_id', 'client_name', 'created_at', 'active_tokens', 'distinct_members', 'redirect_uris', 'scope', 'admin_managed', 'created_by_member_id')
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_TOKENS_FIELD_NUMBER: _ClassVar[int]
    DISTINCT_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URIS_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    ADMIN_MANAGED_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    client_name: str
    created_at: _timestamp_pb2.Timestamp
    active_tokens: int
    distinct_members: int
    redirect_uris: _containers.RepeatedScalarFieldContainer[str]
    scope: str
    admin_managed: bool
    created_by_member_id: str

    def __init__(self, client_id: _Optional[str]=..., client_name: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., active_tokens: _Optional[int]=..., distinct_members: _Optional[int]=..., redirect_uris: _Optional[_Iterable[str]]=..., scope: _Optional[str]=..., admin_managed: bool=..., created_by_member_id: _Optional[str]=...) -> None:
        ...

class AuthorizedApp(_message.Message):
    __slots__ = ('client_id', 'client_name', 'scope', 'first_authorized_at', 'last_authorized_at')
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    FIRST_AUTHORIZED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_AUTHORIZED_AT_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    client_name: str
    scope: str
    first_authorized_at: _timestamp_pb2.Timestamp
    last_authorized_at: _timestamp_pb2.Timestamp

    def __init__(self, client_id: _Optional[str]=..., client_name: _Optional[str]=..., scope: _Optional[str]=..., first_authorized_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., last_authorized_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListOrgOAuthClientsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListOrgOAuthClientsResponse(_message.Message):
    __slots__ = ('clients',)
    CLIENTS_FIELD_NUMBER: _ClassVar[int]
    clients: _containers.RepeatedCompositeFieldContainer[OrgOAuthClient]

    def __init__(self, clients: _Optional[_Iterable[_Union[OrgOAuthClient, _Mapping]]]=...) -> None:
        ...

class CreateOrgOAuthClientRequest(_message.Message):
    __slots__ = ('client_name', 'redirect_uris', 'scopes')
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URIS_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    client_name: str
    redirect_uris: _containers.RepeatedScalarFieldContainer[str]
    scopes: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, client_name: _Optional[str]=..., redirect_uris: _Optional[_Iterable[str]]=..., scopes: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateOrgOAuthClientResponse(_message.Message):
    __slots__ = ('client_id', 'client_secret', 'client')
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    client_secret: str
    client: OrgOAuthClient

    def __init__(self, client_id: _Optional[str]=..., client_secret: _Optional[str]=..., client: _Optional[_Union[OrgOAuthClient, _Mapping]]=...) -> None:
        ...

class UpdateOrgOAuthClientRequest(_message.Message):
    __slots__ = ('client_id', 'client_name', 'redirect_uris', 'scopes')
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URIS_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    client_name: str
    redirect_uris: _containers.RepeatedScalarFieldContainer[str]
    scopes: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, client_id: _Optional[str]=..., client_name: _Optional[str]=..., redirect_uris: _Optional[_Iterable[str]]=..., scopes: _Optional[_Iterable[str]]=...) -> None:
        ...

class UpdateOrgOAuthClientResponse(_message.Message):
    __slots__ = ('client',)
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    client: OrgOAuthClient

    def __init__(self, client: _Optional[_Union[OrgOAuthClient, _Mapping]]=...) -> None:
        ...

class RotateOrgOAuthClientSecretRequest(_message.Message):
    __slots__ = ('client_id',)
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str

    def __init__(self, client_id: _Optional[str]=...) -> None:
        ...

class RotateOrgOAuthClientSecretResponse(_message.Message):
    __slots__ = ('client_secret',)
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    client_secret: str

    def __init__(self, client_secret: _Optional[str]=...) -> None:
        ...

class RevokeOrgOAuthClientRequest(_message.Message):
    __slots__ = ('client_id',)
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str

    def __init__(self, client_id: _Optional[str]=...) -> None:
        ...

class RevokeOrgOAuthClientResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DeleteOrgOAuthClientRequest(_message.Message):
    __slots__ = ('client_id',)
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str

    def __init__(self, client_id: _Optional[str]=...) -> None:
        ...

class DeleteOrgOAuthClientResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListMyAuthorizedAppsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListMyAuthorizedAppsResponse(_message.Message):
    __slots__ = ('apps',)
    APPS_FIELD_NUMBER: _ClassVar[int]
    apps: _containers.RepeatedCompositeFieldContainer[AuthorizedApp]

    def __init__(self, apps: _Optional[_Iterable[_Union[AuthorizedApp, _Mapping]]]=...) -> None:
        ...

class RevokeMyAuthorizedAppRequest(_message.Message):
    __slots__ = ('client_id',)
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str

    def __init__(self, client_id: _Optional[str]=...) -> None:
        ...

class RevokeMyAuthorizedAppResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class OAuthScopeInfo(_message.Message):
    __slots__ = ('id', 'description', 'category')
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    id: str
    description: str
    category: str

    def __init__(self, id: _Optional[str]=..., description: _Optional[str]=..., category: _Optional[str]=...) -> None:
        ...

class ListOAuthScopesRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListOAuthScopesResponse(_message.Message):
    __slots__ = ('scopes',)
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    scopes: _containers.RepeatedCompositeFieldContainer[OAuthScopeInfo]

    def __init__(self, scopes: _Optional[_Iterable[_Union[OAuthScopeInfo, _Mapping]]]=...) -> None:
        ...