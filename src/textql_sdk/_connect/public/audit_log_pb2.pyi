# pylint: skip-file
# mypy: ignore-errors
# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
import datetime
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ..public import options_pb2 as _options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class S3AuthMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    S3_AUTH_MODE_UNSPECIFIED: _ClassVar[S3AuthMode]
    S3_AUTH_MODE_ACCESS_KEY: _ClassVar[S3AuthMode]
    S3_AUTH_MODE_ASSUME_ROLE: _ClassVar[S3AuthMode]
S3_AUTH_MODE_UNSPECIFIED: S3AuthMode
S3_AUTH_MODE_ACCESS_KEY: S3AuthMode
S3_AUTH_MODE_ASSUME_ROLE: S3AuthMode

class AuditLogEntry(_message.Message):
    __slots__ = ('id', 'org_id', 'actor_id', 'actor_email', 'action', 'category', 'resource_type', 'resource_id', 'details', 'ip_address', 'auth_method', 'created_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_EMAIL_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AUTH_METHOD_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    org_id: str
    actor_id: str
    actor_email: str
    action: str
    category: str
    resource_type: str
    resource_id: str
    details: _struct_pb2.Struct
    ip_address: str
    auth_method: str
    created_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., org_id: _Optional[str]=..., actor_id: _Optional[str]=..., actor_email: _Optional[str]=..., action: _Optional[str]=..., category: _Optional[str]=..., resource_type: _Optional[str]=..., resource_id: _Optional[str]=..., details: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., ip_address: _Optional[str]=..., auth_method: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListAuditLogsRequest(_message.Message):
    __slots__ = ('category', 'actor_id', 'action', 'resource_type', 'cursor', 'page_size', 'search_term', 'after')
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_TERM_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    category: str
    actor_id: str
    action: str
    resource_type: str
    cursor: str
    page_size: int
    search_term: str
    after: _timestamp_pb2.Timestamp

    def __init__(self, category: _Optional[str]=..., actor_id: _Optional[str]=..., action: _Optional[str]=..., resource_type: _Optional[str]=..., cursor: _Optional[str]=..., page_size: _Optional[int]=..., search_term: _Optional[str]=..., after: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListAuditLogsResponse(_message.Message):
    __slots__ = ('entries', 'next_cursor')
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[AuditLogEntry]
    next_cursor: str

    def __init__(self, entries: _Optional[_Iterable[_Union[AuditLogEntry, _Mapping]]]=..., next_cursor: _Optional[str]=...) -> None:
        ...

class S3ExportConfig(_message.Message):
    __slots__ = ('bucket', 'region', 'prefix', 'aws_access_key_id', 'aws_secret_access_key', 'enabled', 'last_exported_at', 'created_at', 'updated_at', 'auth_mode', 'role_arn', 'external_id', 'export_interval_seconds')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    AWS_ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    AWS_SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    LAST_EXPORTED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    AUTH_MODE_FIELD_NUMBER: _ClassVar[int]
    ROLE_ARN_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    EXPORT_INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    region: str
    prefix: str
    aws_access_key_id: str
    aws_secret_access_key: str
    enabled: bool
    last_exported_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    auth_mode: S3AuthMode
    role_arn: str
    external_id: str
    export_interval_seconds: int

    def __init__(self, bucket: _Optional[str]=..., region: _Optional[str]=..., prefix: _Optional[str]=..., aws_access_key_id: _Optional[str]=..., aws_secret_access_key: _Optional[str]=..., enabled: bool=..., last_exported_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., auth_mode: _Optional[_Union[S3AuthMode, str]]=..., role_arn: _Optional[str]=..., external_id: _Optional[str]=..., export_interval_seconds: _Optional[int]=...) -> None:
        ...

class ConfigureS3ExportRequest(_message.Message):
    __slots__ = ('bucket', 'region', 'prefix', 'aws_access_key_id', 'aws_secret_access_key', 'enabled', 'auth_mode', 'role_arn', 'external_id', 'export_interval_seconds')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    AWS_ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    AWS_SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    AUTH_MODE_FIELD_NUMBER: _ClassVar[int]
    ROLE_ARN_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    EXPORT_INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    region: str
    prefix: str
    aws_access_key_id: str
    aws_secret_access_key: str
    enabled: bool
    auth_mode: S3AuthMode
    role_arn: str
    external_id: str
    export_interval_seconds: int

    def __init__(self, bucket: _Optional[str]=..., region: _Optional[str]=..., prefix: _Optional[str]=..., aws_access_key_id: _Optional[str]=..., aws_secret_access_key: _Optional[str]=..., enabled: bool=..., auth_mode: _Optional[_Union[S3AuthMode, str]]=..., role_arn: _Optional[str]=..., external_id: _Optional[str]=..., export_interval_seconds: _Optional[int]=...) -> None:
        ...

class ConfigureS3ExportResponse(_message.Message):
    __slots__ = ('config',)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: S3ExportConfig

    def __init__(self, config: _Optional[_Union[S3ExportConfig, _Mapping]]=...) -> None:
        ...

class GetS3ExportConfigRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetS3ExportConfigResponse(_message.Message):
    __slots__ = ('config',)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: S3ExportConfig

    def __init__(self, config: _Optional[_Union[S3ExportConfig, _Mapping]]=...) -> None:
        ...

class DeleteS3ExportConfigRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DeleteS3ExportConfigResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TestS3ExportConnectionRequest(_message.Message):
    __slots__ = ('bucket', 'region', 'aws_access_key_id', 'aws_secret_access_key', 'auth_mode', 'role_arn', 'external_id')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    AWS_ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    AWS_SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    AUTH_MODE_FIELD_NUMBER: _ClassVar[int]
    ROLE_ARN_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    region: str
    aws_access_key_id: str
    aws_secret_access_key: str
    auth_mode: S3AuthMode
    role_arn: str
    external_id: str

    def __init__(self, bucket: _Optional[str]=..., region: _Optional[str]=..., aws_access_key_id: _Optional[str]=..., aws_secret_access_key: _Optional[str]=..., auth_mode: _Optional[_Union[S3AuthMode, str]]=..., role_arn: _Optional[str]=..., external_id: _Optional[str]=...) -> None:
        ...

class TestS3ExportConnectionResponse(_message.Message):
    __slots__ = ('success', 'error_message')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error_message: str

    def __init__(self, success: bool=..., error_message: _Optional[str]=...) -> None:
        ...

class TriggerS3ExportRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TriggerS3ExportResponse(_message.Message):
    __slots__ = ('triggered',)
    TRIGGERED_FIELD_NUMBER: _ClassVar[int]
    triggered: bool

    def __init__(self, triggered: bool=...) -> None:
        ...

class OtlpExportConfig(_message.Message):
    __slots__ = ('enabled', 'otlp_endpoint', 'otlp_headers', 'otlp_protocol', 'push_interval_seconds', 'last_pushed_at', 'created_at', 'updated_at')
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    OTLP_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    OTLP_HEADERS_FIELD_NUMBER: _ClassVar[int]
    OTLP_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    PUSH_INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    LAST_PUSHED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    otlp_endpoint: str
    otlp_headers: str
    otlp_protocol: str
    push_interval_seconds: int
    last_pushed_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp

    def __init__(self, enabled: bool=..., otlp_endpoint: _Optional[str]=..., otlp_headers: _Optional[str]=..., otlp_protocol: _Optional[str]=..., push_interval_seconds: _Optional[int]=..., last_pushed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ConfigureOtlpExportRequest(_message.Message):
    __slots__ = ('enabled', 'otlp_endpoint', 'otlp_headers', 'otlp_protocol', 'push_interval_seconds')
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    OTLP_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    OTLP_HEADERS_FIELD_NUMBER: _ClassVar[int]
    OTLP_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    PUSH_INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    otlp_endpoint: str
    otlp_headers: str
    otlp_protocol: str
    push_interval_seconds: int

    def __init__(self, enabled: bool=..., otlp_endpoint: _Optional[str]=..., otlp_headers: _Optional[str]=..., otlp_protocol: _Optional[str]=..., push_interval_seconds: _Optional[int]=...) -> None:
        ...

class ConfigureOtlpExportResponse(_message.Message):
    __slots__ = ('config',)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: OtlpExportConfig

    def __init__(self, config: _Optional[_Union[OtlpExportConfig, _Mapping]]=...) -> None:
        ...

class GetOtlpExportConfigRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetOtlpExportConfigResponse(_message.Message):
    __slots__ = ('config',)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: OtlpExportConfig

    def __init__(self, config: _Optional[_Union[OtlpExportConfig, _Mapping]]=...) -> None:
        ...

class DeleteOtlpExportConfigRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DeleteOtlpExportConfigResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TestOtlpExportConnectionRequest(_message.Message):
    __slots__ = ('otlp_endpoint', 'otlp_headers', 'otlp_protocol')
    OTLP_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    OTLP_HEADERS_FIELD_NUMBER: _ClassVar[int]
    OTLP_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    otlp_endpoint: str
    otlp_headers: str
    otlp_protocol: str

    def __init__(self, otlp_endpoint: _Optional[str]=..., otlp_headers: _Optional[str]=..., otlp_protocol: _Optional[str]=...) -> None:
        ...

class TestOtlpExportConnectionResponse(_message.Message):
    __slots__ = ('success', 'error_message')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error_message: str

    def __init__(self, success: bool=..., error_message: _Optional[str]=...) -> None:
        ...

class TriggerOtlpExportRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TriggerOtlpExportResponse(_message.Message):
    __slots__ = ('triggered',)
    TRIGGERED_FIELD_NUMBER: _ClassVar[int]
    triggered: bool

    def __init__(self, triggered: bool=...) -> None:
        ...