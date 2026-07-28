# pylint: skip-file
# mypy: ignore-errors
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/mcp.proto')
_sym_db = _symbol_database.Default()
from ..google.api import visibility_pb2 as google_dot_api_dot_visibility__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10public/mcp.proto\x12\x15textql.rpc.public.mcp\x1a\x1bgoogle/api/visibility.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa4\x01\n\nHttpConfig\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12H\n\x07headers\x18\x02 \x03(\x0b2..textql.rpc.public.mcp.HttpConfig.HeadersEntryR\x07headers\x1a:\n\x0cHeadersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01"\xa2\x01\n\tSseConfig\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12G\n\x07headers\x18\x02 \x03(\x0b2-.textql.rpc.public.mcp.SseConfig.HeadersEntryR\x07headers\x1a:\n\x0cHeadersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01"\xdf\x03\n\tMCPServer\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12E\n\ttransport\x18\x03 \x01(\x0e2\'.textql.rpc.public.mcp.MCPTransportTypeR\ttransport\x12D\n\x0bhttp_config\x18\x04 \x01(\x0b2!.textql.rpc.public.mcp.HttpConfigH\x00R\nhttpConfig\x12A\n\nsse_config\x18\x05 \x01(\x0b2 .textql.rpc.public.mcp.SseConfigH\x00R\tsseConfig\x12\x1b\n\tmember_id\x18\x06 \x01(\tR\x08memberId\x12\'\n\x0forganization_id\x18\x07 \x01(\tR\x0eorganizationId\x129\n\ncreated_at\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt\x129\n\nupdated_at\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampR\tupdatedAt\x12\x18\n\x07enabled\x18\n \x01(\x08R\x07enabledB\x08\n\x06config"W\n\x07MCPTool\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0bdescription\x18\x02 \x01(\tR\x0bdescription\x12\x16\n\x06schema\x18\x03 \x01(\tR\x06schema"\xad\x02\n\x12MCPServerWithTools\x12?\n\nmcp_server\x18\x01 \x01(\x0b2 .textql.rpc.public.mcp.MCPServerR\tmcpServer\x124\n\x05tools\x18\x02 \x03(\x0b2\x1e.textql.rpc.public.mcp.MCPToolR\x05tools\x12:\n\x05error\x18\x03 \x01(\x0e2\x1f.textql.rpc.public.mcp.MCPErrorH\x00R\x05error\x88\x01\x01\x12Z\n\x12oauth_connected_at\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNALR\x10oauthConnectedAtB\x08\n\x06_error"\x16\n\x14GetMCPServersRequest"c\n\x15GetMCPServersResponse\x12J\n\x0bmcp_servers\x18\x01 \x03(\x0b2).textql.rpc.public.mcp.MCPServerWithToolsR\nmcpServers"\\\n\x17UpsertMCPServersRequest\x12A\n\x0bmcp_servers\x18\x01 \x03(\x0b2 .textql.rpc.public.mcp.MCPServerR\nmcpServers"f\n\x18UpsertMCPServersResponse\x12J\n\x0bmcp_servers\x18\x01 \x03(\x0b2).textql.rpc.public.mcp.MCPServerWithToolsR\nmcpServers"(\n\x16ToggleMCPServerRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"3\n\x17ToggleMCPServerResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success"5\n\x16ClearOAuthTokenRequest\x12\x1b\n\tserver_id\x18\x01 \x01(\tR\x08serverId"I\n\x17ClearOAuthTokenResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x14\n\x05error\x18\x02 \x01(\tR\x05error"(\n\x16DeleteMCPServerRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"I\n\x17DeleteMCPServerResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x14\n\x05error\x18\x02 \x01(\tR\x05error"7\n\x18InitiateOAuthFlowRequest\x12\x1b\n\tserver_id\x18\x01 \x01(\tR\x08serverId"x\n\x19InitiateOAuthFlowResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x14\n\x05error\x18\x02 \x01(\tR\x05error\x12+\n\x11authorization_url\x18\x03 \x01(\tR\x10authorizationUrl"c\n\x1aHandleOAuthCallbackRequest\x12\x1b\n\tserver_id\x18\x01 \x01(\tR\x08serverId\x12\x12\n\x04code\x18\x02 \x01(\tR\x04code\x12\x14\n\x05state\x18\x03 \x01(\tR\x05state"M\n\x1bHandleOAuthCallbackResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x14\n\x05error\x18\x02 \x01(\tR\x05error*I\n\x10MCPTransportType\x12"\n\x1eMCP_TRANSPORT_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03SSE\x10\x01\x12\x08\n\x04HTTP\x10\x02*\xa1\x02\n\x08MCPError\x12\x19\n\x15MCP_ERROR_UNSPECIFIED\x10\x00\x12\x1b\n\x17MCP_ERROR_INVALID_TOKEN\x10\x01\x12%\n!MCP_ERROR_AUTHENTICATION_REQUIRED\x10\x02\x12*\n&MCP_ERROR_UNSUPPORTED_PROTOCOL_VERSION\x10\x03\x12$\n MCP_ERROR_CLIENT_NOT_INITIALIZED\x10\x04\x12\x1a\n\x16MCP_ERROR_URL_REQUIRED\x10\x05\x12(\n$MCP_ERROR_UNSUPPORTED_TRANSPORT_TYPE\x10\x06\x12\x1e\n\x1aMCP_ERROR_SERVER_NOT_FOUND\x10\x072\xb9\x06\n\nMCPService\x12j\n\rGetMCPServers\x12+.textql.rpc.public.mcp.GetMCPServersRequest\x1a,.textql.rpc.public.mcp.GetMCPServersResponse\x12s\n\x10UpsertMCPServers\x12..textql.rpc.public.mcp.UpsertMCPServersRequest\x1a/.textql.rpc.public.mcp.UpsertMCPServersResponse\x12p\n\x0fDeleteMCPServer\x12-.textql.rpc.public.mcp.DeleteMCPServerRequest\x1a..textql.rpc.public.mcp.DeleteMCPServerResponse\x12p\n\x0fToggleMCPServer\x12-.textql.rpc.public.mcp.ToggleMCPServerRequest\x1a..textql.rpc.public.mcp.ToggleMCPServerResponse\x12p\n\x0fClearOAuthToken\x12-.textql.rpc.public.mcp.ClearOAuthTokenRequest\x1a..textql.rpc.public.mcp.ClearOAuthTokenResponse\x12v\n\x11InitiateOAuthFlow\x12/.textql.rpc.public.mcp.InitiateOAuthFlowRequest\x1a0.textql.rpc.public.mcp.InitiateOAuthFlowResponse\x12|\n\x13HandleOAuthCallback\x121.textql.rpc.public.mcp.HandleOAuthCallbackRequest\x1a2.textql.rpc.public.mcp.HandleOAuthCallbackResponseB;Z9github.com/textqllabs/demo2/compute/pkg/rpc/server/publicb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.mcp_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z9github.com/textqllabs/demo2/compute/pkg/rpc/server/public'
    _globals['_HTTPCONFIG_HEADERSENTRY']._loaded_options = None
    _globals['_HTTPCONFIG_HEADERSENTRY']._serialized_options = b'8\x01'
    _globals['_SSECONFIG_HEADERSENTRY']._loaded_options = None
    _globals['_SSECONFIG_HEADERSENTRY']._serialized_options = b'8\x01'
    _globals['_MCPSERVERWITHTOOLS'].fields_by_name['oauth_connected_at']._loaded_options = None
    _globals['_MCPSERVERWITHTOOLS'].fields_by_name['oauth_connected_at']._serialized_options = b'\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL'
    _globals['_MCPTRANSPORTTYPE']._serialized_start = 2336
    _globals['_MCPTRANSPORTTYPE']._serialized_end = 2409
    _globals['_MCPERROR']._serialized_start = 2412
    _globals['_MCPERROR']._serialized_end = 2701
    _globals['_HTTPCONFIG']._serialized_start = 106
    _globals['_HTTPCONFIG']._serialized_end = 270
    _globals['_HTTPCONFIG_HEADERSENTRY']._serialized_start = 212
    _globals['_HTTPCONFIG_HEADERSENTRY']._serialized_end = 270
    _globals['_SSECONFIG']._serialized_start = 273
    _globals['_SSECONFIG']._serialized_end = 435
    _globals['_SSECONFIG_HEADERSENTRY']._serialized_start = 212
    _globals['_SSECONFIG_HEADERSENTRY']._serialized_end = 270
    _globals['_MCPSERVER']._serialized_start = 438
    _globals['_MCPSERVER']._serialized_end = 917
    _globals['_MCPTOOL']._serialized_start = 919
    _globals['_MCPTOOL']._serialized_end = 1006
    _globals['_MCPSERVERWITHTOOLS']._serialized_start = 1009
    _globals['_MCPSERVERWITHTOOLS']._serialized_end = 1310
    _globals['_GETMCPSERVERSREQUEST']._serialized_start = 1312
    _globals['_GETMCPSERVERSREQUEST']._serialized_end = 1334
    _globals['_GETMCPSERVERSRESPONSE']._serialized_start = 1336
    _globals['_GETMCPSERVERSRESPONSE']._serialized_end = 1435
    _globals['_UPSERTMCPSERVERSREQUEST']._serialized_start = 1437
    _globals['_UPSERTMCPSERVERSREQUEST']._serialized_end = 1529
    _globals['_UPSERTMCPSERVERSRESPONSE']._serialized_start = 1531
    _globals['_UPSERTMCPSERVERSRESPONSE']._serialized_end = 1633
    _globals['_TOGGLEMCPSERVERREQUEST']._serialized_start = 1635
    _globals['_TOGGLEMCPSERVERREQUEST']._serialized_end = 1675
    _globals['_TOGGLEMCPSERVERRESPONSE']._serialized_start = 1677
    _globals['_TOGGLEMCPSERVERRESPONSE']._serialized_end = 1728
    _globals['_CLEAROAUTHTOKENREQUEST']._serialized_start = 1730
    _globals['_CLEAROAUTHTOKENREQUEST']._serialized_end = 1783
    _globals['_CLEAROAUTHTOKENRESPONSE']._serialized_start = 1785
    _globals['_CLEAROAUTHTOKENRESPONSE']._serialized_end = 1858
    _globals['_DELETEMCPSERVERREQUEST']._serialized_start = 1860
    _globals['_DELETEMCPSERVERREQUEST']._serialized_end = 1900
    _globals['_DELETEMCPSERVERRESPONSE']._serialized_start = 1902
    _globals['_DELETEMCPSERVERRESPONSE']._serialized_end = 1975
    _globals['_INITIATEOAUTHFLOWREQUEST']._serialized_start = 1977
    _globals['_INITIATEOAUTHFLOWREQUEST']._serialized_end = 2032
    _globals['_INITIATEOAUTHFLOWRESPONSE']._serialized_start = 2034
    _globals['_INITIATEOAUTHFLOWRESPONSE']._serialized_end = 2154
    _globals['_HANDLEOAUTHCALLBACKREQUEST']._serialized_start = 2156
    _globals['_HANDLEOAUTHCALLBACKREQUEST']._serialized_end = 2255
    _globals['_HANDLEOAUTHCALLBACKRESPONSE']._serialized_start = 2257
    _globals['_HANDLEOAUTHCALLBACKRESPONSE']._serialized_end = 2334
    _globals['_MCPSERVICE']._serialized_start = 2704
    _globals['_MCPSERVICE']._serialized_end = 3529