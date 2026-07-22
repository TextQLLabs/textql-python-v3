"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/identity.proto')
_sym_db = _symbol_database.Default()
from ..public import options_pb2 as public_dot_options__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15public/identity.proto\x12\x13textql.rpc.identity\x1a\x14public/options.proto"e\n\x07Session\x12\x1b\n\tmember_id\x18\x01 \x01(\tR\x08memberId\x12\'\n\x0forganization_id\x18\x02 \x01(\tR\x0eorganizationId\x12\x14\n\x05roles\x18\x03 \x03(\tR\x05roles"\xe5\x01\n\rMemberPreview\x12\x1b\n\tmember_id\x18\x01 \x01(\tR\x08memberId\x12&\n\x0cmember_email\x18\x02 \x01(\tH\x00R\x0bmemberEmail\x88\x01\x01\x12$\n\x0bmember_name\x18\x03 \x01(\tH\x01R\nmemberName\x88\x01\x01\x121\n\x12member_picture_url\x18\x04 \x01(\tH\x02R\x10memberPictureUrl\x88\x01\x01B\x0f\n\r_member_emailB\x0e\n\x0c_member_nameB\x15\n\x13_member_picture_urlB\x0c\x92\xb5\x18\x08INTERNALb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.identity_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\x92\xb5\x18\x08INTERNAL'
    _globals['_SESSION']._serialized_start = 68
    _globals['_SESSION']._serialized_end = 169
    _globals['_MEMBERPREVIEW']._serialized_start = 172
    _globals['_MEMBERPREVIEW']._serialized_end = 401