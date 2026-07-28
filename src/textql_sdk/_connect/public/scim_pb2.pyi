# pylint: skip-file
# mypy: ignore-errors
import datetime
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ScimToken(_message.Message):
    __slots__ = ('id', 'description', 'created_by', 'expires_at', 'revoked_at', 'created_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    REVOKED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    description: str
    created_by: str
    expires_at: _timestamp_pb2.Timestamp
    revoked_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., description: _Optional[str]=..., created_by: _Optional[str]=..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., revoked_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ScimOAuthClient(_message.Message):
    __slots__ = ('id', 'client_id', 'description', 'created_by', 'expires_at', 'revoked_at', 'created_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    REVOKED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    client_id: str
    description: str
    created_by: str
    expires_at: _timestamp_pb2.Timestamp
    revoked_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., client_id: _Optional[str]=..., description: _Optional[str]=..., created_by: _Optional[str]=..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., revoked_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CreateScimTokenRequest(_message.Message):
    __slots__ = ('description', 'expires_in_days')
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_DAYS_FIELD_NUMBER: _ClassVar[int]
    description: str
    expires_in_days: int

    def __init__(self, description: _Optional[str]=..., expires_in_days: _Optional[int]=...) -> None:
        ...

class CreateScimTokenResponse(_message.Message):
    __slots__ = ('id', 'token', 'description', 'expires_at', 'created_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    token: str
    description: str
    expires_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., token: _Optional[str]=..., description: _Optional[str]=..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListScimTokensRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListScimTokensResponse(_message.Message):
    __slots__ = ('tokens',)
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    tokens: _containers.RepeatedCompositeFieldContainer[ScimToken]

    def __init__(self, tokens: _Optional[_Iterable[_Union[ScimToken, _Mapping]]]=...) -> None:
        ...

class RevokeScimTokenRequest(_message.Message):
    __slots__ = ('id',)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str

    def __init__(self, id: _Optional[str]=...) -> None:
        ...

class RevokeScimTokenResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CreateScimOAuthClientRequest(_message.Message):
    __slots__ = ('description', 'expires_in_days')
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_DAYS_FIELD_NUMBER: _ClassVar[int]
    description: str
    expires_in_days: int

    def __init__(self, description: _Optional[str]=..., expires_in_days: _Optional[int]=...) -> None:
        ...

class CreateScimOAuthClientResponse(_message.Message):
    __slots__ = ('id', 'client_id', 'client_secret', 'description', 'expires_at', 'created_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    client_id: str
    client_secret: str
    description: str
    expires_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., client_id: _Optional[str]=..., client_secret: _Optional[str]=..., description: _Optional[str]=..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListScimOAuthClientsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListScimOAuthClientsResponse(_message.Message):
    __slots__ = ('clients',)
    CLIENTS_FIELD_NUMBER: _ClassVar[int]
    clients: _containers.RepeatedCompositeFieldContainer[ScimOAuthClient]

    def __init__(self, clients: _Optional[_Iterable[_Union[ScimOAuthClient, _Mapping]]]=...) -> None:
        ...

class RevokeScimOAuthClientRequest(_message.Message):
    __slots__ = ('id',)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str

    def __init__(self, id: _Optional[str]=...) -> None:
        ...

class RevokeScimOAuthClientResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...