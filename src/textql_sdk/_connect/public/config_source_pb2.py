"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/config_source.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1apublic/config_source.proto\x12\x1ftextql.rpc.public.config_source"\xf9\x01\n\x0cConfigSource\x12\x1b\n\tfile_path\x18\x01 \x01(\tR\x08filePath\x12R\n\x0bsync_status\x18\x02 \x01(\x0e21.textql.rpc.public.config_source.ConfigSyncStatusR\nsyncStatus\x12"\n\nsync_error\x18\x03 \x01(\tH\x00R\tsyncError\x88\x01\x01\x12/\n\x11breaking_patch_id\x18\x04 \x01(\tH\x01R\x0fbreakingPatchId\x88\x01\x01B\r\n\x0b_sync_errorB\x14\n\x12_breaking_patch_id*\x93\x01\n\x10ConfigSyncStatus\x12"\n\x1eCONFIG_SYNC_STATUS_UNSPECIFIED\x10\x00\x12\x1e\n\x1aCONFIG_SYNC_STATUS_SYNCING\x10\x01\x12\x1d\n\x19CONFIG_SYNC_STATUS_SYNCED\x10\x02\x12\x1c\n\x18CONFIG_SYNC_STATUS_ERROR\x10\x03b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.config_source_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_CONFIGSYNCSTATUS']._serialized_start = 316
    _globals['_CONFIGSYNCSTATUS']._serialized_end = 463
    _globals['_CONFIGSOURCE']._serialized_start = 64
    _globals['_CONFIGSOURCE']._serialized_end = 313