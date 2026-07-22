"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/dataset.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ..public import dataframe_pb2 as public_dot_dataframe__pb2
from ..public import identity_pb2 as public_dot_identity__pb2
from ..public import powerbi_pb2 as public_dot_powerbi__pb2
from ..public import tableau_pb2 as public_dot_tableau__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14public/dataset.proto\x12\x19textql.rpc.public.dataset\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x16public/dataframe.proto\x1a\x15public/identity.proto\x1a\x14public/powerbi.proto\x1a\x14public/tableau.proto"\x98\x01\n\rDatasetFolder\x12\x12\n\x04path\x18\x01 \x01(\tR\x04path\x128\n\x05owner\x18\x02 \x01(\x0b2".textql.rpc.identity.MemberPreviewR\x05owner\x129\n\ncreated_at\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt"\x8c\x07\n\x07Dataset\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12:\n\x04type\x18\x02 \x01(\x0e2&.textql.rpc.public.dataset.DatasetTypeR\x04type\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12\x18\n\x07version\x18\x04 \x01(\x05R\x07version\x12\x12\n\x04path\x18\x05 \x01(\tR\x04path\x128\n\x05owner\x18\x06 \x01(\x0b2".textql.rpc.identity.MemberPreviewR\x05owner\x12W\n\x10user_permissions\x18\x07 \x01(\x0e2,.textql.rpc.public.dataset.DatasetPermissionR\x0fuserPermissions\x129\n\ncreated_at\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt\x129\n\nupdated_at\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampR\tupdatedAt\x12>\n\nexpires_at\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampH\x01R\texpiresAt\x88\x01\x01\x12\x1c\n\tephemeral\x18\x0b \x01(\x08R\tephemeral\x12K\n\x0ctabular_file\x18\x0c \x01(\x0b2&.textql.rpc.public.dataset.TabularFileH\x00R\x0btabularFile\x12A\n\x08document\x18\r \x01(\x0b2#.textql.rpc.public.dataset.DocumentH\x00R\x08document\x12K\n\tdataframe\x18\x0e \x01(\x0b2+.textql.rpc.public.dataset.SandboxDataFrameH\x00R\tdataframe\x12K\n\x0ctableau_data\x18\x0f \x01(\x0b2&.textql.rpc.public.dataset.TableauDataH\x00R\x0btableauData\x12K\n\x0cpowerbi_data\x18\x10 \x01(\x0b2&.textql.rpc.public.dataset.PowerBIDataH\x00R\x0bpowerbiDataB\x06\n\x04dataB\r\n\x0b_expires_at"\xba\x01\n\x0bTabularFile\x12J\n\x08category\x18\x01 \x01(\x0e2..textql.rpc.public.dataset.TabularFileCategoryR\x08category\x12\x1b\n\trow_count\x18\x02 \x01(\x03R\x08rowCount\x12!\n\x0ccolumn_count\x18\x03 \x01(\x03R\x0bcolumnCount\x12\x1f\n\x0bsheet_count\x18\x04 \x01(\x05R\nsheetCount"J\n\x08Document\x12\x1f\n\x0bpreview_url\x18\x01 \x01(\tR\npreviewUrl\x12\x1d\n\npage_count\x18\x02 \x01(\x05R\tpageCount"R\n\x10SandboxDataFrame\x12>\n\x04info\x18\x01 \x01(\x0b2*.textql.rpc.public.dataframe.DataFrameInfoR\x04info"\x80\x02\n\x0bTableauData\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId\x12\x1d\n\nproject_id\x18\x02 \x01(\tR\tprojectId\x12!\n\x0cproject_name\x18\x03 \x01(\tR\x0bprojectName\x12<\n\x05views\x18\x04 \x03(\x0b2&.textql.rpc.public.tableau.TableauViewR\x05views\x12N\n\x0bdatasources\x18\x05 \x03(\x0b2,.textql.rpc.public.tableau.TableauDatasourceR\x0bdatasources"\x82\x02\n\x0bPowerBIData\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId\x12\x1d\n\nreport_ids\x18\x02 \x03(\tR\treportIds\x12\x1f\n\x0bdataset_ids\x18\x03 \x03(\tR\ndatasetIds\x12!\n\x0creport_names\x18\x04 \x03(\tR\x0breportNames\x12#\n\rdataset_names\x18\x05 \x03(\tR\x0cdatasetNames\x12!\n\x0cworkspace_id\x18\x06 \x01(\tR\x0bworkspaceId\x12%\n\x0eworkspace_name\x18\x07 \x01(\tR\rworkspaceName"J\n\x13CreateFolderRequest\x12\x1f\n\x0bparent_path\x18\x01 \x03(\tR\nparentPath\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name"*\n\x14CreateFolderResponse\x12\x12\n\x04path\x18\x01 \x03(\tR\x04path"\'\n\x11GetFoldersRequest\x12\x12\n\x04path\x18\x01 \x01(\tR\x04path"X\n\x12GetFoldersResponse\x12B\n\x07folders\x18\x01 \x03(\x0b2(.textql.rpc.public.dataset.DatasetFolderR\x07folders"\xf8\x01\n\x1dCreateUploadPresignUrlRequest\x12:\n\x04type\x18\x01 \x01(\x0e2&.textql.rpc.public.dataset.DatasetTypeR\x04type\x12\x1b\n\tfile_name\x18\x02 \x01(\tR\x08fileName\x12\x1f\n\x0bfolder_path\x18\x03 \x03(\tR\nfolderPath\x12\x1c\n\tephemeral\x18\x04 \x01(\x08R\tephemeral\x12+\n\x0fexpires_in_days\x18\x05 \x01(\rH\x00R\rexpiresInDays\x88\x01\x01B\x12\n\x10_expires_in_days"\x89\x01\n\x1eCreateUploadPresignUrlResponse\x12\x1d\n\ndataset_id\x18\x01 \x01(\tR\tdatasetId\x12\'\n\x0fdataset_version\x18\x02 \x01(\x05R\x0edatasetVersion\x12\x1f\n\x0bpresign_url\x18\x03 \x01(\tR\npresignUrl"h\n\x1eProcessUploadPresignUrlRequest\x12\x1d\n\ndataset_id\x18\x01 \x01(\tR\tdatasetId\x12\'\n\x0fdataset_version\x18\x02 \x01(\x05R\x0edatasetVersion"_\n\x1fProcessUploadPresignUrlResponse\x12<\n\x07dataset\x18\x01 \x01(\x0b2".textql.rpc.public.dataset.DatasetR\x07dataset"2\n\x11GetDatasetRequest\x12\x1d\n\ndataset_id\x18\x01 \x01(\tR\tdatasetId"R\n\x12GetDatasetResponse\x12<\n\x07dataset\x18\x01 \x01(\x0b2".textql.rpc.public.dataset.DatasetR\x07dataset"\x93\x03\n\x12GetDatasetsRequest\x12<\n\x05types\x18\x01 \x03(\x0e2&.textql.rpc.public.dataset.DatasetTypeR\x05types\x12\x1d\n\nowner_only\x18\x02 \x01(\x08R\townerOnly\x12-\n\x12include_subfolders\x18\x03 \x01(\x08R\x11includeSubfolders\x12\x17\n\x04path\x18\x04 \x01(\tH\x00R\x04path\x88\x01\x01\x12&\n\x0csearch_param\x18\x05 \x01(\tH\x01R\x0bsearchParam\x88\x01\x01\x12@\n\x04sort\x18\x06 \x01(\x0e2\'.textql.rpc.public.dataset.DatasetsSortH\x02R\x04sort\x88\x01\x01\x12\x19\n\x05limit\x18\x07 \x01(\x05H\x03R\x05limit\x88\x01\x01\x12\x1b\n\x06cursor\x18\x08 \x01(\tH\x04R\x06cursor\x88\x01\x01B\x07\n\x05_pathB\x0f\n\r_search_paramB\x07\n\x05_sortB\x08\n\x06_limitB\t\n\x07_cursor"U\n\x13GetDatasetsResponse\x12>\n\x08datasets\x18\x01 \x03(\x0b2".textql.rpc.public.dataset.DatasetR\x08datasets":\n\x17GetDatasetsByIdsRequest\x12\x1f\n\x0bdataset_ids\x18\x01 \x03(\tR\ndatasetIds"Z\n\x18GetDatasetsByIdsResponse\x12>\n\x08datasets\x18\x01 \x03(\x0b2".textql.rpc.public.dataset.DatasetR\x08datasets"\xd6\x01\n\x14ExportDatasetRequest\x12\x1d\n\ndataset_id\x18\x01 \x01(\tR\tdatasetId\x12W\n\x10preferred_format\x18\x02 \x01(\x0e2\'.textql.rpc.public.dataset.ExportFormatH\x00R\x0fpreferredFormat\x88\x01\x01\x12"\n\nversion_id\x18\x03 \x01(\x05H\x01R\tversionId\x88\x01\x01B\x13\n\x11_preferred_formatB\r\n\x0b_version_id"<\n\x15ExportDatasetResponse\x12#\n\rpresigned_url\x18\x01 \x01(\tR\x0cpresignedUrl"\xd7\x01\n\x17GetDatasetValuesRequest\x12\x1d\n\ndataset_id\x18\x01 \x01(\tR\tdatasetId\x12"\n\nversion_id\x18\x02 \x01(\x05H\x00R\tversionId\x88\x01\x01\x12\x19\n\x05limit\x18\x03 \x01(\x05H\x01R\x05limit\x88\x01\x01\x12\x17\n\x04page\x18\x04 \x01(\x05H\x02R\x04page\x88\x01\x01\x12\x19\n\x05sheet\x18\x05 \x01(\x05H\x03R\x05sheet\x88\x01\x01B\r\n\x0b_version_idB\x08\n\x06_limitB\x07\n\x05_pageB\x08\n\x06_sheet"\x88\x01\n\x18GetDatasetValuesResponse\x126\n\x02df\x18\x01 \x01(\x0b2&.textql.rpc.public.dataframe.DataFrameR\x02df\x12\x19\n\x08num_cols\x18\x02 \x01(\x03R\x07numCols\x12\x19\n\x08num_rows\x18\x03 \x01(\x03R\x07numRows"j\n\x16GetDatasetStatsRequest\x12\x1d\n\ndataset_id\x18\x01 \x01(\tR\tdatasetId\x12"\n\nversion_id\x18\x02 \x01(\x05H\x00R\tversionId\x88\x01\x01B\r\n\x0b_version_id"\x19\n\x17GetDatasetStatsResponse"\xc5\x02\n\x1bCreateTableauDatasetRequest\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x1f\n\x0bfolder_path\x18\x03 \x03(\tR\nfolderPath\x12\x1d\n\nproject_id\x18\x04 \x01(\tR\tprojectId\x12!\n\x0cproject_name\x18\x05 \x01(\tR\x0bprojectName\x12<\n\x05views\x18\x06 \x03(\x0b2&.textql.rpc.public.tableau.TableauViewR\x05views\x12N\n\x0bdatasources\x18\x07 \x03(\x0b2,.textql.rpc.public.tableau.TableauDatasourceR\x0bdatasources"\\\n\x1cCreateTableauDatasetResponse\x12<\n\x07dataset\x18\x01 \x01(\x0b2".textql.rpc.public.dataset.DatasetR\x07dataset"\xca\x02\n\x1bCreatePowerBIDatasetRequest\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x1f\n\x0bfolder_path\x18\x03 \x03(\tR\nfolderPath\x12!\n\x0cworkspace_id\x18\x04 \x01(\tR\x0bworkspaceId\x12%\n\x0eworkspace_name\x18\x05 \x01(\tR\rworkspaceName\x12B\n\x07reports\x18\x06 \x03(\x0b2(.textql.rpc.public.powerbi.PowerBIReportR\x07reports\x12E\n\x08datasets\x18\x07 \x03(\x0b2).textql.rpc.public.powerbi.PowerBIDatasetR\x08datasets"\\\n\x1cCreatePowerBIDatasetResponse\x12<\n\x07dataset\x18\x01 \x01(\x0b2".textql.rpc.public.dataset.DatasetR\x07dataset"W\n\x14UpdateDatasetRequest\x12\x1d\n\ndataset_id\x18\x01 \x01(\tR\tdatasetId\x12\x17\n\x04name\x18\x02 \x01(\tH\x00R\x04name\x88\x01\x01B\x07\n\x05_name"U\n\x15UpdateDatasetResponse\x12<\n\x07dataset\x18\x01 \x01(\x0b2".textql.rpc.public.dataset.DatasetR\x07dataset"5\n\x14DeleteDatasetRequest\x12\x1d\n\ndataset_id\x18\x01 \x01(\tR\tdatasetId"1\n\x15DeleteDatasetResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success*\x9b\x01\n\x0bDatasetType\x12\x10\n\x0cTYPE_UNKNOWN\x10\x00\x12\x10\n\x0cTYPE_TABULAR\x10\x01\x12\x12\n\x0eTYPE_DATAFRAME\x10\x02\x12\x11\n\rTYPE_DOCUMENT\x10\x03\x12\x10\n\x0cTYPE_TABLEAU\x10\x04\x12\x0e\n\nTYPE_IMAGE\x10\x05\x12\r\n\tTYPE_TEXT\x10\x06\x12\x10\n\x0cTYPE_POWERBI\x10\x07*k\n\x11DatasetPermission\x12\x16\n\x12PERMISSION_UNKNOWN\x10\x00\x12\x13\n\x0fPERMISSION_READ\x10\x01\x12\x13\n\x0fPERMISSION_EDIT\x10\x02\x12\x14\n\x10PERMISSION_ADMIN\x10\x03*\x9c\x01\n\x13TabularFileCategory\x12\x14\n\x10CATEGORY_UNKNOWN\x10\x00\x12\x10\n\x0cCATEGORY_CSV\x10\x01\x12\x10\n\x0cCATEGORY_TSV\x10\x02\x12\x11\n\rCATEGORY_XLSX\x10\x03\x12\x10\n\x0cCATEGORY_XLS\x10\x04\x12\x14\n\x10CATEGORY_PARQUET\x10\x05\x12\x10\n\x0cCATEGORY_ODS\x10\x06*U\n\x0cDatasetsSort\x12\x10\n\x0cSORT_UNKNOWN\x10\x00\x12\x0f\n\x0bSORT_LATEST\x10\x01\x12\x0f\n\x0bSORT_OLDEST\x10\x02\x12\x11\n\rSORT_RELEVANT\x10\x03*X\n\x0cExportFormat\x12\x12\n\x0eFORMAT_UNKNOWN\x10\x00\x12\x0e\n\nFORMAT_CSV\x10\x01\x12\x10\n\x0cFORMAT_EXCEL\x10\x02\x12\x12\n\x0eFORMAT_PARQUET\x10\x032\xfb\r\n\x0eDatasetService\x12o\n\x0cCreateFolder\x12..textql.rpc.public.dataset.CreateFolderRequest\x1a/.textql.rpc.public.dataset.CreateFolderResponse\x12n\n\nGetFolders\x12,.textql.rpc.public.dataset.GetFoldersRequest\x1a-.textql.rpc.public.dataset.GetFoldersResponse"\x03\x90\x02\x01\x12\x8d\x01\n\x16CreateUploadPresignUrl\x128.textql.rpc.public.dataset.CreateUploadPresignUrlRequest\x1a9.textql.rpc.public.dataset.CreateUploadPresignUrlResponse\x12\x90\x01\n\x17ProcessUploadPresignUrl\x129.textql.rpc.public.dataset.ProcessUploadPresignUrlRequest\x1a:.textql.rpc.public.dataset.ProcessUploadPresignUrlResponse\x12n\n\nGetDataset\x12,.textql.rpc.public.dataset.GetDatasetRequest\x1a-.textql.rpc.public.dataset.GetDatasetResponse"\x03\x90\x02\x01\x12q\n\x0bGetDatasets\x12-.textql.rpc.public.dataset.GetDatasetsRequest\x1a..textql.rpc.public.dataset.GetDatasetsResponse"\x03\x90\x02\x01\x12\x80\x01\n\x10GetDatasetsByIds\x122.textql.rpc.public.dataset.GetDatasetsByIdsRequest\x1a3.textql.rpc.public.dataset.GetDatasetsByIdsResponse"\x03\x90\x02\x01\x12w\n\rUpdateDataset\x12/.textql.rpc.public.dataset.UpdateDatasetRequest\x1a0.textql.rpc.public.dataset.UpdateDatasetResponse"\x03\x90\x02\x02\x12w\n\rExportDataset\x12/.textql.rpc.public.dataset.ExportDatasetRequest\x1a0.textql.rpc.public.dataset.ExportDatasetResponse"\x03\x90\x02\x01\x12\x80\x01\n\x10GetDatasetValues\x122.textql.rpc.public.dataset.GetDatasetValuesRequest\x1a3.textql.rpc.public.dataset.GetDatasetValuesResponse"\x03\x90\x02\x01\x12}\n\x0fGetDatasetStats\x121.textql.rpc.public.dataset.GetDatasetStatsRequest\x1a2.textql.rpc.public.dataset.GetDatasetStatsResponse"\x03\x90\x02\x01\x12\x87\x01\n\x14CreateTableauDataset\x126.textql.rpc.public.dataset.CreateTableauDatasetRequest\x1a7.textql.rpc.public.dataset.CreateTableauDatasetResponse\x12\x87\x01\n\x14CreatePowerBIDataset\x126.textql.rpc.public.dataset.CreatePowerBIDatasetRequest\x1a7.textql.rpc.public.dataset.CreatePowerBIDatasetResponse\x12w\n\rDeleteDataset\x12/.textql.rpc.public.dataset.DeleteDatasetRequest\x1a0.textql.rpc.public.dataset.DeleteDatasetResponse"\x03\x90\x02\x02b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.dataset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['GetFolders']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['GetFolders']._serialized_options = b'\x90\x02\x01'
    _globals['_DATASETSERVICE'].methods_by_name['GetDataset']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['GetDataset']._serialized_options = b'\x90\x02\x01'
    _globals['_DATASETSERVICE'].methods_by_name['GetDatasets']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['GetDatasets']._serialized_options = b'\x90\x02\x01'
    _globals['_DATASETSERVICE'].methods_by_name['GetDatasetsByIds']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['GetDatasetsByIds']._serialized_options = b'\x90\x02\x01'
    _globals['_DATASETSERVICE'].methods_by_name['UpdateDataset']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['UpdateDataset']._serialized_options = b'\x90\x02\x02'
    _globals['_DATASETSERVICE'].methods_by_name['ExportDataset']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['ExportDataset']._serialized_options = b'\x90\x02\x01'
    _globals['_DATASETSERVICE'].methods_by_name['GetDatasetValues']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['GetDatasetValues']._serialized_options = b'\x90\x02\x01'
    _globals['_DATASETSERVICE'].methods_by_name['GetDatasetStats']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['GetDatasetStats']._serialized_options = b'\x90\x02\x01'
    _globals['_DATASETSERVICE'].methods_by_name['DeleteDataset']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['DeleteDataset']._serialized_options = b'\x90\x02\x02'
    _globals['_DATASETTYPE']._serialized_start = 5639
    _globals['_DATASETTYPE']._serialized_end = 5794
    _globals['_DATASETPERMISSION']._serialized_start = 5796
    _globals['_DATASETPERMISSION']._serialized_end = 5903
    _globals['_TABULARFILECATEGORY']._serialized_start = 5906
    _globals['_TABULARFILECATEGORY']._serialized_end = 6062
    _globals['_DATASETSSORT']._serialized_start = 6064
    _globals['_DATASETSSORT']._serialized_end = 6149
    _globals['_EXPORTFORMAT']._serialized_start = 6151
    _globals['_EXPORTFORMAT']._serialized_end = 6239
    _globals['_DATASETFOLDER']._serialized_start = 176
    _globals['_DATASETFOLDER']._serialized_end = 328
    _globals['_DATASET']._serialized_start = 331
    _globals['_DATASET']._serialized_end = 1239
    _globals['_TABULARFILE']._serialized_start = 1242
    _globals['_TABULARFILE']._serialized_end = 1428
    _globals['_DOCUMENT']._serialized_start = 1430
    _globals['_DOCUMENT']._serialized_end = 1504
    _globals['_SANDBOXDATAFRAME']._serialized_start = 1506
    _globals['_SANDBOXDATAFRAME']._serialized_end = 1588
    _globals['_TABLEAUDATA']._serialized_start = 1591
    _globals['_TABLEAUDATA']._serialized_end = 1847
    _globals['_POWERBIDATA']._serialized_start = 1850
    _globals['_POWERBIDATA']._serialized_end = 2108
    _globals['_CREATEFOLDERREQUEST']._serialized_start = 2110
    _globals['_CREATEFOLDERREQUEST']._serialized_end = 2184
    _globals['_CREATEFOLDERRESPONSE']._serialized_start = 2186
    _globals['_CREATEFOLDERRESPONSE']._serialized_end = 2228
    _globals['_GETFOLDERSREQUEST']._serialized_start = 2230
    _globals['_GETFOLDERSREQUEST']._serialized_end = 2269
    _globals['_GETFOLDERSRESPONSE']._serialized_start = 2271
    _globals['_GETFOLDERSRESPONSE']._serialized_end = 2359
    _globals['_CREATEUPLOADPRESIGNURLREQUEST']._serialized_start = 2362
    _globals['_CREATEUPLOADPRESIGNURLREQUEST']._serialized_end = 2610
    _globals['_CREATEUPLOADPRESIGNURLRESPONSE']._serialized_start = 2613
    _globals['_CREATEUPLOADPRESIGNURLRESPONSE']._serialized_end = 2750
    _globals['_PROCESSUPLOADPRESIGNURLREQUEST']._serialized_start = 2752
    _globals['_PROCESSUPLOADPRESIGNURLREQUEST']._serialized_end = 2856
    _globals['_PROCESSUPLOADPRESIGNURLRESPONSE']._serialized_start = 2858
    _globals['_PROCESSUPLOADPRESIGNURLRESPONSE']._serialized_end = 2953
    _globals['_GETDATASETREQUEST']._serialized_start = 2955
    _globals['_GETDATASETREQUEST']._serialized_end = 3005
    _globals['_GETDATASETRESPONSE']._serialized_start = 3007
    _globals['_GETDATASETRESPONSE']._serialized_end = 3089
    _globals['_GETDATASETSREQUEST']._serialized_start = 3092
    _globals['_GETDATASETSREQUEST']._serialized_end = 3495
    _globals['_GETDATASETSRESPONSE']._serialized_start = 3497
    _globals['_GETDATASETSRESPONSE']._serialized_end = 3582
    _globals['_GETDATASETSBYIDSREQUEST']._serialized_start = 3584
    _globals['_GETDATASETSBYIDSREQUEST']._serialized_end = 3642
    _globals['_GETDATASETSBYIDSRESPONSE']._serialized_start = 3644
    _globals['_GETDATASETSBYIDSRESPONSE']._serialized_end = 3734
    _globals['_EXPORTDATASETREQUEST']._serialized_start = 3737
    _globals['_EXPORTDATASETREQUEST']._serialized_end = 3951
    _globals['_EXPORTDATASETRESPONSE']._serialized_start = 3953
    _globals['_EXPORTDATASETRESPONSE']._serialized_end = 4013
    _globals['_GETDATASETVALUESREQUEST']._serialized_start = 4016
    _globals['_GETDATASETVALUESREQUEST']._serialized_end = 4231
    _globals['_GETDATASETVALUESRESPONSE']._serialized_start = 4234
    _globals['_GETDATASETVALUESRESPONSE']._serialized_end = 4370
    _globals['_GETDATASETSTATSREQUEST']._serialized_start = 4372
    _globals['_GETDATASETSTATSREQUEST']._serialized_end = 4478
    _globals['_GETDATASETSTATSRESPONSE']._serialized_start = 4480
    _globals['_GETDATASETSTATSRESPONSE']._serialized_end = 4505
    _globals['_CREATETABLEAUDATASETREQUEST']._serialized_start = 4508
    _globals['_CREATETABLEAUDATASETREQUEST']._serialized_end = 4833
    _globals['_CREATETABLEAUDATASETRESPONSE']._serialized_start = 4835
    _globals['_CREATETABLEAUDATASETRESPONSE']._serialized_end = 4927
    _globals['_CREATEPOWERBIDATASETREQUEST']._serialized_start = 4930
    _globals['_CREATEPOWERBIDATASETREQUEST']._serialized_end = 5260
    _globals['_CREATEPOWERBIDATASETRESPONSE']._serialized_start = 5262
    _globals['_CREATEPOWERBIDATASETRESPONSE']._serialized_end = 5354
    _globals['_UPDATEDATASETREQUEST']._serialized_start = 5356
    _globals['_UPDATEDATASETREQUEST']._serialized_end = 5443
    _globals['_UPDATEDATASETRESPONSE']._serialized_start = 5445
    _globals['_UPDATEDATASETRESPONSE']._serialized_end = 5530
    _globals['_DELETEDATASETREQUEST']._serialized_start = 5532
    _globals['_DELETEDATASETREQUEST']._serialized_end = 5585
    _globals['_DELETEDATASETRESPONSE']._serialized_start = 5587
    _globals['_DELETEDATASETRESPONSE']._serialized_end = 5636
    _globals['_DATASETSERVICE']._serialized_start = 6242
    _globals['_DATASETSERVICE']._serialized_end = 8029