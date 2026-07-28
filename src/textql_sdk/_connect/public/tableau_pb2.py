# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
# pylint: skip-file
# mypy: ignore-errors
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/tableau.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14public/tableau.proto\x12\x19textql.rpc.public.tableau\x1a\x1fgoogle/protobuf/timestamp.proto"\x9a\x02\n\x1cTestTableauConnectionRequest\x12&\n\x0cconnector_id\x18\x01 \x01(\x05H\x00R\x0bconnectorId\x88\x01\x01\x12"\n\nserver_url\x18\x02 \x01(\tH\x01R\tserverUrl\x88\x01\x01\x12 \n\tsite_name\x18\x03 \x01(\tH\x02R\x08siteName\x88\x01\x01\x12\x1e\n\x08pat_name\x18\x04 \x01(\tH\x03R\x07patName\x88\x01\x01\x12"\n\npat_secret\x18\x05 \x01(\tH\x04R\tpatSecret\x88\x01\x01B\x0f\n\r_connector_idB\r\n\x0b_server_urlB\x0c\n\n_site_nameB\x0b\n\t_pat_nameB\r\n\x0b_pat_secret"O\n\x1dTestTableauConnectionResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x14\n\x05error\x18\x02 \x01(\tR\x05error"\xa9\x02\n\x0eTableauProject\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0bdescription\x18\x03 \x01(\tR\x0bdescription\x129\n\ncreated_at\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt\x129\n\nupdated_at\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampR\tupdatedAt\x12/\n\x13content_permissions\x18\x06 \x01(\tR\x12contentPermissions\x12*\n\x11parent_project_id\x18\x07 \x01(\tR\x0fparentProjectId"?\n\x1aListTableauProjectsRequest\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId"d\n\x1bListTableauProjectsResponse\x12E\n\x08projects\x18\x01 \x03(\x0b2).textql.rpc.public.tableau.TableauProjectR\x08projects"\xed\x01\n\x0fTableauWorkbook\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12!\n\x0cproject_name\x18\x03 \x01(\tR\x0bprojectName\x12\x1d\n\nproject_id\x18\x04 \x01(\tR\tprojectId\x129\n\ncreated_at\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt\x129\n\nupdated_at\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampR\tupdatedAt"\x82\x01\n\x1bListTableauWorkbooksRequest\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId\x12\x1d\n\nproject_id\x18\x02 \x01(\tR\tprojectId\x12!\n\x0cproject_name\x18\x03 \x01(\tR\x0bprojectName"h\n\x1cListTableauWorkbooksResponse\x12H\n\tworkbooks\x18\x01 \x03(\x0b2*.textql.rpc.public.tableau.TableauWorkbookR\tworkbooks"\xab\x02\n\x0bTableauView\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x1f\n\x0bcontent_url\x18\x03 \x01(\tR\ncontentUrl\x12\x1f\n\x0bworkbook_id\x18\x04 \x01(\tR\nworkbookId\x12#\n\rworkbook_name\x18\x05 \x01(\tR\x0cworkbookName\x129\n\ncreated_at\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt\x129\n\nupdated_at\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampR\tupdatedAt\x12\x1b\n\tembed_url\x18\x08 \x01(\tR\x08embedUrl"\x82\x01\n\x17ListTableauViewsRequest\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId\x12\x1f\n\x0bworkbook_id\x18\x02 \x01(\tR\nworkbookId\x12#\n\rworkbook_name\x18\x03 \x01(\tR\x0cworkbookName"X\n\x18ListTableauViewsResponse\x12<\n\x05views\x18\x01 \x03(\x0b2&.textql.rpc.public.tableau.TableauViewR\x05views"\xa6\x02\n\x11TableauDatasource\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x12\n\x04type\x18\x03 \x01(\tR\x04type\x129\n\ncreated_at\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt\x129\n\nupdated_at\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampR\tupdatedAt\x12!\n\x0cis_published\x18\x06 \x01(\x08R\x0bisPublished\x12\x1d\n\nproject_id\x18\x07 \x01(\tR\tprojectId\x12!\n\x0cproject_name\x18\x08 \x01(\tR\x0bprojectName"\x90\x01\n\x1dListTableauDatasourcesRequest\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId\x12\x1f\n\nproject_id\x18\x02 \x01(\tH\x00R\tprojectId\x12!\n\x0bworkbook_id\x18\x03 \x01(\tH\x00R\nworkbookIdB\x08\n\x06filter"p\n\x1eListTableauDatasourcesResponse\x12N\n\x0bdatasources\x18\x01 \x03(\x0b2,.textql.rpc.public.tableau.TableauDatasourceR\x0bdatasources"\xf1\x01\n\x12TableauStarredItem\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId\x12G\n\titem_type\x18\x02 \x01(\x0e2*.textql.rpc.public.tableau.TableauItemTypeR\x08itemType\x12\x17\n\x07item_id\x18\x03 \x01(\tR\x06itemId\x12\x1b\n\titem_name\x18\x04 \x01(\tR\x08itemName\x129\n\ncreated_at\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt"\xba\x01\n\x16StarTableauItemRequest\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId\x12G\n\titem_type\x18\x02 \x01(\x0e2*.textql.rpc.public.tableau.TableauItemTypeR\x08itemType\x12\x17\n\x07item_id\x18\x03 \x01(\tR\x06itemId\x12\x1b\n\titem_name\x18\x04 \x01(\tR\x08itemName"3\n\x17StarTableauItemResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success"\x9f\x01\n\x18UnstarTableauItemRequest\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId\x12G\n\titem_type\x18\x02 \x01(\x0e2*.textql.rpc.public.tableau.TableauItemTypeR\x08itemType\x12\x17\n\x07item_id\x18\x03 \x01(\tR\x06itemId"5\n\x19UnstarTableauItemResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success"B\n\x1dGetStarredTableauItemsRequest\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId"e\n\x1eGetStarredTableauItemsResponse\x12C\n\x05items\x18\x01 \x03(\x0b2-.textql.rpc.public.tableau.TableauStarredItemR\x05items">\n\x1dGetCollectionThumbnailRequest\x12\x1d\n\ndataset_id\x18\x01 \x01(\tR\tdatasetId"=\n\x1eGetCollectionThumbnailResponse\x12\x1b\n\timage_url\x18\x01 \x01(\tR\x08imageUrl"W\n\x19GenerateEmbedTokenRequest\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId\x12\x17\n\x07view_id\x18\x02 \x01(\tR\x06viewId"O\n\x1aGenerateEmbedTokenResponse\x12\x14\n\x05token\x18\x01 \x01(\tR\x05token\x12\x1b\n\tembed_url\x18\x02 \x01(\tR\x08embedUrl"A\n\x1cGetConnectedAppStatusRequest\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId"\xae\x01\n\x1dGetConnectedAppStatusResponse\x12\x1e\n\nconfigured\x18\x01 \x01(\x08R\nconfigured\x12\x19\n\x08app_name\x18\x02 \x01(\tR\x07appName\x12(\n\x10client_id_suffix\x18\x03 \x01(\tR\x0eclientIdSuffix\x12(\n\x10secret_id_suffix\x18\x04 \x01(\tR\x0esecretIdSuffix"=\n\x18ResetConnectedAppRequest\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId"5\n\x19ResetConnectedAppResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success"@\n\x1fRefreshTableauCollectionRequest\x12\x1d\n\ndataset_id\x18\x01 \x01(\tR\tdatasetId"p\n RefreshTableauCollectionResponse\x12\x1f\n\x0bviews_count\x18\x01 \x01(\x05R\nviewsCount\x12+\n\x11datasources_count\x18\x02 \x01(\x05R\x10datasourcesCount*\x85\x01\n\x0fTableauItemType\x12\x15\n\x11ITEM_TYPE_UNKNOWN\x10\x00\x12\x15\n\x11ITEM_TYPE_PROJECT\x10\x01\x12\x16\n\x12ITEM_TYPE_WORKBOOK\x10\x02\x12\x12\n\x0eITEM_TYPE_VIEW\x10\x03\x12\x18\n\x14ITEM_TYPE_DATASOURCE\x10\x042\x98\x0e\n\x0eTableauService\x12\x8c\x01\n\x15TestTableauConnection\x127.textql.rpc.public.tableau.TestTableauConnectionRequest\x1a8.textql.rpc.public.tableau.TestTableauConnectionResponse"\x00\x12\x86\x01\n\x13ListTableauProjects\x125.textql.rpc.public.tableau.ListTableauProjectsRequest\x1a6.textql.rpc.public.tableau.ListTableauProjectsResponse"\x00\x12\x89\x01\n\x14ListTableauWorkbooks\x126.textql.rpc.public.tableau.ListTableauWorkbooksRequest\x1a7.textql.rpc.public.tableau.ListTableauWorkbooksResponse"\x00\x12}\n\x10ListTableauViews\x122.textql.rpc.public.tableau.ListTableauViewsRequest\x1a3.textql.rpc.public.tableau.ListTableauViewsResponse"\x00\x12\x8f\x01\n\x16ListTableauDatasources\x128.textql.rpc.public.tableau.ListTableauDatasourcesRequest\x1a9.textql.rpc.public.tableau.ListTableauDatasourcesResponse"\x00\x12z\n\x0fStarTableauItem\x121.textql.rpc.public.tableau.StarTableauItemRequest\x1a2.textql.rpc.public.tableau.StarTableauItemResponse"\x00\x12\x80\x01\n\x11UnstarTableauItem\x123.textql.rpc.public.tableau.UnstarTableauItemRequest\x1a4.textql.rpc.public.tableau.UnstarTableauItemResponse"\x00\x12\x8f\x01\n\x16GetStarredTableauItems\x128.textql.rpc.public.tableau.GetStarredTableauItemsRequest\x1a9.textql.rpc.public.tableau.GetStarredTableauItemsResponse"\x00\x12\x8f\x01\n\x16GetCollectionThumbnail\x128.textql.rpc.public.tableau.GetCollectionThumbnailRequest\x1a9.textql.rpc.public.tableau.GetCollectionThumbnailResponse"\x00\x12\x83\x01\n\x12GenerateEmbedToken\x124.textql.rpc.public.tableau.GenerateEmbedTokenRequest\x1a5.textql.rpc.public.tableau.GenerateEmbedTokenResponse"\x00\x12\x8c\x01\n\x15GetConnectedAppStatus\x127.textql.rpc.public.tableau.GetConnectedAppStatusRequest\x1a8.textql.rpc.public.tableau.GetConnectedAppStatusResponse"\x00\x12\x80\x01\n\x11ResetConnectedApp\x123.textql.rpc.public.tableau.ResetConnectedAppRequest\x1a4.textql.rpc.public.tableau.ResetConnectedAppResponse"\x00\x12\x95\x01\n\x18RefreshTableauCollection\x12:.textql.rpc.public.tableau.RefreshTableauCollectionRequest\x1a;.textql.rpc.public.tableau.RefreshTableauCollectionResponse"\x00B;Z9github.com/textqllabs/demo2/compute/pkg/rpc/server/publicb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.tableau_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z9github.com/textqllabs/demo2/compute/pkg/rpc/server/public'
    _globals['_TABLEAUITEMTYPE']._serialized_start = 4193
    _globals['_TABLEAUITEMTYPE']._serialized_end = 4326
    _globals['_TESTTABLEAUCONNECTIONREQUEST']._serialized_start = 85
    _globals['_TESTTABLEAUCONNECTIONREQUEST']._serialized_end = 367
    _globals['_TESTTABLEAUCONNECTIONRESPONSE']._serialized_start = 369
    _globals['_TESTTABLEAUCONNECTIONRESPONSE']._serialized_end = 448
    _globals['_TABLEAUPROJECT']._serialized_start = 451
    _globals['_TABLEAUPROJECT']._serialized_end = 748
    _globals['_LISTTABLEAUPROJECTSREQUEST']._serialized_start = 750
    _globals['_LISTTABLEAUPROJECTSREQUEST']._serialized_end = 813
    _globals['_LISTTABLEAUPROJECTSRESPONSE']._serialized_start = 815
    _globals['_LISTTABLEAUPROJECTSRESPONSE']._serialized_end = 915
    _globals['_TABLEAUWORKBOOK']._serialized_start = 918
    _globals['_TABLEAUWORKBOOK']._serialized_end = 1155
    _globals['_LISTTABLEAUWORKBOOKSREQUEST']._serialized_start = 1158
    _globals['_LISTTABLEAUWORKBOOKSREQUEST']._serialized_end = 1288
    _globals['_LISTTABLEAUWORKBOOKSRESPONSE']._serialized_start = 1290
    _globals['_LISTTABLEAUWORKBOOKSRESPONSE']._serialized_end = 1394
    _globals['_TABLEAUVIEW']._serialized_start = 1397
    _globals['_TABLEAUVIEW']._serialized_end = 1696
    _globals['_LISTTABLEAUVIEWSREQUEST']._serialized_start = 1699
    _globals['_LISTTABLEAUVIEWSREQUEST']._serialized_end = 1829
    _globals['_LISTTABLEAUVIEWSRESPONSE']._serialized_start = 1831
    _globals['_LISTTABLEAUVIEWSRESPONSE']._serialized_end = 1919
    _globals['_TABLEAUDATASOURCE']._serialized_start = 1922
    _globals['_TABLEAUDATASOURCE']._serialized_end = 2216
    _globals['_LISTTABLEAUDATASOURCESREQUEST']._serialized_start = 2219
    _globals['_LISTTABLEAUDATASOURCESREQUEST']._serialized_end = 2363
    _globals['_LISTTABLEAUDATASOURCESRESPONSE']._serialized_start = 2365
    _globals['_LISTTABLEAUDATASOURCESRESPONSE']._serialized_end = 2477
    _globals['_TABLEAUSTARREDITEM']._serialized_start = 2480
    _globals['_TABLEAUSTARREDITEM']._serialized_end = 2721
    _globals['_STARTABLEAUITEMREQUEST']._serialized_start = 2724
    _globals['_STARTABLEAUITEMREQUEST']._serialized_end = 2910
    _globals['_STARTABLEAUITEMRESPONSE']._serialized_start = 2912
    _globals['_STARTABLEAUITEMRESPONSE']._serialized_end = 2963
    _globals['_UNSTARTABLEAUITEMREQUEST']._serialized_start = 2966
    _globals['_UNSTARTABLEAUITEMREQUEST']._serialized_end = 3125
    _globals['_UNSTARTABLEAUITEMRESPONSE']._serialized_start = 3127
    _globals['_UNSTARTABLEAUITEMRESPONSE']._serialized_end = 3180
    _globals['_GETSTARREDTABLEAUITEMSREQUEST']._serialized_start = 3182
    _globals['_GETSTARREDTABLEAUITEMSREQUEST']._serialized_end = 3248
    _globals['_GETSTARREDTABLEAUITEMSRESPONSE']._serialized_start = 3250
    _globals['_GETSTARREDTABLEAUITEMSRESPONSE']._serialized_end = 3351
    _globals['_GETCOLLECTIONTHUMBNAILREQUEST']._serialized_start = 3353
    _globals['_GETCOLLECTIONTHUMBNAILREQUEST']._serialized_end = 3415
    _globals['_GETCOLLECTIONTHUMBNAILRESPONSE']._serialized_start = 3417
    _globals['_GETCOLLECTIONTHUMBNAILRESPONSE']._serialized_end = 3478
    _globals['_GENERATEEMBEDTOKENREQUEST']._serialized_start = 3480
    _globals['_GENERATEEMBEDTOKENREQUEST']._serialized_end = 3567
    _globals['_GENERATEEMBEDTOKENRESPONSE']._serialized_start = 3569
    _globals['_GENERATEEMBEDTOKENRESPONSE']._serialized_end = 3648
    _globals['_GETCONNECTEDAPPSTATUSREQUEST']._serialized_start = 3650
    _globals['_GETCONNECTEDAPPSTATUSREQUEST']._serialized_end = 3715
    _globals['_GETCONNECTEDAPPSTATUSRESPONSE']._serialized_start = 3718
    _globals['_GETCONNECTEDAPPSTATUSRESPONSE']._serialized_end = 3892
    _globals['_RESETCONNECTEDAPPREQUEST']._serialized_start = 3894
    _globals['_RESETCONNECTEDAPPREQUEST']._serialized_end = 3955
    _globals['_RESETCONNECTEDAPPRESPONSE']._serialized_start = 3957
    _globals['_RESETCONNECTEDAPPRESPONSE']._serialized_end = 4010
    _globals['_REFRESHTABLEAUCOLLECTIONREQUEST']._serialized_start = 4012
    _globals['_REFRESHTABLEAUCOLLECTIONREQUEST']._serialized_end = 4076
    _globals['_REFRESHTABLEAUCOLLECTIONRESPONSE']._serialized_start = 4078
    _globals['_REFRESHTABLEAUCOLLECTIONRESPONSE']._serialized_end = 4190
    _globals['_TABLEAUSERVICE']._serialized_start = 4329
    _globals['_TABLEAUSERVICE']._serialized_end = 6145