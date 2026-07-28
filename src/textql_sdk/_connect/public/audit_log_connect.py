# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
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
from . import audit_log_pb2 as public_dot_audit__log__pb2

class AuditLogService(Protocol):

    async def list_audit_logs(self, request: public_dot_audit__log__pb2.ListAuditLogsRequest, ctx: RequestContext) -> public_dot_audit__log__pb2.ListAuditLogsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def configure_s3_export(self, request: public_dot_audit__log__pb2.ConfigureS3ExportRequest, ctx: RequestContext) -> public_dot_audit__log__pb2.ConfigureS3ExportResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_s3_export_config(self, request: public_dot_audit__log__pb2.GetS3ExportConfigRequest, ctx: RequestContext) -> public_dot_audit__log__pb2.GetS3ExportConfigResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_s3_export_config(self, request: public_dot_audit__log__pb2.DeleteS3ExportConfigRequest, ctx: RequestContext) -> public_dot_audit__log__pb2.DeleteS3ExportConfigResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def test_s3_export_connection(self, request: public_dot_audit__log__pb2.TestS3ExportConnectionRequest, ctx: RequestContext) -> public_dot_audit__log__pb2.TestS3ExportConnectionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def trigger_s3_export(self, request: public_dot_audit__log__pb2.TriggerS3ExportRequest, ctx: RequestContext) -> public_dot_audit__log__pb2.TriggerS3ExportResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def configure_otlp_export(self, request: public_dot_audit__log__pb2.ConfigureOtlpExportRequest, ctx: RequestContext) -> public_dot_audit__log__pb2.ConfigureOtlpExportResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_otlp_export_config(self, request: public_dot_audit__log__pb2.GetOtlpExportConfigRequest, ctx: RequestContext) -> public_dot_audit__log__pb2.GetOtlpExportConfigResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_otlp_export_config(self, request: public_dot_audit__log__pb2.DeleteOtlpExportConfigRequest, ctx: RequestContext) -> public_dot_audit__log__pb2.DeleteOtlpExportConfigResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def test_otlp_export_connection(self, request: public_dot_audit__log__pb2.TestOtlpExportConnectionRequest, ctx: RequestContext) -> public_dot_audit__log__pb2.TestOtlpExportConnectionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def trigger_otlp_export(self, request: public_dot_audit__log__pb2.TriggerOtlpExportRequest, ctx: RequestContext) -> public_dot_audit__log__pb2.TriggerOtlpExportResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class AuditLogServiceASGIApplication(ConnectASGIApplication[AuditLogService]):

    def __init__(self, service: AuditLogService | AsyncGenerator[AuditLogService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.audit_log.AuditLogService/ListAuditLogs': Endpoint.unary(method=MethodInfo(name='ListAuditLogs', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.ListAuditLogsRequest, output=public_dot_audit__log__pb2.ListAuditLogsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_audit_logs), '/textql.rpc.public.audit_log.AuditLogService/ConfigureS3Export': Endpoint.unary(method=MethodInfo(name='ConfigureS3Export', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.ConfigureS3ExportRequest, output=public_dot_audit__log__pb2.ConfigureS3ExportResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.configure_s3_export), '/textql.rpc.public.audit_log.AuditLogService/GetS3ExportConfig': Endpoint.unary(method=MethodInfo(name='GetS3ExportConfig', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.GetS3ExportConfigRequest, output=public_dot_audit__log__pb2.GetS3ExportConfigResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_s3_export_config), '/textql.rpc.public.audit_log.AuditLogService/DeleteS3ExportConfig': Endpoint.unary(method=MethodInfo(name='DeleteS3ExportConfig', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.DeleteS3ExportConfigRequest, output=public_dot_audit__log__pb2.DeleteS3ExportConfigResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_s3_export_config), '/textql.rpc.public.audit_log.AuditLogService/TestS3ExportConnection': Endpoint.unary(method=MethodInfo(name='TestS3ExportConnection', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.TestS3ExportConnectionRequest, output=public_dot_audit__log__pb2.TestS3ExportConnectionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.test_s3_export_connection), '/textql.rpc.public.audit_log.AuditLogService/TriggerS3Export': Endpoint.unary(method=MethodInfo(name='TriggerS3Export', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.TriggerS3ExportRequest, output=public_dot_audit__log__pb2.TriggerS3ExportResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.trigger_s3_export), '/textql.rpc.public.audit_log.AuditLogService/ConfigureOtlpExport': Endpoint.unary(method=MethodInfo(name='ConfigureOtlpExport', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.ConfigureOtlpExportRequest, output=public_dot_audit__log__pb2.ConfigureOtlpExportResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.configure_otlp_export), '/textql.rpc.public.audit_log.AuditLogService/GetOtlpExportConfig': Endpoint.unary(method=MethodInfo(name='GetOtlpExportConfig', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.GetOtlpExportConfigRequest, output=public_dot_audit__log__pb2.GetOtlpExportConfigResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_otlp_export_config), '/textql.rpc.public.audit_log.AuditLogService/DeleteOtlpExportConfig': Endpoint.unary(method=MethodInfo(name='DeleteOtlpExportConfig', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.DeleteOtlpExportConfigRequest, output=public_dot_audit__log__pb2.DeleteOtlpExportConfigResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_otlp_export_config), '/textql.rpc.public.audit_log.AuditLogService/TestOtlpExportConnection': Endpoint.unary(method=MethodInfo(name='TestOtlpExportConnection', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.TestOtlpExportConnectionRequest, output=public_dot_audit__log__pb2.TestOtlpExportConnectionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.test_otlp_export_connection), '/textql.rpc.public.audit_log.AuditLogService/TriggerOtlpExport': Endpoint.unary(method=MethodInfo(name='TriggerOtlpExport', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.TriggerOtlpExportRequest, output=public_dot_audit__log__pb2.TriggerOtlpExportResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.trigger_otlp_export)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.audit_log.AuditLogService'

class AuditLogServiceClient(ConnectClient):

    async def list_audit_logs(self, request: public_dot_audit__log__pb2.ListAuditLogsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_audit__log__pb2.ListAuditLogsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListAuditLogs', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.ListAuditLogsRequest, output=public_dot_audit__log__pb2.ListAuditLogsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def configure_s3_export(self, request: public_dot_audit__log__pb2.ConfigureS3ExportRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_audit__log__pb2.ConfigureS3ExportResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ConfigureS3Export', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.ConfigureS3ExportRequest, output=public_dot_audit__log__pb2.ConfigureS3ExportResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_s3_export_config(self, request: public_dot_audit__log__pb2.GetS3ExportConfigRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_audit__log__pb2.GetS3ExportConfigResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetS3ExportConfig', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.GetS3ExportConfigRequest, output=public_dot_audit__log__pb2.GetS3ExportConfigResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def delete_s3_export_config(self, request: public_dot_audit__log__pb2.DeleteS3ExportConfigRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_audit__log__pb2.DeleteS3ExportConfigResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteS3ExportConfig', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.DeleteS3ExportConfigRequest, output=public_dot_audit__log__pb2.DeleteS3ExportConfigResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def test_s3_export_connection(self, request: public_dot_audit__log__pb2.TestS3ExportConnectionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_audit__log__pb2.TestS3ExportConnectionResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='TestS3ExportConnection', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.TestS3ExportConnectionRequest, output=public_dot_audit__log__pb2.TestS3ExportConnectionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def trigger_s3_export(self, request: public_dot_audit__log__pb2.TriggerS3ExportRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_audit__log__pb2.TriggerS3ExportResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='TriggerS3Export', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.TriggerS3ExportRequest, output=public_dot_audit__log__pb2.TriggerS3ExportResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def configure_otlp_export(self, request: public_dot_audit__log__pb2.ConfigureOtlpExportRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_audit__log__pb2.ConfigureOtlpExportResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ConfigureOtlpExport', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.ConfigureOtlpExportRequest, output=public_dot_audit__log__pb2.ConfigureOtlpExportResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_otlp_export_config(self, request: public_dot_audit__log__pb2.GetOtlpExportConfigRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_audit__log__pb2.GetOtlpExportConfigResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetOtlpExportConfig', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.GetOtlpExportConfigRequest, output=public_dot_audit__log__pb2.GetOtlpExportConfigResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def delete_otlp_export_config(self, request: public_dot_audit__log__pb2.DeleteOtlpExportConfigRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_audit__log__pb2.DeleteOtlpExportConfigResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteOtlpExportConfig', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.DeleteOtlpExportConfigRequest, output=public_dot_audit__log__pb2.DeleteOtlpExportConfigResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def test_otlp_export_connection(self, request: public_dot_audit__log__pb2.TestOtlpExportConnectionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_audit__log__pb2.TestOtlpExportConnectionResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='TestOtlpExportConnection', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.TestOtlpExportConnectionRequest, output=public_dot_audit__log__pb2.TestOtlpExportConnectionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def trigger_otlp_export(self, request: public_dot_audit__log__pb2.TriggerOtlpExportRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_audit__log__pb2.TriggerOtlpExportResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='TriggerOtlpExport', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.TriggerOtlpExportRequest, output=public_dot_audit__log__pb2.TriggerOtlpExportResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class AuditLogServiceSync(Protocol):

    def list_audit_logs(self, request: public_dot_audit__log__pb2.ListAuditLogsRequest, ctx: RequestContext) -> public_dot_audit__log__pb2.ListAuditLogsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def configure_s3_export(self, request: public_dot_audit__log__pb2.ConfigureS3ExportRequest, ctx: RequestContext) -> public_dot_audit__log__pb2.ConfigureS3ExportResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_s3_export_config(self, request: public_dot_audit__log__pb2.GetS3ExportConfigRequest, ctx: RequestContext) -> public_dot_audit__log__pb2.GetS3ExportConfigResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_s3_export_config(self, request: public_dot_audit__log__pb2.DeleteS3ExportConfigRequest, ctx: RequestContext) -> public_dot_audit__log__pb2.DeleteS3ExportConfigResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def test_s3_export_connection(self, request: public_dot_audit__log__pb2.TestS3ExportConnectionRequest, ctx: RequestContext) -> public_dot_audit__log__pb2.TestS3ExportConnectionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def trigger_s3_export(self, request: public_dot_audit__log__pb2.TriggerS3ExportRequest, ctx: RequestContext) -> public_dot_audit__log__pb2.TriggerS3ExportResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def configure_otlp_export(self, request: public_dot_audit__log__pb2.ConfigureOtlpExportRequest, ctx: RequestContext) -> public_dot_audit__log__pb2.ConfigureOtlpExportResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_otlp_export_config(self, request: public_dot_audit__log__pb2.GetOtlpExportConfigRequest, ctx: RequestContext) -> public_dot_audit__log__pb2.GetOtlpExportConfigResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_otlp_export_config(self, request: public_dot_audit__log__pb2.DeleteOtlpExportConfigRequest, ctx: RequestContext) -> public_dot_audit__log__pb2.DeleteOtlpExportConfigResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def test_otlp_export_connection(self, request: public_dot_audit__log__pb2.TestOtlpExportConnectionRequest, ctx: RequestContext) -> public_dot_audit__log__pb2.TestOtlpExportConnectionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def trigger_otlp_export(self, request: public_dot_audit__log__pb2.TriggerOtlpExportRequest, ctx: RequestContext) -> public_dot_audit__log__pb2.TriggerOtlpExportResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class AuditLogServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: AuditLogServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.audit_log.AuditLogService/ListAuditLogs': EndpointSync.unary(method=MethodInfo(name='ListAuditLogs', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.ListAuditLogsRequest, output=public_dot_audit__log__pb2.ListAuditLogsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_audit_logs), '/textql.rpc.public.audit_log.AuditLogService/ConfigureS3Export': EndpointSync.unary(method=MethodInfo(name='ConfigureS3Export', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.ConfigureS3ExportRequest, output=public_dot_audit__log__pb2.ConfigureS3ExportResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.configure_s3_export), '/textql.rpc.public.audit_log.AuditLogService/GetS3ExportConfig': EndpointSync.unary(method=MethodInfo(name='GetS3ExportConfig', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.GetS3ExportConfigRequest, output=public_dot_audit__log__pb2.GetS3ExportConfigResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_s3_export_config), '/textql.rpc.public.audit_log.AuditLogService/DeleteS3ExportConfig': EndpointSync.unary(method=MethodInfo(name='DeleteS3ExportConfig', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.DeleteS3ExportConfigRequest, output=public_dot_audit__log__pb2.DeleteS3ExportConfigResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_s3_export_config), '/textql.rpc.public.audit_log.AuditLogService/TestS3ExportConnection': EndpointSync.unary(method=MethodInfo(name='TestS3ExportConnection', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.TestS3ExportConnectionRequest, output=public_dot_audit__log__pb2.TestS3ExportConnectionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.test_s3_export_connection), '/textql.rpc.public.audit_log.AuditLogService/TriggerS3Export': EndpointSync.unary(method=MethodInfo(name='TriggerS3Export', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.TriggerS3ExportRequest, output=public_dot_audit__log__pb2.TriggerS3ExportResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.trigger_s3_export), '/textql.rpc.public.audit_log.AuditLogService/ConfigureOtlpExport': EndpointSync.unary(method=MethodInfo(name='ConfigureOtlpExport', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.ConfigureOtlpExportRequest, output=public_dot_audit__log__pb2.ConfigureOtlpExportResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.configure_otlp_export), '/textql.rpc.public.audit_log.AuditLogService/GetOtlpExportConfig': EndpointSync.unary(method=MethodInfo(name='GetOtlpExportConfig', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.GetOtlpExportConfigRequest, output=public_dot_audit__log__pb2.GetOtlpExportConfigResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_otlp_export_config), '/textql.rpc.public.audit_log.AuditLogService/DeleteOtlpExportConfig': EndpointSync.unary(method=MethodInfo(name='DeleteOtlpExportConfig', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.DeleteOtlpExportConfigRequest, output=public_dot_audit__log__pb2.DeleteOtlpExportConfigResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_otlp_export_config), '/textql.rpc.public.audit_log.AuditLogService/TestOtlpExportConnection': EndpointSync.unary(method=MethodInfo(name='TestOtlpExportConnection', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.TestOtlpExportConnectionRequest, output=public_dot_audit__log__pb2.TestOtlpExportConnectionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.test_otlp_export_connection), '/textql.rpc.public.audit_log.AuditLogService/TriggerOtlpExport': EndpointSync.unary(method=MethodInfo(name='TriggerOtlpExport', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.TriggerOtlpExportRequest, output=public_dot_audit__log__pb2.TriggerOtlpExportResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.trigger_otlp_export)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.audit_log.AuditLogService'

class AuditLogServiceClientSync(ConnectClientSync):

    def list_audit_logs(self, request: public_dot_audit__log__pb2.ListAuditLogsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_audit__log__pb2.ListAuditLogsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListAuditLogs', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.ListAuditLogsRequest, output=public_dot_audit__log__pb2.ListAuditLogsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def configure_s3_export(self, request: public_dot_audit__log__pb2.ConfigureS3ExportRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_audit__log__pb2.ConfigureS3ExportResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ConfigureS3Export', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.ConfigureS3ExportRequest, output=public_dot_audit__log__pb2.ConfigureS3ExportResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_s3_export_config(self, request: public_dot_audit__log__pb2.GetS3ExportConfigRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_audit__log__pb2.GetS3ExportConfigResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetS3ExportConfig', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.GetS3ExportConfigRequest, output=public_dot_audit__log__pb2.GetS3ExportConfigResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def delete_s3_export_config(self, request: public_dot_audit__log__pb2.DeleteS3ExportConfigRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_audit__log__pb2.DeleteS3ExportConfigResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteS3ExportConfig', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.DeleteS3ExportConfigRequest, output=public_dot_audit__log__pb2.DeleteS3ExportConfigResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def test_s3_export_connection(self, request: public_dot_audit__log__pb2.TestS3ExportConnectionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_audit__log__pb2.TestS3ExportConnectionResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='TestS3ExportConnection', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.TestS3ExportConnectionRequest, output=public_dot_audit__log__pb2.TestS3ExportConnectionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def trigger_s3_export(self, request: public_dot_audit__log__pb2.TriggerS3ExportRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_audit__log__pb2.TriggerS3ExportResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='TriggerS3Export', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.TriggerS3ExportRequest, output=public_dot_audit__log__pb2.TriggerS3ExportResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def configure_otlp_export(self, request: public_dot_audit__log__pb2.ConfigureOtlpExportRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_audit__log__pb2.ConfigureOtlpExportResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ConfigureOtlpExport', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.ConfigureOtlpExportRequest, output=public_dot_audit__log__pb2.ConfigureOtlpExportResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_otlp_export_config(self, request: public_dot_audit__log__pb2.GetOtlpExportConfigRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_audit__log__pb2.GetOtlpExportConfigResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetOtlpExportConfig', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.GetOtlpExportConfigRequest, output=public_dot_audit__log__pb2.GetOtlpExportConfigResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def delete_otlp_export_config(self, request: public_dot_audit__log__pb2.DeleteOtlpExportConfigRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_audit__log__pb2.DeleteOtlpExportConfigResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteOtlpExportConfig', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.DeleteOtlpExportConfigRequest, output=public_dot_audit__log__pb2.DeleteOtlpExportConfigResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def test_otlp_export_connection(self, request: public_dot_audit__log__pb2.TestOtlpExportConnectionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_audit__log__pb2.TestOtlpExportConnectionResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='TestOtlpExportConnection', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.TestOtlpExportConnectionRequest, output=public_dot_audit__log__pb2.TestOtlpExportConnectionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def trigger_otlp_export(self, request: public_dot_audit__log__pb2.TriggerOtlpExportRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_audit__log__pb2.TriggerOtlpExportResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='TriggerOtlpExport', service_name='textql.rpc.public.audit_log.AuditLogService', input=public_dot_audit__log__pb2.TriggerOtlpExportRequest, output=public_dot_audit__log__pb2.TriggerOtlpExportResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)