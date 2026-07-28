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
from . import issues_pb2 as public_dot_issues__pb2

class IssueService(Protocol):

    async def list_issues(self, request: public_dot_issues__pb2.ListIssuesRequest, ctx: RequestContext) -> public_dot_issues__pb2.ListIssuesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_issue(self, request: public_dot_issues__pb2.GetIssueRequest, ctx: RequestContext) -> public_dot_issues__pb2.GetIssueResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_issue_stats(self, request: public_dot_issues__pb2.GetIssueStatsRequest, ctx: RequestContext) -> public_dot_issues__pb2.GetIssueStatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_issue_state(self, request: public_dot_issues__pb2.UpdateIssueStateRequest, ctx: RequestContext) -> public_dot_issues__pb2.UpdateIssueStateResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_report_state(self, request: public_dot_issues__pb2.UpdateReportStateRequest, ctx: RequestContext) -> public_dot_issues__pb2.UpdateReportStateResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def assign_issue(self, request: public_dot_issues__pb2.AssignIssueRequest, ctx: RequestContext) -> public_dot_issues__pb2.AssignIssueResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def unassign_issue(self, request: public_dot_issues__pb2.UnassignIssueRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def bulk_assign_issues(self, request: public_dot_issues__pb2.BulkAssignIssuesRequest, ctx: RequestContext) -> public_dot_issues__pb2.BulkAssignIssuesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def bulk_unassign_issues(self, request: public_dot_issues__pb2.BulkUnassignIssuesRequest, ctx: RequestContext) -> public_dot_issues__pb2.BulkUnassignIssuesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class IssueServiceASGIApplication(ConnectASGIApplication[IssueService]):

    def __init__(self, service: IssueService | AsyncGenerator[IssueService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.issues.IssueService/ListIssues': Endpoint.unary(method=MethodInfo(name='ListIssues', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.ListIssuesRequest, output=public_dot_issues__pb2.ListIssuesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_issues), '/textql.rpc.public.issues.IssueService/GetIssue': Endpoint.unary(method=MethodInfo(name='GetIssue', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.GetIssueRequest, output=public_dot_issues__pb2.GetIssueResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_issue), '/textql.rpc.public.issues.IssueService/GetIssueStats': Endpoint.unary(method=MethodInfo(name='GetIssueStats', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.GetIssueStatsRequest, output=public_dot_issues__pb2.GetIssueStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_issue_stats), '/textql.rpc.public.issues.IssueService/UpdateIssueState': Endpoint.unary(method=MethodInfo(name='UpdateIssueState', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.UpdateIssueStateRequest, output=public_dot_issues__pb2.UpdateIssueStateResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_issue_state), '/textql.rpc.public.issues.IssueService/UpdateReportState': Endpoint.unary(method=MethodInfo(name='UpdateReportState', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.UpdateReportStateRequest, output=public_dot_issues__pb2.UpdateReportStateResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_report_state), '/textql.rpc.public.issues.IssueService/AssignIssue': Endpoint.unary(method=MethodInfo(name='AssignIssue', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.AssignIssueRequest, output=public_dot_issues__pb2.AssignIssueResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.assign_issue), '/textql.rpc.public.issues.IssueService/UnassignIssue': Endpoint.unary(method=MethodInfo(name='UnassignIssue', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.UnassignIssueRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.unassign_issue), '/textql.rpc.public.issues.IssueService/BulkAssignIssues': Endpoint.unary(method=MethodInfo(name='BulkAssignIssues', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.BulkAssignIssuesRequest, output=public_dot_issues__pb2.BulkAssignIssuesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.bulk_assign_issues), '/textql.rpc.public.issues.IssueService/BulkUnassignIssues': Endpoint.unary(method=MethodInfo(name='BulkUnassignIssues', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.BulkUnassignIssuesRequest, output=public_dot_issues__pb2.BulkUnassignIssuesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.bulk_unassign_issues)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.issues.IssueService'

class IssueServiceClient(ConnectClient):

    async def list_issues(self, request: public_dot_issues__pb2.ListIssuesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_issues__pb2.ListIssuesResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListIssues', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.ListIssuesRequest, output=public_dot_issues__pb2.ListIssuesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_issue(self, request: public_dot_issues__pb2.GetIssueRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_issues__pb2.GetIssueResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetIssue', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.GetIssueRequest, output=public_dot_issues__pb2.GetIssueResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_issue_stats(self, request: public_dot_issues__pb2.GetIssueStatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_issues__pb2.GetIssueStatsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetIssueStats', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.GetIssueStatsRequest, output=public_dot_issues__pb2.GetIssueStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def update_issue_state(self, request: public_dot_issues__pb2.UpdateIssueStateRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_issues__pb2.UpdateIssueStateResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateIssueState', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.UpdateIssueStateRequest, output=public_dot_issues__pb2.UpdateIssueStateResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def update_report_state(self, request: public_dot_issues__pb2.UpdateReportStateRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_issues__pb2.UpdateReportStateResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateReportState', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.UpdateReportStateRequest, output=public_dot_issues__pb2.UpdateReportStateResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def assign_issue(self, request: public_dot_issues__pb2.AssignIssueRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_issues__pb2.AssignIssueResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='AssignIssue', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.AssignIssueRequest, output=public_dot_issues__pb2.AssignIssueResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def unassign_issue(self, request: public_dot_issues__pb2.UnassignIssueRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='UnassignIssue', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.UnassignIssueRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def bulk_assign_issues(self, request: public_dot_issues__pb2.BulkAssignIssuesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_issues__pb2.BulkAssignIssuesResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='BulkAssignIssues', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.BulkAssignIssuesRequest, output=public_dot_issues__pb2.BulkAssignIssuesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def bulk_unassign_issues(self, request: public_dot_issues__pb2.BulkUnassignIssuesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_issues__pb2.BulkUnassignIssuesResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='BulkUnassignIssues', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.BulkUnassignIssuesRequest, output=public_dot_issues__pb2.BulkUnassignIssuesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class IssueServiceSync(Protocol):

    def list_issues(self, request: public_dot_issues__pb2.ListIssuesRequest, ctx: RequestContext) -> public_dot_issues__pb2.ListIssuesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_issue(self, request: public_dot_issues__pb2.GetIssueRequest, ctx: RequestContext) -> public_dot_issues__pb2.GetIssueResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_issue_stats(self, request: public_dot_issues__pb2.GetIssueStatsRequest, ctx: RequestContext) -> public_dot_issues__pb2.GetIssueStatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_issue_state(self, request: public_dot_issues__pb2.UpdateIssueStateRequest, ctx: RequestContext) -> public_dot_issues__pb2.UpdateIssueStateResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_report_state(self, request: public_dot_issues__pb2.UpdateReportStateRequest, ctx: RequestContext) -> public_dot_issues__pb2.UpdateReportStateResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def assign_issue(self, request: public_dot_issues__pb2.AssignIssueRequest, ctx: RequestContext) -> public_dot_issues__pb2.AssignIssueResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def unassign_issue(self, request: public_dot_issues__pb2.UnassignIssueRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def bulk_assign_issues(self, request: public_dot_issues__pb2.BulkAssignIssuesRequest, ctx: RequestContext) -> public_dot_issues__pb2.BulkAssignIssuesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def bulk_unassign_issues(self, request: public_dot_issues__pb2.BulkUnassignIssuesRequest, ctx: RequestContext) -> public_dot_issues__pb2.BulkUnassignIssuesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class IssueServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: IssueServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.issues.IssueService/ListIssues': EndpointSync.unary(method=MethodInfo(name='ListIssues', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.ListIssuesRequest, output=public_dot_issues__pb2.ListIssuesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_issues), '/textql.rpc.public.issues.IssueService/GetIssue': EndpointSync.unary(method=MethodInfo(name='GetIssue', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.GetIssueRequest, output=public_dot_issues__pb2.GetIssueResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_issue), '/textql.rpc.public.issues.IssueService/GetIssueStats': EndpointSync.unary(method=MethodInfo(name='GetIssueStats', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.GetIssueStatsRequest, output=public_dot_issues__pb2.GetIssueStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_issue_stats), '/textql.rpc.public.issues.IssueService/UpdateIssueState': EndpointSync.unary(method=MethodInfo(name='UpdateIssueState', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.UpdateIssueStateRequest, output=public_dot_issues__pb2.UpdateIssueStateResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_issue_state), '/textql.rpc.public.issues.IssueService/UpdateReportState': EndpointSync.unary(method=MethodInfo(name='UpdateReportState', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.UpdateReportStateRequest, output=public_dot_issues__pb2.UpdateReportStateResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_report_state), '/textql.rpc.public.issues.IssueService/AssignIssue': EndpointSync.unary(method=MethodInfo(name='AssignIssue', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.AssignIssueRequest, output=public_dot_issues__pb2.AssignIssueResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.assign_issue), '/textql.rpc.public.issues.IssueService/UnassignIssue': EndpointSync.unary(method=MethodInfo(name='UnassignIssue', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.UnassignIssueRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.unassign_issue), '/textql.rpc.public.issues.IssueService/BulkAssignIssues': EndpointSync.unary(method=MethodInfo(name='BulkAssignIssues', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.BulkAssignIssuesRequest, output=public_dot_issues__pb2.BulkAssignIssuesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.bulk_assign_issues), '/textql.rpc.public.issues.IssueService/BulkUnassignIssues': EndpointSync.unary(method=MethodInfo(name='BulkUnassignIssues', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.BulkUnassignIssuesRequest, output=public_dot_issues__pb2.BulkUnassignIssuesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.bulk_unassign_issues)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.issues.IssueService'

class IssueServiceClientSync(ConnectClientSync):

    def list_issues(self, request: public_dot_issues__pb2.ListIssuesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_issues__pb2.ListIssuesResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListIssues', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.ListIssuesRequest, output=public_dot_issues__pb2.ListIssuesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_issue(self, request: public_dot_issues__pb2.GetIssueRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_issues__pb2.GetIssueResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetIssue', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.GetIssueRequest, output=public_dot_issues__pb2.GetIssueResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_issue_stats(self, request: public_dot_issues__pb2.GetIssueStatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_issues__pb2.GetIssueStatsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetIssueStats', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.GetIssueStatsRequest, output=public_dot_issues__pb2.GetIssueStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def update_issue_state(self, request: public_dot_issues__pb2.UpdateIssueStateRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_issues__pb2.UpdateIssueStateResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateIssueState', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.UpdateIssueStateRequest, output=public_dot_issues__pb2.UpdateIssueStateResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def update_report_state(self, request: public_dot_issues__pb2.UpdateReportStateRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_issues__pb2.UpdateReportStateResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateReportState', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.UpdateReportStateRequest, output=public_dot_issues__pb2.UpdateReportStateResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def assign_issue(self, request: public_dot_issues__pb2.AssignIssueRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_issues__pb2.AssignIssueResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='AssignIssue', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.AssignIssueRequest, output=public_dot_issues__pb2.AssignIssueResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def unassign_issue(self, request: public_dot_issues__pb2.UnassignIssueRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='UnassignIssue', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.UnassignIssueRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def bulk_assign_issues(self, request: public_dot_issues__pb2.BulkAssignIssuesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_issues__pb2.BulkAssignIssuesResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='BulkAssignIssues', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.BulkAssignIssuesRequest, output=public_dot_issues__pb2.BulkAssignIssuesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def bulk_unassign_issues(self, request: public_dot_issues__pb2.BulkUnassignIssuesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_issues__pb2.BulkUnassignIssuesResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='BulkUnassignIssues', service_name='textql.rpc.public.issues.IssueService', input=public_dot_issues__pb2.BulkUnassignIssuesRequest, output=public_dot_issues__pb2.BulkUnassignIssuesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)