# pylint: skip-file
# mypy: ignore-errors
# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
import datetime
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ..public import options_pb2 as _options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MetricsExportConfig(_message.Message):
    __slots__ = ('prometheus_enabled', 'otlp_enabled', 'otlp_endpoint', 'otlp_headers', 'otlp_protocol', 'push_interval_seconds', 'last_pushed_at', 'created_at', 'updated_at')
    PROMETHEUS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    OTLP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    OTLP_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    OTLP_HEADERS_FIELD_NUMBER: _ClassVar[int]
    OTLP_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    PUSH_INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    LAST_PUSHED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    prometheus_enabled: bool
    otlp_enabled: bool
    otlp_endpoint: str
    otlp_headers: str
    otlp_protocol: str
    push_interval_seconds: int
    last_pushed_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp

    def __init__(self, prometheus_enabled: bool=..., otlp_enabled: bool=..., otlp_endpoint: _Optional[str]=..., otlp_headers: _Optional[str]=..., otlp_protocol: _Optional[str]=..., push_interval_seconds: _Optional[int]=..., last_pushed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ConfigureMetricsExportRequest(_message.Message):
    __slots__ = ('prometheus_enabled', 'otlp_enabled', 'otlp_endpoint', 'otlp_headers', 'otlp_protocol', 'push_interval_seconds')
    PROMETHEUS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    OTLP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    OTLP_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    OTLP_HEADERS_FIELD_NUMBER: _ClassVar[int]
    OTLP_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    PUSH_INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    prometheus_enabled: bool
    otlp_enabled: bool
    otlp_endpoint: str
    otlp_headers: str
    otlp_protocol: str
    push_interval_seconds: int

    def __init__(self, prometheus_enabled: bool=..., otlp_enabled: bool=..., otlp_endpoint: _Optional[str]=..., otlp_headers: _Optional[str]=..., otlp_protocol: _Optional[str]=..., push_interval_seconds: _Optional[int]=...) -> None:
        ...

class ConfigureMetricsExportResponse(_message.Message):
    __slots__ = ('config',)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: MetricsExportConfig

    def __init__(self, config: _Optional[_Union[MetricsExportConfig, _Mapping]]=...) -> None:
        ...

class GetMetricsExportConfigRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetMetricsExportConfigResponse(_message.Message):
    __slots__ = ('config',)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: MetricsExportConfig

    def __init__(self, config: _Optional[_Union[MetricsExportConfig, _Mapping]]=...) -> None:
        ...

class DeleteMetricsExportConfigRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DeleteMetricsExportConfigResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TestMetricsExportConnectionRequest(_message.Message):
    __slots__ = ('otlp_endpoint', 'otlp_headers', 'otlp_protocol')
    OTLP_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    OTLP_HEADERS_FIELD_NUMBER: _ClassVar[int]
    OTLP_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    otlp_endpoint: str
    otlp_headers: str
    otlp_protocol: str

    def __init__(self, otlp_endpoint: _Optional[str]=..., otlp_headers: _Optional[str]=..., otlp_protocol: _Optional[str]=...) -> None:
        ...

class TestMetricsExportConnectionResponse(_message.Message):
    __slots__ = ('success', 'error_message')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error_message: str

    def __init__(self, success: bool=..., error_message: _Optional[str]=...) -> None:
        ...

class TriggerMetricsPushRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TriggerMetricsPushResponse(_message.Message):
    __slots__ = ('triggered',)
    TRIGGERED_FIELD_NUMBER: _ClassVar[int]
    triggered: bool

    def __init__(self, triggered: bool=...) -> None:
        ...