from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class PowerBISelection(_message.Message):
    __slots__ = ('workspace_id', 'report_ids', 'dataset_ids', 'workspace_name', 'connector_id')
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    REPORT_IDS_FIELD_NUMBER: _ClassVar[int]
    DATASET_IDS_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    report_ids: _containers.RepeatedScalarFieldContainer[str]
    dataset_ids: _containers.RepeatedScalarFieldContainer[str]
    workspace_name: str
    connector_id: int

    def __init__(self, workspace_id: _Optional[str]=..., report_ids: _Optional[_Iterable[str]]=..., dataset_ids: _Optional[_Iterable[str]]=..., workspace_name: _Optional[str]=..., connector_id: _Optional[int]=...) -> None:
        ...