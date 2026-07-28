# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
# pylint: skip-file
# mypy: ignore-errors
import datetime
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ..public import common_pb2 as _common_pb2
from ..public import config_source_pb2 as _config_source_pb2
from ..public import identity_pb2 as _identity_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DashboardType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DASHBOARD_TYPE_UNSPECIFIED: _ClassVar[DashboardType]
    DASHBOARD_TYPE_STREAMLIT: _ClassVar[DashboardType]
    DASHBOARD_TYPE_HTML: _ClassVar[DashboardType]
    DASHBOARD_TYPE_DASH: _ClassVar[DashboardType]

class DashboardStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DASHBOARD_STATUS_UNSPECIFIED: _ClassVar[DashboardStatus]
    DASHBOARD_STATUS_DRAFT: _ClassVar[DashboardStatus]
    DASHBOARD_STATUS_PUBLISHED: _ClassVar[DashboardStatus]

class DashboardSortField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DASHBOARD_SORT_FIELD_UNSPECIFIED: _ClassVar[DashboardSortField]
    DASHBOARD_SORT_FIELD_NAME: _ClassVar[DashboardSortField]
    DASHBOARD_SORT_FIELD_CREATED_AT: _ClassVar[DashboardSortField]
    DASHBOARD_SORT_FIELD_UPDATED_AT: _ClassVar[DashboardSortField]
    DASHBOARD_SORT_FIELD_REFRESHED_AT: _ClassVar[DashboardSortField]
DASHBOARD_TYPE_UNSPECIFIED: DashboardType
DASHBOARD_TYPE_STREAMLIT: DashboardType
DASHBOARD_TYPE_HTML: DashboardType
DASHBOARD_TYPE_DASH: DashboardType
DASHBOARD_STATUS_UNSPECIFIED: DashboardStatus
DASHBOARD_STATUS_DRAFT: DashboardStatus
DASHBOARD_STATUS_PUBLISHED: DashboardStatus
DASHBOARD_SORT_FIELD_UNSPECIFIED: DashboardSortField
DASHBOARD_SORT_FIELD_NAME: DashboardSortField
DASHBOARD_SORT_FIELD_CREATED_AT: DashboardSortField
DASHBOARD_SORT_FIELD_UPDATED_AT: DashboardSortField
DASHBOARD_SORT_FIELD_REFRESHED_AT: DashboardSortField

class Dashboard(_message.Message):
    __slots__ = ('id', 'org_id', 'creator_id', 'name', 'description', 'code', 'type', 'chat_id', 'cell_id', 'is_public', 'screenshot_url', 'html_url', 'created_at', 'updated_at', 'refreshed_at', 'creator', 'streamlit_url', 'status', 'published_code', 'published_at', 'has_unpublished_changes', 'data_sources', 'schedule_enabled', 'cron_string', 'latest_scheduled_run_at', 'folder_id', 'config_source', 'is_favorited')
    ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    CREATOR_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    SCREENSHOT_URL_FIELD_NUMBER: _ClassVar[int]
    HTML_URL_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    REFRESHED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    STREAMLIT_URL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_CODE_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    HAS_UNPUBLISHED_CHANGES_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCES_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CRON_STRING_FIELD_NUMBER: _ClassVar[int]
    LATEST_SCHEDULED_RUN_AT_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_SOURCE_FIELD_NUMBER: _ClassVar[int]
    IS_FAVORITED_FIELD_NUMBER: _ClassVar[int]
    id: str
    org_id: str
    creator_id: str
    name: str
    description: str
    code: str
    type: DashboardType
    chat_id: str
    cell_id: str
    is_public: bool
    screenshot_url: str
    html_url: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    refreshed_at: _timestamp_pb2.Timestamp
    creator: DashboardCreator
    streamlit_url: str
    status: DashboardStatus
    published_code: str
    published_at: _timestamp_pb2.Timestamp
    has_unpublished_changes: bool
    data_sources: _containers.RepeatedCompositeFieldContainer[DataSource]
    schedule_enabled: bool
    cron_string: str
    latest_scheduled_run_at: _timestamp_pb2.Timestamp
    folder_id: str
    config_source: _config_source_pb2.ConfigSource
    is_favorited: bool

    def __init__(self, id: _Optional[str]=..., org_id: _Optional[str]=..., creator_id: _Optional[str]=..., name: _Optional[str]=..., description: _Optional[str]=..., code: _Optional[str]=..., type: _Optional[_Union[DashboardType, str]]=..., chat_id: _Optional[str]=..., cell_id: _Optional[str]=..., is_public: bool=..., screenshot_url: _Optional[str]=..., html_url: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., refreshed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., creator: _Optional[_Union[DashboardCreator, _Mapping]]=..., streamlit_url: _Optional[str]=..., status: _Optional[_Union[DashboardStatus, str]]=..., published_code: _Optional[str]=..., published_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., has_unpublished_changes: bool=..., data_sources: _Optional[_Iterable[_Union[DataSource, _Mapping]]]=..., schedule_enabled: bool=..., cron_string: _Optional[str]=..., latest_scheduled_run_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., folder_id: _Optional[str]=..., config_source: _Optional[_Union[_config_source_pb2.ConfigSource, _Mapping]]=..., is_favorited: bool=...) -> None:
        ...

class DataSource(_message.Message):
    __slots__ = ('type', 'name', 'sql_query', 'file', 'python_code', 'ontology_sql', 'library_tql', 'parameters', 'grant')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SQL_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    PYTHON_CODE_FIELD_NUMBER: _ClassVar[int]
    ONTOLOGY_SQL_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_TQL_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    GRANT_FIELD_NUMBER: _ClassVar[int]
    type: str
    name: str
    sql_query: SqlQuerySource
    file: FileSource
    python_code: PythonCodeSource
    ontology_sql: OntologySqlSource
    library_tql: LibraryTQLSource
    parameters: _containers.RepeatedCompositeFieldContainer[QueryParameter]
    grant: Grant

    def __init__(self, type: _Optional[str]=..., name: _Optional[str]=..., sql_query: _Optional[_Union[SqlQuerySource, _Mapping]]=..., file: _Optional[_Union[FileSource, _Mapping]]=..., python_code: _Optional[_Union[PythonCodeSource, _Mapping]]=..., ontology_sql: _Optional[_Union[OntologySqlSource, _Mapping]]=..., library_tql: _Optional[_Union[LibraryTQLSource, _Mapping]]=..., parameters: _Optional[_Iterable[_Union[QueryParameter, _Mapping]]]=..., grant: _Optional[_Union[Grant, _Mapping]]=...) -> None:
        ...

class Grant(_message.Message):
    __slots__ = ('roles', 'members')
    ROLES_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    roles: _containers.RepeatedScalarFieldContainer[str]
    members: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, roles: _Optional[_Iterable[str]]=..., members: _Optional[_Iterable[str]]=...) -> None:
        ...

class QueryParameter(_message.Message):
    __slots__ = ('name', 'type', 'default')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    default: str

    def __init__(self, name: _Optional[str]=..., type: _Optional[str]=..., default: _Optional[str]=...) -> None:
        ...

class SqlQuerySource(_message.Message):
    __slots__ = ('query', 'connector_id', 'predicate')
    QUERY_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    PREDICATE_FIELD_NUMBER: _ClassVar[int]
    query: str
    connector_id: int
    predicate: str

    def __init__(self, query: _Optional[str]=..., connector_id: _Optional[int]=..., predicate: _Optional[str]=...) -> None:
        ...

class FileSource(_message.Message):
    __slots__ = ('dataset_id', 'file_name', 'sheet_index')
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    SHEET_INDEX_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    file_name: str
    sheet_index: int

    def __init__(self, dataset_id: _Optional[str]=..., file_name: _Optional[str]=..., sheet_index: _Optional[int]=...) -> None:
        ...

class PythonCodeSource(_message.Message):
    __slots__ = ('code',)
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str

    def __init__(self, code: _Optional[str]=...) -> None:
        ...

class OntologySqlSource(_message.Message):
    __slots__ = ('query', 'dataset', 'ontology_id')
    QUERY_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    ONTOLOGY_ID_FIELD_NUMBER: _ClassVar[int]
    query: str
    dataset: str
    ontology_id: int

    def __init__(self, query: _Optional[str]=..., dataset: _Optional[str]=..., ontology_id: _Optional[int]=...) -> None:
        ...

class LibraryTQLSource(_message.Message):
    __slots__ = ('tql_path', 'connector_id', 'params_json')
    TQL_PATH_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMS_JSON_FIELD_NUMBER: _ClassVar[int]
    tql_path: str
    connector_id: int
    params_json: str

    def __init__(self, tql_path: _Optional[str]=..., connector_id: _Optional[int]=..., params_json: _Optional[str]=...) -> None:
        ...

class DashboardCreator(_message.Message):
    __slots__ = ('member_id', 'member_email', 'member_name')
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    MEMBER_NAME_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    member_email: str
    member_name: str

    def __init__(self, member_id: _Optional[str]=..., member_email: _Optional[str]=..., member_name: _Optional[str]=...) -> None:
        ...

class DashboardFolder(_message.Message):
    __slots__ = ('id', 'org_id', 'parent_id', 'name', 'creator_id', 'created_at', 'updated_at', 'dashboard_count', 'total_dashboard_count', 'children', 'app_count', 'total_app_count')
    ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATOR_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DASHBOARD_COUNT_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    APP_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_APP_COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    org_id: str
    parent_id: str
    name: str
    creator_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    dashboard_count: int
    total_dashboard_count: int
    children: _containers.RepeatedCompositeFieldContainer[DashboardFolder]
    app_count: int
    total_app_count: int

    def __init__(self, id: _Optional[str]=..., org_id: _Optional[str]=..., parent_id: _Optional[str]=..., name: _Optional[str]=..., creator_id: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., dashboard_count: _Optional[int]=..., total_dashboard_count: _Optional[int]=..., children: _Optional[_Iterable[_Union[DashboardFolder, _Mapping]]]=..., app_count: _Optional[int]=..., total_app_count: _Optional[int]=...) -> None:
        ...

class CreateDashboardRequest(_message.Message):
    __slots__ = ('name', 'description', 'code', 'type', 'html_url', 'chat_id', 'cell_id', 'folder_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    HTML_URL_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    code: str
    type: DashboardType
    html_url: str
    chat_id: str
    cell_id: str
    folder_id: str

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., code: _Optional[str]=..., type: _Optional[_Union[DashboardType, str]]=..., html_url: _Optional[str]=..., chat_id: _Optional[str]=..., cell_id: _Optional[str]=..., folder_id: _Optional[str]=...) -> None:
        ...

class CreateDashboardResponse(_message.Message):
    __slots__ = ('dashboard',)
    DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    dashboard: Dashboard

    def __init__(self, dashboard: _Optional[_Union[Dashboard, _Mapping]]=...) -> None:
        ...

class GetDashboardRequest(_message.Message):
    __slots__ = ('dashboard_id',)
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str

    def __init__(self, dashboard_id: _Optional[str]=...) -> None:
        ...

class GetDashboardResponse(_message.Message):
    __slots__ = ('dashboard', 'has_write_permission')
    DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    HAS_WRITE_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    dashboard: Dashboard
    has_write_permission: bool

    def __init__(self, dashboard: _Optional[_Union[Dashboard, _Mapping]]=..., has_write_permission: bool=...) -> None:
        ...

class ListDashboardsRequest(_message.Message):
    __slots__ = ('search_term', 'my_dashboards_only', 'sort_by', 'sort_direction', 'limit', 'offset', 'folder_id', 'uncategorized_only', 'creator_member_id', 'shared_with_me', 'creator_member_ids', 'status_filter')
    SEARCH_TERM_FIELD_NUMBER: _ClassVar[int]
    MY_DASHBOARDS_ONLY_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    SORT_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    UNCATEGORIZED_ONLY_FIELD_NUMBER: _ClassVar[int]
    CREATOR_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    SHARED_WITH_ME_FIELD_NUMBER: _ClassVar[int]
    CREATOR_MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FILTER_FIELD_NUMBER: _ClassVar[int]
    search_term: str
    my_dashboards_only: bool
    sort_by: DashboardSortField
    sort_direction: _common_pb2.SortDirection
    limit: int
    offset: int
    folder_id: str
    uncategorized_only: bool
    creator_member_id: str
    shared_with_me: bool
    creator_member_ids: _containers.RepeatedScalarFieldContainer[str]
    status_filter: DashboardStatus

    def __init__(self, search_term: _Optional[str]=..., my_dashboards_only: bool=..., sort_by: _Optional[_Union[DashboardSortField, str]]=..., sort_direction: _Optional[_Union[_common_pb2.SortDirection, str]]=..., limit: _Optional[int]=..., offset: _Optional[int]=..., folder_id: _Optional[str]=..., uncategorized_only: bool=..., creator_member_id: _Optional[str]=..., shared_with_me: bool=..., creator_member_ids: _Optional[_Iterable[str]]=..., status_filter: _Optional[_Union[DashboardStatus, str]]=...) -> None:
        ...

class ListDashboardsResponse(_message.Message):
    __slots__ = ('dashboards', 'total_count')
    DASHBOARDS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    dashboards: _containers.RepeatedCompositeFieldContainer[Dashboard]
    total_count: int

    def __init__(self, dashboards: _Optional[_Iterable[_Union[Dashboard, _Mapping]]]=..., total_count: _Optional[int]=...) -> None:
        ...

class UpdateDashboardRequest(_message.Message):
    __slots__ = ('dashboard_id', 'name', 'description', 'code', 'type', 'html_url', 'data_sources')
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    HTML_URL_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCES_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    name: str
    description: str
    code: str
    type: DashboardType
    html_url: str
    data_sources: DataSourcesPatch

    def __init__(self, dashboard_id: _Optional[str]=..., name: _Optional[str]=..., description: _Optional[str]=..., code: _Optional[str]=..., type: _Optional[_Union[DashboardType, str]]=..., html_url: _Optional[str]=..., data_sources: _Optional[_Union[DataSourcesPatch, _Mapping]]=...) -> None:
        ...

class DataSourcesPatch(_message.Message):
    __slots__ = ('sources',)
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    sources: _containers.RepeatedCompositeFieldContainer[DataSource]

    def __init__(self, sources: _Optional[_Iterable[_Union[DataSource, _Mapping]]]=...) -> None:
        ...

class UpdateDashboardResponse(_message.Message):
    __slots__ = ('dashboard',)
    DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    dashboard: Dashboard

    def __init__(self, dashboard: _Optional[_Union[Dashboard, _Mapping]]=...) -> None:
        ...

class DeleteDashboardRequest(_message.Message):
    __slots__ = ('dashboard_id',)
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str

    def __init__(self, dashboard_id: _Optional[str]=...) -> None:
        ...

class DuplicateDashboardRequest(_message.Message):
    __slots__ = ('dashboard_id', 'name')
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    name: str

    def __init__(self, dashboard_id: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class DuplicateDashboardResponse(_message.Message):
    __slots__ = ('dashboard',)
    DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    dashboard: Dashboard

    def __init__(self, dashboard: _Optional[_Union[Dashboard, _Mapping]]=...) -> None:
        ...

class SpawnDashboardRequest(_message.Message):
    __slots__ = ('dashboard_id', 'force_restart', 'refresh_data_only', 'refresh_source_names', 'refresh_code_only')
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_RESTART_FIELD_NUMBER: _ClassVar[int]
    REFRESH_DATA_ONLY_FIELD_NUMBER: _ClassVar[int]
    REFRESH_SOURCE_NAMES_FIELD_NUMBER: _ClassVar[int]
    REFRESH_CODE_ONLY_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    force_restart: bool
    refresh_data_only: bool
    refresh_source_names: _containers.RepeatedScalarFieldContainer[str]
    refresh_code_only: bool

    def __init__(self, dashboard_id: _Optional[str]=..., force_restart: bool=..., refresh_data_only: bool=..., refresh_source_names: _Optional[_Iterable[str]]=..., refresh_code_only: bool=...) -> None:
        ...

class SpawnDashboardResponse(_message.Message):
    __slots__ = ('refreshed_at',)
    REFRESHED_AT_FIELD_NUMBER: _ClassVar[int]
    refreshed_at: _timestamp_pb2.Timestamp

    def __init__(self, refreshed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CheckDashboardHealthRequest(_message.Message):
    __slots__ = ('dashboard_ids',)
    DASHBOARD_IDS_FIELD_NUMBER: _ClassVar[int]
    dashboard_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, dashboard_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class CheckDashboardHealthResponse(_message.Message):
    __slots__ = ('dashboards',)

    class HealthStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HEALTH_STATUS_NOT_RUNNING: _ClassVar[CheckDashboardHealthResponse.HealthStatus]
        HEALTH_STATUS_HEALTHY: _ClassVar[CheckDashboardHealthResponse.HealthStatus]
        HEALTH_STATUS_STARTING: _ClassVar[CheckDashboardHealthResponse.HealthStatus]
        HEALTH_STATUS_FAILED: _ClassVar[CheckDashboardHealthResponse.HealthStatus]
        HEALTH_STATUS_UPDATING: _ClassVar[CheckDashboardHealthResponse.HealthStatus]
    HEALTH_STATUS_NOT_RUNNING: CheckDashboardHealthResponse.HealthStatus
    HEALTH_STATUS_HEALTHY: CheckDashboardHealthResponse.HealthStatus
    HEALTH_STATUS_STARTING: CheckDashboardHealthResponse.HealthStatus
    HEALTH_STATUS_FAILED: CheckDashboardHealthResponse.HealthStatus
    HEALTH_STATUS_UPDATING: CheckDashboardHealthResponse.HealthStatus

    class DashboardHealth(_message.Message):
        __slots__ = ('dashboard_id', 'status', 'error_message', 'streamlit_url', 'embed_url', 'refreshed_at', 'code', 'data_sources', 'dashboard_status', 'published_code', 'published_at', 'schedule_enabled', 'cron_string', 'warnings')
        DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        STREAMLIT_URL_FIELD_NUMBER: _ClassVar[int]
        EMBED_URL_FIELD_NUMBER: _ClassVar[int]
        REFRESHED_AT_FIELD_NUMBER: _ClassVar[int]
        CODE_FIELD_NUMBER: _ClassVar[int]
        DATA_SOURCES_FIELD_NUMBER: _ClassVar[int]
        DASHBOARD_STATUS_FIELD_NUMBER: _ClassVar[int]
        PUBLISHED_CODE_FIELD_NUMBER: _ClassVar[int]
        PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
        SCHEDULE_ENABLED_FIELD_NUMBER: _ClassVar[int]
        CRON_STRING_FIELD_NUMBER: _ClassVar[int]
        WARNINGS_FIELD_NUMBER: _ClassVar[int]
        dashboard_id: str
        status: CheckDashboardHealthResponse.HealthStatus
        error_message: str
        streamlit_url: str
        embed_url: str
        refreshed_at: _timestamp_pb2.Timestamp
        code: str
        data_sources: _containers.RepeatedCompositeFieldContainer[DataSource]
        dashboard_status: DashboardStatus
        published_code: str
        published_at: _timestamp_pb2.Timestamp
        schedule_enabled: bool
        cron_string: str
        warnings: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, dashboard_id: _Optional[str]=..., status: _Optional[_Union[CheckDashboardHealthResponse.HealthStatus, str]]=..., error_message: _Optional[str]=..., streamlit_url: _Optional[str]=..., embed_url: _Optional[str]=..., refreshed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., code: _Optional[str]=..., data_sources: _Optional[_Iterable[_Union[DataSource, _Mapping]]]=..., dashboard_status: _Optional[_Union[DashboardStatus, str]]=..., published_code: _Optional[str]=..., published_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., schedule_enabled: bool=..., cron_string: _Optional[str]=..., warnings: _Optional[_Iterable[str]]=...) -> None:
            ...
    DASHBOARDS_FIELD_NUMBER: _ClassVar[int]
    dashboards: _containers.RepeatedCompositeFieldContainer[CheckDashboardHealthResponse.DashboardHealth]

    def __init__(self, dashboards: _Optional[_Iterable[_Union[CheckDashboardHealthResponse.DashboardHealth, _Mapping]]]=...) -> None:
        ...

class RegenerateScreenshotRequest(_message.Message):
    __slots__ = ('dashboard_id',)
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str

    def __init__(self, dashboard_id: _Optional[str]=...) -> None:
        ...

class RegenerateScreenshotResponse(_message.Message):
    __slots__ = ('screenshot_url',)
    SCREENSHOT_URL_FIELD_NUMBER: _ClassVar[int]
    screenshot_url: str

    def __init__(self, screenshot_url: _Optional[str]=...) -> None:
        ...

class GetMembersWithDashboardsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetMembersWithDashboardsResponse(_message.Message):
    __slots__ = ('members',)
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    members: _containers.RepeatedCompositeFieldContainer[_identity_pb2.MemberPreview]

    def __init__(self, members: _Optional[_Iterable[_Union[_identity_pb2.MemberPreview, _Mapping]]]=...) -> None:
        ...

class PublishDashboardRequest(_message.Message):
    __slots__ = ('dashboard_id', 'label')
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    label: str

    def __init__(self, dashboard_id: _Optional[str]=..., label: _Optional[str]=...) -> None:
        ...

class PublishDashboardResponse(_message.Message):
    __slots__ = ('dashboard',)
    DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    dashboard: Dashboard

    def __init__(self, dashboard: _Optional[_Union[Dashboard, _Mapping]]=...) -> None:
        ...

class DiscardDashboardChangesRequest(_message.Message):
    __slots__ = ('dashboard_id',)
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str

    def __init__(self, dashboard_id: _Optional[str]=...) -> None:
        ...

class DiscardDashboardChangesResponse(_message.Message):
    __slots__ = ('dashboard',)
    DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    dashboard: Dashboard

    def __init__(self, dashboard: _Optional[_Union[Dashboard, _Mapping]]=...) -> None:
        ...

class UpdateDashboardScheduleRequest(_message.Message):
    __slots__ = ('dashboard_id', 'schedule_enabled', 'cron_string', 'data_sources')
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CRON_STRING_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCES_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    schedule_enabled: bool
    cron_string: str
    data_sources: _containers.RepeatedCompositeFieldContainer[DataSource]

    def __init__(self, dashboard_id: _Optional[str]=..., schedule_enabled: bool=..., cron_string: _Optional[str]=..., data_sources: _Optional[_Iterable[_Union[DataSource, _Mapping]]]=...) -> None:
        ...

class UpdateDashboardScheduleResponse(_message.Message):
    __slots__ = ('dashboard',)
    DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    dashboard: Dashboard

    def __init__(self, dashboard: _Optional[_Union[Dashboard, _Mapping]]=...) -> None:
        ...

class RunScheduledDashboardRequest(_message.Message):
    __slots__ = ('dashboard_id',)
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str

    def __init__(self, dashboard_id: _Optional[str]=...) -> None:
        ...

class RunScheduledDashboardResponse(_message.Message):
    __slots__ = ('dashboard_id',)
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str

    def __init__(self, dashboard_id: _Optional[str]=...) -> None:
        ...

class CreateDashboardFolderRequest(_message.Message):
    __slots__ = ('name', 'parent_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    parent_id: str

    def __init__(self, name: _Optional[str]=..., parent_id: _Optional[str]=...) -> None:
        ...

class CreateDashboardFolderResponse(_message.Message):
    __slots__ = ('folder',)
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    folder: DashboardFolder

    def __init__(self, folder: _Optional[_Union[DashboardFolder, _Mapping]]=...) -> None:
        ...

class ListDashboardFoldersRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListDashboardFoldersResponse(_message.Message):
    __slots__ = ('folders',)
    FOLDERS_FIELD_NUMBER: _ClassVar[int]
    folders: _containers.RepeatedCompositeFieldContainer[DashboardFolder]

    def __init__(self, folders: _Optional[_Iterable[_Union[DashboardFolder, _Mapping]]]=...) -> None:
        ...

class UpdateDashboardFolderRequest(_message.Message):
    __slots__ = ('folder_id', 'name', 'parent_id')
    FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    folder_id: str
    name: str
    parent_id: str

    def __init__(self, folder_id: _Optional[str]=..., name: _Optional[str]=..., parent_id: _Optional[str]=...) -> None:
        ...

class UpdateDashboardFolderResponse(_message.Message):
    __slots__ = ('folder',)
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    folder: DashboardFolder

    def __init__(self, folder: _Optional[_Union[DashboardFolder, _Mapping]]=...) -> None:
        ...

class DeleteDashboardFolderRequest(_message.Message):
    __slots__ = ('folder_id',)
    FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    folder_id: str

    def __init__(self, folder_id: _Optional[str]=...) -> None:
        ...

class MoveDashboardToFolderRequest(_message.Message):
    __slots__ = ('dashboard_id', 'folder_id')
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    folder_id: str

    def __init__(self, dashboard_id: _Optional[str]=..., folder_id: _Optional[str]=...) -> None:
        ...

class MoveDashboardToFolderResponse(_message.Message):
    __slots__ = ('dashboard',)
    DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    dashboard: Dashboard

    def __init__(self, dashboard: _Optional[_Union[Dashboard, _Mapping]]=...) -> None:
        ...

class WatchDashboardHealthRequest(_message.Message):
    __slots__ = ('dashboard_id',)
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str

    def __init__(self, dashboard_id: _Optional[str]=...) -> None:
        ...

class DashboardHealthEvent(_message.Message):
    __slots__ = ('dashboard_id', 'status', 'error_message', 'streamlit_url', 'embed_url', 'refreshed_at', 'code', 'data_sources', 'dashboard_status', 'published_code', 'published_at', 'schedule_enabled', 'cron_string', 'spawn_phase', 'warnings')
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STREAMLIT_URL_FIELD_NUMBER: _ClassVar[int]
    EMBED_URL_FIELD_NUMBER: _ClassVar[int]
    REFRESHED_AT_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCES_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_STATUS_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_CODE_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CRON_STRING_FIELD_NUMBER: _ClassVar[int]
    SPAWN_PHASE_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    status: CheckDashboardHealthResponse.HealthStatus
    error_message: str
    streamlit_url: str
    embed_url: str
    refreshed_at: _timestamp_pb2.Timestamp
    code: str
    data_sources: _containers.RepeatedCompositeFieldContainer[DataSource]
    dashboard_status: DashboardStatus
    published_code: str
    published_at: _timestamp_pb2.Timestamp
    schedule_enabled: bool
    cron_string: str
    spawn_phase: str
    warnings: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, dashboard_id: _Optional[str]=..., status: _Optional[_Union[CheckDashboardHealthResponse.HealthStatus, str]]=..., error_message: _Optional[str]=..., streamlit_url: _Optional[str]=..., embed_url: _Optional[str]=..., refreshed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., code: _Optional[str]=..., data_sources: _Optional[_Iterable[_Union[DataSource, _Mapping]]]=..., dashboard_status: _Optional[_Union[DashboardStatus, str]]=..., published_code: _Optional[str]=..., published_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., schedule_enabled: bool=..., cron_string: _Optional[str]=..., spawn_phase: _Optional[str]=..., warnings: _Optional[_Iterable[str]]=...) -> None:
        ...

class DashboardVersion(_message.Message):
    __slots__ = ('id', 'dashboard_id', 'version_number', 'code', 'data_sources', 'name', 'description', 'type', 'published_by', 'label', 'published_at', 'publisher')
    ID_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_BY_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    id: str
    dashboard_id: str
    version_number: int
    code: str
    data_sources: _containers.RepeatedCompositeFieldContainer[DataSource]
    name: str
    description: str
    type: DashboardType
    published_by: str
    label: str
    published_at: _timestamp_pb2.Timestamp
    publisher: DashboardCreator

    def __init__(self, id: _Optional[str]=..., dashboard_id: _Optional[str]=..., version_number: _Optional[int]=..., code: _Optional[str]=..., data_sources: _Optional[_Iterable[_Union[DataSource, _Mapping]]]=..., name: _Optional[str]=..., description: _Optional[str]=..., type: _Optional[_Union[DashboardType, str]]=..., published_by: _Optional[str]=..., label: _Optional[str]=..., published_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., publisher: _Optional[_Union[DashboardCreator, _Mapping]]=...) -> None:
        ...

class ListDashboardVersionsRequest(_message.Message):
    __slots__ = ('dashboard_id', 'limit', 'offset')
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    limit: int
    offset: int

    def __init__(self, dashboard_id: _Optional[str]=..., limit: _Optional[int]=..., offset: _Optional[int]=...) -> None:
        ...

class ListDashboardVersionsResponse(_message.Message):
    __slots__ = ('versions', 'total_count')
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    versions: _containers.RepeatedCompositeFieldContainer[DashboardVersion]
    total_count: int

    def __init__(self, versions: _Optional[_Iterable[_Union[DashboardVersion, _Mapping]]]=..., total_count: _Optional[int]=...) -> None:
        ...

class GetDashboardVersionRequest(_message.Message):
    __slots__ = ('dashboard_id', 'version_number')
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    version_number: int

    def __init__(self, dashboard_id: _Optional[str]=..., version_number: _Optional[int]=...) -> None:
        ...

class GetDashboardVersionResponse(_message.Message):
    __slots__ = ('version',)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: DashboardVersion

    def __init__(self, version: _Optional[_Union[DashboardVersion, _Mapping]]=...) -> None:
        ...

class RestoreDashboardVersionRequest(_message.Message):
    __slots__ = ('dashboard_id', 'version_number')
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    version_number: int

    def __init__(self, dashboard_id: _Optional[str]=..., version_number: _Optional[int]=...) -> None:
        ...

class RestoreDashboardVersionResponse(_message.Message):
    __slots__ = ('dashboard',)
    DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    dashboard: Dashboard

    def __init__(self, dashboard: _Optional[_Union[Dashboard, _Mapping]]=...) -> None:
        ...

class GetDashboardViewStatsRequest(_message.Message):
    __slots__ = ('dashboard_id',)
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str

    def __init__(self, dashboard_id: _Optional[str]=...) -> None:
        ...

class DashboardViewerInfo(_message.Message):
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

class GetDashboardViewStatsResponse(_message.Message):
    __slots__ = ('total_views', 'unique_viewers', 'recent_viewers')
    TOTAL_VIEWS_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_VIEWERS_FIELD_NUMBER: _ClassVar[int]
    RECENT_VIEWERS_FIELD_NUMBER: _ClassVar[int]
    total_views: int
    unique_viewers: int
    recent_viewers: _containers.RepeatedCompositeFieldContainer[DashboardViewerInfo]

    def __init__(self, total_views: _Optional[int]=..., unique_viewers: _Optional[int]=..., recent_viewers: _Optional[_Iterable[_Union[DashboardViewerInfo, _Mapping]]]=...) -> None:
        ...

class PreviewConfigDashboardRequest(_message.Message):
    __slots__ = ('patch_ref', 'dashboard_path')
    PATCH_REF_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_PATH_FIELD_NUMBER: _ClassVar[int]
    patch_ref: str
    dashboard_path: str

    def __init__(self, patch_ref: _Optional[str]=..., dashboard_path: _Optional[str]=...) -> None:
        ...

class PreviewConfigDashboardResponse(_message.Message):
    __slots__ = ('url', 'embed_url')
    URL_FIELD_NUMBER: _ClassVar[int]
    EMBED_URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    embed_url: str

    def __init__(self, url: _Optional[str]=..., embed_url: _Optional[str]=...) -> None:
        ...