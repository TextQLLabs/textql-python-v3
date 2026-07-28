# pylint: skip-file
# mypy: ignore-errors
# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/api_oauth.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ..public import options_pb2 as public_dot_options__pb2
from ..public import secret_pb2 as public_dot_secret__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16public/api_oauth.proto\x12\x1btextql.rpc.public.api_oauth\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14public/options.proto\x1a\x13public/secret.proto"g\n\x15GetApiOAuthURLRequest\x128\n\x03ref\x18\x01 \x01(\x0b2&.textql.rpc.public.secret.ApiAccessRefR\x03ref\x12\x14\n\x05state\x18\x02 \x01(\tR\x05state"`\n\x16GetApiOAuthURLResponse\x12\x1b\n\toauth_url\x18\x01 \x01(\tR\x08oauthUrl\x12)\n\rcode_verifier\x18\x02 \x01(\tB\x04\x88\xb5\x18\x01R\x0ccodeVerifier"\xb2\x01\n\x1bExchangeApiOAuthCodeRequest\x128\n\x03ref\x18\x01 \x01(\x0b2&.textql.rpc.public.secret.ApiAccessRefR\x03ref\x12\x18\n\x04code\x18\x02 \x01(\tB\x04\x88\xb5\x18\x01R\x04code\x12\x14\n\x05state\x18\x03 \x01(\tR\x05state\x12)\n\rcode_verifier\x18\x04 \x01(\tB\x04\x88\xb5\x18\x01R\x0ccodeVerifier"\x86\x01\n\x1cExchangeApiOAuthCodeResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12)\n\x11api_access_key_id\x18\x02 \x01(\tR\x0eapiAccessKeyId\x12!\n\x0cdisplay_name\x18\x03 \x01(\tR\x0bdisplayName"d\n(ExchangeApiOAuthClientCredentialsRequest\x128\n\x03ref\x18\x01 \x01(\x0b2&.textql.rpc.public.secret.ApiAccessRefR\x03ref"\\\n ExchangeApiOAuthJwtBearerRequest\x128\n\x03ref\x18\x01 \x01(\x0b2&.textql.rpc.public.secret.ApiAccessRefR\x03ref"^\n"InitiateDeviceAuthorizationRequest\x128\n\x03ref\x18\x01 \x01(\x0b2&.textql.rpc.public.secret.ApiAccessRefR\x03ref"\x8b\x02\n#InitiateDeviceAuthorizationResponse\x12%\n\x0bdevice_code\x18\x01 \x01(\tB\x04\x88\xb5\x18\x01R\ndeviceCode\x12\x1b\n\tuser_code\x18\x02 \x01(\tR\x08userCode\x12)\n\x10verification_uri\x18\x03 \x01(\tR\x0fverificationUri\x12:\n\x19verification_uri_complete\x18\x04 \x01(\tR\x17verificationUriComplete\x12\x1d\n\nexpires_in\x18\x05 \x01(\x05R\texpiresIn\x12\x1a\n\x08interval\x18\x06 \x01(\x05R\x08interval"}\n\x1aPollDeviceCodeTokenRequest\x128\n\x03ref\x18\x01 \x01(\x0b2&.textql.rpc.public.secret.ApiAccessRefR\x03ref\x12%\n\x0bdevice_code\x18\x02 \x01(\tB\x04\x88\xb5\x18\x01R\ndeviceCode"\x85\x01\n\x1bPollDeviceCodeTokenResponse\x12\x16\n\x06status\x18\x01 \x01(\tR\x06status\x12!\n\x0cdisplay_name\x18\x02 \x01(\tR\x0bdisplayName\x12+\n\x11error_description\x18\x03 \x01(\tR\x10errorDescription"E\n\x18GetApiOAuthStatusRequest\x12)\n\x11api_access_key_id\x18\x01 \x01(\tR\x0eapiAccessKeyId"\x89\x01\n\x19GetApiOAuthStatusResponse\x12$\n\rauthenticated\x18\x01 \x01(\x08R\rauthenticated\x12#\n\rtoken_expired\x18\x02 \x01(\x08R\x0ctokenExpired\x12!\n\x0cdisplay_name\x18\x03 \x01(\tR\x0bdisplayName"V\n\x1aRevokeApiOAuthTokenRequest\x128\n\x03ref\x18\x01 \x01(\x0b2&.textql.rpc.public.secret.ApiAccessRefR\x03ref"\x1d\n\x1bRevokeApiOAuthTokenResponse"\x87\x05\n\x0eApiOAuthConfig\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1b\n\tclient_id\x18\x03 \x01(\tR\x08clientId\x12\x19\n\x08auth_url\x18\x04 \x01(\tR\x07authUrl\x12\x1b\n\ttoken_url\x18\x05 \x01(\tR\x08tokenUrl\x12\x16\n\x06scopes\x18\x06 \x01(\tR\x06scopes\x12\x19\n\x08use_pkce\x18\x07 \x01(\x08R\x07usePkce\x12*\n\x11token_auth_method\x18\x08 \x01(\tR\x0ftokenAuthMethod\x12_\n\x0cextra_config\x18\t \x03(\x0b2<.textql.rpc.public.api_oauth.ApiOAuthConfig.ExtraConfigEntryR\x0bextraConfig\x129\n\ncreated_at\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt\x129\n\nupdated_at\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampR\tupdatedAt\x12)\n\x11api_access_key_id\x18\x0c \x01(\tR\x0eapiAccessKeyId\x12\x1f\n\x0bauth_header\x18\r \x01(\tR\nauthHeader\x12\x1f\n\x0bauth_prefix\x18\x0e \x01(\tR\nauthPrefix\x12\x1d\n\ngrant_type\x18\x0f \x01(\tR\tgrantType\x1a>\n\x10ExtraConfigEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01J\x04\x08\x02\x10\x03R\x08provider"\xd5\x04\n\x1bUpsertApiOAuthConfigRequest\x12\x1b\n\tclient_id\x18\x02 \x01(\tR\x08clientId\x12)\n\rclient_secret\x18\x03 \x01(\tB\x04\x88\xb5\x18\x01R\x0cclientSecret\x12\x19\n\x08auth_url\x18\x04 \x01(\tR\x07authUrl\x12\x1b\n\ttoken_url\x18\x05 \x01(\tR\x08tokenUrl\x12\x16\n\x06scopes\x18\x06 \x01(\tR\x06scopes\x12\x19\n\x08use_pkce\x18\x07 \x01(\x08R\x07usePkce\x12*\n\x11token_auth_method\x18\x08 \x01(\tR\x0ftokenAuthMethod\x12l\n\x0cextra_config\x18\t \x03(\x0b2I.textql.rpc.public.api_oauth.UpsertApiOAuthConfigRequest.ExtraConfigEntryR\x0bextraConfig\x128\n\x03ref\x18\n \x01(\x0b2&.textql.rpc.public.secret.ApiAccessRefR\x03ref\x12\x1f\n\x0bauth_header\x18\x0b \x01(\tR\nauthHeader\x12\x1f\n\x0bauth_prefix\x18\x0c \x01(\tR\nauthPrefix\x12\x1d\n\ngrant_type\x18\r \x01(\tR\tgrantType\x1a>\n\x10ExtraConfigEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01J\x04\x08\x01\x10\x02R\x08provider"c\n\x1cUpsertApiOAuthConfigResponse\x12C\n\x06config\x18\x01 \x01(\x0b2+.textql.rpc.public.api_oauth.ApiOAuthConfigR\x06config"E\n\x18GetApiOAuthConfigRequest\x12)\n\x11api_access_key_id\x18\x01 \x01(\tR\x0eapiAccessKeyId"`\n\x19GetApiOAuthConfigResponse\x12C\n\x06config\x18\x01 \x01(\x0b2+.textql.rpc.public.api_oauth.ApiOAuthConfigR\x06config2\xba\x0b\n\x0fApiOAuthService\x12~\n\x0eGetApiOAuthURL\x122.textql.rpc.public.api_oauth.GetApiOAuthURLRequest\x1a3.textql.rpc.public.api_oauth.GetApiOAuthURLResponse"\x03\x90\x02\x01\x12\x8b\x01\n\x14ExchangeApiOAuthCode\x128.textql.rpc.public.api_oauth.ExchangeApiOAuthCodeRequest\x1a9.textql.rpc.public.api_oauth.ExchangeApiOAuthCodeResponse\x12\xa5\x01\n!ExchangeApiOAuthClientCredentials\x12E.textql.rpc.public.api_oauth.ExchangeApiOAuthClientCredentialsRequest\x1a9.textql.rpc.public.api_oauth.ExchangeApiOAuthCodeResponse\x12\x95\x01\n\x19ExchangeApiOAuthJwtBearer\x12=.textql.rpc.public.api_oauth.ExchangeApiOAuthJwtBearerRequest\x1a9.textql.rpc.public.api_oauth.ExchangeApiOAuthCodeResponse\x12\xa0\x01\n\x1bInitiateDeviceAuthorization\x12?.textql.rpc.public.api_oauth.InitiateDeviceAuthorizationRequest\x1a@.textql.rpc.public.api_oauth.InitiateDeviceAuthorizationResponse\x12\x88\x01\n\x13PollDeviceCodeToken\x127.textql.rpc.public.api_oauth.PollDeviceCodeTokenRequest\x1a8.textql.rpc.public.api_oauth.PollDeviceCodeTokenResponse\x12\x87\x01\n\x11GetApiOAuthStatus\x125.textql.rpc.public.api_oauth.GetApiOAuthStatusRequest\x1a6.textql.rpc.public.api_oauth.GetApiOAuthStatusResponse"\x03\x90\x02\x01\x12\x88\x01\n\x13RevokeApiOAuthToken\x127.textql.rpc.public.api_oauth.RevokeApiOAuthTokenRequest\x1a8.textql.rpc.public.api_oauth.RevokeApiOAuthTokenResponse\x12\x8b\x01\n\x14UpsertApiOAuthConfig\x128.textql.rpc.public.api_oauth.UpsertApiOAuthConfigRequest\x1a9.textql.rpc.public.api_oauth.UpsertApiOAuthConfigResponse\x12\x87\x01\n\x11GetApiOAuthConfig\x125.textql.rpc.public.api_oauth.GetApiOAuthConfigRequest\x1a6.textql.rpc.public.api_oauth.GetApiOAuthConfigResponse"\x03\x90\x02\x01BGZ9github.com/textqllabs/demo2/compute/pkg/rpc/server/public\x92\xb5\x18\x08INTERNALb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.api_oauth_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z9github.com/textqllabs/demo2/compute/pkg/rpc/server/public\x92\xb5\x18\x08INTERNAL'
    _globals['_GETAPIOAUTHURLRESPONSE'].fields_by_name['code_verifier']._loaded_options = None
    _globals['_GETAPIOAUTHURLRESPONSE'].fields_by_name['code_verifier']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_EXCHANGEAPIOAUTHCODEREQUEST'].fields_by_name['code']._loaded_options = None
    _globals['_EXCHANGEAPIOAUTHCODEREQUEST'].fields_by_name['code']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_EXCHANGEAPIOAUTHCODEREQUEST'].fields_by_name['code_verifier']._loaded_options = None
    _globals['_EXCHANGEAPIOAUTHCODEREQUEST'].fields_by_name['code_verifier']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_INITIATEDEVICEAUTHORIZATIONRESPONSE'].fields_by_name['device_code']._loaded_options = None
    _globals['_INITIATEDEVICEAUTHORIZATIONRESPONSE'].fields_by_name['device_code']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_POLLDEVICECODETOKENREQUEST'].fields_by_name['device_code']._loaded_options = None
    _globals['_POLLDEVICECODETOKENREQUEST'].fields_by_name['device_code']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_APIOAUTHCONFIG_EXTRACONFIGENTRY']._loaded_options = None
    _globals['_APIOAUTHCONFIG_EXTRACONFIGENTRY']._serialized_options = b'8\x01'
    _globals['_UPSERTAPIOAUTHCONFIGREQUEST_EXTRACONFIGENTRY']._loaded_options = None
    _globals['_UPSERTAPIOAUTHCONFIGREQUEST_EXTRACONFIGENTRY']._serialized_options = b'8\x01'
    _globals['_UPSERTAPIOAUTHCONFIGREQUEST'].fields_by_name['client_secret']._loaded_options = None
    _globals['_UPSERTAPIOAUTHCONFIGREQUEST'].fields_by_name['client_secret']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_APIOAUTHSERVICE'].methods_by_name['GetApiOAuthURL']._loaded_options = None
    _globals['_APIOAUTHSERVICE'].methods_by_name['GetApiOAuthURL']._serialized_options = b'\x90\x02\x01'
    _globals['_APIOAUTHSERVICE'].methods_by_name['GetApiOAuthStatus']._loaded_options = None
    _globals['_APIOAUTHSERVICE'].methods_by_name['GetApiOAuthStatus']._serialized_options = b'\x90\x02\x01'
    _globals['_APIOAUTHSERVICE'].methods_by_name['GetApiOAuthConfig']._loaded_options = None
    _globals['_APIOAUTHSERVICE'].methods_by_name['GetApiOAuthConfig']._serialized_options = b'\x90\x02\x01'
    _globals['_GETAPIOAUTHURLREQUEST']._serialized_start = 131
    _globals['_GETAPIOAUTHURLREQUEST']._serialized_end = 234
    _globals['_GETAPIOAUTHURLRESPONSE']._serialized_start = 236
    _globals['_GETAPIOAUTHURLRESPONSE']._serialized_end = 332
    _globals['_EXCHANGEAPIOAUTHCODEREQUEST']._serialized_start = 335
    _globals['_EXCHANGEAPIOAUTHCODEREQUEST']._serialized_end = 513
    _globals['_EXCHANGEAPIOAUTHCODERESPONSE']._serialized_start = 516
    _globals['_EXCHANGEAPIOAUTHCODERESPONSE']._serialized_end = 650
    _globals['_EXCHANGEAPIOAUTHCLIENTCREDENTIALSREQUEST']._serialized_start = 652
    _globals['_EXCHANGEAPIOAUTHCLIENTCREDENTIALSREQUEST']._serialized_end = 752
    _globals['_EXCHANGEAPIOAUTHJWTBEARERREQUEST']._serialized_start = 754
    _globals['_EXCHANGEAPIOAUTHJWTBEARERREQUEST']._serialized_end = 846
    _globals['_INITIATEDEVICEAUTHORIZATIONREQUEST']._serialized_start = 848
    _globals['_INITIATEDEVICEAUTHORIZATIONREQUEST']._serialized_end = 942
    _globals['_INITIATEDEVICEAUTHORIZATIONRESPONSE']._serialized_start = 945
    _globals['_INITIATEDEVICEAUTHORIZATIONRESPONSE']._serialized_end = 1212
    _globals['_POLLDEVICECODETOKENREQUEST']._serialized_start = 1214
    _globals['_POLLDEVICECODETOKENREQUEST']._serialized_end = 1339
    _globals['_POLLDEVICECODETOKENRESPONSE']._serialized_start = 1342
    _globals['_POLLDEVICECODETOKENRESPONSE']._serialized_end = 1475
    _globals['_GETAPIOAUTHSTATUSREQUEST']._serialized_start = 1477
    _globals['_GETAPIOAUTHSTATUSREQUEST']._serialized_end = 1546
    _globals['_GETAPIOAUTHSTATUSRESPONSE']._serialized_start = 1549
    _globals['_GETAPIOAUTHSTATUSRESPONSE']._serialized_end = 1686
    _globals['_REVOKEAPIOAUTHTOKENREQUEST']._serialized_start = 1688
    _globals['_REVOKEAPIOAUTHTOKENREQUEST']._serialized_end = 1774
    _globals['_REVOKEAPIOAUTHTOKENRESPONSE']._serialized_start = 1776
    _globals['_REVOKEAPIOAUTHTOKENRESPONSE']._serialized_end = 1805
    _globals['_APIOAUTHCONFIG']._serialized_start = 1808
    _globals['_APIOAUTHCONFIG']._serialized_end = 2455
    _globals['_APIOAUTHCONFIG_EXTRACONFIGENTRY']._serialized_start = 2377
    _globals['_APIOAUTHCONFIG_EXTRACONFIGENTRY']._serialized_end = 2439
    _globals['_UPSERTAPIOAUTHCONFIGREQUEST']._serialized_start = 2458
    _globals['_UPSERTAPIOAUTHCONFIGREQUEST']._serialized_end = 3055
    _globals['_UPSERTAPIOAUTHCONFIGREQUEST_EXTRACONFIGENTRY']._serialized_start = 2377
    _globals['_UPSERTAPIOAUTHCONFIGREQUEST_EXTRACONFIGENTRY']._serialized_end = 2439
    _globals['_UPSERTAPIOAUTHCONFIGRESPONSE']._serialized_start = 3057
    _globals['_UPSERTAPIOAUTHCONFIGRESPONSE']._serialized_end = 3156
    _globals['_GETAPIOAUTHCONFIGREQUEST']._serialized_start = 3158
    _globals['_GETAPIOAUTHCONFIGREQUEST']._serialized_end = 3227
    _globals['_GETAPIOAUTHCONFIGRESPONSE']._serialized_start = 3229
    _globals['_GETAPIOAUTHCONFIGRESPONSE']._serialized_end = 3325
    _globals['_APIOAUTHSERVICE']._serialized_start = 3328
    _globals['_APIOAUTHSERVICE']._serialized_end = 4794