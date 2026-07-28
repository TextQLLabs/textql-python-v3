# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
# pylint: skip-file
# mypy: ignore-errors
from .. import auth_pb2 as _auth_pb2
from ..public import options_pb2 as _options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class StartPhoneVerificationRequest(_message.Message):
    __slots__ = ('phone_number',)
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    phone_number: str

    def __init__(self, phone_number: _Optional[str]=...) -> None:
        ...

class StartPhoneVerificationResponse(_message.Message):
    __slots__ = ('code_sent',)
    CODE_SENT_FIELD_NUMBER: _ClassVar[int]
    code_sent: bool

    def __init__(self, code_sent: bool=...) -> None:
        ...

class ConfirmPhoneVerificationRequest(_message.Message):
    __slots__ = ('code',)
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str

    def __init__(self, code: _Optional[str]=...) -> None:
        ...

class ConfirmPhoneVerificationResponse(_message.Message):
    __slots__ = ('member', 'agent_id')
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    member: _auth_pb2.Member
    agent_id: str

    def __init__(self, member: _Optional[_Union[_auth_pb2.Member, _Mapping]]=..., agent_id: _Optional[str]=...) -> None:
        ...

class SetSmsAgentRequest(_message.Message):
    __slots__ = ('agent_id',)
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str

    def __init__(self, agent_id: _Optional[str]=...) -> None:
        ...

class SetSmsAgentResponse(_message.Message):
    __slots__ = ('member',)
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: _auth_pb2.Member

    def __init__(self, member: _Optional[_Union[_auth_pb2.Member, _Mapping]]=...) -> None:
        ...

class RemovePhoneRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class RemovePhoneResponse(_message.Message):
    __slots__ = ('member',)
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: _auth_pb2.Member

    def __init__(self, member: _Optional[_Union[_auth_pb2.Member, _Mapping]]=...) -> None:
        ...