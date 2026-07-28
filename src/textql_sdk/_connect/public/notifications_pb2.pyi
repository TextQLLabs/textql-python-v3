# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
# pylint: skip-file
# mypy: ignore-errors
import datetime
from google.protobuf import empty_pb2 as _empty_pb2
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

class NotificationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTIFICATION_TYPE_UNSPECIFIED: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_FEED_TAG: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_FEED_POST: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_FEED_COMMENT: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_LIBRARY_SYNC_FAILED: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_LIBRARY_PATCH_OPEN: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_LIBRARY_PATCH_APPROVED: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_LIBRARY_PATCH_DENIED: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_CONFIG_SYNC_FAILED: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_CODEOWNER_ASSIGNED: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_CODEOWNER_REMOVED: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_LIBRARY_PATCH_REVERTED: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_SHARE_GRANT: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_REQUEST_ACCESS: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_REQUEST_ACCESS_APPROVED: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_REQUEST_ACCESS_DENIED: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_SYSTEM_ALERT: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_PLAYBOOK_RECAP: _ClassVar[NotificationType]

class NotificationChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTIFICATION_CHANNEL_UNSPECIFIED: _ClassVar[NotificationChannel]
    NOTIFICATION_CHANNEL_APP: _ClassVar[NotificationChannel]
    NOTIFICATION_CHANNEL_SLACK: _ClassVar[NotificationChannel]
    NOTIFICATION_CHANNEL_EMAIL: _ClassVar[NotificationChannel]
    NOTIFICATION_CHANNEL_TEAMS: _ClassVar[NotificationChannel]

class BroadcastStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BROADCAST_STATUS_UNSPECIFIED: _ClassVar[BroadcastStatus]
    BROADCAST_STATUS_SCHEDULED: _ClassVar[BroadcastStatus]
    BROADCAST_STATUS_SENT: _ClassVar[BroadcastStatus]
    BROADCAST_STATUS_CANCELLED: _ClassVar[BroadcastStatus]
NOTIFICATION_TYPE_UNSPECIFIED: NotificationType
NOTIFICATION_TYPE_FEED_TAG: NotificationType
NOTIFICATION_TYPE_FEED_POST: NotificationType
NOTIFICATION_TYPE_FEED_COMMENT: NotificationType
NOTIFICATION_TYPE_LIBRARY_SYNC_FAILED: NotificationType
NOTIFICATION_TYPE_LIBRARY_PATCH_OPEN: NotificationType
NOTIFICATION_TYPE_LIBRARY_PATCH_APPROVED: NotificationType
NOTIFICATION_TYPE_LIBRARY_PATCH_DENIED: NotificationType
NOTIFICATION_TYPE_CONFIG_SYNC_FAILED: NotificationType
NOTIFICATION_TYPE_CODEOWNER_ASSIGNED: NotificationType
NOTIFICATION_TYPE_CODEOWNER_REMOVED: NotificationType
NOTIFICATION_TYPE_LIBRARY_PATCH_REVERTED: NotificationType
NOTIFICATION_TYPE_SHARE_GRANT: NotificationType
NOTIFICATION_TYPE_REQUEST_ACCESS: NotificationType
NOTIFICATION_TYPE_REQUEST_ACCESS_APPROVED: NotificationType
NOTIFICATION_TYPE_REQUEST_ACCESS_DENIED: NotificationType
NOTIFICATION_TYPE_SYSTEM_ALERT: NotificationType
NOTIFICATION_TYPE_PLAYBOOK_RECAP: NotificationType
NOTIFICATION_CHANNEL_UNSPECIFIED: NotificationChannel
NOTIFICATION_CHANNEL_APP: NotificationChannel
NOTIFICATION_CHANNEL_SLACK: NotificationChannel
NOTIFICATION_CHANNEL_EMAIL: NotificationChannel
NOTIFICATION_CHANNEL_TEAMS: NotificationChannel
BROADCAST_STATUS_UNSPECIFIED: BroadcastStatus
BROADCAST_STATUS_SCHEDULED: BroadcastStatus
BROADCAST_STATUS_SENT: BroadcastStatus
BROADCAST_STATUS_CANCELLED: BroadcastStatus

class Notification(_message.Message):
    __slots__ = ('id', 'notification_type', 'context', 'created_at', 'read_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    READ_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    notification_type: NotificationType
    context: _struct_pb2.Struct
    created_at: _timestamp_pb2.Timestamp
    read_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., notification_type: _Optional[_Union[NotificationType, str]]=..., context: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., read_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class NotificationEvent(_message.Message):
    __slots__ = ('notification', 'unread_count')
    NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    UNREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    notification: Notification
    unread_count: int

    def __init__(self, notification: _Optional[_Union[Notification, _Mapping]]=..., unread_count: _Optional[int]=...) -> None:
        ...

class GetNotificationsRequest(_message.Message):
    __slots__ = ('unread_only', 'limit', 'before_id')
    UNREAD_ONLY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    BEFORE_ID_FIELD_NUMBER: _ClassVar[int]
    unread_only: bool
    limit: int
    before_id: str

    def __init__(self, unread_only: bool=..., limit: _Optional[int]=..., before_id: _Optional[str]=...) -> None:
        ...

class GetNotificationsResponse(_message.Message):
    __slots__ = ('notifications', 'unread_count')
    NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    UNREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    notifications: _containers.RepeatedCompositeFieldContainer[Notification]
    unread_count: int

    def __init__(self, notifications: _Optional[_Iterable[_Union[Notification, _Mapping]]]=..., unread_count: _Optional[int]=...) -> None:
        ...

class MarkNotificationReadRequest(_message.Message):
    __slots__ = ('notification_id',)
    NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
    notification_id: str

    def __init__(self, notification_id: _Optional[str]=...) -> None:
        ...

class NotificationRule(_message.Message):
    __slots__ = ('notification_type', 'channel', 'enabled')
    NOTIFICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    notification_type: NotificationType
    channel: NotificationChannel
    enabled: bool

    def __init__(self, notification_type: _Optional[_Union[NotificationType, str]]=..., channel: _Optional[_Union[NotificationChannel, str]]=..., enabled: bool=...) -> None:
        ...

class GetNotificationRulesResponse(_message.Message):
    __slots__ = ('rules', 'defaults')
    RULES_FIELD_NUMBER: _ClassVar[int]
    DEFAULTS_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.RepeatedCompositeFieldContainer[NotificationRule]
    defaults: _containers.RepeatedCompositeFieldContainer[NotificationRule]

    def __init__(self, rules: _Optional[_Iterable[_Union[NotificationRule, _Mapping]]]=..., defaults: _Optional[_Iterable[_Union[NotificationRule, _Mapping]]]=...) -> None:
        ...

class UpsertNotificationRuleRequest(_message.Message):
    __slots__ = ('notification_type', 'channel', 'enabled')
    NOTIFICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    notification_type: NotificationType
    channel: NotificationChannel
    enabled: bool

    def __init__(self, notification_type: _Optional[_Union[NotificationType, str]]=..., channel: _Optional[_Union[NotificationChannel, str]]=..., enabled: bool=...) -> None:
        ...

class AlertAudience(_message.Message):
    __slots__ = ('member_ids', 'role_names', 'all_org')
    MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    ROLE_NAMES_FIELD_NUMBER: _ClassVar[int]
    ALL_ORG_FIELD_NUMBER: _ClassVar[int]
    member_ids: _containers.RepeatedScalarFieldContainer[str]
    role_names: _containers.RepeatedScalarFieldContainer[str]
    all_org: bool

    def __init__(self, member_ids: _Optional[_Iterable[str]]=..., role_names: _Optional[_Iterable[str]]=..., all_org: bool=...) -> None:
        ...

class Broadcast(_message.Message):
    __slots__ = ('id', 'title', 'body', 'category', 'deep_link', 'action_label', 'action_url', 'audience', 'metadata', 'target_org_ids', 'all_orgs', 'scheduled_at', 'status', 'created_by', 'created_at', 'dispatched_at', 'orgs_targeted')

    class MetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    DEEP_LINK_FIELD_NUMBER: _ClassVar[int]
    ACTION_LABEL_FIELD_NUMBER: _ClassVar[int]
    ACTION_URL_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TARGET_ORG_IDS_FIELD_NUMBER: _ClassVar[int]
    ALL_ORGS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DISPATCHED_AT_FIELD_NUMBER: _ClassVar[int]
    ORGS_TARGETED_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    body: str
    category: str
    deep_link: str
    action_label: str
    action_url: str
    audience: AlertAudience
    metadata: _containers.ScalarMap[str, str]
    target_org_ids: _containers.RepeatedScalarFieldContainer[str]
    all_orgs: bool
    scheduled_at: _timestamp_pb2.Timestamp
    status: BroadcastStatus
    created_by: str
    created_at: _timestamp_pb2.Timestamp
    dispatched_at: _timestamp_pb2.Timestamp
    orgs_targeted: int

    def __init__(self, id: _Optional[str]=..., title: _Optional[str]=..., body: _Optional[str]=..., category: _Optional[str]=..., deep_link: _Optional[str]=..., action_label: _Optional[str]=..., action_url: _Optional[str]=..., audience: _Optional[_Union[AlertAudience, _Mapping]]=..., metadata: _Optional[_Mapping[str, str]]=..., target_org_ids: _Optional[_Iterable[str]]=..., all_orgs: bool=..., scheduled_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., status: _Optional[_Union[BroadcastStatus, str]]=..., created_by: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., dispatched_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., orgs_targeted: _Optional[int]=...) -> None:
        ...

class CreateBroadcastRequest(_message.Message):
    __slots__ = ('title', 'body', 'category', 'deep_link', 'action_label', 'action_url', 'audience', 'metadata', 'target_org_ids', 'all_orgs', 'scheduled_at')

    class MetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    DEEP_LINK_FIELD_NUMBER: _ClassVar[int]
    ACTION_LABEL_FIELD_NUMBER: _ClassVar[int]
    ACTION_URL_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TARGET_ORG_IDS_FIELD_NUMBER: _ClassVar[int]
    ALL_ORGS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_AT_FIELD_NUMBER: _ClassVar[int]
    title: str
    body: str
    category: str
    deep_link: str
    action_label: str
    action_url: str
    audience: AlertAudience
    metadata: _containers.ScalarMap[str, str]
    target_org_ids: _containers.RepeatedScalarFieldContainer[str]
    all_orgs: bool
    scheduled_at: _timestamp_pb2.Timestamp

    def __init__(self, title: _Optional[str]=..., body: _Optional[str]=..., category: _Optional[str]=..., deep_link: _Optional[str]=..., action_label: _Optional[str]=..., action_url: _Optional[str]=..., audience: _Optional[_Union[AlertAudience, _Mapping]]=..., metadata: _Optional[_Mapping[str, str]]=..., target_org_ids: _Optional[_Iterable[str]]=..., all_orgs: bool=..., scheduled_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListBroadcastsRequest(_message.Message):
    __slots__ = ('limit', 'before_id', 'statuses')
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    BEFORE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    limit: int
    before_id: str
    statuses: _containers.RepeatedScalarFieldContainer[BroadcastStatus]

    def __init__(self, limit: _Optional[int]=..., before_id: _Optional[str]=..., statuses: _Optional[_Iterable[_Union[BroadcastStatus, str]]]=...) -> None:
        ...

class ListBroadcastsResponse(_message.Message):
    __slots__ = ('broadcasts',)
    BROADCASTS_FIELD_NUMBER: _ClassVar[int]
    broadcasts: _containers.RepeatedCompositeFieldContainer[Broadcast]

    def __init__(self, broadcasts: _Optional[_Iterable[_Union[Broadcast, _Mapping]]]=...) -> None:
        ...

class CancelBroadcastRequest(_message.Message):
    __slots__ = ('broadcast_id',)
    BROADCAST_ID_FIELD_NUMBER: _ClassVar[int]
    broadcast_id: str

    def __init__(self, broadcast_id: _Optional[str]=...) -> None:
        ...

class UpdateBroadcastRequest(_message.Message):
    __slots__ = ('broadcast_id', 'title', 'body', 'category', 'deep_link', 'action_label', 'action_url', 'audience', 'scheduled_at')
    BROADCAST_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    DEEP_LINK_FIELD_NUMBER: _ClassVar[int]
    ACTION_LABEL_FIELD_NUMBER: _ClassVar[int]
    ACTION_URL_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_AT_FIELD_NUMBER: _ClassVar[int]
    broadcast_id: str
    title: str
    body: str
    category: str
    deep_link: str
    action_label: str
    action_url: str
    audience: AlertAudience
    scheduled_at: _timestamp_pb2.Timestamp

    def __init__(self, broadcast_id: _Optional[str]=..., title: _Optional[str]=..., body: _Optional[str]=..., category: _Optional[str]=..., deep_link: _Optional[str]=..., action_label: _Optional[str]=..., action_url: _Optional[str]=..., audience: _Optional[_Union[AlertAudience, _Mapping]]=..., scheduled_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...