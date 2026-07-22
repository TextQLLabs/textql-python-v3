"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/template.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ..public import options_pb2 as public_dot_options__pb2
from ..public import playbook_pb2 as public_dot_playbook__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15public/template.proto\x12\x1atextql.rpc.public.template\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14public/options.proto\x1a\x15public/playbook.proto"\x9f\x03\n\x16PlaybookTemplateHeader\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x121\n\x07headers\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\x07headers\x12#\n\rtemplate_name\x18\x03 \x01(\tR\x0ctemplateName\x12\x15\n\x06org_id\x18\x04 \x01(\tR\x05orgId\x129\n\ncreated_at\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt\x129\n\nupdated_at\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampR\tupdatedAt\x12\x19\n\x08can_edit\x18\x07 \x01(\x08R\x07canEdit\x12"\n\ncreated_by\x18\x08 \x01(\tH\x00R\tcreatedBy\x88\x01\x01\x12-\n\x10created_by_email\x18\t \x01(\tH\x01R\x0ecreatedByEmail\x88\x01\x01B\r\n\x0b_created_byB\x13\n\x11_created_by_email"}\n#CreatePlaybookTemplateHeaderRequest\x121\n\x07headers\x18\x01 \x01(\x0b2\x17.google.protobuf.StructR\x07headers\x12#\n\rtemplate_name\x18\x02 \x01(\tR\x0ctemplateName"r\n$CreatePlaybookTemplateHeaderResponse\x12J\n\x06header\x18\x01 \x01(\x0b22.textql.rpc.public.template.PlaybookTemplateHeaderR\x06header"?\n GetPlaybookTemplateHeaderRequest\x12\x1b\n\theader_id\x18\x01 \x01(\tR\x08headerId"o\n!GetPlaybookTemplateHeaderResponse\x12J\n\x06header\x18\x01 \x01(\x0b22.textql.rpc.public.template.PlaybookTemplateHeaderR\x06header"\x9a\x01\n#UpdatePlaybookTemplateHeaderRequest\x12\x1b\n\theader_id\x18\x01 \x01(\tR\x08headerId\x121\n\x07headers\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\x07headers\x12#\n\rtemplate_name\x18\x03 \x01(\tR\x0ctemplateName"r\n$UpdatePlaybookTemplateHeaderResponse\x12J\n\x06header\x18\x01 \x01(\x0b22.textql.rpc.public.template.PlaybookTemplateHeaderR\x06header"B\n#DeletePlaybookTemplateHeaderRequest\x12\x1b\n\theader_id\x18\x01 \x01(\tR\x08headerId"$\n"ListPlaybookTemplateHeadersRequest"s\n#ListPlaybookTemplateHeadersResponse\x12L\n\x07headers\x18\x01 \x03(\x0b22.textql.rpc.public.template.PlaybookTemplateHeaderR\x07headers"\xe7\x05\n\x14PlaybookTemplateData\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\'\n\x0fplaybook_header\x18\x02 \x01(\tR\x0eplaybookHeader\x121\n\x07entries\x18\x03 \x01(\x0b2\x17.google.protobuf.StructR\x07entries\x12\x15\n\x06org_id\x18\x04 \x01(\tR\x05orgId\x129\n\ncreated_at\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt\x129\n\nupdated_at\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampR\tupdatedAt\x12b\n\x10execution_status\x18\x07 \x01(\x0e27.textql.rpc.public.playbook.TemplateDataExecutionStatusR\x0fexecutionStatus\x12Z\n\x19last_execution_started_at\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00R\x16lastExecutionStartedAt\x88\x01\x01\x12^\n\x1blast_execution_completed_at\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampH\x01R\x18lastExecutionCompletedAt\x88\x01\x01\x125\n\x14last_execution_error\x18\n \x01(\tH\x02R\x12lastExecutionError\x88\x01\x01\x12\x1c\n\x07chat_id\x18\x0b \x01(\tH\x03R\x06chatId\x88\x01\x01B\x1c\n\x1a_last_execution_started_atB\x1e\n\x1c_last_execution_completed_atB\x17\n\x15_last_execution_errorB\n\n\x08_chat_id"\x7f\n!CreatePlaybookTemplateDataRequest\x12\'\n\x0fplaybook_header\x18\x01 \x01(\tR\x0eplaybookHeader\x121\n\x07entries\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\x07entries"j\n"CreatePlaybookTemplateDataResponse\x12D\n\x04data\x18\x01 \x01(\x0b20.textql.rpc.public.template.PlaybookTemplateDataR\x04data"9\n\x1eGetPlaybookTemplateDataRequest\x12\x17\n\x07data_id\x18\x01 \x01(\tR\x06dataId"g\n\x1fGetPlaybookTemplateDataResponse\x12D\n\x04data\x18\x01 \x01(\x0b20.textql.rpc.public.template.PlaybookTemplateDataR\x04data"\x9e\x01\n&GetPlaybookTemplateDataByHeaderRequest\x12\'\n\x0fplaybook_header\x18\x01 \x01(\tR\x0eplaybookHeader\x12\x19\n\x05limit\x18\x02 \x01(\x05H\x00R\x05limit\x88\x01\x01\x12\x1b\n\x06offset\x18\x03 \x01(\x05H\x01R\x06offset\x88\x01\x01B\x08\n\x06_limitB\t\n\x07_offset"\xe2\x01\n\'GetPlaybookTemplateDataByHeaderResponse\x12M\n\tdata_rows\x18\x01 \x03(\x0b20.textql.rpc.public.template.PlaybookTemplateDataR\x08dataRows\x12\x1f\n\x0btotal_count\x18\x02 \x01(\x05R\ntotalCount\x12\x16\n\x06offset\x18\x03 \x01(\x05R\x06offset\x12\x14\n\x05limit\x18\x04 \x01(\x05R\x05limit\x12\x19\n\x08has_more\x18\x05 \x01(\x08R\x07hasMore"\xfe\x01\n-GetPlaybookTemplateDataWithBatchStatusRequest\x12\'\n\x0fplaybook_header\x18\x01 \x01(\tR\x0eplaybookHeader\x12\x1f\n\x0bplaybook_id\x18\x02 \x01(\tR\nplaybookId\x12%\n\x0cbatch_run_id\x18\x03 \x01(\tH\x00R\nbatchRunId\x88\x01\x01\x12\x19\n\x05limit\x18\x04 \x01(\x05H\x01R\x05limit\x88\x01\x01\x12\x1b\n\x06offset\x18\x05 \x01(\x05H\x02R\x06offset\x88\x01\x01B\x0f\n\r_batch_run_idB\x08\n\x06_limitB\t\n\x07_offset"\xe9\x01\n.GetPlaybookTemplateDataWithBatchStatusResponse\x12M\n\tdata_rows\x18\x01 \x03(\x0b20.textql.rpc.public.template.PlaybookTemplateDataR\x08dataRows\x12\x1f\n\x0btotal_count\x18\x02 \x01(\x05R\ntotalCount\x12\x16\n\x06offset\x18\x03 \x01(\x05R\x06offset\x12\x14\n\x05limit\x18\x04 \x01(\x05R\x05limit\x12\x19\n\x08has_more\x18\x05 \x01(\x08R\x07hasMore"\xe0\x01\n!SearchPlaybookTemplateDataRequest\x12\'\n\x0fplaybook_header\x18\x01 \x01(\tR\x0eplaybookHeader\x12E\n\x07filters\x18\x02 \x03(\x0b2+.textql.rpc.public.playbook.FilterConditionR\x07filters\x12\x19\n\x05limit\x18\x03 \x01(\x05H\x00R\x05limit\x88\x01\x01\x12\x1b\n\x06offset\x18\x04 \x01(\x05H\x01R\x06offset\x88\x01\x01B\x08\n\x06_limitB\t\n\x07_offset"\xdd\x01\n"SearchPlaybookTemplateDataResponse\x12M\n\tdata_rows\x18\x01 \x03(\x0b20.textql.rpc.public.template.PlaybookTemplateDataR\x08dataRows\x12\x1f\n\x0btotal_count\x18\x02 \x01(\x05R\ntotalCount\x12\x16\n\x06offset\x18\x03 \x01(\x05R\x06offset\x12\x14\n\x05limit\x18\x04 \x01(\x05R\x05limit\x12\x19\n\x08has_more\x18\x05 \x01(\x08R\x07hasMore"o\n!UpdatePlaybookTemplateDataRequest\x12\x17\n\x07data_id\x18\x01 \x01(\tR\x06dataId\x121\n\x07entries\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\x07entries"j\n"UpdatePlaybookTemplateDataResponse\x12D\n\x04data\x18\x01 \x01(\x0b20.textql.rpc.public.template.PlaybookTemplateDataR\x04data"<\n!DeletePlaybookTemplateDataRequest\x12\x17\n\x07data_id\x18\x01 \x01(\tR\x06dataId"T\n)DeletePlaybookTemplateDataByHeaderRequest\x12\'\n\x0fplaybook_header\x18\x01 \x01(\tR\x0eplaybookHeader"f\n\x1cCreateTemplateFromCSVRequest\x12!\n\x0cfile_content\x18\x01 \x01(\x0cR\x0bfileContent\x12#\n\rtemplate_name\x18\x02 \x01(\tR\x0ctemplateName"<\n\x1dCreateTemplateFromCSVResponse\x12\x1b\n\theader_id\x18\x01 \x01(\tR\x08headerId"g\n\x1dCreateTemplateFromXLSXRequest\x12!\n\x0cfile_content\x18\x01 \x01(\x0cR\x0bfileContent\x12#\n\rtemplate_name\x18\x02 \x01(\tR\x0ctemplateName"=\n\x1eCreateTemplateFromXLSXResponse\x12\x1b\n\theader_id\x18\x01 \x01(\tR\x08headerId2\xa6\x12\n\x0fTemplateService\x12\xa1\x01\n\x1cCreatePlaybookTemplateHeader\x12?.textql.rpc.public.template.CreatePlaybookTemplateHeaderRequest\x1a@.textql.rpc.public.template.CreatePlaybookTemplateHeaderResponse\x12\x9d\x01\n\x19GetPlaybookTemplateHeader\x12<.textql.rpc.public.template.GetPlaybookTemplateHeaderRequest\x1a=.textql.rpc.public.template.GetPlaybookTemplateHeaderResponse"\x03\x90\x02\x01\x12\xa1\x01\n\x1cUpdatePlaybookTemplateHeader\x12?.textql.rpc.public.template.UpdatePlaybookTemplateHeaderRequest\x1a@.textql.rpc.public.template.UpdatePlaybookTemplateHeaderResponse\x12w\n\x1cDeletePlaybookTemplateHeader\x12?.textql.rpc.public.template.DeletePlaybookTemplateHeaderRequest\x1a\x16.google.protobuf.Empty\x12\xa3\x01\n\x1bListPlaybookTemplateHeaders\x12>.textql.rpc.public.template.ListPlaybookTemplateHeadersRequest\x1a?.textql.rpc.public.template.ListPlaybookTemplateHeadersResponse"\x03\x90\x02\x01\x12\x9b\x01\n\x1aCreatePlaybookTemplateData\x12=.textql.rpc.public.template.CreatePlaybookTemplateDataRequest\x1a>.textql.rpc.public.template.CreatePlaybookTemplateDataResponse\x12\x97\x01\n\x17GetPlaybookTemplateData\x12:.textql.rpc.public.template.GetPlaybookTemplateDataRequest\x1a;.textql.rpc.public.template.GetPlaybookTemplateDataResponse"\x03\x90\x02\x01\x12\xaf\x01\n\x1fGetPlaybookTemplateDataByHeader\x12B.textql.rpc.public.template.GetPlaybookTemplateDataByHeaderRequest\x1aC.textql.rpc.public.template.GetPlaybookTemplateDataByHeaderResponse"\x03\x90\x02\x01\x12\xc4\x01\n&GetPlaybookTemplateDataWithBatchStatus\x12I.textql.rpc.public.template.GetPlaybookTemplateDataWithBatchStatusRequest\x1aJ.textql.rpc.public.template.GetPlaybookTemplateDataWithBatchStatusResponse"\x03\x90\x02\x01\x12\xa0\x01\n\x1aSearchPlaybookTemplateData\x12=.textql.rpc.public.template.SearchPlaybookTemplateDataRequest\x1a>.textql.rpc.public.template.SearchPlaybookTemplateDataResponse"\x03\x90\x02\x01\x12\x9b\x01\n\x1aUpdatePlaybookTemplateData\x12=.textql.rpc.public.template.UpdatePlaybookTemplateDataRequest\x1a>.textql.rpc.public.template.UpdatePlaybookTemplateDataResponse\x12s\n\x1aDeletePlaybookTemplateData\x12=.textql.rpc.public.template.DeletePlaybookTemplateDataRequest\x1a\x16.google.protobuf.Empty\x12\x83\x01\n"DeletePlaybookTemplateDataByHeader\x12E.textql.rpc.public.template.DeletePlaybookTemplateDataByHeaderRequest\x1a\x16.google.protobuf.Empty\x12\x8c\x01\n\x15CreateTemplateFromCSV\x128.textql.rpc.public.template.CreateTemplateFromCSVRequest\x1a9.textql.rpc.public.template.CreateTemplateFromCSVResponse\x12\x8f\x01\n\x16CreateTemplateFromXLSX\x129.textql.rpc.public.template.CreateTemplateFromXLSXRequest\x1a:.textql.rpc.public.template.CreateTemplateFromXLSXResponseB\x0c\x92\xb5\x18\x08INTERNALb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.template_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\x92\xb5\x18\x08INTERNAL'
    _globals['_TEMPLATESERVICE'].methods_by_name['GetPlaybookTemplateHeader']._loaded_options = None
    _globals['_TEMPLATESERVICE'].methods_by_name['GetPlaybookTemplateHeader']._serialized_options = b'\x90\x02\x01'
    _globals['_TEMPLATESERVICE'].methods_by_name['ListPlaybookTemplateHeaders']._loaded_options = None
    _globals['_TEMPLATESERVICE'].methods_by_name['ListPlaybookTemplateHeaders']._serialized_options = b'\x90\x02\x01'
    _globals['_TEMPLATESERVICE'].methods_by_name['GetPlaybookTemplateData']._loaded_options = None
    _globals['_TEMPLATESERVICE'].methods_by_name['GetPlaybookTemplateData']._serialized_options = b'\x90\x02\x01'
    _globals['_TEMPLATESERVICE'].methods_by_name['GetPlaybookTemplateDataByHeader']._loaded_options = None
    _globals['_TEMPLATESERVICE'].methods_by_name['GetPlaybookTemplateDataByHeader']._serialized_options = b'\x90\x02\x01'
    _globals['_TEMPLATESERVICE'].methods_by_name['GetPlaybookTemplateDataWithBatchStatus']._loaded_options = None
    _globals['_TEMPLATESERVICE'].methods_by_name['GetPlaybookTemplateDataWithBatchStatus']._serialized_options = b'\x90\x02\x01'
    _globals['_TEMPLATESERVICE'].methods_by_name['SearchPlaybookTemplateData']._loaded_options = None
    _globals['_TEMPLATESERVICE'].methods_by_name['SearchPlaybookTemplateData']._serialized_options = b'\x90\x02\x01'
    _globals['_PLAYBOOKTEMPLATEHEADER']._serialized_start = 191
    _globals['_PLAYBOOKTEMPLATEHEADER']._serialized_end = 606
    _globals['_CREATEPLAYBOOKTEMPLATEHEADERREQUEST']._serialized_start = 608
    _globals['_CREATEPLAYBOOKTEMPLATEHEADERREQUEST']._serialized_end = 733
    _globals['_CREATEPLAYBOOKTEMPLATEHEADERRESPONSE']._serialized_start = 735
    _globals['_CREATEPLAYBOOKTEMPLATEHEADERRESPONSE']._serialized_end = 849
    _globals['_GETPLAYBOOKTEMPLATEHEADERREQUEST']._serialized_start = 851
    _globals['_GETPLAYBOOKTEMPLATEHEADERREQUEST']._serialized_end = 914
    _globals['_GETPLAYBOOKTEMPLATEHEADERRESPONSE']._serialized_start = 916
    _globals['_GETPLAYBOOKTEMPLATEHEADERRESPONSE']._serialized_end = 1027
    _globals['_UPDATEPLAYBOOKTEMPLATEHEADERREQUEST']._serialized_start = 1030
    _globals['_UPDATEPLAYBOOKTEMPLATEHEADERREQUEST']._serialized_end = 1184
    _globals['_UPDATEPLAYBOOKTEMPLATEHEADERRESPONSE']._serialized_start = 1186
    _globals['_UPDATEPLAYBOOKTEMPLATEHEADERRESPONSE']._serialized_end = 1300
    _globals['_DELETEPLAYBOOKTEMPLATEHEADERREQUEST']._serialized_start = 1302
    _globals['_DELETEPLAYBOOKTEMPLATEHEADERREQUEST']._serialized_end = 1368
    _globals['_LISTPLAYBOOKTEMPLATEHEADERSREQUEST']._serialized_start = 1370
    _globals['_LISTPLAYBOOKTEMPLATEHEADERSREQUEST']._serialized_end = 1406
    _globals['_LISTPLAYBOOKTEMPLATEHEADERSRESPONSE']._serialized_start = 1408
    _globals['_LISTPLAYBOOKTEMPLATEHEADERSRESPONSE']._serialized_end = 1523
    _globals['_PLAYBOOKTEMPLATEDATA']._serialized_start = 1526
    _globals['_PLAYBOOKTEMPLATEDATA']._serialized_end = 2269
    _globals['_CREATEPLAYBOOKTEMPLATEDATAREQUEST']._serialized_start = 2271
    _globals['_CREATEPLAYBOOKTEMPLATEDATAREQUEST']._serialized_end = 2398
    _globals['_CREATEPLAYBOOKTEMPLATEDATARESPONSE']._serialized_start = 2400
    _globals['_CREATEPLAYBOOKTEMPLATEDATARESPONSE']._serialized_end = 2506
    _globals['_GETPLAYBOOKTEMPLATEDATAREQUEST']._serialized_start = 2508
    _globals['_GETPLAYBOOKTEMPLATEDATAREQUEST']._serialized_end = 2565
    _globals['_GETPLAYBOOKTEMPLATEDATARESPONSE']._serialized_start = 2567
    _globals['_GETPLAYBOOKTEMPLATEDATARESPONSE']._serialized_end = 2670
    _globals['_GETPLAYBOOKTEMPLATEDATABYHEADERREQUEST']._serialized_start = 2673
    _globals['_GETPLAYBOOKTEMPLATEDATABYHEADERREQUEST']._serialized_end = 2831
    _globals['_GETPLAYBOOKTEMPLATEDATABYHEADERRESPONSE']._serialized_start = 2834
    _globals['_GETPLAYBOOKTEMPLATEDATABYHEADERRESPONSE']._serialized_end = 3060
    _globals['_GETPLAYBOOKTEMPLATEDATAWITHBATCHSTATUSREQUEST']._serialized_start = 3063
    _globals['_GETPLAYBOOKTEMPLATEDATAWITHBATCHSTATUSREQUEST']._serialized_end = 3317
    _globals['_GETPLAYBOOKTEMPLATEDATAWITHBATCHSTATUSRESPONSE']._serialized_start = 3320
    _globals['_GETPLAYBOOKTEMPLATEDATAWITHBATCHSTATUSRESPONSE']._serialized_end = 3553
    _globals['_SEARCHPLAYBOOKTEMPLATEDATAREQUEST']._serialized_start = 3556
    _globals['_SEARCHPLAYBOOKTEMPLATEDATAREQUEST']._serialized_end = 3780
    _globals['_SEARCHPLAYBOOKTEMPLATEDATARESPONSE']._serialized_start = 3783
    _globals['_SEARCHPLAYBOOKTEMPLATEDATARESPONSE']._serialized_end = 4004
    _globals['_UPDATEPLAYBOOKTEMPLATEDATAREQUEST']._serialized_start = 4006
    _globals['_UPDATEPLAYBOOKTEMPLATEDATAREQUEST']._serialized_end = 4117
    _globals['_UPDATEPLAYBOOKTEMPLATEDATARESPONSE']._serialized_start = 4119
    _globals['_UPDATEPLAYBOOKTEMPLATEDATARESPONSE']._serialized_end = 4225
    _globals['_DELETEPLAYBOOKTEMPLATEDATAREQUEST']._serialized_start = 4227
    _globals['_DELETEPLAYBOOKTEMPLATEDATAREQUEST']._serialized_end = 4287
    _globals['_DELETEPLAYBOOKTEMPLATEDATABYHEADERREQUEST']._serialized_start = 4289
    _globals['_DELETEPLAYBOOKTEMPLATEDATABYHEADERREQUEST']._serialized_end = 4373
    _globals['_CREATETEMPLATEFROMCSVREQUEST']._serialized_start = 4375
    _globals['_CREATETEMPLATEFROMCSVREQUEST']._serialized_end = 4477
    _globals['_CREATETEMPLATEFROMCSVRESPONSE']._serialized_start = 4479
    _globals['_CREATETEMPLATEFROMCSVRESPONSE']._serialized_end = 4539
    _globals['_CREATETEMPLATEFROMXLSXREQUEST']._serialized_start = 4541
    _globals['_CREATETEMPLATEFROMXLSXREQUEST']._serialized_end = 4644
    _globals['_CREATETEMPLATEFROMXLSXRESPONSE']._serialized_start = 4646
    _globals['_CREATETEMPLATEFROMXLSXRESPONSE']._serialized_end = 4707
    _globals['_TEMPLATESERVICE']._serialized_start = 4710
    _globals['_TEMPLATESERVICE']._serialized_end = 7052