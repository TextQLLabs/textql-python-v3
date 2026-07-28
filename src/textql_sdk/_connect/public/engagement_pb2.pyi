# pylint: skip-file
# mypy: ignore-errors
import datetime
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ..public import options_pb2 as _options_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EngagementType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENGAGEMENT_TYPE_UNSPECIFIED: _ClassVar[EngagementType]
    ENGAGEMENT_TYPE_VIEW: _ClassVar[EngagementType]
    ENGAGEMENT_TYPE_SHARE: _ClassVar[EngagementType]
    ENGAGEMENT_TYPE_IMPRESSION: _ClassVar[EngagementType]

class PrimitiveType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRIMITIVE_TYPE_UNSPECIFIED: _ClassVar[PrimitiveType]
    PRIMITIVE_TYPE_DASHBOARD: _ClassVar[PrimitiveType]
    PRIMITIVE_TYPE_CHAT: _ClassVar[PrimitiveType]
    PRIMITIVE_TYPE_FEED: _ClassVar[PrimitiveType]
    PRIMITIVE_TYPE_PLAYBOOK: _ClassVar[PrimitiveType]
    PRIMITIVE_TYPE_APP: _ClassVar[PrimitiveType]
ENGAGEMENT_TYPE_UNSPECIFIED: EngagementType
ENGAGEMENT_TYPE_VIEW: EngagementType
ENGAGEMENT_TYPE_SHARE: EngagementType
ENGAGEMENT_TYPE_IMPRESSION: EngagementType
PRIMITIVE_TYPE_UNSPECIFIED: PrimitiveType
PRIMITIVE_TYPE_DASHBOARD: PrimitiveType
PRIMITIVE_TYPE_CHAT: PrimitiveType
PRIMITIVE_TYPE_FEED: PrimitiveType
PRIMITIVE_TYPE_PLAYBOOK: PrimitiveType
PRIMITIVE_TYPE_APP: PrimitiveType

class Engagement(_message.Message):
    __slots__ = ('id', 'event_type', 'primitive_id', 'primitive_type', 'user_id', 'org_id', 'share_token', 'occurred_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRIMITIVE_ID_FIELD_NUMBER: _ClassVar[int]
    PRIMITIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    SHARE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    event_type: EngagementType
    primitive_id: str
    primitive_type: PrimitiveType
    user_id: str
    org_id: str
    share_token: str
    occurred_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., event_type: _Optional[_Union[EngagementType, str]]=..., primitive_id: _Optional[str]=..., primitive_type: _Optional[_Union[PrimitiveType, str]]=..., user_id: _Optional[str]=..., org_id: _Optional[str]=..., share_token: _Optional[str]=..., occurred_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class RecordEngagementRequest(_message.Message):
    __slots__ = ('event_type', 'primitive_id', 'primitive_type', 'share_token')
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRIMITIVE_ID_FIELD_NUMBER: _ClassVar[int]
    PRIMITIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHARE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    event_type: EngagementType
    primitive_id: str
    primitive_type: PrimitiveType
    share_token: str

    def __init__(self, event_type: _Optional[_Union[EngagementType, str]]=..., primitive_id: _Optional[str]=..., primitive_type: _Optional[_Union[PrimitiveType, str]]=..., share_token: _Optional[str]=...) -> None:
        ...