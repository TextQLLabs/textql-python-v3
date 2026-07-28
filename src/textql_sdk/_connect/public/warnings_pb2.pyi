# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
# pylint: skip-file
# mypy: ignore-errors
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class WarningCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WARNING_CATEGORY_UNSPECIFIED: _ClassVar[WarningCategory]
    WARNING_CATEGORY_CAUSE: _ClassVar[WarningCategory]
    WARNING_CATEGORY_SYMPTOM: _ClassVar[WarningCategory]
    WARNING_CATEGORY_OUTCOME: _ClassVar[WarningCategory]
    WARNING_CATEGORY_STRENGTH: _ClassVar[WarningCategory]

class ThreadWarningType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    THREAD_WARNING_TYPE_UNSPECIFIED: _ClassVar[ThreadWarningType]
    THREAD_WARNING_TYPE_MISSING_CONTEXT: _ClassVar[ThreadWarningType]
    THREAD_WARNING_TYPE_ERROR_LOOP: _ClassVar[ThreadWarningType]
    THREAD_WARNING_TYPE_EXCESSIVE_TOOL_CALLS: _ClassVar[ThreadWarningType]
    THREAD_WARNING_TYPE_SLOW_QUERY: _ClassVar[ThreadWarningType]
    THREAD_WARNING_TYPE_NO_RESULTS: _ClassVar[ThreadWarningType]
    THREAD_WARNING_TYPE_USER_FRUSTRATION: _ClassVar[ThreadWarningType]
    THREAD_WARNING_TYPE_POTENTIAL_HALLUCINATION: _ClassVar[ThreadWarningType]
    THREAD_WARNING_TYPE_IGNORED_INSTRUCTION: _ClassVar[ThreadWarningType]
    THREAD_WARNING_TYPE_USER_THUMBS_DOWN: _ClassVar[ThreadWarningType]
    THREAD_WARNING_TYPE_NO_CONCLUSION: _ClassVar[ThreadWarningType]
    THREAD_WARNING_TYPE_USER_THUMBS_UP: _ClassVar[ThreadWarningType]
    THREAD_WARNING_TYPE_GOAL_ACHIEVED: _ClassVar[ThreadWarningType]
    THREAD_WARNING_TYPE_USER_SATISFACTION: _ClassVar[ThreadWarningType]
WARNING_CATEGORY_UNSPECIFIED: WarningCategory
WARNING_CATEGORY_CAUSE: WarningCategory
WARNING_CATEGORY_SYMPTOM: WarningCategory
WARNING_CATEGORY_OUTCOME: WarningCategory
WARNING_CATEGORY_STRENGTH: WarningCategory
THREAD_WARNING_TYPE_UNSPECIFIED: ThreadWarningType
THREAD_WARNING_TYPE_MISSING_CONTEXT: ThreadWarningType
THREAD_WARNING_TYPE_ERROR_LOOP: ThreadWarningType
THREAD_WARNING_TYPE_EXCESSIVE_TOOL_CALLS: ThreadWarningType
THREAD_WARNING_TYPE_SLOW_QUERY: ThreadWarningType
THREAD_WARNING_TYPE_NO_RESULTS: ThreadWarningType
THREAD_WARNING_TYPE_USER_FRUSTRATION: ThreadWarningType
THREAD_WARNING_TYPE_POTENTIAL_HALLUCINATION: ThreadWarningType
THREAD_WARNING_TYPE_IGNORED_INSTRUCTION: ThreadWarningType
THREAD_WARNING_TYPE_USER_THUMBS_DOWN: ThreadWarningType
THREAD_WARNING_TYPE_NO_CONCLUSION: ThreadWarningType
THREAD_WARNING_TYPE_USER_THUMBS_UP: ThreadWarningType
THREAD_WARNING_TYPE_GOAL_ACHIEVED: ThreadWarningType
THREAD_WARNING_TYPE_USER_SATISFACTION: ThreadWarningType
WARNING_CATEGORY_FIELD_NUMBER: _ClassVar[int]
warning_category: _descriptor.FieldDescriptor