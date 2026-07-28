# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
# pylint: skip-file
# mypy: ignore-errors
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/powerbi.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14public/powerbi.proto\x12\x19textql.rpc.public.powerbi\x1a\x1fgoogle/protobuf/timestamp.proto"\xf3\x01\n\x1cTestPowerBIConnectionRequest\x12&\n\x0cconnector_id\x18\x01 \x01(\x05H\x00R\x0bconnectorId\x88\x01\x01\x12 \n\ttenant_id\x18\x02 \x01(\tH\x01R\x08tenantId\x88\x01\x01\x12 \n\tclient_id\x18\x03 \x01(\tH\x02R\x08clientId\x88\x01\x01\x12(\n\rclient_secret\x18\x04 \x01(\tH\x03R\x0cclientSecret\x88\x01\x01B\x0f\n\r_connector_idB\x0c\n\n_tenant_idB\x0c\n\n_client_idB\x10\n\x0e_client_secret"O\n\x1dTestPowerBIConnectionResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x14\n\x05error\x18\x02 \x01(\tR\x05error"|\n\x10PowerBIWorkspace\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0cis_read_only\x18\x03 \x01(\x08R\nisReadOnly\x12"\n\ris_on_premium\x18\x04 \x01(\x08R\x0bisOnPremium"A\n\x1cListPowerBIWorkspacesRequest\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId"\x91\x01\n\x1dListPowerBIWorkspacesResponse\x12K\n\nworkspaces\x18\x01 \x03(\x0b2+.textql.rpc.public.powerbi.PowerBIWorkspaceR\nworkspaces\x12\x19\n\x05error\x18\x02 \x01(\tH\x00R\x05error\x88\x01\x01B\x08\n\x06_error"\xe4\x03\n\x0ePowerBIDataset\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12/\n\x14add_rows_api_enabled\x18\x03 \x01(\x08R\x11addRowsApiEnabled\x12#\n\rconfigured_by\x18\x04 \x01(\tR\x0cconfiguredBy\x12%\n\x0eis_refreshable\x18\x05 \x01(\x08R\risRefreshable\x12C\n\x1eis_effective_identity_required\x18\x06 \x01(\x08R\x1bisEffectiveIdentityRequired\x12N\n$is_effective_identity_roles_required\x18\x07 \x01(\x08R isEffectiveIdentityRolesRequired\x12<\n\x1bis_on_prem_gateway_required\x18\x08 \x01(\x08R\x17isOnPremGatewayRequired\x12=\n\x0ccreated_date\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampR\x0bcreatedDate\x12\x1f\n\x0btable_names\x18\n \x03(\tR\ntableNames"b\n\x1aListPowerBIDatasetsRequest\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId\x12!\n\x0cworkspace_id\x18\x02 \x01(\tR\x0bworkspaceId"\x89\x01\n\x1bListPowerBIDatasetsResponse\x12E\n\x08datasets\x18\x01 \x03(\x0b2).textql.rpc.public.powerbi.PowerBIDatasetR\x08datasets\x12\x19\n\x05error\x18\x02 \x01(\tH\x00R\x05error\x88\x01\x01B\x08\n\x06_error"\xe6\x01\n\rPowerBIReport\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x17\n\x07web_url\x18\x03 \x01(\tR\x06webUrl\x12\x1b\n\tembed_url\x18\x04 \x01(\tR\x08embedUrl\x12\x1d\n\ndataset_id\x18\x05 \x01(\tR\tdatasetId\x12\x1d\n\ncreated_by\x18\x06 \x01(\tR\tcreatedBy\x12=\n\x0ccreated_date\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0bcreatedDate"a\n\x19ListPowerBIReportsRequest\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId\x12!\n\x0cworkspace_id\x18\x02 \x01(\tR\x0bworkspaceId"\x85\x01\n\x1aListPowerBIReportsResponse\x12B\n\x07reports\x18\x01 \x03(\x0b2(.textql.rpc.public.powerbi.PowerBIReportR\x07reports\x12\x19\n\x05error\x18\x02 \x01(\tH\x00R\x05error\x88\x01\x01B\x08\n\x06_error"\x84\x01\n\x1fExportPowerBIReportImageRequest\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId\x12!\n\x0cworkspace_id\x18\x02 \x01(\tR\x0bworkspaceId\x12\x1b\n\treport_id\x18\x03 \x01(\tR\x08reportId"\x83\x01\n ExportPowerBIReportImageResponse\x12\x1d\n\nimage_data\x18\x01 \x01(\x0cR\timageData\x12\x1b\n\timage_url\x18\x02 \x01(\tR\x08imageUrl\x12\x19\n\x05error\x18\x03 \x01(\tH\x00R\x05error\x88\x01\x01B\x08\n\x06_error"\xa4\x01\n GeneratePowerBIEmbedTokenRequest\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId\x12!\n\x0cworkspace_id\x18\x02 \x01(\tR\x0bworkspaceId\x12\x1b\n\treport_id\x18\x03 \x01(\tR\x08reportId\x12\x1d\n\ndataset_id\x18\x04 \x01(\tR\tdatasetId"\x90\x01\n!GeneratePowerBIEmbedTokenResponse\x12\x14\n\x05token\x18\x01 \x01(\tR\x05token\x12\x19\n\x08token_id\x18\x02 \x01(\tR\x07tokenId\x12:\n\nexpiration\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\nexpiration"\x91\x02\n\x17SyncPowerBIItemsRequest\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId\x12!\n\x0cworkspace_id\x18\x02 \x01(\tR\x0bworkspaceId\x12%\n\x0eworkspace_name\x18\x03 \x01(\tR\rworkspaceName\x12B\n\x07reports\x18\x04 \x03(\x0b2(.textql.rpc.public.powerbi.PowerBIReportR\x07reports\x12E\n\x08datasets\x18\x05 \x03(\x0b2).textql.rpc.public.powerbi.PowerBIDatasetR\x08datasets"\xb3\x01\n\x18SyncPowerBIItemsResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x19\n\x05error\x18\x02 \x01(\tH\x00R\x05error\x88\x01\x01\x12*\n\x11synced_report_ids\x18\x03 \x03(\tR\x0fsyncedReportIds\x12,\n\x12synced_dataset_ids\x18\x04 \x03(\tR\x10syncedDatasetIdsB\x08\n\x06_error"~\n\x19UnsyncPowerBIItemsRequest\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId\x12\x1d\n\nreport_ids\x18\x02 \x03(\tR\treportIds\x12\x1f\n\x0bdataset_ids\x18\x03 \x03(\tR\ndatasetIds"[\n\x1aUnsyncPowerBIItemsResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x19\n\x05error\x18\x02 \x01(\tH\x00R\x05error\x88\x01\x01B\x08\n\x06_error"A\n\x1cGetSyncedPowerBIItemsRequest\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId"\xb6\x01\n\x1dGetSyncedPowerBIItemsResponse\x12H\n\x07reports\x18\x01 \x03(\x0b2..textql.rpc.public.powerbi.SyncedPowerBIReportR\x07reports\x12K\n\x08datasets\x18\x02 \x03(\x0b2/.textql.rpc.public.powerbi.SyncedPowerBIDatasetR\x08datasets"\xda\x01\n\x13SyncedPowerBIReport\x12@\n\x06report\x18\x01 \x01(\x0b2(.textql.rpc.public.powerbi.PowerBIReportR\x06report\x12!\n\x0cworkspace_id\x18\x02 \x01(\tR\x0bworkspaceId\x12%\n\x0eworkspace_name\x18\x03 \x01(\tR\rworkspaceName\x127\n\tsynced_at\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\x08syncedAt"\xde\x01\n\x14SyncedPowerBIDataset\x12C\n\x07dataset\x18\x01 \x01(\x0b2).textql.rpc.public.powerbi.PowerBIDatasetR\x07dataset\x12!\n\x0cworkspace_id\x18\x02 \x01(\tR\x0bworkspaceId\x12%\n\x0eworkspace_name\x18\x03 \x01(\tR\rworkspaceName\x127\n\tsynced_at\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\x08syncedAt"\xbf\x01\n\x1fGetPowerBIDatasetPreviewRequest\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId\x12!\n\x0cworkspace_id\x18\x02 \x01(\tR\x0bworkspaceId\x12\x1d\n\ndataset_id\x18\x03 \x01(\tR\tdatasetId\x12!\n\x0cdataset_name\x18\x04 \x01(\tR\x0bdatasetName\x12\x14\n\x05limit\x18\x05 \x01(\x05R\x05limit"\x97\x01\n\x13PowerBITablePreview\x12\x1d\n\ntable_name\x18\x01 \x01(\tR\ttableName\x12\x1d\n\narrow_data\x18\x02 \x01(\x0cR\tarrowData\x12\x1d\n\ntotal_rows\x18\x03 \x01(\x03R\ttotalRows\x12\x19\n\x05error\x18\x04 \x01(\tH\x00R\x05error\x88\x01\x01B\x08\n\x06_error"\xb8\x01\n GetPowerBIDatasetPreviewResponse\x12U\n\x0etable_previews\x18\x01 \x03(\x0b2..textql.rpc.public.powerbi.PowerBITablePreviewR\rtablePreviews\x12\x18\n\x07success\x18\x02 \x01(\x08R\x07success\x12\x19\n\x05error\x18\x03 \x01(\tH\x00R\x05error\x88\x01\x01B\x08\n\x06_error2\x9c\x0b\n\x0ePowerBIService\x12\x8c\x01\n\x15TestPowerBIConnection\x127.textql.rpc.public.powerbi.TestPowerBIConnectionRequest\x1a8.textql.rpc.public.powerbi.TestPowerBIConnectionResponse"\x00\x12\x8c\x01\n\x15ListPowerBIWorkspaces\x127.textql.rpc.public.powerbi.ListPowerBIWorkspacesRequest\x1a8.textql.rpc.public.powerbi.ListPowerBIWorkspacesResponse"\x00\x12\x86\x01\n\x13ListPowerBIDatasets\x125.textql.rpc.public.powerbi.ListPowerBIDatasetsRequest\x1a6.textql.rpc.public.powerbi.ListPowerBIDatasetsResponse"\x00\x12\x83\x01\n\x12ListPowerBIReports\x124.textql.rpc.public.powerbi.ListPowerBIReportsRequest\x1a5.textql.rpc.public.powerbi.ListPowerBIReportsResponse"\x00\x12\x95\x01\n\x18ExportPowerBIReportImage\x12:.textql.rpc.public.powerbi.ExportPowerBIReportImageRequest\x1a;.textql.rpc.public.powerbi.ExportPowerBIReportImageResponse"\x00\x12\x98\x01\n\x19GeneratePowerBIEmbedToken\x12;.textql.rpc.public.powerbi.GeneratePowerBIEmbedTokenRequest\x1a<.textql.rpc.public.powerbi.GeneratePowerBIEmbedTokenResponse"\x00\x12}\n\x10SyncPowerBIItems\x122.textql.rpc.public.powerbi.SyncPowerBIItemsRequest\x1a3.textql.rpc.public.powerbi.SyncPowerBIItemsResponse"\x00\x12\x83\x01\n\x12UnsyncPowerBIItems\x124.textql.rpc.public.powerbi.UnsyncPowerBIItemsRequest\x1a5.textql.rpc.public.powerbi.UnsyncPowerBIItemsResponse"\x00\x12\x8c\x01\n\x15GetSyncedPowerBIItems\x127.textql.rpc.public.powerbi.GetSyncedPowerBIItemsRequest\x1a8.textql.rpc.public.powerbi.GetSyncedPowerBIItemsResponse"\x00\x12\x95\x01\n\x18GetPowerBIDatasetPreview\x12:.textql.rpc.public.powerbi.GetPowerBIDatasetPreviewRequest\x1a;.textql.rpc.public.powerbi.GetPowerBIDatasetPreviewResponse"\x00B;Z9github.com/textqllabs/demo2/compute/pkg/rpc/server/publicb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.powerbi_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z9github.com/textqllabs/demo2/compute/pkg/rpc/server/public'
    _globals['_TESTPOWERBICONNECTIONREQUEST']._serialized_start = 85
    _globals['_TESTPOWERBICONNECTIONREQUEST']._serialized_end = 328
    _globals['_TESTPOWERBICONNECTIONRESPONSE']._serialized_start = 330
    _globals['_TESTPOWERBICONNECTIONRESPONSE']._serialized_end = 409
    _globals['_POWERBIWORKSPACE']._serialized_start = 411
    _globals['_POWERBIWORKSPACE']._serialized_end = 535
    _globals['_LISTPOWERBIWORKSPACESREQUEST']._serialized_start = 537
    _globals['_LISTPOWERBIWORKSPACESREQUEST']._serialized_end = 602
    _globals['_LISTPOWERBIWORKSPACESRESPONSE']._serialized_start = 605
    _globals['_LISTPOWERBIWORKSPACESRESPONSE']._serialized_end = 750
    _globals['_POWERBIDATASET']._serialized_start = 753
    _globals['_POWERBIDATASET']._serialized_end = 1237
    _globals['_LISTPOWERBIDATASETSREQUEST']._serialized_start = 1239
    _globals['_LISTPOWERBIDATASETSREQUEST']._serialized_end = 1337
    _globals['_LISTPOWERBIDATASETSRESPONSE']._serialized_start = 1340
    _globals['_LISTPOWERBIDATASETSRESPONSE']._serialized_end = 1477
    _globals['_POWERBIREPORT']._serialized_start = 1480
    _globals['_POWERBIREPORT']._serialized_end = 1710
    _globals['_LISTPOWERBIREPORTSREQUEST']._serialized_start = 1712
    _globals['_LISTPOWERBIREPORTSREQUEST']._serialized_end = 1809
    _globals['_LISTPOWERBIREPORTSRESPONSE']._serialized_start = 1812
    _globals['_LISTPOWERBIREPORTSRESPONSE']._serialized_end = 1945
    _globals['_EXPORTPOWERBIREPORTIMAGEREQUEST']._serialized_start = 1948
    _globals['_EXPORTPOWERBIREPORTIMAGEREQUEST']._serialized_end = 2080
    _globals['_EXPORTPOWERBIREPORTIMAGERESPONSE']._serialized_start = 2083
    _globals['_EXPORTPOWERBIREPORTIMAGERESPONSE']._serialized_end = 2214
    _globals['_GENERATEPOWERBIEMBEDTOKENREQUEST']._serialized_start = 2217
    _globals['_GENERATEPOWERBIEMBEDTOKENREQUEST']._serialized_end = 2381
    _globals['_GENERATEPOWERBIEMBEDTOKENRESPONSE']._serialized_start = 2384
    _globals['_GENERATEPOWERBIEMBEDTOKENRESPONSE']._serialized_end = 2528
    _globals['_SYNCPOWERBIITEMSREQUEST']._serialized_start = 2531
    _globals['_SYNCPOWERBIITEMSREQUEST']._serialized_end = 2804
    _globals['_SYNCPOWERBIITEMSRESPONSE']._serialized_start = 2807
    _globals['_SYNCPOWERBIITEMSRESPONSE']._serialized_end = 2986
    _globals['_UNSYNCPOWERBIITEMSREQUEST']._serialized_start = 2988
    _globals['_UNSYNCPOWERBIITEMSREQUEST']._serialized_end = 3114
    _globals['_UNSYNCPOWERBIITEMSRESPONSE']._serialized_start = 3116
    _globals['_UNSYNCPOWERBIITEMSRESPONSE']._serialized_end = 3207
    _globals['_GETSYNCEDPOWERBIITEMSREQUEST']._serialized_start = 3209
    _globals['_GETSYNCEDPOWERBIITEMSREQUEST']._serialized_end = 3274
    _globals['_GETSYNCEDPOWERBIITEMSRESPONSE']._serialized_start = 3277
    _globals['_GETSYNCEDPOWERBIITEMSRESPONSE']._serialized_end = 3459
    _globals['_SYNCEDPOWERBIREPORT']._serialized_start = 3462
    _globals['_SYNCEDPOWERBIREPORT']._serialized_end = 3680
    _globals['_SYNCEDPOWERBIDATASET']._serialized_start = 3683
    _globals['_SYNCEDPOWERBIDATASET']._serialized_end = 3905
    _globals['_GETPOWERBIDATASETPREVIEWREQUEST']._serialized_start = 3908
    _globals['_GETPOWERBIDATASETPREVIEWREQUEST']._serialized_end = 4099
    _globals['_POWERBITABLEPREVIEW']._serialized_start = 4102
    _globals['_POWERBITABLEPREVIEW']._serialized_end = 4253
    _globals['_GETPOWERBIDATASETPREVIEWRESPONSE']._serialized_start = 4256
    _globals['_GETPOWERBIDATASETPREVIEWRESPONSE']._serialized_end = 4440
    _globals['_POWERBISERVICE']._serialized_start = 4443
    _globals['_POWERBISERVICE']._serialized_end = 5879