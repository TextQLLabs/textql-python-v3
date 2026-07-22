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
import google.protobuf.empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import dashboard_pb2 as public_dot_dashboard__pb2

class DashboardService(Protocol):

    async def create_dashboard(self, request: public_dot_dashboard__pb2.CreateDashboardRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.CreateDashboardResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_dashboard(self, request: public_dot_dashboard__pb2.GetDashboardRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.GetDashboardResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_dashboards(self, request: public_dot_dashboard__pb2.ListDashboardsRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.ListDashboardsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_dashboard(self, request: public_dot_dashboard__pb2.UpdateDashboardRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.UpdateDashboardResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_dashboard(self, request: public_dot_dashboard__pb2.DeleteDashboardRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def duplicate_dashboard(self, request: public_dot_dashboard__pb2.DuplicateDashboardRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.DuplicateDashboardResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def spawn_dashboard(self, request: public_dot_dashboard__pb2.SpawnDashboardRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.SpawnDashboardResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def check_dashboard_health(self, request: public_dot_dashboard__pb2.CheckDashboardHealthRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.CheckDashboardHealthResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def watch_dashboard_health(self, request: public_dot_dashboard__pb2.WatchDashboardHealthRequest, ctx: RequestContext) -> AsyncIterator[public_dot_dashboard__pb2.DashboardHealthEvent]:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def regenerate_screenshot(self, request: public_dot_dashboard__pb2.RegenerateScreenshotRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.RegenerateScreenshotResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_members_with_dashboards(self, request: public_dot_dashboard__pb2.GetMembersWithDashboardsRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.GetMembersWithDashboardsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def publish_dashboard(self, request: public_dot_dashboard__pb2.PublishDashboardRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.PublishDashboardResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def discard_dashboard_changes(self, request: public_dot_dashboard__pb2.DiscardDashboardChangesRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.DiscardDashboardChangesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_dashboard_schedule(self, request: public_dot_dashboard__pb2.UpdateDashboardScheduleRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.UpdateDashboardScheduleResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def run_scheduled_dashboard(self, request: public_dot_dashboard__pb2.RunScheduledDashboardRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.RunScheduledDashboardResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def create_dashboard_folder(self, request: public_dot_dashboard__pb2.CreateDashboardFolderRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.CreateDashboardFolderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_dashboard_folders(self, request: public_dot_dashboard__pb2.ListDashboardFoldersRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.ListDashboardFoldersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_dashboard_folder(self, request: public_dot_dashboard__pb2.UpdateDashboardFolderRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.UpdateDashboardFolderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_dashboard_folder(self, request: public_dot_dashboard__pb2.DeleteDashboardFolderRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def move_dashboard_to_folder(self, request: public_dot_dashboard__pb2.MoveDashboardToFolderRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.MoveDashboardToFolderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_dashboard_versions(self, request: public_dot_dashboard__pb2.ListDashboardVersionsRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.ListDashboardVersionsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_dashboard_version(self, request: public_dot_dashboard__pb2.GetDashboardVersionRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.GetDashboardVersionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def restore_dashboard_version(self, request: public_dot_dashboard__pb2.RestoreDashboardVersionRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.RestoreDashboardVersionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_dashboard_view_stats(self, request: public_dot_dashboard__pb2.GetDashboardViewStatsRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.GetDashboardViewStatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def preview_config_dashboard(self, request: public_dot_dashboard__pb2.PreviewConfigDashboardRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.PreviewConfigDashboardResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class DashboardServiceASGIApplication(ConnectASGIApplication[DashboardService]):

    def __init__(self, service: DashboardService | AsyncGenerator[DashboardService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.dashboard.DashboardService/CreateDashboard': Endpoint.unary(method=MethodInfo(name='CreateDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.CreateDashboardRequest, output=public_dot_dashboard__pb2.CreateDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_dashboard), '/textql.rpc.public.dashboard.DashboardService/GetDashboard': Endpoint.unary(method=MethodInfo(name='GetDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.GetDashboardRequest, output=public_dot_dashboard__pb2.GetDashboardResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_dashboard), '/textql.rpc.public.dashboard.DashboardService/ListDashboards': Endpoint.unary(method=MethodInfo(name='ListDashboards', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.ListDashboardsRequest, output=public_dot_dashboard__pb2.ListDashboardsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_dashboards), '/textql.rpc.public.dashboard.DashboardService/UpdateDashboard': Endpoint.unary(method=MethodInfo(name='UpdateDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.UpdateDashboardRequest, output=public_dot_dashboard__pb2.UpdateDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_dashboard), '/textql.rpc.public.dashboard.DashboardService/DeleteDashboard': Endpoint.unary(method=MethodInfo(name='DeleteDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.DeleteDashboardRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_dashboard), '/textql.rpc.public.dashboard.DashboardService/DuplicateDashboard': Endpoint.unary(method=MethodInfo(name='DuplicateDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.DuplicateDashboardRequest, output=public_dot_dashboard__pb2.DuplicateDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.duplicate_dashboard), '/textql.rpc.public.dashboard.DashboardService/SpawnDashboard': Endpoint.unary(method=MethodInfo(name='SpawnDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.SpawnDashboardRequest, output=public_dot_dashboard__pb2.SpawnDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.spawn_dashboard), '/textql.rpc.public.dashboard.DashboardService/CheckDashboardHealth': Endpoint.unary(method=MethodInfo(name='CheckDashboardHealth', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.CheckDashboardHealthRequest, output=public_dot_dashboard__pb2.CheckDashboardHealthResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.check_dashboard_health), '/textql.rpc.public.dashboard.DashboardService/WatchDashboardHealth': Endpoint.server_stream(method=MethodInfo(name='WatchDashboardHealth', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.WatchDashboardHealthRequest, output=public_dot_dashboard__pb2.DashboardHealthEvent, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.watch_dashboard_health), '/textql.rpc.public.dashboard.DashboardService/RegenerateScreenshot': Endpoint.unary(method=MethodInfo(name='RegenerateScreenshot', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.RegenerateScreenshotRequest, output=public_dot_dashboard__pb2.RegenerateScreenshotResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.regenerate_screenshot), '/textql.rpc.public.dashboard.DashboardService/GetMembersWithDashboards': Endpoint.unary(method=MethodInfo(name='GetMembersWithDashboards', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.GetMembersWithDashboardsRequest, output=public_dot_dashboard__pb2.GetMembersWithDashboardsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_members_with_dashboards), '/textql.rpc.public.dashboard.DashboardService/PublishDashboard': Endpoint.unary(method=MethodInfo(name='PublishDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.PublishDashboardRequest, output=public_dot_dashboard__pb2.PublishDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.publish_dashboard), '/textql.rpc.public.dashboard.DashboardService/DiscardDashboardChanges': Endpoint.unary(method=MethodInfo(name='DiscardDashboardChanges', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.DiscardDashboardChangesRequest, output=public_dot_dashboard__pb2.DiscardDashboardChangesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.discard_dashboard_changes), '/textql.rpc.public.dashboard.DashboardService/UpdateDashboardSchedule': Endpoint.unary(method=MethodInfo(name='UpdateDashboardSchedule', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.UpdateDashboardScheduleRequest, output=public_dot_dashboard__pb2.UpdateDashboardScheduleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_dashboard_schedule), '/textql.rpc.public.dashboard.DashboardService/RunScheduledDashboard': Endpoint.unary(method=MethodInfo(name='RunScheduledDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.RunScheduledDashboardRequest, output=public_dot_dashboard__pb2.RunScheduledDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.run_scheduled_dashboard), '/textql.rpc.public.dashboard.DashboardService/CreateDashboardFolder': Endpoint.unary(method=MethodInfo(name='CreateDashboardFolder', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.CreateDashboardFolderRequest, output=public_dot_dashboard__pb2.CreateDashboardFolderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_dashboard_folder), '/textql.rpc.public.dashboard.DashboardService/ListDashboardFolders': Endpoint.unary(method=MethodInfo(name='ListDashboardFolders', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.ListDashboardFoldersRequest, output=public_dot_dashboard__pb2.ListDashboardFoldersResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_dashboard_folders), '/textql.rpc.public.dashboard.DashboardService/UpdateDashboardFolder': Endpoint.unary(method=MethodInfo(name='UpdateDashboardFolder', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.UpdateDashboardFolderRequest, output=public_dot_dashboard__pb2.UpdateDashboardFolderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_dashboard_folder), '/textql.rpc.public.dashboard.DashboardService/DeleteDashboardFolder': Endpoint.unary(method=MethodInfo(name='DeleteDashboardFolder', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.DeleteDashboardFolderRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_dashboard_folder), '/textql.rpc.public.dashboard.DashboardService/MoveDashboardToFolder': Endpoint.unary(method=MethodInfo(name='MoveDashboardToFolder', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.MoveDashboardToFolderRequest, output=public_dot_dashboard__pb2.MoveDashboardToFolderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.move_dashboard_to_folder), '/textql.rpc.public.dashboard.DashboardService/ListDashboardVersions': Endpoint.unary(method=MethodInfo(name='ListDashboardVersions', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.ListDashboardVersionsRequest, output=public_dot_dashboard__pb2.ListDashboardVersionsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_dashboard_versions), '/textql.rpc.public.dashboard.DashboardService/GetDashboardVersion': Endpoint.unary(method=MethodInfo(name='GetDashboardVersion', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.GetDashboardVersionRequest, output=public_dot_dashboard__pb2.GetDashboardVersionResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_dashboard_version), '/textql.rpc.public.dashboard.DashboardService/RestoreDashboardVersion': Endpoint.unary(method=MethodInfo(name='RestoreDashboardVersion', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.RestoreDashboardVersionRequest, output=public_dot_dashboard__pb2.RestoreDashboardVersionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.restore_dashboard_version), '/textql.rpc.public.dashboard.DashboardService/GetDashboardViewStats': Endpoint.unary(method=MethodInfo(name='GetDashboardViewStats', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.GetDashboardViewStatsRequest, output=public_dot_dashboard__pb2.GetDashboardViewStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_dashboard_view_stats), '/textql.rpc.public.dashboard.DashboardService/PreviewConfigDashboard': Endpoint.unary(method=MethodInfo(name='PreviewConfigDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.PreviewConfigDashboardRequest, output=public_dot_dashboard__pb2.PreviewConfigDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.preview_config_dashboard)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.dashboard.DashboardService'

class DashboardServiceClient(ConnectClient):

    async def create_dashboard(self, request: public_dot_dashboard__pb2.CreateDashboardRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.CreateDashboardResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.CreateDashboardRequest, output=public_dot_dashboard__pb2.CreateDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_dashboard(self, request: public_dot_dashboard__pb2.GetDashboardRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dashboard__pb2.GetDashboardResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.GetDashboardRequest, output=public_dot_dashboard__pb2.GetDashboardResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def list_dashboards(self, request: public_dot_dashboard__pb2.ListDashboardsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dashboard__pb2.ListDashboardsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListDashboards', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.ListDashboardsRequest, output=public_dot_dashboard__pb2.ListDashboardsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def update_dashboard(self, request: public_dot_dashboard__pb2.UpdateDashboardRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.UpdateDashboardResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.UpdateDashboardRequest, output=public_dot_dashboard__pb2.UpdateDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def delete_dashboard(self, request: public_dot_dashboard__pb2.DeleteDashboardRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.DeleteDashboardRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def duplicate_dashboard(self, request: public_dot_dashboard__pb2.DuplicateDashboardRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.DuplicateDashboardResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DuplicateDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.DuplicateDashboardRequest, output=public_dot_dashboard__pb2.DuplicateDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def spawn_dashboard(self, request: public_dot_dashboard__pb2.SpawnDashboardRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.SpawnDashboardResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='SpawnDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.SpawnDashboardRequest, output=public_dot_dashboard__pb2.SpawnDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def check_dashboard_health(self, request: public_dot_dashboard__pb2.CheckDashboardHealthRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dashboard__pb2.CheckDashboardHealthResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CheckDashboardHealth', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.CheckDashboardHealthRequest, output=public_dot_dashboard__pb2.CheckDashboardHealthResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def watch_dashboard_health(self, request: public_dot_dashboard__pb2.WatchDashboardHealthRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> AsyncIterator[public_dot_dashboard__pb2.DashboardHealthEvent]:
        return self.execute_server_stream(request=request, method=MethodInfo(name='WatchDashboardHealth', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.WatchDashboardHealthRequest, output=public_dot_dashboard__pb2.DashboardHealthEvent, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def regenerate_screenshot(self, request: public_dot_dashboard__pb2.RegenerateScreenshotRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.RegenerateScreenshotResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RegenerateScreenshot', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.RegenerateScreenshotRequest, output=public_dot_dashboard__pb2.RegenerateScreenshotResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_members_with_dashboards(self, request: public_dot_dashboard__pb2.GetMembersWithDashboardsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dashboard__pb2.GetMembersWithDashboardsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetMembersWithDashboards', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.GetMembersWithDashboardsRequest, output=public_dot_dashboard__pb2.GetMembersWithDashboardsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def publish_dashboard(self, request: public_dot_dashboard__pb2.PublishDashboardRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.PublishDashboardResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='PublishDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.PublishDashboardRequest, output=public_dot_dashboard__pb2.PublishDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def discard_dashboard_changes(self, request: public_dot_dashboard__pb2.DiscardDashboardChangesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.DiscardDashboardChangesResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DiscardDashboardChanges', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.DiscardDashboardChangesRequest, output=public_dot_dashboard__pb2.DiscardDashboardChangesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def update_dashboard_schedule(self, request: public_dot_dashboard__pb2.UpdateDashboardScheduleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.UpdateDashboardScheduleResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateDashboardSchedule', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.UpdateDashboardScheduleRequest, output=public_dot_dashboard__pb2.UpdateDashboardScheduleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def run_scheduled_dashboard(self, request: public_dot_dashboard__pb2.RunScheduledDashboardRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.RunScheduledDashboardResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RunScheduledDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.RunScheduledDashboardRequest, output=public_dot_dashboard__pb2.RunScheduledDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def create_dashboard_folder(self, request: public_dot_dashboard__pb2.CreateDashboardFolderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.CreateDashboardFolderResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateDashboardFolder', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.CreateDashboardFolderRequest, output=public_dot_dashboard__pb2.CreateDashboardFolderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_dashboard_folders(self, request: public_dot_dashboard__pb2.ListDashboardFoldersRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dashboard__pb2.ListDashboardFoldersResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListDashboardFolders', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.ListDashboardFoldersRequest, output=public_dot_dashboard__pb2.ListDashboardFoldersResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def update_dashboard_folder(self, request: public_dot_dashboard__pb2.UpdateDashboardFolderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.UpdateDashboardFolderResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateDashboardFolder', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.UpdateDashboardFolderRequest, output=public_dot_dashboard__pb2.UpdateDashboardFolderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def delete_dashboard_folder(self, request: public_dot_dashboard__pb2.DeleteDashboardFolderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteDashboardFolder', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.DeleteDashboardFolderRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def move_dashboard_to_folder(self, request: public_dot_dashboard__pb2.MoveDashboardToFolderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.MoveDashboardToFolderResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='MoveDashboardToFolder', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.MoveDashboardToFolderRequest, output=public_dot_dashboard__pb2.MoveDashboardToFolderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_dashboard_versions(self, request: public_dot_dashboard__pb2.ListDashboardVersionsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dashboard__pb2.ListDashboardVersionsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListDashboardVersions', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.ListDashboardVersionsRequest, output=public_dot_dashboard__pb2.ListDashboardVersionsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_dashboard_version(self, request: public_dot_dashboard__pb2.GetDashboardVersionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dashboard__pb2.GetDashboardVersionResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetDashboardVersion', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.GetDashboardVersionRequest, output=public_dot_dashboard__pb2.GetDashboardVersionResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def restore_dashboard_version(self, request: public_dot_dashboard__pb2.RestoreDashboardVersionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.RestoreDashboardVersionResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RestoreDashboardVersion', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.RestoreDashboardVersionRequest, output=public_dot_dashboard__pb2.RestoreDashboardVersionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_dashboard_view_stats(self, request: public_dot_dashboard__pb2.GetDashboardViewStatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dashboard__pb2.GetDashboardViewStatsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetDashboardViewStats', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.GetDashboardViewStatsRequest, output=public_dot_dashboard__pb2.GetDashboardViewStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def preview_config_dashboard(self, request: public_dot_dashboard__pb2.PreviewConfigDashboardRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.PreviewConfigDashboardResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='PreviewConfigDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.PreviewConfigDashboardRequest, output=public_dot_dashboard__pb2.PreviewConfigDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class DashboardServiceSync(Protocol):

    def create_dashboard(self, request: public_dot_dashboard__pb2.CreateDashboardRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.CreateDashboardResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_dashboard(self, request: public_dot_dashboard__pb2.GetDashboardRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.GetDashboardResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_dashboards(self, request: public_dot_dashboard__pb2.ListDashboardsRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.ListDashboardsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_dashboard(self, request: public_dot_dashboard__pb2.UpdateDashboardRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.UpdateDashboardResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_dashboard(self, request: public_dot_dashboard__pb2.DeleteDashboardRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def duplicate_dashboard(self, request: public_dot_dashboard__pb2.DuplicateDashboardRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.DuplicateDashboardResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def spawn_dashboard(self, request: public_dot_dashboard__pb2.SpawnDashboardRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.SpawnDashboardResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def check_dashboard_health(self, request: public_dot_dashboard__pb2.CheckDashboardHealthRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.CheckDashboardHealthResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def watch_dashboard_health(self, request: public_dot_dashboard__pb2.WatchDashboardHealthRequest, ctx: RequestContext) -> Iterator[public_dot_dashboard__pb2.DashboardHealthEvent]:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def regenerate_screenshot(self, request: public_dot_dashboard__pb2.RegenerateScreenshotRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.RegenerateScreenshotResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_members_with_dashboards(self, request: public_dot_dashboard__pb2.GetMembersWithDashboardsRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.GetMembersWithDashboardsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def publish_dashboard(self, request: public_dot_dashboard__pb2.PublishDashboardRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.PublishDashboardResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def discard_dashboard_changes(self, request: public_dot_dashboard__pb2.DiscardDashboardChangesRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.DiscardDashboardChangesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_dashboard_schedule(self, request: public_dot_dashboard__pb2.UpdateDashboardScheduleRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.UpdateDashboardScheduleResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def run_scheduled_dashboard(self, request: public_dot_dashboard__pb2.RunScheduledDashboardRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.RunScheduledDashboardResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def create_dashboard_folder(self, request: public_dot_dashboard__pb2.CreateDashboardFolderRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.CreateDashboardFolderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_dashboard_folders(self, request: public_dot_dashboard__pb2.ListDashboardFoldersRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.ListDashboardFoldersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_dashboard_folder(self, request: public_dot_dashboard__pb2.UpdateDashboardFolderRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.UpdateDashboardFolderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_dashboard_folder(self, request: public_dot_dashboard__pb2.DeleteDashboardFolderRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def move_dashboard_to_folder(self, request: public_dot_dashboard__pb2.MoveDashboardToFolderRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.MoveDashboardToFolderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_dashboard_versions(self, request: public_dot_dashboard__pb2.ListDashboardVersionsRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.ListDashboardVersionsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_dashboard_version(self, request: public_dot_dashboard__pb2.GetDashboardVersionRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.GetDashboardVersionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def restore_dashboard_version(self, request: public_dot_dashboard__pb2.RestoreDashboardVersionRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.RestoreDashboardVersionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_dashboard_view_stats(self, request: public_dot_dashboard__pb2.GetDashboardViewStatsRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.GetDashboardViewStatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def preview_config_dashboard(self, request: public_dot_dashboard__pb2.PreviewConfigDashboardRequest, ctx: RequestContext) -> public_dot_dashboard__pb2.PreviewConfigDashboardResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class DashboardServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: DashboardServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.dashboard.DashboardService/CreateDashboard': EndpointSync.unary(method=MethodInfo(name='CreateDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.CreateDashboardRequest, output=public_dot_dashboard__pb2.CreateDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_dashboard), '/textql.rpc.public.dashboard.DashboardService/GetDashboard': EndpointSync.unary(method=MethodInfo(name='GetDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.GetDashboardRequest, output=public_dot_dashboard__pb2.GetDashboardResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_dashboard), '/textql.rpc.public.dashboard.DashboardService/ListDashboards': EndpointSync.unary(method=MethodInfo(name='ListDashboards', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.ListDashboardsRequest, output=public_dot_dashboard__pb2.ListDashboardsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_dashboards), '/textql.rpc.public.dashboard.DashboardService/UpdateDashboard': EndpointSync.unary(method=MethodInfo(name='UpdateDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.UpdateDashboardRequest, output=public_dot_dashboard__pb2.UpdateDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_dashboard), '/textql.rpc.public.dashboard.DashboardService/DeleteDashboard': EndpointSync.unary(method=MethodInfo(name='DeleteDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.DeleteDashboardRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_dashboard), '/textql.rpc.public.dashboard.DashboardService/DuplicateDashboard': EndpointSync.unary(method=MethodInfo(name='DuplicateDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.DuplicateDashboardRequest, output=public_dot_dashboard__pb2.DuplicateDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.duplicate_dashboard), '/textql.rpc.public.dashboard.DashboardService/SpawnDashboard': EndpointSync.unary(method=MethodInfo(name='SpawnDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.SpawnDashboardRequest, output=public_dot_dashboard__pb2.SpawnDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.spawn_dashboard), '/textql.rpc.public.dashboard.DashboardService/CheckDashboardHealth': EndpointSync.unary(method=MethodInfo(name='CheckDashboardHealth', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.CheckDashboardHealthRequest, output=public_dot_dashboard__pb2.CheckDashboardHealthResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.check_dashboard_health), '/textql.rpc.public.dashboard.DashboardService/WatchDashboardHealth': EndpointSync.server_stream(method=MethodInfo(name='WatchDashboardHealth', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.WatchDashboardHealthRequest, output=public_dot_dashboard__pb2.DashboardHealthEvent, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.watch_dashboard_health), '/textql.rpc.public.dashboard.DashboardService/RegenerateScreenshot': EndpointSync.unary(method=MethodInfo(name='RegenerateScreenshot', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.RegenerateScreenshotRequest, output=public_dot_dashboard__pb2.RegenerateScreenshotResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.regenerate_screenshot), '/textql.rpc.public.dashboard.DashboardService/GetMembersWithDashboards': EndpointSync.unary(method=MethodInfo(name='GetMembersWithDashboards', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.GetMembersWithDashboardsRequest, output=public_dot_dashboard__pb2.GetMembersWithDashboardsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_members_with_dashboards), '/textql.rpc.public.dashboard.DashboardService/PublishDashboard': EndpointSync.unary(method=MethodInfo(name='PublishDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.PublishDashboardRequest, output=public_dot_dashboard__pb2.PublishDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.publish_dashboard), '/textql.rpc.public.dashboard.DashboardService/DiscardDashboardChanges': EndpointSync.unary(method=MethodInfo(name='DiscardDashboardChanges', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.DiscardDashboardChangesRequest, output=public_dot_dashboard__pb2.DiscardDashboardChangesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.discard_dashboard_changes), '/textql.rpc.public.dashboard.DashboardService/UpdateDashboardSchedule': EndpointSync.unary(method=MethodInfo(name='UpdateDashboardSchedule', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.UpdateDashboardScheduleRequest, output=public_dot_dashboard__pb2.UpdateDashboardScheduleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_dashboard_schedule), '/textql.rpc.public.dashboard.DashboardService/RunScheduledDashboard': EndpointSync.unary(method=MethodInfo(name='RunScheduledDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.RunScheduledDashboardRequest, output=public_dot_dashboard__pb2.RunScheduledDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.run_scheduled_dashboard), '/textql.rpc.public.dashboard.DashboardService/CreateDashboardFolder': EndpointSync.unary(method=MethodInfo(name='CreateDashboardFolder', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.CreateDashboardFolderRequest, output=public_dot_dashboard__pb2.CreateDashboardFolderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_dashboard_folder), '/textql.rpc.public.dashboard.DashboardService/ListDashboardFolders': EndpointSync.unary(method=MethodInfo(name='ListDashboardFolders', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.ListDashboardFoldersRequest, output=public_dot_dashboard__pb2.ListDashboardFoldersResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_dashboard_folders), '/textql.rpc.public.dashboard.DashboardService/UpdateDashboardFolder': EndpointSync.unary(method=MethodInfo(name='UpdateDashboardFolder', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.UpdateDashboardFolderRequest, output=public_dot_dashboard__pb2.UpdateDashboardFolderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_dashboard_folder), '/textql.rpc.public.dashboard.DashboardService/DeleteDashboardFolder': EndpointSync.unary(method=MethodInfo(name='DeleteDashboardFolder', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.DeleteDashboardFolderRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_dashboard_folder), '/textql.rpc.public.dashboard.DashboardService/MoveDashboardToFolder': EndpointSync.unary(method=MethodInfo(name='MoveDashboardToFolder', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.MoveDashboardToFolderRequest, output=public_dot_dashboard__pb2.MoveDashboardToFolderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.move_dashboard_to_folder), '/textql.rpc.public.dashboard.DashboardService/ListDashboardVersions': EndpointSync.unary(method=MethodInfo(name='ListDashboardVersions', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.ListDashboardVersionsRequest, output=public_dot_dashboard__pb2.ListDashboardVersionsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_dashboard_versions), '/textql.rpc.public.dashboard.DashboardService/GetDashboardVersion': EndpointSync.unary(method=MethodInfo(name='GetDashboardVersion', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.GetDashboardVersionRequest, output=public_dot_dashboard__pb2.GetDashboardVersionResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_dashboard_version), '/textql.rpc.public.dashboard.DashboardService/RestoreDashboardVersion': EndpointSync.unary(method=MethodInfo(name='RestoreDashboardVersion', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.RestoreDashboardVersionRequest, output=public_dot_dashboard__pb2.RestoreDashboardVersionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.restore_dashboard_version), '/textql.rpc.public.dashboard.DashboardService/GetDashboardViewStats': EndpointSync.unary(method=MethodInfo(name='GetDashboardViewStats', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.GetDashboardViewStatsRequest, output=public_dot_dashboard__pb2.GetDashboardViewStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_dashboard_view_stats), '/textql.rpc.public.dashboard.DashboardService/PreviewConfigDashboard': EndpointSync.unary(method=MethodInfo(name='PreviewConfigDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.PreviewConfigDashboardRequest, output=public_dot_dashboard__pb2.PreviewConfigDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.preview_config_dashboard)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.dashboard.DashboardService'

class DashboardServiceClientSync(ConnectClientSync):

    def create_dashboard(self, request: public_dot_dashboard__pb2.CreateDashboardRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.CreateDashboardResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.CreateDashboardRequest, output=public_dot_dashboard__pb2.CreateDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_dashboard(self, request: public_dot_dashboard__pb2.GetDashboardRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dashboard__pb2.GetDashboardResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.GetDashboardRequest, output=public_dot_dashboard__pb2.GetDashboardResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def list_dashboards(self, request: public_dot_dashboard__pb2.ListDashboardsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dashboard__pb2.ListDashboardsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListDashboards', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.ListDashboardsRequest, output=public_dot_dashboard__pb2.ListDashboardsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def update_dashboard(self, request: public_dot_dashboard__pb2.UpdateDashboardRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.UpdateDashboardResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.UpdateDashboardRequest, output=public_dot_dashboard__pb2.UpdateDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def delete_dashboard(self, request: public_dot_dashboard__pb2.DeleteDashboardRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.DeleteDashboardRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def duplicate_dashboard(self, request: public_dot_dashboard__pb2.DuplicateDashboardRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.DuplicateDashboardResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DuplicateDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.DuplicateDashboardRequest, output=public_dot_dashboard__pb2.DuplicateDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def spawn_dashboard(self, request: public_dot_dashboard__pb2.SpawnDashboardRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.SpawnDashboardResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='SpawnDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.SpawnDashboardRequest, output=public_dot_dashboard__pb2.SpawnDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def check_dashboard_health(self, request: public_dot_dashboard__pb2.CheckDashboardHealthRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dashboard__pb2.CheckDashboardHealthResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CheckDashboardHealth', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.CheckDashboardHealthRequest, output=public_dot_dashboard__pb2.CheckDashboardHealthResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def watch_dashboard_health(self, request: public_dot_dashboard__pb2.WatchDashboardHealthRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> Iterator[public_dot_dashboard__pb2.DashboardHealthEvent]:
        return self.execute_server_stream(request=request, method=MethodInfo(name='WatchDashboardHealth', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.WatchDashboardHealthRequest, output=public_dot_dashboard__pb2.DashboardHealthEvent, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def regenerate_screenshot(self, request: public_dot_dashboard__pb2.RegenerateScreenshotRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.RegenerateScreenshotResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RegenerateScreenshot', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.RegenerateScreenshotRequest, output=public_dot_dashboard__pb2.RegenerateScreenshotResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_members_with_dashboards(self, request: public_dot_dashboard__pb2.GetMembersWithDashboardsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dashboard__pb2.GetMembersWithDashboardsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetMembersWithDashboards', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.GetMembersWithDashboardsRequest, output=public_dot_dashboard__pb2.GetMembersWithDashboardsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def publish_dashboard(self, request: public_dot_dashboard__pb2.PublishDashboardRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.PublishDashboardResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='PublishDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.PublishDashboardRequest, output=public_dot_dashboard__pb2.PublishDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def discard_dashboard_changes(self, request: public_dot_dashboard__pb2.DiscardDashboardChangesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.DiscardDashboardChangesResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DiscardDashboardChanges', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.DiscardDashboardChangesRequest, output=public_dot_dashboard__pb2.DiscardDashboardChangesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def update_dashboard_schedule(self, request: public_dot_dashboard__pb2.UpdateDashboardScheduleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.UpdateDashboardScheduleResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateDashboardSchedule', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.UpdateDashboardScheduleRequest, output=public_dot_dashboard__pb2.UpdateDashboardScheduleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def run_scheduled_dashboard(self, request: public_dot_dashboard__pb2.RunScheduledDashboardRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.RunScheduledDashboardResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RunScheduledDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.RunScheduledDashboardRequest, output=public_dot_dashboard__pb2.RunScheduledDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def create_dashboard_folder(self, request: public_dot_dashboard__pb2.CreateDashboardFolderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.CreateDashboardFolderResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateDashboardFolder', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.CreateDashboardFolderRequest, output=public_dot_dashboard__pb2.CreateDashboardFolderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_dashboard_folders(self, request: public_dot_dashboard__pb2.ListDashboardFoldersRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dashboard__pb2.ListDashboardFoldersResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListDashboardFolders', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.ListDashboardFoldersRequest, output=public_dot_dashboard__pb2.ListDashboardFoldersResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def update_dashboard_folder(self, request: public_dot_dashboard__pb2.UpdateDashboardFolderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.UpdateDashboardFolderResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateDashboardFolder', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.UpdateDashboardFolderRequest, output=public_dot_dashboard__pb2.UpdateDashboardFolderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def delete_dashboard_folder(self, request: public_dot_dashboard__pb2.DeleteDashboardFolderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteDashboardFolder', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.DeleteDashboardFolderRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def move_dashboard_to_folder(self, request: public_dot_dashboard__pb2.MoveDashboardToFolderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.MoveDashboardToFolderResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='MoveDashboardToFolder', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.MoveDashboardToFolderRequest, output=public_dot_dashboard__pb2.MoveDashboardToFolderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_dashboard_versions(self, request: public_dot_dashboard__pb2.ListDashboardVersionsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dashboard__pb2.ListDashboardVersionsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListDashboardVersions', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.ListDashboardVersionsRequest, output=public_dot_dashboard__pb2.ListDashboardVersionsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_dashboard_version(self, request: public_dot_dashboard__pb2.GetDashboardVersionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dashboard__pb2.GetDashboardVersionResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetDashboardVersion', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.GetDashboardVersionRequest, output=public_dot_dashboard__pb2.GetDashboardVersionResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def restore_dashboard_version(self, request: public_dot_dashboard__pb2.RestoreDashboardVersionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.RestoreDashboardVersionResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RestoreDashboardVersion', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.RestoreDashboardVersionRequest, output=public_dot_dashboard__pb2.RestoreDashboardVersionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_dashboard_view_stats(self, request: public_dot_dashboard__pb2.GetDashboardViewStatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dashboard__pb2.GetDashboardViewStatsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetDashboardViewStats', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.GetDashboardViewStatsRequest, output=public_dot_dashboard__pb2.GetDashboardViewStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def preview_config_dashboard(self, request: public_dot_dashboard__pb2.PreviewConfigDashboardRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dashboard__pb2.PreviewConfigDashboardResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='PreviewConfigDashboard', service_name='textql.rpc.public.dashboard.DashboardService', input=public_dot_dashboard__pb2.PreviewConfigDashboardRequest, output=public_dot_dashboard__pb2.PreviewConfigDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)