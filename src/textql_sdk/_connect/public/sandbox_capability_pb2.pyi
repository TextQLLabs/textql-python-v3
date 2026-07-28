# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
# pylint: skip-file
# mypy: ignore-errors
from ..public import sandbox_query_pb2 as _sandbox_query_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SandboxExecuteWriteRequest(_message.Message):
    __slots__ = ('name', 'connector_id', 'statement', 'parameters', 'max_rows')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    MAX_ROWS_FIELD_NUMBER: _ClassVar[int]
    name: str
    connector_id: int
    statement: str
    parameters: _containers.RepeatedCompositeFieldContainer[_sandbox_query_pb2.SandboxQueryParam]
    max_rows: int

    def __init__(self, name: _Optional[str]=..., connector_id: _Optional[int]=..., statement: _Optional[str]=..., parameters: _Optional[_Iterable[_Union[_sandbox_query_pb2.SandboxQueryParam, _Mapping]]]=..., max_rows: _Optional[int]=...) -> None:
        ...

class SandboxExecuteWriteResponse(_message.Message):
    __slots__ = ('arrow_data', 'total_rows', 'error', 'refreshed_token')
    ARROW_DATA_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ROWS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REFRESHED_TOKEN_FIELD_NUMBER: _ClassVar[int]
    arrow_data: bytes
    total_rows: int
    error: str
    refreshed_token: str

    def __init__(self, arrow_data: _Optional[bytes]=..., total_rows: _Optional[int]=..., error: _Optional[str]=..., refreshed_token: _Optional[str]=...) -> None:
        ...

class SandboxStateOpRequest(_message.Message):
    __slots__ = ('op', 'scope', 'key', 'value')
    OP_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    op: str
    scope: str
    key: str
    value: str

    def __init__(self, op: _Optional[str]=..., scope: _Optional[str]=..., key: _Optional[str]=..., value: _Optional[str]=...) -> None:
        ...

class SandboxStateOpResponse(_message.Message):
    __slots__ = ('value', 'found', 'keys', 'error', 'refreshed_token')
    VALUE_FIELD_NUMBER: _ClassVar[int]
    FOUND_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REFRESHED_TOKEN_FIELD_NUMBER: _ClassVar[int]
    value: str
    found: bool
    keys: _containers.RepeatedScalarFieldContainer[str]
    error: str
    refreshed_token: str

    def __init__(self, value: _Optional[str]=..., found: bool=..., keys: _Optional[_Iterable[str]]=..., error: _Optional[str]=..., refreshed_token: _Optional[str]=...) -> None:
        ...

class SandboxPutAssetRequest(_message.Message):
    __slots__ = ('file_name', 'content_type', 'data')
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    content_type: str
    data: bytes

    def __init__(self, file_name: _Optional[str]=..., content_type: _Optional[str]=..., data: _Optional[bytes]=...) -> None:
        ...

class SandboxPutAssetResponse(_message.Message):
    __slots__ = ('url', 'error', 'refreshed_token')
    URL_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REFRESHED_TOKEN_FIELD_NUMBER: _ClassVar[int]
    url: str
    error: str
    refreshed_token: str

    def __init__(self, url: _Optional[str]=..., error: _Optional[str]=..., refreshed_token: _Optional[str]=...) -> None:
        ...

class SandboxSendNotifyRequest(_message.Message):
    __slots__ = ('name', 'subject', 'body', 'parameters')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    subject: str
    body: str
    parameters: _containers.RepeatedCompositeFieldContainer[_sandbox_query_pb2.SandboxQueryParam]

    def __init__(self, name: _Optional[str]=..., subject: _Optional[str]=..., body: _Optional[str]=..., parameters: _Optional[_Iterable[_Union[_sandbox_query_pb2.SandboxQueryParam, _Mapping]]]=...) -> None:
        ...

class SandboxSendNotifyResponse(_message.Message):
    __slots__ = ('sent', 'error', 'refreshed_token')
    SENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REFRESHED_TOKEN_FIELD_NUMBER: _ClassVar[int]
    sent: bool
    error: str
    refreshed_token: str

    def __init__(self, sent: bool=..., error: _Optional[str]=..., refreshed_token: _Optional[str]=...) -> None:
        ...