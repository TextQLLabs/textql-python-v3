# pylint: skip-file
# mypy: ignore-errors
# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/secret.proto')
_sym_db = _symbol_database.Default()
from ..google.api import visibility_pb2 as google_dot_api_dot_visibility__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ..public import identity_pb2 as public_dot_identity__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13public/secret.proto\x12\x18textql.rpc.public.secret\x1a\x1bgoogle/api/visibility.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x15public/identity.proto"\xed\x02\n\x06Secret\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x129\n\ncreated_at\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt\x129\n\nupdated_at\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\tupdatedAt\x12%\n\x0bdescription\x18\x05 \x01(\tH\x00R\x0bdescription\x88\x01\x01\x12\x17\n\x04link\x18\x06 \x01(\tH\x01R\x04link\x88\x01\x01\x12\x1d\n\ncreated_by\x18\x07 \x01(\tR\tcreatedBy\x12$\n\x0baccess_type\x18\x08 \x01(\tH\x02R\naccessType\x88\x01\x01\x12\x1b\n\tis_public\x18\t \x01(\x08R\x08isPublicB\x0e\n\x0c_descriptionB\x07\n\x05_linkB\x0e\n\x0c_access_type"\x14\n\x12ListSecretsRequest"Q\n\x13ListSecretsResponse\x12:\n\x07secrets\x18\x01 \x03(\x0b2 .textql.rpc.public.secret.SecretR\x07secrets"\xb4\x01\n\x10PutSecretRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\x12%\n\x0bdescription\x18\x03 \x01(\tH\x00R\x0bdescription\x88\x01\x01\x12\x17\n\x04link\x18\x04 \x01(\tH\x01R\x04link\x88\x01\x01\x12\x1d\n\nis_private\x18\x05 \x01(\x08R\tisPrivateB\x0e\n\x0c_descriptionB\x07\n\x05_link"\x13\n\x11PutSecretResponse"\xa7\x01\n\x13UpdateSecretRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x19\n\x05value\x18\x02 \x01(\tH\x00R\x05value\x88\x01\x01\x12%\n\x0bdescription\x18\x03 \x01(\tH\x01R\x0bdescription\x88\x01\x01\x12\x17\n\x04link\x18\x04 \x01(\tH\x02R\x04link\x88\x01\x01B\x08\n\x06_valueB\x0e\n\x0c_descriptionB\x07\n\x05_link"\x16\n\x14UpdateSecretResponse")\n\x13DeleteSecretRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\x16\n\x14DeleteSecretResponse"\x1e\n\x1cGetMembersWithSecretsRequest"]\n\x1dGetMembersWithSecretsResponse\x12<\n\x07members\x18\x01 \x03(\x0b2".textql.rpc.identity.MemberPreviewR\x07members"G\n\rHttpBasicAuth\x12\x1a\n\x08username\x18\x01 \x01(\tR\x08username\x12\x1a\n\x08password\x18\x02 \x01(\tR\x08password"U\n\x0cApiAccessRef\x12)\n\x11api_access_key_id\x18\x01 \x01(\tR\x0eapiAccessKeyId\x12\x1a\n\x08revision\x18\x02 \x01(\x04R\x08revision"\x9f\n\n\x0cApiAccessKey\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x1b\n\tmember_id\x18\x03 \x01(\tR\x08memberId\x12\x14\n\x05hosts\x18\x04 \x03(\tR\x05hosts\x12M\n\x07headers\x18\x05 \x03(\x0b23.textql.rpc.public.secret.ApiAccessKey.HeadersEntryR\x07headers\x12Z\n\x0cquery_params\x18\x06 \x03(\x0b27.textql.rpc.public.secret.ApiAccessKey.QueryParamsEntryR\x0bqueryParams\x12 \n\x0bdescription\x18\x07 \x01(\tR\x0bdescription\x129\n\ncreated_at\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt\x129\n\nupdated_at\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampR\tupdatedAt\x12>\n\nexpires_at\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampH\x00R\texpiresAt\x88\x01\x01\x12\x1a\n\x08provider\x18\x0b \x01(\tR\x08provider\x12\x1b\n\tauth_type\x18\x0c \x01(\tR\x08authType\x12<\n\x1amember_oauth_authenticated\x18\r \x01(\x08R\x18memberOauthAuthenticated\x129\n\x19member_oauth_display_name\x18\x0e \x01(\tR\x16memberOauthDisplayName\x12T\n\x0fhttp_basic_auth\x18\x10 \x01(\x0b2\'.textql.rpc.public.secret.HttpBasicAuthH\x01R\rhttpBasicAuth\x88\x01\x01\x12D\n\x04body\x18\x11 \x03(\x0b20.textql.rpc.public.secret.ApiAccessKey.BodyEntryR\x04body\x12L\n\x0ccontent_type\x18\x12 \x01(\x0e2).textql.rpc.public.secret.BodyContentTypeR\x0bcontentType\x12\x1b\n\tcan_write\x18\x13 \x01(\x08R\x08canWrite\x12$\n\x0baccess_type\x18\x14 \x01(\tH\x02R\naccessType\x88\x01\x01\x12\x1b\n\tis_public\x18\x15 \x01(\x08R\x08isPublic\x12\x19\n\x08test_url\x18\x16 \x01(\tR\x07testUrl\x12\x12\n\x04name\x18\x17 \x01(\tR\x04name\x12\x1f\n\x0bauth_prefix\x18\x18 \x01(\tR\nauthPrefix\x1a:\n\x0cHeadersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01\x1a>\n\x10QueryParamsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01\x1a7\n\tBodyEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01B\r\n\x0b_expires_atB\x12\n\x10_http_basic_authB\x0e\n\x0c_access_type"`\n\x18CreateApiRevisionRequest\x12.\n\x11api_access_key_id\x18\x01 \x01(\tH\x00R\x0eapiAccessKeyId\x88\x01\x01B\x14\n\x12_api_access_key_id"\xbb\x01\n\x19CreateApiRevisionResponse\x128\n\x03ref\x18\x01 \x01(\x0b2&.textql.rpc.public.secret.ApiAccessRefR\x03ref\x12Q\n\x0eapi_access_key\x18\x02 \x01(\x0b2&.textql.rpc.public.secret.ApiAccessKeyH\x00R\x0capiAccessKey\x88\x01\x01B\x11\n\x0f_api_access_key"\xb6\x08\n\x19UpsertApiAccessKeyRequest\x128\n\x03ref\x18\x01 \x01(\x0b2&.textql.rpc.public.secret.ApiAccessRefR\x03ref\x12"\n\rpersist_to_db\x18\x02 \x01(\x08R\x0bpersistToDb\x12\x14\n\x05hosts\x18\x03 \x03(\tR\x05hosts\x12Z\n\x07headers\x18\x04 \x03(\x0b2@.textql.rpc.public.secret.UpsertApiAccessKeyRequest.HeadersEntryR\x07headers\x12g\n\x0cquery_params\x18\x05 \x03(\x0b2D.textql.rpc.public.secret.UpsertApiAccessKeyRequest.QueryParamsEntryR\x0bqueryParams\x12 \n\x0bdescription\x18\x06 \x01(\tR\x0bdescription\x12>\n\nexpires_at\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00R\texpiresAt\x88\x01\x01\x12\x1a\n\x08provider\x18\t \x01(\tR\x08provider\x12\x1d\n\nauth_value\x18\n \x01(\tR\tauthValue\x12(\n\x10auth_value_extra\x18\x0b \x01(\tR\x0eauthValueExtra\x12\x1b\n\tauth_type\x18\x0c \x01(\tR\x08authType\x12T\n\x0fhttp_basic_auth\x18\r \x01(\x0b2\'.textql.rpc.public.secret.HttpBasicAuthH\x01R\rhttpBasicAuth\x88\x01\x01\x12Q\n\x04body\x18\x0e \x03(\x0b2=.textql.rpc.public.secret.UpsertApiAccessKeyRequest.BodyEntryR\x04body\x12L\n\x0ccontent_type\x18\x0f \x01(\x0e2).textql.rpc.public.secret.BodyContentTypeR\x0bcontentType\x12\x19\n\x08test_url\x18\x10 \x01(\tR\x07testUrl\x12\x12\n\x04name\x18\x11 \x01(\tR\x04name\x1a:\n\x0cHeadersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01\x1a>\n\x10QueryParamsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01\x1a7\n\tBodyEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01B\r\n\x0b_expires_atB\x12\n\x10_http_basic_auth"j\n\x1aUpsertApiAccessKeyResponse\x12L\n\x0eapi_access_key\x18\x01 \x01(\x0b2&.textql.rpc.public.secret.ApiAccessKeyR\x0capiAccessKey"T\n\x18DeleteApiRevisionRequest\x128\n\x03ref\x18\x01 \x01(\x0b2&.textql.rpc.public.secret.ApiAccessRefR\x03ref"\x1b\n\x19DeleteApiRevisionResponse"\x1a\n\x18ListApiAccessKeysRequest"k\n\x19ListApiAccessKeysResponse\x12N\n\x0fapi_access_keys\x18\x01 \x03(\x0b2&.textql.rpc.public.secret.ApiAccessKeyR\rapiAccessKeys"(\n\x16GetApiAccessKeyRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"g\n\x17GetApiAccessKeyResponse\x12L\n\x0eapi_access_key\x18\x01 \x01(\x0b2&.textql.rpc.public.secret.ApiAccessKeyR\x0capiAccessKey"+\n\x19DeleteApiAccessKeyRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x1c\n\x1aDeleteApiAccessKeyResponse"\xb7\x01\n\x0bEnvVarField\x12\x17\n\x07env_var\x18\x01 \x01(\tR\x06envVar\x12\x14\n\x05label\x18\x02 \x01(\tR\x05label\x12\x1a\n\x08required\x18\x03 \x01(\x08R\x08required\x12\x16\n\x06secret\x18\x04 \x01(\x08R\x06secret\x12#\n\rdefault_value\x18\x05 \x01(\tR\x0cdefaultValue\x12 \n\x0bplaceholder\x18\x06 \x01(\tR\x0bplaceholder"\xd9\x06\n\x0bApiProvider\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x19\n\x08icon_url\x18\x03 \x01(\tR\x07iconUrl\x12\x1b\n\tauth_type\x18\x04 \x01(\tR\x08authType\x12 \n\x0bdescription\x18\x05 \x01(\tR\x0bdescription\x12\x19\n\x08docs_url\x18\x06 \x01(\tR\x07docsUrl\x12#\n\rdefault_hosts\x18\x07 \x03(\tR\x0cdefaultHosts\x12\x1f\n\x0btoken_label\x18\x08 \x01(\tR\ntokenLabel\x12\x1f\n\x0bauth_header\x18\t \x01(\tR\nauthHeader\x12\x1f\n\x0bauth_prefix\x18\n \x01(\tR\nauthPrefix\x12\'\n\x0foauth_supported\x18\x0b \x01(\x08R\x0eoauthSupported\x12)\n\x10oauth_configured\x18\x0c \x01(\x08R\x0foauthConfigured\x121\n\x14member_authenticated\x18\r \x01(\x08R\x13memberAuthenticated\x127\n\x18member_auth_display_name\x18\x0e \x01(\tR\x15memberAuthDisplayName\x12K\n\x0eenv_var_fields\x18\x0f \x03(\x0b2%.textql.rpc.public.secret.EnvVarFieldR\x0cenvVarFields\x123\n\x16oauth_has_default_urls\x18\x10 \x01(\x08R\x13oauthHasDefaultUrls\x12$\n\x0eoauth_auth_url\x18\x11 \x01(\tR\x0coauthAuthUrl\x12&\n\x0foauth_token_url\x18\x12 \x01(\tR\roauthTokenUrl\x12!\n\x0coauth_scopes\x18\x13 \x01(\tR\x0boauthScopes\x12$\n\x0eoauth_use_pkce\x18\x14 \x01(\x08R\x0coauthUsePkce\x125\n\x17oauth_token_auth_method\x18\x15 \x01(\tR\x14oauthTokenAuthMethod\x12\x19\n\x08test_url\x18\x16 \x01(\tR\x07testUrl"S\n\x17TestApiAccessKeyRequest\x128\n\x03ref\x18\x01 \x01(\x0b2&.textql.rpc.public.secret.ApiAccessRefR\x03ref"o\n\x18TestApiAccessKeyResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x1f\n\x0bstatus_code\x18\x02 \x01(\x05R\nstatusCode\x12\x18\n\x07message\x18\x03 \x01(\tR\x07message"\x19\n\x17ListApiProvidersRequest"_\n\x18ListApiProvidersResponse\x12C\n\tproviders\x18\x01 \x03(\x0b2%.textql.rpc.public.secret.ApiProviderR\tproviders"\x80\x02\n"MigrateSecretToApiConnectorRequest\x12\x1f\n\x0bsecret_name\x18\x01 \x01(\tR\nsecretName\x12)\n\x11api_access_key_id\x18\x02 \x01(\tR\x0eapiAccessKeyId\x12\x1f\n\x0bheader_name\x18\x03 \x01(\tR\nheaderName\x12\x14\n\x05hosts\x18\x04 \x03(\tR\x05hosts\x12 \n\x0bdescription\x18\x05 \x01(\tR\x0bdescription\x12!\n\x0cvalue_prefix\x18\x06 \x01(\tR\x0bvaluePrefix\x12\x12\n\x04name\x18\x07 \x01(\tR\x04name"s\n#MigrateSecretToApiConnectorResponse\x12L\n\x0eapi_access_key\x18\x01 \x01(\x0b2&.textql.rpc.public.secret.ApiAccessKeyR\x0capiAccessKey*e\n\x0fBodyContentType\x12\x1a\n\x16BODY_CONTENT_TYPE_NONE\x10\x00\x12\x1a\n\x16BODY_CONTENT_TYPE_JSON\x10\x01\x12\x1a\n\x16BODY_CONTENT_TYPE_FORM\x10\x022\x91\x0f\n\rSecretService\x12o\n\x0bListSecrets\x12,.textql.rpc.public.secret.ListSecretsRequest\x1a-.textql.rpc.public.secret.ListSecretsResponse"\x03\x90\x02\x01\x12\x8d\x01\n\x15GetMembersWithSecrets\x126.textql.rpc.public.secret.GetMembersWithSecretsRequest\x1a7.textql.rpc.public.secret.GetMembersWithSecretsResponse"\x03\x90\x02\x01\x12d\n\tPutSecret\x12*.textql.rpc.public.secret.PutSecretRequest\x1a+.textql.rpc.public.secret.PutSecretResponse\x12m\n\x0cUpdateSecret\x12-.textql.rpc.public.secret.UpdateSecretRequest\x1a..textql.rpc.public.secret.UpdateSecretResponse\x12m\n\x0cDeleteSecret\x12-.textql.rpc.public.secret.DeleteSecretRequest\x1a..textql.rpc.public.secret.DeleteSecretResponse\x12\x8e\x01\n\x11CreateApiRevision\x122.textql.rpc.public.secret.CreateApiRevisionRequest\x1a3.textql.rpc.public.secret.CreateApiRevisionResponse"\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL\x12\x91\x01\n\x12UpsertApiAccessKey\x123.textql.rpc.public.secret.UpsertApiAccessKeyRequest\x1a4.textql.rpc.public.secret.UpsertApiAccessKeyResponse"\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL\x12\x8e\x01\n\x11DeleteApiRevision\x122.textql.rpc.public.secret.DeleteApiRevisionRequest\x1a3.textql.rpc.public.secret.DeleteApiRevisionResponse"\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL\x12\x91\x01\n\x11ListApiAccessKeys\x122.textql.rpc.public.secret.ListApiAccessKeysRequest\x1a3.textql.rpc.public.secret.ListApiAccessKeysResponse"\x13\x90\x02\x01\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL\x12\x8b\x01\n\x0fGetApiAccessKey\x120.textql.rpc.public.secret.GetApiAccessKeyRequest\x1a1.textql.rpc.public.secret.GetApiAccessKeyResponse"\x13\x90\x02\x01\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL\x12\x91\x01\n\x12DeleteApiAccessKey\x123.textql.rpc.public.secret.DeleteApiAccessKeyRequest\x1a4.textql.rpc.public.secret.DeleteApiAccessKeyResponse"\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL\x12\x8e\x01\n\x10ListApiProviders\x121.textql.rpc.public.secret.ListApiProvidersRequest\x1a2.textql.rpc.public.secret.ListApiProvidersResponse"\x13\x90\x02\x01\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL\x12\x8e\x01\n\x10TestApiAccessKey\x121.textql.rpc.public.secret.TestApiAccessKeyRequest\x1a2.textql.rpc.public.secret.TestApiAccessKeyResponse"\x13\x90\x02\x02\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL\x12\xac\x01\n\x1bMigrateSecretToApiConnector\x12<.textql.rpc.public.secret.MigrateSecretToApiConnectorRequest\x1a=.textql.rpc.public.secret.MigrateSecretToApiConnectorResponse"\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNALb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.secret_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_APIACCESSKEY_HEADERSENTRY']._loaded_options = None
    _globals['_APIACCESSKEY_HEADERSENTRY']._serialized_options = b'8\x01'
    _globals['_APIACCESSKEY_QUERYPARAMSENTRY']._loaded_options = None
    _globals['_APIACCESSKEY_QUERYPARAMSENTRY']._serialized_options = b'8\x01'
    _globals['_APIACCESSKEY_BODYENTRY']._loaded_options = None
    _globals['_APIACCESSKEY_BODYENTRY']._serialized_options = b'8\x01'
    _globals['_UPSERTAPIACCESSKEYREQUEST_HEADERSENTRY']._loaded_options = None
    _globals['_UPSERTAPIACCESSKEYREQUEST_HEADERSENTRY']._serialized_options = b'8\x01'
    _globals['_UPSERTAPIACCESSKEYREQUEST_QUERYPARAMSENTRY']._loaded_options = None
    _globals['_UPSERTAPIACCESSKEYREQUEST_QUERYPARAMSENTRY']._serialized_options = b'8\x01'
    _globals['_UPSERTAPIACCESSKEYREQUEST_BODYENTRY']._loaded_options = None
    _globals['_UPSERTAPIACCESSKEYREQUEST_BODYENTRY']._serialized_options = b'8\x01'
    _globals['_SECRETSERVICE'].methods_by_name['ListSecrets']._loaded_options = None
    _globals['_SECRETSERVICE'].methods_by_name['ListSecrets']._serialized_options = b'\x90\x02\x01'
    _globals['_SECRETSERVICE'].methods_by_name['GetMembersWithSecrets']._loaded_options = None
    _globals['_SECRETSERVICE'].methods_by_name['GetMembersWithSecrets']._serialized_options = b'\x90\x02\x01'
    _globals['_SECRETSERVICE'].methods_by_name['CreateApiRevision']._loaded_options = None
    _globals['_SECRETSERVICE'].methods_by_name['CreateApiRevision']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_SECRETSERVICE'].methods_by_name['UpsertApiAccessKey']._loaded_options = None
    _globals['_SECRETSERVICE'].methods_by_name['UpsertApiAccessKey']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_SECRETSERVICE'].methods_by_name['DeleteApiRevision']._loaded_options = None
    _globals['_SECRETSERVICE'].methods_by_name['DeleteApiRevision']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_SECRETSERVICE'].methods_by_name['ListApiAccessKeys']._loaded_options = None
    _globals['_SECRETSERVICE'].methods_by_name['ListApiAccessKeys']._serialized_options = b'\x90\x02\x01\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_SECRETSERVICE'].methods_by_name['GetApiAccessKey']._loaded_options = None
    _globals['_SECRETSERVICE'].methods_by_name['GetApiAccessKey']._serialized_options = b'\x90\x02\x01\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_SECRETSERVICE'].methods_by_name['DeleteApiAccessKey']._loaded_options = None
    _globals['_SECRETSERVICE'].methods_by_name['DeleteApiAccessKey']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_SECRETSERVICE'].methods_by_name['ListApiProviders']._loaded_options = None
    _globals['_SECRETSERVICE'].methods_by_name['ListApiProviders']._serialized_options = b'\x90\x02\x01\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_SECRETSERVICE'].methods_by_name['TestApiAccessKey']._loaded_options = None
    _globals['_SECRETSERVICE'].methods_by_name['TestApiAccessKey']._serialized_options = b'\x90\x02\x02\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_SECRETSERVICE'].methods_by_name['MigrateSecretToApiConnector']._loaded_options = None
    _globals['_SECRETSERVICE'].methods_by_name['MigrateSecretToApiConnector']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_BODYCONTENTTYPE']._serialized_start = 6368
    _globals['_BODYCONTENTTYPE']._serialized_end = 6469
    _globals['_SECRET']._serialized_start = 135
    _globals['_SECRET']._serialized_end = 500
    _globals['_LISTSECRETSREQUEST']._serialized_start = 502
    _globals['_LISTSECRETSREQUEST']._serialized_end = 522
    _globals['_LISTSECRETSRESPONSE']._serialized_start = 524
    _globals['_LISTSECRETSRESPONSE']._serialized_end = 605
    _globals['_PUTSECRETREQUEST']._serialized_start = 608
    _globals['_PUTSECRETREQUEST']._serialized_end = 788
    _globals['_PUTSECRETRESPONSE']._serialized_start = 790
    _globals['_PUTSECRETRESPONSE']._serialized_end = 809
    _globals['_UPDATESECRETREQUEST']._serialized_start = 812
    _globals['_UPDATESECRETREQUEST']._serialized_end = 979
    _globals['_UPDATESECRETRESPONSE']._serialized_start = 981
    _globals['_UPDATESECRETRESPONSE']._serialized_end = 1003
    _globals['_DELETESECRETREQUEST']._serialized_start = 1005
    _globals['_DELETESECRETREQUEST']._serialized_end = 1046
    _globals['_DELETESECRETRESPONSE']._serialized_start = 1048
    _globals['_DELETESECRETRESPONSE']._serialized_end = 1070
    _globals['_GETMEMBERSWITHSECRETSREQUEST']._serialized_start = 1072
    _globals['_GETMEMBERSWITHSECRETSREQUEST']._serialized_end = 1102
    _globals['_GETMEMBERSWITHSECRETSRESPONSE']._serialized_start = 1104
    _globals['_GETMEMBERSWITHSECRETSRESPONSE']._serialized_end = 1197
    _globals['_HTTPBASICAUTH']._serialized_start = 1199
    _globals['_HTTPBASICAUTH']._serialized_end = 1270
    _globals['_APIACCESSREF']._serialized_start = 1272
    _globals['_APIACCESSREF']._serialized_end = 1357
    _globals['_APIACCESSKEY']._serialized_start = 1360
    _globals['_APIACCESSKEY']._serialized_end = 2671
    _globals['_APIACCESSKEY_HEADERSENTRY']._serialized_start = 2441
    _globals['_APIACCESSKEY_HEADERSENTRY']._serialized_end = 2499
    _globals['_APIACCESSKEY_QUERYPARAMSENTRY']._serialized_start = 2501
    _globals['_APIACCESSKEY_QUERYPARAMSENTRY']._serialized_end = 2563
    _globals['_APIACCESSKEY_BODYENTRY']._serialized_start = 2565
    _globals['_APIACCESSKEY_BODYENTRY']._serialized_end = 2620
    _globals['_CREATEAPIREVISIONREQUEST']._serialized_start = 2673
    _globals['_CREATEAPIREVISIONREQUEST']._serialized_end = 2769
    _globals['_CREATEAPIREVISIONRESPONSE']._serialized_start = 2772
    _globals['_CREATEAPIREVISIONRESPONSE']._serialized_end = 2959
    _globals['_UPSERTAPIACCESSKEYREQUEST']._serialized_start = 2962
    _globals['_UPSERTAPIACCESSKEYREQUEST']._serialized_end = 4040
    _globals['_UPSERTAPIACCESSKEYREQUEST_HEADERSENTRY']._serialized_start = 2441
    _globals['_UPSERTAPIACCESSKEYREQUEST_HEADERSENTRY']._serialized_end = 2499
    _globals['_UPSERTAPIACCESSKEYREQUEST_QUERYPARAMSENTRY']._serialized_start = 2501
    _globals['_UPSERTAPIACCESSKEYREQUEST_QUERYPARAMSENTRY']._serialized_end = 2563
    _globals['_UPSERTAPIACCESSKEYREQUEST_BODYENTRY']._serialized_start = 2565
    _globals['_UPSERTAPIACCESSKEYREQUEST_BODYENTRY']._serialized_end = 2620
    _globals['_UPSERTAPIACCESSKEYRESPONSE']._serialized_start = 4042
    _globals['_UPSERTAPIACCESSKEYRESPONSE']._serialized_end = 4148
    _globals['_DELETEAPIREVISIONREQUEST']._serialized_start = 4150
    _globals['_DELETEAPIREVISIONREQUEST']._serialized_end = 4234
    _globals['_DELETEAPIREVISIONRESPONSE']._serialized_start = 4236
    _globals['_DELETEAPIREVISIONRESPONSE']._serialized_end = 4263
    _globals['_LISTAPIACCESSKEYSREQUEST']._serialized_start = 4265
    _globals['_LISTAPIACCESSKEYSREQUEST']._serialized_end = 4291
    _globals['_LISTAPIACCESSKEYSRESPONSE']._serialized_start = 4293
    _globals['_LISTAPIACCESSKEYSRESPONSE']._serialized_end = 4400
    _globals['_GETAPIACCESSKEYREQUEST']._serialized_start = 4402
    _globals['_GETAPIACCESSKEYREQUEST']._serialized_end = 4442
    _globals['_GETAPIACCESSKEYRESPONSE']._serialized_start = 4444
    _globals['_GETAPIACCESSKEYRESPONSE']._serialized_end = 4547
    _globals['_DELETEAPIACCESSKEYREQUEST']._serialized_start = 4549
    _globals['_DELETEAPIACCESSKEYREQUEST']._serialized_end = 4592
    _globals['_DELETEAPIACCESSKEYRESPONSE']._serialized_start = 4594
    _globals['_DELETEAPIACCESSKEYRESPONSE']._serialized_end = 4622
    _globals['_ENVVARFIELD']._serialized_start = 4625
    _globals['_ENVVARFIELD']._serialized_end = 4808
    _globals['_APIPROVIDER']._serialized_start = 4811
    _globals['_APIPROVIDER']._serialized_end = 5668
    _globals['_TESTAPIACCESSKEYREQUEST']._serialized_start = 5670
    _globals['_TESTAPIACCESSKEYREQUEST']._serialized_end = 5753
    _globals['_TESTAPIACCESSKEYRESPONSE']._serialized_start = 5755
    _globals['_TESTAPIACCESSKEYRESPONSE']._serialized_end = 5866
    _globals['_LISTAPIPROVIDERSREQUEST']._serialized_start = 5868
    _globals['_LISTAPIPROVIDERSREQUEST']._serialized_end = 5893
    _globals['_LISTAPIPROVIDERSRESPONSE']._serialized_start = 5895
    _globals['_LISTAPIPROVIDERSRESPONSE']._serialized_end = 5990
    _globals['_MIGRATESECRETTOAPICONNECTORREQUEST']._serialized_start = 5993
    _globals['_MIGRATESECRETTOAPICONNECTORREQUEST']._serialized_end = 6249
    _globals['_MIGRATESECRETTOAPICONNECTORRESPONSE']._serialized_start = 6251
    _globals['_MIGRATESECRETTOAPICONNECTORRESPONSE']._serialized_end = 6366
    _globals['_SECRETSERVICE']._serialized_start = 6472
    _globals['_SECRETSERVICE']._serialized_end = 8409