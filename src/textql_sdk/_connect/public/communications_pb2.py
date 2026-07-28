# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
# pylint: skip-file
# mypy: ignore-errors
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/communications.proto')
_sym_db = _symbol_database.Default()
from ..public import options_pb2 as public_dot_options__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bpublic/communications.proto\x12 textql.rpc.public.communications\x1a\x14public/options.proto"\xfb\x01\n\x10SendEmailRequest\x12\x18\n\x07subject\x18\x01 \x01(\tR\x07subject\x12\x12\n\x04body\x18\x02 \x01(\tR\x04body\x12\x13\n\x02to\x18\x03 \x01(\tH\x00R\x02to\x88\x01\x01\x12 \n\treport_id\x18\x04 \x01(\tH\x01R\x08reportId\x88\x01\x01\x12"\n\nowner_name\x18\x05 \x01(\tH\x02R\townerName\x88\x01\x01\x12(\n\rreport_source\x18\x06 \x01(\tH\x03R\x0creportSource\x88\x01\x01B\x05\n\x03_toB\x0c\n\n_report_idB\r\n\x0b_owner_nameB\x10\n\x0e_report_source"R\n\x11SendEmailResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x19\n\x05error\x18\x02 \x01(\tH\x00R\x05error\x88\x01\x01B\x08\n\x06_error"A\n\x1fUploadFeedbackScreenshotRequest\x12\x1e\n\nscreenshot\x18\x01 \x01(\x0cR\nscreenshot"I\n UploadFeedbackScreenshotResponse\x12%\n\x0escreenshot_url\x18\x01 \x01(\tR\rscreenshotUrl2\xb1\x02\n\x15CommunicationsService\x12t\n\tSendEmail\x122.textql.rpc.public.communications.SendEmailRequest\x1a3.textql.rpc.public.communications.SendEmailResponse\x12\xa1\x01\n\x18UploadFeedbackScreenshot\x12A.textql.rpc.public.communications.UploadFeedbackScreenshotRequest\x1aB.textql.rpc.public.communications.UploadFeedbackScreenshotResponseB\x0c\x92\xb5\x18\x08INTERNALb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.communications_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\x92\xb5\x18\x08INTERNAL'
    _globals['_SENDEMAILREQUEST']._serialized_start = 88
    _globals['_SENDEMAILREQUEST']._serialized_end = 339
    _globals['_SENDEMAILRESPONSE']._serialized_start = 341
    _globals['_SENDEMAILRESPONSE']._serialized_end = 423
    _globals['_UPLOADFEEDBACKSCREENSHOTREQUEST']._serialized_start = 425
    _globals['_UPLOADFEEDBACKSCREENSHOTREQUEST']._serialized_end = 490
    _globals['_UPLOADFEEDBACKSCREENSHOTRESPONSE']._serialized_start = 492
    _globals['_UPLOADFEEDBACKSCREENSHOTRESPONSE']._serialized_end = 565
    _globals['_COMMUNICATIONSSERVICE']._serialized_start = 568
    _globals['_COMMUNICATIONSSERVICE']._serialized_end = 873