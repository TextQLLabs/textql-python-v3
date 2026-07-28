# pylint: skip-file
# mypy: ignore-errors
# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
from ..public import options_pb2 as _options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class GetSnowflakeOAuthURLRequest(_message.Message):
    __slots__ = ('account_url', 'client_id', 'state', 'role')
    ACCOUNT_URL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    account_url: str
    client_id: str
    state: str
    role: str

    def __init__(self, account_url: _Optional[str]=..., client_id: _Optional[str]=..., state: _Optional[str]=..., role: _Optional[str]=...) -> None:
        ...

class GetSnowflakeOAuthURLResponse(_message.Message):
    __slots__ = ('oauth_url',)
    OAUTH_URL_FIELD_NUMBER: _ClassVar[int]
    oauth_url: str

    def __init__(self, oauth_url: _Optional[str]=...) -> None:
        ...

class ExchangeSnowflakeCodeRequest(_message.Message):
    __slots__ = ('code', 'state', 'account_url', 'client_id', 'client_secret')
    CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_URL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    code: str
    state: str
    account_url: str
    client_id: str
    client_secret: str

    def __init__(self, code: _Optional[str]=..., state: _Optional[str]=..., account_url: _Optional[str]=..., client_id: _Optional[str]=..., client_secret: _Optional[str]=...) -> None:
        ...

class ExchangeSnowflakeCodeResponse(_message.Message):
    __slots__ = ('success', 'access_token', 'refresh_token', 'expires_in', 'scope', 'token_type', 'username')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    success: bool
    access_token: str
    refresh_token: str
    expires_in: int
    scope: str
    token_type: str
    username: str

    def __init__(self, success: bool=..., access_token: _Optional[str]=..., refresh_token: _Optional[str]=..., expires_in: _Optional[int]=..., scope: _Optional[str]=..., token_type: _Optional[str]=..., username: _Optional[str]=...) -> None:
        ...