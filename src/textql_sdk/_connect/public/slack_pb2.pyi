# pylint: skip-file
# mypy: ignore-errors
import datetime
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ..public import cells_pb2 as _cells_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SyncWorkspaceRequest(_message.Message):
    __slots__ = ('team_id',)
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    team_id: str

    def __init__(self, team_id: _Optional[str]=...) -> None:
        ...

class SyncWorkspaceResponse(_message.Message):
    __slots__ = ('queued', 'message')
    QUEUED_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    queued: bool
    message: str

    def __init__(self, queued: bool=..., message: _Optional[str]=...) -> None:
        ...

class ListInstallationsResponse(_message.Message):
    __slots__ = ('installations',)
    INSTALLATIONS_FIELD_NUMBER: _ClassVar[int]
    installations: _containers.RepeatedCompositeFieldContainer[Installation]

    def __init__(self, installations: _Optional[_Iterable[_Union[Installation, _Mapping]]]=...) -> None:
        ...

class Installation(_message.Message):
    __slots__ = ('team_id', 'created_at', 'name')
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    team_id: str
    created_at: _timestamp_pb2.Timestamp
    name: str

    def __init__(self, team_id: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., name: _Optional[str]=...) -> None:
        ...

class GetCurrentUserResponse(_message.Message):
    __slots__ = ('user',)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: SlackUser

    def __init__(self, user: _Optional[_Union[SlackUser, _Mapping]]=...) -> None:
        ...

class SlackUser(_message.Message):
    __slots__ = ('id', 'name', 'real_name', 'email')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REAL_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    real_name: str
    email: str

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., real_name: _Optional[str]=..., email: _Optional[str]=...) -> None:
        ...

class ListChannelsResponse(_message.Message):
    __slots__ = ('channels',)
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    channels: _containers.RepeatedCompositeFieldContainer[_cells_pb2.SlackChannelRef]

    def __init__(self, channels: _Optional[_Iterable[_Union[_cells_pb2.SlackChannelRef, _Mapping]]]=...) -> None:
        ...

class ListUsersResponse(_message.Message):
    __slots__ = ('users',)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[_cells_pb2.SlackUserRef]

    def __init__(self, users: _Optional[_Iterable[_Union[_cells_pb2.SlackUserRef, _Mapping]]]=...) -> None:
        ...

class DeleteInstallationRequest(_message.Message):
    __slots__ = ('team_id',)
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    team_id: str

    def __init__(self, team_id: _Optional[str]=...) -> None:
        ...

class CreateSlackUuidResponse(_message.Message):
    __slots__ = ('uuid',)
    UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: str

    def __init__(self, uuid: _Optional[str]=...) -> None:
        ...

class HandleSlackOAuthCallbackRequest(_message.Message):
    __slots__ = ('code', 'state')
    CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    code: str
    state: str

    def __init__(self, code: _Optional[str]=..., state: _Optional[str]=...) -> None:
        ...

class HandleSlackOAuthCallbackResponse(_message.Message):
    __slots__ = ('success', 'error_message', 'team_id')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error_message: str
    team_id: str

    def __init__(self, success: bool=..., error_message: _Optional[str]=..., team_id: _Optional[str]=...) -> None:
        ...