# pylint: skip-file
# mypy: ignore-errors
# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/sandbox_admin.proto')
_sym_db = _symbol_database.Default()
from ..google.api import visibility_pb2 as google_dot_api_dot_visibility__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1apublic/sandbox_admin.proto\x12\x1ftextql.rpc.public.sandbox_admin\x1a\x1bgoogle/api/visibility.proto\x1a\x1fgoogle/protobuf/timestamp.proto" \n\x1eGetSandboxLeaseSettingsRequest"\xdc\x01\n\x1fGetSandboxLeaseSettingsResponse\x12;\n\x17thread_duration_minutes\x18\x01 \x01(\x05H\x00R\x15threadDurationMinutes\x88\x01\x01\x12A\n\x1adashboard_duration_minutes\x18\x02 \x01(\x05H\x01R\x18dashboardDurationMinutes\x88\x01\x01B\x1a\n\x18_thread_duration_minutesB\x1d\n\x1b_dashboard_duration_minutes"\xdb\x01\n\x1eSetSandboxLeaseSettingsRequest\x12;\n\x17thread_duration_minutes\x18\x01 \x01(\x05H\x00R\x15threadDurationMinutes\x88\x01\x01\x12A\n\x1adashboard_duration_minutes\x18\x02 \x01(\x05H\x01R\x18dashboardDurationMinutes\x88\x01\x01B\x1a\n\x18_thread_duration_minutesB\x1d\n\x1b_dashboard_duration_minutes"!\n\x1fSetSandboxLeaseSettingsResponse"\x8a\x02\n\x0eSandboxSummary\x12\x1d\n\nsandbox_id\x18\x01 \x01(\tR\tsandboxId\x12\x16\n\x06status\x18\x02 \x01(\tR\x06status\x12\x1b\n\tmember_id\x18\x03 \x01(\tR\x08memberId\x12\x17\n\x07chat_id\x18\x04 \x01(\tR\x06chatId\x129\n\nstarted_at\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampR\tstartedAt\x12@\n\x0breleased_at\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00R\nreleasedAt\x88\x01\x01B\x0e\n\x0c_released_at"\\\n\x14ListSandboxesRequest\x12\x16\n\x06status\x18\x01 \x01(\tR\x06status\x12\x14\n\x05limit\x18\x02 \x01(\x05R\x05limit\x12\x16\n\x06cursor\x18\x03 \x01(\tR\x06cursor"\x87\x01\n\x15ListSandboxesResponse\x12M\n\tsandboxes\x18\x01 \x03(\x0b2/.textql.rpc.public.sandbox_admin.SandboxSummaryR\tsandboxes\x12\x1f\n\x0bnext_cursor\x18\x02 \x01(\tR\nnextCursor"3\n\x12StopSandboxRequest\x12\x1d\n\nsandbox_id\x18\x01 \x01(\tR\tsandboxId"/\n\x13StopSandboxResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success"6\n\x15RestartSandboxRequest\x12\x1d\n\nsandbox_id\x18\x01 \x01(\tR\tsandboxId"r\n\x16RestartSandboxResponse\x12\x1d\n\nsandbox_id\x18\x01 \x01(\tR\tsandboxId\x129\n\nstarted_at\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\tstartedAt"2\n\x11GetSandboxRequest\x12\x1d\n\nsandbox_id\x18\x01 \x01(\tR\tsandboxId"\x87\x02\n\x12GetSandboxResponse\x12I\n\x07sandbox\x18\x01 \x01(\x0b2/.textql.rpc.public.sandbox_admin.SandboxSummaryR\x07sandbox\x12%\n\x0elive_available\x18\x02 \x01(\x08R\rliveAvailable\x12,\n\x12memory_usage_bytes\x18\x03 \x01(\x03R\x10memoryUsageBytes\x12Q\n\ndataframes\x18\x04 \x03(\x0b21.textql.rpc.public.sandbox_admin.SandboxDataframeR\ndataframes"\x8a\x01\n\x10SandboxDataframe\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x19\n\x08num_rows\x18\x02 \x01(\x03R\x07numRows\x12\x19\n\x08num_cols\x18\x03 \x01(\x03R\x07numCols\x12,\n\x12memory_usage_bytes\x18\x04 \x01(\x03R\x10memoryUsageBytes"\xfd\x01\n\x10SandboxExecution\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04kind\x18\x02 \x01(\tR\x04kind\x12\x16\n\x06source\x18\x03 \x01(\tR\x06source\x12\x14\n\x05input\x18\x04 \x01(\tR\x05input\x12%\n\x0eoutput_preview\x18\x05 \x01(\tR\routputPreview\x12\x14\n\x05error\x18\x06 \x01(\tR\x05error\x12\x1f\n\x0bduration_ms\x18\x07 \x01(\x03R\ndurationMs\x129\n\ncreated_at\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt"k\n\x1cListSandboxExecutionsRequest\x12\x1d\n\nsandbox_id\x18\x01 \x01(\tR\tsandboxId\x12\x14\n\x05limit\x18\x02 \x01(\x05R\x05limit\x12\x16\n\x06cursor\x18\x03 \x01(\tR\x06cursor"\x93\x01\n\x1dListSandboxExecutionsResponse\x12Q\n\nexecutions\x18\x01 \x03(\x0b21.textql.rpc.public.sandbox_admin.SandboxExecutionR\nexecutions\x12\x1f\n\x0bnext_cursor\x18\x02 \x01(\tR\nnextCursor"\xad\x01\n\x10SandboxFileEntry\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04path\x18\x02 \x01(\tR\x04path\x12\x15\n\x06is_dir\x18\x03 \x01(\x08R\x05isDir\x12\x1d\n\nsize_bytes\x18\x04 \x01(\x03R\tsizeBytes\x12;\n\x0bmodified_at\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampR\nmodifiedAt"L\n\x17ListSandboxFilesRequest\x12\x1d\n\nsandbox_id\x18\x01 \x01(\tR\tsandboxId\x12\x12\n\x04path\x18\x02 \x01(\tR\x04path"\x85\x01\n\x18ListSandboxFilesResponse\x12\x1c\n\tavailable\x18\x01 \x01(\x08R\tavailable\x12K\n\x07entries\x18\x02 \x03(\x0b21.textql.rpc.public.sandbox_admin.SandboxFileEntryR\x07entries"K\n\x16ReadSandboxFileRequest\x12\x1d\n\nsandbox_id\x18\x01 \x01(\tR\tsandboxId\x12\x12\n\x04path\x18\x02 \x01(\tR\x04path"\xf9\x02\n\x11SandboxEgressCall\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x16\n\x06method\x18\x02 \x01(\tR\x06method\x12\x16\n\x06scheme\x18\x03 \x01(\tR\x06scheme\x12\x12\n\x04host\x18\x04 \x01(\tR\x04host\x12\x12\n\x04path\x18\x05 \x01(\tR\x04path\x12\x1f\n\x0bstatus_code\x18\x06 \x01(\x05R\nstatusCode\x12\x18\n\x07outcome\x18\x07 \x01(\tR\x07outcome\x12\x1f\n\x0bduration_ms\x18\x08 \x01(\x03R\ndurationMs\x12#\n\rrequest_bytes\x18\t \x01(\x03R\x0crequestBytes\x12%\n\x0eresponse_bytes\x18\n \x01(\x03R\rresponseBytes\x12\x17\n\x07cell_id\x18\x0b \x01(\tR\x06cellId\x12;\n\x0boccurred_at\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampR\noccurredAt"O\n\x18ListSandboxEgressRequest\x12\x1d\n\nsandbox_id\x18\x01 \x01(\tR\tsandboxId\x12\x14\n\x05limit\x18\x02 \x01(\x05R\x05limit"e\n\x19ListSandboxEgressResponse\x12H\n\x05calls\x18\x01 \x03(\x0b22.textql.rpc.public.sandbox_admin.SandboxEgressCallR\x05calls"\xe7\x01\n\x14SandboxSpendInterval\x129\n\nstarted_at\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampR\tstartedAt\x12:\n\x08ended_at\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00R\x07endedAt\x88\x01\x01\x12\x1f\n\x0bduration_ms\x18\x03 \x01(\x03R\ndurationMs\x12\x12\n\x04acus\x18\x04 \x01(\x01R\x04acus\x12\x16\n\x06active\x18\x05 \x01(\x08R\x06activeB\x0b\n\t_ended_at"8\n\x17ListSandboxSpendRequest\x12\x1d\n\nsandbox_id\x18\x01 \x01(\tR\tsandboxId"\xe4\x01\n\x18ListSandboxSpendResponse\x12S\n\tintervals\x18\x01 \x03(\x0b25.textql.rpc.public.sandbox_admin.SandboxSpendIntervalR\tintervals\x12"\n\racus_per_hour\x18\x02 \x01(\x01R\x0bacusPerHour\x12\x1d\n\ntotal_acus\x18\x03 \x01(\x01R\ttotalAcus\x120\n\x15acu_rate_per_1000_usd\x18\x04 \x01(\x01R\x11acuRatePer1000Usd"\xee\x02\n\x15SandboxResourceSample\x129\n\nsampled_at\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampR\tsampledAt\x12&\n\x0fcpu_usage_cores\x18\x02 \x01(\x01R\rcpuUsageCores\x12&\n\x0fcpu_limit_cores\x18\x03 \x01(\x01R\rcpuLimitCores\x12*\n\x11cpu_usage_percent\x18\x04 \x01(\x01R\x0fcpuUsagePercent\x12,\n\x12memory_usage_bytes\x18\x05 \x01(\x03R\x10memoryUsageBytes\x12,\n\x12memory_limit_bytes\x18\x06 \x01(\x03R\x10memoryLimitBytes\x120\n\x14memory_usage_percent\x18\x07 \x01(\x01R\x12memoryUsagePercent:\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL"\xb8\x01\n\x1bListSandboxResourcesRequest\x12\x1d\n\nsandbox_id\x18\x01 \x01(\tR\tsandboxId\x125\n\x08start_at\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x07startAt\x121\n\x06end_at\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\x05endAt:\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL"\x82\x01\n\x1cListSandboxResourcesResponse\x12P\n\x07samples\x18\x01 \x03(\x0b26.textql.rpc.public.sandbox_admin.SandboxResourceSampleR\x07samples:\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL"\xee\x01\n\x1bStoredSandboxResourceSample\x12\x13\n\x05ts_ms\x18\x01 \x01(\x03R\x04tsMs\x12%\n\x0ecpu_millicores\x18\x02 \x01(\x03R\rcpuMillicores\x120\n\x14cpu_limit_millicores\x18\x03 \x01(\x03R\x12cpuLimitMillicores\x12!\n\x0cmemory_bytes\x18\x04 \x01(\x03R\x0bmemoryBytes\x12,\n\x12memory_limit_bytes\x18\x05 \x01(\x03R\x10memoryLimitBytes:\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL"\x83\x02\n\x17ReadSandboxFileResponse\x12\x1c\n\tavailable\x18\x01 \x01(\x08R\tavailable\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x1d\n\nsize_bytes\x18\x03 \x01(\x03R\tsizeBytes\x12\x1b\n\tmime_type\x18\x04 \x01(\tR\x08mimeType\x12\x18\n\x07content\x18\x05 \x01(\tR\x07content\x12%\n\x0ebinary_content\x18\x06 \x01(\x0cR\rbinaryContent\x12\x1c\n\ttruncated\x18\x07 \x01(\x08R\ttruncated\x12\x1b\n\tis_binary\x18\x08 \x01(\x08R\x08isBinary2\xff\r\n\x13SandboxAdminService\x12\x83\x01\n\rListSandboxes\x125.textql.rpc.public.sandbox_admin.ListSandboxesRequest\x1a6.textql.rpc.public.sandbox_admin.ListSandboxesResponse"\x03\x90\x02\x01\x12x\n\x0bStopSandbox\x123.textql.rpc.public.sandbox_admin.StopSandboxRequest\x1a4.textql.rpc.public.sandbox_admin.StopSandboxResponse\x12\x81\x01\n\x0eRestartSandbox\x126.textql.rpc.public.sandbox_admin.RestartSandboxRequest\x1a7.textql.rpc.public.sandbox_admin.RestartSandboxResponse\x12z\n\nGetSandbox\x122.textql.rpc.public.sandbox_admin.GetSandboxRequest\x1a3.textql.rpc.public.sandbox_admin.GetSandboxResponse"\x03\x90\x02\x01\x12\x9b\x01\n\x15ListSandboxExecutions\x12=.textql.rpc.public.sandbox_admin.ListSandboxExecutionsRequest\x1a>.textql.rpc.public.sandbox_admin.ListSandboxExecutionsResponse"\x03\x90\x02\x01\x12\x8c\x01\n\x10ListSandboxFiles\x128.textql.rpc.public.sandbox_admin.ListSandboxFilesRequest\x1a9.textql.rpc.public.sandbox_admin.ListSandboxFilesResponse"\x03\x90\x02\x01\x12\x89\x01\n\x0fReadSandboxFile\x127.textql.rpc.public.sandbox_admin.ReadSandboxFileRequest\x1a8.textql.rpc.public.sandbox_admin.ReadSandboxFileResponse"\x03\x90\x02\x01\x12\x8f\x01\n\x11ListSandboxEgress\x129.textql.rpc.public.sandbox_admin.ListSandboxEgressRequest\x1a:.textql.rpc.public.sandbox_admin.ListSandboxEgressResponse"\x03\x90\x02\x01\x12\x8c\x01\n\x10ListSandboxSpend\x128.textql.rpc.public.sandbox_admin.ListSandboxSpendRequest\x1a9.textql.rpc.public.sandbox_admin.ListSandboxSpendResponse"\x03\x90\x02\x01\x12\xa8\x01\n\x14ListSandboxResources\x12<.textql.rpc.public.sandbox_admin.ListSandboxResourcesRequest\x1a=.textql.rpc.public.sandbox_admin.ListSandboxResourcesResponse"\x13\x90\x02\x01\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL\x12\xb1\x01\n\x17GetSandboxLeaseSettings\x12?.textql.rpc.public.sandbox_admin.GetSandboxLeaseSettingsRequest\x1a@.textql.rpc.public.sandbox_admin.GetSandboxLeaseSettingsResponse"\x13\x90\x02\x01\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL\x12\xae\x01\n\x17SetSandboxLeaseSettings\x12?.textql.rpc.public.sandbox_admin.SetSandboxLeaseSettingsRequest\x1a@.textql.rpc.public.sandbox_admin.SetSandboxLeaseSettingsResponse"\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNALB;Z9github.com/textqllabs/demo2/compute/pkg/rpc/server/publicb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.sandbox_admin_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z9github.com/textqllabs/demo2/compute/pkg/rpc/server/public'
    _globals['_SANDBOXRESOURCESAMPLE']._loaded_options = None
    _globals['_SANDBOXRESOURCESAMPLE']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_LISTSANDBOXRESOURCESREQUEST']._loaded_options = None
    _globals['_LISTSANDBOXRESOURCESREQUEST']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_LISTSANDBOXRESOURCESRESPONSE']._loaded_options = None
    _globals['_LISTSANDBOXRESOURCESRESPONSE']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_STOREDSANDBOXRESOURCESAMPLE']._loaded_options = None
    _globals['_STOREDSANDBOXRESOURCESAMPLE']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_SANDBOXADMINSERVICE'].methods_by_name['ListSandboxes']._loaded_options = None
    _globals['_SANDBOXADMINSERVICE'].methods_by_name['ListSandboxes']._serialized_options = b'\x90\x02\x01'
    _globals['_SANDBOXADMINSERVICE'].methods_by_name['GetSandbox']._loaded_options = None
    _globals['_SANDBOXADMINSERVICE'].methods_by_name['GetSandbox']._serialized_options = b'\x90\x02\x01'
    _globals['_SANDBOXADMINSERVICE'].methods_by_name['ListSandboxExecutions']._loaded_options = None
    _globals['_SANDBOXADMINSERVICE'].methods_by_name['ListSandboxExecutions']._serialized_options = b'\x90\x02\x01'
    _globals['_SANDBOXADMINSERVICE'].methods_by_name['ListSandboxFiles']._loaded_options = None
    _globals['_SANDBOXADMINSERVICE'].methods_by_name['ListSandboxFiles']._serialized_options = b'\x90\x02\x01'
    _globals['_SANDBOXADMINSERVICE'].methods_by_name['ReadSandboxFile']._loaded_options = None
    _globals['_SANDBOXADMINSERVICE'].methods_by_name['ReadSandboxFile']._serialized_options = b'\x90\x02\x01'
    _globals['_SANDBOXADMINSERVICE'].methods_by_name['ListSandboxEgress']._loaded_options = None
    _globals['_SANDBOXADMINSERVICE'].methods_by_name['ListSandboxEgress']._serialized_options = b'\x90\x02\x01'
    _globals['_SANDBOXADMINSERVICE'].methods_by_name['ListSandboxSpend']._loaded_options = None
    _globals['_SANDBOXADMINSERVICE'].methods_by_name['ListSandboxSpend']._serialized_options = b'\x90\x02\x01'
    _globals['_SANDBOXADMINSERVICE'].methods_by_name['ListSandboxResources']._loaded_options = None
    _globals['_SANDBOXADMINSERVICE'].methods_by_name['ListSandboxResources']._serialized_options = b'\x90\x02\x01\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_SANDBOXADMINSERVICE'].methods_by_name['GetSandboxLeaseSettings']._loaded_options = None
    _globals['_SANDBOXADMINSERVICE'].methods_by_name['GetSandboxLeaseSettings']._serialized_options = b'\x90\x02\x01\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_SANDBOXADMINSERVICE'].methods_by_name['SetSandboxLeaseSettings']._loaded_options = None
    _globals['_SANDBOXADMINSERVICE'].methods_by_name['SetSandboxLeaseSettings']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_GETSANDBOXLEASESETTINGSREQUEST']._serialized_start = 125
    _globals['_GETSANDBOXLEASESETTINGSREQUEST']._serialized_end = 157
    _globals['_GETSANDBOXLEASESETTINGSRESPONSE']._serialized_start = 160
    _globals['_GETSANDBOXLEASESETTINGSRESPONSE']._serialized_end = 380
    _globals['_SETSANDBOXLEASESETTINGSREQUEST']._serialized_start = 383
    _globals['_SETSANDBOXLEASESETTINGSREQUEST']._serialized_end = 602
    _globals['_SETSANDBOXLEASESETTINGSRESPONSE']._serialized_start = 604
    _globals['_SETSANDBOXLEASESETTINGSRESPONSE']._serialized_end = 637
    _globals['_SANDBOXSUMMARY']._serialized_start = 640
    _globals['_SANDBOXSUMMARY']._serialized_end = 906
    _globals['_LISTSANDBOXESREQUEST']._serialized_start = 908
    _globals['_LISTSANDBOXESREQUEST']._serialized_end = 1000
    _globals['_LISTSANDBOXESRESPONSE']._serialized_start = 1003
    _globals['_LISTSANDBOXESRESPONSE']._serialized_end = 1138
    _globals['_STOPSANDBOXREQUEST']._serialized_start = 1140
    _globals['_STOPSANDBOXREQUEST']._serialized_end = 1191
    _globals['_STOPSANDBOXRESPONSE']._serialized_start = 1193
    _globals['_STOPSANDBOXRESPONSE']._serialized_end = 1240
    _globals['_RESTARTSANDBOXREQUEST']._serialized_start = 1242
    _globals['_RESTARTSANDBOXREQUEST']._serialized_end = 1296
    _globals['_RESTARTSANDBOXRESPONSE']._serialized_start = 1298
    _globals['_RESTARTSANDBOXRESPONSE']._serialized_end = 1412
    _globals['_GETSANDBOXREQUEST']._serialized_start = 1414
    _globals['_GETSANDBOXREQUEST']._serialized_end = 1464
    _globals['_GETSANDBOXRESPONSE']._serialized_start = 1467
    _globals['_GETSANDBOXRESPONSE']._serialized_end = 1730
    _globals['_SANDBOXDATAFRAME']._serialized_start = 1733
    _globals['_SANDBOXDATAFRAME']._serialized_end = 1871
    _globals['_SANDBOXEXECUTION']._serialized_start = 1874
    _globals['_SANDBOXEXECUTION']._serialized_end = 2127
    _globals['_LISTSANDBOXEXECUTIONSREQUEST']._serialized_start = 2129
    _globals['_LISTSANDBOXEXECUTIONSREQUEST']._serialized_end = 2236
    _globals['_LISTSANDBOXEXECUTIONSRESPONSE']._serialized_start = 2239
    _globals['_LISTSANDBOXEXECUTIONSRESPONSE']._serialized_end = 2386
    _globals['_SANDBOXFILEENTRY']._serialized_start = 2389
    _globals['_SANDBOXFILEENTRY']._serialized_end = 2562
    _globals['_LISTSANDBOXFILESREQUEST']._serialized_start = 2564
    _globals['_LISTSANDBOXFILESREQUEST']._serialized_end = 2640
    _globals['_LISTSANDBOXFILESRESPONSE']._serialized_start = 2643
    _globals['_LISTSANDBOXFILESRESPONSE']._serialized_end = 2776
    _globals['_READSANDBOXFILEREQUEST']._serialized_start = 2778
    _globals['_READSANDBOXFILEREQUEST']._serialized_end = 2853
    _globals['_SANDBOXEGRESSCALL']._serialized_start = 2856
    _globals['_SANDBOXEGRESSCALL']._serialized_end = 3233
    _globals['_LISTSANDBOXEGRESSREQUEST']._serialized_start = 3235
    _globals['_LISTSANDBOXEGRESSREQUEST']._serialized_end = 3314
    _globals['_LISTSANDBOXEGRESSRESPONSE']._serialized_start = 3316
    _globals['_LISTSANDBOXEGRESSRESPONSE']._serialized_end = 3417
    _globals['_SANDBOXSPENDINTERVAL']._serialized_start = 3420
    _globals['_SANDBOXSPENDINTERVAL']._serialized_end = 3651
    _globals['_LISTSANDBOXSPENDREQUEST']._serialized_start = 3653
    _globals['_LISTSANDBOXSPENDREQUEST']._serialized_end = 3709
    _globals['_LISTSANDBOXSPENDRESPONSE']._serialized_start = 3712
    _globals['_LISTSANDBOXSPENDRESPONSE']._serialized_end = 3940
    _globals['_SANDBOXRESOURCESAMPLE']._serialized_start = 3943
    _globals['_SANDBOXRESOURCESAMPLE']._serialized_end = 4309
    _globals['_LISTSANDBOXRESOURCESREQUEST']._serialized_start = 4312
    _globals['_LISTSANDBOXRESOURCESREQUEST']._serialized_end = 4496
    _globals['_LISTSANDBOXRESOURCESRESPONSE']._serialized_start = 4499
    _globals['_LISTSANDBOXRESOURCESRESPONSE']._serialized_end = 4629
    _globals['_STOREDSANDBOXRESOURCESAMPLE']._serialized_start = 4632
    _globals['_STOREDSANDBOXRESOURCESAMPLE']._serialized_end = 4870
    _globals['_READSANDBOXFILERESPONSE']._serialized_start = 4873
    _globals['_READSANDBOXFILERESPONSE']._serialized_end = 5132
    _globals['_SANDBOXADMINSERVICE']._serialized_start = 5135
    _globals['_SANDBOXADMINSERVICE']._serialized_end = 6926