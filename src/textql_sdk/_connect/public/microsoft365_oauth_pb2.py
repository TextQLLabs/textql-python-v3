# pylint: skip-file
# mypy: ignore-errors
# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/microsoft365_oauth.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ..public import options_pb2 as public_dot_options__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fpublic/microsoft365_oauth.proto\x12$textql.rpc.public.microsoft365_oauth\x1a\x1cgoogle/protobuf/struct.proto\x1a\x14public/options.proto"\xb6\x01\n\x1fExchangeMicrosoft365CodeRequest\x12\x18\n\x04code\x18\x01 \x01(\tB\x04\x88\xb5\x18\x01R\x04code\x12\x14\n\x05state\x18\x02 \x01(\tR\x05state\x12\x1b\n\ttenant_id\x18\x03 \x01(\tR\x08tenantId\x12\x1b\n\tclient_id\x18\x04 \x01(\tR\x08clientId\x12)\n\rclient_secret\x18\x05 \x01(\tB\x04\x88\xb5\x18\x01R\x0cclientSecret"\xbd\x02\n ExchangeMicrosoft365CodeResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\'\n\x0caccess_token\x18\x02 \x01(\tB\x04\x88\xb5\x18\x01R\x0baccessToken\x12)\n\rrefresh_token\x18\x03 \x01(\tB\x04\x88\xb5\x18\x01R\x0crefreshToken\x12\x1d\n\nexpires_in\x18\x04 \x01(\x03R\texpiresIn\x12\x14\n\x05scope\x18\x05 \x01(\tR\x05scope\x12\x1d\n\ntoken_type\x18\x06 \x01(\tR\ttokenType\x12!\n\x0ctoken_expiry\x18\x07 \x01(\tR\x0btokenExpiry\x124\n\tuser_info\x18\x08 \x01(\x0b2\x17.google.protobuf.StructR\x08userInfo2\xc6\x01\n\x18Microsoft365OAuthService\x12\xa9\x01\n\x18ExchangeMicrosoft365Code\x12E.textql.rpc.public.microsoft365_oauth.ExchangeMicrosoft365CodeRequest\x1aF.textql.rpc.public.microsoft365_oauth.ExchangeMicrosoft365CodeResponseBGZ9github.com/textqllabs/demo2/compute/pkg/rpc/server/public\x92\xb5\x18\x08INTERNALb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.microsoft365_oauth_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z9github.com/textqllabs/demo2/compute/pkg/rpc/server/public\x92\xb5\x18\x08INTERNAL'
    _globals['_EXCHANGEMICROSOFT365CODEREQUEST'].fields_by_name['code']._loaded_options = None
    _globals['_EXCHANGEMICROSOFT365CODEREQUEST'].fields_by_name['code']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_EXCHANGEMICROSOFT365CODEREQUEST'].fields_by_name['client_secret']._loaded_options = None
    _globals['_EXCHANGEMICROSOFT365CODEREQUEST'].fields_by_name['client_secret']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_EXCHANGEMICROSOFT365CODERESPONSE'].fields_by_name['access_token']._loaded_options = None
    _globals['_EXCHANGEMICROSOFT365CODERESPONSE'].fields_by_name['access_token']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_EXCHANGEMICROSOFT365CODERESPONSE'].fields_by_name['refresh_token']._loaded_options = None
    _globals['_EXCHANGEMICROSOFT365CODERESPONSE'].fields_by_name['refresh_token']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_EXCHANGEMICROSOFT365CODEREQUEST']._serialized_start = 126
    _globals['_EXCHANGEMICROSOFT365CODEREQUEST']._serialized_end = 308
    _globals['_EXCHANGEMICROSOFT365CODERESPONSE']._serialized_start = 311
    _globals['_EXCHANGEMICROSOFT365CODERESPONSE']._serialized_end = 628
    _globals['_MICROSOFT365OAUTHSERVICE']._serialized_start = 631
    _globals['_MICROSOFT365OAUTHSERVICE']._serialized_end = 829