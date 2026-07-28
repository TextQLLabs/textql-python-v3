# pylint: skip-file
# mypy: ignore-errors
# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'textable.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0etextable.proto\x12\x13textql.rpc.textable\x1a\x19google/protobuf/any.proto"\x84\x02\n\x14LoadToSandboxRequest\x12\x16\n\x06source\x18\x01 \x01(\tR\x06source\x12<\n\x08csv_data\x18\x02 \x01(\x0b2\x1f.textql.rpc.textable.CSVRequestH\x00R\x07csvData\x12<\n\x08sql_data\x18\x03 \x01(\x0b2\x1f.textql.rpc.textable.SQLRequestH\x00R\x07sqlData\x12H\n\x0ctableau_data\x18\x04 \x01(\x0b2#.textql.rpc.textable.TableauRequestH\x00R\x0btableauDataB\x0e\n\x0crequest_data"\xa9\x01\n\x15LoadToSandboxResponse\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04head\x18\x02 \x01(\tR\x04head\x12\x12\n\x04size\x18\x03 \x01(\x03R\x04size\x12$\n\x0eloaded_in_full\x18\x04 \x01(\x08R\x0cloadedInFull\x12\x18\n\x07preview\x18\x05 \x01(\tR\x07preview\x12\x14\n\x05error\x18\x06 \x01(\tR\x05error"\xa9\x02\n\x14QueryTextableRequest\x12\x16\n\x06source\x18\x01 \x01(\tR\x06source\x12<\n\x08csv_data\x18\x02 \x01(\x0b2\x1f.textql.rpc.textable.CSVRequestH\x00R\x07csvData\x12<\n\x08sql_data\x18\x03 \x01(\x0b2\x1f.textql.rpc.textable.SQLRequestH\x00R\x07sqlData\x12H\n\x0ctableau_data\x18\x04 \x01(\x0b2#.textql.rpc.textable.TableauRequestH\x00R\x0btableauData\x12#\n\rinclude_stats\x18\x05 \x01(\x08R\x0cincludeStatsB\x0e\n\x0crequest_data"\xdf\x01\n\x15QueryTextableResponse\x12!\n\x0ccolumn_names\x18\x01 \x03(\tR\x0bcolumnNames\x12!\n\x0ccolumn_types\x18\x02 \x03(\tR\x0bcolumnTypes\x120\n\x06values\x18\x03 \x03(\x0b2\x18.textql.rpc.textable.RowR\x06values\x12\x16\n\x06length\x18\x04 \x01(\x05R\x06length\x126\n\x05stats\x18\x05 \x03(\x0b2 .textql.rpc.textable.ColumnStatsR\x05stats"3\n\x03Row\x12,\n\x06values\x18\x01 \x03(\x0b2\x14.google.protobuf.AnyR\x06values"\x84\x02\n\x14RetrieveStatsRequest\x12\x16\n\x06source\x18\x01 \x01(\tR\x06source\x12<\n\x08csv_data\x18\x02 \x01(\x0b2\x1f.textql.rpc.textable.CSVRequestH\x00R\x07csvData\x12<\n\x08sql_data\x18\x03 \x01(\x0b2\x1f.textql.rpc.textable.SQLRequestH\x00R\x07sqlData\x12H\n\x0ctableau_data\x18\x04 \x01(\x0b2#.textql.rpc.textable.TableauRequestH\x00R\x0btableauDataB\x0e\n\x0crequest_data"]\n\x0bStatsResult\x12\x16\n\x06length\x18\x01 \x01(\x05R\x06length\x126\n\x05stats\x18\x02 \x03(\x0b2 .textql.rpc.textable.ColumnStatsR\x05stats"\xa9\x02\n\x14CheckTextableRequest\x12\x16\n\x06source\x18\x01 \x01(\tR\x06source\x12<\n\x08csv_data\x18\x02 \x01(\x0b2\x1f.textql.rpc.textable.CSVRequestH\x00R\x07csvData\x12<\n\x08sql_data\x18\x03 \x01(\x0b2\x1f.textql.rpc.textable.SQLRequestH\x00R\x07sqlData\x12H\n\x0ctableau_data\x18\x04 \x01(\x0b2#.textql.rpc.textable.TableauRequestH\x00R\x0btableauData\x12#\n\rinclude_stats\x18\x05 \x01(\x08R\x0cincludeStatsB\x0e\n\x0crequest_data"\xad\x01\n\x15CheckTextableResponse\x12!\n\x0ccolumn_names\x18\x01 \x03(\tR\x0bcolumnNames\x12!\n\x0ccolumn_types\x18\x02 \x03(\tR\x0bcolumnTypes\x12\x16\n\x06length\x18\x03 \x01(\x05R\x06length\x126\n\x05stats\x18\x04 \x03(\x0b2 .textql.rpc.textable.ColumnStatsR\x05stats"\xbe\x01\n\nCSVRequest\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12\x14\n\x05limit\x18\x02 \x01(\x05R\x05limit\x12\x12\n\x04page\x18\x03 \x01(\x05R\x04page\x122\n\x15histogram_bucket_size\x18\x04 \x01(\x05R\x13histogramBucketSize\x12\x18\n\x07timeout\x18\x05 \x01(\tR\x07timeout\x12&\n\x0fdata_frame_name\x18\x06 \x01(\tR\rdataFrameName"\xd8\x02\n\nSQLRequest\x12\x14\n\x05query\x18\x01 \x01(\tR\x05query\x12\'\n\x0fdeployment_type\x18\x02 \x01(\tR\x0edeploymentType\x12?\n\ndeployment\x18\x03 \x01(\x0b2\x1f.textql.rpc.textable.DeploymentR\ndeployment\x12*\n\x11force_exact_query\x18\x04 \x01(\x08R\x0fforceExactQuery\x12\x14\n\x05limit\x18\x05 \x01(\x05R\x05limit\x12\x12\n\x04page\x18\x06 \x01(\x05R\x04page\x122\n\x15histogram_bucket_size\x18\x07 \x01(\x05R\x13histogramBucketSize\x12\x18\n\x07timeout\x18\x08 \x01(\tR\x07timeout\x12&\n\x0fdata_frame_name\x18\t \x01(\tR\rdataFrameName"\x8a\x02\n\x0eTableauRequest\x12?\n\ndeployment\x18\x01 \x01(\x0b2\x1f.textql.rpc.textable.DeploymentR\ndeployment\x12\x17\n\x07view_id\x18\x02 \x01(\tR\x06viewId\x12\x14\n\x05limit\x18\x03 \x01(\x05R\x05limit\x12\x12\n\x04page\x18\x04 \x01(\x05R\x04page\x122\n\x15histogram_bucket_size\x18\x05 \x01(\x05R\x13histogramBucketSize\x12\x18\n\x07timeout\x18\x06 \x01(\tR\x07timeout\x12&\n\x0fdata_frame_name\x18\x07 \x01(\tR\rdataFrameName"&\n\nDeployment\x12\x18\n\x07dialect\x18\x01 \x01(\tR\x07dialect"\xc9\x01\n\x0bColumnStats\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type\x12\x10\n\x03min\x18\x03 \x01(\x01R\x03min\x12\x10\n\x03max\x18\x04 \x01(\x01R\x03max\x12\x12\n\x04mean\x18\x05 \x01(\x01R\x04mean\x12\x16\n\x06median\x18\x06 \x01(\x01R\x06median\x12B\n\thistogram\x18\x07 \x03(\x0b2$.textql.rpc.textable.HistogramBucketR\thistogram"M\n\x0fHistogramBucket\x12\x10\n\x03low\x18\x01 \x01(\x01R\x03low\x12\x12\n\x04high\x18\x02 \x01(\x01R\x04high\x12\x14\n\x05count\x18\x03 \x01(\x05R\x05count2\xaf\x03\n\x0fTextableService\x12h\n\rLoadToSandbox\x12).textql.rpc.textable.LoadToSandboxRequest\x1a*.textql.rpc.textable.LoadToSandboxResponse"\x00\x12h\n\rQueryTextable\x12).textql.rpc.textable.QueryTextableRequest\x1a*.textql.rpc.textable.QueryTextableResponse"\x00\x12^\n\rRetrieveStats\x12).textql.rpc.textable.RetrieveStatsRequest\x1a .textql.rpc.textable.StatsResult"\x00\x12h\n\rCheckTextable\x12).textql.rpc.textable.CheckTextableRequest\x1a*.textql.rpc.textable.CheckTextableResponse"\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'textable_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_LOADTOSANDBOXREQUEST']._serialized_start = 67
    _globals['_LOADTOSANDBOXREQUEST']._serialized_end = 327
    _globals['_LOADTOSANDBOXRESPONSE']._serialized_start = 330
    _globals['_LOADTOSANDBOXRESPONSE']._serialized_end = 499
    _globals['_QUERYTEXTABLEREQUEST']._serialized_start = 502
    _globals['_QUERYTEXTABLEREQUEST']._serialized_end = 799
    _globals['_QUERYTEXTABLERESPONSE']._serialized_start = 802
    _globals['_QUERYTEXTABLERESPONSE']._serialized_end = 1025
    _globals['_ROW']._serialized_start = 1027
    _globals['_ROW']._serialized_end = 1078
    _globals['_RETRIEVESTATSREQUEST']._serialized_start = 1081
    _globals['_RETRIEVESTATSREQUEST']._serialized_end = 1341
    _globals['_STATSRESULT']._serialized_start = 1343
    _globals['_STATSRESULT']._serialized_end = 1436
    _globals['_CHECKTEXTABLEREQUEST']._serialized_start = 1439
    _globals['_CHECKTEXTABLEREQUEST']._serialized_end = 1736
    _globals['_CHECKTEXTABLERESPONSE']._serialized_start = 1739
    _globals['_CHECKTEXTABLERESPONSE']._serialized_end = 1912
    _globals['_CSVREQUEST']._serialized_start = 1915
    _globals['_CSVREQUEST']._serialized_end = 2105
    _globals['_SQLREQUEST']._serialized_start = 2108
    _globals['_SQLREQUEST']._serialized_end = 2452
    _globals['_TABLEAUREQUEST']._serialized_start = 2455
    _globals['_TABLEAUREQUEST']._serialized_end = 2721
    _globals['_DEPLOYMENT']._serialized_start = 2723
    _globals['_DEPLOYMENT']._serialized_end = 2761
    _globals['_COLUMNSTATS']._serialized_start = 2764
    _globals['_COLUMNSTATS']._serialized_end = 2965
    _globals['_HISTOGRAMBUCKET']._serialized_start = 2967
    _globals['_HISTOGRAMBUCKET']._serialized_end = 3044
    _globals['_TEXTABLESERVICE']._serialized_start = 3047
    _globals['_TEXTABLESERVICE']._serialized_end = 3478