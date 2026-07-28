# pylint: skip-file
# mypy: ignore-errors
# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/snowflake_oauth.proto')
_sym_db = _symbol_database.Default()
from ..public import options_pb2 as public_dot_options__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cpublic/snowflake_oauth.proto\x12!textql.rpc.public.snowflake_oauth\x1a\x14public/options.proto"\x85\x01\n\x1bGetSnowflakeOAuthURLRequest\x12\x1f\n\x0baccount_url\x18\x01 \x01(\tR\naccountUrl\x12\x1b\n\tclient_id\x18\x02 \x01(\tR\x08clientId\x12\x14\n\x05state\x18\x03 \x01(\tR\x05state\x12\x12\n\x04role\x18\x04 \x01(\tR\x04role";\n\x1cGetSnowflakeOAuthURLResponse\x12\x1b\n\toauth_url\x18\x01 \x01(\tR\x08oauthUrl"\xb7\x01\n\x1cExchangeSnowflakeCodeRequest\x12\x18\n\x04code\x18\x01 \x01(\tB\x04\x88\xb5\x18\x01R\x04code\x12\x14\n\x05state\x18\x02 \x01(\tR\x05state\x12\x1f\n\x0baccount_url\x18\x03 \x01(\tR\naccountUrl\x12\x1b\n\tclient_id\x18\x04 \x01(\tR\x08clientId\x12)\n\rclient_secret\x18\x05 \x01(\tB\x04\x88\xb5\x18\x01R\x0cclientSecret"\xfd\x01\n\x1dExchangeSnowflakeCodeResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\'\n\x0caccess_token\x18\x02 \x01(\tB\x04\x88\xb5\x18\x01R\x0baccessToken\x12)\n\rrefresh_token\x18\x03 \x01(\tB\x04\x88\xb5\x18\x01R\x0crefreshToken\x12\x1d\n\nexpires_in\x18\x04 \x01(\x03R\texpiresIn\x12\x14\n\x05scope\x18\x05 \x01(\tR\x05scope\x12\x1d\n\ntoken_type\x18\x06 \x01(\tR\ttokenType\x12\x1a\n\x08username\x18\x07 \x01(\tR\x08username2\xce\x02\n\x15SnowflakeOAuthService\x12\x97\x01\n\x14GetSnowflakeOAuthURL\x12>.textql.rpc.public.snowflake_oauth.GetSnowflakeOAuthURLRequest\x1a?.textql.rpc.public.snowflake_oauth.GetSnowflakeOAuthURLResponse\x12\x9a\x01\n\x15ExchangeSnowflakeCode\x12?.textql.rpc.public.snowflake_oauth.ExchangeSnowflakeCodeRequest\x1a@.textql.rpc.public.snowflake_oauth.ExchangeSnowflakeCodeResponseBGZ9github.com/textqllabs/demo2/compute/pkg/rpc/server/public\x92\xb5\x18\x08INTERNALb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.snowflake_oauth_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z9github.com/textqllabs/demo2/compute/pkg/rpc/server/public\x92\xb5\x18\x08INTERNAL'
    _globals['_EXCHANGESNOWFLAKECODEREQUEST'].fields_by_name['code']._loaded_options = None
    _globals['_EXCHANGESNOWFLAKECODEREQUEST'].fields_by_name['code']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_EXCHANGESNOWFLAKECODEREQUEST'].fields_by_name['client_secret']._loaded_options = None
    _globals['_EXCHANGESNOWFLAKECODEREQUEST'].fields_by_name['client_secret']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_EXCHANGESNOWFLAKECODERESPONSE'].fields_by_name['access_token']._loaded_options = None
    _globals['_EXCHANGESNOWFLAKECODERESPONSE'].fields_by_name['access_token']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_EXCHANGESNOWFLAKECODERESPONSE'].fields_by_name['refresh_token']._loaded_options = None
    _globals['_EXCHANGESNOWFLAKECODERESPONSE'].fields_by_name['refresh_token']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_GETSNOWFLAKEOAUTHURLREQUEST']._serialized_start = 90
    _globals['_GETSNOWFLAKEOAUTHURLREQUEST']._serialized_end = 223
    _globals['_GETSNOWFLAKEOAUTHURLRESPONSE']._serialized_start = 225
    _globals['_GETSNOWFLAKEOAUTHURLRESPONSE']._serialized_end = 284
    _globals['_EXCHANGESNOWFLAKECODEREQUEST']._serialized_start = 287
    _globals['_EXCHANGESNOWFLAKECODEREQUEST']._serialized_end = 470
    _globals['_EXCHANGESNOWFLAKECODERESPONSE']._serialized_start = 473
    _globals['_EXCHANGESNOWFLAKECODERESPONSE']._serialized_end = 726
    _globals['_SNOWFLAKEOAUTHSERVICE']._serialized_start = 729
    _globals['_SNOWFLAKEOAUTHSERVICE']._serialized_end = 1063