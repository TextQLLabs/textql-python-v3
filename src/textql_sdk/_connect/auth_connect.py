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
from . import auth_pb2 as auth__pb2

class AuthService(Protocol):

    async def start_session(self, request: auth__pb2.StartSessionRequest, ctx: RequestContext) -> auth__pb2.SessionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def renew_session(self, request: auth__pb2.RenewSessionRequest, ctx: RequestContext) -> auth__pb2.SessionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def renew_long_term_access_token(self, request: auth__pb2.RenewLongTermAccessTokenRequest, ctx: RequestContext) -> auth__pb2.LongTermAccessTokenResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def create_org(self, request: auth__pb2.CreateOrgRequest, ctx: RequestContext) -> auth__pb2.CreateOrgResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def find_orgs_by_slug(self, request: auth__pb2.FindOrgsBySlugRequest, ctx: RequestContext) -> auth__pb2.FindOrgsBySlugResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_org(self, request: auth__pb2.UpdateOrgRequest, ctx: RequestContext) -> auth__pb2.UpdateOrgResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_org_by_id(self, request: auth__pb2.GetOrgByIdRequest, ctx: RequestContext) -> auth__pb2.GetOrgByIdResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def create_org_member(self, request: auth__pb2.CreateOrgMemberRequest, ctx: RequestContext) -> auth__pb2.CreateOrgMemberResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def find_members_in_org(self, request: auth__pb2.FindMembersInOrgRequest, ctx: RequestContext) -> auth__pb2.FindMembersInOrgResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def email_invite_member(self, request: auth__pb2.EmailInviteMemberRequest, ctx: RequestContext) -> auth__pb2.EmailInviteMemberResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_org_member_by_member_id(self, request: auth__pb2.GetOrgMemberByMemberIdRequest, ctx: RequestContext) -> auth__pb2.GetOrgMemberByMemberIdResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_member(self, request: auth__pb2.DeleteMemberRequest, ctx: RequestContext) -> auth__pb2.DeleteMemberResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_organization(self, request: auth__pb2.DeleteOrganizationRequest, ctx: RequestContext) -> auth__pb2.DeleteOrganizationResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class AuthServiceASGIApplication(ConnectASGIApplication[AuthService]):

    def __init__(self, service: AuthService | AsyncGenerator[AuthService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.auth.AuthService/StartSession': Endpoint.unary(method=MethodInfo(name='StartSession', service_name='textql.rpc.auth.AuthService', input=auth__pb2.StartSessionRequest, output=auth__pb2.SessionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.start_session), '/textql.rpc.auth.AuthService/RenewSession': Endpoint.unary(method=MethodInfo(name='RenewSession', service_name='textql.rpc.auth.AuthService', input=auth__pb2.RenewSessionRequest, output=auth__pb2.SessionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.renew_session), '/textql.rpc.auth.AuthService/RenewLongTermAccessToken': Endpoint.unary(method=MethodInfo(name='RenewLongTermAccessToken', service_name='textql.rpc.auth.AuthService', input=auth__pb2.RenewLongTermAccessTokenRequest, output=auth__pb2.LongTermAccessTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.renew_long_term_access_token), '/textql.rpc.auth.AuthService/CreateOrg': Endpoint.unary(method=MethodInfo(name='CreateOrg', service_name='textql.rpc.auth.AuthService', input=auth__pb2.CreateOrgRequest, output=auth__pb2.CreateOrgResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_org), '/textql.rpc.auth.AuthService/FindOrgsBySlug': Endpoint.unary(method=MethodInfo(name='FindOrgsBySlug', service_name='textql.rpc.auth.AuthService', input=auth__pb2.FindOrgsBySlugRequest, output=auth__pb2.FindOrgsBySlugResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.find_orgs_by_slug), '/textql.rpc.auth.AuthService/UpdateOrg': Endpoint.unary(method=MethodInfo(name='UpdateOrg', service_name='textql.rpc.auth.AuthService', input=auth__pb2.UpdateOrgRequest, output=auth__pb2.UpdateOrgResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_org), '/textql.rpc.auth.AuthService/GetOrgById': Endpoint.unary(method=MethodInfo(name='GetOrgById', service_name='textql.rpc.auth.AuthService', input=auth__pb2.GetOrgByIdRequest, output=auth__pb2.GetOrgByIdResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_org_by_id), '/textql.rpc.auth.AuthService/CreateOrgMember': Endpoint.unary(method=MethodInfo(name='CreateOrgMember', service_name='textql.rpc.auth.AuthService', input=auth__pb2.CreateOrgMemberRequest, output=auth__pb2.CreateOrgMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_org_member), '/textql.rpc.auth.AuthService/FindMembersInOrg': Endpoint.unary(method=MethodInfo(name='FindMembersInOrg', service_name='textql.rpc.auth.AuthService', input=auth__pb2.FindMembersInOrgRequest, output=auth__pb2.FindMembersInOrgResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.find_members_in_org), '/textql.rpc.auth.AuthService/EmailInviteMember': Endpoint.unary(method=MethodInfo(name='EmailInviteMember', service_name='textql.rpc.auth.AuthService', input=auth__pb2.EmailInviteMemberRequest, output=auth__pb2.EmailInviteMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.email_invite_member), '/textql.rpc.auth.AuthService/GetOrgMemberByMemberId': Endpoint.unary(method=MethodInfo(name='GetOrgMemberByMemberId', service_name='textql.rpc.auth.AuthService', input=auth__pb2.GetOrgMemberByMemberIdRequest, output=auth__pb2.GetOrgMemberByMemberIdResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_org_member_by_member_id), '/textql.rpc.auth.AuthService/DeleteMember': Endpoint.unary(method=MethodInfo(name='DeleteMember', service_name='textql.rpc.auth.AuthService', input=auth__pb2.DeleteMemberRequest, output=auth__pb2.DeleteMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_member), '/textql.rpc.auth.AuthService/DeleteOrganization': Endpoint.unary(method=MethodInfo(name='DeleteOrganization', service_name='textql.rpc.auth.AuthService', input=auth__pb2.DeleteOrganizationRequest, output=auth__pb2.DeleteOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_organization)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.auth.AuthService'

class AuthServiceClient(ConnectClient):

    async def start_session(self, request: auth__pb2.StartSessionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.SessionResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='StartSession', service_name='textql.rpc.auth.AuthService', input=auth__pb2.StartSessionRequest, output=auth__pb2.SessionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def renew_session(self, request: auth__pb2.RenewSessionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.SessionResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RenewSession', service_name='textql.rpc.auth.AuthService', input=auth__pb2.RenewSessionRequest, output=auth__pb2.SessionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def renew_long_term_access_token(self, request: auth__pb2.RenewLongTermAccessTokenRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.LongTermAccessTokenResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RenewLongTermAccessToken', service_name='textql.rpc.auth.AuthService', input=auth__pb2.RenewLongTermAccessTokenRequest, output=auth__pb2.LongTermAccessTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def create_org(self, request: auth__pb2.CreateOrgRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.CreateOrgResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateOrg', service_name='textql.rpc.auth.AuthService', input=auth__pb2.CreateOrgRequest, output=auth__pb2.CreateOrgResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def find_orgs_by_slug(self, request: auth__pb2.FindOrgsBySlugRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.FindOrgsBySlugResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='FindOrgsBySlug', service_name='textql.rpc.auth.AuthService', input=auth__pb2.FindOrgsBySlugRequest, output=auth__pb2.FindOrgsBySlugResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def update_org(self, request: auth__pb2.UpdateOrgRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.UpdateOrgResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateOrg', service_name='textql.rpc.auth.AuthService', input=auth__pb2.UpdateOrgRequest, output=auth__pb2.UpdateOrgResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_org_by_id(self, request: auth__pb2.GetOrgByIdRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.GetOrgByIdResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetOrgById', service_name='textql.rpc.auth.AuthService', input=auth__pb2.GetOrgByIdRequest, output=auth__pb2.GetOrgByIdResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def create_org_member(self, request: auth__pb2.CreateOrgMemberRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.CreateOrgMemberResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateOrgMember', service_name='textql.rpc.auth.AuthService', input=auth__pb2.CreateOrgMemberRequest, output=auth__pb2.CreateOrgMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def find_members_in_org(self, request: auth__pb2.FindMembersInOrgRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.FindMembersInOrgResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='FindMembersInOrg', service_name='textql.rpc.auth.AuthService', input=auth__pb2.FindMembersInOrgRequest, output=auth__pb2.FindMembersInOrgResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def email_invite_member(self, request: auth__pb2.EmailInviteMemberRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.EmailInviteMemberResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='EmailInviteMember', service_name='textql.rpc.auth.AuthService', input=auth__pb2.EmailInviteMemberRequest, output=auth__pb2.EmailInviteMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_org_member_by_member_id(self, request: auth__pb2.GetOrgMemberByMemberIdRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.GetOrgMemberByMemberIdResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetOrgMemberByMemberId', service_name='textql.rpc.auth.AuthService', input=auth__pb2.GetOrgMemberByMemberIdRequest, output=auth__pb2.GetOrgMemberByMemberIdResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def delete_member(self, request: auth__pb2.DeleteMemberRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.DeleteMemberResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteMember', service_name='textql.rpc.auth.AuthService', input=auth__pb2.DeleteMemberRequest, output=auth__pb2.DeleteMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def delete_organization(self, request: auth__pb2.DeleteOrganizationRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.DeleteOrganizationResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteOrganization', service_name='textql.rpc.auth.AuthService', input=auth__pb2.DeleteOrganizationRequest, output=auth__pb2.DeleteOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class AuthServiceSync(Protocol):

    def start_session(self, request: auth__pb2.StartSessionRequest, ctx: RequestContext) -> auth__pb2.SessionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def renew_session(self, request: auth__pb2.RenewSessionRequest, ctx: RequestContext) -> auth__pb2.SessionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def renew_long_term_access_token(self, request: auth__pb2.RenewLongTermAccessTokenRequest, ctx: RequestContext) -> auth__pb2.LongTermAccessTokenResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def create_org(self, request: auth__pb2.CreateOrgRequest, ctx: RequestContext) -> auth__pb2.CreateOrgResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def find_orgs_by_slug(self, request: auth__pb2.FindOrgsBySlugRequest, ctx: RequestContext) -> auth__pb2.FindOrgsBySlugResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_org(self, request: auth__pb2.UpdateOrgRequest, ctx: RequestContext) -> auth__pb2.UpdateOrgResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_org_by_id(self, request: auth__pb2.GetOrgByIdRequest, ctx: RequestContext) -> auth__pb2.GetOrgByIdResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def create_org_member(self, request: auth__pb2.CreateOrgMemberRequest, ctx: RequestContext) -> auth__pb2.CreateOrgMemberResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def find_members_in_org(self, request: auth__pb2.FindMembersInOrgRequest, ctx: RequestContext) -> auth__pb2.FindMembersInOrgResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def email_invite_member(self, request: auth__pb2.EmailInviteMemberRequest, ctx: RequestContext) -> auth__pb2.EmailInviteMemberResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_org_member_by_member_id(self, request: auth__pb2.GetOrgMemberByMemberIdRequest, ctx: RequestContext) -> auth__pb2.GetOrgMemberByMemberIdResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_member(self, request: auth__pb2.DeleteMemberRequest, ctx: RequestContext) -> auth__pb2.DeleteMemberResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_organization(self, request: auth__pb2.DeleteOrganizationRequest, ctx: RequestContext) -> auth__pb2.DeleteOrganizationResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class AuthServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: AuthServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.auth.AuthService/StartSession': EndpointSync.unary(method=MethodInfo(name='StartSession', service_name='textql.rpc.auth.AuthService', input=auth__pb2.StartSessionRequest, output=auth__pb2.SessionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.start_session), '/textql.rpc.auth.AuthService/RenewSession': EndpointSync.unary(method=MethodInfo(name='RenewSession', service_name='textql.rpc.auth.AuthService', input=auth__pb2.RenewSessionRequest, output=auth__pb2.SessionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.renew_session), '/textql.rpc.auth.AuthService/RenewLongTermAccessToken': EndpointSync.unary(method=MethodInfo(name='RenewLongTermAccessToken', service_name='textql.rpc.auth.AuthService', input=auth__pb2.RenewLongTermAccessTokenRequest, output=auth__pb2.LongTermAccessTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.renew_long_term_access_token), '/textql.rpc.auth.AuthService/CreateOrg': EndpointSync.unary(method=MethodInfo(name='CreateOrg', service_name='textql.rpc.auth.AuthService', input=auth__pb2.CreateOrgRequest, output=auth__pb2.CreateOrgResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_org), '/textql.rpc.auth.AuthService/FindOrgsBySlug': EndpointSync.unary(method=MethodInfo(name='FindOrgsBySlug', service_name='textql.rpc.auth.AuthService', input=auth__pb2.FindOrgsBySlugRequest, output=auth__pb2.FindOrgsBySlugResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.find_orgs_by_slug), '/textql.rpc.auth.AuthService/UpdateOrg': EndpointSync.unary(method=MethodInfo(name='UpdateOrg', service_name='textql.rpc.auth.AuthService', input=auth__pb2.UpdateOrgRequest, output=auth__pb2.UpdateOrgResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_org), '/textql.rpc.auth.AuthService/GetOrgById': EndpointSync.unary(method=MethodInfo(name='GetOrgById', service_name='textql.rpc.auth.AuthService', input=auth__pb2.GetOrgByIdRequest, output=auth__pb2.GetOrgByIdResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_org_by_id), '/textql.rpc.auth.AuthService/CreateOrgMember': EndpointSync.unary(method=MethodInfo(name='CreateOrgMember', service_name='textql.rpc.auth.AuthService', input=auth__pb2.CreateOrgMemberRequest, output=auth__pb2.CreateOrgMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_org_member), '/textql.rpc.auth.AuthService/FindMembersInOrg': EndpointSync.unary(method=MethodInfo(name='FindMembersInOrg', service_name='textql.rpc.auth.AuthService', input=auth__pb2.FindMembersInOrgRequest, output=auth__pb2.FindMembersInOrgResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.find_members_in_org), '/textql.rpc.auth.AuthService/EmailInviteMember': EndpointSync.unary(method=MethodInfo(name='EmailInviteMember', service_name='textql.rpc.auth.AuthService', input=auth__pb2.EmailInviteMemberRequest, output=auth__pb2.EmailInviteMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.email_invite_member), '/textql.rpc.auth.AuthService/GetOrgMemberByMemberId': EndpointSync.unary(method=MethodInfo(name='GetOrgMemberByMemberId', service_name='textql.rpc.auth.AuthService', input=auth__pb2.GetOrgMemberByMemberIdRequest, output=auth__pb2.GetOrgMemberByMemberIdResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_org_member_by_member_id), '/textql.rpc.auth.AuthService/DeleteMember': EndpointSync.unary(method=MethodInfo(name='DeleteMember', service_name='textql.rpc.auth.AuthService', input=auth__pb2.DeleteMemberRequest, output=auth__pb2.DeleteMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_member), '/textql.rpc.auth.AuthService/DeleteOrganization': EndpointSync.unary(method=MethodInfo(name='DeleteOrganization', service_name='textql.rpc.auth.AuthService', input=auth__pb2.DeleteOrganizationRequest, output=auth__pb2.DeleteOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_organization)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.auth.AuthService'

class AuthServiceClientSync(ConnectClientSync):

    def start_session(self, request: auth__pb2.StartSessionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.SessionResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='StartSession', service_name='textql.rpc.auth.AuthService', input=auth__pb2.StartSessionRequest, output=auth__pb2.SessionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def renew_session(self, request: auth__pb2.RenewSessionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.SessionResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RenewSession', service_name='textql.rpc.auth.AuthService', input=auth__pb2.RenewSessionRequest, output=auth__pb2.SessionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def renew_long_term_access_token(self, request: auth__pb2.RenewLongTermAccessTokenRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.LongTermAccessTokenResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RenewLongTermAccessToken', service_name='textql.rpc.auth.AuthService', input=auth__pb2.RenewLongTermAccessTokenRequest, output=auth__pb2.LongTermAccessTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def create_org(self, request: auth__pb2.CreateOrgRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.CreateOrgResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateOrg', service_name='textql.rpc.auth.AuthService', input=auth__pb2.CreateOrgRequest, output=auth__pb2.CreateOrgResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def find_orgs_by_slug(self, request: auth__pb2.FindOrgsBySlugRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.FindOrgsBySlugResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='FindOrgsBySlug', service_name='textql.rpc.auth.AuthService', input=auth__pb2.FindOrgsBySlugRequest, output=auth__pb2.FindOrgsBySlugResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def update_org(self, request: auth__pb2.UpdateOrgRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.UpdateOrgResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateOrg', service_name='textql.rpc.auth.AuthService', input=auth__pb2.UpdateOrgRequest, output=auth__pb2.UpdateOrgResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_org_by_id(self, request: auth__pb2.GetOrgByIdRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.GetOrgByIdResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetOrgById', service_name='textql.rpc.auth.AuthService', input=auth__pb2.GetOrgByIdRequest, output=auth__pb2.GetOrgByIdResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def create_org_member(self, request: auth__pb2.CreateOrgMemberRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.CreateOrgMemberResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateOrgMember', service_name='textql.rpc.auth.AuthService', input=auth__pb2.CreateOrgMemberRequest, output=auth__pb2.CreateOrgMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def find_members_in_org(self, request: auth__pb2.FindMembersInOrgRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.FindMembersInOrgResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='FindMembersInOrg', service_name='textql.rpc.auth.AuthService', input=auth__pb2.FindMembersInOrgRequest, output=auth__pb2.FindMembersInOrgResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def email_invite_member(self, request: auth__pb2.EmailInviteMemberRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.EmailInviteMemberResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='EmailInviteMember', service_name='textql.rpc.auth.AuthService', input=auth__pb2.EmailInviteMemberRequest, output=auth__pb2.EmailInviteMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_org_member_by_member_id(self, request: auth__pb2.GetOrgMemberByMemberIdRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.GetOrgMemberByMemberIdResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetOrgMemberByMemberId', service_name='textql.rpc.auth.AuthService', input=auth__pb2.GetOrgMemberByMemberIdRequest, output=auth__pb2.GetOrgMemberByMemberIdResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def delete_member(self, request: auth__pb2.DeleteMemberRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.DeleteMemberResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteMember', service_name='textql.rpc.auth.AuthService', input=auth__pb2.DeleteMemberRequest, output=auth__pb2.DeleteMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def delete_organization(self, request: auth__pb2.DeleteOrganizationRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.DeleteOrganizationResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteOrganization', service_name='textql.rpc.auth.AuthService', input=auth__pb2.DeleteOrganizationRequest, output=auth__pb2.DeleteOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)