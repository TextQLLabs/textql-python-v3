# pylint: skip-file
# mypy: ignore-errors
# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
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
from . import tableau_pb2 as public_dot_tableau__pb2

class TableauService(Protocol):

    async def test_tableau_connection(self, request: public_dot_tableau__pb2.TestTableauConnectionRequest, ctx: RequestContext) -> public_dot_tableau__pb2.TestTableauConnectionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_tableau_projects(self, request: public_dot_tableau__pb2.ListTableauProjectsRequest, ctx: RequestContext) -> public_dot_tableau__pb2.ListTableauProjectsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_tableau_workbooks(self, request: public_dot_tableau__pb2.ListTableauWorkbooksRequest, ctx: RequestContext) -> public_dot_tableau__pb2.ListTableauWorkbooksResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_tableau_views(self, request: public_dot_tableau__pb2.ListTableauViewsRequest, ctx: RequestContext) -> public_dot_tableau__pb2.ListTableauViewsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_tableau_datasources(self, request: public_dot_tableau__pb2.ListTableauDatasourcesRequest, ctx: RequestContext) -> public_dot_tableau__pb2.ListTableauDatasourcesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def star_tableau_item(self, request: public_dot_tableau__pb2.StarTableauItemRequest, ctx: RequestContext) -> public_dot_tableau__pb2.StarTableauItemResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def unstar_tableau_item(self, request: public_dot_tableau__pb2.UnstarTableauItemRequest, ctx: RequestContext) -> public_dot_tableau__pb2.UnstarTableauItemResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_starred_tableau_items(self, request: public_dot_tableau__pb2.GetStarredTableauItemsRequest, ctx: RequestContext) -> public_dot_tableau__pb2.GetStarredTableauItemsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_collection_thumbnail(self, request: public_dot_tableau__pb2.GetCollectionThumbnailRequest, ctx: RequestContext) -> public_dot_tableau__pb2.GetCollectionThumbnailResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def generate_embed_token(self, request: public_dot_tableau__pb2.GenerateEmbedTokenRequest, ctx: RequestContext) -> public_dot_tableau__pb2.GenerateEmbedTokenResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_connected_app_status(self, request: public_dot_tableau__pb2.GetConnectedAppStatusRequest, ctx: RequestContext) -> public_dot_tableau__pb2.GetConnectedAppStatusResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def reset_connected_app(self, request: public_dot_tableau__pb2.ResetConnectedAppRequest, ctx: RequestContext) -> public_dot_tableau__pb2.ResetConnectedAppResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def refresh_tableau_collection(self, request: public_dot_tableau__pb2.RefreshTableauCollectionRequest, ctx: RequestContext) -> public_dot_tableau__pb2.RefreshTableauCollectionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class TableauServiceASGIApplication(ConnectASGIApplication[TableauService]):

    def __init__(self, service: TableauService | AsyncGenerator[TableauService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.tableau.TableauService/TestTableauConnection': Endpoint.unary(method=MethodInfo(name='TestTableauConnection', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.TestTableauConnectionRequest, output=public_dot_tableau__pb2.TestTableauConnectionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.test_tableau_connection), '/textql.rpc.public.tableau.TableauService/ListTableauProjects': Endpoint.unary(method=MethodInfo(name='ListTableauProjects', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.ListTableauProjectsRequest, output=public_dot_tableau__pb2.ListTableauProjectsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_tableau_projects), '/textql.rpc.public.tableau.TableauService/ListTableauWorkbooks': Endpoint.unary(method=MethodInfo(name='ListTableauWorkbooks', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.ListTableauWorkbooksRequest, output=public_dot_tableau__pb2.ListTableauWorkbooksResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_tableau_workbooks), '/textql.rpc.public.tableau.TableauService/ListTableauViews': Endpoint.unary(method=MethodInfo(name='ListTableauViews', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.ListTableauViewsRequest, output=public_dot_tableau__pb2.ListTableauViewsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_tableau_views), '/textql.rpc.public.tableau.TableauService/ListTableauDatasources': Endpoint.unary(method=MethodInfo(name='ListTableauDatasources', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.ListTableauDatasourcesRequest, output=public_dot_tableau__pb2.ListTableauDatasourcesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_tableau_datasources), '/textql.rpc.public.tableau.TableauService/StarTableauItem': Endpoint.unary(method=MethodInfo(name='StarTableauItem', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.StarTableauItemRequest, output=public_dot_tableau__pb2.StarTableauItemResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.star_tableau_item), '/textql.rpc.public.tableau.TableauService/UnstarTableauItem': Endpoint.unary(method=MethodInfo(name='UnstarTableauItem', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.UnstarTableauItemRequest, output=public_dot_tableau__pb2.UnstarTableauItemResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.unstar_tableau_item), '/textql.rpc.public.tableau.TableauService/GetStarredTableauItems': Endpoint.unary(method=MethodInfo(name='GetStarredTableauItems', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.GetStarredTableauItemsRequest, output=public_dot_tableau__pb2.GetStarredTableauItemsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_starred_tableau_items), '/textql.rpc.public.tableau.TableauService/GetCollectionThumbnail': Endpoint.unary(method=MethodInfo(name='GetCollectionThumbnail', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.GetCollectionThumbnailRequest, output=public_dot_tableau__pb2.GetCollectionThumbnailResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_collection_thumbnail), '/textql.rpc.public.tableau.TableauService/GenerateEmbedToken': Endpoint.unary(method=MethodInfo(name='GenerateEmbedToken', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.GenerateEmbedTokenRequest, output=public_dot_tableau__pb2.GenerateEmbedTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.generate_embed_token), '/textql.rpc.public.tableau.TableauService/GetConnectedAppStatus': Endpoint.unary(method=MethodInfo(name='GetConnectedAppStatus', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.GetConnectedAppStatusRequest, output=public_dot_tableau__pb2.GetConnectedAppStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_connected_app_status), '/textql.rpc.public.tableau.TableauService/ResetConnectedApp': Endpoint.unary(method=MethodInfo(name='ResetConnectedApp', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.ResetConnectedAppRequest, output=public_dot_tableau__pb2.ResetConnectedAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.reset_connected_app), '/textql.rpc.public.tableau.TableauService/RefreshTableauCollection': Endpoint.unary(method=MethodInfo(name='RefreshTableauCollection', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.RefreshTableauCollectionRequest, output=public_dot_tableau__pb2.RefreshTableauCollectionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.refresh_tableau_collection)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.tableau.TableauService'

class TableauServiceClient(ConnectClient):

    async def test_tableau_connection(self, request: public_dot_tableau__pb2.TestTableauConnectionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_tableau__pb2.TestTableauConnectionResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='TestTableauConnection', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.TestTableauConnectionRequest, output=public_dot_tableau__pb2.TestTableauConnectionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_tableau_projects(self, request: public_dot_tableau__pb2.ListTableauProjectsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_tableau__pb2.ListTableauProjectsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListTableauProjects', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.ListTableauProjectsRequest, output=public_dot_tableau__pb2.ListTableauProjectsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_tableau_workbooks(self, request: public_dot_tableau__pb2.ListTableauWorkbooksRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_tableau__pb2.ListTableauWorkbooksResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListTableauWorkbooks', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.ListTableauWorkbooksRequest, output=public_dot_tableau__pb2.ListTableauWorkbooksResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_tableau_views(self, request: public_dot_tableau__pb2.ListTableauViewsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_tableau__pb2.ListTableauViewsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListTableauViews', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.ListTableauViewsRequest, output=public_dot_tableau__pb2.ListTableauViewsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_tableau_datasources(self, request: public_dot_tableau__pb2.ListTableauDatasourcesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_tableau__pb2.ListTableauDatasourcesResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListTableauDatasources', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.ListTableauDatasourcesRequest, output=public_dot_tableau__pb2.ListTableauDatasourcesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def star_tableau_item(self, request: public_dot_tableau__pb2.StarTableauItemRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_tableau__pb2.StarTableauItemResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='StarTableauItem', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.StarTableauItemRequest, output=public_dot_tableau__pb2.StarTableauItemResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def unstar_tableau_item(self, request: public_dot_tableau__pb2.UnstarTableauItemRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_tableau__pb2.UnstarTableauItemResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UnstarTableauItem', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.UnstarTableauItemRequest, output=public_dot_tableau__pb2.UnstarTableauItemResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_starred_tableau_items(self, request: public_dot_tableau__pb2.GetStarredTableauItemsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_tableau__pb2.GetStarredTableauItemsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetStarredTableauItems', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.GetStarredTableauItemsRequest, output=public_dot_tableau__pb2.GetStarredTableauItemsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_collection_thumbnail(self, request: public_dot_tableau__pb2.GetCollectionThumbnailRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_tableau__pb2.GetCollectionThumbnailResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetCollectionThumbnail', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.GetCollectionThumbnailRequest, output=public_dot_tableau__pb2.GetCollectionThumbnailResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def generate_embed_token(self, request: public_dot_tableau__pb2.GenerateEmbedTokenRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_tableau__pb2.GenerateEmbedTokenResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GenerateEmbedToken', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.GenerateEmbedTokenRequest, output=public_dot_tableau__pb2.GenerateEmbedTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_connected_app_status(self, request: public_dot_tableau__pb2.GetConnectedAppStatusRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_tableau__pb2.GetConnectedAppStatusResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetConnectedAppStatus', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.GetConnectedAppStatusRequest, output=public_dot_tableau__pb2.GetConnectedAppStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def reset_connected_app(self, request: public_dot_tableau__pb2.ResetConnectedAppRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_tableau__pb2.ResetConnectedAppResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ResetConnectedApp', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.ResetConnectedAppRequest, output=public_dot_tableau__pb2.ResetConnectedAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def refresh_tableau_collection(self, request: public_dot_tableau__pb2.RefreshTableauCollectionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_tableau__pb2.RefreshTableauCollectionResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RefreshTableauCollection', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.RefreshTableauCollectionRequest, output=public_dot_tableau__pb2.RefreshTableauCollectionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class TableauServiceSync(Protocol):

    def test_tableau_connection(self, request: public_dot_tableau__pb2.TestTableauConnectionRequest, ctx: RequestContext) -> public_dot_tableau__pb2.TestTableauConnectionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_tableau_projects(self, request: public_dot_tableau__pb2.ListTableauProjectsRequest, ctx: RequestContext) -> public_dot_tableau__pb2.ListTableauProjectsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_tableau_workbooks(self, request: public_dot_tableau__pb2.ListTableauWorkbooksRequest, ctx: RequestContext) -> public_dot_tableau__pb2.ListTableauWorkbooksResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_tableau_views(self, request: public_dot_tableau__pb2.ListTableauViewsRequest, ctx: RequestContext) -> public_dot_tableau__pb2.ListTableauViewsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_tableau_datasources(self, request: public_dot_tableau__pb2.ListTableauDatasourcesRequest, ctx: RequestContext) -> public_dot_tableau__pb2.ListTableauDatasourcesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def star_tableau_item(self, request: public_dot_tableau__pb2.StarTableauItemRequest, ctx: RequestContext) -> public_dot_tableau__pb2.StarTableauItemResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def unstar_tableau_item(self, request: public_dot_tableau__pb2.UnstarTableauItemRequest, ctx: RequestContext) -> public_dot_tableau__pb2.UnstarTableauItemResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_starred_tableau_items(self, request: public_dot_tableau__pb2.GetStarredTableauItemsRequest, ctx: RequestContext) -> public_dot_tableau__pb2.GetStarredTableauItemsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_collection_thumbnail(self, request: public_dot_tableau__pb2.GetCollectionThumbnailRequest, ctx: RequestContext) -> public_dot_tableau__pb2.GetCollectionThumbnailResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def generate_embed_token(self, request: public_dot_tableau__pb2.GenerateEmbedTokenRequest, ctx: RequestContext) -> public_dot_tableau__pb2.GenerateEmbedTokenResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_connected_app_status(self, request: public_dot_tableau__pb2.GetConnectedAppStatusRequest, ctx: RequestContext) -> public_dot_tableau__pb2.GetConnectedAppStatusResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def reset_connected_app(self, request: public_dot_tableau__pb2.ResetConnectedAppRequest, ctx: RequestContext) -> public_dot_tableau__pb2.ResetConnectedAppResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def refresh_tableau_collection(self, request: public_dot_tableau__pb2.RefreshTableauCollectionRequest, ctx: RequestContext) -> public_dot_tableau__pb2.RefreshTableauCollectionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class TableauServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: TableauServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.tableau.TableauService/TestTableauConnection': EndpointSync.unary(method=MethodInfo(name='TestTableauConnection', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.TestTableauConnectionRequest, output=public_dot_tableau__pb2.TestTableauConnectionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.test_tableau_connection), '/textql.rpc.public.tableau.TableauService/ListTableauProjects': EndpointSync.unary(method=MethodInfo(name='ListTableauProjects', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.ListTableauProjectsRequest, output=public_dot_tableau__pb2.ListTableauProjectsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_tableau_projects), '/textql.rpc.public.tableau.TableauService/ListTableauWorkbooks': EndpointSync.unary(method=MethodInfo(name='ListTableauWorkbooks', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.ListTableauWorkbooksRequest, output=public_dot_tableau__pb2.ListTableauWorkbooksResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_tableau_workbooks), '/textql.rpc.public.tableau.TableauService/ListTableauViews': EndpointSync.unary(method=MethodInfo(name='ListTableauViews', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.ListTableauViewsRequest, output=public_dot_tableau__pb2.ListTableauViewsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_tableau_views), '/textql.rpc.public.tableau.TableauService/ListTableauDatasources': EndpointSync.unary(method=MethodInfo(name='ListTableauDatasources', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.ListTableauDatasourcesRequest, output=public_dot_tableau__pb2.ListTableauDatasourcesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_tableau_datasources), '/textql.rpc.public.tableau.TableauService/StarTableauItem': EndpointSync.unary(method=MethodInfo(name='StarTableauItem', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.StarTableauItemRequest, output=public_dot_tableau__pb2.StarTableauItemResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.star_tableau_item), '/textql.rpc.public.tableau.TableauService/UnstarTableauItem': EndpointSync.unary(method=MethodInfo(name='UnstarTableauItem', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.UnstarTableauItemRequest, output=public_dot_tableau__pb2.UnstarTableauItemResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.unstar_tableau_item), '/textql.rpc.public.tableau.TableauService/GetStarredTableauItems': EndpointSync.unary(method=MethodInfo(name='GetStarredTableauItems', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.GetStarredTableauItemsRequest, output=public_dot_tableau__pb2.GetStarredTableauItemsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_starred_tableau_items), '/textql.rpc.public.tableau.TableauService/GetCollectionThumbnail': EndpointSync.unary(method=MethodInfo(name='GetCollectionThumbnail', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.GetCollectionThumbnailRequest, output=public_dot_tableau__pb2.GetCollectionThumbnailResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_collection_thumbnail), '/textql.rpc.public.tableau.TableauService/GenerateEmbedToken': EndpointSync.unary(method=MethodInfo(name='GenerateEmbedToken', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.GenerateEmbedTokenRequest, output=public_dot_tableau__pb2.GenerateEmbedTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.generate_embed_token), '/textql.rpc.public.tableau.TableauService/GetConnectedAppStatus': EndpointSync.unary(method=MethodInfo(name='GetConnectedAppStatus', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.GetConnectedAppStatusRequest, output=public_dot_tableau__pb2.GetConnectedAppStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_connected_app_status), '/textql.rpc.public.tableau.TableauService/ResetConnectedApp': EndpointSync.unary(method=MethodInfo(name='ResetConnectedApp', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.ResetConnectedAppRequest, output=public_dot_tableau__pb2.ResetConnectedAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.reset_connected_app), '/textql.rpc.public.tableau.TableauService/RefreshTableauCollection': EndpointSync.unary(method=MethodInfo(name='RefreshTableauCollection', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.RefreshTableauCollectionRequest, output=public_dot_tableau__pb2.RefreshTableauCollectionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.refresh_tableau_collection)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.tableau.TableauService'

class TableauServiceClientSync(ConnectClientSync):

    def test_tableau_connection(self, request: public_dot_tableau__pb2.TestTableauConnectionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_tableau__pb2.TestTableauConnectionResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='TestTableauConnection', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.TestTableauConnectionRequest, output=public_dot_tableau__pb2.TestTableauConnectionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_tableau_projects(self, request: public_dot_tableau__pb2.ListTableauProjectsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_tableau__pb2.ListTableauProjectsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListTableauProjects', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.ListTableauProjectsRequest, output=public_dot_tableau__pb2.ListTableauProjectsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_tableau_workbooks(self, request: public_dot_tableau__pb2.ListTableauWorkbooksRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_tableau__pb2.ListTableauWorkbooksResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListTableauWorkbooks', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.ListTableauWorkbooksRequest, output=public_dot_tableau__pb2.ListTableauWorkbooksResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_tableau_views(self, request: public_dot_tableau__pb2.ListTableauViewsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_tableau__pb2.ListTableauViewsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListTableauViews', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.ListTableauViewsRequest, output=public_dot_tableau__pb2.ListTableauViewsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_tableau_datasources(self, request: public_dot_tableau__pb2.ListTableauDatasourcesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_tableau__pb2.ListTableauDatasourcesResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListTableauDatasources', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.ListTableauDatasourcesRequest, output=public_dot_tableau__pb2.ListTableauDatasourcesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def star_tableau_item(self, request: public_dot_tableau__pb2.StarTableauItemRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_tableau__pb2.StarTableauItemResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='StarTableauItem', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.StarTableauItemRequest, output=public_dot_tableau__pb2.StarTableauItemResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def unstar_tableau_item(self, request: public_dot_tableau__pb2.UnstarTableauItemRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_tableau__pb2.UnstarTableauItemResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UnstarTableauItem', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.UnstarTableauItemRequest, output=public_dot_tableau__pb2.UnstarTableauItemResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_starred_tableau_items(self, request: public_dot_tableau__pb2.GetStarredTableauItemsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_tableau__pb2.GetStarredTableauItemsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetStarredTableauItems', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.GetStarredTableauItemsRequest, output=public_dot_tableau__pb2.GetStarredTableauItemsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_collection_thumbnail(self, request: public_dot_tableau__pb2.GetCollectionThumbnailRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_tableau__pb2.GetCollectionThumbnailResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetCollectionThumbnail', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.GetCollectionThumbnailRequest, output=public_dot_tableau__pb2.GetCollectionThumbnailResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def generate_embed_token(self, request: public_dot_tableau__pb2.GenerateEmbedTokenRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_tableau__pb2.GenerateEmbedTokenResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GenerateEmbedToken', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.GenerateEmbedTokenRequest, output=public_dot_tableau__pb2.GenerateEmbedTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_connected_app_status(self, request: public_dot_tableau__pb2.GetConnectedAppStatusRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_tableau__pb2.GetConnectedAppStatusResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetConnectedAppStatus', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.GetConnectedAppStatusRequest, output=public_dot_tableau__pb2.GetConnectedAppStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def reset_connected_app(self, request: public_dot_tableau__pb2.ResetConnectedAppRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_tableau__pb2.ResetConnectedAppResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ResetConnectedApp', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.ResetConnectedAppRequest, output=public_dot_tableau__pb2.ResetConnectedAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def refresh_tableau_collection(self, request: public_dot_tableau__pb2.RefreshTableauCollectionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_tableau__pb2.RefreshTableauCollectionResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RefreshTableauCollection', service_name='textql.rpc.public.tableau.TableauService', input=public_dot_tableau__pb2.RefreshTableauCollectionRequest, output=public_dot_tableau__pb2.RefreshTableauCollectionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)