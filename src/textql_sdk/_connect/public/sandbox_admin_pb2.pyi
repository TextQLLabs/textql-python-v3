# pylint: skip-file
# mypy: ignore-errors
# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
import datetime
from ..google.api import visibility_pb2 as _visibility_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetSandboxLeaseSettingsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetSandboxLeaseSettingsResponse(_message.Message):
    __slots__ = ('thread_duration_minutes', 'dashboard_duration_minutes')
    THREAD_DURATION_MINUTES_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_DURATION_MINUTES_FIELD_NUMBER: _ClassVar[int]
    thread_duration_minutes: int
    dashboard_duration_minutes: int

    def __init__(self, thread_duration_minutes: _Optional[int]=..., dashboard_duration_minutes: _Optional[int]=...) -> None:
        ...

class SetSandboxLeaseSettingsRequest(_message.Message):
    __slots__ = ('thread_duration_minutes', 'dashboard_duration_minutes')
    THREAD_DURATION_MINUTES_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_DURATION_MINUTES_FIELD_NUMBER: _ClassVar[int]
    thread_duration_minutes: int
    dashboard_duration_minutes: int

    def __init__(self, thread_duration_minutes: _Optional[int]=..., dashboard_duration_minutes: _Optional[int]=...) -> None:
        ...

class SetSandboxLeaseSettingsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class SandboxSummary(_message.Message):
    __slots__ = ('sandbox_id', 'status', 'member_id', 'chat_id', 'started_at', 'released_at')
    SANDBOX_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    RELEASED_AT_FIELD_NUMBER: _ClassVar[int]
    sandbox_id: str
    status: str
    member_id: str
    chat_id: str
    started_at: _timestamp_pb2.Timestamp
    released_at: _timestamp_pb2.Timestamp

    def __init__(self, sandbox_id: _Optional[str]=..., status: _Optional[str]=..., member_id: _Optional[str]=..., chat_id: _Optional[str]=..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., released_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListSandboxesRequest(_message.Message):
    __slots__ = ('status', 'limit', 'cursor')
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    status: str
    limit: int
    cursor: str

    def __init__(self, status: _Optional[str]=..., limit: _Optional[int]=..., cursor: _Optional[str]=...) -> None:
        ...

class ListSandboxesResponse(_message.Message):
    __slots__ = ('sandboxes', 'next_cursor')
    SANDBOXES_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    sandboxes: _containers.RepeatedCompositeFieldContainer[SandboxSummary]
    next_cursor: str

    def __init__(self, sandboxes: _Optional[_Iterable[_Union[SandboxSummary, _Mapping]]]=..., next_cursor: _Optional[str]=...) -> None:
        ...

class StopSandboxRequest(_message.Message):
    __slots__ = ('sandbox_id',)
    SANDBOX_ID_FIELD_NUMBER: _ClassVar[int]
    sandbox_id: str

    def __init__(self, sandbox_id: _Optional[str]=...) -> None:
        ...

class StopSandboxResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class RestartSandboxRequest(_message.Message):
    __slots__ = ('sandbox_id',)
    SANDBOX_ID_FIELD_NUMBER: _ClassVar[int]
    sandbox_id: str

    def __init__(self, sandbox_id: _Optional[str]=...) -> None:
        ...

class RestartSandboxResponse(_message.Message):
    __slots__ = ('sandbox_id', 'started_at')
    SANDBOX_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    sandbox_id: str
    started_at: _timestamp_pb2.Timestamp

    def __init__(self, sandbox_id: _Optional[str]=..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GetSandboxRequest(_message.Message):
    __slots__ = ('sandbox_id',)
    SANDBOX_ID_FIELD_NUMBER: _ClassVar[int]
    sandbox_id: str

    def __init__(self, sandbox_id: _Optional[str]=...) -> None:
        ...

class GetSandboxResponse(_message.Message):
    __slots__ = ('sandbox', 'live_available', 'memory_usage_bytes', 'dataframes')
    SANDBOX_FIELD_NUMBER: _ClassVar[int]
    LIVE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DATAFRAMES_FIELD_NUMBER: _ClassVar[int]
    sandbox: SandboxSummary
    live_available: bool
    memory_usage_bytes: int
    dataframes: _containers.RepeatedCompositeFieldContainer[SandboxDataframe]

    def __init__(self, sandbox: _Optional[_Union[SandboxSummary, _Mapping]]=..., live_available: bool=..., memory_usage_bytes: _Optional[int]=..., dataframes: _Optional[_Iterable[_Union[SandboxDataframe, _Mapping]]]=...) -> None:
        ...

class SandboxDataframe(_message.Message):
    __slots__ = ('name', 'num_rows', 'num_cols', 'memory_usage_bytes')
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_ROWS_FIELD_NUMBER: _ClassVar[int]
    NUM_COLS_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    name: str
    num_rows: int
    num_cols: int
    memory_usage_bytes: int

    def __init__(self, name: _Optional[str]=..., num_rows: _Optional[int]=..., num_cols: _Optional[int]=..., memory_usage_bytes: _Optional[int]=...) -> None:
        ...

class SandboxExecution(_message.Message):
    __slots__ = ('id', 'kind', 'source', 'input', 'output_preview', 'error', 'duration_ms', 'created_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    kind: str
    source: str
    input: str
    output_preview: str
    error: str
    duration_ms: int
    created_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., kind: _Optional[str]=..., source: _Optional[str]=..., input: _Optional[str]=..., output_preview: _Optional[str]=..., error: _Optional[str]=..., duration_ms: _Optional[int]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListSandboxExecutionsRequest(_message.Message):
    __slots__ = ('sandbox_id', 'limit', 'cursor')
    SANDBOX_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    sandbox_id: str
    limit: int
    cursor: str

    def __init__(self, sandbox_id: _Optional[str]=..., limit: _Optional[int]=..., cursor: _Optional[str]=...) -> None:
        ...

class ListSandboxExecutionsResponse(_message.Message):
    __slots__ = ('executions', 'next_cursor')
    EXECUTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    executions: _containers.RepeatedCompositeFieldContainer[SandboxExecution]
    next_cursor: str

    def __init__(self, executions: _Optional[_Iterable[_Union[SandboxExecution, _Mapping]]]=..., next_cursor: _Optional[str]=...) -> None:
        ...

class SandboxFileEntry(_message.Message):
    __slots__ = ('name', 'path', 'is_dir', 'size_bytes', 'modified_at')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    IS_DIR_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    name: str
    path: str
    is_dir: bool
    size_bytes: int
    modified_at: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., path: _Optional[str]=..., is_dir: bool=..., size_bytes: _Optional[int]=..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListSandboxFilesRequest(_message.Message):
    __slots__ = ('sandbox_id', 'path')
    SANDBOX_ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    sandbox_id: str
    path: str

    def __init__(self, sandbox_id: _Optional[str]=..., path: _Optional[str]=...) -> None:
        ...

class ListSandboxFilesResponse(_message.Message):
    __slots__ = ('available', 'entries')
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    available: bool
    entries: _containers.RepeatedCompositeFieldContainer[SandboxFileEntry]

    def __init__(self, available: bool=..., entries: _Optional[_Iterable[_Union[SandboxFileEntry, _Mapping]]]=...) -> None:
        ...

class ReadSandboxFileRequest(_message.Message):
    __slots__ = ('sandbox_id', 'path')
    SANDBOX_ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    sandbox_id: str
    path: str

    def __init__(self, sandbox_id: _Optional[str]=..., path: _Optional[str]=...) -> None:
        ...

class SandboxEgressCall(_message.Message):
    __slots__ = ('id', 'method', 'scheme', 'host', 'path', 'status_code', 'outcome', 'duration_ms', 'request_bytes', 'response_bytes', 'cell_id', 'occurred_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    SCHEME_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_BYTES_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_BYTES_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    method: str
    scheme: str
    host: str
    path: str
    status_code: int
    outcome: str
    duration_ms: int
    request_bytes: int
    response_bytes: int
    cell_id: str
    occurred_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., method: _Optional[str]=..., scheme: _Optional[str]=..., host: _Optional[str]=..., path: _Optional[str]=..., status_code: _Optional[int]=..., outcome: _Optional[str]=..., duration_ms: _Optional[int]=..., request_bytes: _Optional[int]=..., response_bytes: _Optional[int]=..., cell_id: _Optional[str]=..., occurred_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListSandboxEgressRequest(_message.Message):
    __slots__ = ('sandbox_id', 'limit')
    SANDBOX_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    sandbox_id: str
    limit: int

    def __init__(self, sandbox_id: _Optional[str]=..., limit: _Optional[int]=...) -> None:
        ...

class ListSandboxEgressResponse(_message.Message):
    __slots__ = ('calls',)
    CALLS_FIELD_NUMBER: _ClassVar[int]
    calls: _containers.RepeatedCompositeFieldContainer[SandboxEgressCall]

    def __init__(self, calls: _Optional[_Iterable[_Union[SandboxEgressCall, _Mapping]]]=...) -> None:
        ...

class SandboxSpendInterval(_message.Message):
    __slots__ = ('started_at', 'ended_at', 'duration_ms', 'acus', 'active')
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    ACUS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    started_at: _timestamp_pb2.Timestamp
    ended_at: _timestamp_pb2.Timestamp
    duration_ms: int
    acus: float
    active: bool

    def __init__(self, started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., ended_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., duration_ms: _Optional[int]=..., acus: _Optional[float]=..., active: bool=...) -> None:
        ...

class ListSandboxSpendRequest(_message.Message):
    __slots__ = ('sandbox_id',)
    SANDBOX_ID_FIELD_NUMBER: _ClassVar[int]
    sandbox_id: str

    def __init__(self, sandbox_id: _Optional[str]=...) -> None:
        ...

class ListSandboxSpendResponse(_message.Message):
    __slots__ = ('intervals', 'acus_per_hour', 'total_acus', 'acu_rate_per_1000_usd')
    INTERVALS_FIELD_NUMBER: _ClassVar[int]
    ACUS_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ACUS_FIELD_NUMBER: _ClassVar[int]
    ACU_RATE_PER_1000_USD_FIELD_NUMBER: _ClassVar[int]
    intervals: _containers.RepeatedCompositeFieldContainer[SandboxSpendInterval]
    acus_per_hour: float
    total_acus: float
    acu_rate_per_1000_usd: float

    def __init__(self, intervals: _Optional[_Iterable[_Union[SandboxSpendInterval, _Mapping]]]=..., acus_per_hour: _Optional[float]=..., total_acus: _Optional[float]=..., acu_rate_per_1000_usd: _Optional[float]=...) -> None:
        ...

class SandboxResourceSample(_message.Message):
    __slots__ = ('sampled_at', 'cpu_usage_cores', 'cpu_limit_cores', 'cpu_usage_percent', 'memory_usage_bytes', 'memory_limit_bytes', 'memory_usage_percent')
    SAMPLED_AT_FIELD_NUMBER: _ClassVar[int]
    CPU_USAGE_CORES_FIELD_NUMBER: _ClassVar[int]
    CPU_LIMIT_CORES_FIELD_NUMBER: _ClassVar[int]
    CPU_USAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MEMORY_LIMIT_BYTES_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    sampled_at: _timestamp_pb2.Timestamp
    cpu_usage_cores: float
    cpu_limit_cores: float
    cpu_usage_percent: float
    memory_usage_bytes: int
    memory_limit_bytes: int
    memory_usage_percent: float

    def __init__(self, sampled_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., cpu_usage_cores: _Optional[float]=..., cpu_limit_cores: _Optional[float]=..., cpu_usage_percent: _Optional[float]=..., memory_usage_bytes: _Optional[int]=..., memory_limit_bytes: _Optional[int]=..., memory_usage_percent: _Optional[float]=...) -> None:
        ...

class ListSandboxResourcesRequest(_message.Message):
    __slots__ = ('sandbox_id', 'start_at', 'end_at')
    SANDBOX_ID_FIELD_NUMBER: _ClassVar[int]
    START_AT_FIELD_NUMBER: _ClassVar[int]
    END_AT_FIELD_NUMBER: _ClassVar[int]
    sandbox_id: str
    start_at: _timestamp_pb2.Timestamp
    end_at: _timestamp_pb2.Timestamp

    def __init__(self, sandbox_id: _Optional[str]=..., start_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., end_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListSandboxResourcesResponse(_message.Message):
    __slots__ = ('samples',)
    SAMPLES_FIELD_NUMBER: _ClassVar[int]
    samples: _containers.RepeatedCompositeFieldContainer[SandboxResourceSample]

    def __init__(self, samples: _Optional[_Iterable[_Union[SandboxResourceSample, _Mapping]]]=...) -> None:
        ...

class StoredSandboxResourceSample(_message.Message):
    __slots__ = ('ts_ms', 'cpu_millicores', 'cpu_limit_millicores', 'memory_bytes', 'memory_limit_bytes')
    TS_MS_FIELD_NUMBER: _ClassVar[int]
    CPU_MILLICORES_FIELD_NUMBER: _ClassVar[int]
    CPU_LIMIT_MILLICORES_FIELD_NUMBER: _ClassVar[int]
    MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
    MEMORY_LIMIT_BYTES_FIELD_NUMBER: _ClassVar[int]
    ts_ms: int
    cpu_millicores: int
    cpu_limit_millicores: int
    memory_bytes: int
    memory_limit_bytes: int

    def __init__(self, ts_ms: _Optional[int]=..., cpu_millicores: _Optional[int]=..., cpu_limit_millicores: _Optional[int]=..., memory_bytes: _Optional[int]=..., memory_limit_bytes: _Optional[int]=...) -> None:
        ...

class ReadSandboxFileResponse(_message.Message):
    __slots__ = ('available', 'name', 'size_bytes', 'mime_type', 'content', 'binary_content', 'truncated', 'is_binary')
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    BINARY_CONTENT_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    IS_BINARY_FIELD_NUMBER: _ClassVar[int]
    available: bool
    name: str
    size_bytes: int
    mime_type: str
    content: str
    binary_content: bytes
    truncated: bool
    is_binary: bool

    def __init__(self, available: bool=..., name: _Optional[str]=..., size_bytes: _Optional[int]=..., mime_type: _Optional[str]=..., content: _Optional[str]=..., binary_content: _Optional[bytes]=..., truncated: bool=..., is_binary: bool=...) -> None:
        ...