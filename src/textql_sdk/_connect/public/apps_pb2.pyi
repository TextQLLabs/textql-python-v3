import datetime
from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from public import dashboard_pb2 as _dashboard_pb2
from public import identity_pb2 as _identity_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AppActivityRecord(_message.Message):
    __slots__ = ('seq', 'member_id', 'display_name', 'type', 'scope', 'payload_json', 'created_at')
    SEQ_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_JSON_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    seq: int
    member_id: str
    display_name: str
    type: str
    scope: str
    payload_json: str
    created_at: _timestamp_pb2.Timestamp

    def __init__(self, seq: _Optional[int]=..., member_id: _Optional[str]=..., display_name: _Optional[str]=..., type: _Optional[str]=..., scope: _Optional[str]=..., payload_json: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListAppActivitySinceRequest(_message.Message):
    __slots__ = ('app_id', 'scope', 'after_seq', 'limit')
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    AFTER_SEQ_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    app_id: str
    scope: str
    after_seq: int
    limit: int

    def __init__(self, app_id: _Optional[str]=..., scope: _Optional[str]=..., after_seq: _Optional[int]=..., limit: _Optional[int]=...) -> None:
        ...

class ListAppActivitySinceResponse(_message.Message):
    __slots__ = ('records',)
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    records: _containers.RepeatedCompositeFieldContainer[AppActivityRecord]

    def __init__(self, records: _Optional[_Iterable[_Union[AppActivityRecord, _Mapping]]]=...) -> None:
        ...

class AppPresenceMember(_message.Message):
    __slots__ = ('member_id', 'display_name', 'zone')
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    display_name: str
    zone: str

    def __init__(self, member_id: _Optional[str]=..., display_name: _Optional[str]=..., zone: _Optional[str]=...) -> None:
        ...

class AppPresenceSnapshot(_message.Message):
    __slots__ = ('members',)
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    members: _containers.RepeatedCompositeFieldContainer[AppPresenceMember]

    def __init__(self, members: _Optional[_Iterable[_Union[AppPresenceMember, _Mapping]]]=...) -> None:
        ...

class AppActivityBatch(_message.Message):
    __slots__ = ('records',)
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    records: _containers.RepeatedCompositeFieldContainer[AppActivityRecord]

    def __init__(self, records: _Optional[_Iterable[_Union[AppActivityRecord, _Mapping]]]=...) -> None:
        ...

class AppActivityHeartbeat(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class AppActivityStreamEvent(_message.Message):
    __slots__ = ('activity', 'presence', 'heartbeat')
    ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    PRESENCE_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    activity: AppActivityBatch
    presence: AppPresenceSnapshot
    heartbeat: AppActivityHeartbeat

    def __init__(self, activity: _Optional[_Union[AppActivityBatch, _Mapping]]=..., presence: _Optional[_Union[AppPresenceSnapshot, _Mapping]]=..., heartbeat: _Optional[_Union[AppActivityHeartbeat, _Mapping]]=...) -> None:
        ...

class StreamAppActivityRequest(_message.Message):
    __slots__ = ('app_id', 'scope', 'after_seq')
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    AFTER_SEQ_FIELD_NUMBER: _ClassVar[int]
    app_id: str
    scope: str
    after_seq: int

    def __init__(self, app_id: _Optional[str]=..., scope: _Optional[str]=..., after_seq: _Optional[int]=...) -> None:
        ...

class PresenceHeartbeatRequest(_message.Message):
    __slots__ = ('app_id', 'zone')
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    app_id: str
    zone: str

    def __init__(self, app_id: _Optional[str]=..., zone: _Optional[str]=...) -> None:
        ...

class GetAppMemberStateRequest(_message.Message):
    __slots__ = ('app_id',)
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    app_id: str

    def __init__(self, app_id: _Optional[str]=...) -> None:
        ...

class GetAppMemberStateResponse(_message.Message):
    __slots__ = ('value_json',)
    VALUE_JSON_FIELD_NUMBER: _ClassVar[int]
    value_json: str

    def __init__(self, value_json: _Optional[str]=...) -> None:
        ...

class SetAppMemberStateRequest(_message.Message):
    __slots__ = ('app_id', 'value_json')
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_JSON_FIELD_NUMBER: _ClassVar[int]
    app_id: str
    value_json: str

    def __init__(self, app_id: _Optional[str]=..., value_json: _Optional[str]=...) -> None:
        ...

class SetAppMemberStateResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class RecordAppMemberActivityRequest(_message.Message):
    __slots__ = ('app_id', 'type', 'scope', 'payload_json', 'idem_key')
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_JSON_FIELD_NUMBER: _ClassVar[int]
    IDEM_KEY_FIELD_NUMBER: _ClassVar[int]
    app_id: str
    type: str
    scope: str
    payload_json: str
    idem_key: str

    def __init__(self, app_id: _Optional[str]=..., type: _Optional[str]=..., scope: _Optional[str]=..., payload_json: _Optional[str]=..., idem_key: _Optional[str]=...) -> None:
        ...

class RecordAppMemberActivityResponse(_message.Message):
    __slots__ = ('seq', 'created_at')
    SEQ_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    seq: int
    created_at: _timestamp_pb2.Timestamp

    def __init__(self, seq: _Optional[int]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListMyAppMemberActivityRequest(_message.Message):
    __slots__ = ('app_id', 'type', 'limit')
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    app_id: str
    type: str
    limit: int

    def __init__(self, app_id: _Optional[str]=..., type: _Optional[str]=..., limit: _Optional[int]=...) -> None:
        ...

class AppMemberActivityRow(_message.Message):
    __slots__ = ('seq', 'type', 'scope', 'payload_json', 'created_at')
    SEQ_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_JSON_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    seq: int
    type: str
    scope: str
    payload_json: str
    created_at: _timestamp_pb2.Timestamp

    def __init__(self, seq: _Optional[int]=..., type: _Optional[str]=..., scope: _Optional[str]=..., payload_json: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListMyAppMemberActivityResponse(_message.Message):
    __slots__ = ('rows',)
    ROWS_FIELD_NUMBER: _ClassVar[int]
    rows: _containers.RepeatedCompositeFieldContainer[AppMemberActivityRow]

    def __init__(self, rows: _Optional[_Iterable[_Union[AppMemberActivityRow, _Mapping]]]=...) -> None:
        ...

class GetComponentGalleryUrlRequest(_message.Message):
    __slots__ = ('runtime_version', 'accent_hex')
    RUNTIME_VERSION_FIELD_NUMBER: _ClassVar[int]
    ACCENT_HEX_FIELD_NUMBER: _ClassVar[int]
    runtime_version: str
    accent_hex: str

    def __init__(self, runtime_version: _Optional[str]=..., accent_hex: _Optional[str]=...) -> None:
        ...

class GetComponentGalleryUrlResponse(_message.Message):
    __slots__ = ('url',)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str

    def __init__(self, url: _Optional[str]=...) -> None:
        ...

class SetFavoriteRequest(_message.Message):
    __slots__ = ('primitive_type', 'primitive_id', 'favorited')
    PRIMITIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRIMITIVE_ID_FIELD_NUMBER: _ClassVar[int]
    FAVORITED_FIELD_NUMBER: _ClassVar[int]
    primitive_type: str
    primitive_id: str
    favorited: bool

    def __init__(self, primitive_type: _Optional[str]=..., primitive_id: _Optional[str]=..., favorited: bool=...) -> None:
        ...

class SetFavoriteResponse(_message.Message):
    __slots__ = ('favorited',)
    FAVORITED_FIELD_NUMBER: _ClassVar[int]
    favorited: bool

    def __init__(self, favorited: bool=...) -> None:
        ...

class AppHeartbeatRequest(_message.Message):
    __slots__ = ('app_id',)
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    app_id: str

    def __init__(self, app_id: _Optional[str]=...) -> None:
        ...

class App(_message.Message):
    __slots__ = ('id', 'org_id', 'creator_id', 'name', 'description', 'code', 'data_sources', 'html_url', 'screenshot_url', 'console_errors', 'chat_id', 'published_html_url', 'has_unpublished_changes', 'compute_functions', 'files', 'schedule_enabled', 'cron_string', 'folder_id', 'is_favorited', 'capabilities', 'app_db_setup', 'member_features_enabled', 'uses_member_features', 'viewer_grants', 'created_at', 'updated_at', 'refreshed_at', 'published_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    CREATOR_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCES_FIELD_NUMBER: _ClassVar[int]
    HTML_URL_FIELD_NUMBER: _ClassVar[int]
    SCREENSHOT_URL_FIELD_NUMBER: _ClassVar[int]
    CONSOLE_ERRORS_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_HTML_URL_FIELD_NUMBER: _ClassVar[int]
    HAS_UNPUBLISHED_CHANGES_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CRON_STRING_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    IS_FAVORITED_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    APP_DB_SETUP_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FEATURES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    USES_MEMBER_FEATURES_FIELD_NUMBER: _ClassVar[int]
    VIEWER_GRANTS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    REFRESHED_AT_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    org_id: str
    creator_id: str
    name: str
    description: str
    code: str
    data_sources: _containers.RepeatedCompositeFieldContainer[_dashboard_pb2.DataSource]
    html_url: str
    screenshot_url: str
    console_errors: _containers.RepeatedScalarFieldContainer[str]
    chat_id: str
    published_html_url: str
    has_unpublished_changes: bool
    compute_functions: _containers.RepeatedCompositeFieldContainer[ComputeFunction]
    files: _containers.RepeatedCompositeFieldContainer[AppFile]
    schedule_enabled: bool
    cron_string: str
    folder_id: str
    is_favorited: bool
    capabilities: _containers.RepeatedCompositeFieldContainer[Capability]
    app_db_setup: _containers.RepeatedScalarFieldContainer[str]
    member_features_enabled: bool
    uses_member_features: bool
    viewer_grants: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    refreshed_at: _timestamp_pb2.Timestamp
    published_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., org_id: _Optional[str]=..., creator_id: _Optional[str]=..., name: _Optional[str]=..., description: _Optional[str]=..., code: _Optional[str]=..., data_sources: _Optional[_Iterable[_Union[_dashboard_pb2.DataSource, _Mapping]]]=..., html_url: _Optional[str]=..., screenshot_url: _Optional[str]=..., console_errors: _Optional[_Iterable[str]]=..., chat_id: _Optional[str]=..., published_html_url: _Optional[str]=..., has_unpublished_changes: bool=..., compute_functions: _Optional[_Iterable[_Union[ComputeFunction, _Mapping]]]=..., files: _Optional[_Iterable[_Union[AppFile, _Mapping]]]=..., schedule_enabled: bool=..., cron_string: _Optional[str]=..., folder_id: _Optional[str]=..., is_favorited: bool=..., capabilities: _Optional[_Iterable[_Union[Capability, _Mapping]]]=..., app_db_setup: _Optional[_Iterable[str]]=..., member_features_enabled: bool=..., uses_member_features: bool=..., viewer_grants: _Optional[_Iterable[str]]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., refreshed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., published_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CreateAppRequest(_message.Message):
    __slots__ = ('name', 'description', 'code', 'data_sources', 'compute_functions', 'files', 'capabilities', 'app_db_setup')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCES_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    APP_DB_SETUP_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    code: str
    data_sources: _containers.RepeatedCompositeFieldContainer[_dashboard_pb2.DataSource]
    compute_functions: _containers.RepeatedCompositeFieldContainer[ComputeFunction]
    files: _containers.RepeatedCompositeFieldContainer[AppFile]
    capabilities: _containers.RepeatedCompositeFieldContainer[Capability]
    app_db_setup: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., code: _Optional[str]=..., data_sources: _Optional[_Iterable[_Union[_dashboard_pb2.DataSource, _Mapping]]]=..., compute_functions: _Optional[_Iterable[_Union[ComputeFunction, _Mapping]]]=..., files: _Optional[_Iterable[_Union[AppFile, _Mapping]]]=..., capabilities: _Optional[_Iterable[_Union[Capability, _Mapping]]]=..., app_db_setup: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateAppResponse(_message.Message):
    __slots__ = ('app',)
    APP_FIELD_NUMBER: _ClassVar[int]
    app: App

    def __init__(self, app: _Optional[_Union[App, _Mapping]]=...) -> None:
        ...

class DuplicateAppRequest(_message.Message):
    __slots__ = ('app_id',)
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    app_id: str

    def __init__(self, app_id: _Optional[str]=...) -> None:
        ...

class DuplicateAppResponse(_message.Message):
    __slots__ = ('app',)
    APP_FIELD_NUMBER: _ClassVar[int]
    app: App

    def __init__(self, app: _Optional[_Union[App, _Mapping]]=...) -> None:
        ...

class GetAppRequest(_message.Message):
    __slots__ = ('app_id',)
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    app_id: str

    def __init__(self, app_id: _Optional[str]=...) -> None:
        ...

class GetAppResponse(_message.Message):
    __slots__ = ('app', 'has_write_permission')
    APP_FIELD_NUMBER: _ClassVar[int]
    HAS_WRITE_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    app: App
    has_write_permission: bool

    def __init__(self, app: _Optional[_Union[App, _Mapping]]=..., has_write_permission: bool=...) -> None:
        ...

class ListAppsRequest(_message.Message):
    __slots__ = ('search_term', 'limit', 'offset', 'folder_id', 'uncategorized_only', 'shared_with_me')
    SEARCH_TERM_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    UNCATEGORIZED_ONLY_FIELD_NUMBER: _ClassVar[int]
    SHARED_WITH_ME_FIELD_NUMBER: _ClassVar[int]
    search_term: str
    limit: int
    offset: int
    folder_id: str
    uncategorized_only: bool
    shared_with_me: bool

    def __init__(self, search_term: _Optional[str]=..., limit: _Optional[int]=..., offset: _Optional[int]=..., folder_id: _Optional[str]=..., uncategorized_only: bool=..., shared_with_me: bool=...) -> None:
        ...

class ListAppsResponse(_message.Message):
    __slots__ = ('apps', 'total_count')
    APPS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    apps: _containers.RepeatedCompositeFieldContainer[App]
    total_count: int

    def __init__(self, apps: _Optional[_Iterable[_Union[App, _Mapping]]]=..., total_count: _Optional[int]=...) -> None:
        ...

class GetMembersWithAppsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetMembersWithAppsResponse(_message.Message):
    __slots__ = ('members',)
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    members: _containers.RepeatedCompositeFieldContainer[_identity_pb2.MemberPreview]

    def __init__(self, members: _Optional[_Iterable[_Union[_identity_pb2.MemberPreview, _Mapping]]]=...) -> None:
        ...

class UpdateAppRequest(_message.Message):
    __slots__ = ('app_id', 'name', 'description', 'code', 'data_sources', 'replace_data_sources', 'publish', 'compute_functions', 'replace_compute_functions', 'files', 'replace_files', 'schedule_enabled', 'cron_string', 'capabilities', 'replace_capabilities', 'app_db_setup', 'replace_app_db_setup')
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCES_FIELD_NUMBER: _ClassVar[int]
    REPLACE_DATA_SOURCES_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    REPLACE_COMPUTE_FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    REPLACE_FILES_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CRON_STRING_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    REPLACE_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    APP_DB_SETUP_FIELD_NUMBER: _ClassVar[int]
    REPLACE_APP_DB_SETUP_FIELD_NUMBER: _ClassVar[int]
    app_id: str
    name: str
    description: str
    code: str
    data_sources: _containers.RepeatedCompositeFieldContainer[_dashboard_pb2.DataSource]
    replace_data_sources: bool
    publish: bool
    compute_functions: _containers.RepeatedCompositeFieldContainer[ComputeFunction]
    replace_compute_functions: bool
    files: _containers.RepeatedCompositeFieldContainer[AppFile]
    replace_files: bool
    schedule_enabled: bool
    cron_string: str
    capabilities: _containers.RepeatedCompositeFieldContainer[Capability]
    replace_capabilities: bool
    app_db_setup: _containers.RepeatedScalarFieldContainer[str]
    replace_app_db_setup: bool

    def __init__(self, app_id: _Optional[str]=..., name: _Optional[str]=..., description: _Optional[str]=..., code: _Optional[str]=..., data_sources: _Optional[_Iterable[_Union[_dashboard_pb2.DataSource, _Mapping]]]=..., replace_data_sources: bool=..., publish: bool=..., compute_functions: _Optional[_Iterable[_Union[ComputeFunction, _Mapping]]]=..., replace_compute_functions: bool=..., files: _Optional[_Iterable[_Union[AppFile, _Mapping]]]=..., replace_files: bool=..., schedule_enabled: bool=..., cron_string: _Optional[str]=..., capabilities: _Optional[_Iterable[_Union[Capability, _Mapping]]]=..., replace_capabilities: bool=..., app_db_setup: _Optional[_Iterable[str]]=..., replace_app_db_setup: bool=...) -> None:
        ...

class UpdateAppResponse(_message.Message):
    __slots__ = ('app',)
    APP_FIELD_NUMBER: _ClassVar[int]
    app: App

    def __init__(self, app: _Optional[_Union[App, _Mapping]]=...) -> None:
        ...

class DeleteAppRequest(_message.Message):
    __slots__ = ('app_id',)
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    app_id: str

    def __init__(self, app_id: _Optional[str]=...) -> None:
        ...

class MoveAppToFolderRequest(_message.Message):
    __slots__ = ('app_id', 'folder_id')
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    app_id: str
    folder_id: str

    def __init__(self, app_id: _Optional[str]=..., folder_id: _Optional[str]=...) -> None:
        ...

class MoveAppToFolderResponse(_message.Message):
    __slots__ = ('app',)
    APP_FIELD_NUMBER: _ClassVar[int]
    app: App

    def __init__(self, app: _Optional[_Union[App, _Mapping]]=...) -> None:
        ...

class RefreshAppRequest(_message.Message):
    __slots__ = ('app_id',)
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    app_id: str

    def __init__(self, app_id: _Optional[str]=...) -> None:
        ...

class RefreshAppResponse(_message.Message):
    __slots__ = ('app',)
    APP_FIELD_NUMBER: _ClassVar[int]
    app: App

    def __init__(self, app: _Optional[_Union[App, _Mapping]]=...) -> None:
        ...

class ComputeFunctionParam(_message.Message):
    __slots__ = ('name', 'type', 'description')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    description: str

    def __init__(self, name: _Optional[str]=..., type: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...

class CapabilityParam(_message.Message):
    __slots__ = ('name', 'type', 'description')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    description: str

    def __init__(self, name: _Optional[str]=..., type: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...

class Capability(_message.Message):
    __slots__ = ('type', 'name', 'connector_id', 'statement', 'scope', 'subject', 'body', 'parameters')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    type: str
    name: str
    connector_id: int
    statement: str
    scope: str
    subject: str
    body: str
    parameters: _containers.RepeatedCompositeFieldContainer[CapabilityParam]

    def __init__(self, type: _Optional[str]=..., name: _Optional[str]=..., connector_id: _Optional[int]=..., statement: _Optional[str]=..., scope: _Optional[str]=..., subject: _Optional[str]=..., body: _Optional[str]=..., parameters: _Optional[_Iterable[_Union[CapabilityParam, _Mapping]]]=...) -> None:
        ...

class ComputeFunction(_message.Message):
    __slots__ = ('name', 'description', 'params', 'returns', 'code', 'tql_path', 'tql', 'grant', 'connector_id', 'sql')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    RETURNS_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    TQL_PATH_FIELD_NUMBER: _ClassVar[int]
    TQL_FIELD_NUMBER: _ClassVar[int]
    GRANT_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    SQL_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    params: _containers.RepeatedCompositeFieldContainer[ComputeFunctionParam]
    returns: str
    code: str
    tql_path: str
    tql: str
    grant: _dashboard_pb2.Grant
    connector_id: int
    sql: str

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., params: _Optional[_Iterable[_Union[ComputeFunctionParam, _Mapping]]]=..., returns: _Optional[str]=..., code: _Optional[str]=..., tql_path: _Optional[str]=..., tql: _Optional[str]=..., grant: _Optional[_Union[_dashboard_pb2.Grant, _Mapping]]=..., connector_id: _Optional[int]=..., sql: _Optional[str]=...) -> None:
        ...

class InvokeAppComputeFunctionRequest(_message.Message):
    __slots__ = ('app_id', 'function_name', 'params_json')
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMS_JSON_FIELD_NUMBER: _ClassVar[int]
    app_id: str
    function_name: str
    params_json: str

    def __init__(self, app_id: _Optional[str]=..., function_name: _Optional[str]=..., params_json: _Optional[str]=...) -> None:
        ...

class InvokeAppComputeFunctionResponse(_message.Message):
    __slots__ = ('result_json', 'invoke_mode', 'rewarmed')
    RESULT_JSON_FIELD_NUMBER: _ClassVar[int]
    INVOKE_MODE_FIELD_NUMBER: _ClassVar[int]
    REWARMED_FIELD_NUMBER: _ClassVar[int]
    result_json: str
    invoke_mode: str
    rewarmed: bool

    def __init__(self, result_json: _Optional[str]=..., invoke_mode: _Optional[str]=..., rewarmed: bool=...) -> None:
        ...

class AppFile(_message.Message):
    __slots__ = ('path', 'content')
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    path: str
    content: str

    def __init__(self, path: _Optional[str]=..., content: _Optional[str]=...) -> None:
        ...

class AppVersion(_message.Message):
    __slots__ = ('id', 'app_id', 'version_number', 'code', 'data_sources', 'compute_functions', 'files', 'name', 'description', 'published_html_url', 'published_by', 'label', 'published_at', 'publisher')
    ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCES_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_HTML_URL_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_BY_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    id: str
    app_id: str
    version_number: int
    code: str
    data_sources: _containers.RepeatedCompositeFieldContainer[_dashboard_pb2.DataSource]
    compute_functions: _containers.RepeatedCompositeFieldContainer[ComputeFunction]
    files: _containers.RepeatedCompositeFieldContainer[AppFile]
    name: str
    description: str
    published_html_url: str
    published_by: str
    label: str
    published_at: _timestamp_pb2.Timestamp
    publisher: _identity_pb2.MemberPreview

    def __init__(self, id: _Optional[str]=..., app_id: _Optional[str]=..., version_number: _Optional[int]=..., code: _Optional[str]=..., data_sources: _Optional[_Iterable[_Union[_dashboard_pb2.DataSource, _Mapping]]]=..., compute_functions: _Optional[_Iterable[_Union[ComputeFunction, _Mapping]]]=..., files: _Optional[_Iterable[_Union[AppFile, _Mapping]]]=..., name: _Optional[str]=..., description: _Optional[str]=..., published_html_url: _Optional[str]=..., published_by: _Optional[str]=..., label: _Optional[str]=..., published_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., publisher: _Optional[_Union[_identity_pb2.MemberPreview, _Mapping]]=...) -> None:
        ...

class ListAppVersionsRequest(_message.Message):
    __slots__ = ('app_id', 'limit', 'offset')
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    app_id: str
    limit: int
    offset: int

    def __init__(self, app_id: _Optional[str]=..., limit: _Optional[int]=..., offset: _Optional[int]=...) -> None:
        ...

class ListAppVersionsResponse(_message.Message):
    __slots__ = ('versions', 'total_count')
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    versions: _containers.RepeatedCompositeFieldContainer[AppVersion]
    total_count: int

    def __init__(self, versions: _Optional[_Iterable[_Union[AppVersion, _Mapping]]]=..., total_count: _Optional[int]=...) -> None:
        ...

class GetAppVersionRequest(_message.Message):
    __slots__ = ('app_id', 'version_number')
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    app_id: str
    version_number: int

    def __init__(self, app_id: _Optional[str]=..., version_number: _Optional[int]=...) -> None:
        ...

class GetAppVersionResponse(_message.Message):
    __slots__ = ('version',)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: AppVersion

    def __init__(self, version: _Optional[_Union[AppVersion, _Mapping]]=...) -> None:
        ...

class RestoreAppVersionRequest(_message.Message):
    __slots__ = ('app_id', 'version_number')
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    app_id: str
    version_number: int

    def __init__(self, app_id: _Optional[str]=..., version_number: _Optional[int]=...) -> None:
        ...

class RestoreAppVersionResponse(_message.Message):
    __slots__ = ('app',)
    APP_FIELD_NUMBER: _ClassVar[int]
    app: App

    def __init__(self, app: _Optional[_Union[App, _Mapping]]=...) -> None:
        ...

class GetAppViewStatsRequest(_message.Message):
    __slots__ = ('app_id',)
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    app_id: str

    def __init__(self, app_id: _Optional[str]=...) -> None:
        ...

class AppViewerInfo(_message.Message):
    __slots__ = ('member_id', 'last_viewed', 'view_count', 'display_name', 'recent_view_times')
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_VIEWED_FIELD_NUMBER: _ClassVar[int]
    VIEW_COUNT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    RECENT_VIEW_TIMES_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    last_viewed: _timestamp_pb2.Timestamp
    view_count: int
    display_name: str
    recent_view_times: _containers.RepeatedCompositeFieldContainer[_timestamp_pb2.Timestamp]

    def __init__(self, member_id: _Optional[str]=..., last_viewed: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., view_count: _Optional[int]=..., display_name: _Optional[str]=..., recent_view_times: _Optional[_Iterable[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]]=...) -> None:
        ...

class GetAppViewStatsResponse(_message.Message):
    __slots__ = ('total_views', 'unique_viewers', 'recent_viewers')
    TOTAL_VIEWS_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_VIEWERS_FIELD_NUMBER: _ClassVar[int]
    RECENT_VIEWERS_FIELD_NUMBER: _ClassVar[int]
    total_views: int
    unique_viewers: int
    recent_viewers: _containers.RepeatedCompositeFieldContainer[AppViewerInfo]

    def __init__(self, total_views: _Optional[int]=..., unique_viewers: _Optional[int]=..., recent_viewers: _Optional[_Iterable[_Union[AppViewerInfo, _Mapping]]]=...) -> None:
        ...