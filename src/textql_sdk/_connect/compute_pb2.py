# pylint: skip-file
# mypy: ignore-errors
# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'compute.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rcompute.proto\x12\x12textql.rpc.compute\x1a\x1bgoogle/protobuf/empty.proto"!\n\x0bExecRequest\x12\x12\n\x04code\x18\x01 \x01(\tR\x04code"`\n\x0cExecResponse\x12\x16\n\x06output\x18\x01 \x03(\tR\x06output\x12\x14\n\x05error\x18\x02 \x01(\tR\x05error\x12"\n\x0cdataFrameIds\x18\x03 \x03(\x05R\x0cdataFrameIds"/\n\x15SandboxStatusResponse\x12\x16\n\x06status\x18\x01 \x01(\tR\x06status"\'\n\x0fQuerySQLRequest\x12\x14\n\x05query\x18\x01 \x01(\tR\x05query"@\n\x10QuerySQLResponse\x12\x16\n\x06result\x18\x01 \x01(\tR\x06result\x12\x14\n\x05error\x18\x02 \x01(\tR\x05error"!\n\x07DataRow\x12\x16\n\x06values\x18\x01 \x03(\tR\x06values"\x86\x01\n\x0fLoadDataRequest\x12 \n\x0bcolumnNames\x18\x01 \x03(\tR\x0bcolumnNames\x12 \n\x0bcolumnTypes\x18\x02 \x03(\tR\x0bcolumnTypes\x12/\n\x04rows\x18\x03 \x03(\x0b2\x1b.textql.rpc.compute.DataRowR\x04rows"\x9b\x01\n\x0fLoadFileRequest\x12$\n\rfileLocations\x18\x01 \x03(\tR\rfileLocations\x12\x1c\n\tfileTypes\x18\x02 \x03(\tR\tfileTypes\x12\x1c\n\thasHeader\x18\x03 \x03(\x08R\thasHeader\x12&\n\x0edataFrameNames\x18\x04 \x03(\tR\x0edataFrameNames"\x9c\x01\n\x10LoadDataResponse\x12\x1c\n\tdataframe\x18\x01 \x01(\tR\tdataframe\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x18\n\x07preview\x18\x03 \x01(\tR\x07preview\x12\x12\n\x04size\x18\x04 \x01(\x05R\x04size\x12\x14\n\x05error\x18\x05 \x01(\tR\x05error\x12\x12\n\x04head\x18\x06 \x01(\tR\x04head2\x86\x04\n\x0eComputeService\x12K\n\x04Exec\x12\x1f.textql.rpc.compute.ExecRequest\x1a .textql.rpc.compute.ExecResponse"\x00\x12W\n\x08LoadData\x12#.textql.rpc.compute.LoadDataRequest\x1a$.textql.rpc.compute.LoadDataResponse"\x00\x12X\n\tLoadFiles\x12#.textql.rpc.compute.LoadFileRequest\x1a$.textql.rpc.compute.LoadDataResponse"\x00\x12W\n\x10GetSandboxStatus\x12\x16.google.protobuf.Empty\x1a).textql.rpc.compute.SandboxStatusResponse"\x00\x12B\n\x0eRefreshSandbox\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty"\x00\x12W\n\x08QuerySQL\x12#.textql.rpc.compute.QuerySQLRequest\x1a$.textql.rpc.compute.QuerySQLResponse"\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'compute_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_EXECREQUEST']._serialized_start = 66
    _globals['_EXECREQUEST']._serialized_end = 99
    _globals['_EXECRESPONSE']._serialized_start = 101
    _globals['_EXECRESPONSE']._serialized_end = 197
    _globals['_SANDBOXSTATUSRESPONSE']._serialized_start = 199
    _globals['_SANDBOXSTATUSRESPONSE']._serialized_end = 246
    _globals['_QUERYSQLREQUEST']._serialized_start = 248
    _globals['_QUERYSQLREQUEST']._serialized_end = 287
    _globals['_QUERYSQLRESPONSE']._serialized_start = 289
    _globals['_QUERYSQLRESPONSE']._serialized_end = 353
    _globals['_DATAROW']._serialized_start = 355
    _globals['_DATAROW']._serialized_end = 388
    _globals['_LOADDATAREQUEST']._serialized_start = 391
    _globals['_LOADDATAREQUEST']._serialized_end = 525
    _globals['_LOADFILEREQUEST']._serialized_start = 528
    _globals['_LOADFILEREQUEST']._serialized_end = 683
    _globals['_LOADDATARESPONSE']._serialized_start = 686
    _globals['_LOADDATARESPONSE']._serialized_end = 842
    _globals['_COMPUTESERVICE']._serialized_start = 845
    _globals['_COMPUTESERVICE']._serialized_end = 1363