# pylint: skip-file
# mypy: ignore-errors
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/paradigm.proto')
_sym_db = _symbol_database.Default()
from ..google.api import visibility_pb2 as google_dot_api_dot_visibility__pb2
from .. import paradigm_params_pb2 as paradigm__params__pb2
from .. import powerbi_selection_pb2 as powerbi__selection__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15public/paradigm.proto\x12\x1atextql.rpc.public.paradigm\x1a\x1bgoogle/api/visibility.proto\x1a\x15paradigm_params.proto\x1a\x17powerbi_selection.proto"\xa9\x01\n\x08Paradigm\x12<\n\x04type\x18\x01 \x01(\x0e2(.textql.rpc.paradigm_params.ParadigmTypeR\x04type\x12\x18\n\x07version\x18\x02 \x01(\x05R\x07version\x12E\n\x07options\x18\x03 \x01(\x0b2+.textql.rpc.public.paradigm.ParadigmOptionsR\x07options"\xca\x06\n\x0fParadigmOptions\x12L\n\x03sql\x18\x01 \x01(\x0b2&.textql.rpc.public.paradigm.SqlOptionsB\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNALH\x00R\x03sql\x12[\n\x08research\x18\x02 \x01(\x0b2+.textql.rpc.public.paradigm.ResearchOptionsB\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNALH\x00R\x08research\x12[\n\x08ontology\x18\x03 \x01(\x0b2+.textql.rpc.public.paradigm.OntologyOptionsB\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNALH\x00R\x08ontology\x12R\n\x05basic\x18\x04 \x01(\x0b2(.textql.rpc.public.paradigm.BasicOptionsB\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNALH\x00R\x05basic\x12X\n\x07tableau\x18\x05 \x01(\x0b2*.textql.rpc.public.paradigm.TableauOptionsB\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNALH\x00R\x07tableau\x12g\n\x0cexperimental\x18\x06 \x01(\x0b2/.textql.rpc.public.paradigm.ExperimentalOptionsB\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNALH\x00R\x0cexperimental\x12L\n\tuniversal\x18\x07 \x01(\x0b2,.textql.rpc.public.paradigm.UniversalOptionsH\x00R\tuniversal\x12b\n\x0bpublic_demo\x18\x08 \x01(\x0b2-.textql.rpc.public.paradigm.PublicDemoOptionsB\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNALH\x00R\npublicDemo\x12[\n\x08template\x18\t \x01(\x0b2+.textql.rpc.public.paradigm.TemplateOptionsB\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNALH\x00R\x08templateB\t\n\x07options"C\n\nSqlOptions\x12#\n\rconnector_ids\x18\x01 \x03(\x05R\x0cconnectorIds:\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL"\xaf\x01\n\x0fResearchOptions\x12#\n\rconnector_ids\x18\x01 \x03(\x05R\x0cconnectorIds\x12.\n\x10background_color\x18\x02 \x01(\tH\x00R\x0fbackgroundColor\x88\x01\x01\x12\x17\n\x04logo\x18\x03 \x01(\tH\x01R\x04logo\x88\x01\x01:\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNALB\x13\n\x11_background_colorB\x07\n\x05_logo"~\n\x13ExperimentalOptions\x12#\n\rconnector_ids\x18\x01 \x03(\x05R\x0cconnectorIds\x120\n\x14auto_approve_enabled\x18\x02 \x01(\x08R\x12autoApproveEnabled:\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL" \n\x0cBasicOptions:\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL"k\n\x0fOntologyOptions\x12#\n\rconnector_ids\x18\x01 \x03(\x05R\x0cconnectorIds\x12!\n\x0contology_ids\x18\x02 \x03(\x05R\x0bontologyIds:\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL"A\n\x0eTableauOptions\x12\x1d\n\ndataset_id\x18\x01 \x01(\tR\tdatasetId:\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL"\x8a\x0b\n\x10UniversalOptions\x12#\n\rconnector_ids\x18\x01 \x03(\x05R\x0cconnectorIds\x12"\n\ndataset_id\x18\x02 \x01(\tH\x00R\tdatasetId\x88\x01\x01\x12,\n\x12web_search_enabled\x18\x03 \x01(\x08R\x10webSearchEnabled\x12\x1f\n\x0bsql_enabled\x18\x04 \x01(\x08R\nsqlEnabled\x12)\n\x10ontology_enabled\x18\x05 \x01(\x08R\x0fontologyEnabled\x128\n\x18ontology_editing_enabled\x18\x06 \x01(\x08R\x16ontologyEditingEnabled\x12%\n\x0epython_enabled\x18\x07 \x01(\x08R\rpythonEnabled\x120\n\x14auto_approve_enabled\x18\x08 \x01(\x08R\x12autoApproveEnabled\x120\n\x14google_drive_enabled\x18\t \x01(\x08R\x12googleDriveEnabled\x12\'\n\x0fpowerbi_enabled\x18\n \x01(\x08R\x0epowerbiEnabled\x126\n\x17context_editing_enabled\x18\x0b \x01(\x08R\x15contextEditingEnabled\x12.\n\x13form_editor_enabled\x18\x0c \x01(\x08R\x11formEditorEnabled\x124\n\x16playbook_tools_enabled\x18\r \x01(\x08R\x14playbookToolsEnabled\x121\n\x14microsoft365_enabled\x18\x0e \x01(\x08R\x13microsoft365Enabled\x122\n\x15feed_explorer_enabled\x18\x0f \x01(\x08R\x13feedExplorerEnabled\x12!\n\x0cbash_enabled\x18\x10 \x01(\x08R\x0bbashEnabled\x12-\n\x12javascript_enabled\x18\x11 \x01(\x08R\x11javascriptEnabled\x12*\n\x11feed_post_enabled\x18\x12 \x01(\x08R\x0ffeedPostEnabled\x120\n\x14feed_comment_enabled\x18\x13 \x01(\x08R\x12feedCommentEnabled\x12.\n\x13feed_engage_enabled\x18\x14 \x01(\x08R\x11feedEngageEnabled\x12+\n\x11streamlit_enabled\x18\x15 \x01(\x08R\x10streamlitEnabled\x12/\n\x13compaction_disabled\x18\x16 \x01(\x08R\x12compactionDisabled\x12#\n\rgmail_enabled\x18\x17 \x01(\x08R\x0cgmailEnabled\x12=\n\x1bchat_history_search_enabled\x18\x18 \x01(\x08R\x18chatHistorySearchEnabled\x126\n\x17google_calendar_enabled\x18\x19 \x01(\x08R\x15googleCalendarEnabled\x120\n\x14email_output_enabled\x18\x1a \x01(\x08R\x12emailOutputEnabled\x12]\n\x12powerbi_selections\x18\x1b \x03(\x0b2..textql.rpc.powerbi_selection.PowerBISelectionR\x11powerbiSelections\x12\x19\n\x08sms_mode\x18\x1c \x01(\x08R\x07smsMode\x12+\n\x12api_access_key_ids\x18\x1d \x03(\tR\x0fapiAccessKeyIdsB\r\n\x0b_dataset_id"I\n\x12GoogleDriveOptions\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId:\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL"H\n\x11PublicDemoOptions\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId:\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL"H\n\x0fTemplateOptions\x12#\n\rcapture_tools\x18\x01 \x03(\tR\x0ccaptureTools:\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNALb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.paradigm_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_PARADIGMOPTIONS'].fields_by_name['sql']._loaded_options = None
    _globals['_PARADIGMOPTIONS'].fields_by_name['sql']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_PARADIGMOPTIONS'].fields_by_name['research']._loaded_options = None
    _globals['_PARADIGMOPTIONS'].fields_by_name['research']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_PARADIGMOPTIONS'].fields_by_name['ontology']._loaded_options = None
    _globals['_PARADIGMOPTIONS'].fields_by_name['ontology']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_PARADIGMOPTIONS'].fields_by_name['basic']._loaded_options = None
    _globals['_PARADIGMOPTIONS'].fields_by_name['basic']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_PARADIGMOPTIONS'].fields_by_name['tableau']._loaded_options = None
    _globals['_PARADIGMOPTIONS'].fields_by_name['tableau']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_PARADIGMOPTIONS'].fields_by_name['experimental']._loaded_options = None
    _globals['_PARADIGMOPTIONS'].fields_by_name['experimental']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_PARADIGMOPTIONS'].fields_by_name['public_demo']._loaded_options = None
    _globals['_PARADIGMOPTIONS'].fields_by_name['public_demo']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_PARADIGMOPTIONS'].fields_by_name['template']._loaded_options = None
    _globals['_PARADIGMOPTIONS'].fields_by_name['template']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_SQLOPTIONS']._loaded_options = None
    _globals['_SQLOPTIONS']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_RESEARCHOPTIONS']._loaded_options = None
    _globals['_RESEARCHOPTIONS']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_EXPERIMENTALOPTIONS']._loaded_options = None
    _globals['_EXPERIMENTALOPTIONS']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_BASICOPTIONS']._loaded_options = None
    _globals['_BASICOPTIONS']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_ONTOLOGYOPTIONS']._loaded_options = None
    _globals['_ONTOLOGYOPTIONS']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_TABLEAUOPTIONS']._loaded_options = None
    _globals['_TABLEAUOPTIONS']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_GOOGLEDRIVEOPTIONS']._loaded_options = None
    _globals['_GOOGLEDRIVEOPTIONS']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_PUBLICDEMOOPTIONS']._loaded_options = None
    _globals['_PUBLICDEMOOPTIONS']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_TEMPLATEOPTIONS']._loaded_options = None
    _globals['_TEMPLATEOPTIONS']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_PARADIGM']._serialized_start = 131
    _globals['_PARADIGM']._serialized_end = 300
    _globals['_PARADIGMOPTIONS']._serialized_start = 303
    _globals['_PARADIGMOPTIONS']._serialized_end = 1145
    _globals['_SQLOPTIONS']._serialized_start = 1147
    _globals['_SQLOPTIONS']._serialized_end = 1214
    _globals['_RESEARCHOPTIONS']._serialized_start = 1217
    _globals['_RESEARCHOPTIONS']._serialized_end = 1392
    _globals['_EXPERIMENTALOPTIONS']._serialized_start = 1394
    _globals['_EXPERIMENTALOPTIONS']._serialized_end = 1520
    _globals['_BASICOPTIONS']._serialized_start = 1522
    _globals['_BASICOPTIONS']._serialized_end = 1554
    _globals['_ONTOLOGYOPTIONS']._serialized_start = 1556
    _globals['_ONTOLOGYOPTIONS']._serialized_end = 1663
    _globals['_TABLEAUOPTIONS']._serialized_start = 1665
    _globals['_TABLEAUOPTIONS']._serialized_end = 1730
    _globals['_UNIVERSALOPTIONS']._serialized_start = 1733
    _globals['_UNIVERSALOPTIONS']._serialized_end = 3151
    _globals['_GOOGLEDRIVEOPTIONS']._serialized_start = 3153
    _globals['_GOOGLEDRIVEOPTIONS']._serialized_end = 3226
    _globals['_PUBLICDEMOOPTIONS']._serialized_start = 3228
    _globals['_PUBLICDEMOOPTIONS']._serialized_end = 3300
    _globals['_TEMPLATEOPTIONS']._serialized_start = 3302
    _globals['_TEMPLATEOPTIONS']._serialized_end = 3374