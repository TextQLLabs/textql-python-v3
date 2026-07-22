"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/sharing.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ..public import engagement_pb2 as public_dot_engagement__pb2
from ..public import options_pb2 as public_dot_options__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14public/sharing.proto\x12\x19textql.rpc.public.sharing\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17public/engagement.proto\x1a\x14public/options.proto".\n\x16GetSharePreviewRequest\x12\x14\n\x05token\x18\x01 \x01(\tR\x05token"\x96\x01\n\x17GetSharePreviewResponse\x12%\n\x0eprimitive_type\x18\x01 \x01(\tR\rprimitiveType\x12.\n\x13sharer_display_name\x18\x02 \x01(\tR\x11sharerDisplayName\x12$\n\x0eorg_brand_name\x18\x03 \x01(\tR\x0corgBrandName"\x9c\x03\n\x05Share\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1f\n\x0bshare_token\x18\x02 \x01(\tR\nshareToken\x12!\n\x0cprimitive_id\x18\x03 \x01(\tR\x0bprimitiveId\x12R\n\x0eprimitive_type\x18\x04 \x01(\x0e2+.textql.rpc.public.engagement.PrimitiveTypeR\rprimitiveType\x12\x1b\n\tsharer_id\x18\x05 \x01(\tR\x08sharerId\x12\x15\n\x06org_id\x18\x06 \x01(\tR\x05orgId\x12A\n\x07channel\x18\x07 \x01(\x0e2\'.textql.rpc.public.sharing.ShareChannelR\x07channel\x129\n\ncreated_at\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt\x129\n\nexpires_at\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampR\texpiresAt"\x89\x02\n\x12CreateShareRequest\x12!\n\x0cprimitive_id\x18\x01 \x01(\tR\x0bprimitiveId\x12R\n\x0eprimitive_type\x18\x02 \x01(\x0e2+.textql.rpc.public.engagement.PrimitiveTypeR\rprimitiveType\x12A\n\x07channel\x18\x03 \x01(\x0e2\'.textql.rpc.public.sharing.ShareChannelR\x07channel\x129\n\nexpires_at\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\texpiresAt"_\n\x13CreateShareResponse\x126\n\x05share\x18\x01 \x01(\x0b2 .textql.rpc.public.sharing.ShareR\x05share\x12\x10\n\x03url\x18\x02 \x01(\tR\x03url"2\n\x0fGetShareRequest\x12\x1f\n\x0bshare_token\x18\x01 \x01(\tR\nshareToken"J\n\x10GetShareResponse\x126\n\x05share\x18\x01 \x01(\x0b2 .textql.rpc.public.sharing.ShareR\x05share"?\n\x1cResolveShareForCallerRequest\x12\x1f\n\x0bshare_token\x18\x01 \x01(\tR\nshareToken"\xf2\x01\n\x1dResolveShareForCallerResponse\x12(\n\x10caller_is_member\x18\x01 \x01(\x08R\x0ecallerIsMember\x12\x19\n\x08same_org\x18\x02 \x01(\x08R\x07sameOrg\x12!\n\x0cprimitive_id\x18\x03 \x01(\tR\x0bprimitiveId\x12R\n\x0eprimitive_type\x18\x04 \x01(\x0e2+.textql.rpc.public.engagement.PrimitiveTypeR\rprimitiveType\x12\x15\n\x06org_id\x18\x05 \x01(\tR\x05orgId*|\n\x0cShareChannel\x12\x1d\n\x19SHARE_CHANNEL_UNSPECIFIED\x10\x00\x12\x17\n\x13SHARE_CHANNEL_SLACK\x10\x01\x12\x17\n\x13SHARE_CHANNEL_EMAIL\x10\x02\x12\x1b\n\x17SHARE_CHANNEL_LINK_COPY\x10\x032\xfa\x02\n\x0eSharingService\x12l\n\x0bCreateShare\x12-.textql.rpc.public.sharing.CreateShareRequest\x1a..textql.rpc.public.sharing.CreateShareResponse\x12h\n\x08GetShare\x12*.textql.rpc.public.sharing.GetShareRequest\x1a+.textql.rpc.public.sharing.GetShareResponse"\x03\x90\x02\x01\x12\x8f\x01\n\x15ResolveShareForCaller\x127.textql.rpc.public.sharing.ResolveShareForCallerRequest\x1a8.textql.rpc.public.sharing.ResolveShareForCallerResponse"\x03\x90\x02\x012\x96\x01\n\x15SharingPreviewService\x12}\n\x0fGetSharePreview\x121.textql.rpc.public.sharing.GetSharePreviewRequest\x1a2.textql.rpc.public.sharing.GetSharePreviewResponse"\x03\x90\x02\x01B\x0c\x92\xb5\x18\x08INTERNALb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.sharing_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\x92\xb5\x18\x08INTERNAL'
    _globals['_SHARINGSERVICE'].methods_by_name['GetShare']._loaded_options = None
    _globals['_SHARINGSERVICE'].methods_by_name['GetShare']._serialized_options = b'\x90\x02\x01'
    _globals['_SHARINGSERVICE'].methods_by_name['ResolveShareForCaller']._loaded_options = None
    _globals['_SHARINGSERVICE'].methods_by_name['ResolveShareForCaller']._serialized_options = b'\x90\x02\x01'
    _globals['_SHARINGPREVIEWSERVICE'].methods_by_name['GetSharePreview']._loaded_options = None
    _globals['_SHARINGPREVIEWSERVICE'].methods_by_name['GetSharePreview']._serialized_options = b'\x90\x02\x01'
    _globals['_SHARECHANNEL']._serialized_start = 1550
    _globals['_SHARECHANNEL']._serialized_end = 1674
    _globals['_GETSHAREPREVIEWREQUEST']._serialized_start = 131
    _globals['_GETSHAREPREVIEWREQUEST']._serialized_end = 177
    _globals['_GETSHAREPREVIEWRESPONSE']._serialized_start = 180
    _globals['_GETSHAREPREVIEWRESPONSE']._serialized_end = 330
    _globals['_SHARE']._serialized_start = 333
    _globals['_SHARE']._serialized_end = 745
    _globals['_CREATESHAREREQUEST']._serialized_start = 748
    _globals['_CREATESHAREREQUEST']._serialized_end = 1013
    _globals['_CREATESHARERESPONSE']._serialized_start = 1015
    _globals['_CREATESHARERESPONSE']._serialized_end = 1110
    _globals['_GETSHAREREQUEST']._serialized_start = 1112
    _globals['_GETSHAREREQUEST']._serialized_end = 1162
    _globals['_GETSHARERESPONSE']._serialized_start = 1164
    _globals['_GETSHARERESPONSE']._serialized_end = 1238
    _globals['_RESOLVESHAREFORCALLERREQUEST']._serialized_start = 1240
    _globals['_RESOLVESHAREFORCALLERREQUEST']._serialized_end = 1303
    _globals['_RESOLVESHAREFORCALLERRESPONSE']._serialized_start = 1306
    _globals['_RESOLVESHAREFORCALLERRESPONSE']._serialized_end = 1548
    _globals['_SHARINGSERVICE']._serialized_start = 1677
    _globals['_SHARINGSERVICE']._serialized_end = 2055
    _globals['_SHARINGPREVIEWSERVICE']._serialized_start = 2058
    _globals['_SHARINGPREVIEWSERVICE']._serialized_end = 2208