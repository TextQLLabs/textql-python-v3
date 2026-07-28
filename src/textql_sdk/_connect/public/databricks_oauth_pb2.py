# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
# pylint: skip-file
# mypy: ignore-errors
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/databricks_oauth.proto')
_sym_db = _symbol_database.Default()
from ..public import options_pb2 as public_dot_options__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dpublic/databricks_oauth.proto\x12"textql.rpc.public.databricks_oauth\x1a\x14public/options.proto"v\n\x1cGetDatabricksOAuthURLRequest\x12#\n\rworkspace_url\x18\x01 \x01(\tR\x0cworkspaceUrl\x12\x1b\n\tclient_id\x18\x02 \x01(\tR\x08clientId\x12\x14\n\x05state\x18\x03 \x01(\tR\x05state"g\n\x1dGetDatabricksOAuthURLResponse\x12\x1b\n\toauth_url\x18\x01 \x01(\tR\x08oauthUrl\x12)\n\rcode_verifier\x18\x02 \x01(\tB\x04\x88\xb5\x18\x01R\x0ccodeVerifier"\xe7\x01\n\x1dExchangeDatabricksCodeRequest\x12\x18\n\x04code\x18\x01 \x01(\tB\x04\x88\xb5\x18\x01R\x04code\x12\x14\n\x05state\x18\x02 \x01(\tR\x05state\x12#\n\rworkspace_url\x18\x03 \x01(\tR\x0cworkspaceUrl\x12\x1b\n\tclient_id\x18\x04 \x01(\tR\x08clientId\x12)\n\rclient_secret\x18\x05 \x01(\tB\x04\x88\xb5\x18\x01R\x0cclientSecret\x12)\n\rcode_verifier\x18\x06 \x01(\tB\x04\x88\xb5\x18\x01R\x0ccodeVerifier"\xe2\x01\n\x1eExchangeDatabricksCodeResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\'\n\x0caccess_token\x18\x02 \x01(\tB\x04\x88\xb5\x18\x01R\x0baccessToken\x12)\n\rrefresh_token\x18\x03 \x01(\tB\x04\x88\xb5\x18\x01R\x0crefreshToken\x12\x1d\n\nexpires_in\x18\x04 \x01(\x03R\texpiresIn\x12\x14\n\x05scope\x18\x05 \x01(\tR\x05scope\x12\x1d\n\ntoken_type\x18\x06 \x01(\tR\ttokenType2\xd9\x02\n\x16DatabricksOAuthService\x12\x9c\x01\n\x15GetDatabricksOAuthURL\x12@.textql.rpc.public.databricks_oauth.GetDatabricksOAuthURLRequest\x1aA.textql.rpc.public.databricks_oauth.GetDatabricksOAuthURLResponse\x12\x9f\x01\n\x16ExchangeDatabricksCode\x12A.textql.rpc.public.databricks_oauth.ExchangeDatabricksCodeRequest\x1aB.textql.rpc.public.databricks_oauth.ExchangeDatabricksCodeResponseBGZ9github.com/textqllabs/demo2/compute/pkg/rpc/server/public\x92\xb5\x18\x08INTERNALb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.databricks_oauth_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z9github.com/textqllabs/demo2/compute/pkg/rpc/server/public\x92\xb5\x18\x08INTERNAL'
    _globals['_GETDATABRICKSOAUTHURLRESPONSE'].fields_by_name['code_verifier']._loaded_options = None
    _globals['_GETDATABRICKSOAUTHURLRESPONSE'].fields_by_name['code_verifier']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_EXCHANGEDATABRICKSCODEREQUEST'].fields_by_name['code']._loaded_options = None
    _globals['_EXCHANGEDATABRICKSCODEREQUEST'].fields_by_name['code']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_EXCHANGEDATABRICKSCODEREQUEST'].fields_by_name['client_secret']._loaded_options = None
    _globals['_EXCHANGEDATABRICKSCODEREQUEST'].fields_by_name['client_secret']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_EXCHANGEDATABRICKSCODEREQUEST'].fields_by_name['code_verifier']._loaded_options = None
    _globals['_EXCHANGEDATABRICKSCODEREQUEST'].fields_by_name['code_verifier']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_EXCHANGEDATABRICKSCODERESPONSE'].fields_by_name['access_token']._loaded_options = None
    _globals['_EXCHANGEDATABRICKSCODERESPONSE'].fields_by_name['access_token']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_EXCHANGEDATABRICKSCODERESPONSE'].fields_by_name['refresh_token']._loaded_options = None
    _globals['_EXCHANGEDATABRICKSCODERESPONSE'].fields_by_name['refresh_token']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_GETDATABRICKSOAUTHURLREQUEST']._serialized_start = 91
    _globals['_GETDATABRICKSOAUTHURLREQUEST']._serialized_end = 209
    _globals['_GETDATABRICKSOAUTHURLRESPONSE']._serialized_start = 211
    _globals['_GETDATABRICKSOAUTHURLRESPONSE']._serialized_end = 314
    _globals['_EXCHANGEDATABRICKSCODEREQUEST']._serialized_start = 317
    _globals['_EXCHANGEDATABRICKSCODEREQUEST']._serialized_end = 548
    _globals['_EXCHANGEDATABRICKSCODERESPONSE']._serialized_start = 551
    _globals['_EXCHANGEDATABRICKSCODERESPONSE']._serialized_end = 777
    _globals['_DATABRICKSOAUTHSERVICE']._serialized_start = 780
    _globals['_DATABRICKSOAUTHSERVICE']._serialized_end = 1125