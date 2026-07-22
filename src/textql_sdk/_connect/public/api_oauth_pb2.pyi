import datetime
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from public import options_pb2 as _options_pb2
from public import secret_pb2 as _secret_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetApiOAuthURLRequest(_message.Message):
    __slots__ = ('ref', 'state')
    REF_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ref: _secret_pb2.ApiAccessRef
    state: str

    def __init__(self, ref: _Optional[_Union[_secret_pb2.ApiAccessRef, _Mapping]]=..., state: _Optional[str]=...) -> None:
        ...

class GetApiOAuthURLResponse(_message.Message):
    __slots__ = ('oauth_url', 'code_verifier')
    OAUTH_URL_FIELD_NUMBER: _ClassVar[int]
    CODE_VERIFIER_FIELD_NUMBER: _ClassVar[int]
    oauth_url: str
    code_verifier: str

    def __init__(self, oauth_url: _Optional[str]=..., code_verifier: _Optional[str]=...) -> None:
        ...

class ExchangeApiOAuthCodeRequest(_message.Message):
    __slots__ = ('ref', 'code', 'state', 'code_verifier')
    REF_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CODE_VERIFIER_FIELD_NUMBER: _ClassVar[int]
    ref: _secret_pb2.ApiAccessRef
    code: str
    state: str
    code_verifier: str

    def __init__(self, ref: _Optional[_Union[_secret_pb2.ApiAccessRef, _Mapping]]=..., code: _Optional[str]=..., state: _Optional[str]=..., code_verifier: _Optional[str]=...) -> None:
        ...

class ExchangeApiOAuthCodeResponse(_message.Message):
    __slots__ = ('success', 'api_access_key_id', 'display_name')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    API_ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    success: bool
    api_access_key_id: str
    display_name: str

    def __init__(self, success: bool=..., api_access_key_id: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
        ...

class ExchangeApiOAuthClientCredentialsRequest(_message.Message):
    __slots__ = ('ref',)
    REF_FIELD_NUMBER: _ClassVar[int]
    ref: _secret_pb2.ApiAccessRef

    def __init__(self, ref: _Optional[_Union[_secret_pb2.ApiAccessRef, _Mapping]]=...) -> None:
        ...

class ExchangeApiOAuthJwtBearerRequest(_message.Message):
    __slots__ = ('ref',)
    REF_FIELD_NUMBER: _ClassVar[int]
    ref: _secret_pb2.ApiAccessRef

    def __init__(self, ref: _Optional[_Union[_secret_pb2.ApiAccessRef, _Mapping]]=...) -> None:
        ...

class InitiateDeviceAuthorizationRequest(_message.Message):
    __slots__ = ('ref',)
    REF_FIELD_NUMBER: _ClassVar[int]
    ref: _secret_pb2.ApiAccessRef

    def __init__(self, ref: _Optional[_Union[_secret_pb2.ApiAccessRef, _Mapping]]=...) -> None:
        ...

class InitiateDeviceAuthorizationResponse(_message.Message):
    __slots__ = ('device_code', 'user_code', 'verification_uri', 'verification_uri_complete', 'expires_in', 'interval')
    DEVICE_CODE_FIELD_NUMBER: _ClassVar[int]
    USER_CODE_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_URI_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_URI_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    device_code: str
    user_code: str
    verification_uri: str
    verification_uri_complete: str
    expires_in: int
    interval: int

    def __init__(self, device_code: _Optional[str]=..., user_code: _Optional[str]=..., verification_uri: _Optional[str]=..., verification_uri_complete: _Optional[str]=..., expires_in: _Optional[int]=..., interval: _Optional[int]=...) -> None:
        ...

class PollDeviceCodeTokenRequest(_message.Message):
    __slots__ = ('ref', 'device_code')
    REF_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CODE_FIELD_NUMBER: _ClassVar[int]
    ref: _secret_pb2.ApiAccessRef
    device_code: str

    def __init__(self, ref: _Optional[_Union[_secret_pb2.ApiAccessRef, _Mapping]]=..., device_code: _Optional[str]=...) -> None:
        ...

class PollDeviceCodeTokenResponse(_message.Message):
    __slots__ = ('status', 'display_name', 'error_description')
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ERROR_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    status: str
    display_name: str
    error_description: str

    def __init__(self, status: _Optional[str]=..., display_name: _Optional[str]=..., error_description: _Optional[str]=...) -> None:
        ...

class GetApiOAuthStatusRequest(_message.Message):
    __slots__ = ('api_access_key_id',)
    API_ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    api_access_key_id: str

    def __init__(self, api_access_key_id: _Optional[str]=...) -> None:
        ...

class GetApiOAuthStatusResponse(_message.Message):
    __slots__ = ('authenticated', 'token_expired', 'display_name')
    AUTHENTICATED_FIELD_NUMBER: _ClassVar[int]
    TOKEN_EXPIRED_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    authenticated: bool
    token_expired: bool
    display_name: str

    def __init__(self, authenticated: bool=..., token_expired: bool=..., display_name: _Optional[str]=...) -> None:
        ...

class RevokeApiOAuthTokenRequest(_message.Message):
    __slots__ = ('ref',)
    REF_FIELD_NUMBER: _ClassVar[int]
    ref: _secret_pb2.ApiAccessRef

    def __init__(self, ref: _Optional[_Union[_secret_pb2.ApiAccessRef, _Mapping]]=...) -> None:
        ...

class RevokeApiOAuthTokenResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ApiOAuthConfig(_message.Message):
    __slots__ = ('id', 'client_id', 'auth_url', 'token_url', 'scopes', 'use_pkce', 'token_auth_method', 'extra_config', 'created_at', 'updated_at', 'api_access_key_id', 'auth_header', 'auth_prefix', 'grant_type')

    class ExtraConfigEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    AUTH_URL_FIELD_NUMBER: _ClassVar[int]
    TOKEN_URL_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    USE_PKCE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_AUTH_METHOD_FIELD_NUMBER: _ClassVar[int]
    EXTRA_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    API_ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    AUTH_HEADER_FIELD_NUMBER: _ClassVar[int]
    AUTH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    GRANT_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    client_id: str
    auth_url: str
    token_url: str
    scopes: str
    use_pkce: bool
    token_auth_method: str
    extra_config: _containers.ScalarMap[str, str]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    api_access_key_id: str
    auth_header: str
    auth_prefix: str
    grant_type: str

    def __init__(self, id: _Optional[str]=..., client_id: _Optional[str]=..., auth_url: _Optional[str]=..., token_url: _Optional[str]=..., scopes: _Optional[str]=..., use_pkce: bool=..., token_auth_method: _Optional[str]=..., extra_config: _Optional[_Mapping[str, str]]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., api_access_key_id: _Optional[str]=..., auth_header: _Optional[str]=..., auth_prefix: _Optional[str]=..., grant_type: _Optional[str]=...) -> None:
        ...

class UpsertApiOAuthConfigRequest(_message.Message):
    __slots__ = ('client_id', 'client_secret', 'auth_url', 'token_url', 'scopes', 'use_pkce', 'token_auth_method', 'extra_config', 'ref', 'auth_header', 'auth_prefix', 'grant_type')

    class ExtraConfigEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    AUTH_URL_FIELD_NUMBER: _ClassVar[int]
    TOKEN_URL_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    USE_PKCE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_AUTH_METHOD_FIELD_NUMBER: _ClassVar[int]
    EXTRA_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REF_FIELD_NUMBER: _ClassVar[int]
    AUTH_HEADER_FIELD_NUMBER: _ClassVar[int]
    AUTH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    GRANT_TYPE_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    client_secret: str
    auth_url: str
    token_url: str
    scopes: str
    use_pkce: bool
    token_auth_method: str
    extra_config: _containers.ScalarMap[str, str]
    ref: _secret_pb2.ApiAccessRef
    auth_header: str
    auth_prefix: str
    grant_type: str

    def __init__(self, client_id: _Optional[str]=..., client_secret: _Optional[str]=..., auth_url: _Optional[str]=..., token_url: _Optional[str]=..., scopes: _Optional[str]=..., use_pkce: bool=..., token_auth_method: _Optional[str]=..., extra_config: _Optional[_Mapping[str, str]]=..., ref: _Optional[_Union[_secret_pb2.ApiAccessRef, _Mapping]]=..., auth_header: _Optional[str]=..., auth_prefix: _Optional[str]=..., grant_type: _Optional[str]=...) -> None:
        ...

class UpsertApiOAuthConfigResponse(_message.Message):
    __slots__ = ('config',)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: ApiOAuthConfig

    def __init__(self, config: _Optional[_Union[ApiOAuthConfig, _Mapping]]=...) -> None:
        ...

class GetApiOAuthConfigRequest(_message.Message):
    __slots__ = ('api_access_key_id',)
    API_ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    api_access_key_id: str

    def __init__(self, api_access_key_id: _Optional[str]=...) -> None:
        ...

class GetApiOAuthConfigResponse(_message.Message):
    __slots__ = ('config',)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: ApiOAuthConfig

    def __init__(self, config: _Optional[_Union[ApiOAuthConfig, _Mapping]]=...) -> None:
        ...