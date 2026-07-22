"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/sandbox_query.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1apublic/sandbox_query.proto\x12\x1ftextql.rpc.public.sandbox_query"\xce\x03\n\x1aSandboxExecuteQueryRequest\x12\x1f\n\x0bsource_name\x18\x01 \x01(\tR\nsourceName\x12!\n\x0cconnector_id\x18\x02 \x01(\x05R\x0bconnectorId\x12R\n\nparameters\x18\x03 \x03(\x0b22.textql.rpc.public.sandbox_query.SandboxQueryParamR\nparameters\x12\x19\n\x08max_rows\x18\x04 \x01(\x03R\x07maxRows\x12P\n\tsql_query\x18\x05 \x01(\x0b21.textql.rpc.public.sandbox_query.SqlQueryTemplateH\x00R\x08sqlQuery\x12V\n\x0blibrary_tql\x18\x06 \x01(\x0b23.textql.rpc.public.sandbox_query.LibraryTQLTemplateH\x00R\nlibraryTql\x12G\n\x06app_db\x18\x07 \x01(\x0b2..textql.rpc.public.sandbox_query.AppDBTemplateH\x00R\x05appDbB\n\n\x08template"(\n\x10SqlQueryTemplate\x12\x14\n\x05query\x18\x01 \x01(\tR\x05query"/\n\x12LibraryTQLTemplate\x12\x19\n\x08tql_path\x18\x01 \x01(\tR\x07tqlPath"%\n\rAppDBTemplate\x12\x14\n\x05query\x18\x01 \x01(\tR\x05query"=\n\x11SandboxQueryParam\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value"\xb3\x01\n\x1bSandboxExecuteQueryResponse\x12\x1d\n\narrow_data\x18\x01 \x01(\x0cR\tarrowData\x12\x1d\n\ntotal_rows\x18\x02 \x01(\x03R\ttotalRows\x12\x14\n\x05error\x18\x03 \x01(\tR\x05error\x12,\n\x0frefreshed_token\x18\x04 \x01(\tH\x00R\x0erefreshedToken\x88\x01\x01B\x12\n\x10_refreshed_token2\xa3\x01\n\x13SandboxQueryService\x12\x8b\x01\n\x0cExecuteQuery\x12;.textql.rpc.public.sandbox_query.SandboxExecuteQueryRequest\x1a<.textql.rpc.public.sandbox_query.SandboxExecuteQueryResponse"\x00B;Z9github.com/textqllabs/demo2/compute/pkg/rpc/server/publicb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.sandbox_query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z9github.com/textqllabs/demo2/compute/pkg/rpc/server/public'
    _globals['_SANDBOXEXECUTEQUERYREQUEST']._serialized_start = 64
    _globals['_SANDBOXEXECUTEQUERYREQUEST']._serialized_end = 526
    _globals['_SQLQUERYTEMPLATE']._serialized_start = 528
    _globals['_SQLQUERYTEMPLATE']._serialized_end = 568
    _globals['_LIBRARYTQLTEMPLATE']._serialized_start = 570
    _globals['_LIBRARYTQLTEMPLATE']._serialized_end = 617
    _globals['_APPDBTEMPLATE']._serialized_start = 619
    _globals['_APPDBTEMPLATE']._serialized_end = 656
    _globals['_SANDBOXQUERYPARAM']._serialized_start = 658
    _globals['_SANDBOXQUERYPARAM']._serialized_end = 719
    _globals['_SANDBOXEXECUTEQUERYRESPONSE']._serialized_start = 722
    _globals['_SANDBOXEXECUTEQUERYRESPONSE']._serialized_end = 901
    _globals['_SANDBOXQUERYSERVICE']._serialized_start = 904
    _globals['_SANDBOXQUERYSERVICE']._serialized_end = 1067