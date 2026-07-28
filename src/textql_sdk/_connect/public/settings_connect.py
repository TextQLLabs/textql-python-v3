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
from . import settings_pb2 as public_dot_settings__pb2

class SettingsService(Protocol):

    async def update_organization_settings(self, request: public_dot_settings__pb2.UpdateOrganizationSettingsRequest, ctx: RequestContext) -> public_dot_settings__pb2.UpdateOrganizationSettingsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_organization_members(self, request: public_dot_settings__pb2.ListOrganizationMembersRequest, ctx: RequestContext) -> public_dot_settings__pb2.ListOrganizationMembersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def invite_organization_member(self, request: public_dot_settings__pb2.InviteOrganizationMemberRequest, ctx: RequestContext) -> public_dot_settings__pb2.InviteOrganizationMemberResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_organization_member(self, request: public_dot_settings__pb2.DeleteOrganizationMemberRequest, ctx: RequestContext) -> public_dot_settings__pb2.DeleteOrganizationMemberResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_organization(self, request: public_dot_settings__pb2.DeleteOrganizationRequest, ctx: RequestContext) -> public_dot_settings__pb2.DeleteOrganizationResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_current_member_profile(self, request: public_dot_settings__pb2.UpdateCurrentMemberProfileRequest, ctx: RequestContext) -> public_dot_settings__pb2.UpdateCurrentMemberProfileResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def check_member_status(self, request: public_dot_settings__pb2.CheckMemberStatusRequest, ctx: RequestContext) -> public_dot_settings__pb2.CheckMemberStatusResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_model_deprecations(self, request: public_dot_settings__pb2.GetModelDeprecationsRequest, ctx: RequestContext) -> public_dot_settings__pb2.GetModelDeprecationsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class SettingsServiceASGIApplication(ConnectASGIApplication[SettingsService]):

    def __init__(self, service: SettingsService | AsyncGenerator[SettingsService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.settings.SettingsService/UpdateOrganizationSettings': Endpoint.unary(method=MethodInfo(name='UpdateOrganizationSettings', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.UpdateOrganizationSettingsRequest, output=public_dot_settings__pb2.UpdateOrganizationSettingsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_organization_settings), '/textql.rpc.public.settings.SettingsService/ListOrganizationMembers': Endpoint.unary(method=MethodInfo(name='ListOrganizationMembers', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.ListOrganizationMembersRequest, output=public_dot_settings__pb2.ListOrganizationMembersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_organization_members), '/textql.rpc.public.settings.SettingsService/InviteOrganizationMember': Endpoint.unary(method=MethodInfo(name='InviteOrganizationMember', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.InviteOrganizationMemberRequest, output=public_dot_settings__pb2.InviteOrganizationMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.invite_organization_member), '/textql.rpc.public.settings.SettingsService/DeleteOrganizationMember': Endpoint.unary(method=MethodInfo(name='DeleteOrganizationMember', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.DeleteOrganizationMemberRequest, output=public_dot_settings__pb2.DeleteOrganizationMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_organization_member), '/textql.rpc.public.settings.SettingsService/DeleteOrganization': Endpoint.unary(method=MethodInfo(name='DeleteOrganization', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.DeleteOrganizationRequest, output=public_dot_settings__pb2.DeleteOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_organization), '/textql.rpc.public.settings.SettingsService/UpdateCurrentMemberProfile': Endpoint.unary(method=MethodInfo(name='UpdateCurrentMemberProfile', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.UpdateCurrentMemberProfileRequest, output=public_dot_settings__pb2.UpdateCurrentMemberProfileResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_current_member_profile), '/textql.rpc.public.settings.SettingsService/CheckMemberStatus': Endpoint.unary(method=MethodInfo(name='CheckMemberStatus', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.CheckMemberStatusRequest, output=public_dot_settings__pb2.CheckMemberStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.check_member_status), '/textql.rpc.public.settings.SettingsService/GetModelDeprecations': Endpoint.unary(method=MethodInfo(name='GetModelDeprecations', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.GetModelDeprecationsRequest, output=public_dot_settings__pb2.GetModelDeprecationsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_model_deprecations)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.settings.SettingsService'

class SettingsServiceClient(ConnectClient):

    async def update_organization_settings(self, request: public_dot_settings__pb2.UpdateOrganizationSettingsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_settings__pb2.UpdateOrganizationSettingsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateOrganizationSettings', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.UpdateOrganizationSettingsRequest, output=public_dot_settings__pb2.UpdateOrganizationSettingsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_organization_members(self, request: public_dot_settings__pb2.ListOrganizationMembersRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_settings__pb2.ListOrganizationMembersResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListOrganizationMembers', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.ListOrganizationMembersRequest, output=public_dot_settings__pb2.ListOrganizationMembersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def invite_organization_member(self, request: public_dot_settings__pb2.InviteOrganizationMemberRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_settings__pb2.InviteOrganizationMemberResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='InviteOrganizationMember', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.InviteOrganizationMemberRequest, output=public_dot_settings__pb2.InviteOrganizationMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def delete_organization_member(self, request: public_dot_settings__pb2.DeleteOrganizationMemberRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_settings__pb2.DeleteOrganizationMemberResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteOrganizationMember', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.DeleteOrganizationMemberRequest, output=public_dot_settings__pb2.DeleteOrganizationMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def delete_organization(self, request: public_dot_settings__pb2.DeleteOrganizationRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_settings__pb2.DeleteOrganizationResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteOrganization', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.DeleteOrganizationRequest, output=public_dot_settings__pb2.DeleteOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def update_current_member_profile(self, request: public_dot_settings__pb2.UpdateCurrentMemberProfileRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_settings__pb2.UpdateCurrentMemberProfileResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateCurrentMemberProfile', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.UpdateCurrentMemberProfileRequest, output=public_dot_settings__pb2.UpdateCurrentMemberProfileResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def check_member_status(self, request: public_dot_settings__pb2.CheckMemberStatusRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_settings__pb2.CheckMemberStatusResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CheckMemberStatus', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.CheckMemberStatusRequest, output=public_dot_settings__pb2.CheckMemberStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_model_deprecations(self, request: public_dot_settings__pb2.GetModelDeprecationsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_settings__pb2.GetModelDeprecationsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetModelDeprecations', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.GetModelDeprecationsRequest, output=public_dot_settings__pb2.GetModelDeprecationsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class SettingsServiceSync(Protocol):

    def update_organization_settings(self, request: public_dot_settings__pb2.UpdateOrganizationSettingsRequest, ctx: RequestContext) -> public_dot_settings__pb2.UpdateOrganizationSettingsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_organization_members(self, request: public_dot_settings__pb2.ListOrganizationMembersRequest, ctx: RequestContext) -> public_dot_settings__pb2.ListOrganizationMembersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def invite_organization_member(self, request: public_dot_settings__pb2.InviteOrganizationMemberRequest, ctx: RequestContext) -> public_dot_settings__pb2.InviteOrganizationMemberResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_organization_member(self, request: public_dot_settings__pb2.DeleteOrganizationMemberRequest, ctx: RequestContext) -> public_dot_settings__pb2.DeleteOrganizationMemberResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_organization(self, request: public_dot_settings__pb2.DeleteOrganizationRequest, ctx: RequestContext) -> public_dot_settings__pb2.DeleteOrganizationResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_current_member_profile(self, request: public_dot_settings__pb2.UpdateCurrentMemberProfileRequest, ctx: RequestContext) -> public_dot_settings__pb2.UpdateCurrentMemberProfileResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def check_member_status(self, request: public_dot_settings__pb2.CheckMemberStatusRequest, ctx: RequestContext) -> public_dot_settings__pb2.CheckMemberStatusResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_model_deprecations(self, request: public_dot_settings__pb2.GetModelDeprecationsRequest, ctx: RequestContext) -> public_dot_settings__pb2.GetModelDeprecationsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class SettingsServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: SettingsServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.settings.SettingsService/UpdateOrganizationSettings': EndpointSync.unary(method=MethodInfo(name='UpdateOrganizationSettings', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.UpdateOrganizationSettingsRequest, output=public_dot_settings__pb2.UpdateOrganizationSettingsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_organization_settings), '/textql.rpc.public.settings.SettingsService/ListOrganizationMembers': EndpointSync.unary(method=MethodInfo(name='ListOrganizationMembers', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.ListOrganizationMembersRequest, output=public_dot_settings__pb2.ListOrganizationMembersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_organization_members), '/textql.rpc.public.settings.SettingsService/InviteOrganizationMember': EndpointSync.unary(method=MethodInfo(name='InviteOrganizationMember', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.InviteOrganizationMemberRequest, output=public_dot_settings__pb2.InviteOrganizationMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.invite_organization_member), '/textql.rpc.public.settings.SettingsService/DeleteOrganizationMember': EndpointSync.unary(method=MethodInfo(name='DeleteOrganizationMember', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.DeleteOrganizationMemberRequest, output=public_dot_settings__pb2.DeleteOrganizationMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_organization_member), '/textql.rpc.public.settings.SettingsService/DeleteOrganization': EndpointSync.unary(method=MethodInfo(name='DeleteOrganization', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.DeleteOrganizationRequest, output=public_dot_settings__pb2.DeleteOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_organization), '/textql.rpc.public.settings.SettingsService/UpdateCurrentMemberProfile': EndpointSync.unary(method=MethodInfo(name='UpdateCurrentMemberProfile', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.UpdateCurrentMemberProfileRequest, output=public_dot_settings__pb2.UpdateCurrentMemberProfileResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_current_member_profile), '/textql.rpc.public.settings.SettingsService/CheckMemberStatus': EndpointSync.unary(method=MethodInfo(name='CheckMemberStatus', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.CheckMemberStatusRequest, output=public_dot_settings__pb2.CheckMemberStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.check_member_status), '/textql.rpc.public.settings.SettingsService/GetModelDeprecations': EndpointSync.unary(method=MethodInfo(name='GetModelDeprecations', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.GetModelDeprecationsRequest, output=public_dot_settings__pb2.GetModelDeprecationsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_model_deprecations)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.settings.SettingsService'

class SettingsServiceClientSync(ConnectClientSync):

    def update_organization_settings(self, request: public_dot_settings__pb2.UpdateOrganizationSettingsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_settings__pb2.UpdateOrganizationSettingsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateOrganizationSettings', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.UpdateOrganizationSettingsRequest, output=public_dot_settings__pb2.UpdateOrganizationSettingsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_organization_members(self, request: public_dot_settings__pb2.ListOrganizationMembersRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_settings__pb2.ListOrganizationMembersResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListOrganizationMembers', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.ListOrganizationMembersRequest, output=public_dot_settings__pb2.ListOrganizationMembersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def invite_organization_member(self, request: public_dot_settings__pb2.InviteOrganizationMemberRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_settings__pb2.InviteOrganizationMemberResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='InviteOrganizationMember', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.InviteOrganizationMemberRequest, output=public_dot_settings__pb2.InviteOrganizationMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def delete_organization_member(self, request: public_dot_settings__pb2.DeleteOrganizationMemberRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_settings__pb2.DeleteOrganizationMemberResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteOrganizationMember', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.DeleteOrganizationMemberRequest, output=public_dot_settings__pb2.DeleteOrganizationMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def delete_organization(self, request: public_dot_settings__pb2.DeleteOrganizationRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_settings__pb2.DeleteOrganizationResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteOrganization', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.DeleteOrganizationRequest, output=public_dot_settings__pb2.DeleteOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def update_current_member_profile(self, request: public_dot_settings__pb2.UpdateCurrentMemberProfileRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_settings__pb2.UpdateCurrentMemberProfileResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateCurrentMemberProfile', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.UpdateCurrentMemberProfileRequest, output=public_dot_settings__pb2.UpdateCurrentMemberProfileResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def check_member_status(self, request: public_dot_settings__pb2.CheckMemberStatusRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_settings__pb2.CheckMemberStatusResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CheckMemberStatus', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.CheckMemberStatusRequest, output=public_dot_settings__pb2.CheckMemberStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_model_deprecations(self, request: public_dot_settings__pb2.GetModelDeprecationsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_settings__pb2.GetModelDeprecationsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetModelDeprecations', service_name='textql.rpc.public.settings.SettingsService', input=public_dot_settings__pb2.GetModelDeprecationsRequest, output=public_dot_settings__pb2.GetModelDeprecationsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)