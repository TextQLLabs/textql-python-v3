# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
# pylint: skip-file
# mypy: ignore-errors
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'powerbi_selection.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17powerbi_selection.proto\x12\x1ctextql.rpc.powerbi_selection"\xbf\x01\n\x10PowerBISelection\x12!\n\x0cworkspace_id\x18\x01 \x01(\tR\x0bworkspaceId\x12\x1d\n\nreport_ids\x18\x02 \x03(\tR\treportIds\x12\x1f\n\x0bdataset_ids\x18\x03 \x03(\tR\ndatasetIds\x12%\n\x0eworkspace_name\x18\x04 \x01(\tR\rworkspaceName\x12!\n\x0cconnector_id\x18\x05 \x01(\x05R\x0bconnectorIdb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'powerbi_selection_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_POWERBISELECTION']._serialized_start = 58
    _globals['_POWERBISELECTION']._serialized_end = 249