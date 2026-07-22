"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/sandbox_capability.proto')
_sym_db = _symbol_database.Default()
from ..public import sandbox_query_pb2 as public_dot_sandbox__query__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fpublic/sandbox_capability.proto\x12$textql.rpc.public.sandbox_capability\x1a\x1apublic/sandbox_query.proto"\xe0\x01\n\x1aSandboxExecuteWriteRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12!\n\x0cconnector_id\x18\x02 \x01(\x05R\x0bconnectorId\x12\x1c\n\tstatement\x18\x03 \x01(\tR\tstatement\x12R\n\nparameters\x18\x04 \x03(\x0b22.textql.rpc.public.sandbox_query.SandboxQueryParamR\nparameters\x12\x19\n\x08max_rows\x18\x05 \x01(\x03R\x07maxRows"\xb3\x01\n\x1bSandboxExecuteWriteResponse\x12\x1d\n\narrow_data\x18\x01 \x01(\x0cR\tarrowData\x12\x1d\n\ntotal_rows\x18\x02 \x01(\x03R\ttotalRows\x12\x14\n\x05error\x18\x03 \x01(\tR\x05error\x12,\n\x0frefreshed_token\x18\x04 \x01(\tH\x00R\x0erefreshedToken\x88\x01\x01B\x12\n\x10_refreshed_token"e\n\x15SandboxStateOpRequest\x12\x0e\n\x02op\x18\x01 \x01(\tR\x02op\x12\x14\n\x05scope\x18\x02 \x01(\tR\x05scope\x12\x10\n\x03key\x18\x03 \x01(\tR\x03key\x12\x14\n\x05value\x18\x04 \x01(\tR\x05value"\xb0\x01\n\x16SandboxStateOpResponse\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value\x12\x14\n\x05found\x18\x02 \x01(\x08R\x05found\x12\x12\n\x04keys\x18\x03 \x03(\tR\x04keys\x12\x14\n\x05error\x18\x04 \x01(\tR\x05error\x12,\n\x0frefreshed_token\x18\x05 \x01(\tH\x00R\x0erefreshedToken\x88\x01\x01B\x12\n\x10_refreshed_token"l\n\x16SandboxPutAssetRequest\x12\x1b\n\tfile_name\x18\x01 \x01(\tR\x08fileName\x12!\n\x0ccontent_type\x18\x02 \x01(\tR\x0bcontentType\x12\x12\n\x04data\x18\x03 \x01(\x0cR\x04data"\x83\x01\n\x17SandboxPutAssetResponse\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12\x14\n\x05error\x18\x02 \x01(\tR\x05error\x12,\n\x0frefreshed_token\x18\x03 \x01(\tH\x00R\x0erefreshedToken\x88\x01\x01B\x12\n\x10_refreshed_token"\xb0\x01\n\x18SandboxSendNotifyRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07subject\x18\x02 \x01(\tR\x07subject\x12\x12\n\x04body\x18\x03 \x01(\tR\x04body\x12R\n\nparameters\x18\x04 \x03(\x0b22.textql.rpc.public.sandbox_query.SandboxQueryParamR\nparameters"\x87\x01\n\x19SandboxSendNotifyResponse\x12\x12\n\x04sent\x18\x01 \x01(\x08R\x04sent\x12\x14\n\x05error\x18\x02 \x01(\tR\x05error\x12,\n\x0frefreshed_token\x18\x03 \x01(\tH\x00R\x0erefreshedToken\x88\x01\x01B\x12\n\x10_refreshed_token2\xd9\x04\n\x18SandboxCapabilityService\x12\x95\x01\n\x0cExecuteWrite\x12@.textql.rpc.public.sandbox_capability.SandboxExecuteWriteRequest\x1aA.textql.rpc.public.sandbox_capability.SandboxExecuteWriteResponse"\x00\x12\x86\x01\n\x07StateOp\x12;.textql.rpc.public.sandbox_capability.SandboxStateOpRequest\x1a<.textql.rpc.public.sandbox_capability.SandboxStateOpResponse"\x00\x12\x89\x01\n\x08PutAsset\x12<.textql.rpc.public.sandbox_capability.SandboxPutAssetRequest\x1a=.textql.rpc.public.sandbox_capability.SandboxPutAssetResponse"\x00\x12\x8f\x01\n\nSendNotify\x12>.textql.rpc.public.sandbox_capability.SandboxSendNotifyRequest\x1a?.textql.rpc.public.sandbox_capability.SandboxSendNotifyResponse"\x00B;Z9github.com/textqllabs/demo2/compute/pkg/rpc/server/publicb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.sandbox_capability_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z9github.com/textqllabs/demo2/compute/pkg/rpc/server/public'
    _globals['_SANDBOXEXECUTEWRITEREQUEST']._serialized_start = 102
    _globals['_SANDBOXEXECUTEWRITEREQUEST']._serialized_end = 326
    _globals['_SANDBOXEXECUTEWRITERESPONSE']._serialized_start = 329
    _globals['_SANDBOXEXECUTEWRITERESPONSE']._serialized_end = 508
    _globals['_SANDBOXSTATEOPREQUEST']._serialized_start = 510
    _globals['_SANDBOXSTATEOPREQUEST']._serialized_end = 611
    _globals['_SANDBOXSTATEOPRESPONSE']._serialized_start = 614
    _globals['_SANDBOXSTATEOPRESPONSE']._serialized_end = 790
    _globals['_SANDBOXPUTASSETREQUEST']._serialized_start = 792
    _globals['_SANDBOXPUTASSETREQUEST']._serialized_end = 900
    _globals['_SANDBOXPUTASSETRESPONSE']._serialized_start = 903
    _globals['_SANDBOXPUTASSETRESPONSE']._serialized_end = 1034
    _globals['_SANDBOXSENDNOTIFYREQUEST']._serialized_start = 1037
    _globals['_SANDBOXSENDNOTIFYREQUEST']._serialized_end = 1213
    _globals['_SANDBOXSENDNOTIFYRESPONSE']._serialized_start = 1216
    _globals['_SANDBOXSENDNOTIFYRESPONSE']._serialized_end = 1351
    _globals['_SANDBOXCAPABILITYSERVICE']._serialized_start = 1354
    _globals['_SANDBOXCAPABILITYSERVICE']._serialized_end = 1955