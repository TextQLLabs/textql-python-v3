# pylint: skip-file
# mypy: ignore-errors
# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/form.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ..public import options_pb2 as public_dot_options__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11public/form.proto\x12\x16textql.rpc.public.form\x1a\x1cgoogle/protobuf/struct.proto\x1a\x14public/options.proto"A\n\x0fValidationIssue\x12\x14\n\x05field\x18\x01 \x01(\tR\x05field\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message"u\n\x0eFormTestResult\x12\x16\n\x06status\x18\x01 \x01(\tR\x06status\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x121\n\x07details\x18\x03 \x01(\x0b2\x17.google.protobuf.StructR\x07details"\xe6\x03\n\x04Form\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x17\n\x07chat_id\x18\x02 \x01(\tR\x06chatId\x12\x1b\n\tform_type\x18\x03 \x01(\tR\x08formType\x12+\n\x04data\x18\x04 \x01(\x0b2\x17.google.protobuf.StructR\x04data\x12\x16\n\x06status\x18\x05 \x01(\tR\x06status\x12<\n\rsubmit_result\x18\x06 \x01(\x0b2\x17.google.protobuf.StructR\x0csubmitResult\x12\x1f\n\x0btest_status\x18\x07 \x01(\tR\ntestStatus\x12G\n\x0btest_result\x18\x08 \x01(\x0b2&.textql.rpc.public.form.FormTestResultR\ntestResult\x12\x1d\n\ntest_stale\x18\t \x01(\x08R\ttestStale\x12?\n\x06issues\x18\n \x03(\x0b2\'.textql.rpc.public.form.ValidationIssueR\x06issues\x12&\n\x0crevision_ref\x18\x0b \x01(\tH\x00R\x0brevisionRef\x88\x01\x01\x12\x12\n\x04name\x18\x0c \x01(\tR\x04nameB\x0f\n\r_revision_ref")\n\x0eGetFormRequest\x12\x17\n\x07form_id\x18\x01 \x01(\tR\x06formId"C\n\x0fGetFormResponse\x120\n\x04form\x18\x01 \x01(\x0b2\x1c.textql.rpc.public.form.FormR\x04form"+\n\x10ListFormsRequest\x12\x17\n\x07chat_id\x18\x01 \x01(\tR\x06chatId"G\n\x11ListFormsResponse\x122\n\x05forms\x18\x01 \x03(\x0b2\x1c.textql.rpc.public.form.FormR\x05forms"1\n\x16PrepareFormEditRequest\x12\x17\n\x07form_id\x18\x01 \x01(\tR\x06formId"K\n\x17PrepareFormEditResponse\x120\n\x04form\x18\x01 \x01(\x0b2\x1c.textql.rpc.public.form.FormR\x04form"[\n\x13ValidateFormRequest\x12\x17\n\x07form_id\x18\x01 \x01(\tR\x06formId\x12+\n\x04data\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\x04data"W\n\x14ValidateFormResponse\x12?\n\x06issues\x18\x01 \x03(\x0b2\'.textql.rpc.public.form.ValidationIssueR\x06issues"]\n\x15UpdateFormDataRequest\x12\x17\n\x07form_id\x18\x01 \x01(\tR\x06formId\x12+\n\x04data\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\x04data"J\n\x16UpdateFormDataResponse\x120\n\x04form\x18\x01 \x01(\x0b2\x1c.textql.rpc.public.form.FormR\x04form"*\n\x0fTestFormRequest\x12\x17\n\x07form_id\x18\x01 \x01(\tR\x06formId"\x96\x01\n\x10TestFormResponse\x12\x1f\n\x0btest_status\x18\x01 \x01(\tR\ntestStatus\x12G\n\x0btest_result\x18\x02 \x01(\x0b2&.textql.rpc.public.form.FormTestResultR\ntestResult\x12\x18\n\x07running\x18\x03 \x01(\x08R\x07running"-\n\x12GetFormTestRequest\x12\x17\n\x07form_id\x18\x01 \x01(\tR\x06formId"\x9e\x01\n\x13GetFormTestResponse\x12\x1f\n\x0btest_status\x18\x01 \x01(\tR\ntestStatus\x12G\n\x0btest_result\x18\x02 \x01(\x0b2&.textql.rpc.public.form.FormTestResultR\ntestResult\x12\x1d\n\ntest_stale\x18\x03 \x01(\x08R\ttestStale",\n\x11SubmitFormRequest\x12\x17\n\x07form_id\x18\x01 \x01(\tR\x06formId"F\n\x12SubmitFormResponse\x120\n\x04form\x18\x01 \x01(\x0b2\x1c.textql.rpc.public.form.FormR\x04form"G\n\x14SetFormStatusRequest\x12\x17\n\x07form_id\x18\x01 \x01(\tR\x06formId\x12\x16\n\x06status\x18\x02 \x01(\tR\x06status"I\n\x15SetFormStatusResponse\x120\n\x04form\x18\x01 \x01(\x0b2\x1c.textql.rpc.public.form.FormR\x04form"W\n\x19BackupFormRevisionRequest\x12\x17\n\x07form_id\x18\x01 \x01(\tR\x06formId\x12!\n\x0crevision_ref\x18\x02 \x01(\tR\x0brevisionRef"N\n\x1aBackupFormRevisionResponse\x120\n\x04form\x18\x01 \x01(\x0b2\x1c.textql.rpc.public.form.FormR\x04form2\xc6\x08\n\x0bFormService\x12_\n\x07GetForm\x12&.textql.rpc.public.form.GetFormRequest\x1a\'.textql.rpc.public.form.GetFormResponse"\x03\x90\x02\x01\x12e\n\tListForms\x12(.textql.rpc.public.form.ListFormsRequest\x1a).textql.rpc.public.form.ListFormsResponse"\x03\x90\x02\x01\x12r\n\x0fPrepareFormEdit\x12..textql.rpc.public.form.PrepareFormEditRequest\x1a/.textql.rpc.public.form.PrepareFormEditResponse\x12n\n\x0cValidateForm\x12+.textql.rpc.public.form.ValidateFormRequest\x1a,.textql.rpc.public.form.ValidateFormResponse"\x03\x90\x02\x01\x12o\n\x0eUpdateFormData\x12-.textql.rpc.public.form.UpdateFormDataRequest\x1a..textql.rpc.public.form.UpdateFormDataResponse\x12]\n\x08TestForm\x12\'.textql.rpc.public.form.TestFormRequest\x1a(.textql.rpc.public.form.TestFormResponse\x12k\n\x0bGetFormTest\x12*.textql.rpc.public.form.GetFormTestRequest\x1a+.textql.rpc.public.form.GetFormTestResponse"\x03\x90\x02\x01\x12c\n\nSubmitForm\x12).textql.rpc.public.form.SubmitFormRequest\x1a*.textql.rpc.public.form.SubmitFormResponse\x12l\n\rSetFormStatus\x12,.textql.rpc.public.form.SetFormStatusRequest\x1a-.textql.rpc.public.form.SetFormStatusResponse\x12{\n\x12BackupFormRevision\x121.textql.rpc.public.form.BackupFormRevisionRequest\x1a2.textql.rpc.public.form.BackupFormRevisionResponseB\x0c\x92\xb5\x18\x08INTERNALb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.form_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\x92\xb5\x18\x08INTERNAL'
    _globals['_FORMSERVICE'].methods_by_name['GetForm']._loaded_options = None
    _globals['_FORMSERVICE'].methods_by_name['GetForm']._serialized_options = b'\x90\x02\x01'
    _globals['_FORMSERVICE'].methods_by_name['ListForms']._loaded_options = None
    _globals['_FORMSERVICE'].methods_by_name['ListForms']._serialized_options = b'\x90\x02\x01'
    _globals['_FORMSERVICE'].methods_by_name['ValidateForm']._loaded_options = None
    _globals['_FORMSERVICE'].methods_by_name['ValidateForm']._serialized_options = b'\x90\x02\x01'
    _globals['_FORMSERVICE'].methods_by_name['GetFormTest']._loaded_options = None
    _globals['_FORMSERVICE'].methods_by_name['GetFormTest']._serialized_options = b'\x90\x02\x01'
    _globals['_VALIDATIONISSUE']._serialized_start = 97
    _globals['_VALIDATIONISSUE']._serialized_end = 162
    _globals['_FORMTESTRESULT']._serialized_start = 164
    _globals['_FORMTESTRESULT']._serialized_end = 281
    _globals['_FORM']._serialized_start = 284
    _globals['_FORM']._serialized_end = 770
    _globals['_GETFORMREQUEST']._serialized_start = 772
    _globals['_GETFORMREQUEST']._serialized_end = 813
    _globals['_GETFORMRESPONSE']._serialized_start = 815
    _globals['_GETFORMRESPONSE']._serialized_end = 882
    _globals['_LISTFORMSREQUEST']._serialized_start = 884
    _globals['_LISTFORMSREQUEST']._serialized_end = 927
    _globals['_LISTFORMSRESPONSE']._serialized_start = 929
    _globals['_LISTFORMSRESPONSE']._serialized_end = 1000
    _globals['_PREPAREFORMEDITREQUEST']._serialized_start = 1002
    _globals['_PREPAREFORMEDITREQUEST']._serialized_end = 1051
    _globals['_PREPAREFORMEDITRESPONSE']._serialized_start = 1053
    _globals['_PREPAREFORMEDITRESPONSE']._serialized_end = 1128
    _globals['_VALIDATEFORMREQUEST']._serialized_start = 1130
    _globals['_VALIDATEFORMREQUEST']._serialized_end = 1221
    _globals['_VALIDATEFORMRESPONSE']._serialized_start = 1223
    _globals['_VALIDATEFORMRESPONSE']._serialized_end = 1310
    _globals['_UPDATEFORMDATAREQUEST']._serialized_start = 1312
    _globals['_UPDATEFORMDATAREQUEST']._serialized_end = 1405
    _globals['_UPDATEFORMDATARESPONSE']._serialized_start = 1407
    _globals['_UPDATEFORMDATARESPONSE']._serialized_end = 1481
    _globals['_TESTFORMREQUEST']._serialized_start = 1483
    _globals['_TESTFORMREQUEST']._serialized_end = 1525
    _globals['_TESTFORMRESPONSE']._serialized_start = 1528
    _globals['_TESTFORMRESPONSE']._serialized_end = 1678
    _globals['_GETFORMTESTREQUEST']._serialized_start = 1680
    _globals['_GETFORMTESTREQUEST']._serialized_end = 1725
    _globals['_GETFORMTESTRESPONSE']._serialized_start = 1728
    _globals['_GETFORMTESTRESPONSE']._serialized_end = 1886
    _globals['_SUBMITFORMREQUEST']._serialized_start = 1888
    _globals['_SUBMITFORMREQUEST']._serialized_end = 1932
    _globals['_SUBMITFORMRESPONSE']._serialized_start = 1934
    _globals['_SUBMITFORMRESPONSE']._serialized_end = 2004
    _globals['_SETFORMSTATUSREQUEST']._serialized_start = 2006
    _globals['_SETFORMSTATUSREQUEST']._serialized_end = 2077
    _globals['_SETFORMSTATUSRESPONSE']._serialized_start = 2079
    _globals['_SETFORMSTATUSRESPONSE']._serialized_end = 2152
    _globals['_BACKUPFORMREVISIONREQUEST']._serialized_start = 2154
    _globals['_BACKUPFORMREVISIONREQUEST']._serialized_end = 2241
    _globals['_BACKUPFORMREVISIONRESPONSE']._serialized_start = 2243
    _globals['_BACKUPFORMREVISIONRESPONSE']._serialized_end = 2321
    _globals['_FORMSERVICE']._serialized_start = 2324
    _globals['_FORMSERVICE']._serialized_end = 3418