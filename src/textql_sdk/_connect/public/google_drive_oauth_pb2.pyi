from google.protobuf import struct_pb2 as _struct_pb2
from public import options_pb2 as _options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeGoogleDriveCodeRequest(_message.Message):
    __slots__ = ('code', 'state')
    CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    code: str
    state: str

    def __init__(self, code: _Optional[str]=..., state: _Optional[str]=...) -> None:
        ...

class ExchangeGoogleDriveCodeResponse(_message.Message):
    __slots__ = ('success', 'access_token', 'refresh_token', 'expires_in', 'scope', 'token_type', 'user_info')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    success: bool
    access_token: str
    refresh_token: str
    expires_in: int
    scope: str
    token_type: str
    user_info: _struct_pb2.Struct

    def __init__(self, success: bool=..., access_token: _Optional[str]=..., refresh_token: _Optional[str]=..., expires_in: _Optional[int]=..., scope: _Optional[str]=..., token_type: _Optional[str]=..., user_info: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...