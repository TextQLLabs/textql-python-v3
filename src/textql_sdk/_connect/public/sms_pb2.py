"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/sms.proto')
_sym_db = _symbol_database.Default()
from .. import auth_pb2 as auth__pb2
from ..public import options_pb2 as public_dot_options__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10public/sms.proto\x12\x15textql.rpc.public.sms\x1a\nauth.proto\x1a\x14public/options.proto"B\n\x1dStartPhoneVerificationRequest\x12!\n\x0cphone_number\x18\x01 \x01(\tR\x0bphoneNumber"=\n\x1eStartPhoneVerificationResponse\x12\x1b\n\tcode_sent\x18\x01 \x01(\x08R\x08codeSent"5\n\x1fConfirmPhoneVerificationRequest\x12\x12\n\x04code\x18\x01 \x01(\tR\x04code"n\n ConfirmPhoneVerificationResponse\x12/\n\x06member\x18\x01 \x01(\x0b2\x17.textql.rpc.auth.MemberR\x06member\x12\x19\n\x08agent_id\x18\x02 \x01(\tR\x07agentId"/\n\x12SetSmsAgentRequest\x12\x19\n\x08agent_id\x18\x01 \x01(\tR\x07agentId"F\n\x13SetSmsAgentResponse\x12/\n\x06member\x18\x01 \x01(\x0b2\x17.textql.rpc.auth.MemberR\x06member"\x14\n\x12RemovePhoneRequest"F\n\x13RemovePhoneResponse\x12/\n\x06member\x18\x01 \x01(\x0b2\x17.textql.rpc.auth.MemberR\x06member2\xee\x03\n\nSmsService\x12\x85\x01\n\x16StartPhoneVerification\x124.textql.rpc.public.sms.StartPhoneVerificationRequest\x1a5.textql.rpc.public.sms.StartPhoneVerificationResponse\x12\x8b\x01\n\x18ConfirmPhoneVerification\x126.textql.rpc.public.sms.ConfirmPhoneVerificationRequest\x1a7.textql.rpc.public.sms.ConfirmPhoneVerificationResponse\x12d\n\x0bSetSmsAgent\x12).textql.rpc.public.sms.SetSmsAgentRequest\x1a*.textql.rpc.public.sms.SetSmsAgentResponse\x12d\n\x0bRemovePhone\x12).textql.rpc.public.sms.RemovePhoneRequest\x1a*.textql.rpc.public.sms.RemovePhoneResponseB\x0c\x92\xb5\x18\x08INTERNALb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.sms_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\x92\xb5\x18\x08INTERNAL'
    _globals['_STARTPHONEVERIFICATIONREQUEST']._serialized_start = 77
    _globals['_STARTPHONEVERIFICATIONREQUEST']._serialized_end = 143
    _globals['_STARTPHONEVERIFICATIONRESPONSE']._serialized_start = 145
    _globals['_STARTPHONEVERIFICATIONRESPONSE']._serialized_end = 206
    _globals['_CONFIRMPHONEVERIFICATIONREQUEST']._serialized_start = 208
    _globals['_CONFIRMPHONEVERIFICATIONREQUEST']._serialized_end = 261
    _globals['_CONFIRMPHONEVERIFICATIONRESPONSE']._serialized_start = 263
    _globals['_CONFIRMPHONEVERIFICATIONRESPONSE']._serialized_end = 373
    _globals['_SETSMSAGENTREQUEST']._serialized_start = 375
    _globals['_SETSMSAGENTREQUEST']._serialized_end = 422
    _globals['_SETSMSAGENTRESPONSE']._serialized_start = 424
    _globals['_SETSMSAGENTRESPONSE']._serialized_end = 494
    _globals['_REMOVEPHONEREQUEST']._serialized_start = 496
    _globals['_REMOVEPHONEREQUEST']._serialized_end = 516
    _globals['_REMOVEPHONERESPONSE']._serialized_start = 518
    _globals['_REMOVEPHONERESPONSE']._serialized_end = 588
    _globals['_SMSSERVICE']._serialized_start = 591
    _globals['_SMSSERVICE']._serialized_end = 1085