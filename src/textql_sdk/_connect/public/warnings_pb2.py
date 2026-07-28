# pylint: skip-file
# mypy: ignore-errors
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/warnings.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15public/warnings.proto\x12\x16textql.rpc.public.chat\x1a google/protobuf/descriptor.proto*\xaa\x01\n\x0fWarningCategory\x12 \n\x1cWARNING_CATEGORY_UNSPECIFIED\x10\x00\x12\x1a\n\x16WARNING_CATEGORY_CAUSE\x10\x01\x12\x1c\n\x18WARNING_CATEGORY_SYMPTOM\x10\x02\x12\x1c\n\x18WARNING_CATEGORY_OUTCOME\x10\x03\x12\x1d\n\x19WARNING_CATEGORY_STRENGTH\x10\x04*\xf5\x05\n\x11ThreadWarningType\x12#\n\x1fTHREAD_WARNING_TYPE_UNSPECIFIED\x10\x00\x12-\n#THREAD_WARNING_TYPE_MISSING_CONTEXT\x10\x01\x1a\x04\x90\xb5\x18\x01\x12(\n\x1eTHREAD_WARNING_TYPE_ERROR_LOOP\x10\x02\x1a\x04\x90\xb5\x18\x02\x122\n(THREAD_WARNING_TYPE_EXCESSIVE_TOOL_CALLS\x10\x03\x1a\x04\x90\xb5\x18\x02\x12(\n\x1eTHREAD_WARNING_TYPE_SLOW_QUERY\x10\x06\x1a\x04\x90\xb5\x18\x02\x12(\n\x1eTHREAD_WARNING_TYPE_NO_RESULTS\x10\x07\x1a\x04\x90\xb5\x18\x02\x12.\n$THREAD_WARNING_TYPE_USER_FRUSTRATION\x10\x08\x1a\x04\x90\xb5\x18\x03\x125\n+THREAD_WARNING_TYPE_POTENTIAL_HALLUCINATION\x10\t\x1a\x04\x90\xb5\x18\x03\x121\n\'THREAD_WARNING_TYPE_IGNORED_INSTRUCTION\x10\n\x1a\x04\x90\xb5\x18\x03\x12.\n$THREAD_WARNING_TYPE_USER_THUMBS_DOWN\x10\x0b\x1a\x04\x90\xb5\x18\x03\x12+\n!THREAD_WARNING_TYPE_NO_CONCLUSION\x10\x0c\x1a\x04\x90\xb5\x18\x03\x12,\n"THREAD_WARNING_TYPE_USER_THUMBS_UP\x10\r\x1a\x04\x90\xb5\x18\x04\x12+\n!THREAD_WARNING_TYPE_GOAL_ACHIEVED\x10\x0e\x1a\x04\x90\xb5\x18\x04\x12/\n%THREAD_WARNING_TYPE_USER_SATISFACTION\x10\x0f\x1a\x04\x90\xb5\x18\x04"\x04\x08\x05\x10\x05"\x04\x08\x04\x10\x04*$THREAD_WARNING_TYPE_CONNECTOR_ERRORS*%THREAD_WARNING_TYPE_LONG_CONVERSATION:w\n\x10warning_category\x12!.google.protobuf.EnumValueOptions\x18\xd2\x86\x03 \x01(\x0e2\'.textql.rpc.public.chat.WarningCategoryR\x0fwarningCategoryb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.warnings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_THREADWARNINGTYPE'].values_by_name['THREAD_WARNING_TYPE_MISSING_CONTEXT']._loaded_options = None
    _globals['_THREADWARNINGTYPE'].values_by_name['THREAD_WARNING_TYPE_MISSING_CONTEXT']._serialized_options = b'\x90\xb5\x18\x01'
    _globals['_THREADWARNINGTYPE'].values_by_name['THREAD_WARNING_TYPE_ERROR_LOOP']._loaded_options = None
    _globals['_THREADWARNINGTYPE'].values_by_name['THREAD_WARNING_TYPE_ERROR_LOOP']._serialized_options = b'\x90\xb5\x18\x02'
    _globals['_THREADWARNINGTYPE'].values_by_name['THREAD_WARNING_TYPE_EXCESSIVE_TOOL_CALLS']._loaded_options = None
    _globals['_THREADWARNINGTYPE'].values_by_name['THREAD_WARNING_TYPE_EXCESSIVE_TOOL_CALLS']._serialized_options = b'\x90\xb5\x18\x02'
    _globals['_THREADWARNINGTYPE'].values_by_name['THREAD_WARNING_TYPE_SLOW_QUERY']._loaded_options = None
    _globals['_THREADWARNINGTYPE'].values_by_name['THREAD_WARNING_TYPE_SLOW_QUERY']._serialized_options = b'\x90\xb5\x18\x02'
    _globals['_THREADWARNINGTYPE'].values_by_name['THREAD_WARNING_TYPE_NO_RESULTS']._loaded_options = None
    _globals['_THREADWARNINGTYPE'].values_by_name['THREAD_WARNING_TYPE_NO_RESULTS']._serialized_options = b'\x90\xb5\x18\x02'
    _globals['_THREADWARNINGTYPE'].values_by_name['THREAD_WARNING_TYPE_USER_FRUSTRATION']._loaded_options = None
    _globals['_THREADWARNINGTYPE'].values_by_name['THREAD_WARNING_TYPE_USER_FRUSTRATION']._serialized_options = b'\x90\xb5\x18\x03'
    _globals['_THREADWARNINGTYPE'].values_by_name['THREAD_WARNING_TYPE_POTENTIAL_HALLUCINATION']._loaded_options = None
    _globals['_THREADWARNINGTYPE'].values_by_name['THREAD_WARNING_TYPE_POTENTIAL_HALLUCINATION']._serialized_options = b'\x90\xb5\x18\x03'
    _globals['_THREADWARNINGTYPE'].values_by_name['THREAD_WARNING_TYPE_IGNORED_INSTRUCTION']._loaded_options = None
    _globals['_THREADWARNINGTYPE'].values_by_name['THREAD_WARNING_TYPE_IGNORED_INSTRUCTION']._serialized_options = b'\x90\xb5\x18\x03'
    _globals['_THREADWARNINGTYPE'].values_by_name['THREAD_WARNING_TYPE_USER_THUMBS_DOWN']._loaded_options = None
    _globals['_THREADWARNINGTYPE'].values_by_name['THREAD_WARNING_TYPE_USER_THUMBS_DOWN']._serialized_options = b'\x90\xb5\x18\x03'
    _globals['_THREADWARNINGTYPE'].values_by_name['THREAD_WARNING_TYPE_NO_CONCLUSION']._loaded_options = None
    _globals['_THREADWARNINGTYPE'].values_by_name['THREAD_WARNING_TYPE_NO_CONCLUSION']._serialized_options = b'\x90\xb5\x18\x03'
    _globals['_THREADWARNINGTYPE'].values_by_name['THREAD_WARNING_TYPE_USER_THUMBS_UP']._loaded_options = None
    _globals['_THREADWARNINGTYPE'].values_by_name['THREAD_WARNING_TYPE_USER_THUMBS_UP']._serialized_options = b'\x90\xb5\x18\x04'
    _globals['_THREADWARNINGTYPE'].values_by_name['THREAD_WARNING_TYPE_GOAL_ACHIEVED']._loaded_options = None
    _globals['_THREADWARNINGTYPE'].values_by_name['THREAD_WARNING_TYPE_GOAL_ACHIEVED']._serialized_options = b'\x90\xb5\x18\x04'
    _globals['_THREADWARNINGTYPE'].values_by_name['THREAD_WARNING_TYPE_USER_SATISFACTION']._loaded_options = None
    _globals['_THREADWARNINGTYPE'].values_by_name['THREAD_WARNING_TYPE_USER_SATISFACTION']._serialized_options = b'\x90\xb5\x18\x04'
    _globals['_WARNINGCATEGORY']._serialized_start = 84
    _globals['_WARNINGCATEGORY']._serialized_end = 254
    _globals['_THREADWARNINGTYPE']._serialized_start = 257
    _globals['_THREADWARNINGTYPE']._serialized_end = 1014