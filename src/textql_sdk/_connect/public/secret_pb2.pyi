# pylint: skip-file
# mypy: ignore-errors
# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
import datetime
from ..google.api import visibility_pb2 as _visibility_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ..public import identity_pb2 as _identity_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class BodyContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BODY_CONTENT_TYPE_NONE: _ClassVar[BodyContentType]
    BODY_CONTENT_TYPE_JSON: _ClassVar[BodyContentType]
    BODY_CONTENT_TYPE_FORM: _ClassVar[BodyContentType]
BODY_CONTENT_TYPE_NONE: BodyContentType
BODY_CONTENT_TYPE_JSON: BodyContentType
BODY_CONTENT_TYPE_FORM: BodyContentType

class Secret(_message.Message):
    __slots__ = ('id', 'name', 'created_at', 'updated_at', 'description', 'link', 'created_by', 'access_type', 'is_public')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    description: str
    link: str
    created_by: str
    access_type: str
    is_public: bool

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., link: _Optional[str]=..., created_by: _Optional[str]=..., access_type: _Optional[str]=..., is_public: bool=...) -> None:
        ...

class ListSecretsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListSecretsResponse(_message.Message):
    __slots__ = ('secrets',)
    SECRETS_FIELD_NUMBER: _ClassVar[int]
    secrets: _containers.RepeatedCompositeFieldContainer[Secret]

    def __init__(self, secrets: _Optional[_Iterable[_Union[Secret, _Mapping]]]=...) -> None:
        ...

class PutSecretRequest(_message.Message):
    __slots__ = ('name', 'value', 'description', 'link', 'is_private')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    IS_PRIVATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    description: str
    link: str
    is_private: bool

    def __init__(self, name: _Optional[str]=..., value: _Optional[str]=..., description: _Optional[str]=..., link: _Optional[str]=..., is_private: bool=...) -> None:
        ...

class PutSecretResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class UpdateSecretRequest(_message.Message):
    __slots__ = ('name', 'value', 'description', 'link')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    description: str
    link: str

    def __init__(self, name: _Optional[str]=..., value: _Optional[str]=..., description: _Optional[str]=..., link: _Optional[str]=...) -> None:
        ...

class UpdateSecretResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DeleteSecretRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteSecretResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetMembersWithSecretsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetMembersWithSecretsResponse(_message.Message):
    __slots__ = ('members',)
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    members: _containers.RepeatedCompositeFieldContainer[_identity_pb2.MemberPreview]

    def __init__(self, members: _Optional[_Iterable[_Union[_identity_pb2.MemberPreview, _Mapping]]]=...) -> None:
        ...

class HttpBasicAuth(_message.Message):
    __slots__ = ('username', 'password')
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str

    def __init__(self, username: _Optional[str]=..., password: _Optional[str]=...) -> None:
        ...

class ApiAccessRef(_message.Message):
    __slots__ = ('api_access_key_id', 'revision')
    API_ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    api_access_key_id: str
    revision: int

    def __init__(self, api_access_key_id: _Optional[str]=..., revision: _Optional[int]=...) -> None:
        ...

class ApiAccessKey(_message.Message):
    __slots__ = ('id', 'org_id', 'member_id', 'hosts', 'headers', 'query_params', 'description', 'created_at', 'updated_at', 'expires_at', 'provider', 'auth_type', 'member_oauth_authenticated', 'member_oauth_display_name', 'http_basic_auth', 'body', 'content_type', 'can_write', 'access_type', 'is_public', 'test_url', 'name', 'auth_prefix')

    class HeadersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class QueryParamsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class BodyEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    QUERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_OAUTH_AUTHENTICATED_FIELD_NUMBER: _ClassVar[int]
    MEMBER_OAUTH_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    HTTP_BASIC_AUTH_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CAN_WRITE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    TEST_URL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AUTH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    id: str
    org_id: str
    member_id: str
    hosts: _containers.RepeatedScalarFieldContainer[str]
    headers: _containers.ScalarMap[str, str]
    query_params: _containers.ScalarMap[str, str]
    description: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    provider: str
    auth_type: str
    member_oauth_authenticated: bool
    member_oauth_display_name: str
    http_basic_auth: HttpBasicAuth
    body: _containers.ScalarMap[str, str]
    content_type: BodyContentType
    can_write: bool
    access_type: str
    is_public: bool
    test_url: str
    name: str
    auth_prefix: str

    def __init__(self, id: _Optional[str]=..., org_id: _Optional[str]=..., member_id: _Optional[str]=..., hosts: _Optional[_Iterable[str]]=..., headers: _Optional[_Mapping[str, str]]=..., query_params: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., provider: _Optional[str]=..., auth_type: _Optional[str]=..., member_oauth_authenticated: bool=..., member_oauth_display_name: _Optional[str]=..., http_basic_auth: _Optional[_Union[HttpBasicAuth, _Mapping]]=..., body: _Optional[_Mapping[str, str]]=..., content_type: _Optional[_Union[BodyContentType, str]]=..., can_write: bool=..., access_type: _Optional[str]=..., is_public: bool=..., test_url: _Optional[str]=..., name: _Optional[str]=..., auth_prefix: _Optional[str]=...) -> None:
        ...

class CreateApiRevisionRequest(_message.Message):
    __slots__ = ('api_access_key_id',)
    API_ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    api_access_key_id: str

    def __init__(self, api_access_key_id: _Optional[str]=...) -> None:
        ...

class CreateApiRevisionResponse(_message.Message):
    __slots__ = ('ref', 'api_access_key')
    REF_FIELD_NUMBER: _ClassVar[int]
    API_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    ref: ApiAccessRef
    api_access_key: ApiAccessKey

    def __init__(self, ref: _Optional[_Union[ApiAccessRef, _Mapping]]=..., api_access_key: _Optional[_Union[ApiAccessKey, _Mapping]]=...) -> None:
        ...

class UpsertApiAccessKeyRequest(_message.Message):
    __slots__ = ('ref', 'persist_to_db', 'hosts', 'headers', 'query_params', 'description', 'expires_at', 'provider', 'auth_value', 'auth_value_extra', 'auth_type', 'http_basic_auth', 'body', 'content_type', 'test_url', 'name')

    class HeadersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class QueryParamsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class BodyEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    REF_FIELD_NUMBER: _ClassVar[int]
    PERSIST_TO_DB_FIELD_NUMBER: _ClassVar[int]
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    QUERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    AUTH_VALUE_FIELD_NUMBER: _ClassVar[int]
    AUTH_VALUE_EXTRA_FIELD_NUMBER: _ClassVar[int]
    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    HTTP_BASIC_AUTH_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TEST_URL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ref: ApiAccessRef
    persist_to_db: bool
    hosts: _containers.RepeatedScalarFieldContainer[str]
    headers: _containers.ScalarMap[str, str]
    query_params: _containers.ScalarMap[str, str]
    description: str
    expires_at: _timestamp_pb2.Timestamp
    provider: str
    auth_value: str
    auth_value_extra: str
    auth_type: str
    http_basic_auth: HttpBasicAuth
    body: _containers.ScalarMap[str, str]
    content_type: BodyContentType
    test_url: str
    name: str

    def __init__(self, ref: _Optional[_Union[ApiAccessRef, _Mapping]]=..., persist_to_db: bool=..., hosts: _Optional[_Iterable[str]]=..., headers: _Optional[_Mapping[str, str]]=..., query_params: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., provider: _Optional[str]=..., auth_value: _Optional[str]=..., auth_value_extra: _Optional[str]=..., auth_type: _Optional[str]=..., http_basic_auth: _Optional[_Union[HttpBasicAuth, _Mapping]]=..., body: _Optional[_Mapping[str, str]]=..., content_type: _Optional[_Union[BodyContentType, str]]=..., test_url: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class UpsertApiAccessKeyResponse(_message.Message):
    __slots__ = ('api_access_key',)
    API_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    api_access_key: ApiAccessKey

    def __init__(self, api_access_key: _Optional[_Union[ApiAccessKey, _Mapping]]=...) -> None:
        ...

class DeleteApiRevisionRequest(_message.Message):
    __slots__ = ('ref',)
    REF_FIELD_NUMBER: _ClassVar[int]
    ref: ApiAccessRef

    def __init__(self, ref: _Optional[_Union[ApiAccessRef, _Mapping]]=...) -> None:
        ...

class DeleteApiRevisionResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListApiAccessKeysRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListApiAccessKeysResponse(_message.Message):
    __slots__ = ('api_access_keys',)
    API_ACCESS_KEYS_FIELD_NUMBER: _ClassVar[int]
    api_access_keys: _containers.RepeatedCompositeFieldContainer[ApiAccessKey]

    def __init__(self, api_access_keys: _Optional[_Iterable[_Union[ApiAccessKey, _Mapping]]]=...) -> None:
        ...

class GetApiAccessKeyRequest(_message.Message):
    __slots__ = ('id',)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str

    def __init__(self, id: _Optional[str]=...) -> None:
        ...

class GetApiAccessKeyResponse(_message.Message):
    __slots__ = ('api_access_key',)
    API_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    api_access_key: ApiAccessKey

    def __init__(self, api_access_key: _Optional[_Union[ApiAccessKey, _Mapping]]=...) -> None:
        ...

class DeleteApiAccessKeyRequest(_message.Message):
    __slots__ = ('id',)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str

    def __init__(self, id: _Optional[str]=...) -> None:
        ...

class DeleteApiAccessKeyResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class EnvVarField(_message.Message):
    __slots__ = ('env_var', 'label', 'required', 'secret', 'default_value', 'placeholder')
    ENV_VAR_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    env_var: str
    label: str
    required: bool
    secret: bool
    default_value: str
    placeholder: str

    def __init__(self, env_var: _Optional[str]=..., label: _Optional[str]=..., required: bool=..., secret: bool=..., default_value: _Optional[str]=..., placeholder: _Optional[str]=...) -> None:
        ...

class ApiProvider(_message.Message):
    __slots__ = ('id', 'name', 'icon_url', 'auth_type', 'description', 'docs_url', 'default_hosts', 'token_label', 'auth_header', 'auth_prefix', 'oauth_supported', 'oauth_configured', 'member_authenticated', 'member_auth_display_name', 'env_var_fields', 'oauth_has_default_urls', 'oauth_auth_url', 'oauth_token_url', 'oauth_scopes', 'oauth_use_pkce', 'oauth_token_auth_method', 'test_url')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_URL_FIELD_NUMBER: _ClassVar[int]
    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DOCS_URL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_HOSTS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_LABEL_FIELD_NUMBER: _ClassVar[int]
    AUTH_HEADER_FIELD_NUMBER: _ClassVar[int]
    AUTH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    OAUTH_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    OAUTH_CONFIGURED_FIELD_NUMBER: _ClassVar[int]
    MEMBER_AUTHENTICATED_FIELD_NUMBER: _ClassVar[int]
    MEMBER_AUTH_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ENV_VAR_FIELDS_FIELD_NUMBER: _ClassVar[int]
    OAUTH_HAS_DEFAULT_URLS_FIELD_NUMBER: _ClassVar[int]
    OAUTH_AUTH_URL_FIELD_NUMBER: _ClassVar[int]
    OAUTH_TOKEN_URL_FIELD_NUMBER: _ClassVar[int]
    OAUTH_SCOPES_FIELD_NUMBER: _ClassVar[int]
    OAUTH_USE_PKCE_FIELD_NUMBER: _ClassVar[int]
    OAUTH_TOKEN_AUTH_METHOD_FIELD_NUMBER: _ClassVar[int]
    TEST_URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    icon_url: str
    auth_type: str
    description: str
    docs_url: str
    default_hosts: _containers.RepeatedScalarFieldContainer[str]
    token_label: str
    auth_header: str
    auth_prefix: str
    oauth_supported: bool
    oauth_configured: bool
    member_authenticated: bool
    member_auth_display_name: str
    env_var_fields: _containers.RepeatedCompositeFieldContainer[EnvVarField]
    oauth_has_default_urls: bool
    oauth_auth_url: str
    oauth_token_url: str
    oauth_scopes: str
    oauth_use_pkce: bool
    oauth_token_auth_method: str
    test_url: str

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., icon_url: _Optional[str]=..., auth_type: _Optional[str]=..., description: _Optional[str]=..., docs_url: _Optional[str]=..., default_hosts: _Optional[_Iterable[str]]=..., token_label: _Optional[str]=..., auth_header: _Optional[str]=..., auth_prefix: _Optional[str]=..., oauth_supported: bool=..., oauth_configured: bool=..., member_authenticated: bool=..., member_auth_display_name: _Optional[str]=..., env_var_fields: _Optional[_Iterable[_Union[EnvVarField, _Mapping]]]=..., oauth_has_default_urls: bool=..., oauth_auth_url: _Optional[str]=..., oauth_token_url: _Optional[str]=..., oauth_scopes: _Optional[str]=..., oauth_use_pkce: bool=..., oauth_token_auth_method: _Optional[str]=..., test_url: _Optional[str]=...) -> None:
        ...

class TestApiAccessKeyRequest(_message.Message):
    __slots__ = ('ref',)
    REF_FIELD_NUMBER: _ClassVar[int]
    ref: ApiAccessRef

    def __init__(self, ref: _Optional[_Union[ApiAccessRef, _Mapping]]=...) -> None:
        ...

class TestApiAccessKeyResponse(_message.Message):
    __slots__ = ('success', 'status_code', 'message')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    status_code: int
    message: str

    def __init__(self, success: bool=..., status_code: _Optional[int]=..., message: _Optional[str]=...) -> None:
        ...

class ListApiProvidersRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListApiProvidersResponse(_message.Message):
    __slots__ = ('providers',)
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    providers: _containers.RepeatedCompositeFieldContainer[ApiProvider]

    def __init__(self, providers: _Optional[_Iterable[_Union[ApiProvider, _Mapping]]]=...) -> None:
        ...

class MigrateSecretToApiConnectorRequest(_message.Message):
    __slots__ = ('secret_name', 'api_access_key_id', 'header_name', 'hosts', 'description', 'value_prefix', 'name')
    SECRET_NAME_FIELD_NUMBER: _ClassVar[int]
    API_ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    HEADER_NAME_FIELD_NUMBER: _ClassVar[int]
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VALUE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    secret_name: str
    api_access_key_id: str
    header_name: str
    hosts: _containers.RepeatedScalarFieldContainer[str]
    description: str
    value_prefix: str
    name: str

    def __init__(self, secret_name: _Optional[str]=..., api_access_key_id: _Optional[str]=..., header_name: _Optional[str]=..., hosts: _Optional[_Iterable[str]]=..., description: _Optional[str]=..., value_prefix: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class MigrateSecretToApiConnectorResponse(_message.Message):
    __slots__ = ('api_access_key',)
    API_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    api_access_key: ApiAccessKey

    def __init__(self, api_access_key: _Optional[_Union[ApiAccessKey, _Mapping]]=...) -> None:
        ...