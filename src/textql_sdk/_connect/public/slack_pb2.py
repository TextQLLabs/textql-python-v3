# pylint: skip-file
# mypy: ignore-errors
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/slack.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ..public import cells_pb2 as public_dot_cells__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12public/slack.proto\x12\x17textql.rpc.public.slack\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x12public/cells.proto"/\n\x14SyncWorkspaceRequest\x12\x17\n\x07team_id\x18\x01 \x01(\tR\x06teamId"I\n\x15SyncWorkspaceResponse\x12\x16\n\x06queued\x18\x01 \x01(\x08R\x06queued\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message"h\n\x19ListInstallationsResponse\x12K\n\rinstallations\x18\x01 \x03(\x0b2%.textql.rpc.public.slack.InstallationR\rinstallations"\x84\x01\n\x0cInstallation\x12\x17\n\x07team_id\x18\x01 \x01(\tR\x06teamId\x129\n\ncreated_at\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt\x12\x17\n\x04name\x18\x03 \x01(\tH\x00R\x04name\x88\x01\x01B\x07\n\x05_name"^\n\x16GetCurrentUserResponse\x12;\n\x04user\x18\x01 \x01(\x0b2".textql.rpc.public.slack.SlackUserH\x00R\x04user\x88\x01\x01B\x07\n\x05_user"\x92\x01\n\tSlackUser\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x17\n\x04name\x18\x02 \x01(\tH\x00R\x04name\x88\x01\x01\x12 \n\treal_name\x18\x03 \x01(\tH\x01R\x08realName\x88\x01\x01\x12\x19\n\x05email\x18\x04 \x01(\tH\x02R\x05email\x88\x01\x01B\x07\n\x05_nameB\x0c\n\n_real_nameB\x08\n\x06_email"\\\n\x14ListChannelsResponse\x12D\n\x08channels\x18\x01 \x03(\x0b2(.textql.rpc.public.cells.SlackChannelRefR\x08channels"P\n\x11ListUsersResponse\x12;\n\x05users\x18\x01 \x03(\x0b2%.textql.rpc.public.cells.SlackUserRefR\x05users"4\n\x19DeleteInstallationRequest\x12\x17\n\x07team_id\x18\x01 \x01(\tR\x06teamId"-\n\x17CreateSlackUuidResponse\x12\x12\n\x04uuid\x18\x01 \x01(\tR\x04uuid"K\n\x1fHandleSlackOAuthCallbackRequest\x12\x12\n\x04code\x18\x01 \x01(\tR\x04code\x12\x14\n\x05state\x18\x02 \x01(\tR\x05state"\xa2\x01\n HandleSlackOAuthCallbackResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12(\n\rerror_message\x18\x02 \x01(\tH\x00R\x0cerrorMessage\x88\x01\x01\x12\x1c\n\x07team_id\x18\x03 \x01(\tH\x01R\x06teamId\x88\x01\x01B\x10\n\x0e_error_messageB\n\n\x08_team_id2\xb3\x06\n\x0cSlackService\x12n\n\rSyncWorkspace\x12-.textql.rpc.public.slack.SyncWorkspaceRequest\x1a..textql.rpc.public.slack.SyncWorkspaceResponse\x12_\n\x11ListInstallations\x12\x16.google.protobuf.Empty\x1a2.textql.rpc.public.slack.ListInstallationsResponse\x12Y\n\x0eGetCurrentUser\x12\x16.google.protobuf.Empty\x1a/.textql.rpc.public.slack.GetCurrentUserResponse\x12U\n\x0cListChannels\x12\x16.google.protobuf.Empty\x1a-.textql.rpc.public.slack.ListChannelsResponse\x12O\n\tListUsers\x12\x16.google.protobuf.Empty\x1a*.textql.rpc.public.slack.ListUsersResponse\x12`\n\x12DeleteInstallation\x122.textql.rpc.public.slack.DeleteInstallationRequest\x1a\x16.google.protobuf.Empty\x12[\n\x0fCreateSlackUuid\x12\x16.google.protobuf.Empty\x1a0.textql.rpc.public.slack.CreateSlackUuidResponse\x12\x8f\x01\n\x18HandleSlackOAuthCallback\x128.textql.rpc.public.slack.HandleSlackOAuthCallbackRequest\x1a9.textql.rpc.public.slack.HandleSlackOAuthCallbackResponseb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.slack_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_SYNCWORKSPACEREQUEST']._serialized_start = 129
    _globals['_SYNCWORKSPACEREQUEST']._serialized_end = 176
    _globals['_SYNCWORKSPACERESPONSE']._serialized_start = 178
    _globals['_SYNCWORKSPACERESPONSE']._serialized_end = 251
    _globals['_LISTINSTALLATIONSRESPONSE']._serialized_start = 253
    _globals['_LISTINSTALLATIONSRESPONSE']._serialized_end = 357
    _globals['_INSTALLATION']._serialized_start = 360
    _globals['_INSTALLATION']._serialized_end = 492
    _globals['_GETCURRENTUSERRESPONSE']._serialized_start = 494
    _globals['_GETCURRENTUSERRESPONSE']._serialized_end = 588
    _globals['_SLACKUSER']._serialized_start = 591
    _globals['_SLACKUSER']._serialized_end = 737
    _globals['_LISTCHANNELSRESPONSE']._serialized_start = 739
    _globals['_LISTCHANNELSRESPONSE']._serialized_end = 831
    _globals['_LISTUSERSRESPONSE']._serialized_start = 833
    _globals['_LISTUSERSRESPONSE']._serialized_end = 913
    _globals['_DELETEINSTALLATIONREQUEST']._serialized_start = 915
    _globals['_DELETEINSTALLATIONREQUEST']._serialized_end = 967
    _globals['_CREATESLACKUUIDRESPONSE']._serialized_start = 969
    _globals['_CREATESLACKUUIDRESPONSE']._serialized_end = 1014
    _globals['_HANDLESLACKOAUTHCALLBACKREQUEST']._serialized_start = 1016
    _globals['_HANDLESLACKOAUTHCALLBACKREQUEST']._serialized_end = 1091
    _globals['_HANDLESLACKOAUTHCALLBACKRESPONSE']._serialized_start = 1094
    _globals['_HANDLESLACKOAUTHCALLBACKRESPONSE']._serialized_end = 1256
    _globals['_SLACKSERVICE']._serialized_start = 1259
    _globals['_SLACKSERVICE']._serialized_end = 2078