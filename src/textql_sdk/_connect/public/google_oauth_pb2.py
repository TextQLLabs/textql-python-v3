# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
# pylint: skip-file
# mypy: ignore-errors
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/google_oauth.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ..public import options_pb2 as public_dot_options__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19public/google_oauth.proto\x12\x1etextql.rpc.public.google_oauth\x1a\x1cgoogle/protobuf/struct.proto\x1a\x14public/options.proto" \n\x1eInitiateGoogleOAuthFlowRequest"R\n\x1fInitiateGoogleOAuthFlowResponse\x12\x19\n\x08auth_url\x18\x01 \x01(\tR\x07authUrl\x12\x14\n\x05state\x18\x02 \x01(\tR\x05state"E\n\x19ExchangeGoogleCodeRequest\x12\x12\n\x04code\x18\x01 \x01(\tR\x04code\x12\x14\n\x05state\x18\x02 \x01(\tR\x05state"\xb7\x02\n\x1aExchangeGoogleCodeResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\'\n\x0caccess_token\x18\x02 \x01(\tB\x04\x88\xb5\x18\x01R\x0baccessToken\x12)\n\rrefresh_token\x18\x03 \x01(\tB\x04\x88\xb5\x18\x01R\x0crefreshToken\x12\x1d\n\nexpires_in\x18\x04 \x01(\x03R\texpiresIn\x12\x14\n\x05scope\x18\x05 \x01(\tR\x05scope\x12\x1d\n\ntoken_type\x18\x06 \x01(\tR\ttokenType\x124\n\tuser_info\x18\x07 \x01(\x0b2\x17.google.protobuf.StructR\x08userInfo\x12!\n\x0ctoken_expiry\x18\x08 \x01(\tR\x0btokenExpiry2\xbf\x02\n\x12GoogleOAuthService\x12\x9a\x01\n\x17InitiateGoogleOAuthFlow\x12>.textql.rpc.public.google_oauth.InitiateGoogleOAuthFlowRequest\x1a?.textql.rpc.public.google_oauth.InitiateGoogleOAuthFlowResponse\x12\x8b\x01\n\x12ExchangeGoogleCode\x129.textql.rpc.public.google_oauth.ExchangeGoogleCodeRequest\x1a:.textql.rpc.public.google_oauth.ExchangeGoogleCodeResponseBGZ9github.com/textqllabs/demo2/compute/pkg/rpc/server/public\x92\xb5\x18\x08INTERNALb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.google_oauth_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z9github.com/textqllabs/demo2/compute/pkg/rpc/server/public\x92\xb5\x18\x08INTERNAL'
    _globals['_EXCHANGEGOOGLECODERESPONSE'].fields_by_name['access_token']._loaded_options = None
    _globals['_EXCHANGEGOOGLECODERESPONSE'].fields_by_name['access_token']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_EXCHANGEGOOGLECODERESPONSE'].fields_by_name['refresh_token']._loaded_options = None
    _globals['_EXCHANGEGOOGLECODERESPONSE'].fields_by_name['refresh_token']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_INITIATEGOOGLEOAUTHFLOWREQUEST']._serialized_start = 113
    _globals['_INITIATEGOOGLEOAUTHFLOWREQUEST']._serialized_end = 145
    _globals['_INITIATEGOOGLEOAUTHFLOWRESPONSE']._serialized_start = 147
    _globals['_INITIATEGOOGLEOAUTHFLOWRESPONSE']._serialized_end = 229
    _globals['_EXCHANGEGOOGLECODEREQUEST']._serialized_start = 231
    _globals['_EXCHANGEGOOGLECODEREQUEST']._serialized_end = 300
    _globals['_EXCHANGEGOOGLECODERESPONSE']._serialized_start = 303
    _globals['_EXCHANGEGOOGLECODERESPONSE']._serialized_end = 614
    _globals['_GOOGLEOAUTHSERVICE']._serialized_start = 617
    _globals['_GOOGLEOAUTHSERVICE']._serialized_end = 936