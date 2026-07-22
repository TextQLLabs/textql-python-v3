"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/connector_member_auth.proto')
_sym_db = _symbol_database.Default()
from ..public import options_pb2 as public_dot_options__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"public/connector_member_auth.proto\x12\'textql.rpc.public.connector_member_auth\x1a\x14public/options.proto"\xef\x01\n%AuthenticateMemberForConnectorRequest\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId\x12\'\n\x0caccess_token\x18\x02 \x01(\tB\x04\x88\xb5\x18\x01R\x0baccessToken\x12)\n\rrefresh_token\x18\x03 \x01(\tB\x04\x88\xb5\x18\x01R\x0crefreshToken\x12\x1d\n\nexpires_in\x18\x04 \x01(\x03R\texpiresIn\x12\x1a\n\x08username\x18\x05 \x01(\tR\x08username\x12\x14\n\x05scope\x18\x06 \x01(\tR\x05scope"B\n&AuthenticateMemberForConnectorResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success"\xc2\x01\n!ExchangeAndStoreMemberAuthRequest\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId\x12\x18\n\x04code\x18\x02 \x01(\tB\x04\x88\xb5\x18\x01R\x04code\x12\x14\n\x05state\x18\x03 \x01(\tR\x05state\x12\x1f\n\x0baccount_url\x18\x04 \x01(\tR\naccountUrl\x12)\n\rcode_verifier\x18\x05 \x01(\tB\x04\x88\xb5\x18\x01R\x0ccodeVerifier"Z\n"ExchangeAndStoreMemberAuthResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x1a\n\x08username\x18\x02 \x01(\tR\x08username"J\n#GetMemberConnectorAuthStatusRequest\x12#\n\rconnector_ids\x18\x01 \x03(\x05R\x0cconnectorIds"\x9f\x01\n\x13ConnectorAuthStatus\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId\x12$\n\rauthenticated\x18\x02 \x01(\x08R\rauthenticated\x12\x1a\n\x08username\x18\x03 \x01(\tR\x08username\x12#\n\rtoken_expired\x18\x04 \x01(\x08R\x0ctokenExpired"\x80\x01\n$GetMemberConnectorAuthStatusResponse\x12X\n\x08statuses\x18\x01 \x03(\x0b2<.textql.rpc.public.connector_member_auth.ConnectorAuthStatusR\x08statuses2\xd6\x04\n\x1aConnectorMemberAuthService\x12\xc1\x01\n\x1eAuthenticateMemberForConnector\x12N.textql.rpc.public.connector_member_auth.AuthenticateMemberForConnectorRequest\x1aO.textql.rpc.public.connector_member_auth.AuthenticateMemberForConnectorResponse\x12\xb5\x01\n\x1aExchangeAndStoreMemberAuth\x12J.textql.rpc.public.connector_member_auth.ExchangeAndStoreMemberAuthRequest\x1aK.textql.rpc.public.connector_member_auth.ExchangeAndStoreMemberAuthResponse\x12\xbb\x01\n\x1cGetMemberConnectorAuthStatus\x12L.textql.rpc.public.connector_member_auth.GetMemberConnectorAuthStatusRequest\x1aM.textql.rpc.public.connector_member_auth.GetMemberConnectorAuthStatusResponseBGZ9github.com/textqllabs/demo2/compute/pkg/rpc/server/public\x92\xb5\x18\x08INTERNALb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.connector_member_auth_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z9github.com/textqllabs/demo2/compute/pkg/rpc/server/public\x92\xb5\x18\x08INTERNAL'
    _globals['_AUTHENTICATEMEMBERFORCONNECTORREQUEST'].fields_by_name['access_token']._loaded_options = None
    _globals['_AUTHENTICATEMEMBERFORCONNECTORREQUEST'].fields_by_name['access_token']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_AUTHENTICATEMEMBERFORCONNECTORREQUEST'].fields_by_name['refresh_token']._loaded_options = None
    _globals['_AUTHENTICATEMEMBERFORCONNECTORREQUEST'].fields_by_name['refresh_token']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_EXCHANGEANDSTOREMEMBERAUTHREQUEST'].fields_by_name['code']._loaded_options = None
    _globals['_EXCHANGEANDSTOREMEMBERAUTHREQUEST'].fields_by_name['code']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_EXCHANGEANDSTOREMEMBERAUTHREQUEST'].fields_by_name['code_verifier']._loaded_options = None
    _globals['_EXCHANGEANDSTOREMEMBERAUTHREQUEST'].fields_by_name['code_verifier']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_AUTHENTICATEMEMBERFORCONNECTORREQUEST']._serialized_start = 102
    _globals['_AUTHENTICATEMEMBERFORCONNECTORREQUEST']._serialized_end = 341
    _globals['_AUTHENTICATEMEMBERFORCONNECTORRESPONSE']._serialized_start = 343
    _globals['_AUTHENTICATEMEMBERFORCONNECTORRESPONSE']._serialized_end = 409
    _globals['_EXCHANGEANDSTOREMEMBERAUTHREQUEST']._serialized_start = 412
    _globals['_EXCHANGEANDSTOREMEMBERAUTHREQUEST']._serialized_end = 606
    _globals['_EXCHANGEANDSTOREMEMBERAUTHRESPONSE']._serialized_start = 608
    _globals['_EXCHANGEANDSTOREMEMBERAUTHRESPONSE']._serialized_end = 698
    _globals['_GETMEMBERCONNECTORAUTHSTATUSREQUEST']._serialized_start = 700
    _globals['_GETMEMBERCONNECTORAUTHSTATUSREQUEST']._serialized_end = 774
    _globals['_CONNECTORAUTHSTATUS']._serialized_start = 777
    _globals['_CONNECTORAUTHSTATUS']._serialized_end = 936
    _globals['_GETMEMBERCONNECTORAUTHSTATUSRESPONSE']._serialized_start = 939
    _globals['_GETMEMBERCONNECTORAUTHSTATUSRESPONSE']._serialized_end = 1067
    _globals['_CONNECTORMEMBERAUTHSERVICE']._serialized_start = 1070
    _globals['_CONNECTORMEMBERAUTHSERVICE']._serialized_end = 1668