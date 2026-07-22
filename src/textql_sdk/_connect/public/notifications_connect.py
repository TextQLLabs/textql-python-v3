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
from . import notifications_pb2 as public_dot_notifications__pb2

class NotificationService(Protocol):

    async def get_notifications(self, request: public_dot_notifications__pb2.GetNotificationsRequest, ctx: RequestContext) -> public_dot_notifications__pb2.GetNotificationsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def mark_notification_read(self, request: public_dot_notifications__pb2.MarkNotificationReadRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def mark_all_notifications_read(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def stream_notifications(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> AsyncIterator[public_dot_notifications__pb2.NotificationEvent]:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_notification_rules(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_notifications__pb2.GetNotificationRulesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def upsert_notification_rule(self, request: public_dot_notifications__pb2.UpsertNotificationRuleRequest, ctx: RequestContext) -> public_dot_notifications__pb2.NotificationRule:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class NotificationServiceASGIApplication(ConnectASGIApplication[NotificationService]):

    def __init__(self, service: NotificationService | AsyncGenerator[NotificationService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.notifications.NotificationService/GetNotifications': Endpoint.unary(method=MethodInfo(name='GetNotifications', service_name='textql.rpc.public.notifications.NotificationService', input=public_dot_notifications__pb2.GetNotificationsRequest, output=public_dot_notifications__pb2.GetNotificationsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_notifications), '/textql.rpc.public.notifications.NotificationService/MarkNotificationRead': Endpoint.unary(method=MethodInfo(name='MarkNotificationRead', service_name='textql.rpc.public.notifications.NotificationService', input=public_dot_notifications__pb2.MarkNotificationReadRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.mark_notification_read), '/textql.rpc.public.notifications.NotificationService/MarkAllNotificationsRead': Endpoint.unary(method=MethodInfo(name='MarkAllNotificationsRead', service_name='textql.rpc.public.notifications.NotificationService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.mark_all_notifications_read), '/textql.rpc.public.notifications.NotificationService/StreamNotifications': Endpoint.server_stream(method=MethodInfo(name='StreamNotifications', service_name='textql.rpc.public.notifications.NotificationService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_notifications__pb2.NotificationEvent, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.stream_notifications), '/textql.rpc.public.notifications.NotificationService/GetNotificationRules': Endpoint.unary(method=MethodInfo(name='GetNotificationRules', service_name='textql.rpc.public.notifications.NotificationService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_notifications__pb2.GetNotificationRulesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_notification_rules), '/textql.rpc.public.notifications.NotificationService/UpsertNotificationRule': Endpoint.unary(method=MethodInfo(name='UpsertNotificationRule', service_name='textql.rpc.public.notifications.NotificationService', input=public_dot_notifications__pb2.UpsertNotificationRuleRequest, output=public_dot_notifications__pb2.NotificationRule, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.upsert_notification_rule)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.notifications.NotificationService'

class NotificationServiceClient(ConnectClient):

    async def get_notifications(self, request: public_dot_notifications__pb2.GetNotificationsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_notifications__pb2.GetNotificationsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetNotifications', service_name='textql.rpc.public.notifications.NotificationService', input=public_dot_notifications__pb2.GetNotificationsRequest, output=public_dot_notifications__pb2.GetNotificationsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def mark_notification_read(self, request: public_dot_notifications__pb2.MarkNotificationReadRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='MarkNotificationRead', service_name='textql.rpc.public.notifications.NotificationService', input=public_dot_notifications__pb2.MarkNotificationReadRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def mark_all_notifications_read(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='MarkAllNotificationsRead', service_name='textql.rpc.public.notifications.NotificationService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def stream_notifications(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> AsyncIterator[public_dot_notifications__pb2.NotificationEvent]:
        return self.execute_server_stream(request=request, method=MethodInfo(name='StreamNotifications', service_name='textql.rpc.public.notifications.NotificationService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_notifications__pb2.NotificationEvent, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_notification_rules(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_notifications__pb2.GetNotificationRulesResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetNotificationRules', service_name='textql.rpc.public.notifications.NotificationService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_notifications__pb2.GetNotificationRulesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def upsert_notification_rule(self, request: public_dot_notifications__pb2.UpsertNotificationRuleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_notifications__pb2.NotificationRule:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpsertNotificationRule', service_name='textql.rpc.public.notifications.NotificationService', input=public_dot_notifications__pb2.UpsertNotificationRuleRequest, output=public_dot_notifications__pb2.NotificationRule, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class SystemAlertService(Protocol):

    async def create_broadcast(self, request: public_dot_notifications__pb2.CreateBroadcastRequest, ctx: RequestContext) -> public_dot_notifications__pb2.Broadcast:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_broadcasts(self, request: public_dot_notifications__pb2.ListBroadcastsRequest, ctx: RequestContext) -> public_dot_notifications__pb2.ListBroadcastsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def cancel_broadcast(self, request: public_dot_notifications__pb2.CancelBroadcastRequest, ctx: RequestContext) -> public_dot_notifications__pb2.Broadcast:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_broadcast(self, request: public_dot_notifications__pb2.UpdateBroadcastRequest, ctx: RequestContext) -> public_dot_notifications__pb2.Broadcast:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class SystemAlertServiceASGIApplication(ConnectASGIApplication[SystemAlertService]):

    def __init__(self, service: SystemAlertService | AsyncGenerator[SystemAlertService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.notifications.SystemAlertService/CreateBroadcast': Endpoint.unary(method=MethodInfo(name='CreateBroadcast', service_name='textql.rpc.public.notifications.SystemAlertService', input=public_dot_notifications__pb2.CreateBroadcastRequest, output=public_dot_notifications__pb2.Broadcast, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_broadcast), '/textql.rpc.public.notifications.SystemAlertService/ListBroadcasts': Endpoint.unary(method=MethodInfo(name='ListBroadcasts', service_name='textql.rpc.public.notifications.SystemAlertService', input=public_dot_notifications__pb2.ListBroadcastsRequest, output=public_dot_notifications__pb2.ListBroadcastsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_broadcasts), '/textql.rpc.public.notifications.SystemAlertService/CancelBroadcast': Endpoint.unary(method=MethodInfo(name='CancelBroadcast', service_name='textql.rpc.public.notifications.SystemAlertService', input=public_dot_notifications__pb2.CancelBroadcastRequest, output=public_dot_notifications__pb2.Broadcast, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.cancel_broadcast), '/textql.rpc.public.notifications.SystemAlertService/UpdateBroadcast': Endpoint.unary(method=MethodInfo(name='UpdateBroadcast', service_name='textql.rpc.public.notifications.SystemAlertService', input=public_dot_notifications__pb2.UpdateBroadcastRequest, output=public_dot_notifications__pb2.Broadcast, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_broadcast)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.notifications.SystemAlertService'

class SystemAlertServiceClient(ConnectClient):

    async def create_broadcast(self, request: public_dot_notifications__pb2.CreateBroadcastRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_notifications__pb2.Broadcast:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateBroadcast', service_name='textql.rpc.public.notifications.SystemAlertService', input=public_dot_notifications__pb2.CreateBroadcastRequest, output=public_dot_notifications__pb2.Broadcast, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_broadcasts(self, request: public_dot_notifications__pb2.ListBroadcastsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_notifications__pb2.ListBroadcastsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListBroadcasts', service_name='textql.rpc.public.notifications.SystemAlertService', input=public_dot_notifications__pb2.ListBroadcastsRequest, output=public_dot_notifications__pb2.ListBroadcastsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def cancel_broadcast(self, request: public_dot_notifications__pb2.CancelBroadcastRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_notifications__pb2.Broadcast:
        return await self.execute_unary(request=request, method=MethodInfo(name='CancelBroadcast', service_name='textql.rpc.public.notifications.SystemAlertService', input=public_dot_notifications__pb2.CancelBroadcastRequest, output=public_dot_notifications__pb2.Broadcast, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def update_broadcast(self, request: public_dot_notifications__pb2.UpdateBroadcastRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_notifications__pb2.Broadcast:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateBroadcast', service_name='textql.rpc.public.notifications.SystemAlertService', input=public_dot_notifications__pb2.UpdateBroadcastRequest, output=public_dot_notifications__pb2.Broadcast, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class NotificationServiceSync(Protocol):

    def get_notifications(self, request: public_dot_notifications__pb2.GetNotificationsRequest, ctx: RequestContext) -> public_dot_notifications__pb2.GetNotificationsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def mark_notification_read(self, request: public_dot_notifications__pb2.MarkNotificationReadRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def mark_all_notifications_read(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def stream_notifications(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> Iterator[public_dot_notifications__pb2.NotificationEvent]:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_notification_rules(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_notifications__pb2.GetNotificationRulesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def upsert_notification_rule(self, request: public_dot_notifications__pb2.UpsertNotificationRuleRequest, ctx: RequestContext) -> public_dot_notifications__pb2.NotificationRule:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class NotificationServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: NotificationServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.notifications.NotificationService/GetNotifications': EndpointSync.unary(method=MethodInfo(name='GetNotifications', service_name='textql.rpc.public.notifications.NotificationService', input=public_dot_notifications__pb2.GetNotificationsRequest, output=public_dot_notifications__pb2.GetNotificationsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_notifications), '/textql.rpc.public.notifications.NotificationService/MarkNotificationRead': EndpointSync.unary(method=MethodInfo(name='MarkNotificationRead', service_name='textql.rpc.public.notifications.NotificationService', input=public_dot_notifications__pb2.MarkNotificationReadRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.mark_notification_read), '/textql.rpc.public.notifications.NotificationService/MarkAllNotificationsRead': EndpointSync.unary(method=MethodInfo(name='MarkAllNotificationsRead', service_name='textql.rpc.public.notifications.NotificationService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.mark_all_notifications_read), '/textql.rpc.public.notifications.NotificationService/StreamNotifications': EndpointSync.server_stream(method=MethodInfo(name='StreamNotifications', service_name='textql.rpc.public.notifications.NotificationService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_notifications__pb2.NotificationEvent, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.stream_notifications), '/textql.rpc.public.notifications.NotificationService/GetNotificationRules': EndpointSync.unary(method=MethodInfo(name='GetNotificationRules', service_name='textql.rpc.public.notifications.NotificationService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_notifications__pb2.GetNotificationRulesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_notification_rules), '/textql.rpc.public.notifications.NotificationService/UpsertNotificationRule': EndpointSync.unary(method=MethodInfo(name='UpsertNotificationRule', service_name='textql.rpc.public.notifications.NotificationService', input=public_dot_notifications__pb2.UpsertNotificationRuleRequest, output=public_dot_notifications__pb2.NotificationRule, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.upsert_notification_rule)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.notifications.NotificationService'

class NotificationServiceClientSync(ConnectClientSync):

    def get_notifications(self, request: public_dot_notifications__pb2.GetNotificationsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_notifications__pb2.GetNotificationsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetNotifications', service_name='textql.rpc.public.notifications.NotificationService', input=public_dot_notifications__pb2.GetNotificationsRequest, output=public_dot_notifications__pb2.GetNotificationsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def mark_notification_read(self, request: public_dot_notifications__pb2.MarkNotificationReadRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='MarkNotificationRead', service_name='textql.rpc.public.notifications.NotificationService', input=public_dot_notifications__pb2.MarkNotificationReadRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def mark_all_notifications_read(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='MarkAllNotificationsRead', service_name='textql.rpc.public.notifications.NotificationService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def stream_notifications(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> Iterator[public_dot_notifications__pb2.NotificationEvent]:
        return self.execute_server_stream(request=request, method=MethodInfo(name='StreamNotifications', service_name='textql.rpc.public.notifications.NotificationService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_notifications__pb2.NotificationEvent, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_notification_rules(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_notifications__pb2.GetNotificationRulesResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetNotificationRules', service_name='textql.rpc.public.notifications.NotificationService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_notifications__pb2.GetNotificationRulesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def upsert_notification_rule(self, request: public_dot_notifications__pb2.UpsertNotificationRuleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_notifications__pb2.NotificationRule:
        return self.execute_unary(request=request, method=MethodInfo(name='UpsertNotificationRule', service_name='textql.rpc.public.notifications.NotificationService', input=public_dot_notifications__pb2.UpsertNotificationRuleRequest, output=public_dot_notifications__pb2.NotificationRule, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class SystemAlertServiceSync(Protocol):

    def create_broadcast(self, request: public_dot_notifications__pb2.CreateBroadcastRequest, ctx: RequestContext) -> public_dot_notifications__pb2.Broadcast:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_broadcasts(self, request: public_dot_notifications__pb2.ListBroadcastsRequest, ctx: RequestContext) -> public_dot_notifications__pb2.ListBroadcastsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def cancel_broadcast(self, request: public_dot_notifications__pb2.CancelBroadcastRequest, ctx: RequestContext) -> public_dot_notifications__pb2.Broadcast:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_broadcast(self, request: public_dot_notifications__pb2.UpdateBroadcastRequest, ctx: RequestContext) -> public_dot_notifications__pb2.Broadcast:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class SystemAlertServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: SystemAlertServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.notifications.SystemAlertService/CreateBroadcast': EndpointSync.unary(method=MethodInfo(name='CreateBroadcast', service_name='textql.rpc.public.notifications.SystemAlertService', input=public_dot_notifications__pb2.CreateBroadcastRequest, output=public_dot_notifications__pb2.Broadcast, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_broadcast), '/textql.rpc.public.notifications.SystemAlertService/ListBroadcasts': EndpointSync.unary(method=MethodInfo(name='ListBroadcasts', service_name='textql.rpc.public.notifications.SystemAlertService', input=public_dot_notifications__pb2.ListBroadcastsRequest, output=public_dot_notifications__pb2.ListBroadcastsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_broadcasts), '/textql.rpc.public.notifications.SystemAlertService/CancelBroadcast': EndpointSync.unary(method=MethodInfo(name='CancelBroadcast', service_name='textql.rpc.public.notifications.SystemAlertService', input=public_dot_notifications__pb2.CancelBroadcastRequest, output=public_dot_notifications__pb2.Broadcast, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.cancel_broadcast), '/textql.rpc.public.notifications.SystemAlertService/UpdateBroadcast': EndpointSync.unary(method=MethodInfo(name='UpdateBroadcast', service_name='textql.rpc.public.notifications.SystemAlertService', input=public_dot_notifications__pb2.UpdateBroadcastRequest, output=public_dot_notifications__pb2.Broadcast, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_broadcast)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.notifications.SystemAlertService'

class SystemAlertServiceClientSync(ConnectClientSync):

    def create_broadcast(self, request: public_dot_notifications__pb2.CreateBroadcastRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_notifications__pb2.Broadcast:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateBroadcast', service_name='textql.rpc.public.notifications.SystemAlertService', input=public_dot_notifications__pb2.CreateBroadcastRequest, output=public_dot_notifications__pb2.Broadcast, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_broadcasts(self, request: public_dot_notifications__pb2.ListBroadcastsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_notifications__pb2.ListBroadcastsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListBroadcasts', service_name='textql.rpc.public.notifications.SystemAlertService', input=public_dot_notifications__pb2.ListBroadcastsRequest, output=public_dot_notifications__pb2.ListBroadcastsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def cancel_broadcast(self, request: public_dot_notifications__pb2.CancelBroadcastRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_notifications__pb2.Broadcast:
        return self.execute_unary(request=request, method=MethodInfo(name='CancelBroadcast', service_name='textql.rpc.public.notifications.SystemAlertService', input=public_dot_notifications__pb2.CancelBroadcastRequest, output=public_dot_notifications__pb2.Broadcast, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def update_broadcast(self, request: public_dot_notifications__pb2.UpdateBroadcastRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_notifications__pb2.Broadcast:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateBroadcast', service_name='textql.rpc.public.notifications.SystemAlertService', input=public_dot_notifications__pb2.UpdateBroadcastRequest, output=public_dot_notifications__pb2.Broadcast, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)