"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/notifications.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ..public import options_pb2 as public_dot_options__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1apublic/notifications.proto\x12\x1ftextql.rpc.public.notifications\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14public/options.proto"\xa1\x02\n\x0cNotification\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12^\n\x11notification_type\x18\x02 \x01(\x0e21.textql.rpc.public.notifications.NotificationTypeR\x10notificationType\x121\n\x07context\x18\x03 \x01(\x0b2\x17.google.protobuf.StructR\x07context\x129\n\ncreated_at\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt\x123\n\x07read_at\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampR\x06readAt"\x89\x01\n\x11NotificationEvent\x12Q\n\x0cnotification\x18\x01 \x01(\x0b2-.textql.rpc.public.notifications.NotificationR\x0cnotification\x12!\n\x0cunread_count\x18\x02 \x01(\x05R\x0bunreadCount"m\n\x17GetNotificationsRequest\x12\x1f\n\x0bunread_only\x18\x01 \x01(\x08R\nunreadOnly\x12\x14\n\x05limit\x18\x02 \x01(\x05R\x05limit\x12\x1b\n\tbefore_id\x18\x03 \x01(\tR\x08beforeId"\x92\x01\n\x18GetNotificationsResponse\x12S\n\rnotifications\x18\x01 \x03(\x0b2-.textql.rpc.public.notifications.NotificationR\rnotifications\x12!\n\x0cunread_count\x18\x02 \x01(\x05R\x0bunreadCount"F\n\x1bMarkNotificationReadRequest\x12\'\n\x0fnotification_id\x18\x01 \x01(\tR\x0enotificationId"\xdc\x01\n\x10NotificationRule\x12^\n\x11notification_type\x18\x01 \x01(\x0e21.textql.rpc.public.notifications.NotificationTypeR\x10notificationType\x12N\n\x07channel\x18\x02 \x01(\x0e24.textql.rpc.public.notifications.NotificationChannelR\x07channel\x12\x18\n\x07enabled\x18\x03 \x01(\x08R\x07enabled"\xb6\x01\n\x1cGetNotificationRulesResponse\x12G\n\x05rules\x18\x01 \x03(\x0b21.textql.rpc.public.notifications.NotificationRuleR\x05rules\x12M\n\x08defaults\x18\x02 \x03(\x0b21.textql.rpc.public.notifications.NotificationRuleR\x08defaults"\xe9\x01\n\x1dUpsertNotificationRuleRequest\x12^\n\x11notification_type\x18\x01 \x01(\x0e21.textql.rpc.public.notifications.NotificationTypeR\x10notificationType\x12N\n\x07channel\x18\x02 \x01(\x0e24.textql.rpc.public.notifications.NotificationChannelR\x07channel\x12\x18\n\x07enabled\x18\x03 \x01(\x08R\x07enabled"f\n\rAlertAudience\x12\x1d\n\nmember_ids\x18\x01 \x03(\tR\tmemberIds\x12\x1d\n\nrole_names\x18\x02 \x03(\tR\troleNames\x12\x17\n\x07all_org\x18\x03 \x01(\x08R\x06allOrg"\xa9\x06\n\tBroadcast\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x14\n\x05title\x18\x02 \x01(\tR\x05title\x12\x12\n\x04body\x18\x03 \x01(\tR\x04body\x12\x1a\n\x08category\x18\x04 \x01(\tR\x08category\x12\x1b\n\tdeep_link\x18\x05 \x01(\tR\x08deepLink\x12!\n\x0caction_label\x18\x06 \x01(\tR\x0bactionLabel\x12\x1d\n\naction_url\x18\x07 \x01(\tR\tactionUrl\x12J\n\x08audience\x18\x08 \x01(\x0b2..textql.rpc.public.notifications.AlertAudienceR\x08audience\x12T\n\x08metadata\x18\t \x03(\x0b28.textql.rpc.public.notifications.Broadcast.MetadataEntryR\x08metadata\x12$\n\x0etarget_org_ids\x18\n \x03(\tR\x0ctargetOrgIds\x12\x19\n\x08all_orgs\x18\x0b \x01(\x08R\x07allOrgs\x12=\n\x0cscheduled_at\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampR\x0bscheduledAt\x12H\n\x06status\x18\r \x01(\x0e20.textql.rpc.public.notifications.BroadcastStatusR\x06status\x12\x1d\n\ncreated_by\x18\x0e \x01(\tR\tcreatedBy\x129\n\ncreated_at\x18\x0f \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt\x12?\n\rdispatched_at\x18\x10 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0cdispatchedAt\x12#\n\rorgs_targeted\x18\x11 \x01(\x05R\x0corgsTargeted\x1a;\n\rMetadataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01"\xa9\x04\n\x16CreateBroadcastRequest\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12\x12\n\x04body\x18\x02 \x01(\tR\x04body\x12\x1a\n\x08category\x18\x03 \x01(\tR\x08category\x12\x1b\n\tdeep_link\x18\x04 \x01(\tR\x08deepLink\x12!\n\x0caction_label\x18\x05 \x01(\tR\x0bactionLabel\x12\x1d\n\naction_url\x18\x06 \x01(\tR\tactionUrl\x12J\n\x08audience\x18\x07 \x01(\x0b2..textql.rpc.public.notifications.AlertAudienceR\x08audience\x12a\n\x08metadata\x18\x08 \x03(\x0b2E.textql.rpc.public.notifications.CreateBroadcastRequest.MetadataEntryR\x08metadata\x12$\n\x0etarget_org_ids\x18\n \x03(\tR\x0ctargetOrgIds\x12\x19\n\x08all_orgs\x18\x0b \x01(\x08R\x07allOrgs\x12=\n\x0cscheduled_at\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampR\x0bscheduledAt\x1a;\n\rMetadataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01"\x98\x01\n\x15ListBroadcastsRequest\x12\x14\n\x05limit\x18\x01 \x01(\x05R\x05limit\x12\x1b\n\tbefore_id\x18\x02 \x01(\tR\x08beforeId\x12L\n\x08statuses\x18\x03 \x03(\x0e20.textql.rpc.public.notifications.BroadcastStatusR\x08statuses"d\n\x16ListBroadcastsResponse\x12J\n\nbroadcasts\x18\x01 \x03(\x0b2*.textql.rpc.public.notifications.BroadcastR\nbroadcasts";\n\x16CancelBroadcastRequest\x12!\n\x0cbroadcast_id\x18\x01 \x01(\tR\x0bbroadcastId"\xd7\x03\n\x16UpdateBroadcastRequest\x12!\n\x0cbroadcast_id\x18\x01 \x01(\tR\x0bbroadcastId\x12\x19\n\x05title\x18\x02 \x01(\tH\x00R\x05title\x88\x01\x01\x12\x17\n\x04body\x18\x03 \x01(\tH\x01R\x04body\x88\x01\x01\x12\x1f\n\x08category\x18\x04 \x01(\tH\x02R\x08category\x88\x01\x01\x12 \n\tdeep_link\x18\x05 \x01(\tH\x03R\x08deepLink\x88\x01\x01\x12&\n\x0caction_label\x18\x06 \x01(\tH\x04R\x0bactionLabel\x88\x01\x01\x12"\n\naction_url\x18\x07 \x01(\tH\x05R\tactionUrl\x88\x01\x01\x12J\n\x08audience\x18\x08 \x01(\x0b2..textql.rpc.public.notifications.AlertAudienceR\x08audience\x12=\n\x0cscheduled_at\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampR\x0bscheduledAtB\x08\n\x06_titleB\x07\n\x05_bodyB\x0b\n\t_categoryB\x0c\n\n_deep_linkB\x0f\n\r_action_labelB\r\n\x0b_action_url*\x81\x06\n\x10NotificationType\x12!\n\x1dNOTIFICATION_TYPE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aNOTIFICATION_TYPE_FEED_TAG\x10\x01\x12\x1f\n\x1bNOTIFICATION_TYPE_FEED_POST\x10\x02\x12"\n\x1eNOTIFICATION_TYPE_FEED_COMMENT\x10\x03\x12)\n%NOTIFICATION_TYPE_LIBRARY_SYNC_FAILED\x10\n\x12(\n$NOTIFICATION_TYPE_LIBRARY_PATCH_OPEN\x10\x0b\x12,\n(NOTIFICATION_TYPE_LIBRARY_PATCH_APPROVED\x10\x0c\x12*\n&NOTIFICATION_TYPE_LIBRARY_PATCH_DENIED\x10\r\x12(\n$NOTIFICATION_TYPE_CONFIG_SYNC_FAILED\x10\x0e\x12(\n$NOTIFICATION_TYPE_CODEOWNER_ASSIGNED\x10\x0f\x12\'\n#NOTIFICATION_TYPE_CODEOWNER_REMOVED\x10\x10\x12,\n(NOTIFICATION_TYPE_LIBRARY_PATCH_REVERTED\x10\x11\x12!\n\x1dNOTIFICATION_TYPE_SHARE_GRANT\x10\x14\x12$\n NOTIFICATION_TYPE_REQUEST_ACCESS\x10\x15\x12-\n)NOTIFICATION_TYPE_REQUEST_ACCESS_APPROVED\x10\x16\x12+\n\'NOTIFICATION_TYPE_REQUEST_ACCESS_DENIED\x10\x17\x12"\n\x1eNOTIFICATION_TYPE_SYSTEM_ALERT\x10\x1e\x12$\n NOTIFICATION_TYPE_PLAYBOOK_RECAP\x10("\x04\x08\x04\x10\t"\x04\x08\x12\x10\x13"\x04\x08\x18\x10\x1d"\x04\x08\x1f\x10\'"\x04\x08)\x101*\xb9\x01\n\x13NotificationChannel\x12$\n NOTIFICATION_CHANNEL_UNSPECIFIED\x10\x00\x12\x1c\n\x18NOTIFICATION_CHANNEL_APP\x10\x01\x12\x1e\n\x1aNOTIFICATION_CHANNEL_SLACK\x10\x02\x12\x1e\n\x1aNOTIFICATION_CHANNEL_EMAIL\x10\x03\x12\x1e\n\x1aNOTIFICATION_CHANNEL_TEAMS\x10\x04*\x8e\x01\n\x0fBroadcastStatus\x12 \n\x1cBROADCAST_STATUS_UNSPECIFIED\x10\x00\x12\x1e\n\x1aBROADCAST_STATUS_SCHEDULED\x10\x01\x12\x19\n\x15BROADCAST_STATUS_SENT\x10\x02\x12\x1e\n\x1aBROADCAST_STATUS_CANCELLED\x10\x032\xc5\x05\n\x13NotificationService\x12\x8c\x01\n\x10GetNotifications\x128.textql.rpc.public.notifications.GetNotificationsRequest\x1a9.textql.rpc.public.notifications.GetNotificationsResponse"\x03\x90\x02\x01\x12l\n\x14MarkNotificationRead\x12<.textql.rpc.public.notifications.MarkNotificationReadRequest\x1a\x16.google.protobuf.Empty\x12J\n\x18MarkAllNotificationsRead\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\x12c\n\x13StreamNotifications\x12\x16.google.protobuf.Empty\x1a2.textql.rpc.public.notifications.NotificationEvent0\x01\x12r\n\x14GetNotificationRules\x12\x16.google.protobuf.Empty\x1a=.textql.rpc.public.notifications.GetNotificationRulesResponse"\x03\x90\x02\x01\x12\x8b\x01\n\x16UpsertNotificationRule\x12>.textql.rpc.public.notifications.UpsertNotificationRuleRequest\x1a1.textql.rpc.public.notifications.NotificationRule2\x85\x04\n\x12SystemAlertService\x12v\n\x0fCreateBroadcast\x127.textql.rpc.public.notifications.CreateBroadcastRequest\x1a*.textql.rpc.public.notifications.Broadcast\x12\x86\x01\n\x0eListBroadcasts\x126.textql.rpc.public.notifications.ListBroadcastsRequest\x1a7.textql.rpc.public.notifications.ListBroadcastsResponse"\x03\x90\x02\x01\x12v\n\x0fCancelBroadcast\x127.textql.rpc.public.notifications.CancelBroadcastRequest\x1a*.textql.rpc.public.notifications.Broadcast\x12v\n\x0fUpdateBroadcast\x127.textql.rpc.public.notifications.UpdateBroadcastRequest\x1a*.textql.rpc.public.notifications.BroadcastB\x0c\x92\xb5\x18\x08INTERNALb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.notifications_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\x92\xb5\x18\x08INTERNAL'
    _globals['_BROADCAST_METADATAENTRY']._loaded_options = None
    _globals['_BROADCAST_METADATAENTRY']._serialized_options = b'8\x01'
    _globals['_CREATEBROADCASTREQUEST_METADATAENTRY']._loaded_options = None
    _globals['_CREATEBROADCASTREQUEST_METADATAENTRY']._serialized_options = b'8\x01'
    _globals['_NOTIFICATIONSERVICE'].methods_by_name['GetNotifications']._loaded_options = None
    _globals['_NOTIFICATIONSERVICE'].methods_by_name['GetNotifications']._serialized_options = b'\x90\x02\x01'
    _globals['_NOTIFICATIONSERVICE'].methods_by_name['GetNotificationRules']._loaded_options = None
    _globals['_NOTIFICATIONSERVICE'].methods_by_name['GetNotificationRules']._serialized_options = b'\x90\x02\x01'
    _globals['_SYSTEMALERTSERVICE'].methods_by_name['ListBroadcasts']._loaded_options = None
    _globals['_SYSTEMALERTSERVICE'].methods_by_name['ListBroadcasts']._serialized_options = b'\x90\x02\x01'
    _globals['_NOTIFICATIONTYPE']._serialized_start = 3850
    _globals['_NOTIFICATIONTYPE']._serialized_end = 4619
    _globals['_NOTIFICATIONCHANNEL']._serialized_start = 4622
    _globals['_NOTIFICATIONCHANNEL']._serialized_end = 4807
    _globals['_BROADCASTSTATUS']._serialized_start = 4810
    _globals['_BROADCASTSTATUS']._serialized_end = 4952
    _globals['_NOTIFICATION']._serialized_start = 178
    _globals['_NOTIFICATION']._serialized_end = 467
    _globals['_NOTIFICATIONEVENT']._serialized_start = 470
    _globals['_NOTIFICATIONEVENT']._serialized_end = 607
    _globals['_GETNOTIFICATIONSREQUEST']._serialized_start = 609
    _globals['_GETNOTIFICATIONSREQUEST']._serialized_end = 718
    _globals['_GETNOTIFICATIONSRESPONSE']._serialized_start = 721
    _globals['_GETNOTIFICATIONSRESPONSE']._serialized_end = 867
    _globals['_MARKNOTIFICATIONREADREQUEST']._serialized_start = 869
    _globals['_MARKNOTIFICATIONREADREQUEST']._serialized_end = 939
    _globals['_NOTIFICATIONRULE']._serialized_start = 942
    _globals['_NOTIFICATIONRULE']._serialized_end = 1162
    _globals['_GETNOTIFICATIONRULESRESPONSE']._serialized_start = 1165
    _globals['_GETNOTIFICATIONRULESRESPONSE']._serialized_end = 1347
    _globals['_UPSERTNOTIFICATIONRULEREQUEST']._serialized_start = 1350
    _globals['_UPSERTNOTIFICATIONRULEREQUEST']._serialized_end = 1583
    _globals['_ALERTAUDIENCE']._serialized_start = 1585
    _globals['_ALERTAUDIENCE']._serialized_end = 1687
    _globals['_BROADCAST']._serialized_start = 1690
    _globals['_BROADCAST']._serialized_end = 2499
    _globals['_BROADCAST_METADATAENTRY']._serialized_start = 2440
    _globals['_BROADCAST_METADATAENTRY']._serialized_end = 2499
    _globals['_CREATEBROADCASTREQUEST']._serialized_start = 2502
    _globals['_CREATEBROADCASTREQUEST']._serialized_end = 3055
    _globals['_CREATEBROADCASTREQUEST_METADATAENTRY']._serialized_start = 2440
    _globals['_CREATEBROADCASTREQUEST_METADATAENTRY']._serialized_end = 2499
    _globals['_LISTBROADCASTSREQUEST']._serialized_start = 3058
    _globals['_LISTBROADCASTSREQUEST']._serialized_end = 3210
    _globals['_LISTBROADCASTSRESPONSE']._serialized_start = 3212
    _globals['_LISTBROADCASTSRESPONSE']._serialized_end = 3312
    _globals['_CANCELBROADCASTREQUEST']._serialized_start = 3314
    _globals['_CANCELBROADCASTREQUEST']._serialized_end = 3373
    _globals['_UPDATEBROADCASTREQUEST']._serialized_start = 3376
    _globals['_UPDATEBROADCASTREQUEST']._serialized_end = 3847
    _globals['_NOTIFICATIONSERVICE']._serialized_start = 4955
    _globals['_NOTIFICATIONSERVICE']._serialized_end = 5664
    _globals['_SYSTEMALERTSERVICE']._serialized_start = 5667
    _globals['_SYSTEMALERTSERVICE']._serialized_end = 6184