# pylint: skip-file
# mypy: ignore-errors
# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
from ..public import options_pb2 as _options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class SendEmailRequest(_message.Message):
    __slots__ = ('subject', 'body', 'to', 'report_id', 'owner_name', 'report_source')
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    REPORT_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_NAME_FIELD_NUMBER: _ClassVar[int]
    REPORT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    subject: str
    body: str
    to: str
    report_id: str
    owner_name: str
    report_source: str

    def __init__(self, subject: _Optional[str]=..., body: _Optional[str]=..., to: _Optional[str]=..., report_id: _Optional[str]=..., owner_name: _Optional[str]=..., report_source: _Optional[str]=...) -> None:
        ...

class SendEmailResponse(_message.Message):
    __slots__ = ('success', 'error')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: str

    def __init__(self, success: bool=..., error: _Optional[str]=...) -> None:
        ...

class UploadFeedbackScreenshotRequest(_message.Message):
    __slots__ = ('screenshot',)
    SCREENSHOT_FIELD_NUMBER: _ClassVar[int]
    screenshot: bytes

    def __init__(self, screenshot: _Optional[bytes]=...) -> None:
        ...

class UploadFeedbackScreenshotResponse(_message.Message):
    __slots__ = ('screenshot_url',)
    SCREENSHOT_URL_FIELD_NUMBER: _ClassVar[int]
    screenshot_url: str

    def __init__(self, screenshot_url: _Optional[str]=...) -> None:
        ...