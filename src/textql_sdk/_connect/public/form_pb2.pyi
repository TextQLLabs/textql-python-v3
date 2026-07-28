# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
# pylint: skip-file
# mypy: ignore-errors
from google.protobuf import struct_pb2 as _struct_pb2
from ..public import options_pb2 as _options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ValidationIssue(_message.Message):
    __slots__ = ('field', 'message')
    FIELD_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    field: str
    message: str

    def __init__(self, field: _Optional[str]=..., message: _Optional[str]=...) -> None:
        ...

class FormTestResult(_message.Message):
    __slots__ = ('status', 'message', 'details')
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    status: str
    message: str
    details: _struct_pb2.Struct

    def __init__(self, status: _Optional[str]=..., message: _Optional[str]=..., details: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...

class Form(_message.Message):
    __slots__ = ('id', 'chat_id', 'form_type', 'data', 'status', 'submit_result', 'test_status', 'test_result', 'test_stale', 'issues', 'revision_ref', 'name')
    ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    FORM_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_RESULT_FIELD_NUMBER: _ClassVar[int]
    TEST_STATUS_FIELD_NUMBER: _ClassVar[int]
    TEST_RESULT_FIELD_NUMBER: _ClassVar[int]
    TEST_STALE_FIELD_NUMBER: _ClassVar[int]
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    REVISION_REF_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    chat_id: str
    form_type: str
    data: _struct_pb2.Struct
    status: str
    submit_result: _struct_pb2.Struct
    test_status: str
    test_result: FormTestResult
    test_stale: bool
    issues: _containers.RepeatedCompositeFieldContainer[ValidationIssue]
    revision_ref: str
    name: str

    def __init__(self, id: _Optional[str]=..., chat_id: _Optional[str]=..., form_type: _Optional[str]=..., data: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., status: _Optional[str]=..., submit_result: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., test_status: _Optional[str]=..., test_result: _Optional[_Union[FormTestResult, _Mapping]]=..., test_stale: bool=..., issues: _Optional[_Iterable[_Union[ValidationIssue, _Mapping]]]=..., revision_ref: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class GetFormRequest(_message.Message):
    __slots__ = ('form_id',)
    FORM_ID_FIELD_NUMBER: _ClassVar[int]
    form_id: str

    def __init__(self, form_id: _Optional[str]=...) -> None:
        ...

class GetFormResponse(_message.Message):
    __slots__ = ('form',)
    FORM_FIELD_NUMBER: _ClassVar[int]
    form: Form

    def __init__(self, form: _Optional[_Union[Form, _Mapping]]=...) -> None:
        ...

class ListFormsRequest(_message.Message):
    __slots__ = ('chat_id',)
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str

    def __init__(self, chat_id: _Optional[str]=...) -> None:
        ...

class ListFormsResponse(_message.Message):
    __slots__ = ('forms',)
    FORMS_FIELD_NUMBER: _ClassVar[int]
    forms: _containers.RepeatedCompositeFieldContainer[Form]

    def __init__(self, forms: _Optional[_Iterable[_Union[Form, _Mapping]]]=...) -> None:
        ...

class PrepareFormEditRequest(_message.Message):
    __slots__ = ('form_id',)
    FORM_ID_FIELD_NUMBER: _ClassVar[int]
    form_id: str

    def __init__(self, form_id: _Optional[str]=...) -> None:
        ...

class PrepareFormEditResponse(_message.Message):
    __slots__ = ('form',)
    FORM_FIELD_NUMBER: _ClassVar[int]
    form: Form

    def __init__(self, form: _Optional[_Union[Form, _Mapping]]=...) -> None:
        ...

class ValidateFormRequest(_message.Message):
    __slots__ = ('form_id', 'data')
    FORM_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    form_id: str
    data: _struct_pb2.Struct

    def __init__(self, form_id: _Optional[str]=..., data: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...

class ValidateFormResponse(_message.Message):
    __slots__ = ('issues',)
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    issues: _containers.RepeatedCompositeFieldContainer[ValidationIssue]

    def __init__(self, issues: _Optional[_Iterable[_Union[ValidationIssue, _Mapping]]]=...) -> None:
        ...

class UpdateFormDataRequest(_message.Message):
    __slots__ = ('form_id', 'data')
    FORM_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    form_id: str
    data: _struct_pb2.Struct

    def __init__(self, form_id: _Optional[str]=..., data: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...

class UpdateFormDataResponse(_message.Message):
    __slots__ = ('form',)
    FORM_FIELD_NUMBER: _ClassVar[int]
    form: Form

    def __init__(self, form: _Optional[_Union[Form, _Mapping]]=...) -> None:
        ...

class TestFormRequest(_message.Message):
    __slots__ = ('form_id',)
    FORM_ID_FIELD_NUMBER: _ClassVar[int]
    form_id: str

    def __init__(self, form_id: _Optional[str]=...) -> None:
        ...

class TestFormResponse(_message.Message):
    __slots__ = ('test_status', 'test_result', 'running')
    TEST_STATUS_FIELD_NUMBER: _ClassVar[int]
    TEST_RESULT_FIELD_NUMBER: _ClassVar[int]
    RUNNING_FIELD_NUMBER: _ClassVar[int]
    test_status: str
    test_result: FormTestResult
    running: bool

    def __init__(self, test_status: _Optional[str]=..., test_result: _Optional[_Union[FormTestResult, _Mapping]]=..., running: bool=...) -> None:
        ...

class GetFormTestRequest(_message.Message):
    __slots__ = ('form_id',)
    FORM_ID_FIELD_NUMBER: _ClassVar[int]
    form_id: str

    def __init__(self, form_id: _Optional[str]=...) -> None:
        ...

class GetFormTestResponse(_message.Message):
    __slots__ = ('test_status', 'test_result', 'test_stale')
    TEST_STATUS_FIELD_NUMBER: _ClassVar[int]
    TEST_RESULT_FIELD_NUMBER: _ClassVar[int]
    TEST_STALE_FIELD_NUMBER: _ClassVar[int]
    test_status: str
    test_result: FormTestResult
    test_stale: bool

    def __init__(self, test_status: _Optional[str]=..., test_result: _Optional[_Union[FormTestResult, _Mapping]]=..., test_stale: bool=...) -> None:
        ...

class SubmitFormRequest(_message.Message):
    __slots__ = ('form_id',)
    FORM_ID_FIELD_NUMBER: _ClassVar[int]
    form_id: str

    def __init__(self, form_id: _Optional[str]=...) -> None:
        ...

class SubmitFormResponse(_message.Message):
    __slots__ = ('form',)
    FORM_FIELD_NUMBER: _ClassVar[int]
    form: Form

    def __init__(self, form: _Optional[_Union[Form, _Mapping]]=...) -> None:
        ...

class SetFormStatusRequest(_message.Message):
    __slots__ = ('form_id', 'status')
    FORM_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    form_id: str
    status: str

    def __init__(self, form_id: _Optional[str]=..., status: _Optional[str]=...) -> None:
        ...

class SetFormStatusResponse(_message.Message):
    __slots__ = ('form',)
    FORM_FIELD_NUMBER: _ClassVar[int]
    form: Form

    def __init__(self, form: _Optional[_Union[Form, _Mapping]]=...) -> None:
        ...

class BackupFormRevisionRequest(_message.Message):
    __slots__ = ('form_id', 'revision_ref')
    FORM_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_REF_FIELD_NUMBER: _ClassVar[int]
    form_id: str
    revision_ref: str

    def __init__(self, form_id: _Optional[str]=..., revision_ref: _Optional[str]=...) -> None:
        ...

class BackupFormRevisionResponse(_message.Message):
    __slots__ = ('form',)
    FORM_FIELD_NUMBER: _ClassVar[int]
    form: Form

    def __init__(self, form: _Optional[_Union[Form, _Mapping]]=...) -> None:
        ...