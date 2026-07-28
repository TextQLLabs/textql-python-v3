# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
# pylint: skip-file
# mypy: ignore-errors
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'paradigm_params.proto')
_sym_db = _symbol_database.Default()
from .google.api import visibility_pb2 as google_dot_api_dot_visibility__pb2
from . import powerbi_selection_pb2 as powerbi__selection__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15paradigm_params.proto\x12\x1atextql.rpc.paradigm_params\x1a\x1bgoogle/api/visibility.proto\x1a\x17powerbi_selection.proto"\xaa\x0c\n\x0eParadigmParams\x12,\n\x12web_search_enabled\x18\x01 \x01(\x08R\x10webSearchEnabled\x12\x1f\n\x0bsql_enabled\x18\x02 \x01(\x08R\nsqlEnabled\x12)\n\x10ontology_enabled\x18\x03 \x01(\x08R\x0fontologyEnabled\x128\n\x18ontology_editing_enabled\x18\x04 \x01(\x08R\x16ontologyEditingEnabled\x12%\n\x0epython_enabled\x18\x06 \x01(\x08R\rpythonEnabled\x12\'\n\x0fpowerbi_enabled\x18\x07 \x01(\x08R\x0epowerbiEnabled\x120\n\x14google_drive_enabled\x18\x08 \x01(\x08R\x12googleDriveEnabled\x120\n\x14auto_approve_enabled\x18\t \x01(\x08R\x12autoApproveEnabled\x126\n\x17context_editing_enabled\x18\n \x01(\x08R\x15contextEditingEnabled\x12.\n\x13form_editor_enabled\x18\x0b \x01(\x08R\x11formEditorEnabled\x12\'\n\x0ftableau_enabled\x18\x0c \x01(\x08R\x0etableauEnabled\x12.\n\x13file_upload_enabled\x18\r \x01(\x08R\x11fileUploadEnabled\x126\n\x17multiple_connector_mode\x18\x0e \x01(\x08R\x15multipleConnectorMode\x124\n\x16playbook_tools_enabled\x18\x0f \x01(\x08R\x14playbookToolsEnabled\x122\n\x15microsoft_365_enabled\x18\x10 \x01(\x08R\x13microsoft365Enabled\x12!\n\x0cbash_enabled\x18\x11 \x01(\x08R\x0bbashEnabled\x12-\n\x12javascript_enabled\x18\x12 \x01(\x08R\x11javascriptEnabled\x126\n\x17model_switching_enabled\x18\x13 \x01(\x08R\x15modelSwitchingEnabled\x122\n\x15feed_explorer_enabled\x18\x14 \x01(\x08R\x13feedExplorerEnabled\x12*\n\x11feed_post_enabled\x18\x15 \x01(\x08R\x0ffeedPostEnabled\x120\n\x14feed_comment_enabled\x18\x16 \x01(\x08R\x12feedCommentEnabled\x12.\n\x13feed_engage_enabled\x18\x17 \x01(\x08R\x11feedEngageEnabled\x12/\n\x13compaction_disabled\x18\x18 \x01(\x08R\x12compactionDisabled\x12#\n\rgmail_enabled\x18\x19 \x01(\x08R\x0cgmailEnabled\x12=\n\x1bchat_history_search_enabled\x18\x1a \x01(\x08R\x18chatHistorySearchEnabled\x126\n\x17google_calendar_enabled\x18\x1b \x01(\x08R\x15googleCalendarEnabled\x124\n\x16parallel_tools_enabled\x18\x1c \x01(\x08R\x14parallelToolsEnabled\x120\n\x14email_output_enabled\x18\x1e \x01(\x08R\x12emailOutputEnabled\x124\n\x16questions_tool_enabled\x18\x1f \x01(\x08R\x14questionsToolEnabled\x12]\n\x12powerbi_selections\x18  \x03(\x0b2..textql.rpc.powerbi_selection.PowerBISelectionR\x11powerbiSelections\x12"\n\ndataset_id\x18! \x01(\tH\x00R\tdatasetId\x88\x01\x01B\r\n\x0b_dataset_idJ\x04\x08\x1d\x10\x1e*\xf2\x03\n\x0cParadigmType\x12\x10\n\x0cTYPE_UNKNOWN\x10\x00\x12\x1e\n\x08TYPE_SQL\x10\x01\x1a\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL\x12#\n\rTYPE_RESEARCH\x10\x02\x1a\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL\x12#\n\rTYPE_ONTOLOGY\x10\x03\x1a\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL\x12 \n\nTYPE_BASIC\x10\x04\x1a\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL\x12"\n\x0cTYPE_TABLEAU\x10\x05\x1a\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL\x12\'\n\x11TYPE_EXPERIMENTAL\x10\x07\x1a\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL\x12\x12\n\x0eTYPE_UNIVERSAL\x10\x08\x12&\n\x10TYPE_PUBLIC_DEMO\x10\t\x1a\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL\x12"\n\x0cTYPE_SUMMARY\x10\n\x1a\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL\x12(\n\x12TYPE_OBSERVABILITY\x10\x0b\x1a\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL\x12#\n\rTYPE_TEMPLATE\x10\x0c\x1a\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL\x12%\n\x0fTYPE_MINIMALIST\x10\r\x1a\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL\x12!\n\x0bTYPE_TOPICS\x10\x0e\x1a\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNALb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'paradigm_params_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_PARADIGMTYPE'].values_by_name['TYPE_SQL']._loaded_options = None
    _globals['_PARADIGMTYPE'].values_by_name['TYPE_SQL']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_PARADIGMTYPE'].values_by_name['TYPE_RESEARCH']._loaded_options = None
    _globals['_PARADIGMTYPE'].values_by_name['TYPE_RESEARCH']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_PARADIGMTYPE'].values_by_name['TYPE_ONTOLOGY']._loaded_options = None
    _globals['_PARADIGMTYPE'].values_by_name['TYPE_ONTOLOGY']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_PARADIGMTYPE'].values_by_name['TYPE_BASIC']._loaded_options = None
    _globals['_PARADIGMTYPE'].values_by_name['TYPE_BASIC']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_PARADIGMTYPE'].values_by_name['TYPE_TABLEAU']._loaded_options = None
    _globals['_PARADIGMTYPE'].values_by_name['TYPE_TABLEAU']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_PARADIGMTYPE'].values_by_name['TYPE_EXPERIMENTAL']._loaded_options = None
    _globals['_PARADIGMTYPE'].values_by_name['TYPE_EXPERIMENTAL']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_PARADIGMTYPE'].values_by_name['TYPE_PUBLIC_DEMO']._loaded_options = None
    _globals['_PARADIGMTYPE'].values_by_name['TYPE_PUBLIC_DEMO']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_PARADIGMTYPE'].values_by_name['TYPE_SUMMARY']._loaded_options = None
    _globals['_PARADIGMTYPE'].values_by_name['TYPE_SUMMARY']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_PARADIGMTYPE'].values_by_name['TYPE_OBSERVABILITY']._loaded_options = None
    _globals['_PARADIGMTYPE'].values_by_name['TYPE_OBSERVABILITY']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_PARADIGMTYPE'].values_by_name['TYPE_TEMPLATE']._loaded_options = None
    _globals['_PARADIGMTYPE'].values_by_name['TYPE_TEMPLATE']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_PARADIGMTYPE'].values_by_name['TYPE_MINIMALIST']._loaded_options = None
    _globals['_PARADIGMTYPE'].values_by_name['TYPE_MINIMALIST']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_PARADIGMTYPE'].values_by_name['TYPE_TOPICS']._loaded_options = None
    _globals['_PARADIGMTYPE'].values_by_name['TYPE_TOPICS']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_PARADIGMTYPE']._serialized_start = 1689
    _globals['_PARADIGMTYPE']._serialized_end = 2187
    _globals['_PARADIGMPARAMS']._serialized_start = 108
    _globals['_PARADIGMPARAMS']._serialized_end = 1686