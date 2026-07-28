# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
# pylint: skip-file
# mypy: ignore-errors
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/google_drive_oauth.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ..public import options_pb2 as public_dot_options__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fpublic/google_drive_oauth.proto\x12$textql.rpc.public.google_drive_oauth\x1a\x1cgoogle/protobuf/struct.proto\x1a\x14public/options.proto"J\n\x1eExchangeGoogleDriveCodeRequest\x12\x12\n\x04code\x18\x01 \x01(\tR\x04code\x12\x14\n\x05state\x18\x02 \x01(\tR\x05state"\x99\x02\n\x1fExchangeGoogleDriveCodeResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\'\n\x0caccess_token\x18\x02 \x01(\tB\x04\x88\xb5\x18\x01R\x0baccessToken\x12)\n\rrefresh_token\x18\x03 \x01(\tB\x04\x88\xb5\x18\x01R\x0crefreshToken\x12\x1d\n\nexpires_in\x18\x04 \x01(\x03R\texpiresIn\x12\x14\n\x05scope\x18\x05 \x01(\tR\x05scope\x12\x1d\n\ntoken_type\x18\x06 \x01(\tR\ttokenType\x124\n\tuser_info\x18\x07 \x01(\x0b2\x17.google.protobuf.StructR\x08userInfo2\xc2\x01\n\x17GoogleDriveOAuthService\x12\xa6\x01\n\x17ExchangeGoogleDriveCode\x12D.textql.rpc.public.google_drive_oauth.ExchangeGoogleDriveCodeRequest\x1aE.textql.rpc.public.google_drive_oauth.ExchangeGoogleDriveCodeResponseBGZ9github.com/textqllabs/demo2/compute/pkg/rpc/server/public\x92\xb5\x18\x08INTERNALb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.google_drive_oauth_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z9github.com/textqllabs/demo2/compute/pkg/rpc/server/public\x92\xb5\x18\x08INTERNAL'
    _globals['_EXCHANGEGOOGLEDRIVECODERESPONSE'].fields_by_name['access_token']._loaded_options = None
    _globals['_EXCHANGEGOOGLEDRIVECODERESPONSE'].fields_by_name['access_token']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_EXCHANGEGOOGLEDRIVECODERESPONSE'].fields_by_name['refresh_token']._loaded_options = None
    _globals['_EXCHANGEGOOGLEDRIVECODERESPONSE'].fields_by_name['refresh_token']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_EXCHANGEGOOGLEDRIVECODEREQUEST']._serialized_start = 125
    _globals['_EXCHANGEGOOGLEDRIVECODEREQUEST']._serialized_end = 199
    _globals['_EXCHANGEGOOGLEDRIVECODERESPONSE']._serialized_start = 202
    _globals['_EXCHANGEGOOGLEDRIVECODERESPONSE']._serialized_end = 483
    _globals['_GOOGLEDRIVEOAUTHSERVICE']._serialized_start = 486
    _globals['_GOOGLEDRIVEOAUTHSERVICE']._serialized_end = 680