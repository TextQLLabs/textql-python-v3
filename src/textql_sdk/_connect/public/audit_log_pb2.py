# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
# pylint: skip-file
# mypy: ignore-errors
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/audit_log.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ..public import options_pb2 as public_dot_options__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16public/audit_log.proto\x12\x1btextql.rpc.public.audit_log\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14public/options.proto"\x9a\x03\n\rAuditLogEntry\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x19\n\x08actor_id\x18\x03 \x01(\tR\x07actorId\x12\x1f\n\x0bactor_email\x18\x04 \x01(\tR\nactorEmail\x12\x16\n\x06action\x18\x05 \x01(\tR\x06action\x12\x1a\n\x08category\x18\x06 \x01(\tR\x08category\x12#\n\rresource_type\x18\x07 \x01(\tR\x0cresourceType\x12\x1f\n\x0bresource_id\x18\x08 \x01(\tR\nresourceId\x121\n\x07details\x18\t \x01(\x0b2\x17.google.protobuf.StructR\x07details\x12\x1d\n\nip_address\x18\n \x01(\tR\tipAddress\x12\x1f\n\x0bauth_method\x18\x0b \x01(\tR\nauthMethod\x129\n\ncreated_at\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt"\xa4\x03\n\x14ListAuditLogsRequest\x12\x1f\n\x08category\x18\x01 \x01(\tH\x00R\x08category\x88\x01\x01\x12\x1e\n\x08actor_id\x18\x02 \x01(\tH\x01R\x07actorId\x88\x01\x01\x12\x1b\n\x06action\x18\x03 \x01(\tH\x02R\x06action\x88\x01\x01\x12(\n\rresource_type\x18\x04 \x01(\tH\x03R\x0cresourceType\x88\x01\x01\x12\x1b\n\x06cursor\x18\x05 \x01(\tH\x04R\x06cursor\x88\x01\x01\x12 \n\tpage_size\x18\x06 \x01(\rH\x05R\x08pageSize\x88\x01\x01\x12$\n\x0bsearch_term\x18\x07 \x01(\tH\x06R\nsearchTerm\x88\x01\x01\x125\n\x05after\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampH\x07R\x05after\x88\x01\x01B\x0b\n\t_categoryB\x0b\n\t_actor_idB\t\n\x07_actionB\x10\n\x0e_resource_typeB\t\n\x07_cursorB\x0c\n\n_page_sizeB\x0e\n\x0c_search_termB\x08\n\x06_after"\x93\x01\n\x15ListAuditLogsResponse\x12D\n\x07entries\x18\x01 \x03(\x0b2*.textql.rpc.public.audit_log.AuditLogEntryR\x07entries\x12$\n\x0bnext_cursor\x18\x02 \x01(\tH\x00R\nnextCursor\x88\x01\x01B\x0e\n\x0c_next_cursor"\xf2\x04\n\x0eS3ExportConfig\x12\x16\n\x06bucket\x18\x01 \x01(\tR\x06bucket\x12\x16\n\x06region\x18\x02 \x01(\tR\x06region\x12\x16\n\x06prefix\x18\x03 \x01(\tR\x06prefix\x12/\n\x11aws_access_key_id\x18\x04 \x01(\tB\x04\x88\xb5\x18\x01R\x0eawsAccessKeyId\x127\n\x15aws_secret_access_key\x18\x05 \x01(\tB\x04\x88\xb5\x18\x01R\x12awsSecretAccessKey\x12\x18\n\x07enabled\x18\x06 \x01(\x08R\x07enabled\x12I\n\x10last_exported_at\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00R\x0elastExportedAt\x88\x01\x01\x129\n\ncreated_at\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt\x129\n\nupdated_at\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampR\tupdatedAt\x12D\n\tauth_mode\x18\n \x01(\x0e2\'.textql.rpc.public.audit_log.S3AuthModeR\x08authMode\x12\x19\n\x08role_arn\x18\x0b \x01(\tR\x07roleArn\x12%\n\x0bexternal_id\x18\x0c \x01(\tB\x04\x88\xb5\x18\x01R\nexternalId\x126\n\x17export_interval_seconds\x18\r \x01(\x05R\x15exportIntervalSecondsB\x13\n\x11_last_exported_at"\xa6\x03\n\x18ConfigureS3ExportRequest\x12\x16\n\x06bucket\x18\x01 \x01(\tR\x06bucket\x12\x16\n\x06region\x18\x02 \x01(\tR\x06region\x12\x16\n\x06prefix\x18\x03 \x01(\tR\x06prefix\x12/\n\x11aws_access_key_id\x18\x04 \x01(\tB\x04\x88\xb5\x18\x01R\x0eawsAccessKeyId\x127\n\x15aws_secret_access_key\x18\x05 \x01(\tB\x04\x88\xb5\x18\x01R\x12awsSecretAccessKey\x12\x18\n\x07enabled\x18\x06 \x01(\x08R\x07enabled\x12D\n\tauth_mode\x18\x07 \x01(\x0e2\'.textql.rpc.public.audit_log.S3AuthModeR\x08authMode\x12\x19\n\x08role_arn\x18\x08 \x01(\tR\x07roleArn\x12%\n\x0bexternal_id\x18\t \x01(\tB\x04\x88\xb5\x18\x01R\nexternalId\x126\n\x17export_interval_seconds\x18\n \x01(\x05R\x15exportIntervalSeconds"`\n\x19ConfigureS3ExportResponse\x12C\n\x06config\x18\x01 \x01(\x0b2+.textql.rpc.public.audit_log.S3ExportConfigR\x06config"\x1a\n\x18GetS3ExportConfigRequest"p\n\x19GetS3ExportConfigResponse\x12H\n\x06config\x18\x01 \x01(\x0b2+.textql.rpc.public.audit_log.S3ExportConfigH\x00R\x06config\x88\x01\x01B\t\n\x07_config"\x1d\n\x1bDeleteS3ExportConfigRequest"\x1e\n\x1cDeleteS3ExportConfigResponse"\xc1\x02\n\x1dTestS3ExportConnectionRequest\x12\x16\n\x06bucket\x18\x01 \x01(\tR\x06bucket\x12\x16\n\x06region\x18\x02 \x01(\tR\x06region\x12/\n\x11aws_access_key_id\x18\x03 \x01(\tB\x04\x88\xb5\x18\x01R\x0eawsAccessKeyId\x127\n\x15aws_secret_access_key\x18\x04 \x01(\tB\x04\x88\xb5\x18\x01R\x12awsSecretAccessKey\x12D\n\tauth_mode\x18\x05 \x01(\x0e2\'.textql.rpc.public.audit_log.S3AuthModeR\x08authMode\x12\x19\n\x08role_arn\x18\x06 \x01(\tR\x07roleArn\x12%\n\x0bexternal_id\x18\x07 \x01(\tB\x04\x88\xb5\x18\x01R\nexternalId"_\n\x1eTestS3ExportConnectionResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12#\n\rerror_message\x18\x02 \x01(\tR\x0cerrorMessage"\x18\n\x16TriggerS3ExportRequest"7\n\x17TriggerS3ExportResponse\x12\x1c\n\ttriggered\x18\x01 \x01(\x08R\ttriggered"\xa3\x03\n\x10OtlpExportConfig\x12\x18\n\x07enabled\x18\x01 \x01(\x08R\x07enabled\x12#\n\rotlp_endpoint\x18\x02 \x01(\tR\x0cotlpEndpoint\x12\'\n\x0cotlp_headers\x18\x03 \x01(\tB\x04\x88\xb5\x18\x01R\x0botlpHeaders\x12#\n\rotlp_protocol\x18\x04 \x01(\tR\x0cotlpProtocol\x122\n\x15push_interval_seconds\x18\x05 \x01(\x05R\x13pushIntervalSeconds\x12E\n\x0elast_pushed_at\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00R\x0clastPushedAt\x88\x01\x01\x129\n\ncreated_at\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt\x129\n\nupdated_at\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampR\tupdatedAtB\x11\n\x0f_last_pushed_at"\xdd\x01\n\x1aConfigureOtlpExportRequest\x12\x18\n\x07enabled\x18\x01 \x01(\x08R\x07enabled\x12#\n\rotlp_endpoint\x18\x02 \x01(\tR\x0cotlpEndpoint\x12\'\n\x0cotlp_headers\x18\x03 \x01(\tB\x04\x88\xb5\x18\x01R\x0botlpHeaders\x12#\n\rotlp_protocol\x18\x04 \x01(\tR\x0cotlpProtocol\x122\n\x15push_interval_seconds\x18\x05 \x01(\x05R\x13pushIntervalSeconds"d\n\x1bConfigureOtlpExportResponse\x12E\n\x06config\x18\x01 \x01(\x0b2-.textql.rpc.public.audit_log.OtlpExportConfigR\x06config"\x1c\n\x1aGetOtlpExportConfigRequest"t\n\x1bGetOtlpExportConfigResponse\x12J\n\x06config\x18\x01 \x01(\x0b2-.textql.rpc.public.audit_log.OtlpExportConfigH\x00R\x06config\x88\x01\x01B\t\n\x07_config"\x1f\n\x1dDeleteOtlpExportConfigRequest" \n\x1eDeleteOtlpExportConfigResponse"\x94\x01\n\x1fTestOtlpExportConnectionRequest\x12#\n\rotlp_endpoint\x18\x01 \x01(\tR\x0cotlpEndpoint\x12\'\n\x0cotlp_headers\x18\x02 \x01(\tB\x04\x88\xb5\x18\x01R\x0botlpHeaders\x12#\n\rotlp_protocol\x18\x03 \x01(\tR\x0cotlpProtocol"a\n TestOtlpExportConnectionResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12#\n\rerror_message\x18\x02 \x01(\tR\x0cerrorMessage"\x1a\n\x18TriggerOtlpExportRequest"9\n\x19TriggerOtlpExportResponse\x12\x1c\n\ttriggered\x18\x01 \x01(\x08R\ttriggered*e\n\nS3AuthMode\x12\x1c\n\x18S3_AUTH_MODE_UNSPECIFIED\x10\x00\x12\x1b\n\x17S3_AUTH_MODE_ACCESS_KEY\x10\x01\x12\x1c\n\x18S3_AUTH_MODE_ASSUME_ROLE\x10\x022\x8b\x0c\n\x0fAuditLogService\x12{\n\rListAuditLogs\x121.textql.rpc.public.audit_log.ListAuditLogsRequest\x1a2.textql.rpc.public.audit_log.ListAuditLogsResponse"\x03\x90\x02\x01\x12\x82\x01\n\x11ConfigureS3Export\x125.textql.rpc.public.audit_log.ConfigureS3ExportRequest\x1a6.textql.rpc.public.audit_log.ConfigureS3ExportResponse\x12\x87\x01\n\x11GetS3ExportConfig\x125.textql.rpc.public.audit_log.GetS3ExportConfigRequest\x1a6.textql.rpc.public.audit_log.GetS3ExportConfigResponse"\x03\x90\x02\x01\x12\x8b\x01\n\x14DeleteS3ExportConfig\x128.textql.rpc.public.audit_log.DeleteS3ExportConfigRequest\x1a9.textql.rpc.public.audit_log.DeleteS3ExportConfigResponse\x12\x91\x01\n\x16TestS3ExportConnection\x12:.textql.rpc.public.audit_log.TestS3ExportConnectionRequest\x1a;.textql.rpc.public.audit_log.TestS3ExportConnectionResponse\x12|\n\x0fTriggerS3Export\x123.textql.rpc.public.audit_log.TriggerS3ExportRequest\x1a4.textql.rpc.public.audit_log.TriggerS3ExportResponse\x12\x88\x01\n\x13ConfigureOtlpExport\x127.textql.rpc.public.audit_log.ConfigureOtlpExportRequest\x1a8.textql.rpc.public.audit_log.ConfigureOtlpExportResponse\x12\x8d\x01\n\x13GetOtlpExportConfig\x127.textql.rpc.public.audit_log.GetOtlpExportConfigRequest\x1a8.textql.rpc.public.audit_log.GetOtlpExportConfigResponse"\x03\x90\x02\x01\x12\x91\x01\n\x16DeleteOtlpExportConfig\x12:.textql.rpc.public.audit_log.DeleteOtlpExportConfigRequest\x1a;.textql.rpc.public.audit_log.DeleteOtlpExportConfigResponse\x12\x97\x01\n\x18TestOtlpExportConnection\x12<.textql.rpc.public.audit_log.TestOtlpExportConnectionRequest\x1a=.textql.rpc.public.audit_log.TestOtlpExportConnectionResponse\x12\x82\x01\n\x11TriggerOtlpExport\x125.textql.rpc.public.audit_log.TriggerOtlpExportRequest\x1a6.textql.rpc.public.audit_log.TriggerOtlpExportResponseb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.audit_log_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_S3EXPORTCONFIG'].fields_by_name['aws_access_key_id']._loaded_options = None
    _globals['_S3EXPORTCONFIG'].fields_by_name['aws_access_key_id']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_S3EXPORTCONFIG'].fields_by_name['aws_secret_access_key']._loaded_options = None
    _globals['_S3EXPORTCONFIG'].fields_by_name['aws_secret_access_key']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_S3EXPORTCONFIG'].fields_by_name['external_id']._loaded_options = None
    _globals['_S3EXPORTCONFIG'].fields_by_name['external_id']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_CONFIGURES3EXPORTREQUEST'].fields_by_name['aws_access_key_id']._loaded_options = None
    _globals['_CONFIGURES3EXPORTREQUEST'].fields_by_name['aws_access_key_id']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_CONFIGURES3EXPORTREQUEST'].fields_by_name['aws_secret_access_key']._loaded_options = None
    _globals['_CONFIGURES3EXPORTREQUEST'].fields_by_name['aws_secret_access_key']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_CONFIGURES3EXPORTREQUEST'].fields_by_name['external_id']._loaded_options = None
    _globals['_CONFIGURES3EXPORTREQUEST'].fields_by_name['external_id']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_TESTS3EXPORTCONNECTIONREQUEST'].fields_by_name['aws_access_key_id']._loaded_options = None
    _globals['_TESTS3EXPORTCONNECTIONREQUEST'].fields_by_name['aws_access_key_id']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_TESTS3EXPORTCONNECTIONREQUEST'].fields_by_name['aws_secret_access_key']._loaded_options = None
    _globals['_TESTS3EXPORTCONNECTIONREQUEST'].fields_by_name['aws_secret_access_key']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_TESTS3EXPORTCONNECTIONREQUEST'].fields_by_name['external_id']._loaded_options = None
    _globals['_TESTS3EXPORTCONNECTIONREQUEST'].fields_by_name['external_id']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_OTLPEXPORTCONFIG'].fields_by_name['otlp_headers']._loaded_options = None
    _globals['_OTLPEXPORTCONFIG'].fields_by_name['otlp_headers']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_CONFIGUREOTLPEXPORTREQUEST'].fields_by_name['otlp_headers']._loaded_options = None
    _globals['_CONFIGUREOTLPEXPORTREQUEST'].fields_by_name['otlp_headers']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_TESTOTLPEXPORTCONNECTIONREQUEST'].fields_by_name['otlp_headers']._loaded_options = None
    _globals['_TESTOTLPEXPORTCONNECTIONREQUEST'].fields_by_name['otlp_headers']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_AUDITLOGSERVICE'].methods_by_name['ListAuditLogs']._loaded_options = None
    _globals['_AUDITLOGSERVICE'].methods_by_name['ListAuditLogs']._serialized_options = b'\x90\x02\x01'
    _globals['_AUDITLOGSERVICE'].methods_by_name['GetS3ExportConfig']._loaded_options = None
    _globals['_AUDITLOGSERVICE'].methods_by_name['GetS3ExportConfig']._serialized_options = b'\x90\x02\x01'
    _globals['_AUDITLOGSERVICE'].methods_by_name['GetOtlpExportConfig']._loaded_options = None
    _globals['_AUDITLOGSERVICE'].methods_by_name['GetOtlpExportConfig']._serialized_options = b'\x90\x02\x01'
    _globals['_S3AUTHMODE']._serialized_start = 4287
    _globals['_S3AUTHMODE']._serialized_end = 4388
    _globals['_AUDITLOGENTRY']._serialized_start = 141
    _globals['_AUDITLOGENTRY']._serialized_end = 551
    _globals['_LISTAUDITLOGSREQUEST']._serialized_start = 554
    _globals['_LISTAUDITLOGSREQUEST']._serialized_end = 974
    _globals['_LISTAUDITLOGSRESPONSE']._serialized_start = 977
    _globals['_LISTAUDITLOGSRESPONSE']._serialized_end = 1124
    _globals['_S3EXPORTCONFIG']._serialized_start = 1127
    _globals['_S3EXPORTCONFIG']._serialized_end = 1753
    _globals['_CONFIGURES3EXPORTREQUEST']._serialized_start = 1756
    _globals['_CONFIGURES3EXPORTREQUEST']._serialized_end = 2178
    _globals['_CONFIGURES3EXPORTRESPONSE']._serialized_start = 2180
    _globals['_CONFIGURES3EXPORTRESPONSE']._serialized_end = 2276
    _globals['_GETS3EXPORTCONFIGREQUEST']._serialized_start = 2278
    _globals['_GETS3EXPORTCONFIGREQUEST']._serialized_end = 2304
    _globals['_GETS3EXPORTCONFIGRESPONSE']._serialized_start = 2306
    _globals['_GETS3EXPORTCONFIGRESPONSE']._serialized_end = 2418
    _globals['_DELETES3EXPORTCONFIGREQUEST']._serialized_start = 2420
    _globals['_DELETES3EXPORTCONFIGREQUEST']._serialized_end = 2449
    _globals['_DELETES3EXPORTCONFIGRESPONSE']._serialized_start = 2451
    _globals['_DELETES3EXPORTCONFIGRESPONSE']._serialized_end = 2481
    _globals['_TESTS3EXPORTCONNECTIONREQUEST']._serialized_start = 2484
    _globals['_TESTS3EXPORTCONNECTIONREQUEST']._serialized_end = 2805
    _globals['_TESTS3EXPORTCONNECTIONRESPONSE']._serialized_start = 2807
    _globals['_TESTS3EXPORTCONNECTIONRESPONSE']._serialized_end = 2902
    _globals['_TRIGGERS3EXPORTREQUEST']._serialized_start = 2904
    _globals['_TRIGGERS3EXPORTREQUEST']._serialized_end = 2928
    _globals['_TRIGGERS3EXPORTRESPONSE']._serialized_start = 2930
    _globals['_TRIGGERS3EXPORTRESPONSE']._serialized_end = 2985
    _globals['_OTLPEXPORTCONFIG']._serialized_start = 2988
    _globals['_OTLPEXPORTCONFIG']._serialized_end = 3407
    _globals['_CONFIGUREOTLPEXPORTREQUEST']._serialized_start = 3410
    _globals['_CONFIGUREOTLPEXPORTREQUEST']._serialized_end = 3631
    _globals['_CONFIGUREOTLPEXPORTRESPONSE']._serialized_start = 3633
    _globals['_CONFIGUREOTLPEXPORTRESPONSE']._serialized_end = 3733
    _globals['_GETOTLPEXPORTCONFIGREQUEST']._serialized_start = 3735
    _globals['_GETOTLPEXPORTCONFIGREQUEST']._serialized_end = 3763
    _globals['_GETOTLPEXPORTCONFIGRESPONSE']._serialized_start = 3765
    _globals['_GETOTLPEXPORTCONFIGRESPONSE']._serialized_end = 3881
    _globals['_DELETEOTLPEXPORTCONFIGREQUEST']._serialized_start = 3883
    _globals['_DELETEOTLPEXPORTCONFIGREQUEST']._serialized_end = 3914
    _globals['_DELETEOTLPEXPORTCONFIGRESPONSE']._serialized_start = 3916
    _globals['_DELETEOTLPEXPORTCONFIGRESPONSE']._serialized_end = 3948
    _globals['_TESTOTLPEXPORTCONNECTIONREQUEST']._serialized_start = 3951
    _globals['_TESTOTLPEXPORTCONNECTIONREQUEST']._serialized_end = 4099
    _globals['_TESTOTLPEXPORTCONNECTIONRESPONSE']._serialized_start = 4101
    _globals['_TESTOTLPEXPORTCONNECTIONRESPONSE']._serialized_end = 4198
    _globals['_TRIGGEROTLPEXPORTREQUEST']._serialized_start = 4200
    _globals['_TRIGGEROTLPEXPORTREQUEST']._serialized_end = 4226
    _globals['_TRIGGEROTLPEXPORTRESPONSE']._serialized_start = 4228
    _globals['_TRIGGEROTLPEXPORTRESPONSE']._serialized_end = 4285
    _globals['_AUDITLOGSERVICE']._serialized_start = 4391
    _globals['_AUDITLOGSERVICE']._serialized_end = 5938