# pylint: skip-file
# mypy: ignore-errors
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/teams.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ..public import cells_pb2 as public_dot_cells__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12public/teams.proto\x12\x17textql.rpc.public.teams\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x12public/cells.proto"8\n\x19TeamsSyncWorkspaceRequest\x12\x1b\n\ttenant_id\x18\x01 \x01(\tR\x08tenantId"N\n\x1aTeamsSyncWorkspaceResponse\x12\x16\n\x06queued\x18\x01 \x01(\x08R\x06queued\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message"r\n\x1eTeamsListInstallationsResponse\x12P\n\rinstallations\x18\x01 \x03(\x0b2*.textql.rpc.public.teams.TeamsInstallationR\rinstallations"\x8d\x01\n\x11TeamsInstallation\x12\x1b\n\ttenant_id\x18\x01 \x01(\tR\x08tenantId\x129\n\ncreated_at\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt\x12\x17\n\x04name\x18\x03 \x01(\tH\x00R\x04name\x88\x01\x01B\x07\n\x05_name"c\n\x1bTeamsGetCurrentUserResponse\x12;\n\x04user\x18\x01 \x01(\x0b2".textql.rpc.public.teams.TeamsUserH\x00R\x04user\x88\x01\x01B\x07\n\x05_user"b\n\tTeamsUser\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x17\n\x04name\x18\x02 \x01(\tH\x00R\x04name\x88\x01\x01\x12\x19\n\x05email\x18\x03 \x01(\tH\x01R\x05email\x88\x01\x01B\x07\n\x05_nameB\x08\n\x06_email"a\n\x19TeamsListChannelsResponse\x12D\n\x08channels\x18\x01 \x03(\x0b2(.textql.rpc.public.cells.TeamsChannelRefR\x08channels"U\n\x16TeamsListUsersResponse\x12;\n\x05users\x18\x01 \x03(\x0b2%.textql.rpc.public.cells.TeamsUserRefR\x05users"=\n\x1eTeamsDeleteInstallationRequest\x12\x1b\n\ttenant_id\x18\x01 \x01(\tR\x08tenantId"-\n\x17CreateTeamsUuidResponse\x12\x12\n\x04uuid\x18\x01 \x01(\tR\x04uuid"K\n\x1fHandleTeamsOAuthCallbackRequest\x12\x12\n\x04code\x18\x01 \x01(\tR\x04code\x12\x14\n\x05state\x18\x02 \x01(\tR\x05state"\xa8\x01\n HandleTeamsOAuthCallbackResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12(\n\rerror_message\x18\x02 \x01(\tH\x00R\x0cerrorMessage\x88\x01\x01\x12 \n\ttenant_id\x18\x03 \x01(\tH\x01R\x08tenantId\x88\x01\x01B\x10\n\x0e_error_messageB\x0c\n\n_tenant_id2\xd6\x06\n\x0cTeamsService\x12x\n\rSyncWorkspace\x122.textql.rpc.public.teams.TeamsSyncWorkspaceRequest\x1a3.textql.rpc.public.teams.TeamsSyncWorkspaceResponse\x12d\n\x11ListInstallations\x12\x16.google.protobuf.Empty\x1a7.textql.rpc.public.teams.TeamsListInstallationsResponse\x12^\n\x0eGetCurrentUser\x12\x16.google.protobuf.Empty\x1a4.textql.rpc.public.teams.TeamsGetCurrentUserResponse\x12Z\n\x0cListChannels\x12\x16.google.protobuf.Empty\x1a2.textql.rpc.public.teams.TeamsListChannelsResponse\x12T\n\tListUsers\x12\x16.google.protobuf.Empty\x1a/.textql.rpc.public.teams.TeamsListUsersResponse\x12e\n\x12DeleteInstallation\x127.textql.rpc.public.teams.TeamsDeleteInstallationRequest\x1a\x16.google.protobuf.Empty\x12[\n\x0fCreateTeamsUuid\x12\x16.google.protobuf.Empty\x1a0.textql.rpc.public.teams.CreateTeamsUuidResponse\x12\x8f\x01\n\x18HandleTeamsOAuthCallback\x128.textql.rpc.public.teams.HandleTeamsOAuthCallbackRequest\x1a9.textql.rpc.public.teams.HandleTeamsOAuthCallbackResponseb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.teams_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_TEAMSSYNCWORKSPACEREQUEST']._serialized_start = 129
    _globals['_TEAMSSYNCWORKSPACEREQUEST']._serialized_end = 185
    _globals['_TEAMSSYNCWORKSPACERESPONSE']._serialized_start = 187
    _globals['_TEAMSSYNCWORKSPACERESPONSE']._serialized_end = 265
    _globals['_TEAMSLISTINSTALLATIONSRESPONSE']._serialized_start = 267
    _globals['_TEAMSLISTINSTALLATIONSRESPONSE']._serialized_end = 381
    _globals['_TEAMSINSTALLATION']._serialized_start = 384
    _globals['_TEAMSINSTALLATION']._serialized_end = 525
    _globals['_TEAMSGETCURRENTUSERRESPONSE']._serialized_start = 527
    _globals['_TEAMSGETCURRENTUSERRESPONSE']._serialized_end = 626
    _globals['_TEAMSUSER']._serialized_start = 628
    _globals['_TEAMSUSER']._serialized_end = 726
    _globals['_TEAMSLISTCHANNELSRESPONSE']._serialized_start = 728
    _globals['_TEAMSLISTCHANNELSRESPONSE']._serialized_end = 825
    _globals['_TEAMSLISTUSERSRESPONSE']._serialized_start = 827
    _globals['_TEAMSLISTUSERSRESPONSE']._serialized_end = 912
    _globals['_TEAMSDELETEINSTALLATIONREQUEST']._serialized_start = 914
    _globals['_TEAMSDELETEINSTALLATIONREQUEST']._serialized_end = 975
    _globals['_CREATETEAMSUUIDRESPONSE']._serialized_start = 977
    _globals['_CREATETEAMSUUIDRESPONSE']._serialized_end = 1022
    _globals['_HANDLETEAMSOAUTHCALLBACKREQUEST']._serialized_start = 1024
    _globals['_HANDLETEAMSOAUTHCALLBACKREQUEST']._serialized_end = 1099
    _globals['_HANDLETEAMSOAUTHCALLBACKRESPONSE']._serialized_start = 1102
    _globals['_HANDLETEAMSOAUTHCALLBACKRESPONSE']._serialized_end = 1270
    _globals['_TEAMSSERVICE']._serialized_start = 1273
    _globals['_TEAMSSERVICE']._serialized_end = 2127