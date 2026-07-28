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
from . import powerbi_pb2 as public_dot_powerbi__pb2

class PowerBIService(Protocol):

    async def test_power_b_i_connection(self, request: public_dot_powerbi__pb2.TestPowerBIConnectionRequest, ctx: RequestContext) -> public_dot_powerbi__pb2.TestPowerBIConnectionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_power_b_i_workspaces(self, request: public_dot_powerbi__pb2.ListPowerBIWorkspacesRequest, ctx: RequestContext) -> public_dot_powerbi__pb2.ListPowerBIWorkspacesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_power_b_i_datasets(self, request: public_dot_powerbi__pb2.ListPowerBIDatasetsRequest, ctx: RequestContext) -> public_dot_powerbi__pb2.ListPowerBIDatasetsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_power_b_i_reports(self, request: public_dot_powerbi__pb2.ListPowerBIReportsRequest, ctx: RequestContext) -> public_dot_powerbi__pb2.ListPowerBIReportsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def export_power_b_i_report_image(self, request: public_dot_powerbi__pb2.ExportPowerBIReportImageRequest, ctx: RequestContext) -> public_dot_powerbi__pb2.ExportPowerBIReportImageResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def generate_power_b_i_embed_token(self, request: public_dot_powerbi__pb2.GeneratePowerBIEmbedTokenRequest, ctx: RequestContext) -> public_dot_powerbi__pb2.GeneratePowerBIEmbedTokenResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def sync_power_b_i_items(self, request: public_dot_powerbi__pb2.SyncPowerBIItemsRequest, ctx: RequestContext) -> public_dot_powerbi__pb2.SyncPowerBIItemsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def unsync_power_b_i_items(self, request: public_dot_powerbi__pb2.UnsyncPowerBIItemsRequest, ctx: RequestContext) -> public_dot_powerbi__pb2.UnsyncPowerBIItemsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_synced_power_b_i_items(self, request: public_dot_powerbi__pb2.GetSyncedPowerBIItemsRequest, ctx: RequestContext) -> public_dot_powerbi__pb2.GetSyncedPowerBIItemsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_power_b_i_dataset_preview(self, request: public_dot_powerbi__pb2.GetPowerBIDatasetPreviewRequest, ctx: RequestContext) -> public_dot_powerbi__pb2.GetPowerBIDatasetPreviewResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class PowerBIServiceASGIApplication(ConnectASGIApplication[PowerBIService]):

    def __init__(self, service: PowerBIService | AsyncGenerator[PowerBIService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.powerbi.PowerBIService/TestPowerBIConnection': Endpoint.unary(method=MethodInfo(name='TestPowerBIConnection', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.TestPowerBIConnectionRequest, output=public_dot_powerbi__pb2.TestPowerBIConnectionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.test_power_b_i_connection), '/textql.rpc.public.powerbi.PowerBIService/ListPowerBIWorkspaces': Endpoint.unary(method=MethodInfo(name='ListPowerBIWorkspaces', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.ListPowerBIWorkspacesRequest, output=public_dot_powerbi__pb2.ListPowerBIWorkspacesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_power_b_i_workspaces), '/textql.rpc.public.powerbi.PowerBIService/ListPowerBIDatasets': Endpoint.unary(method=MethodInfo(name='ListPowerBIDatasets', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.ListPowerBIDatasetsRequest, output=public_dot_powerbi__pb2.ListPowerBIDatasetsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_power_b_i_datasets), '/textql.rpc.public.powerbi.PowerBIService/ListPowerBIReports': Endpoint.unary(method=MethodInfo(name='ListPowerBIReports', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.ListPowerBIReportsRequest, output=public_dot_powerbi__pb2.ListPowerBIReportsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_power_b_i_reports), '/textql.rpc.public.powerbi.PowerBIService/ExportPowerBIReportImage': Endpoint.unary(method=MethodInfo(name='ExportPowerBIReportImage', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.ExportPowerBIReportImageRequest, output=public_dot_powerbi__pb2.ExportPowerBIReportImageResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.export_power_b_i_report_image), '/textql.rpc.public.powerbi.PowerBIService/GeneratePowerBIEmbedToken': Endpoint.unary(method=MethodInfo(name='GeneratePowerBIEmbedToken', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.GeneratePowerBIEmbedTokenRequest, output=public_dot_powerbi__pb2.GeneratePowerBIEmbedTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.generate_power_b_i_embed_token), '/textql.rpc.public.powerbi.PowerBIService/SyncPowerBIItems': Endpoint.unary(method=MethodInfo(name='SyncPowerBIItems', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.SyncPowerBIItemsRequest, output=public_dot_powerbi__pb2.SyncPowerBIItemsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.sync_power_b_i_items), '/textql.rpc.public.powerbi.PowerBIService/UnsyncPowerBIItems': Endpoint.unary(method=MethodInfo(name='UnsyncPowerBIItems', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.UnsyncPowerBIItemsRequest, output=public_dot_powerbi__pb2.UnsyncPowerBIItemsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.unsync_power_b_i_items), '/textql.rpc.public.powerbi.PowerBIService/GetSyncedPowerBIItems': Endpoint.unary(method=MethodInfo(name='GetSyncedPowerBIItems', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.GetSyncedPowerBIItemsRequest, output=public_dot_powerbi__pb2.GetSyncedPowerBIItemsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_synced_power_b_i_items), '/textql.rpc.public.powerbi.PowerBIService/GetPowerBIDatasetPreview': Endpoint.unary(method=MethodInfo(name='GetPowerBIDatasetPreview', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.GetPowerBIDatasetPreviewRequest, output=public_dot_powerbi__pb2.GetPowerBIDatasetPreviewResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_power_b_i_dataset_preview)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.powerbi.PowerBIService'

class PowerBIServiceClient(ConnectClient):

    async def test_power_b_i_connection(self, request: public_dot_powerbi__pb2.TestPowerBIConnectionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_powerbi__pb2.TestPowerBIConnectionResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='TestPowerBIConnection', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.TestPowerBIConnectionRequest, output=public_dot_powerbi__pb2.TestPowerBIConnectionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_power_b_i_workspaces(self, request: public_dot_powerbi__pb2.ListPowerBIWorkspacesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_powerbi__pb2.ListPowerBIWorkspacesResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListPowerBIWorkspaces', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.ListPowerBIWorkspacesRequest, output=public_dot_powerbi__pb2.ListPowerBIWorkspacesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_power_b_i_datasets(self, request: public_dot_powerbi__pb2.ListPowerBIDatasetsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_powerbi__pb2.ListPowerBIDatasetsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListPowerBIDatasets', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.ListPowerBIDatasetsRequest, output=public_dot_powerbi__pb2.ListPowerBIDatasetsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_power_b_i_reports(self, request: public_dot_powerbi__pb2.ListPowerBIReportsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_powerbi__pb2.ListPowerBIReportsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListPowerBIReports', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.ListPowerBIReportsRequest, output=public_dot_powerbi__pb2.ListPowerBIReportsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def export_power_b_i_report_image(self, request: public_dot_powerbi__pb2.ExportPowerBIReportImageRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_powerbi__pb2.ExportPowerBIReportImageResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ExportPowerBIReportImage', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.ExportPowerBIReportImageRequest, output=public_dot_powerbi__pb2.ExportPowerBIReportImageResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def generate_power_b_i_embed_token(self, request: public_dot_powerbi__pb2.GeneratePowerBIEmbedTokenRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_powerbi__pb2.GeneratePowerBIEmbedTokenResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GeneratePowerBIEmbedToken', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.GeneratePowerBIEmbedTokenRequest, output=public_dot_powerbi__pb2.GeneratePowerBIEmbedTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def sync_power_b_i_items(self, request: public_dot_powerbi__pb2.SyncPowerBIItemsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_powerbi__pb2.SyncPowerBIItemsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='SyncPowerBIItems', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.SyncPowerBIItemsRequest, output=public_dot_powerbi__pb2.SyncPowerBIItemsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def unsync_power_b_i_items(self, request: public_dot_powerbi__pb2.UnsyncPowerBIItemsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_powerbi__pb2.UnsyncPowerBIItemsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UnsyncPowerBIItems', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.UnsyncPowerBIItemsRequest, output=public_dot_powerbi__pb2.UnsyncPowerBIItemsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_synced_power_b_i_items(self, request: public_dot_powerbi__pb2.GetSyncedPowerBIItemsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_powerbi__pb2.GetSyncedPowerBIItemsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetSyncedPowerBIItems', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.GetSyncedPowerBIItemsRequest, output=public_dot_powerbi__pb2.GetSyncedPowerBIItemsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_power_b_i_dataset_preview(self, request: public_dot_powerbi__pb2.GetPowerBIDatasetPreviewRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_powerbi__pb2.GetPowerBIDatasetPreviewResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetPowerBIDatasetPreview', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.GetPowerBIDatasetPreviewRequest, output=public_dot_powerbi__pb2.GetPowerBIDatasetPreviewResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class PowerBIServiceSync(Protocol):

    def test_power_b_i_connection(self, request: public_dot_powerbi__pb2.TestPowerBIConnectionRequest, ctx: RequestContext) -> public_dot_powerbi__pb2.TestPowerBIConnectionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_power_b_i_workspaces(self, request: public_dot_powerbi__pb2.ListPowerBIWorkspacesRequest, ctx: RequestContext) -> public_dot_powerbi__pb2.ListPowerBIWorkspacesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_power_b_i_datasets(self, request: public_dot_powerbi__pb2.ListPowerBIDatasetsRequest, ctx: RequestContext) -> public_dot_powerbi__pb2.ListPowerBIDatasetsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_power_b_i_reports(self, request: public_dot_powerbi__pb2.ListPowerBIReportsRequest, ctx: RequestContext) -> public_dot_powerbi__pb2.ListPowerBIReportsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def export_power_b_i_report_image(self, request: public_dot_powerbi__pb2.ExportPowerBIReportImageRequest, ctx: RequestContext) -> public_dot_powerbi__pb2.ExportPowerBIReportImageResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def generate_power_b_i_embed_token(self, request: public_dot_powerbi__pb2.GeneratePowerBIEmbedTokenRequest, ctx: RequestContext) -> public_dot_powerbi__pb2.GeneratePowerBIEmbedTokenResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def sync_power_b_i_items(self, request: public_dot_powerbi__pb2.SyncPowerBIItemsRequest, ctx: RequestContext) -> public_dot_powerbi__pb2.SyncPowerBIItemsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def unsync_power_b_i_items(self, request: public_dot_powerbi__pb2.UnsyncPowerBIItemsRequest, ctx: RequestContext) -> public_dot_powerbi__pb2.UnsyncPowerBIItemsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_synced_power_b_i_items(self, request: public_dot_powerbi__pb2.GetSyncedPowerBIItemsRequest, ctx: RequestContext) -> public_dot_powerbi__pb2.GetSyncedPowerBIItemsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_power_b_i_dataset_preview(self, request: public_dot_powerbi__pb2.GetPowerBIDatasetPreviewRequest, ctx: RequestContext) -> public_dot_powerbi__pb2.GetPowerBIDatasetPreviewResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class PowerBIServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: PowerBIServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.powerbi.PowerBIService/TestPowerBIConnection': EndpointSync.unary(method=MethodInfo(name='TestPowerBIConnection', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.TestPowerBIConnectionRequest, output=public_dot_powerbi__pb2.TestPowerBIConnectionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.test_power_b_i_connection), '/textql.rpc.public.powerbi.PowerBIService/ListPowerBIWorkspaces': EndpointSync.unary(method=MethodInfo(name='ListPowerBIWorkspaces', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.ListPowerBIWorkspacesRequest, output=public_dot_powerbi__pb2.ListPowerBIWorkspacesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_power_b_i_workspaces), '/textql.rpc.public.powerbi.PowerBIService/ListPowerBIDatasets': EndpointSync.unary(method=MethodInfo(name='ListPowerBIDatasets', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.ListPowerBIDatasetsRequest, output=public_dot_powerbi__pb2.ListPowerBIDatasetsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_power_b_i_datasets), '/textql.rpc.public.powerbi.PowerBIService/ListPowerBIReports': EndpointSync.unary(method=MethodInfo(name='ListPowerBIReports', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.ListPowerBIReportsRequest, output=public_dot_powerbi__pb2.ListPowerBIReportsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_power_b_i_reports), '/textql.rpc.public.powerbi.PowerBIService/ExportPowerBIReportImage': EndpointSync.unary(method=MethodInfo(name='ExportPowerBIReportImage', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.ExportPowerBIReportImageRequest, output=public_dot_powerbi__pb2.ExportPowerBIReportImageResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.export_power_b_i_report_image), '/textql.rpc.public.powerbi.PowerBIService/GeneratePowerBIEmbedToken': EndpointSync.unary(method=MethodInfo(name='GeneratePowerBIEmbedToken', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.GeneratePowerBIEmbedTokenRequest, output=public_dot_powerbi__pb2.GeneratePowerBIEmbedTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.generate_power_b_i_embed_token), '/textql.rpc.public.powerbi.PowerBIService/SyncPowerBIItems': EndpointSync.unary(method=MethodInfo(name='SyncPowerBIItems', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.SyncPowerBIItemsRequest, output=public_dot_powerbi__pb2.SyncPowerBIItemsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.sync_power_b_i_items), '/textql.rpc.public.powerbi.PowerBIService/UnsyncPowerBIItems': EndpointSync.unary(method=MethodInfo(name='UnsyncPowerBIItems', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.UnsyncPowerBIItemsRequest, output=public_dot_powerbi__pb2.UnsyncPowerBIItemsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.unsync_power_b_i_items), '/textql.rpc.public.powerbi.PowerBIService/GetSyncedPowerBIItems': EndpointSync.unary(method=MethodInfo(name='GetSyncedPowerBIItems', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.GetSyncedPowerBIItemsRequest, output=public_dot_powerbi__pb2.GetSyncedPowerBIItemsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_synced_power_b_i_items), '/textql.rpc.public.powerbi.PowerBIService/GetPowerBIDatasetPreview': EndpointSync.unary(method=MethodInfo(name='GetPowerBIDatasetPreview', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.GetPowerBIDatasetPreviewRequest, output=public_dot_powerbi__pb2.GetPowerBIDatasetPreviewResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_power_b_i_dataset_preview)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.powerbi.PowerBIService'

class PowerBIServiceClientSync(ConnectClientSync):

    def test_power_b_i_connection(self, request: public_dot_powerbi__pb2.TestPowerBIConnectionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_powerbi__pb2.TestPowerBIConnectionResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='TestPowerBIConnection', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.TestPowerBIConnectionRequest, output=public_dot_powerbi__pb2.TestPowerBIConnectionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_power_b_i_workspaces(self, request: public_dot_powerbi__pb2.ListPowerBIWorkspacesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_powerbi__pb2.ListPowerBIWorkspacesResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListPowerBIWorkspaces', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.ListPowerBIWorkspacesRequest, output=public_dot_powerbi__pb2.ListPowerBIWorkspacesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_power_b_i_datasets(self, request: public_dot_powerbi__pb2.ListPowerBIDatasetsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_powerbi__pb2.ListPowerBIDatasetsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListPowerBIDatasets', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.ListPowerBIDatasetsRequest, output=public_dot_powerbi__pb2.ListPowerBIDatasetsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_power_b_i_reports(self, request: public_dot_powerbi__pb2.ListPowerBIReportsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_powerbi__pb2.ListPowerBIReportsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListPowerBIReports', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.ListPowerBIReportsRequest, output=public_dot_powerbi__pb2.ListPowerBIReportsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def export_power_b_i_report_image(self, request: public_dot_powerbi__pb2.ExportPowerBIReportImageRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_powerbi__pb2.ExportPowerBIReportImageResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ExportPowerBIReportImage', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.ExportPowerBIReportImageRequest, output=public_dot_powerbi__pb2.ExportPowerBIReportImageResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def generate_power_b_i_embed_token(self, request: public_dot_powerbi__pb2.GeneratePowerBIEmbedTokenRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_powerbi__pb2.GeneratePowerBIEmbedTokenResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GeneratePowerBIEmbedToken', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.GeneratePowerBIEmbedTokenRequest, output=public_dot_powerbi__pb2.GeneratePowerBIEmbedTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def sync_power_b_i_items(self, request: public_dot_powerbi__pb2.SyncPowerBIItemsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_powerbi__pb2.SyncPowerBIItemsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='SyncPowerBIItems', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.SyncPowerBIItemsRequest, output=public_dot_powerbi__pb2.SyncPowerBIItemsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def unsync_power_b_i_items(self, request: public_dot_powerbi__pb2.UnsyncPowerBIItemsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_powerbi__pb2.UnsyncPowerBIItemsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UnsyncPowerBIItems', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.UnsyncPowerBIItemsRequest, output=public_dot_powerbi__pb2.UnsyncPowerBIItemsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_synced_power_b_i_items(self, request: public_dot_powerbi__pb2.GetSyncedPowerBIItemsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_powerbi__pb2.GetSyncedPowerBIItemsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetSyncedPowerBIItems', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.GetSyncedPowerBIItemsRequest, output=public_dot_powerbi__pb2.GetSyncedPowerBIItemsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_power_b_i_dataset_preview(self, request: public_dot_powerbi__pb2.GetPowerBIDatasetPreviewRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_powerbi__pb2.GetPowerBIDatasetPreviewResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetPowerBIDatasetPreview', service_name='textql.rpc.public.powerbi.PowerBIService', input=public_dot_powerbi__pb2.GetPowerBIDatasetPreviewRequest, output=public_dot_powerbi__pb2.GetPowerBIDatasetPreviewResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)