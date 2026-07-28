# pylint: skip-file
# mypy: ignore-errors
import datetime
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ..public import options_pb2 as _options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CheckSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHECK_SEVERITY_UNSPECIFIED: _ClassVar[CheckSeverity]
    CHECK_SEVERITY_ERROR: _ClassVar[CheckSeverity]
    CHECK_SEVERITY_WARN: _ClassVar[CheckSeverity]

class CheckClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHECK_CLASS_UNSPECIFIED: _ClassVar[CheckClass]
    CHECK_CLASS_EDIT_FIXABLE: _ClassVar[CheckClass]
    CHECK_CLASS_ORG_STATE_FIXABLE: _ClassVar[CheckClass]
CHECK_SEVERITY_UNSPECIFIED: CheckSeverity
CHECK_SEVERITY_ERROR: CheckSeverity
CHECK_SEVERITY_WARN: CheckSeverity
CHECK_CLASS_UNSPECIFIED: CheckClass
CHECK_CLASS_EDIT_FIXABLE: CheckClass
CHECK_CLASS_ORG_STATE_FIXABLE: CheckClass

class Check(_message.Message):
    __slots__ = ('id', 'resource_type', 'title', 'severity', 'condition', 'description', 'applies_to')
    ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    APPLIES_TO_FIELD_NUMBER: _ClassVar[int]
    id: str
    resource_type: str
    title: str
    severity: CheckSeverity
    condition: str
    description: str
    applies_to: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, id: _Optional[str]=..., resource_type: _Optional[str]=..., title: _Optional[str]=..., severity: _Optional[_Union[CheckSeverity, str]]=..., condition: _Optional[str]=..., description: _Optional[str]=..., applies_to: _Optional[_Iterable[str]]=...) -> None:
        ...

class ListChecksRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListChecksResponse(_message.Message):
    __slots__ = ('checks',)
    CHECKS_FIELD_NUMBER: _ClassVar[int]
    checks: _containers.RepeatedCompositeFieldContainer[Check]

    def __init__(self, checks: _Optional[_Iterable[_Union[Check, _Mapping]]]=...) -> None:
        ...

class Finding(_message.Message):
    __slots__ = ('check_id', 'resource_type', 'path', 'message')
    CHECK_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    check_id: str
    resource_type: str
    path: str
    message: str

    def __init__(self, check_id: _Optional[str]=..., resource_type: _Optional[str]=..., path: _Optional[str]=..., message: _Optional[str]=..., **kwargs) -> None:
        ...

class RunChecksRequest(_message.Message):
    __slots__ = ('patch_id', 'live')
    PATCH_ID_FIELD_NUMBER: _ClassVar[int]
    LIVE_FIELD_NUMBER: _ClassVar[int]
    patch_id: str
    live: bool

    def __init__(self, patch_id: _Optional[str]=..., live: bool=...) -> None:
        ...

class ErroredCheck(_message.Message):
    __slots__ = ('check_id', 'resource_type', 'path', 'message')
    CHECK_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    check_id: str
    resource_type: str
    path: str
    message: str

    def __init__(self, check_id: _Optional[str]=..., resource_type: _Optional[str]=..., path: _Optional[str]=..., message: _Optional[str]=...) -> None:
        ...

class SaveBlockedByChecksDetail(_message.Message):
    __slots__ = ('findings', 'authz_messages')
    FINDINGS_FIELD_NUMBER: _ClassVar[int]
    AUTHZ_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    findings: _containers.RepeatedCompositeFieldContainer[Finding]
    authz_messages: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, findings: _Optional[_Iterable[_Union[Finding, _Mapping]]]=..., authz_messages: _Optional[_Iterable[str]]=...) -> None:
        ...

class RunChecksResponse(_message.Message):
    __slots__ = ('ok', 'findings', 'errored_checks')
    OK_FIELD_NUMBER: _ClassVar[int]
    FINDINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORED_CHECKS_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    findings: _containers.RepeatedCompositeFieldContainer[Finding]
    errored_checks: _containers.RepeatedCompositeFieldContainer[ErroredCheck]

    def __init__(self, ok: bool=..., findings: _Optional[_Iterable[_Union[Finding, _Mapping]]]=..., errored_checks: _Optional[_Iterable[_Union[ErroredCheck, _Mapping]]]=...) -> None:
        ...

class CheckRecord(_message.Message):
    __slots__ = ('id', 'check_id', 'resource_type', 'path', 'messages', 'severity', 'errored', 'first_seen_at', 'last_seen_at', 'fix_chat_id')
    ID_FIELD_NUMBER: _ClassVar[int]
    CHECK_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    ERRORED_FIELD_NUMBER: _ClassVar[int]
    FIRST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    FIX_CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    check_id: str
    resource_type: str
    path: str
    messages: _containers.RepeatedScalarFieldContainer[str]
    severity: CheckSeverity
    errored: bool
    first_seen_at: _timestamp_pb2.Timestamp
    last_seen_at: _timestamp_pb2.Timestamp
    fix_chat_id: str

    def __init__(self, id: _Optional[str]=..., check_id: _Optional[str]=..., resource_type: _Optional[str]=..., path: _Optional[str]=..., messages: _Optional[_Iterable[str]]=..., severity: _Optional[_Union[CheckSeverity, str]]=..., errored: bool=..., first_seen_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., last_seen_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., fix_chat_id: _Optional[str]=..., **kwargs) -> None:
        ...

class CheckRunInfo(_message.Message):
    __slots__ = ('id', 'source', 'started_at', 'finished_at', 'files_scanned', 'checks_run', 'passing', 'warnings', 'failing', 'errored')
    ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    FILES_SCANNED_FIELD_NUMBER: _ClassVar[int]
    CHECKS_RUN_FIELD_NUMBER: _ClassVar[int]
    PASSING_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    FAILING_FIELD_NUMBER: _ClassVar[int]
    ERRORED_FIELD_NUMBER: _ClassVar[int]
    id: str
    source: str
    started_at: _timestamp_pb2.Timestamp
    finished_at: _timestamp_pb2.Timestamp
    files_scanned: int
    checks_run: int
    passing: int
    warnings: int
    failing: int
    errored: int

    def __init__(self, id: _Optional[str]=..., source: _Optional[str]=..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., files_scanned: _Optional[int]=..., checks_run: _Optional[int]=..., passing: _Optional[int]=..., warnings: _Optional[int]=..., failing: _Optional[int]=..., errored: _Optional[int]=...) -> None:
        ...

class GetCheckResultsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetCheckResultsResponse(_message.Message):
    __slots__ = ('records', 'run')
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    RUN_FIELD_NUMBER: _ClassVar[int]
    records: _containers.RepeatedCompositeFieldContainer[CheckRecord]
    run: CheckRunInfo

    def __init__(self, records: _Optional[_Iterable[_Union[CheckRecord, _Mapping]]]=..., run: _Optional[_Union[CheckRunInfo, _Mapping]]=...) -> None:
        ...