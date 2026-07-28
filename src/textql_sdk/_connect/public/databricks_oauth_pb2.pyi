# pylint: skip-file
# mypy: ignore-errors
from ..public import options_pb2 as _options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class GetDatabricksOAuthURLRequest(_message.Message):
    __slots__ = ('workspace_url', 'client_id', 'state')
    WORKSPACE_URL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    workspace_url: str
    client_id: str
    state: str

    def __init__(self, workspace_url: _Optional[str]=..., client_id: _Optional[str]=..., state: _Optional[str]=...) -> None:
        ...

class GetDatabricksOAuthURLResponse(_message.Message):
    __slots__ = ('oauth_url', 'code_verifier')
    OAUTH_URL_FIELD_NUMBER: _ClassVar[int]
    CODE_VERIFIER_FIELD_NUMBER: _ClassVar[int]
    oauth_url: str
    code_verifier: str

    def __init__(self, oauth_url: _Optional[str]=..., code_verifier: _Optional[str]=...) -> None:
        ...

class ExchangeDatabricksCodeRequest(_message.Message):
    __slots__ = ('code', 'state', 'workspace_url', 'client_id', 'client_secret', 'code_verifier')
    CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_URL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    CODE_VERIFIER_FIELD_NUMBER: _ClassVar[int]
    code: str
    state: str
    workspace_url: str
    client_id: str
    client_secret: str
    code_verifier: str

    def __init__(self, code: _Optional[str]=..., state: _Optional[str]=..., workspace_url: _Optional[str]=..., client_id: _Optional[str]=..., client_secret: _Optional[str]=..., code_verifier: _Optional[str]=...) -> None:
        ...

class ExchangeDatabricksCodeResponse(_message.Message):
    __slots__ = ('success', 'access_token', 'refresh_token', 'expires_in', 'scope', 'token_type')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    access_token: str
    refresh_token: str
    expires_in: int
    scope: str
    token_type: str

    def __init__(self, success: bool=..., access_token: _Optional[str]=..., refresh_token: _Optional[str]=..., expires_in: _Optional[int]=..., scope: _Optional[str]=..., token_type: _Optional[str]=...) -> None:
        ...