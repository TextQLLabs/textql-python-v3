# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
# pylint: skip-file
# mypy: ignore-errors
from ..public import options_pb2 as _options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AuthenticateMemberForConnectorRequest(_message.Message):
    __slots__ = ('connector_id', 'access_token', 'refresh_token', 'expires_in', 'username', 'scope')
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    connector_id: int
    access_token: str
    refresh_token: str
    expires_in: int
    username: str
    scope: str

    def __init__(self, connector_id: _Optional[int]=..., access_token: _Optional[str]=..., refresh_token: _Optional[str]=..., expires_in: _Optional[int]=..., username: _Optional[str]=..., scope: _Optional[str]=...) -> None:
        ...

class AuthenticateMemberForConnectorResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class ExchangeAndStoreMemberAuthRequest(_message.Message):
    __slots__ = ('connector_id', 'code', 'state', 'account_url', 'code_verifier')
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_URL_FIELD_NUMBER: _ClassVar[int]
    CODE_VERIFIER_FIELD_NUMBER: _ClassVar[int]
    connector_id: int
    code: str
    state: str
    account_url: str
    code_verifier: str

    def __init__(self, connector_id: _Optional[int]=..., code: _Optional[str]=..., state: _Optional[str]=..., account_url: _Optional[str]=..., code_verifier: _Optional[str]=...) -> None:
        ...

class ExchangeAndStoreMemberAuthResponse(_message.Message):
    __slots__ = ('success', 'username')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    success: bool
    username: str

    def __init__(self, success: bool=..., username: _Optional[str]=...) -> None:
        ...

class GetMemberConnectorAuthStatusRequest(_message.Message):
    __slots__ = ('connector_ids',)
    CONNECTOR_IDS_FIELD_NUMBER: _ClassVar[int]
    connector_ids: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, connector_ids: _Optional[_Iterable[int]]=...) -> None:
        ...

class ConnectorAuthStatus(_message.Message):
    __slots__ = ('connector_id', 'authenticated', 'username', 'token_expired')
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATED_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    TOKEN_EXPIRED_FIELD_NUMBER: _ClassVar[int]
    connector_id: int
    authenticated: bool
    username: str
    token_expired: bool

    def __init__(self, connector_id: _Optional[int]=..., authenticated: bool=..., username: _Optional[str]=..., token_expired: bool=...) -> None:
        ...

class GetMemberConnectorAuthStatusResponse(_message.Message):
    __slots__ = ('statuses',)
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    statuses: _containers.RepeatedCompositeFieldContainer[ConnectorAuthStatus]

    def __init__(self, statuses: _Optional[_Iterable[_Union[ConnectorAuthStatus, _Mapping]]]=...) -> None:
        ...