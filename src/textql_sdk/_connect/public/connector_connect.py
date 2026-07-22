from collections.abc import AsyncGenerator, AsyncIterator, Iterable, Iterator, Mapping
from typing import Protocol
from connectrpc.client import ConnectClient, ConnectClientSync
from connectrpc.code import Code
from connectrpc.compression import Compression
from connectrpc.errors import ConnectError
from connectrpc.interceptor import Interceptor, InterceptorSync
from connectrpc.method import IdempotencyLevel, MethodInfo
from connectrpc.request import Headers, RequestContext
from connectrpc.server import ConnectASGIApplication, ConnectWSGIApplication, Endpoint, EndpointSync
from . import connector_pb2 as public_dot_connector__pb2

class ConnectorService(Protocol):

    async def create_connector(self, request: public_dot_connector__pb2.CreateConnectorRequest, ctx: RequestContext) -> public_dot_connector__pb2.CreateConnectorResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_connector(self, request: public_dot_connector__pb2.UpdateConnectorRequest, ctx: RequestContext) -> public_dot_connector__pb2.UpdateConnectorResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_connector(self, request: public_dot_connector__pb2.GetConnectorRequest, ctx: RequestContext) -> public_dot_connector__pb2.GetConnectorResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_connectors(self, request: public_dot_connector__pb2.GetConnectorsRequest, ctx: RequestContext) -> public_dot_connector__pb2.GetConnectorsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_connector(self, request: public_dot_connector__pb2.DeleteConnectorRequest, ctx: RequestContext) -> public_dot_connector__pb2.DeleteConnectorResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def test_connector(self, request: public_dot_connector__pb2.TestConnectorRequest, ctx: RequestContext) -> public_dot_connector__pb2.TestConnectorResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def duplicate_connector(self, request: public_dot_connector__pb2.DuplicateConnectorRequest, ctx: RequestContext) -> public_dot_connector__pb2.DuplicateConnectorResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_connector_tables(self, request: public_dot_connector__pb2.ListConnectorTablesRequest, ctx: RequestContext) -> public_dot_connector__pb2.ListConnectorTablesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_table_preview(self, request: public_dot_connector__pb2.GetTablePreviewRequest, ctx: RequestContext) -> public_dot_connector__pb2.GetTablePreviewResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def execute_query(self, request: public_dot_connector__pb2.ExecuteQueryRequest, ctx: RequestContext) -> public_dot_connector__pb2.ExecuteQueryResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_example_queries(self, request: public_dot_connector__pb2.GetExampleQueriesRequest, ctx: RequestContext) -> public_dot_connector__pb2.GetExampleQueriesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_connector_stats(self, request: public_dot_connector__pb2.GetConnectorStatsRequest, ctx: RequestContext) -> public_dot_connector__pb2.GetConnectorStatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_query_templates(self, request: public_dot_connector__pb2.ListQueryTemplatesRequest, ctx: RequestContext) -> public_dot_connector__pb2.ListQueryTemplatesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_connector_usage(self, request: public_dot_connector__pb2.GetConnectorUsageRequest, ctx: RequestContext) -> public_dot_connector__pb2.GetConnectorUsageResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_connector_chats(self, request: public_dot_connector__pb2.GetConnectorChatsRequest, ctx: RequestContext) -> public_dot_connector__pb2.GetConnectorChatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_connector_cell_durations(self, request: public_dot_connector__pb2.GetConnectorCellDurationsRequest, ctx: RequestContext) -> public_dot_connector__pb2.GetConnectorCellDurationsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_connector_dashboards(self, request: public_dot_connector__pb2.GetConnectorDashboardsRequest, ctx: RequestContext) -> public_dot_connector__pb2.GetConnectorDashboardsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class ConnectorServiceASGIApplication(ConnectASGIApplication[ConnectorService]):

    def __init__(self, service: ConnectorService | AsyncGenerator[ConnectorService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.connector.ConnectorService/CreateConnector': Endpoint.unary(method=MethodInfo(name='CreateConnector', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.CreateConnectorRequest, output=public_dot_connector__pb2.CreateConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_connector), '/textql.rpc.public.connector.ConnectorService/UpdateConnector': Endpoint.unary(method=MethodInfo(name='UpdateConnector', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.UpdateConnectorRequest, output=public_dot_connector__pb2.UpdateConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_connector), '/textql.rpc.public.connector.ConnectorService/GetConnector': Endpoint.unary(method=MethodInfo(name='GetConnector', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorRequest, output=public_dot_connector__pb2.GetConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_connector), '/textql.rpc.public.connector.ConnectorService/GetConnectors': Endpoint.unary(method=MethodInfo(name='GetConnectors', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorsRequest, output=public_dot_connector__pb2.GetConnectorsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_connectors), '/textql.rpc.public.connector.ConnectorService/DeleteConnector': Endpoint.unary(method=MethodInfo(name='DeleteConnector', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.DeleteConnectorRequest, output=public_dot_connector__pb2.DeleteConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_connector), '/textql.rpc.public.connector.ConnectorService/TestConnector': Endpoint.unary(method=MethodInfo(name='TestConnector', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.TestConnectorRequest, output=public_dot_connector__pb2.TestConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.test_connector), '/textql.rpc.public.connector.ConnectorService/DuplicateConnector': Endpoint.unary(method=MethodInfo(name='DuplicateConnector', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.DuplicateConnectorRequest, output=public_dot_connector__pb2.DuplicateConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.duplicate_connector), '/textql.rpc.public.connector.ConnectorService/ListConnectorTables': Endpoint.unary(method=MethodInfo(name='ListConnectorTables', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.ListConnectorTablesRequest, output=public_dot_connector__pb2.ListConnectorTablesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_connector_tables), '/textql.rpc.public.connector.ConnectorService/GetTablePreview': Endpoint.unary(method=MethodInfo(name='GetTablePreview', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetTablePreviewRequest, output=public_dot_connector__pb2.GetTablePreviewResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_table_preview), '/textql.rpc.public.connector.ConnectorService/ExecuteQuery': Endpoint.unary(method=MethodInfo(name='ExecuteQuery', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.ExecuteQueryRequest, output=public_dot_connector__pb2.ExecuteQueryResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.execute_query), '/textql.rpc.public.connector.ConnectorService/GetExampleQueries': Endpoint.unary(method=MethodInfo(name='GetExampleQueries', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetExampleQueriesRequest, output=public_dot_connector__pb2.GetExampleQueriesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_example_queries), '/textql.rpc.public.connector.ConnectorService/GetConnectorStats': Endpoint.unary(method=MethodInfo(name='GetConnectorStats', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorStatsRequest, output=public_dot_connector__pb2.GetConnectorStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_connector_stats), '/textql.rpc.public.connector.ConnectorService/ListQueryTemplates': Endpoint.unary(method=MethodInfo(name='ListQueryTemplates', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.ListQueryTemplatesRequest, output=public_dot_connector__pb2.ListQueryTemplatesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_query_templates), '/textql.rpc.public.connector.ConnectorService/GetConnectorUsage': Endpoint.unary(method=MethodInfo(name='GetConnectorUsage', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorUsageRequest, output=public_dot_connector__pb2.GetConnectorUsageResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_connector_usage), '/textql.rpc.public.connector.ConnectorService/GetConnectorChats': Endpoint.unary(method=MethodInfo(name='GetConnectorChats', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorChatsRequest, output=public_dot_connector__pb2.GetConnectorChatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_connector_chats), '/textql.rpc.public.connector.ConnectorService/GetConnectorCellDurations': Endpoint.unary(method=MethodInfo(name='GetConnectorCellDurations', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorCellDurationsRequest, output=public_dot_connector__pb2.GetConnectorCellDurationsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_connector_cell_durations), '/textql.rpc.public.connector.ConnectorService/GetConnectorDashboards': Endpoint.unary(method=MethodInfo(name='GetConnectorDashboards', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorDashboardsRequest, output=public_dot_connector__pb2.GetConnectorDashboardsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_connector_dashboards)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.connector.ConnectorService'

class ConnectorServiceClient(ConnectClient):

    async def create_connector(self, request: public_dot_connector__pb2.CreateConnectorRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_connector__pb2.CreateConnectorResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateConnector', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.CreateConnectorRequest, output=public_dot_connector__pb2.CreateConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def update_connector(self, request: public_dot_connector__pb2.UpdateConnectorRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_connector__pb2.UpdateConnectorResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateConnector', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.UpdateConnectorRequest, output=public_dot_connector__pb2.UpdateConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_connector(self, request: public_dot_connector__pb2.GetConnectorRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_connector__pb2.GetConnectorResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetConnector', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorRequest, output=public_dot_connector__pb2.GetConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_connectors(self, request: public_dot_connector__pb2.GetConnectorsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_connector__pb2.GetConnectorsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetConnectors', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorsRequest, output=public_dot_connector__pb2.GetConnectorsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def delete_connector(self, request: public_dot_connector__pb2.DeleteConnectorRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_connector__pb2.DeleteConnectorResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteConnector', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.DeleteConnectorRequest, output=public_dot_connector__pb2.DeleteConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def test_connector(self, request: public_dot_connector__pb2.TestConnectorRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_connector__pb2.TestConnectorResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='TestConnector', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.TestConnectorRequest, output=public_dot_connector__pb2.TestConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def duplicate_connector(self, request: public_dot_connector__pb2.DuplicateConnectorRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_connector__pb2.DuplicateConnectorResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DuplicateConnector', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.DuplicateConnectorRequest, output=public_dot_connector__pb2.DuplicateConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_connector_tables(self, request: public_dot_connector__pb2.ListConnectorTablesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_connector__pb2.ListConnectorTablesResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListConnectorTables', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.ListConnectorTablesRequest, output=public_dot_connector__pb2.ListConnectorTablesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_table_preview(self, request: public_dot_connector__pb2.GetTablePreviewRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_connector__pb2.GetTablePreviewResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetTablePreview', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetTablePreviewRequest, output=public_dot_connector__pb2.GetTablePreviewResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def execute_query(self, request: public_dot_connector__pb2.ExecuteQueryRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_connector__pb2.ExecuteQueryResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ExecuteQuery', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.ExecuteQueryRequest, output=public_dot_connector__pb2.ExecuteQueryResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_example_queries(self, request: public_dot_connector__pb2.GetExampleQueriesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_connector__pb2.GetExampleQueriesResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetExampleQueries', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetExampleQueriesRequest, output=public_dot_connector__pb2.GetExampleQueriesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_connector_stats(self, request: public_dot_connector__pb2.GetConnectorStatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_connector__pb2.GetConnectorStatsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetConnectorStats', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorStatsRequest, output=public_dot_connector__pb2.GetConnectorStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def list_query_templates(self, request: public_dot_connector__pb2.ListQueryTemplatesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_connector__pb2.ListQueryTemplatesResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListQueryTemplates', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.ListQueryTemplatesRequest, output=public_dot_connector__pb2.ListQueryTemplatesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_connector_usage(self, request: public_dot_connector__pb2.GetConnectorUsageRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_connector__pb2.GetConnectorUsageResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetConnectorUsage', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorUsageRequest, output=public_dot_connector__pb2.GetConnectorUsageResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_connector_chats(self, request: public_dot_connector__pb2.GetConnectorChatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_connector__pb2.GetConnectorChatsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetConnectorChats', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorChatsRequest, output=public_dot_connector__pb2.GetConnectorChatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_connector_cell_durations(self, request: public_dot_connector__pb2.GetConnectorCellDurationsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_connector__pb2.GetConnectorCellDurationsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetConnectorCellDurations', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorCellDurationsRequest, output=public_dot_connector__pb2.GetConnectorCellDurationsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_connector_dashboards(self, request: public_dot_connector__pb2.GetConnectorDashboardsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_connector__pb2.GetConnectorDashboardsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetConnectorDashboards', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorDashboardsRequest, output=public_dot_connector__pb2.GetConnectorDashboardsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

class ConnectorServiceSync(Protocol):

    def create_connector(self, request: public_dot_connector__pb2.CreateConnectorRequest, ctx: RequestContext) -> public_dot_connector__pb2.CreateConnectorResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_connector(self, request: public_dot_connector__pb2.UpdateConnectorRequest, ctx: RequestContext) -> public_dot_connector__pb2.UpdateConnectorResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_connector(self, request: public_dot_connector__pb2.GetConnectorRequest, ctx: RequestContext) -> public_dot_connector__pb2.GetConnectorResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_connectors(self, request: public_dot_connector__pb2.GetConnectorsRequest, ctx: RequestContext) -> public_dot_connector__pb2.GetConnectorsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_connector(self, request: public_dot_connector__pb2.DeleteConnectorRequest, ctx: RequestContext) -> public_dot_connector__pb2.DeleteConnectorResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def test_connector(self, request: public_dot_connector__pb2.TestConnectorRequest, ctx: RequestContext) -> public_dot_connector__pb2.TestConnectorResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def duplicate_connector(self, request: public_dot_connector__pb2.DuplicateConnectorRequest, ctx: RequestContext) -> public_dot_connector__pb2.DuplicateConnectorResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_connector_tables(self, request: public_dot_connector__pb2.ListConnectorTablesRequest, ctx: RequestContext) -> public_dot_connector__pb2.ListConnectorTablesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_table_preview(self, request: public_dot_connector__pb2.GetTablePreviewRequest, ctx: RequestContext) -> public_dot_connector__pb2.GetTablePreviewResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def execute_query(self, request: public_dot_connector__pb2.ExecuteQueryRequest, ctx: RequestContext) -> public_dot_connector__pb2.ExecuteQueryResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_example_queries(self, request: public_dot_connector__pb2.GetExampleQueriesRequest, ctx: RequestContext) -> public_dot_connector__pb2.GetExampleQueriesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_connector_stats(self, request: public_dot_connector__pb2.GetConnectorStatsRequest, ctx: RequestContext) -> public_dot_connector__pb2.GetConnectorStatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_query_templates(self, request: public_dot_connector__pb2.ListQueryTemplatesRequest, ctx: RequestContext) -> public_dot_connector__pb2.ListQueryTemplatesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_connector_usage(self, request: public_dot_connector__pb2.GetConnectorUsageRequest, ctx: RequestContext) -> public_dot_connector__pb2.GetConnectorUsageResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_connector_chats(self, request: public_dot_connector__pb2.GetConnectorChatsRequest, ctx: RequestContext) -> public_dot_connector__pb2.GetConnectorChatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_connector_cell_durations(self, request: public_dot_connector__pb2.GetConnectorCellDurationsRequest, ctx: RequestContext) -> public_dot_connector__pb2.GetConnectorCellDurationsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_connector_dashboards(self, request: public_dot_connector__pb2.GetConnectorDashboardsRequest, ctx: RequestContext) -> public_dot_connector__pb2.GetConnectorDashboardsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class ConnectorServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: ConnectorServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.connector.ConnectorService/CreateConnector': EndpointSync.unary(method=MethodInfo(name='CreateConnector', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.CreateConnectorRequest, output=public_dot_connector__pb2.CreateConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_connector), '/textql.rpc.public.connector.ConnectorService/UpdateConnector': EndpointSync.unary(method=MethodInfo(name='UpdateConnector', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.UpdateConnectorRequest, output=public_dot_connector__pb2.UpdateConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_connector), '/textql.rpc.public.connector.ConnectorService/GetConnector': EndpointSync.unary(method=MethodInfo(name='GetConnector', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorRequest, output=public_dot_connector__pb2.GetConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_connector), '/textql.rpc.public.connector.ConnectorService/GetConnectors': EndpointSync.unary(method=MethodInfo(name='GetConnectors', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorsRequest, output=public_dot_connector__pb2.GetConnectorsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_connectors), '/textql.rpc.public.connector.ConnectorService/DeleteConnector': EndpointSync.unary(method=MethodInfo(name='DeleteConnector', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.DeleteConnectorRequest, output=public_dot_connector__pb2.DeleteConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_connector), '/textql.rpc.public.connector.ConnectorService/TestConnector': EndpointSync.unary(method=MethodInfo(name='TestConnector', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.TestConnectorRequest, output=public_dot_connector__pb2.TestConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.test_connector), '/textql.rpc.public.connector.ConnectorService/DuplicateConnector': EndpointSync.unary(method=MethodInfo(name='DuplicateConnector', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.DuplicateConnectorRequest, output=public_dot_connector__pb2.DuplicateConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.duplicate_connector), '/textql.rpc.public.connector.ConnectorService/ListConnectorTables': EndpointSync.unary(method=MethodInfo(name='ListConnectorTables', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.ListConnectorTablesRequest, output=public_dot_connector__pb2.ListConnectorTablesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_connector_tables), '/textql.rpc.public.connector.ConnectorService/GetTablePreview': EndpointSync.unary(method=MethodInfo(name='GetTablePreview', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetTablePreviewRequest, output=public_dot_connector__pb2.GetTablePreviewResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_table_preview), '/textql.rpc.public.connector.ConnectorService/ExecuteQuery': EndpointSync.unary(method=MethodInfo(name='ExecuteQuery', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.ExecuteQueryRequest, output=public_dot_connector__pb2.ExecuteQueryResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.execute_query), '/textql.rpc.public.connector.ConnectorService/GetExampleQueries': EndpointSync.unary(method=MethodInfo(name='GetExampleQueries', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetExampleQueriesRequest, output=public_dot_connector__pb2.GetExampleQueriesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_example_queries), '/textql.rpc.public.connector.ConnectorService/GetConnectorStats': EndpointSync.unary(method=MethodInfo(name='GetConnectorStats', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorStatsRequest, output=public_dot_connector__pb2.GetConnectorStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_connector_stats), '/textql.rpc.public.connector.ConnectorService/ListQueryTemplates': EndpointSync.unary(method=MethodInfo(name='ListQueryTemplates', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.ListQueryTemplatesRequest, output=public_dot_connector__pb2.ListQueryTemplatesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_query_templates), '/textql.rpc.public.connector.ConnectorService/GetConnectorUsage': EndpointSync.unary(method=MethodInfo(name='GetConnectorUsage', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorUsageRequest, output=public_dot_connector__pb2.GetConnectorUsageResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_connector_usage), '/textql.rpc.public.connector.ConnectorService/GetConnectorChats': EndpointSync.unary(method=MethodInfo(name='GetConnectorChats', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorChatsRequest, output=public_dot_connector__pb2.GetConnectorChatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_connector_chats), '/textql.rpc.public.connector.ConnectorService/GetConnectorCellDurations': EndpointSync.unary(method=MethodInfo(name='GetConnectorCellDurations', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorCellDurationsRequest, output=public_dot_connector__pb2.GetConnectorCellDurationsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_connector_cell_durations), '/textql.rpc.public.connector.ConnectorService/GetConnectorDashboards': EndpointSync.unary(method=MethodInfo(name='GetConnectorDashboards', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorDashboardsRequest, output=public_dot_connector__pb2.GetConnectorDashboardsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_connector_dashboards)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.connector.ConnectorService'

class ConnectorServiceClientSync(ConnectClientSync):

    def create_connector(self, request: public_dot_connector__pb2.CreateConnectorRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_connector__pb2.CreateConnectorResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateConnector', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.CreateConnectorRequest, output=public_dot_connector__pb2.CreateConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def update_connector(self, request: public_dot_connector__pb2.UpdateConnectorRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_connector__pb2.UpdateConnectorResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateConnector', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.UpdateConnectorRequest, output=public_dot_connector__pb2.UpdateConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_connector(self, request: public_dot_connector__pb2.GetConnectorRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_connector__pb2.GetConnectorResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetConnector', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorRequest, output=public_dot_connector__pb2.GetConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_connectors(self, request: public_dot_connector__pb2.GetConnectorsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_connector__pb2.GetConnectorsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetConnectors', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorsRequest, output=public_dot_connector__pb2.GetConnectorsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def delete_connector(self, request: public_dot_connector__pb2.DeleteConnectorRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_connector__pb2.DeleteConnectorResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteConnector', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.DeleteConnectorRequest, output=public_dot_connector__pb2.DeleteConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def test_connector(self, request: public_dot_connector__pb2.TestConnectorRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_connector__pb2.TestConnectorResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='TestConnector', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.TestConnectorRequest, output=public_dot_connector__pb2.TestConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def duplicate_connector(self, request: public_dot_connector__pb2.DuplicateConnectorRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_connector__pb2.DuplicateConnectorResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DuplicateConnector', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.DuplicateConnectorRequest, output=public_dot_connector__pb2.DuplicateConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_connector_tables(self, request: public_dot_connector__pb2.ListConnectorTablesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_connector__pb2.ListConnectorTablesResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListConnectorTables', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.ListConnectorTablesRequest, output=public_dot_connector__pb2.ListConnectorTablesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_table_preview(self, request: public_dot_connector__pb2.GetTablePreviewRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_connector__pb2.GetTablePreviewResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetTablePreview', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetTablePreviewRequest, output=public_dot_connector__pb2.GetTablePreviewResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def execute_query(self, request: public_dot_connector__pb2.ExecuteQueryRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_connector__pb2.ExecuteQueryResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ExecuteQuery', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.ExecuteQueryRequest, output=public_dot_connector__pb2.ExecuteQueryResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_example_queries(self, request: public_dot_connector__pb2.GetExampleQueriesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_connector__pb2.GetExampleQueriesResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetExampleQueries', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetExampleQueriesRequest, output=public_dot_connector__pb2.GetExampleQueriesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_connector_stats(self, request: public_dot_connector__pb2.GetConnectorStatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_connector__pb2.GetConnectorStatsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetConnectorStats', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorStatsRequest, output=public_dot_connector__pb2.GetConnectorStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def list_query_templates(self, request: public_dot_connector__pb2.ListQueryTemplatesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_connector__pb2.ListQueryTemplatesResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListQueryTemplates', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.ListQueryTemplatesRequest, output=public_dot_connector__pb2.ListQueryTemplatesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_connector_usage(self, request: public_dot_connector__pb2.GetConnectorUsageRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_connector__pb2.GetConnectorUsageResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetConnectorUsage', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorUsageRequest, output=public_dot_connector__pb2.GetConnectorUsageResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_connector_chats(self, request: public_dot_connector__pb2.GetConnectorChatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_connector__pb2.GetConnectorChatsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetConnectorChats', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorChatsRequest, output=public_dot_connector__pb2.GetConnectorChatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_connector_cell_durations(self, request: public_dot_connector__pb2.GetConnectorCellDurationsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_connector__pb2.GetConnectorCellDurationsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetConnectorCellDurations', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorCellDurationsRequest, output=public_dot_connector__pb2.GetConnectorCellDurationsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_connector_dashboards(self, request: public_dot_connector__pb2.GetConnectorDashboardsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_connector__pb2.GetConnectorDashboardsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetConnectorDashboards', service_name='textql.rpc.public.connector.ConnectorService', input=public_dot_connector__pb2.GetConnectorDashboardsRequest, output=public_dot_connector__pb2.GetConnectorDashboardsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)