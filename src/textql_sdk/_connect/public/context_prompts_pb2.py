# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
# pylint: skip-file
# mypy: ignore-errors
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/context_prompts.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ..public import options_pb2 as public_dot_options__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cpublic/context_prompts.proto\x12!textql.rpc.public.context_prompts\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14public/options.proto"\xd0\x03\n\rContextPrompt\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x16\n\x06prompt\x18\x03 \x01(\tR\x06prompt\x12\x15\n\x06is_org\x18\x04 \x01(\x08R\x05isOrg\x12\x16\n\x06active\x18\x05 \x01(\x08R\x06active\x12%\n\x0eassigned_roles\x18\x06 \x03(\tR\rassignedRoles\x12+\n\x11assigned_datasets\x18\x07 \x03(\tR\x10assignedDatasets\x12/\n\x13assigned_connectors\x18\x08 \x03(\x05R\x12assignedConnectors\x129\n\ncreated_at\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt\x129\n\nupdated_at\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampR\tupdatedAt\x12\x1f\n\x0bauto_attach\x18\x0b \x01(\x08R\nautoAttach\x12\x1b\n\tcan_write\x18\x0c \x01(\x08R\x08canWrite\x12\x1b\n\tis_public\x18\r \x01(\x08R\x08isPublic"\x99\x02\n\x1aCreateContextPromptRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x16\n\x06prompt\x18\x02 \x01(\tR\x06prompt\x12\x15\n\x06is_org\x18\x03 \x01(\x08R\x05isOrg\x12(\n\x10initial_role_ids\x18\x04 \x03(\tR\x0einitialRoleIds\x12)\n\x10initial_datasets\x18\x05 \x03(\tR\x0finitialDatasets\x12-\n\x12initial_connectors\x18\x06 \x03(\x05R\x11initialConnectors\x12$\n\x0bauto_attach\x18\x07 \x01(\x08H\x00R\nautoAttach\x88\x01\x01B\x0e\n\x0c_auto_attach"\xb5\x01\n\x1bCreateContextPromptResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x19\n\x05error\x18\x02 \x01(\tH\x00R\x05error\x88\x01\x01\x12W\n\x0econtext_prompt\x18\x03 \x01(\x0b20.textql.rpc.public.context_prompts.ContextPromptR\rcontextPromptB\x08\n\x06_error"\xd3\x01\n\x1aUpdateContextPromptRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x17\n\x04name\x18\x02 \x01(\tH\x00R\x04name\x88\x01\x01\x12\x1b\n\x06prompt\x18\x03 \x01(\tH\x01R\x06prompt\x88\x01\x01\x12\x1a\n\x06is_org\x18\x04 \x01(\x08H\x02R\x05isOrg\x88\x01\x01\x12$\n\x0bauto_attach\x18\x05 \x01(\x08H\x03R\nautoAttach\x88\x01\x01B\x07\n\x05_nameB\t\n\x07_promptB\t\n\x07_is_orgB\x0e\n\x0c_auto_attach"\xb5\x01\n\x1bUpdateContextPromptResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x19\n\x05error\x18\x02 \x01(\tH\x00R\x05error\x88\x01\x01\x12W\n\x0econtext_prompt\x18\x03 \x01(\x0b20.textql.rpc.public.context_prompts.ContextPromptR\rcontextPromptB\x08\n\x06_error",\n\x1aDeleteContextPromptRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\\\n\x1bDeleteContextPromptResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x19\n\x05error\x18\x02 \x01(\tH\x00R\x05error\x88\x01\x01B\x08\n\x06_error"!\n\x1fListAllOrgContextPromptsRequest"}\n ListAllOrgContextPromptsResponse\x12Y\n\x0fcontext_prompts\x18\x01 \x03(\x0b20.textql.rpc.public.context_prompts.ContextPromptR\x0econtextPrompts"j\n!AssignContextPromptToRolesRequest\x12*\n\x11context_prompt_id\x18\x01 \x01(\tR\x0fcontextPromptId\x12\x19\n\x08role_ids\x18\x02 \x03(\tR\x07roleIds"c\n"AssignContextPromptToRolesResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x19\n\x05error\x18\x02 \x01(\tH\x00R\x05error\x88\x01\x01B\x08\n\x06_error"l\n#RemoveContextPromptFromRolesRequest\x12*\n\x11context_prompt_id\x18\x01 \x01(\tR\x0fcontextPromptId\x12\x19\n\x08role_ids\x18\x02 \x03(\tR\x07roleIds"e\n$RemoveContextPromptFromRolesResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x19\n\x05error\x18\x02 \x01(\tH\x00R\x05error\x88\x01\x01B\x08\n\x06_error"9\n\x1eGetContextPromptsByRoleRequest\x12\x17\n\x07role_id\x18\x01 \x01(\tR\x06roleId"|\n\x1fGetContextPromptsByRoleResponse\x12Y\n\x0fcontext_prompts\x18\x01 \x03(\x0b20.textql.rpc.public.context_prompts.ContextPromptR\x0econtextPrompts"s\n$AssignDatasetsToContextPromptRequest\x12*\n\x11context_prompt_id\x18\x01 \x01(\tR\x0fcontextPromptId\x12\x1f\n\x0bdataset_ids\x18\x02 \x03(\tR\ndatasetIds"f\n%AssignDatasetsToContextPromptResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x19\n\x05error\x18\x02 \x01(\tH\x00R\x05error\x88\x01\x01B\x08\n\x06_error"u\n&RemoveDatasetsFromContextPromptRequest\x12*\n\x11context_prompt_id\x18\x01 \x01(\tR\x0fcontextPromptId\x12\x1f\n\x0bdataset_ids\x18\x02 \x03(\tR\ndatasetIds"h\n\'RemoveDatasetsFromContextPromptResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x19\n\x05error\x18\x02 \x01(\tH\x00R\x05error\x88\x01\x01B\x08\n\x06_error"B\n!GetContextPromptsByDatasetRequest\x12\x1d\n\ndataset_id\x18\x01 \x01(\tR\tdatasetId"\x7f\n"GetContextPromptsByDatasetResponse\x12Y\n\x0fcontext_prompts\x18\x01 \x03(\x0b20.textql.rpc.public.context_prompts.ContextPromptR\x0econtextPrompts"y\n&AssignContextPromptToConnectorsRequest\x12*\n\x11context_prompt_id\x18\x01 \x01(\tR\x0fcontextPromptId\x12#\n\rconnector_ids\x18\x02 \x03(\x05R\x0cconnectorIds"h\n\'AssignContextPromptToConnectorsResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x19\n\x05error\x18\x02 \x01(\tH\x00R\x05error\x88\x01\x01B\x08\n\x06_error"{\n(RemoveContextPromptFromConnectorsRequest\x12*\n\x11context_prompt_id\x18\x01 \x01(\tR\x0fcontextPromptId\x12#\n\rconnector_ids\x18\x02 \x03(\x05R\x0cconnectorIds"j\n)RemoveContextPromptFromConnectorsResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x19\n\x05error\x18\x02 \x01(\tH\x00R\x05error\x88\x01\x01B\x08\n\x06_error"H\n#GetContextPromptsByConnectorRequest\x12!\n\x0cconnector_id\x18\x01 \x01(\x05R\x0bconnectorId"\x81\x01\n$GetContextPromptsByConnectorResponse\x12Y\n\x0fcontext_prompts\x18\x01 \x03(\x0b20.textql.rpc.public.context_prompts.ContextPromptR\x0econtextPrompts"J\n ToggleContextPromptActiveRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x16\n\x06active\x18\x02 \x01(\x08R\x06active"\xbb\x01\n!ToggleContextPromptActiveResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x19\n\x05error\x18\x02 \x01(\tH\x00R\x05error\x88\x01\x01\x12W\n\x0econtext_prompt\x18\x03 \x01(\x0b20.textql.rpc.public.context_prompts.ContextPromptR\rcontextPromptB\x08\n\x06_error2\x8a\x13\n\x15ContextPromptsService\x12\x94\x01\n\x13CreateContextPrompt\x12=.textql.rpc.public.context_prompts.CreateContextPromptRequest\x1a>.textql.rpc.public.context_prompts.CreateContextPromptResponse\x12\x94\x01\n\x13UpdateContextPrompt\x12=.textql.rpc.public.context_prompts.UpdateContextPromptRequest\x1a>.textql.rpc.public.context_prompts.UpdateContextPromptResponse\x12\x94\x01\n\x13DeleteContextPrompt\x12=.textql.rpc.public.context_prompts.DeleteContextPromptRequest\x1a>.textql.rpc.public.context_prompts.DeleteContextPromptResponse\x12\xa8\x01\n\x18ListAllOrgContextPrompts\x12B.textql.rpc.public.context_prompts.ListAllOrgContextPromptsRequest\x1aC.textql.rpc.public.context_prompts.ListAllOrgContextPromptsResponse"\x03\x90\x02\x01\x12\xa9\x01\n\x1aAssignContextPromptToRoles\x12D.textql.rpc.public.context_prompts.AssignContextPromptToRolesRequest\x1aE.textql.rpc.public.context_prompts.AssignContextPromptToRolesResponse\x12\xaf\x01\n\x1cRemoveContextPromptFromRoles\x12F.textql.rpc.public.context_prompts.RemoveContextPromptFromRolesRequest\x1aG.textql.rpc.public.context_prompts.RemoveContextPromptFromRolesResponse\x12\xa5\x01\n\x17GetContextPromptsByRole\x12A.textql.rpc.public.context_prompts.GetContextPromptsByRoleRequest\x1aB.textql.rpc.public.context_prompts.GetContextPromptsByRoleResponse"\x03\x90\x02\x01\x12\xb2\x01\n\x1dAssignDatasetsToContextPrompt\x12G.textql.rpc.public.context_prompts.AssignDatasetsToContextPromptRequest\x1aH.textql.rpc.public.context_prompts.AssignDatasetsToContextPromptResponse\x12\xb8\x01\n\x1fRemoveDatasetsFromContextPrompt\x12I.textql.rpc.public.context_prompts.RemoveDatasetsFromContextPromptRequest\x1aJ.textql.rpc.public.context_prompts.RemoveDatasetsFromContextPromptResponse\x12\xae\x01\n\x1aGetContextPromptsByDataset\x12D.textql.rpc.public.context_prompts.GetContextPromptsByDatasetRequest\x1aE.textql.rpc.public.context_prompts.GetContextPromptsByDatasetResponse"\x03\x90\x02\x01\x12\xb8\x01\n\x1fAssignContextPromptToConnectors\x12I.textql.rpc.public.context_prompts.AssignContextPromptToConnectorsRequest\x1aJ.textql.rpc.public.context_prompts.AssignContextPromptToConnectorsResponse\x12\xbe\x01\n!RemoveContextPromptFromConnectors\x12K.textql.rpc.public.context_prompts.RemoveContextPromptFromConnectorsRequest\x1aL.textql.rpc.public.context_prompts.RemoveContextPromptFromConnectorsResponse\x12\xb4\x01\n\x1cGetContextPromptsByConnector\x12F.textql.rpc.public.context_prompts.GetContextPromptsByConnectorRequest\x1aG.textql.rpc.public.context_prompts.GetContextPromptsByConnectorResponse"\x03\x90\x02\x01\x12\xa6\x01\n\x19ToggleContextPromptActive\x12C.textql.rpc.public.context_prompts.ToggleContextPromptActiveRequest\x1aD.textql.rpc.public.context_prompts.ToggleContextPromptActiveResponseB\x0c\x92\xb5\x18\x08INTERNALb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.context_prompts_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\x92\xb5\x18\x08INTERNAL'
    _globals['_CONTEXTPROMPTSSERVICE'].methods_by_name['ListAllOrgContextPrompts']._loaded_options = None
    _globals['_CONTEXTPROMPTSSERVICE'].methods_by_name['ListAllOrgContextPrompts']._serialized_options = b'\x90\x02\x01'
    _globals['_CONTEXTPROMPTSSERVICE'].methods_by_name['GetContextPromptsByRole']._loaded_options = None
    _globals['_CONTEXTPROMPTSSERVICE'].methods_by_name['GetContextPromptsByRole']._serialized_options = b'\x90\x02\x01'
    _globals['_CONTEXTPROMPTSSERVICE'].methods_by_name['GetContextPromptsByDataset']._loaded_options = None
    _globals['_CONTEXTPROMPTSSERVICE'].methods_by_name['GetContextPromptsByDataset']._serialized_options = b'\x90\x02\x01'
    _globals['_CONTEXTPROMPTSSERVICE'].methods_by_name['GetContextPromptsByConnector']._loaded_options = None
    _globals['_CONTEXTPROMPTSSERVICE'].methods_by_name['GetContextPromptsByConnector']._serialized_options = b'\x90\x02\x01'
    _globals['_CONTEXTPROMPT']._serialized_start = 123
    _globals['_CONTEXTPROMPT']._serialized_end = 587
    _globals['_CREATECONTEXTPROMPTREQUEST']._serialized_start = 590
    _globals['_CREATECONTEXTPROMPTREQUEST']._serialized_end = 871
    _globals['_CREATECONTEXTPROMPTRESPONSE']._serialized_start = 874
    _globals['_CREATECONTEXTPROMPTRESPONSE']._serialized_end = 1055
    _globals['_UPDATECONTEXTPROMPTREQUEST']._serialized_start = 1058
    _globals['_UPDATECONTEXTPROMPTREQUEST']._serialized_end = 1269
    _globals['_UPDATECONTEXTPROMPTRESPONSE']._serialized_start = 1272
    _globals['_UPDATECONTEXTPROMPTRESPONSE']._serialized_end = 1453
    _globals['_DELETECONTEXTPROMPTREQUEST']._serialized_start = 1455
    _globals['_DELETECONTEXTPROMPTREQUEST']._serialized_end = 1499
    _globals['_DELETECONTEXTPROMPTRESPONSE']._serialized_start = 1501
    _globals['_DELETECONTEXTPROMPTRESPONSE']._serialized_end = 1593
    _globals['_LISTALLORGCONTEXTPROMPTSREQUEST']._serialized_start = 1595
    _globals['_LISTALLORGCONTEXTPROMPTSREQUEST']._serialized_end = 1628
    _globals['_LISTALLORGCONTEXTPROMPTSRESPONSE']._serialized_start = 1630
    _globals['_LISTALLORGCONTEXTPROMPTSRESPONSE']._serialized_end = 1755
    _globals['_ASSIGNCONTEXTPROMPTTOROLESREQUEST']._serialized_start = 1757
    _globals['_ASSIGNCONTEXTPROMPTTOROLESREQUEST']._serialized_end = 1863
    _globals['_ASSIGNCONTEXTPROMPTTOROLESRESPONSE']._serialized_start = 1865
    _globals['_ASSIGNCONTEXTPROMPTTOROLESRESPONSE']._serialized_end = 1964
    _globals['_REMOVECONTEXTPROMPTFROMROLESREQUEST']._serialized_start = 1966
    _globals['_REMOVECONTEXTPROMPTFROMROLESREQUEST']._serialized_end = 2074
    _globals['_REMOVECONTEXTPROMPTFROMROLESRESPONSE']._serialized_start = 2076
    _globals['_REMOVECONTEXTPROMPTFROMROLESRESPONSE']._serialized_end = 2177
    _globals['_GETCONTEXTPROMPTSBYROLEREQUEST']._serialized_start = 2179
    _globals['_GETCONTEXTPROMPTSBYROLEREQUEST']._serialized_end = 2236
    _globals['_GETCONTEXTPROMPTSBYROLERESPONSE']._serialized_start = 2238
    _globals['_GETCONTEXTPROMPTSBYROLERESPONSE']._serialized_end = 2362
    _globals['_ASSIGNDATASETSTOCONTEXTPROMPTREQUEST']._serialized_start = 2364
    _globals['_ASSIGNDATASETSTOCONTEXTPROMPTREQUEST']._serialized_end = 2479
    _globals['_ASSIGNDATASETSTOCONTEXTPROMPTRESPONSE']._serialized_start = 2481
    _globals['_ASSIGNDATASETSTOCONTEXTPROMPTRESPONSE']._serialized_end = 2583
    _globals['_REMOVEDATASETSFROMCONTEXTPROMPTREQUEST']._serialized_start = 2585
    _globals['_REMOVEDATASETSFROMCONTEXTPROMPTREQUEST']._serialized_end = 2702
    _globals['_REMOVEDATASETSFROMCONTEXTPROMPTRESPONSE']._serialized_start = 2704
    _globals['_REMOVEDATASETSFROMCONTEXTPROMPTRESPONSE']._serialized_end = 2808
    _globals['_GETCONTEXTPROMPTSBYDATASETREQUEST']._serialized_start = 2810
    _globals['_GETCONTEXTPROMPTSBYDATASETREQUEST']._serialized_end = 2876
    _globals['_GETCONTEXTPROMPTSBYDATASETRESPONSE']._serialized_start = 2878
    _globals['_GETCONTEXTPROMPTSBYDATASETRESPONSE']._serialized_end = 3005
    _globals['_ASSIGNCONTEXTPROMPTTOCONNECTORSREQUEST']._serialized_start = 3007
    _globals['_ASSIGNCONTEXTPROMPTTOCONNECTORSREQUEST']._serialized_end = 3128
    _globals['_ASSIGNCONTEXTPROMPTTOCONNECTORSRESPONSE']._serialized_start = 3130
    _globals['_ASSIGNCONTEXTPROMPTTOCONNECTORSRESPONSE']._serialized_end = 3234
    _globals['_REMOVECONTEXTPROMPTFROMCONNECTORSREQUEST']._serialized_start = 3236
    _globals['_REMOVECONTEXTPROMPTFROMCONNECTORSREQUEST']._serialized_end = 3359
    _globals['_REMOVECONTEXTPROMPTFROMCONNECTORSRESPONSE']._serialized_start = 3361
    _globals['_REMOVECONTEXTPROMPTFROMCONNECTORSRESPONSE']._serialized_end = 3467
    _globals['_GETCONTEXTPROMPTSBYCONNECTORREQUEST']._serialized_start = 3469
    _globals['_GETCONTEXTPROMPTSBYCONNECTORREQUEST']._serialized_end = 3541
    _globals['_GETCONTEXTPROMPTSBYCONNECTORRESPONSE']._serialized_start = 3544
    _globals['_GETCONTEXTPROMPTSBYCONNECTORRESPONSE']._serialized_end = 3673
    _globals['_TOGGLECONTEXTPROMPTACTIVEREQUEST']._serialized_start = 3675
    _globals['_TOGGLECONTEXTPROMPTACTIVEREQUEST']._serialized_end = 3749
    _globals['_TOGGLECONTEXTPROMPTACTIVERESPONSE']._serialized_start = 3752
    _globals['_TOGGLECONTEXTPROMPTACTIVERESPONSE']._serialized_end = 3939
    _globals['_CONTEXTPROMPTSSERVICE']._serialized_start = 3942
    _globals['_CONTEXTPROMPTSSERVICE']._serialized_end = 6384