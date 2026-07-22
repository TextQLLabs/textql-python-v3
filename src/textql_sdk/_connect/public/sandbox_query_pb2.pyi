from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SandboxExecuteQueryRequest(_message.Message):
    __slots__ = ('source_name', 'connector_id', 'parameters', 'max_rows', 'sql_query', 'library_tql', 'app_db')
    SOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    MAX_ROWS_FIELD_NUMBER: _ClassVar[int]
    SQL_QUERY_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_TQL_FIELD_NUMBER: _ClassVar[int]
    APP_DB_FIELD_NUMBER: _ClassVar[int]
    source_name: str
    connector_id: int
    parameters: _containers.RepeatedCompositeFieldContainer[SandboxQueryParam]
    max_rows: int
    sql_query: SqlQueryTemplate
    library_tql: LibraryTQLTemplate
    app_db: AppDBTemplate

    def __init__(self, source_name: _Optional[str]=..., connector_id: _Optional[int]=..., parameters: _Optional[_Iterable[_Union[SandboxQueryParam, _Mapping]]]=..., max_rows: _Optional[int]=..., sql_query: _Optional[_Union[SqlQueryTemplate, _Mapping]]=..., library_tql: _Optional[_Union[LibraryTQLTemplate, _Mapping]]=..., app_db: _Optional[_Union[AppDBTemplate, _Mapping]]=...) -> None:
        ...

class SqlQueryTemplate(_message.Message):
    __slots__ = ('query',)
    QUERY_FIELD_NUMBER: _ClassVar[int]
    query: str

    def __init__(self, query: _Optional[str]=...) -> None:
        ...

class LibraryTQLTemplate(_message.Message):
    __slots__ = ('tql_path',)
    TQL_PATH_FIELD_NUMBER: _ClassVar[int]
    tql_path: str

    def __init__(self, tql_path: _Optional[str]=...) -> None:
        ...

class AppDBTemplate(_message.Message):
    __slots__ = ('query',)
    QUERY_FIELD_NUMBER: _ClassVar[int]
    query: str

    def __init__(self, query: _Optional[str]=...) -> None:
        ...

class SandboxQueryParam(_message.Message):
    __slots__ = ('name', 'value')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str

    def __init__(self, name: _Optional[str]=..., value: _Optional[str]=...) -> None:
        ...

class SandboxExecuteQueryResponse(_message.Message):
    __slots__ = ('arrow_data', 'total_rows', 'error', 'refreshed_token')
    ARROW_DATA_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ROWS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REFRESHED_TOKEN_FIELD_NUMBER: _ClassVar[int]
    arrow_data: bytes
    total_rows: int
    error: str
    refreshed_token: str

    def __init__(self, arrow_data: _Optional[bytes]=..., total_rows: _Optional[int]=..., error: _Optional[str]=..., refreshed_token: _Optional[str]=...) -> None:
        ...