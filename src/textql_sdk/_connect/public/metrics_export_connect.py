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
from . import metrics_export_pb2 as public_dot_metrics__export__pb2

class MetricsExportService(Protocol):

    async def configure_metrics_export(self, request: public_dot_metrics__export__pb2.ConfigureMetricsExportRequest, ctx: RequestContext) -> public_dot_metrics__export__pb2.ConfigureMetricsExportResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_metrics_export_config(self, request: public_dot_metrics__export__pb2.GetMetricsExportConfigRequest, ctx: RequestContext) -> public_dot_metrics__export__pb2.GetMetricsExportConfigResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_metrics_export_config(self, request: public_dot_metrics__export__pb2.DeleteMetricsExportConfigRequest, ctx: RequestContext) -> public_dot_metrics__export__pb2.DeleteMetricsExportConfigResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def test_metrics_export_connection(self, request: public_dot_metrics__export__pb2.TestMetricsExportConnectionRequest, ctx: RequestContext) -> public_dot_metrics__export__pb2.TestMetricsExportConnectionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def trigger_metrics_push(self, request: public_dot_metrics__export__pb2.TriggerMetricsPushRequest, ctx: RequestContext) -> public_dot_metrics__export__pb2.TriggerMetricsPushResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class MetricsExportServiceASGIApplication(ConnectASGIApplication[MetricsExportService]):

    def __init__(self, service: MetricsExportService | AsyncGenerator[MetricsExportService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.metrics_export.MetricsExportService/ConfigureMetricsExport': Endpoint.unary(method=MethodInfo(name='ConfigureMetricsExport', service_name='textql.rpc.public.metrics_export.MetricsExportService', input=public_dot_metrics__export__pb2.ConfigureMetricsExportRequest, output=public_dot_metrics__export__pb2.ConfigureMetricsExportResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.configure_metrics_export), '/textql.rpc.public.metrics_export.MetricsExportService/GetMetricsExportConfig': Endpoint.unary(method=MethodInfo(name='GetMetricsExportConfig', service_name='textql.rpc.public.metrics_export.MetricsExportService', input=public_dot_metrics__export__pb2.GetMetricsExportConfigRequest, output=public_dot_metrics__export__pb2.GetMetricsExportConfigResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_metrics_export_config), '/textql.rpc.public.metrics_export.MetricsExportService/DeleteMetricsExportConfig': Endpoint.unary(method=MethodInfo(name='DeleteMetricsExportConfig', service_name='textql.rpc.public.metrics_export.MetricsExportService', input=public_dot_metrics__export__pb2.DeleteMetricsExportConfigRequest, output=public_dot_metrics__export__pb2.DeleteMetricsExportConfigResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_metrics_export_config), '/textql.rpc.public.metrics_export.MetricsExportService/TestMetricsExportConnection': Endpoint.unary(method=MethodInfo(name='TestMetricsExportConnection', service_name='textql.rpc.public.metrics_export.MetricsExportService', input=public_dot_metrics__export__pb2.TestMetricsExportConnectionRequest, output=public_dot_metrics__export__pb2.TestMetricsExportConnectionResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.test_metrics_export_connection), '/textql.rpc.public.metrics_export.MetricsExportService/TriggerMetricsPush': Endpoint.unary(method=MethodInfo(name='TriggerMetricsPush', service_name='textql.rpc.public.metrics_export.MetricsExportService', input=public_dot_metrics__export__pb2.TriggerMetricsPushRequest, output=public_dot_metrics__export__pb2.TriggerMetricsPushResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.trigger_metrics_push)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.metrics_export.MetricsExportService'

class MetricsExportServiceClient(ConnectClient):

    async def configure_metrics_export(self, request: public_dot_metrics__export__pb2.ConfigureMetricsExportRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_metrics__export__pb2.ConfigureMetricsExportResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ConfigureMetricsExport', service_name='textql.rpc.public.metrics_export.MetricsExportService', input=public_dot_metrics__export__pb2.ConfigureMetricsExportRequest, output=public_dot_metrics__export__pb2.ConfigureMetricsExportResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_metrics_export_config(self, request: public_dot_metrics__export__pb2.GetMetricsExportConfigRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_metrics__export__pb2.GetMetricsExportConfigResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetMetricsExportConfig', service_name='textql.rpc.public.metrics_export.MetricsExportService', input=public_dot_metrics__export__pb2.GetMetricsExportConfigRequest, output=public_dot_metrics__export__pb2.GetMetricsExportConfigResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def delete_metrics_export_config(self, request: public_dot_metrics__export__pb2.DeleteMetricsExportConfigRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_metrics__export__pb2.DeleteMetricsExportConfigResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteMetricsExportConfig', service_name='textql.rpc.public.metrics_export.MetricsExportService', input=public_dot_metrics__export__pb2.DeleteMetricsExportConfigRequest, output=public_dot_metrics__export__pb2.DeleteMetricsExportConfigResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def test_metrics_export_connection(self, request: public_dot_metrics__export__pb2.TestMetricsExportConnectionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_metrics__export__pb2.TestMetricsExportConnectionResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='TestMetricsExportConnection', service_name='textql.rpc.public.metrics_export.MetricsExportService', input=public_dot_metrics__export__pb2.TestMetricsExportConnectionRequest, output=public_dot_metrics__export__pb2.TestMetricsExportConnectionResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def trigger_metrics_push(self, request: public_dot_metrics__export__pb2.TriggerMetricsPushRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_metrics__export__pb2.TriggerMetricsPushResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='TriggerMetricsPush', service_name='textql.rpc.public.metrics_export.MetricsExportService', input=public_dot_metrics__export__pb2.TriggerMetricsPushRequest, output=public_dot_metrics__export__pb2.TriggerMetricsPushResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class MetricsExportServiceSync(Protocol):

    def configure_metrics_export(self, request: public_dot_metrics__export__pb2.ConfigureMetricsExportRequest, ctx: RequestContext) -> public_dot_metrics__export__pb2.ConfigureMetricsExportResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_metrics_export_config(self, request: public_dot_metrics__export__pb2.GetMetricsExportConfigRequest, ctx: RequestContext) -> public_dot_metrics__export__pb2.GetMetricsExportConfigResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_metrics_export_config(self, request: public_dot_metrics__export__pb2.DeleteMetricsExportConfigRequest, ctx: RequestContext) -> public_dot_metrics__export__pb2.DeleteMetricsExportConfigResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def test_metrics_export_connection(self, request: public_dot_metrics__export__pb2.TestMetricsExportConnectionRequest, ctx: RequestContext) -> public_dot_metrics__export__pb2.TestMetricsExportConnectionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def trigger_metrics_push(self, request: public_dot_metrics__export__pb2.TriggerMetricsPushRequest, ctx: RequestContext) -> public_dot_metrics__export__pb2.TriggerMetricsPushResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class MetricsExportServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: MetricsExportServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.metrics_export.MetricsExportService/ConfigureMetricsExport': EndpointSync.unary(method=MethodInfo(name='ConfigureMetricsExport', service_name='textql.rpc.public.metrics_export.MetricsExportService', input=public_dot_metrics__export__pb2.ConfigureMetricsExportRequest, output=public_dot_metrics__export__pb2.ConfigureMetricsExportResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.configure_metrics_export), '/textql.rpc.public.metrics_export.MetricsExportService/GetMetricsExportConfig': EndpointSync.unary(method=MethodInfo(name='GetMetricsExportConfig', service_name='textql.rpc.public.metrics_export.MetricsExportService', input=public_dot_metrics__export__pb2.GetMetricsExportConfigRequest, output=public_dot_metrics__export__pb2.GetMetricsExportConfigResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_metrics_export_config), '/textql.rpc.public.metrics_export.MetricsExportService/DeleteMetricsExportConfig': EndpointSync.unary(method=MethodInfo(name='DeleteMetricsExportConfig', service_name='textql.rpc.public.metrics_export.MetricsExportService', input=public_dot_metrics__export__pb2.DeleteMetricsExportConfigRequest, output=public_dot_metrics__export__pb2.DeleteMetricsExportConfigResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_metrics_export_config), '/textql.rpc.public.metrics_export.MetricsExportService/TestMetricsExportConnection': EndpointSync.unary(method=MethodInfo(name='TestMetricsExportConnection', service_name='textql.rpc.public.metrics_export.MetricsExportService', input=public_dot_metrics__export__pb2.TestMetricsExportConnectionRequest, output=public_dot_metrics__export__pb2.TestMetricsExportConnectionResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.test_metrics_export_connection), '/textql.rpc.public.metrics_export.MetricsExportService/TriggerMetricsPush': EndpointSync.unary(method=MethodInfo(name='TriggerMetricsPush', service_name='textql.rpc.public.metrics_export.MetricsExportService', input=public_dot_metrics__export__pb2.TriggerMetricsPushRequest, output=public_dot_metrics__export__pb2.TriggerMetricsPushResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.trigger_metrics_push)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.metrics_export.MetricsExportService'

class MetricsExportServiceClientSync(ConnectClientSync):

    def configure_metrics_export(self, request: public_dot_metrics__export__pb2.ConfigureMetricsExportRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_metrics__export__pb2.ConfigureMetricsExportResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ConfigureMetricsExport', service_name='textql.rpc.public.metrics_export.MetricsExportService', input=public_dot_metrics__export__pb2.ConfigureMetricsExportRequest, output=public_dot_metrics__export__pb2.ConfigureMetricsExportResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_metrics_export_config(self, request: public_dot_metrics__export__pb2.GetMetricsExportConfigRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_metrics__export__pb2.GetMetricsExportConfigResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetMetricsExportConfig', service_name='textql.rpc.public.metrics_export.MetricsExportService', input=public_dot_metrics__export__pb2.GetMetricsExportConfigRequest, output=public_dot_metrics__export__pb2.GetMetricsExportConfigResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def delete_metrics_export_config(self, request: public_dot_metrics__export__pb2.DeleteMetricsExportConfigRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_metrics__export__pb2.DeleteMetricsExportConfigResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteMetricsExportConfig', service_name='textql.rpc.public.metrics_export.MetricsExportService', input=public_dot_metrics__export__pb2.DeleteMetricsExportConfigRequest, output=public_dot_metrics__export__pb2.DeleteMetricsExportConfigResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def test_metrics_export_connection(self, request: public_dot_metrics__export__pb2.TestMetricsExportConnectionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_metrics__export__pb2.TestMetricsExportConnectionResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='TestMetricsExportConnection', service_name='textql.rpc.public.metrics_export.MetricsExportService', input=public_dot_metrics__export__pb2.TestMetricsExportConnectionRequest, output=public_dot_metrics__export__pb2.TestMetricsExportConnectionResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def trigger_metrics_push(self, request: public_dot_metrics__export__pb2.TriggerMetricsPushRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_metrics__export__pb2.TriggerMetricsPushResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='TriggerMetricsPush', service_name='textql.rpc.public.metrics_export.MetricsExportService', input=public_dot_metrics__export__pb2.TriggerMetricsPushRequest, output=public_dot_metrics__export__pb2.TriggerMetricsPushResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)