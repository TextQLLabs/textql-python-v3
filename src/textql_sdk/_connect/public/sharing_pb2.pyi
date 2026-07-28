# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
# pylint: skip-file
# mypy: ignore-errors
import datetime
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ..public import engagement_pb2 as _engagement_pb2
from ..public import options_pb2 as _options_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ShareChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SHARE_CHANNEL_UNSPECIFIED: _ClassVar[ShareChannel]
    SHARE_CHANNEL_SLACK: _ClassVar[ShareChannel]
    SHARE_CHANNEL_EMAIL: _ClassVar[ShareChannel]
    SHARE_CHANNEL_LINK_COPY: _ClassVar[ShareChannel]
SHARE_CHANNEL_UNSPECIFIED: ShareChannel
SHARE_CHANNEL_SLACK: ShareChannel
SHARE_CHANNEL_EMAIL: ShareChannel
SHARE_CHANNEL_LINK_COPY: ShareChannel

class GetSharePreviewRequest(_message.Message):
    __slots__ = ('token',)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str

    def __init__(self, token: _Optional[str]=...) -> None:
        ...

class GetSharePreviewResponse(_message.Message):
    __slots__ = ('primitive_type', 'sharer_display_name', 'org_brand_name')
    PRIMITIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHARER_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ORG_BRAND_NAME_FIELD_NUMBER: _ClassVar[int]
    primitive_type: str
    sharer_display_name: str
    org_brand_name: str

    def __init__(self, primitive_type: _Optional[str]=..., sharer_display_name: _Optional[str]=..., org_brand_name: _Optional[str]=...) -> None:
        ...

class Share(_message.Message):
    __slots__ = ('id', 'share_token', 'primitive_id', 'primitive_type', 'sharer_id', 'org_id', 'channel', 'created_at', 'expires_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    SHARE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PRIMITIVE_ID_FIELD_NUMBER: _ClassVar[int]
    PRIMITIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHARER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    share_token: str
    primitive_id: str
    primitive_type: _engagement_pb2.PrimitiveType
    sharer_id: str
    org_id: str
    channel: ShareChannel
    created_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., share_token: _Optional[str]=..., primitive_id: _Optional[str]=..., primitive_type: _Optional[_Union[_engagement_pb2.PrimitiveType, str]]=..., sharer_id: _Optional[str]=..., org_id: _Optional[str]=..., channel: _Optional[_Union[ShareChannel, str]]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CreateShareRequest(_message.Message):
    __slots__ = ('primitive_id', 'primitive_type', 'channel', 'expires_at')
    PRIMITIVE_ID_FIELD_NUMBER: _ClassVar[int]
    PRIMITIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    primitive_id: str
    primitive_type: _engagement_pb2.PrimitiveType
    channel: ShareChannel
    expires_at: _timestamp_pb2.Timestamp

    def __init__(self, primitive_id: _Optional[str]=..., primitive_type: _Optional[_Union[_engagement_pb2.PrimitiveType, str]]=..., channel: _Optional[_Union[ShareChannel, str]]=..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CreateShareResponse(_message.Message):
    __slots__ = ('share', 'url')
    SHARE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    share: Share
    url: str

    def __init__(self, share: _Optional[_Union[Share, _Mapping]]=..., url: _Optional[str]=...) -> None:
        ...

class GetShareRequest(_message.Message):
    __slots__ = ('share_token',)
    SHARE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    share_token: str

    def __init__(self, share_token: _Optional[str]=...) -> None:
        ...

class GetShareResponse(_message.Message):
    __slots__ = ('share',)
    SHARE_FIELD_NUMBER: _ClassVar[int]
    share: Share

    def __init__(self, share: _Optional[_Union[Share, _Mapping]]=...) -> None:
        ...

class ResolveShareForCallerRequest(_message.Message):
    __slots__ = ('share_token',)
    SHARE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    share_token: str

    def __init__(self, share_token: _Optional[str]=...) -> None:
        ...

class ResolveShareForCallerResponse(_message.Message):
    __slots__ = ('caller_is_member', 'same_org', 'primitive_id', 'primitive_type', 'org_id')
    CALLER_IS_MEMBER_FIELD_NUMBER: _ClassVar[int]
    SAME_ORG_FIELD_NUMBER: _ClassVar[int]
    PRIMITIVE_ID_FIELD_NUMBER: _ClassVar[int]
    PRIMITIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    caller_is_member: bool
    same_org: bool
    primitive_id: str
    primitive_type: _engagement_pb2.PrimitiveType
    org_id: str

    def __init__(self, caller_is_member: bool=..., same_org: bool=..., primitive_id: _Optional[str]=..., primitive_type: _Optional[_Union[_engagement_pb2.PrimitiveType, str]]=..., org_id: _Optional[str]=...) -> None:
        ...