# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
# pylint: skip-file
# mypy: ignore-errors
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/engagement.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ..public import options_pb2 as public_dot_options__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17public/engagement.proto\x12\x1ctextql.rpc.public.engagement\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14public/options.proto"\x94\x03\n\nEngagement\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12K\n\nevent_type\x18\x02 \x01(\x0e2,.textql.rpc.public.engagement.EngagementTypeR\teventType\x12!\n\x0cprimitive_id\x18\x03 \x01(\tR\x0bprimitiveId\x12R\n\x0eprimitive_type\x18\x04 \x01(\x0e2+.textql.rpc.public.engagement.PrimitiveTypeR\rprimitiveType\x12\x1c\n\x07user_id\x18\x05 \x01(\tH\x00R\x06userId\x88\x01\x01\x12\x15\n\x06org_id\x18\x06 \x01(\tR\x05orgId\x12$\n\x0bshare_token\x18\x07 \x01(\tH\x01R\nshareToken\x88\x01\x01\x12;\n\x0boccurred_at\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampR\noccurredAtB\n\n\x08_user_idB\x0e\n\x0c_share_token"\x93\x02\n\x17RecordEngagementRequest\x12K\n\nevent_type\x18\x01 \x01(\x0e2,.textql.rpc.public.engagement.EngagementTypeR\teventType\x12!\n\x0cprimitive_id\x18\x02 \x01(\tR\x0bprimitiveId\x12R\n\x0eprimitive_type\x18\x03 \x01(\x0e2+.textql.rpc.public.engagement.PrimitiveTypeR\rprimitiveType\x12$\n\x0bshare_token\x18\x04 \x01(\tH\x00R\nshareToken\x88\x01\x01B\x0e\n\x0c_share_token*\x86\x01\n\x0eEngagementType\x12\x1f\n\x1bENGAGEMENT_TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14ENGAGEMENT_TYPE_VIEW\x10\x01\x12\x19\n\x15ENGAGEMENT_TYPE_SHARE\x10\x02\x12\x1e\n\x1aENGAGEMENT_TYPE_IMPRESSION\x10\x03*\xb4\x01\n\rPrimitiveType\x12\x1e\n\x1aPRIMITIVE_TYPE_UNSPECIFIED\x10\x00\x12\x1c\n\x18PRIMITIVE_TYPE_DASHBOARD\x10\x01\x12\x17\n\x13PRIMITIVE_TYPE_CHAT\x10\x02\x12\x17\n\x13PRIMITIVE_TYPE_FEED\x10\x03\x12\x1b\n\x17PRIMITIVE_TYPE_PLAYBOOK\x10\x04\x12\x16\n\x12PRIMITIVE_TYPE_APP\x10\x052v\n\x11EngagementService\x12a\n\x10RecordEngagement\x125.textql.rpc.public.engagement.RecordEngagementRequest\x1a\x16.google.protobuf.EmptyB\x0c\x92\xb5\x18\x08INTERNALb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.engagement_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\x92\xb5\x18\x08INTERNAL'
    _globals['_ENGAGEMENTTYPE']._serialized_start = 827
    _globals['_ENGAGEMENTTYPE']._serialized_end = 961
    _globals['_PRIMITIVETYPE']._serialized_start = 964
    _globals['_PRIMITIVETYPE']._serialized_end = 1144
    _globals['_ENGAGEMENT']._serialized_start = 142
    _globals['_ENGAGEMENT']._serialized_end = 546
    _globals['_RECORDENGAGEMENTREQUEST']._serialized_start = 549
    _globals['_RECORDENGAGEMENTREQUEST']._serialized_end = 824
    _globals['_ENGAGEMENTSERVICE']._serialized_start = 1146
    _globals['_ENGAGEMENTSERVICE']._serialized_end = 1264