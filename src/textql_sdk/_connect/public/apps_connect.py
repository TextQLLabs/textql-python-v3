# pylint: skip-file
# mypy: ignore-errors
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
from . import apps_pb2 as public_dot_apps__pb2

class AppService(Protocol):

    async def create_app(self, request: public_dot_apps__pb2.CreateAppRequest, ctx: RequestContext) -> public_dot_apps__pb2.CreateAppResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def duplicate_app(self, request: public_dot_apps__pb2.DuplicateAppRequest, ctx: RequestContext) -> public_dot_apps__pb2.DuplicateAppResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_app(self, request: public_dot_apps__pb2.GetAppRequest, ctx: RequestContext) -> public_dot_apps__pb2.GetAppResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_apps(self, request: public_dot_apps__pb2.ListAppsRequest, ctx: RequestContext) -> public_dot_apps__pb2.ListAppsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_members_with_apps(self, request: public_dot_apps__pb2.GetMembersWithAppsRequest, ctx: RequestContext) -> public_dot_apps__pb2.GetMembersWithAppsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_app(self, request: public_dot_apps__pb2.UpdateAppRequest, ctx: RequestContext) -> public_dot_apps__pb2.UpdateAppResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_app(self, request: public_dot_apps__pb2.DeleteAppRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def move_app_to_folder(self, request: public_dot_apps__pb2.MoveAppToFolderRequest, ctx: RequestContext) -> public_dot_apps__pb2.MoveAppToFolderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def refresh_app(self, request: public_dot_apps__pb2.RefreshAppRequest, ctx: RequestContext) -> public_dot_apps__pb2.RefreshAppResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_app_versions(self, request: public_dot_apps__pb2.ListAppVersionsRequest, ctx: RequestContext) -> public_dot_apps__pb2.ListAppVersionsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_app_version(self, request: public_dot_apps__pb2.GetAppVersionRequest, ctx: RequestContext) -> public_dot_apps__pb2.GetAppVersionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def restore_app_version(self, request: public_dot_apps__pb2.RestoreAppVersionRequest, ctx: RequestContext) -> public_dot_apps__pb2.RestoreAppVersionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def invoke_app_compute_function(self, request: public_dot_apps__pb2.InvokeAppComputeFunctionRequest, ctx: RequestContext) -> public_dot_apps__pb2.InvokeAppComputeFunctionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def app_heartbeat(self, request: public_dot_apps__pb2.AppHeartbeatRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def set_favorite(self, request: public_dot_apps__pb2.SetFavoriteRequest, ctx: RequestContext) -> public_dot_apps__pb2.SetFavoriteResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_app_view_stats(self, request: public_dot_apps__pb2.GetAppViewStatsRequest, ctx: RequestContext) -> public_dot_apps__pb2.GetAppViewStatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_component_gallery_url(self, request: public_dot_apps__pb2.GetComponentGalleryUrlRequest, ctx: RequestContext) -> public_dot_apps__pb2.GetComponentGalleryUrlResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_app_member_state(self, request: public_dot_apps__pb2.GetAppMemberStateRequest, ctx: RequestContext) -> public_dot_apps__pb2.GetAppMemberStateResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def set_app_member_state(self, request: public_dot_apps__pb2.SetAppMemberStateRequest, ctx: RequestContext) -> public_dot_apps__pb2.SetAppMemberStateResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def record_app_member_activity(self, request: public_dot_apps__pb2.RecordAppMemberActivityRequest, ctx: RequestContext) -> public_dot_apps__pb2.RecordAppMemberActivityResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_my_app_member_activity(self, request: public_dot_apps__pb2.ListMyAppMemberActivityRequest, ctx: RequestContext) -> public_dot_apps__pb2.ListMyAppMemberActivityResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_app_activity_since(self, request: public_dot_apps__pb2.ListAppActivitySinceRequest, ctx: RequestContext) -> public_dot_apps__pb2.ListAppActivitySinceResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def stream_app_activity(self, request: public_dot_apps__pb2.StreamAppActivityRequest, ctx: RequestContext) -> AsyncIterator[public_dot_apps__pb2.AppActivityStreamEvent]:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def presence_heartbeat(self, request: public_dot_apps__pb2.PresenceHeartbeatRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class AppServiceASGIApplication(ConnectASGIApplication[AppService]):

    def __init__(self, service: AppService | AsyncGenerator[AppService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.app.AppService/CreateApp': Endpoint.unary(method=MethodInfo(name='CreateApp', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.CreateAppRequest, output=public_dot_apps__pb2.CreateAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_app), '/textql.rpc.public.app.AppService/DuplicateApp': Endpoint.unary(method=MethodInfo(name='DuplicateApp', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.DuplicateAppRequest, output=public_dot_apps__pb2.DuplicateAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.duplicate_app), '/textql.rpc.public.app.AppService/GetApp': Endpoint.unary(method=MethodInfo(name='GetApp', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.GetAppRequest, output=public_dot_apps__pb2.GetAppResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_app), '/textql.rpc.public.app.AppService/ListApps': Endpoint.unary(method=MethodInfo(name='ListApps', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.ListAppsRequest, output=public_dot_apps__pb2.ListAppsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_apps), '/textql.rpc.public.app.AppService/GetMembersWithApps': Endpoint.unary(method=MethodInfo(name='GetMembersWithApps', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.GetMembersWithAppsRequest, output=public_dot_apps__pb2.GetMembersWithAppsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_members_with_apps), '/textql.rpc.public.app.AppService/UpdateApp': Endpoint.unary(method=MethodInfo(name='UpdateApp', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.UpdateAppRequest, output=public_dot_apps__pb2.UpdateAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_app), '/textql.rpc.public.app.AppService/DeleteApp': Endpoint.unary(method=MethodInfo(name='DeleteApp', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.DeleteAppRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_app), '/textql.rpc.public.app.AppService/MoveAppToFolder': Endpoint.unary(method=MethodInfo(name='MoveAppToFolder', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.MoveAppToFolderRequest, output=public_dot_apps__pb2.MoveAppToFolderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.move_app_to_folder), '/textql.rpc.public.app.AppService/RefreshApp': Endpoint.unary(method=MethodInfo(name='RefreshApp', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.RefreshAppRequest, output=public_dot_apps__pb2.RefreshAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.refresh_app), '/textql.rpc.public.app.AppService/ListAppVersions': Endpoint.unary(method=MethodInfo(name='ListAppVersions', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.ListAppVersionsRequest, output=public_dot_apps__pb2.ListAppVersionsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_app_versions), '/textql.rpc.public.app.AppService/GetAppVersion': Endpoint.unary(method=MethodInfo(name='GetAppVersion', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.GetAppVersionRequest, output=public_dot_apps__pb2.GetAppVersionResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_app_version), '/textql.rpc.public.app.AppService/RestoreAppVersion': Endpoint.unary(method=MethodInfo(name='RestoreAppVersion', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.RestoreAppVersionRequest, output=public_dot_apps__pb2.RestoreAppVersionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.restore_app_version), '/textql.rpc.public.app.AppService/InvokeAppComputeFunction': Endpoint.unary(method=MethodInfo(name='InvokeAppComputeFunction', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.InvokeAppComputeFunctionRequest, output=public_dot_apps__pb2.InvokeAppComputeFunctionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.invoke_app_compute_function), '/textql.rpc.public.app.AppService/AppHeartbeat': Endpoint.unary(method=MethodInfo(name='AppHeartbeat', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.AppHeartbeatRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.app_heartbeat), '/textql.rpc.public.app.AppService/SetFavorite': Endpoint.unary(method=MethodInfo(name='SetFavorite', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.SetFavoriteRequest, output=public_dot_apps__pb2.SetFavoriteResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.set_favorite), '/textql.rpc.public.app.AppService/GetAppViewStats': Endpoint.unary(method=MethodInfo(name='GetAppViewStats', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.GetAppViewStatsRequest, output=public_dot_apps__pb2.GetAppViewStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_app_view_stats), '/textql.rpc.public.app.AppService/GetComponentGalleryUrl': Endpoint.unary(method=MethodInfo(name='GetComponentGalleryUrl', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.GetComponentGalleryUrlRequest, output=public_dot_apps__pb2.GetComponentGalleryUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_component_gallery_url), '/textql.rpc.public.app.AppService/GetAppMemberState': Endpoint.unary(method=MethodInfo(name='GetAppMemberState', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.GetAppMemberStateRequest, output=public_dot_apps__pb2.GetAppMemberStateResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_app_member_state), '/textql.rpc.public.app.AppService/SetAppMemberState': Endpoint.unary(method=MethodInfo(name='SetAppMemberState', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.SetAppMemberStateRequest, output=public_dot_apps__pb2.SetAppMemberStateResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.set_app_member_state), '/textql.rpc.public.app.AppService/RecordAppMemberActivity': Endpoint.unary(method=MethodInfo(name='RecordAppMemberActivity', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.RecordAppMemberActivityRequest, output=public_dot_apps__pb2.RecordAppMemberActivityResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.record_app_member_activity), '/textql.rpc.public.app.AppService/ListMyAppMemberActivity': Endpoint.unary(method=MethodInfo(name='ListMyAppMemberActivity', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.ListMyAppMemberActivityRequest, output=public_dot_apps__pb2.ListMyAppMemberActivityResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_my_app_member_activity), '/textql.rpc.public.app.AppService/ListAppActivitySince': Endpoint.unary(method=MethodInfo(name='ListAppActivitySince', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.ListAppActivitySinceRequest, output=public_dot_apps__pb2.ListAppActivitySinceResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_app_activity_since), '/textql.rpc.public.app.AppService/StreamAppActivity': Endpoint.server_stream(method=MethodInfo(name='StreamAppActivity', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.StreamAppActivityRequest, output=public_dot_apps__pb2.AppActivityStreamEvent, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.stream_app_activity), '/textql.rpc.public.app.AppService/PresenceHeartbeat': Endpoint.unary(method=MethodInfo(name='PresenceHeartbeat', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.PresenceHeartbeatRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.presence_heartbeat)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.app.AppService'

class AppServiceClient(ConnectClient):

    async def create_app(self, request: public_dot_apps__pb2.CreateAppRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_apps__pb2.CreateAppResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateApp', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.CreateAppRequest, output=public_dot_apps__pb2.CreateAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def duplicate_app(self, request: public_dot_apps__pb2.DuplicateAppRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_apps__pb2.DuplicateAppResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DuplicateApp', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.DuplicateAppRequest, output=public_dot_apps__pb2.DuplicateAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_app(self, request: public_dot_apps__pb2.GetAppRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_apps__pb2.GetAppResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetApp', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.GetAppRequest, output=public_dot_apps__pb2.GetAppResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def list_apps(self, request: public_dot_apps__pb2.ListAppsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_apps__pb2.ListAppsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListApps', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.ListAppsRequest, output=public_dot_apps__pb2.ListAppsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_members_with_apps(self, request: public_dot_apps__pb2.GetMembersWithAppsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_apps__pb2.GetMembersWithAppsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetMembersWithApps', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.GetMembersWithAppsRequest, output=public_dot_apps__pb2.GetMembersWithAppsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def update_app(self, request: public_dot_apps__pb2.UpdateAppRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_apps__pb2.UpdateAppResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateApp', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.UpdateAppRequest, output=public_dot_apps__pb2.UpdateAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def delete_app(self, request: public_dot_apps__pb2.DeleteAppRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteApp', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.DeleteAppRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def move_app_to_folder(self, request: public_dot_apps__pb2.MoveAppToFolderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_apps__pb2.MoveAppToFolderResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='MoveAppToFolder', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.MoveAppToFolderRequest, output=public_dot_apps__pb2.MoveAppToFolderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def refresh_app(self, request: public_dot_apps__pb2.RefreshAppRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_apps__pb2.RefreshAppResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RefreshApp', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.RefreshAppRequest, output=public_dot_apps__pb2.RefreshAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_app_versions(self, request: public_dot_apps__pb2.ListAppVersionsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_apps__pb2.ListAppVersionsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListAppVersions', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.ListAppVersionsRequest, output=public_dot_apps__pb2.ListAppVersionsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_app_version(self, request: public_dot_apps__pb2.GetAppVersionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_apps__pb2.GetAppVersionResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetAppVersion', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.GetAppVersionRequest, output=public_dot_apps__pb2.GetAppVersionResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def restore_app_version(self, request: public_dot_apps__pb2.RestoreAppVersionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_apps__pb2.RestoreAppVersionResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RestoreAppVersion', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.RestoreAppVersionRequest, output=public_dot_apps__pb2.RestoreAppVersionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def invoke_app_compute_function(self, request: public_dot_apps__pb2.InvokeAppComputeFunctionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_apps__pb2.InvokeAppComputeFunctionResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='InvokeAppComputeFunction', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.InvokeAppComputeFunctionRequest, output=public_dot_apps__pb2.InvokeAppComputeFunctionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def app_heartbeat(self, request: public_dot_apps__pb2.AppHeartbeatRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='AppHeartbeat', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.AppHeartbeatRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def set_favorite(self, request: public_dot_apps__pb2.SetFavoriteRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_apps__pb2.SetFavoriteResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='SetFavorite', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.SetFavoriteRequest, output=public_dot_apps__pb2.SetFavoriteResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_app_view_stats(self, request: public_dot_apps__pb2.GetAppViewStatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_apps__pb2.GetAppViewStatsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetAppViewStats', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.GetAppViewStatsRequest, output=public_dot_apps__pb2.GetAppViewStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_component_gallery_url(self, request: public_dot_apps__pb2.GetComponentGalleryUrlRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_apps__pb2.GetComponentGalleryUrlResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetComponentGalleryUrl', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.GetComponentGalleryUrlRequest, output=public_dot_apps__pb2.GetComponentGalleryUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_app_member_state(self, request: public_dot_apps__pb2.GetAppMemberStateRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_apps__pb2.GetAppMemberStateResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetAppMemberState', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.GetAppMemberStateRequest, output=public_dot_apps__pb2.GetAppMemberStateResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def set_app_member_state(self, request: public_dot_apps__pb2.SetAppMemberStateRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_apps__pb2.SetAppMemberStateResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='SetAppMemberState', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.SetAppMemberStateRequest, output=public_dot_apps__pb2.SetAppMemberStateResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def record_app_member_activity(self, request: public_dot_apps__pb2.RecordAppMemberActivityRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_apps__pb2.RecordAppMemberActivityResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RecordAppMemberActivity', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.RecordAppMemberActivityRequest, output=public_dot_apps__pb2.RecordAppMemberActivityResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_my_app_member_activity(self, request: public_dot_apps__pb2.ListMyAppMemberActivityRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_apps__pb2.ListMyAppMemberActivityResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListMyAppMemberActivity', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.ListMyAppMemberActivityRequest, output=public_dot_apps__pb2.ListMyAppMemberActivityResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def list_app_activity_since(self, request: public_dot_apps__pb2.ListAppActivitySinceRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_apps__pb2.ListAppActivitySinceResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListAppActivitySince', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.ListAppActivitySinceRequest, output=public_dot_apps__pb2.ListAppActivitySinceResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def stream_app_activity(self, request: public_dot_apps__pb2.StreamAppActivityRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> AsyncIterator[public_dot_apps__pb2.AppActivityStreamEvent]:
        return self.execute_server_stream(request=request, method=MethodInfo(name='StreamAppActivity', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.StreamAppActivityRequest, output=public_dot_apps__pb2.AppActivityStreamEvent, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def presence_heartbeat(self, request: public_dot_apps__pb2.PresenceHeartbeatRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='PresenceHeartbeat', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.PresenceHeartbeatRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

class AppServiceSync(Protocol):

    def create_app(self, request: public_dot_apps__pb2.CreateAppRequest, ctx: RequestContext) -> public_dot_apps__pb2.CreateAppResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def duplicate_app(self, request: public_dot_apps__pb2.DuplicateAppRequest, ctx: RequestContext) -> public_dot_apps__pb2.DuplicateAppResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_app(self, request: public_dot_apps__pb2.GetAppRequest, ctx: RequestContext) -> public_dot_apps__pb2.GetAppResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_apps(self, request: public_dot_apps__pb2.ListAppsRequest, ctx: RequestContext) -> public_dot_apps__pb2.ListAppsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_members_with_apps(self, request: public_dot_apps__pb2.GetMembersWithAppsRequest, ctx: RequestContext) -> public_dot_apps__pb2.GetMembersWithAppsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_app(self, request: public_dot_apps__pb2.UpdateAppRequest, ctx: RequestContext) -> public_dot_apps__pb2.UpdateAppResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_app(self, request: public_dot_apps__pb2.DeleteAppRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def move_app_to_folder(self, request: public_dot_apps__pb2.MoveAppToFolderRequest, ctx: RequestContext) -> public_dot_apps__pb2.MoveAppToFolderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def refresh_app(self, request: public_dot_apps__pb2.RefreshAppRequest, ctx: RequestContext) -> public_dot_apps__pb2.RefreshAppResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_app_versions(self, request: public_dot_apps__pb2.ListAppVersionsRequest, ctx: RequestContext) -> public_dot_apps__pb2.ListAppVersionsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_app_version(self, request: public_dot_apps__pb2.GetAppVersionRequest, ctx: RequestContext) -> public_dot_apps__pb2.GetAppVersionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def restore_app_version(self, request: public_dot_apps__pb2.RestoreAppVersionRequest, ctx: RequestContext) -> public_dot_apps__pb2.RestoreAppVersionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def invoke_app_compute_function(self, request: public_dot_apps__pb2.InvokeAppComputeFunctionRequest, ctx: RequestContext) -> public_dot_apps__pb2.InvokeAppComputeFunctionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def app_heartbeat(self, request: public_dot_apps__pb2.AppHeartbeatRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def set_favorite(self, request: public_dot_apps__pb2.SetFavoriteRequest, ctx: RequestContext) -> public_dot_apps__pb2.SetFavoriteResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_app_view_stats(self, request: public_dot_apps__pb2.GetAppViewStatsRequest, ctx: RequestContext) -> public_dot_apps__pb2.GetAppViewStatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_component_gallery_url(self, request: public_dot_apps__pb2.GetComponentGalleryUrlRequest, ctx: RequestContext) -> public_dot_apps__pb2.GetComponentGalleryUrlResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_app_member_state(self, request: public_dot_apps__pb2.GetAppMemberStateRequest, ctx: RequestContext) -> public_dot_apps__pb2.GetAppMemberStateResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def set_app_member_state(self, request: public_dot_apps__pb2.SetAppMemberStateRequest, ctx: RequestContext) -> public_dot_apps__pb2.SetAppMemberStateResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def record_app_member_activity(self, request: public_dot_apps__pb2.RecordAppMemberActivityRequest, ctx: RequestContext) -> public_dot_apps__pb2.RecordAppMemberActivityResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_my_app_member_activity(self, request: public_dot_apps__pb2.ListMyAppMemberActivityRequest, ctx: RequestContext) -> public_dot_apps__pb2.ListMyAppMemberActivityResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_app_activity_since(self, request: public_dot_apps__pb2.ListAppActivitySinceRequest, ctx: RequestContext) -> public_dot_apps__pb2.ListAppActivitySinceResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def stream_app_activity(self, request: public_dot_apps__pb2.StreamAppActivityRequest, ctx: RequestContext) -> Iterator[public_dot_apps__pb2.AppActivityStreamEvent]:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def presence_heartbeat(self, request: public_dot_apps__pb2.PresenceHeartbeatRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class AppServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: AppServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.app.AppService/CreateApp': EndpointSync.unary(method=MethodInfo(name='CreateApp', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.CreateAppRequest, output=public_dot_apps__pb2.CreateAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_app), '/textql.rpc.public.app.AppService/DuplicateApp': EndpointSync.unary(method=MethodInfo(name='DuplicateApp', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.DuplicateAppRequest, output=public_dot_apps__pb2.DuplicateAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.duplicate_app), '/textql.rpc.public.app.AppService/GetApp': EndpointSync.unary(method=MethodInfo(name='GetApp', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.GetAppRequest, output=public_dot_apps__pb2.GetAppResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_app), '/textql.rpc.public.app.AppService/ListApps': EndpointSync.unary(method=MethodInfo(name='ListApps', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.ListAppsRequest, output=public_dot_apps__pb2.ListAppsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_apps), '/textql.rpc.public.app.AppService/GetMembersWithApps': EndpointSync.unary(method=MethodInfo(name='GetMembersWithApps', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.GetMembersWithAppsRequest, output=public_dot_apps__pb2.GetMembersWithAppsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_members_with_apps), '/textql.rpc.public.app.AppService/UpdateApp': EndpointSync.unary(method=MethodInfo(name='UpdateApp', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.UpdateAppRequest, output=public_dot_apps__pb2.UpdateAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_app), '/textql.rpc.public.app.AppService/DeleteApp': EndpointSync.unary(method=MethodInfo(name='DeleteApp', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.DeleteAppRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_app), '/textql.rpc.public.app.AppService/MoveAppToFolder': EndpointSync.unary(method=MethodInfo(name='MoveAppToFolder', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.MoveAppToFolderRequest, output=public_dot_apps__pb2.MoveAppToFolderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.move_app_to_folder), '/textql.rpc.public.app.AppService/RefreshApp': EndpointSync.unary(method=MethodInfo(name='RefreshApp', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.RefreshAppRequest, output=public_dot_apps__pb2.RefreshAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.refresh_app), '/textql.rpc.public.app.AppService/ListAppVersions': EndpointSync.unary(method=MethodInfo(name='ListAppVersions', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.ListAppVersionsRequest, output=public_dot_apps__pb2.ListAppVersionsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_app_versions), '/textql.rpc.public.app.AppService/GetAppVersion': EndpointSync.unary(method=MethodInfo(name='GetAppVersion', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.GetAppVersionRequest, output=public_dot_apps__pb2.GetAppVersionResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_app_version), '/textql.rpc.public.app.AppService/RestoreAppVersion': EndpointSync.unary(method=MethodInfo(name='RestoreAppVersion', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.RestoreAppVersionRequest, output=public_dot_apps__pb2.RestoreAppVersionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.restore_app_version), '/textql.rpc.public.app.AppService/InvokeAppComputeFunction': EndpointSync.unary(method=MethodInfo(name='InvokeAppComputeFunction', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.InvokeAppComputeFunctionRequest, output=public_dot_apps__pb2.InvokeAppComputeFunctionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.invoke_app_compute_function), '/textql.rpc.public.app.AppService/AppHeartbeat': EndpointSync.unary(method=MethodInfo(name='AppHeartbeat', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.AppHeartbeatRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.app_heartbeat), '/textql.rpc.public.app.AppService/SetFavorite': EndpointSync.unary(method=MethodInfo(name='SetFavorite', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.SetFavoriteRequest, output=public_dot_apps__pb2.SetFavoriteResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.set_favorite), '/textql.rpc.public.app.AppService/GetAppViewStats': EndpointSync.unary(method=MethodInfo(name='GetAppViewStats', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.GetAppViewStatsRequest, output=public_dot_apps__pb2.GetAppViewStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_app_view_stats), '/textql.rpc.public.app.AppService/GetComponentGalleryUrl': EndpointSync.unary(method=MethodInfo(name='GetComponentGalleryUrl', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.GetComponentGalleryUrlRequest, output=public_dot_apps__pb2.GetComponentGalleryUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_component_gallery_url), '/textql.rpc.public.app.AppService/GetAppMemberState': EndpointSync.unary(method=MethodInfo(name='GetAppMemberState', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.GetAppMemberStateRequest, output=public_dot_apps__pb2.GetAppMemberStateResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_app_member_state), '/textql.rpc.public.app.AppService/SetAppMemberState': EndpointSync.unary(method=MethodInfo(name='SetAppMemberState', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.SetAppMemberStateRequest, output=public_dot_apps__pb2.SetAppMemberStateResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.set_app_member_state), '/textql.rpc.public.app.AppService/RecordAppMemberActivity': EndpointSync.unary(method=MethodInfo(name='RecordAppMemberActivity', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.RecordAppMemberActivityRequest, output=public_dot_apps__pb2.RecordAppMemberActivityResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.record_app_member_activity), '/textql.rpc.public.app.AppService/ListMyAppMemberActivity': EndpointSync.unary(method=MethodInfo(name='ListMyAppMemberActivity', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.ListMyAppMemberActivityRequest, output=public_dot_apps__pb2.ListMyAppMemberActivityResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_my_app_member_activity), '/textql.rpc.public.app.AppService/ListAppActivitySince': EndpointSync.unary(method=MethodInfo(name='ListAppActivitySince', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.ListAppActivitySinceRequest, output=public_dot_apps__pb2.ListAppActivitySinceResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_app_activity_since), '/textql.rpc.public.app.AppService/StreamAppActivity': EndpointSync.server_stream(method=MethodInfo(name='StreamAppActivity', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.StreamAppActivityRequest, output=public_dot_apps__pb2.AppActivityStreamEvent, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.stream_app_activity), '/textql.rpc.public.app.AppService/PresenceHeartbeat': EndpointSync.unary(method=MethodInfo(name='PresenceHeartbeat', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.PresenceHeartbeatRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.presence_heartbeat)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.app.AppService'

class AppServiceClientSync(ConnectClientSync):

    def create_app(self, request: public_dot_apps__pb2.CreateAppRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_apps__pb2.CreateAppResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateApp', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.CreateAppRequest, output=public_dot_apps__pb2.CreateAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def duplicate_app(self, request: public_dot_apps__pb2.DuplicateAppRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_apps__pb2.DuplicateAppResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DuplicateApp', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.DuplicateAppRequest, output=public_dot_apps__pb2.DuplicateAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_app(self, request: public_dot_apps__pb2.GetAppRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_apps__pb2.GetAppResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetApp', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.GetAppRequest, output=public_dot_apps__pb2.GetAppResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def list_apps(self, request: public_dot_apps__pb2.ListAppsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_apps__pb2.ListAppsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListApps', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.ListAppsRequest, output=public_dot_apps__pb2.ListAppsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_members_with_apps(self, request: public_dot_apps__pb2.GetMembersWithAppsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_apps__pb2.GetMembersWithAppsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetMembersWithApps', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.GetMembersWithAppsRequest, output=public_dot_apps__pb2.GetMembersWithAppsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def update_app(self, request: public_dot_apps__pb2.UpdateAppRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_apps__pb2.UpdateAppResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateApp', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.UpdateAppRequest, output=public_dot_apps__pb2.UpdateAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def delete_app(self, request: public_dot_apps__pb2.DeleteAppRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteApp', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.DeleteAppRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def move_app_to_folder(self, request: public_dot_apps__pb2.MoveAppToFolderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_apps__pb2.MoveAppToFolderResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='MoveAppToFolder', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.MoveAppToFolderRequest, output=public_dot_apps__pb2.MoveAppToFolderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def refresh_app(self, request: public_dot_apps__pb2.RefreshAppRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_apps__pb2.RefreshAppResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RefreshApp', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.RefreshAppRequest, output=public_dot_apps__pb2.RefreshAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_app_versions(self, request: public_dot_apps__pb2.ListAppVersionsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_apps__pb2.ListAppVersionsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListAppVersions', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.ListAppVersionsRequest, output=public_dot_apps__pb2.ListAppVersionsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_app_version(self, request: public_dot_apps__pb2.GetAppVersionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_apps__pb2.GetAppVersionResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetAppVersion', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.GetAppVersionRequest, output=public_dot_apps__pb2.GetAppVersionResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def restore_app_version(self, request: public_dot_apps__pb2.RestoreAppVersionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_apps__pb2.RestoreAppVersionResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RestoreAppVersion', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.RestoreAppVersionRequest, output=public_dot_apps__pb2.RestoreAppVersionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def invoke_app_compute_function(self, request: public_dot_apps__pb2.InvokeAppComputeFunctionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_apps__pb2.InvokeAppComputeFunctionResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='InvokeAppComputeFunction', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.InvokeAppComputeFunctionRequest, output=public_dot_apps__pb2.InvokeAppComputeFunctionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def app_heartbeat(self, request: public_dot_apps__pb2.AppHeartbeatRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='AppHeartbeat', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.AppHeartbeatRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def set_favorite(self, request: public_dot_apps__pb2.SetFavoriteRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_apps__pb2.SetFavoriteResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='SetFavorite', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.SetFavoriteRequest, output=public_dot_apps__pb2.SetFavoriteResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_app_view_stats(self, request: public_dot_apps__pb2.GetAppViewStatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_apps__pb2.GetAppViewStatsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetAppViewStats', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.GetAppViewStatsRequest, output=public_dot_apps__pb2.GetAppViewStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_component_gallery_url(self, request: public_dot_apps__pb2.GetComponentGalleryUrlRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_apps__pb2.GetComponentGalleryUrlResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetComponentGalleryUrl', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.GetComponentGalleryUrlRequest, output=public_dot_apps__pb2.GetComponentGalleryUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_app_member_state(self, request: public_dot_apps__pb2.GetAppMemberStateRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_apps__pb2.GetAppMemberStateResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetAppMemberState', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.GetAppMemberStateRequest, output=public_dot_apps__pb2.GetAppMemberStateResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def set_app_member_state(self, request: public_dot_apps__pb2.SetAppMemberStateRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_apps__pb2.SetAppMemberStateResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='SetAppMemberState', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.SetAppMemberStateRequest, output=public_dot_apps__pb2.SetAppMemberStateResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def record_app_member_activity(self, request: public_dot_apps__pb2.RecordAppMemberActivityRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_apps__pb2.RecordAppMemberActivityResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RecordAppMemberActivity', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.RecordAppMemberActivityRequest, output=public_dot_apps__pb2.RecordAppMemberActivityResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_my_app_member_activity(self, request: public_dot_apps__pb2.ListMyAppMemberActivityRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_apps__pb2.ListMyAppMemberActivityResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListMyAppMemberActivity', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.ListMyAppMemberActivityRequest, output=public_dot_apps__pb2.ListMyAppMemberActivityResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def list_app_activity_since(self, request: public_dot_apps__pb2.ListAppActivitySinceRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_apps__pb2.ListAppActivitySinceResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListAppActivitySince', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.ListAppActivitySinceRequest, output=public_dot_apps__pb2.ListAppActivitySinceResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def stream_app_activity(self, request: public_dot_apps__pb2.StreamAppActivityRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> Iterator[public_dot_apps__pb2.AppActivityStreamEvent]:
        return self.execute_server_stream(request=request, method=MethodInfo(name='StreamAppActivity', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.StreamAppActivityRequest, output=public_dot_apps__pb2.AppActivityStreamEvent, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def presence_heartbeat(self, request: public_dot_apps__pb2.PresenceHeartbeatRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='PresenceHeartbeat', service_name='textql.rpc.public.app.AppService', input=public_dot_apps__pb2.PresenceHeartbeatRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)