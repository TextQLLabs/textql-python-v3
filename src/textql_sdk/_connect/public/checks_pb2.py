# pylint: skip-file
# mypy: ignore-errors
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/checks.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ..public import options_pb2 as public_dot_options__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13public/checks.proto\x12\x18textql.rpc.public.checks\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14public/options.proto"\x83\x02\n\x05Check\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12#\n\rresource_type\x18\x02 \x01(\tR\x0cresourceType\x12\x14\n\x05title\x18\x03 \x01(\tR\x05title\x12C\n\x08severity\x18\x04 \x01(\x0e2\'.textql.rpc.public.checks.CheckSeverityR\x08severity\x12\x1c\n\tcondition\x18\x06 \x01(\tR\tcondition\x12 \n\x0bdescription\x18\x07 \x01(\tR\x0bdescription\x12\x1d\n\napplies_to\x18\x08 \x03(\tR\tappliesToJ\x04\x08\x05\x10\x06R\x05class"\x13\n\x11ListChecksRequest"M\n\x12ListChecksResponse\x127\n\x06checks\x18\x01 \x03(\x0b2\x1f.textql.rpc.public.checks.CheckR\x06checks"\xb3\x01\n\x07Finding\x12\x19\n\x08check_id\x18\x01 \x01(\tR\x07checkId\x12#\n\rresource_type\x18\x02 \x01(\tR\x0cresourceType\x12\x12\n\x04path\x18\x03 \x01(\tR\x04path\x12\x18\n\x07message\x18\x04 \x01(\tR\x07message\x12:\n\x05class\x18\x05 \x01(\x0e2$.textql.rpc.public.checks.CheckClassR\x05class"O\n\x10RunChecksRequest\x12\x1b\n\x08patch_id\x18\x01 \x01(\tH\x00R\x07patchId\x12\x14\n\x04live\x18\x02 \x01(\x08H\x00R\x04liveB\x08\n\x06target"|\n\x0cErroredCheck\x12\x19\n\x08check_id\x18\x01 \x01(\tR\x07checkId\x12#\n\rresource_type\x18\x02 \x01(\tR\x0cresourceType\x12\x12\n\x04path\x18\x03 \x01(\tR\x04path\x12\x18\n\x07message\x18\x04 \x01(\tR\x07message"\x81\x01\n\x19SaveBlockedByChecksDetail\x12=\n\x08findings\x18\x01 \x03(\x0b2!.textql.rpc.public.checks.FindingR\x08findings\x12%\n\x0eauthz_messages\x18\x02 \x03(\tR\rauthzMessages"\xb1\x01\n\x11RunChecksResponse\x12\x0e\n\x02ok\x18\x01 \x01(\x08R\x02ok\x12=\n\x08findings\x18\x02 \x03(\x0b2!.textql.rpc.public.checks.FindingR\x08findings\x12M\n\x0eerrored_checks\x18\x04 \x03(\x0b2&.textql.rpc.public.checks.ErroredCheckR\rerroredChecks"\xc6\x03\n\x0bCheckRecord\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x19\n\x08check_id\x18\x02 \x01(\tR\x07checkId\x12#\n\rresource_type\x18\x03 \x01(\tR\x0cresourceType\x12\x12\n\x04path\x18\x04 \x01(\tR\x04path\x12\x1a\n\x08messages\x18\x05 \x03(\tR\x08messages\x12:\n\x05class\x18\x06 \x01(\x0e2$.textql.rpc.public.checks.CheckClassR\x05class\x12C\n\x08severity\x18\x07 \x01(\x0e2\'.textql.rpc.public.checks.CheckSeverityR\x08severity\x12\x18\n\x07errored\x18\x08 \x01(\x08R\x07errored\x12>\n\rfirst_seen_at\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampR\x0bfirstSeenAt\x12<\n\x0clast_seen_at\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampR\nlastSeenAt\x12\x1e\n\x0bfix_chat_id\x18\x0b \x01(\tR\tfixChatId"\xdc\x02\n\x0cCheckRunInfo\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x16\n\x06source\x18\x02 \x01(\tR\x06source\x129\n\nstarted_at\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\tstartedAt\x12;\n\x0bfinished_at\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\nfinishedAt\x12#\n\rfiles_scanned\x18\x05 \x01(\x05R\x0cfilesScanned\x12\x1d\n\nchecks_run\x18\x06 \x01(\x05R\tchecksRun\x12\x18\n\x07passing\x18\x07 \x01(\x05R\x07passing\x12\x1a\n\x08warnings\x18\x08 \x01(\x05R\x08warnings\x12\x18\n\x07failing\x18\t \x01(\x05R\x07failing\x12\x18\n\x07errored\x18\n \x01(\x05R\x07errored"\x18\n\x16GetCheckResultsRequest"\xa1\x01\n\x17GetCheckResultsResponse\x12?\n\x07records\x18\x01 \x03(\x0b2%.textql.rpc.public.checks.CheckRecordR\x07records\x12=\n\x03run\x18\x02 \x01(\x0b2&.textql.rpc.public.checks.CheckRunInfoH\x00R\x03run\x88\x01\x01B\x06\n\x04_run*b\n\rCheckSeverity\x12\x1e\n\x1aCHECK_SEVERITY_UNSPECIFIED\x10\x00\x12\x18\n\x14CHECK_SEVERITY_ERROR\x10\x01\x12\x17\n\x13CHECK_SEVERITY_WARN\x10\x02*j\n\nCheckClass\x12\x1b\n\x17CHECK_CLASS_UNSPECIFIED\x10\x00\x12\x1c\n\x18CHECK_CLASS_EDIT_FIXABLE\x10\x01\x12!\n\x1dCHECK_CLASS_ORG_STATE_FIXABLE\x10\x022\xe5\x02\n\rChecksService\x12l\n\nListChecks\x12+.textql.rpc.public.checks.ListChecksRequest\x1a,.textql.rpc.public.checks.ListChecksResponse"\x03\x90\x02\x01\x12i\n\tRunChecks\x12*.textql.rpc.public.checks.RunChecksRequest\x1a+.textql.rpc.public.checks.RunChecksResponse"\x03\x90\x02\x01\x12{\n\x0fGetCheckResults\x120.textql.rpc.public.checks.GetCheckResultsRequest\x1a1.textql.rpc.public.checks.GetCheckResultsResponse"\x03\x90\x02\x01B\x0c\x92\xb5\x18\x08INTERNALb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.checks_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\x92\xb5\x18\x08INTERNAL'
    _globals['_CHECKSSERVICE'].methods_by_name['ListChecks']._loaded_options = None
    _globals['_CHECKSSERVICE'].methods_by_name['ListChecks']._serialized_options = b'\x90\x02\x01'
    _globals['_CHECKSSERVICE'].methods_by_name['RunChecks']._loaded_options = None
    _globals['_CHECKSSERVICE'].methods_by_name['RunChecks']._serialized_options = b'\x90\x02\x01'
    _globals['_CHECKSSERVICE'].methods_by_name['GetCheckResults']._loaded_options = None
    _globals['_CHECKSSERVICE'].methods_by_name['GetCheckResults']._serialized_options = b'\x90\x02\x01'
    _globals['_CHECKSEVERITY']._serialized_start = 2165
    _globals['_CHECKSEVERITY']._serialized_end = 2263
    _globals['_CHECKCLASS']._serialized_start = 2265
    _globals['_CHECKCLASS']._serialized_end = 2371
    _globals['_CHECK']._serialized_start = 105
    _globals['_CHECK']._serialized_end = 364
    _globals['_LISTCHECKSREQUEST']._serialized_start = 366
    _globals['_LISTCHECKSREQUEST']._serialized_end = 385
    _globals['_LISTCHECKSRESPONSE']._serialized_start = 387
    _globals['_LISTCHECKSRESPONSE']._serialized_end = 464
    _globals['_FINDING']._serialized_start = 467
    _globals['_FINDING']._serialized_end = 646
    _globals['_RUNCHECKSREQUEST']._serialized_start = 648
    _globals['_RUNCHECKSREQUEST']._serialized_end = 727
    _globals['_ERROREDCHECK']._serialized_start = 729
    _globals['_ERROREDCHECK']._serialized_end = 853
    _globals['_SAVEBLOCKEDBYCHECKSDETAIL']._serialized_start = 856
    _globals['_SAVEBLOCKEDBYCHECKSDETAIL']._serialized_end = 985
    _globals['_RUNCHECKSRESPONSE']._serialized_start = 988
    _globals['_RUNCHECKSRESPONSE']._serialized_end = 1165
    _globals['_CHECKRECORD']._serialized_start = 1168
    _globals['_CHECKRECORD']._serialized_end = 1622
    _globals['_CHECKRUNINFO']._serialized_start = 1625
    _globals['_CHECKRUNINFO']._serialized_end = 1973
    _globals['_GETCHECKRESULTSREQUEST']._serialized_start = 1975
    _globals['_GETCHECKRESULTSREQUEST']._serialized_end = 1999
    _globals['_GETCHECKRESULTSRESPONSE']._serialized_start = 2002
    _globals['_GETCHECKRESULTSRESPONSE']._serialized_end = 2163
    _globals['_CHECKSSERVICE']._serialized_start = 2374
    _globals['_CHECKSSERVICE']._serialized_end = 2731