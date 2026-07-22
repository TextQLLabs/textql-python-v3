"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/scim.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11public/scim.proto\x12\x16textql.rpc.public.scim\x1a\x1fgoogle/protobuf/timestamp.proto"\xb5\x02\n\tScimToken\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12 \n\x0bdescription\x18\x02 \x01(\tR\x0bdescription\x12\x1d\n\ncreated_by\x18\x03 \x01(\tR\tcreatedBy\x12>\n\nexpires_at\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00R\texpiresAt\x88\x01\x01\x12>\n\nrevoked_at\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampH\x01R\trevokedAt\x88\x01\x01\x129\n\ncreated_at\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAtB\r\n\x0b_expires_atB\r\n\x0b_revoked_at"\xd8\x02\n\x0fScimOAuthClient\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1b\n\tclient_id\x18\x02 \x01(\tR\x08clientId\x12 \n\x0bdescription\x18\x03 \x01(\tR\x0bdescription\x12\x1d\n\ncreated_by\x18\x04 \x01(\tR\tcreatedBy\x12>\n\nexpires_at\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00R\texpiresAt\x88\x01\x01\x12>\n\nrevoked_at\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampH\x01R\trevokedAt\x88\x01\x01\x129\n\ncreated_at\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAtB\r\n\x0b_expires_atB\r\n\x0b_revoked_at"{\n\x16CreateScimTokenRequest\x12 \n\x0bdescription\x18\x01 \x01(\tR\x0bdescription\x12+\n\x0fexpires_in_days\x18\x02 \x01(\x05H\x00R\rexpiresInDays\x88\x01\x01B\x12\n\x10_expires_in_days"\xeb\x01\n\x17CreateScimTokenResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x14\n\x05token\x18\x02 \x01(\tR\x05token\x12 \n\x0bdescription\x18\x03 \x01(\tR\x0bdescription\x12>\n\nexpires_at\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00R\texpiresAt\x88\x01\x01\x129\n\ncreated_at\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAtB\r\n\x0b_expires_at"\x17\n\x15ListScimTokensRequest"S\n\x16ListScimTokensResponse\x129\n\x06tokens\x18\x01 \x03(\x0b2!.textql.rpc.public.scim.ScimTokenR\x06tokens"(\n\x16RevokeScimTokenRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x19\n\x17RevokeScimTokenResponse"\x81\x01\n\x1cCreateScimOAuthClientRequest\x12 \n\x0bdescription\x18\x01 \x01(\tR\x0bdescription\x12+\n\x0fexpires_in_days\x18\x02 \x01(\x05H\x00R\rexpiresInDays\x88\x01\x01B\x12\n\x10_expires_in_days"\x9d\x02\n\x1dCreateScimOAuthClientResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1b\n\tclient_id\x18\x02 \x01(\tR\x08clientId\x12#\n\rclient_secret\x18\x03 \x01(\tR\x0cclientSecret\x12 \n\x0bdescription\x18\x04 \x01(\tR\x0bdescription\x12>\n\nexpires_at\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00R\texpiresAt\x88\x01\x01\x129\n\ncreated_at\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAtB\r\n\x0b_expires_at"\x1d\n\x1bListScimOAuthClientsRequest"a\n\x1cListScimOAuthClientsResponse\x12A\n\x07clients\x18\x01 \x03(\x0b2\'.textql.rpc.public.scim.ScimOAuthClientR\x07clients".\n\x1cRevokeScimOAuthClientRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x1f\n\x1dRevokeScimOAuthClientResponse2\x82\x06\n\x0bScimService\x12r\n\x0fCreateScimToken\x12..textql.rpc.public.scim.CreateScimTokenRequest\x1a/.textql.rpc.public.scim.CreateScimTokenResponse\x12t\n\x0eListScimTokens\x12-.textql.rpc.public.scim.ListScimTokensRequest\x1a..textql.rpc.public.scim.ListScimTokensResponse"\x03\x90\x02\x01\x12r\n\x0fRevokeScimToken\x12..textql.rpc.public.scim.RevokeScimTokenRequest\x1a/.textql.rpc.public.scim.RevokeScimTokenResponse\x12\x84\x01\n\x15CreateScimOAuthClient\x124.textql.rpc.public.scim.CreateScimOAuthClientRequest\x1a5.textql.rpc.public.scim.CreateScimOAuthClientResponse\x12\x86\x01\n\x14ListScimOAuthClients\x123.textql.rpc.public.scim.ListScimOAuthClientsRequest\x1a4.textql.rpc.public.scim.ListScimOAuthClientsResponse"\x03\x90\x02\x01\x12\x84\x01\n\x15RevokeScimOAuthClient\x124.textql.rpc.public.scim.RevokeScimOAuthClientRequest\x1a5.textql.rpc.public.scim.RevokeScimOAuthClientResponseb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.scim_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_SCIMSERVICE'].methods_by_name['ListScimTokens']._loaded_options = None
    _globals['_SCIMSERVICE'].methods_by_name['ListScimTokens']._serialized_options = b'\x90\x02\x01'
    _globals['_SCIMSERVICE'].methods_by_name['ListScimOAuthClients']._loaded_options = None
    _globals['_SCIMSERVICE'].methods_by_name['ListScimOAuthClients']._serialized_options = b'\x90\x02\x01'
    _globals['_SCIMTOKEN']._serialized_start = 79
    _globals['_SCIMTOKEN']._serialized_end = 388
    _globals['_SCIMOAUTHCLIENT']._serialized_start = 391
    _globals['_SCIMOAUTHCLIENT']._serialized_end = 735
    _globals['_CREATESCIMTOKENREQUEST']._serialized_start = 737
    _globals['_CREATESCIMTOKENREQUEST']._serialized_end = 860
    _globals['_CREATESCIMTOKENRESPONSE']._serialized_start = 863
    _globals['_CREATESCIMTOKENRESPONSE']._serialized_end = 1098
    _globals['_LISTSCIMTOKENSREQUEST']._serialized_start = 1100
    _globals['_LISTSCIMTOKENSREQUEST']._serialized_end = 1123
    _globals['_LISTSCIMTOKENSRESPONSE']._serialized_start = 1125
    _globals['_LISTSCIMTOKENSRESPONSE']._serialized_end = 1208
    _globals['_REVOKESCIMTOKENREQUEST']._serialized_start = 1210
    _globals['_REVOKESCIMTOKENREQUEST']._serialized_end = 1250
    _globals['_REVOKESCIMTOKENRESPONSE']._serialized_start = 1252
    _globals['_REVOKESCIMTOKENRESPONSE']._serialized_end = 1277
    _globals['_CREATESCIMOAUTHCLIENTREQUEST']._serialized_start = 1280
    _globals['_CREATESCIMOAUTHCLIENTREQUEST']._serialized_end = 1409
    _globals['_CREATESCIMOAUTHCLIENTRESPONSE']._serialized_start = 1412
    _globals['_CREATESCIMOAUTHCLIENTRESPONSE']._serialized_end = 1697
    _globals['_LISTSCIMOAUTHCLIENTSREQUEST']._serialized_start = 1699
    _globals['_LISTSCIMOAUTHCLIENTSREQUEST']._serialized_end = 1728
    _globals['_LISTSCIMOAUTHCLIENTSRESPONSE']._serialized_start = 1730
    _globals['_LISTSCIMOAUTHCLIENTSRESPONSE']._serialized_end = 1827
    _globals['_REVOKESCIMOAUTHCLIENTREQUEST']._serialized_start = 1829
    _globals['_REVOKESCIMOAUTHCLIENTREQUEST']._serialized_end = 1875
    _globals['_REVOKESCIMOAUTHCLIENTRESPONSE']._serialized_start = 1877
    _globals['_REVOKESCIMOAUTHCLIENTRESPONSE']._serialized_end = 1908
    _globals['_SCIMSERVICE']._serialized_start = 1911
    _globals['_SCIMSERVICE']._serialized_end = 2681