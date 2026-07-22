from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ConfigSyncStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONFIG_SYNC_STATUS_UNSPECIFIED: _ClassVar[ConfigSyncStatus]
    CONFIG_SYNC_STATUS_SYNCING: _ClassVar[ConfigSyncStatus]
    CONFIG_SYNC_STATUS_SYNCED: _ClassVar[ConfigSyncStatus]
    CONFIG_SYNC_STATUS_ERROR: _ClassVar[ConfigSyncStatus]
CONFIG_SYNC_STATUS_UNSPECIFIED: ConfigSyncStatus
CONFIG_SYNC_STATUS_SYNCING: ConfigSyncStatus
CONFIG_SYNC_STATUS_SYNCED: ConfigSyncStatus
CONFIG_SYNC_STATUS_ERROR: ConfigSyncStatus

class ConfigSource(_message.Message):
    __slots__ = ('file_path', 'sync_status', 'sync_error', 'breaking_patch_id')
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    SYNC_STATUS_FIELD_NUMBER: _ClassVar[int]
    SYNC_ERROR_FIELD_NUMBER: _ClassVar[int]
    BREAKING_PATCH_ID_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    sync_status: ConfigSyncStatus
    sync_error: str
    breaking_patch_id: str

    def __init__(self, file_path: _Optional[str]=..., sync_status: _Optional[_Union[ConfigSyncStatus, str]]=..., sync_error: _Optional[str]=..., breaking_patch_id: _Optional[str]=...) -> None:
        ...