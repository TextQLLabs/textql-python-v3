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
from .. import auth_pb2 as auth__pb2
from . import auth_pb2 as public_dot_auth__pb2

class PublicAuthService(Protocol):

    async def login_email_start(self, request: public_dot_auth__pb2.LoginEmailStartRequest, ctx: RequestContext) -> public_dot_auth__pb2.LoginEmailStartResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def validate_intermediary_token(self, request: public_dot_auth__pb2.ValidateIntermediaryTokenRequest, ctx: RequestContext) -> public_dot_auth__pb2.ValidateIntermediaryTokenResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def validate_long_term_token(self, request: public_dot_auth__pb2.ValidateLongTermTokenRequest, ctx: RequestContext) -> public_dot_auth__pb2.ValidateLongTermTokenResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def exchange_intermediary_token(self, request: public_dot_auth__pb2.ExchangeIntermediaryTokenRequest, ctx: RequestContext) -> auth__pb2.LongTermAccessTokenResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def logout(self, request: public_dot_auth__pb2.LogoutRequest, ctx: RequestContext) -> public_dot_auth__pb2.LogoutResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_o_i_d_c_auth_url(self, request: public_dot_auth__pb2.GetOIDCAuthUrlRequest, ctx: RequestContext) -> public_dot_auth__pb2.GetOIDCAuthUrlResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def handle_o_i_d_c_callback(self, request: public_dot_auth__pb2.HandleOIDCCallbackRequest, ctx: RequestContext) -> public_dot_auth__pb2.HandleOIDCCallbackResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def create_s_s_o_organization(self, request: public_dot_auth__pb2.CreateSSOOrganizationRequest, ctx: RequestContext) -> public_dot_auth__pb2.CreateSSOOrganizationResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_organizations(self, request: public_dot_auth__pb2.ListOrganizationsRequest, ctx: RequestContext) -> public_dot_auth__pb2.ListOrganizationsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_member(self, request: public_dot_auth__pb2.GetMemberRequest, ctx: RequestContext) -> public_dot_auth__pb2.GetMemberResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_organization(self, request: public_dot_auth__pb2.GetOrganizationRequest, ctx: RequestContext) -> public_dot_auth__pb2.GetOrganizationResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_member_in_org_by_id(self, request: public_dot_auth__pb2.GetMemberInOrgByIdRequest, ctx: RequestContext) -> public_dot_auth__pb2.GetMemberInOrgByIdResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def exchange_session(self, request: public_dot_auth__pb2.ExchangeSessionRequest, ctx: RequestContext) -> public_dot_auth__pb2.ExchangeSessionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_default_connector(self, request: public_dot_auth__pb2.UpdateDefaultConnectorRequest, ctx: RequestContext) -> public_dot_auth__pb2.UpdateDefaultConnectorResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_o_i_d_c_config(self, request: public_dot_auth__pb2.GetOIDCConfigRequest, ctx: RequestContext) -> public_dot_auth__pb2.GetOIDCConfigResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def save_o_i_d_c_config(self, request: public_dot_auth__pb2.SaveOIDCConfigRequest, ctx: RequestContext) -> public_dot_auth__pb2.SaveOIDCConfigResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def check_domain_for_o_i_d_c(self, request: public_dot_auth__pb2.CheckDomainForOIDCRequest, ctx: RequestContext) -> public_dot_auth__pb2.CheckDomainForOIDCResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_o_i_d_c_providers(self, request: public_dot_auth__pb2.ListOIDCProvidersRequest, ctx: RequestContext) -> public_dot_auth__pb2.ListOIDCProvidersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def create_o_i_d_c_provider(self, request: public_dot_auth__pb2.CreateOIDCProviderRequest, ctx: RequestContext) -> public_dot_auth__pb2.CreateOIDCProviderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_o_i_d_c_provider(self, request: public_dot_auth__pb2.UpdateOIDCProviderRequest, ctx: RequestContext) -> public_dot_auth__pb2.UpdateOIDCProviderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_o_i_d_c_provider(self, request: public_dot_auth__pb2.DeleteOIDCProviderRequest, ctx: RequestContext) -> public_dot_auth__pb2.DeleteOIDCProviderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def add_org_o_i_d_c_provider(self, request: public_dot_auth__pb2.AddOrgOIDCProviderRequest, ctx: RequestContext) -> public_dot_auth__pb2.AddOrgOIDCProviderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def remove_org_o_i_d_c_provider(self, request: public_dot_auth__pb2.RemoveOrgOIDCProviderRequest, ctx: RequestContext) -> public_dot_auth__pb2.RemoveOrgOIDCProviderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_org_o_i_d_c_providers(self, request: public_dot_auth__pb2.UpdateOrgOIDCProvidersRequest, ctx: RequestContext) -> public_dot_auth__pb2.UpdateOrgOIDCProvidersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_org_o_i_d_c_providers(self, request: public_dot_auth__pb2.GetOrgOIDCProvidersRequest, ctx: RequestContext) -> public_dot_auth__pb2.GetOrgOIDCProvidersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_google_o_auth_url(self, request: public_dot_auth__pb2.GetGoogleOAuthUrlRequest, ctx: RequestContext) -> public_dot_auth__pb2.GetGoogleOAuthUrlResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def handle_google_o_auth_callback(self, request: public_dot_auth__pb2.HandleGoogleOAuthCallbackRequest, ctx: RequestContext) -> public_dot_auth__pb2.HandleGoogleOAuthCallbackResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_org_theme(self, request: public_dot_auth__pb2.UpdateOrgThemeRequest, ctx: RequestContext) -> public_dot_auth__pb2.UpdateOrgThemeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_org_tool_restrictions(self, request: public_dot_auth__pb2.UpdateOrgToolRestrictionsRequest, ctx: RequestContext) -> public_dot_auth__pb2.UpdateOrgToolRestrictionsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def create_logo_upload_presign_url(self, request: public_dot_auth__pb2.CreateLogoUploadPresignUrlRequest, ctx: RequestContext) -> public_dot_auth__pb2.CreateLogoUploadPresignUrlResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def process_logo_upload_presign_url(self, request: public_dot_auth__pb2.ProcessLogoUploadPresignUrlRequest, ctx: RequestContext) -> public_dot_auth__pb2.ProcessLogoUploadPresignUrlResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def upload_member_image(self, request: public_dot_auth__pb2.UploadMemberImageRequest, ctx: RequestContext) -> public_dot_auth__pb2.UploadMemberImageResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def generate_magic_link_for_user(self, request: public_dot_auth__pb2.GenerateMagicLinkForUserRequest, ctx: RequestContext) -> public_dot_auth__pb2.GenerateMagicLinkForUserResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_console_auth_token(self, request: public_dot_auth__pb2.GetConsoleAuthTokenRequest, ctx: RequestContext) -> public_dot_auth__pb2.GetConsoleAuthTokenResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def create_organization(self, request: public_dot_auth__pb2.CreateOrganizationRequest, ctx: RequestContext) -> public_dot_auth__pb2.CreateOrganizationResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def create_sibling_organization(self, request: public_dot_auth__pb2.CreateSiblingOrganizationRequest, ctx: RequestContext) -> public_dot_auth__pb2.CreateSiblingOrganizationResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def verify_api_key(self, request: public_dot_auth__pb2.VerifyApiKeyRequest, ctx: RequestContext) -> public_dot_auth__pb2.VerifyApiKeyResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_org_o_auth_clients(self, request: public_dot_auth__pb2.ListOrgOAuthClientsRequest, ctx: RequestContext) -> public_dot_auth__pb2.ListOrgOAuthClientsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def create_org_o_auth_client(self, request: public_dot_auth__pb2.CreateOrgOAuthClientRequest, ctx: RequestContext) -> public_dot_auth__pb2.CreateOrgOAuthClientResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_org_o_auth_client(self, request: public_dot_auth__pb2.UpdateOrgOAuthClientRequest, ctx: RequestContext) -> public_dot_auth__pb2.UpdateOrgOAuthClientResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def rotate_org_o_auth_client_secret(self, request: public_dot_auth__pb2.RotateOrgOAuthClientSecretRequest, ctx: RequestContext) -> public_dot_auth__pb2.RotateOrgOAuthClientSecretResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def revoke_org_o_auth_client(self, request: public_dot_auth__pb2.RevokeOrgOAuthClientRequest, ctx: RequestContext) -> public_dot_auth__pb2.RevokeOrgOAuthClientResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_org_o_auth_client(self, request: public_dot_auth__pb2.DeleteOrgOAuthClientRequest, ctx: RequestContext) -> public_dot_auth__pb2.DeleteOrgOAuthClientResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_my_authorized_apps(self, request: public_dot_auth__pb2.ListMyAuthorizedAppsRequest, ctx: RequestContext) -> public_dot_auth__pb2.ListMyAuthorizedAppsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def revoke_my_authorized_app(self, request: public_dot_auth__pb2.RevokeMyAuthorizedAppRequest, ctx: RequestContext) -> public_dot_auth__pb2.RevokeMyAuthorizedAppResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_o_auth_scopes(self, request: public_dot_auth__pb2.ListOAuthScopesRequest, ctx: RequestContext) -> public_dot_auth__pb2.ListOAuthScopesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class PublicAuthServiceASGIApplication(ConnectASGIApplication[PublicAuthService]):

    def __init__(self, service: PublicAuthService | AsyncGenerator[PublicAuthService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.auth.PublicAuthService/LoginEmailStart': Endpoint.unary(method=MethodInfo(name='LoginEmailStart', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.LoginEmailStartRequest, output=public_dot_auth__pb2.LoginEmailStartResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.login_email_start), '/textql.rpc.public.auth.PublicAuthService/ValidateIntermediaryToken': Endpoint.unary(method=MethodInfo(name='ValidateIntermediaryToken', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ValidateIntermediaryTokenRequest, output=public_dot_auth__pb2.ValidateIntermediaryTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.validate_intermediary_token), '/textql.rpc.public.auth.PublicAuthService/ValidateLongTermToken': Endpoint.unary(method=MethodInfo(name='ValidateLongTermToken', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ValidateLongTermTokenRequest, output=public_dot_auth__pb2.ValidateLongTermTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.validate_long_term_token), '/textql.rpc.public.auth.PublicAuthService/ExchangeIntermediaryToken': Endpoint.unary(method=MethodInfo(name='ExchangeIntermediaryToken', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ExchangeIntermediaryTokenRequest, output=auth__pb2.LongTermAccessTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.exchange_intermediary_token), '/textql.rpc.public.auth.PublicAuthService/Logout': Endpoint.unary(method=MethodInfo(name='Logout', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.LogoutRequest, output=public_dot_auth__pb2.LogoutResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.logout), '/textql.rpc.public.auth.PublicAuthService/GetOIDCAuthUrl': Endpoint.unary(method=MethodInfo(name='GetOIDCAuthUrl', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetOIDCAuthUrlRequest, output=public_dot_auth__pb2.GetOIDCAuthUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_o_i_d_c_auth_url), '/textql.rpc.public.auth.PublicAuthService/HandleOIDCCallback': Endpoint.unary(method=MethodInfo(name='HandleOIDCCallback', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.HandleOIDCCallbackRequest, output=public_dot_auth__pb2.HandleOIDCCallbackResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.handle_o_i_d_c_callback), '/textql.rpc.public.auth.PublicAuthService/CreateSSOOrganization': Endpoint.unary(method=MethodInfo(name='CreateSSOOrganization', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CreateSSOOrganizationRequest, output=public_dot_auth__pb2.CreateSSOOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_s_s_o_organization), '/textql.rpc.public.auth.PublicAuthService/ListOrganizations': Endpoint.unary(method=MethodInfo(name='ListOrganizations', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ListOrganizationsRequest, output=public_dot_auth__pb2.ListOrganizationsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_organizations), '/textql.rpc.public.auth.PublicAuthService/GetMember': Endpoint.unary(method=MethodInfo(name='GetMember', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetMemberRequest, output=public_dot_auth__pb2.GetMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_member), '/textql.rpc.public.auth.PublicAuthService/GetOrganization': Endpoint.unary(method=MethodInfo(name='GetOrganization', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetOrganizationRequest, output=public_dot_auth__pb2.GetOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_organization), '/textql.rpc.public.auth.PublicAuthService/GetMemberInOrgById': Endpoint.unary(method=MethodInfo(name='GetMemberInOrgById', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetMemberInOrgByIdRequest, output=public_dot_auth__pb2.GetMemberInOrgByIdResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_member_in_org_by_id), '/textql.rpc.public.auth.PublicAuthService/ExchangeSession': Endpoint.unary(method=MethodInfo(name='ExchangeSession', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ExchangeSessionRequest, output=public_dot_auth__pb2.ExchangeSessionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.exchange_session), '/textql.rpc.public.auth.PublicAuthService/UpdateDefaultConnector': Endpoint.unary(method=MethodInfo(name='UpdateDefaultConnector', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UpdateDefaultConnectorRequest, output=public_dot_auth__pb2.UpdateDefaultConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_default_connector), '/textql.rpc.public.auth.PublicAuthService/GetOIDCConfig': Endpoint.unary(method=MethodInfo(name='GetOIDCConfig', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetOIDCConfigRequest, output=public_dot_auth__pb2.GetOIDCConfigResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_o_i_d_c_config), '/textql.rpc.public.auth.PublicAuthService/SaveOIDCConfig': Endpoint.unary(method=MethodInfo(name='SaveOIDCConfig', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.SaveOIDCConfigRequest, output=public_dot_auth__pb2.SaveOIDCConfigResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.save_o_i_d_c_config), '/textql.rpc.public.auth.PublicAuthService/CheckDomainForOIDC': Endpoint.unary(method=MethodInfo(name='CheckDomainForOIDC', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CheckDomainForOIDCRequest, output=public_dot_auth__pb2.CheckDomainForOIDCResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.check_domain_for_o_i_d_c), '/textql.rpc.public.auth.PublicAuthService/ListOIDCProviders': Endpoint.unary(method=MethodInfo(name='ListOIDCProviders', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ListOIDCProvidersRequest, output=public_dot_auth__pb2.ListOIDCProvidersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_o_i_d_c_providers), '/textql.rpc.public.auth.PublicAuthService/CreateOIDCProvider': Endpoint.unary(method=MethodInfo(name='CreateOIDCProvider', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CreateOIDCProviderRequest, output=public_dot_auth__pb2.CreateOIDCProviderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_o_i_d_c_provider), '/textql.rpc.public.auth.PublicAuthService/UpdateOIDCProvider': Endpoint.unary(method=MethodInfo(name='UpdateOIDCProvider', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UpdateOIDCProviderRequest, output=public_dot_auth__pb2.UpdateOIDCProviderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_o_i_d_c_provider), '/textql.rpc.public.auth.PublicAuthService/DeleteOIDCProvider': Endpoint.unary(method=MethodInfo(name='DeleteOIDCProvider', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.DeleteOIDCProviderRequest, output=public_dot_auth__pb2.DeleteOIDCProviderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_o_i_d_c_provider), '/textql.rpc.public.auth.PublicAuthService/AddOrgOIDCProvider': Endpoint.unary(method=MethodInfo(name='AddOrgOIDCProvider', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.AddOrgOIDCProviderRequest, output=public_dot_auth__pb2.AddOrgOIDCProviderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.add_org_o_i_d_c_provider), '/textql.rpc.public.auth.PublicAuthService/RemoveOrgOIDCProvider': Endpoint.unary(method=MethodInfo(name='RemoveOrgOIDCProvider', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.RemoveOrgOIDCProviderRequest, output=public_dot_auth__pb2.RemoveOrgOIDCProviderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.remove_org_o_i_d_c_provider), '/textql.rpc.public.auth.PublicAuthService/UpdateOrgOIDCProviders': Endpoint.unary(method=MethodInfo(name='UpdateOrgOIDCProviders', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UpdateOrgOIDCProvidersRequest, output=public_dot_auth__pb2.UpdateOrgOIDCProvidersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_org_o_i_d_c_providers), '/textql.rpc.public.auth.PublicAuthService/GetOrgOIDCProviders': Endpoint.unary(method=MethodInfo(name='GetOrgOIDCProviders', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetOrgOIDCProvidersRequest, output=public_dot_auth__pb2.GetOrgOIDCProvidersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_org_o_i_d_c_providers), '/textql.rpc.public.auth.PublicAuthService/GetGoogleOAuthUrl': Endpoint.unary(method=MethodInfo(name='GetGoogleOAuthUrl', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetGoogleOAuthUrlRequest, output=public_dot_auth__pb2.GetGoogleOAuthUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_google_o_auth_url), '/textql.rpc.public.auth.PublicAuthService/HandleGoogleOAuthCallback': Endpoint.unary(method=MethodInfo(name='HandleGoogleOAuthCallback', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.HandleGoogleOAuthCallbackRequest, output=public_dot_auth__pb2.HandleGoogleOAuthCallbackResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.handle_google_o_auth_callback), '/textql.rpc.public.auth.PublicAuthService/UpdateOrgTheme': Endpoint.unary(method=MethodInfo(name='UpdateOrgTheme', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UpdateOrgThemeRequest, output=public_dot_auth__pb2.UpdateOrgThemeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_org_theme), '/textql.rpc.public.auth.PublicAuthService/UpdateOrgToolRestrictions': Endpoint.unary(method=MethodInfo(name='UpdateOrgToolRestrictions', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UpdateOrgToolRestrictionsRequest, output=public_dot_auth__pb2.UpdateOrgToolRestrictionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_org_tool_restrictions), '/textql.rpc.public.auth.PublicAuthService/CreateLogoUploadPresignUrl': Endpoint.unary(method=MethodInfo(name='CreateLogoUploadPresignUrl', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CreateLogoUploadPresignUrlRequest, output=public_dot_auth__pb2.CreateLogoUploadPresignUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_logo_upload_presign_url), '/textql.rpc.public.auth.PublicAuthService/ProcessLogoUploadPresignUrl': Endpoint.unary(method=MethodInfo(name='ProcessLogoUploadPresignUrl', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ProcessLogoUploadPresignUrlRequest, output=public_dot_auth__pb2.ProcessLogoUploadPresignUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.process_logo_upload_presign_url), '/textql.rpc.public.auth.PublicAuthService/UploadMemberImage': Endpoint.unary(method=MethodInfo(name='UploadMemberImage', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UploadMemberImageRequest, output=public_dot_auth__pb2.UploadMemberImageResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.upload_member_image), '/textql.rpc.public.auth.PublicAuthService/GenerateMagicLinkForUser': Endpoint.unary(method=MethodInfo(name='GenerateMagicLinkForUser', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GenerateMagicLinkForUserRequest, output=public_dot_auth__pb2.GenerateMagicLinkForUserResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.generate_magic_link_for_user), '/textql.rpc.public.auth.PublicAuthService/GetConsoleAuthToken': Endpoint.unary(method=MethodInfo(name='GetConsoleAuthToken', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetConsoleAuthTokenRequest, output=public_dot_auth__pb2.GetConsoleAuthTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_console_auth_token), '/textql.rpc.public.auth.PublicAuthService/CreateOrganization': Endpoint.unary(method=MethodInfo(name='CreateOrganization', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CreateOrganizationRequest, output=public_dot_auth__pb2.CreateOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_organization), '/textql.rpc.public.auth.PublicAuthService/CreateSiblingOrganization': Endpoint.unary(method=MethodInfo(name='CreateSiblingOrganization', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CreateSiblingOrganizationRequest, output=public_dot_auth__pb2.CreateSiblingOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_sibling_organization), '/textql.rpc.public.auth.PublicAuthService/VerifyApiKey': Endpoint.unary(method=MethodInfo(name='VerifyApiKey', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.VerifyApiKeyRequest, output=public_dot_auth__pb2.VerifyApiKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.verify_api_key), '/textql.rpc.public.auth.PublicAuthService/ListOrgOAuthClients': Endpoint.unary(method=MethodInfo(name='ListOrgOAuthClients', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ListOrgOAuthClientsRequest, output=public_dot_auth__pb2.ListOrgOAuthClientsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_org_o_auth_clients), '/textql.rpc.public.auth.PublicAuthService/CreateOrgOAuthClient': Endpoint.unary(method=MethodInfo(name='CreateOrgOAuthClient', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CreateOrgOAuthClientRequest, output=public_dot_auth__pb2.CreateOrgOAuthClientResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_org_o_auth_client), '/textql.rpc.public.auth.PublicAuthService/UpdateOrgOAuthClient': Endpoint.unary(method=MethodInfo(name='UpdateOrgOAuthClient', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UpdateOrgOAuthClientRequest, output=public_dot_auth__pb2.UpdateOrgOAuthClientResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_org_o_auth_client), '/textql.rpc.public.auth.PublicAuthService/RotateOrgOAuthClientSecret': Endpoint.unary(method=MethodInfo(name='RotateOrgOAuthClientSecret', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.RotateOrgOAuthClientSecretRequest, output=public_dot_auth__pb2.RotateOrgOAuthClientSecretResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.rotate_org_o_auth_client_secret), '/textql.rpc.public.auth.PublicAuthService/RevokeOrgOAuthClient': Endpoint.unary(method=MethodInfo(name='RevokeOrgOAuthClient', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.RevokeOrgOAuthClientRequest, output=public_dot_auth__pb2.RevokeOrgOAuthClientResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.revoke_org_o_auth_client), '/textql.rpc.public.auth.PublicAuthService/DeleteOrgOAuthClient': Endpoint.unary(method=MethodInfo(name='DeleteOrgOAuthClient', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.DeleteOrgOAuthClientRequest, output=public_dot_auth__pb2.DeleteOrgOAuthClientResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_org_o_auth_client), '/textql.rpc.public.auth.PublicAuthService/ListMyAuthorizedApps': Endpoint.unary(method=MethodInfo(name='ListMyAuthorizedApps', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ListMyAuthorizedAppsRequest, output=public_dot_auth__pb2.ListMyAuthorizedAppsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_my_authorized_apps), '/textql.rpc.public.auth.PublicAuthService/RevokeMyAuthorizedApp': Endpoint.unary(method=MethodInfo(name='RevokeMyAuthorizedApp', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.RevokeMyAuthorizedAppRequest, output=public_dot_auth__pb2.RevokeMyAuthorizedAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.revoke_my_authorized_app), '/textql.rpc.public.auth.PublicAuthService/ListOAuthScopes': Endpoint.unary(method=MethodInfo(name='ListOAuthScopes', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ListOAuthScopesRequest, output=public_dot_auth__pb2.ListOAuthScopesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_o_auth_scopes)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.auth.PublicAuthService'

class PublicAuthServiceClient(ConnectClient):

    async def login_email_start(self, request: public_dot_auth__pb2.LoginEmailStartRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.LoginEmailStartResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='LoginEmailStart', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.LoginEmailStartRequest, output=public_dot_auth__pb2.LoginEmailStartResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def validate_intermediary_token(self, request: public_dot_auth__pb2.ValidateIntermediaryTokenRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.ValidateIntermediaryTokenResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ValidateIntermediaryToken', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ValidateIntermediaryTokenRequest, output=public_dot_auth__pb2.ValidateIntermediaryTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def validate_long_term_token(self, request: public_dot_auth__pb2.ValidateLongTermTokenRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.ValidateLongTermTokenResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ValidateLongTermToken', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ValidateLongTermTokenRequest, output=public_dot_auth__pb2.ValidateLongTermTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def exchange_intermediary_token(self, request: public_dot_auth__pb2.ExchangeIntermediaryTokenRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.LongTermAccessTokenResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ExchangeIntermediaryToken', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ExchangeIntermediaryTokenRequest, output=auth__pb2.LongTermAccessTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def logout(self, request: public_dot_auth__pb2.LogoutRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.LogoutResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='Logout', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.LogoutRequest, output=public_dot_auth__pb2.LogoutResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_o_i_d_c_auth_url(self, request: public_dot_auth__pb2.GetOIDCAuthUrlRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.GetOIDCAuthUrlResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetOIDCAuthUrl', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetOIDCAuthUrlRequest, output=public_dot_auth__pb2.GetOIDCAuthUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def handle_o_i_d_c_callback(self, request: public_dot_auth__pb2.HandleOIDCCallbackRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.HandleOIDCCallbackResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='HandleOIDCCallback', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.HandleOIDCCallbackRequest, output=public_dot_auth__pb2.HandleOIDCCallbackResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def create_s_s_o_organization(self, request: public_dot_auth__pb2.CreateSSOOrganizationRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.CreateSSOOrganizationResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateSSOOrganization', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CreateSSOOrganizationRequest, output=public_dot_auth__pb2.CreateSSOOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_organizations(self, request: public_dot_auth__pb2.ListOrganizationsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.ListOrganizationsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListOrganizations', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ListOrganizationsRequest, output=public_dot_auth__pb2.ListOrganizationsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_member(self, request: public_dot_auth__pb2.GetMemberRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.GetMemberResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetMember', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetMemberRequest, output=public_dot_auth__pb2.GetMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_organization(self, request: public_dot_auth__pb2.GetOrganizationRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.GetOrganizationResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetOrganization', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetOrganizationRequest, output=public_dot_auth__pb2.GetOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_member_in_org_by_id(self, request: public_dot_auth__pb2.GetMemberInOrgByIdRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.GetMemberInOrgByIdResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetMemberInOrgById', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetMemberInOrgByIdRequest, output=public_dot_auth__pb2.GetMemberInOrgByIdResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def exchange_session(self, request: public_dot_auth__pb2.ExchangeSessionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.ExchangeSessionResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ExchangeSession', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ExchangeSessionRequest, output=public_dot_auth__pb2.ExchangeSessionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def update_default_connector(self, request: public_dot_auth__pb2.UpdateDefaultConnectorRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.UpdateDefaultConnectorResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateDefaultConnector', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UpdateDefaultConnectorRequest, output=public_dot_auth__pb2.UpdateDefaultConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_o_i_d_c_config(self, request: public_dot_auth__pb2.GetOIDCConfigRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.GetOIDCConfigResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetOIDCConfig', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetOIDCConfigRequest, output=public_dot_auth__pb2.GetOIDCConfigResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def save_o_i_d_c_config(self, request: public_dot_auth__pb2.SaveOIDCConfigRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.SaveOIDCConfigResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='SaveOIDCConfig', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.SaveOIDCConfigRequest, output=public_dot_auth__pb2.SaveOIDCConfigResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def check_domain_for_o_i_d_c(self, request: public_dot_auth__pb2.CheckDomainForOIDCRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.CheckDomainForOIDCResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CheckDomainForOIDC', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CheckDomainForOIDCRequest, output=public_dot_auth__pb2.CheckDomainForOIDCResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_o_i_d_c_providers(self, request: public_dot_auth__pb2.ListOIDCProvidersRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.ListOIDCProvidersResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListOIDCProviders', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ListOIDCProvidersRequest, output=public_dot_auth__pb2.ListOIDCProvidersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def create_o_i_d_c_provider(self, request: public_dot_auth__pb2.CreateOIDCProviderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.CreateOIDCProviderResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateOIDCProvider', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CreateOIDCProviderRequest, output=public_dot_auth__pb2.CreateOIDCProviderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def update_o_i_d_c_provider(self, request: public_dot_auth__pb2.UpdateOIDCProviderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.UpdateOIDCProviderResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateOIDCProvider', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UpdateOIDCProviderRequest, output=public_dot_auth__pb2.UpdateOIDCProviderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def delete_o_i_d_c_provider(self, request: public_dot_auth__pb2.DeleteOIDCProviderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.DeleteOIDCProviderResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteOIDCProvider', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.DeleteOIDCProviderRequest, output=public_dot_auth__pb2.DeleteOIDCProviderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def add_org_o_i_d_c_provider(self, request: public_dot_auth__pb2.AddOrgOIDCProviderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.AddOrgOIDCProviderResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='AddOrgOIDCProvider', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.AddOrgOIDCProviderRequest, output=public_dot_auth__pb2.AddOrgOIDCProviderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def remove_org_o_i_d_c_provider(self, request: public_dot_auth__pb2.RemoveOrgOIDCProviderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.RemoveOrgOIDCProviderResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RemoveOrgOIDCProvider', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.RemoveOrgOIDCProviderRequest, output=public_dot_auth__pb2.RemoveOrgOIDCProviderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def update_org_o_i_d_c_providers(self, request: public_dot_auth__pb2.UpdateOrgOIDCProvidersRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.UpdateOrgOIDCProvidersResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateOrgOIDCProviders', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UpdateOrgOIDCProvidersRequest, output=public_dot_auth__pb2.UpdateOrgOIDCProvidersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_org_o_i_d_c_providers(self, request: public_dot_auth__pb2.GetOrgOIDCProvidersRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.GetOrgOIDCProvidersResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetOrgOIDCProviders', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetOrgOIDCProvidersRequest, output=public_dot_auth__pb2.GetOrgOIDCProvidersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_google_o_auth_url(self, request: public_dot_auth__pb2.GetGoogleOAuthUrlRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.GetGoogleOAuthUrlResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetGoogleOAuthUrl', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetGoogleOAuthUrlRequest, output=public_dot_auth__pb2.GetGoogleOAuthUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def handle_google_o_auth_callback(self, request: public_dot_auth__pb2.HandleGoogleOAuthCallbackRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.HandleGoogleOAuthCallbackResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='HandleGoogleOAuthCallback', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.HandleGoogleOAuthCallbackRequest, output=public_dot_auth__pb2.HandleGoogleOAuthCallbackResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def update_org_theme(self, request: public_dot_auth__pb2.UpdateOrgThemeRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.UpdateOrgThemeResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateOrgTheme', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UpdateOrgThemeRequest, output=public_dot_auth__pb2.UpdateOrgThemeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def update_org_tool_restrictions(self, request: public_dot_auth__pb2.UpdateOrgToolRestrictionsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.UpdateOrgToolRestrictionsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateOrgToolRestrictions', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UpdateOrgToolRestrictionsRequest, output=public_dot_auth__pb2.UpdateOrgToolRestrictionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def create_logo_upload_presign_url(self, request: public_dot_auth__pb2.CreateLogoUploadPresignUrlRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.CreateLogoUploadPresignUrlResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateLogoUploadPresignUrl', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CreateLogoUploadPresignUrlRequest, output=public_dot_auth__pb2.CreateLogoUploadPresignUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def process_logo_upload_presign_url(self, request: public_dot_auth__pb2.ProcessLogoUploadPresignUrlRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.ProcessLogoUploadPresignUrlResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ProcessLogoUploadPresignUrl', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ProcessLogoUploadPresignUrlRequest, output=public_dot_auth__pb2.ProcessLogoUploadPresignUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def upload_member_image(self, request: public_dot_auth__pb2.UploadMemberImageRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.UploadMemberImageResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UploadMemberImage', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UploadMemberImageRequest, output=public_dot_auth__pb2.UploadMemberImageResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def generate_magic_link_for_user(self, request: public_dot_auth__pb2.GenerateMagicLinkForUserRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.GenerateMagicLinkForUserResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GenerateMagicLinkForUser', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GenerateMagicLinkForUserRequest, output=public_dot_auth__pb2.GenerateMagicLinkForUserResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_console_auth_token(self, request: public_dot_auth__pb2.GetConsoleAuthTokenRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.GetConsoleAuthTokenResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetConsoleAuthToken', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetConsoleAuthTokenRequest, output=public_dot_auth__pb2.GetConsoleAuthTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def create_organization(self, request: public_dot_auth__pb2.CreateOrganizationRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.CreateOrganizationResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateOrganization', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CreateOrganizationRequest, output=public_dot_auth__pb2.CreateOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def create_sibling_organization(self, request: public_dot_auth__pb2.CreateSiblingOrganizationRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.CreateSiblingOrganizationResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateSiblingOrganization', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CreateSiblingOrganizationRequest, output=public_dot_auth__pb2.CreateSiblingOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def verify_api_key(self, request: public_dot_auth__pb2.VerifyApiKeyRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.VerifyApiKeyResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='VerifyApiKey', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.VerifyApiKeyRequest, output=public_dot_auth__pb2.VerifyApiKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_org_o_auth_clients(self, request: public_dot_auth__pb2.ListOrgOAuthClientsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_auth__pb2.ListOrgOAuthClientsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListOrgOAuthClients', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ListOrgOAuthClientsRequest, output=public_dot_auth__pb2.ListOrgOAuthClientsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def create_org_o_auth_client(self, request: public_dot_auth__pb2.CreateOrgOAuthClientRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.CreateOrgOAuthClientResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateOrgOAuthClient', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CreateOrgOAuthClientRequest, output=public_dot_auth__pb2.CreateOrgOAuthClientResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def update_org_o_auth_client(self, request: public_dot_auth__pb2.UpdateOrgOAuthClientRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.UpdateOrgOAuthClientResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateOrgOAuthClient', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UpdateOrgOAuthClientRequest, output=public_dot_auth__pb2.UpdateOrgOAuthClientResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def rotate_org_o_auth_client_secret(self, request: public_dot_auth__pb2.RotateOrgOAuthClientSecretRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.RotateOrgOAuthClientSecretResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RotateOrgOAuthClientSecret', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.RotateOrgOAuthClientSecretRequest, output=public_dot_auth__pb2.RotateOrgOAuthClientSecretResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def revoke_org_o_auth_client(self, request: public_dot_auth__pb2.RevokeOrgOAuthClientRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.RevokeOrgOAuthClientResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RevokeOrgOAuthClient', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.RevokeOrgOAuthClientRequest, output=public_dot_auth__pb2.RevokeOrgOAuthClientResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def delete_org_o_auth_client(self, request: public_dot_auth__pb2.DeleteOrgOAuthClientRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.DeleteOrgOAuthClientResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteOrgOAuthClient', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.DeleteOrgOAuthClientRequest, output=public_dot_auth__pb2.DeleteOrgOAuthClientResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_my_authorized_apps(self, request: public_dot_auth__pb2.ListMyAuthorizedAppsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_auth__pb2.ListMyAuthorizedAppsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListMyAuthorizedApps', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ListMyAuthorizedAppsRequest, output=public_dot_auth__pb2.ListMyAuthorizedAppsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def revoke_my_authorized_app(self, request: public_dot_auth__pb2.RevokeMyAuthorizedAppRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.RevokeMyAuthorizedAppResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RevokeMyAuthorizedApp', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.RevokeMyAuthorizedAppRequest, output=public_dot_auth__pb2.RevokeMyAuthorizedAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_o_auth_scopes(self, request: public_dot_auth__pb2.ListOAuthScopesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_auth__pb2.ListOAuthScopesResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListOAuthScopes', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ListOAuthScopesRequest, output=public_dot_auth__pb2.ListOAuthScopesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

class PublicAuthServiceSync(Protocol):

    def login_email_start(self, request: public_dot_auth__pb2.LoginEmailStartRequest, ctx: RequestContext) -> public_dot_auth__pb2.LoginEmailStartResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def validate_intermediary_token(self, request: public_dot_auth__pb2.ValidateIntermediaryTokenRequest, ctx: RequestContext) -> public_dot_auth__pb2.ValidateIntermediaryTokenResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def validate_long_term_token(self, request: public_dot_auth__pb2.ValidateLongTermTokenRequest, ctx: RequestContext) -> public_dot_auth__pb2.ValidateLongTermTokenResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def exchange_intermediary_token(self, request: public_dot_auth__pb2.ExchangeIntermediaryTokenRequest, ctx: RequestContext) -> auth__pb2.LongTermAccessTokenResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def logout(self, request: public_dot_auth__pb2.LogoutRequest, ctx: RequestContext) -> public_dot_auth__pb2.LogoutResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_o_i_d_c_auth_url(self, request: public_dot_auth__pb2.GetOIDCAuthUrlRequest, ctx: RequestContext) -> public_dot_auth__pb2.GetOIDCAuthUrlResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def handle_o_i_d_c_callback(self, request: public_dot_auth__pb2.HandleOIDCCallbackRequest, ctx: RequestContext) -> public_dot_auth__pb2.HandleOIDCCallbackResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def create_s_s_o_organization(self, request: public_dot_auth__pb2.CreateSSOOrganizationRequest, ctx: RequestContext) -> public_dot_auth__pb2.CreateSSOOrganizationResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_organizations(self, request: public_dot_auth__pb2.ListOrganizationsRequest, ctx: RequestContext) -> public_dot_auth__pb2.ListOrganizationsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_member(self, request: public_dot_auth__pb2.GetMemberRequest, ctx: RequestContext) -> public_dot_auth__pb2.GetMemberResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_organization(self, request: public_dot_auth__pb2.GetOrganizationRequest, ctx: RequestContext) -> public_dot_auth__pb2.GetOrganizationResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_member_in_org_by_id(self, request: public_dot_auth__pb2.GetMemberInOrgByIdRequest, ctx: RequestContext) -> public_dot_auth__pb2.GetMemberInOrgByIdResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def exchange_session(self, request: public_dot_auth__pb2.ExchangeSessionRequest, ctx: RequestContext) -> public_dot_auth__pb2.ExchangeSessionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_default_connector(self, request: public_dot_auth__pb2.UpdateDefaultConnectorRequest, ctx: RequestContext) -> public_dot_auth__pb2.UpdateDefaultConnectorResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_o_i_d_c_config(self, request: public_dot_auth__pb2.GetOIDCConfigRequest, ctx: RequestContext) -> public_dot_auth__pb2.GetOIDCConfigResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def save_o_i_d_c_config(self, request: public_dot_auth__pb2.SaveOIDCConfigRequest, ctx: RequestContext) -> public_dot_auth__pb2.SaveOIDCConfigResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def check_domain_for_o_i_d_c(self, request: public_dot_auth__pb2.CheckDomainForOIDCRequest, ctx: RequestContext) -> public_dot_auth__pb2.CheckDomainForOIDCResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_o_i_d_c_providers(self, request: public_dot_auth__pb2.ListOIDCProvidersRequest, ctx: RequestContext) -> public_dot_auth__pb2.ListOIDCProvidersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def create_o_i_d_c_provider(self, request: public_dot_auth__pb2.CreateOIDCProviderRequest, ctx: RequestContext) -> public_dot_auth__pb2.CreateOIDCProviderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_o_i_d_c_provider(self, request: public_dot_auth__pb2.UpdateOIDCProviderRequest, ctx: RequestContext) -> public_dot_auth__pb2.UpdateOIDCProviderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_o_i_d_c_provider(self, request: public_dot_auth__pb2.DeleteOIDCProviderRequest, ctx: RequestContext) -> public_dot_auth__pb2.DeleteOIDCProviderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def add_org_o_i_d_c_provider(self, request: public_dot_auth__pb2.AddOrgOIDCProviderRequest, ctx: RequestContext) -> public_dot_auth__pb2.AddOrgOIDCProviderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def remove_org_o_i_d_c_provider(self, request: public_dot_auth__pb2.RemoveOrgOIDCProviderRequest, ctx: RequestContext) -> public_dot_auth__pb2.RemoveOrgOIDCProviderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_org_o_i_d_c_providers(self, request: public_dot_auth__pb2.UpdateOrgOIDCProvidersRequest, ctx: RequestContext) -> public_dot_auth__pb2.UpdateOrgOIDCProvidersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_org_o_i_d_c_providers(self, request: public_dot_auth__pb2.GetOrgOIDCProvidersRequest, ctx: RequestContext) -> public_dot_auth__pb2.GetOrgOIDCProvidersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_google_o_auth_url(self, request: public_dot_auth__pb2.GetGoogleOAuthUrlRequest, ctx: RequestContext) -> public_dot_auth__pb2.GetGoogleOAuthUrlResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def handle_google_o_auth_callback(self, request: public_dot_auth__pb2.HandleGoogleOAuthCallbackRequest, ctx: RequestContext) -> public_dot_auth__pb2.HandleGoogleOAuthCallbackResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_org_theme(self, request: public_dot_auth__pb2.UpdateOrgThemeRequest, ctx: RequestContext) -> public_dot_auth__pb2.UpdateOrgThemeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_org_tool_restrictions(self, request: public_dot_auth__pb2.UpdateOrgToolRestrictionsRequest, ctx: RequestContext) -> public_dot_auth__pb2.UpdateOrgToolRestrictionsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def create_logo_upload_presign_url(self, request: public_dot_auth__pb2.CreateLogoUploadPresignUrlRequest, ctx: RequestContext) -> public_dot_auth__pb2.CreateLogoUploadPresignUrlResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def process_logo_upload_presign_url(self, request: public_dot_auth__pb2.ProcessLogoUploadPresignUrlRequest, ctx: RequestContext) -> public_dot_auth__pb2.ProcessLogoUploadPresignUrlResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def upload_member_image(self, request: public_dot_auth__pb2.UploadMemberImageRequest, ctx: RequestContext) -> public_dot_auth__pb2.UploadMemberImageResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def generate_magic_link_for_user(self, request: public_dot_auth__pb2.GenerateMagicLinkForUserRequest, ctx: RequestContext) -> public_dot_auth__pb2.GenerateMagicLinkForUserResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_console_auth_token(self, request: public_dot_auth__pb2.GetConsoleAuthTokenRequest, ctx: RequestContext) -> public_dot_auth__pb2.GetConsoleAuthTokenResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def create_organization(self, request: public_dot_auth__pb2.CreateOrganizationRequest, ctx: RequestContext) -> public_dot_auth__pb2.CreateOrganizationResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def create_sibling_organization(self, request: public_dot_auth__pb2.CreateSiblingOrganizationRequest, ctx: RequestContext) -> public_dot_auth__pb2.CreateSiblingOrganizationResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def verify_api_key(self, request: public_dot_auth__pb2.VerifyApiKeyRequest, ctx: RequestContext) -> public_dot_auth__pb2.VerifyApiKeyResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_org_o_auth_clients(self, request: public_dot_auth__pb2.ListOrgOAuthClientsRequest, ctx: RequestContext) -> public_dot_auth__pb2.ListOrgOAuthClientsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def create_org_o_auth_client(self, request: public_dot_auth__pb2.CreateOrgOAuthClientRequest, ctx: RequestContext) -> public_dot_auth__pb2.CreateOrgOAuthClientResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_org_o_auth_client(self, request: public_dot_auth__pb2.UpdateOrgOAuthClientRequest, ctx: RequestContext) -> public_dot_auth__pb2.UpdateOrgOAuthClientResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def rotate_org_o_auth_client_secret(self, request: public_dot_auth__pb2.RotateOrgOAuthClientSecretRequest, ctx: RequestContext) -> public_dot_auth__pb2.RotateOrgOAuthClientSecretResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def revoke_org_o_auth_client(self, request: public_dot_auth__pb2.RevokeOrgOAuthClientRequest, ctx: RequestContext) -> public_dot_auth__pb2.RevokeOrgOAuthClientResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_org_o_auth_client(self, request: public_dot_auth__pb2.DeleteOrgOAuthClientRequest, ctx: RequestContext) -> public_dot_auth__pb2.DeleteOrgOAuthClientResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_my_authorized_apps(self, request: public_dot_auth__pb2.ListMyAuthorizedAppsRequest, ctx: RequestContext) -> public_dot_auth__pb2.ListMyAuthorizedAppsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def revoke_my_authorized_app(self, request: public_dot_auth__pb2.RevokeMyAuthorizedAppRequest, ctx: RequestContext) -> public_dot_auth__pb2.RevokeMyAuthorizedAppResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_o_auth_scopes(self, request: public_dot_auth__pb2.ListOAuthScopesRequest, ctx: RequestContext) -> public_dot_auth__pb2.ListOAuthScopesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class PublicAuthServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: PublicAuthServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.auth.PublicAuthService/LoginEmailStart': EndpointSync.unary(method=MethodInfo(name='LoginEmailStart', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.LoginEmailStartRequest, output=public_dot_auth__pb2.LoginEmailStartResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.login_email_start), '/textql.rpc.public.auth.PublicAuthService/ValidateIntermediaryToken': EndpointSync.unary(method=MethodInfo(name='ValidateIntermediaryToken', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ValidateIntermediaryTokenRequest, output=public_dot_auth__pb2.ValidateIntermediaryTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.validate_intermediary_token), '/textql.rpc.public.auth.PublicAuthService/ValidateLongTermToken': EndpointSync.unary(method=MethodInfo(name='ValidateLongTermToken', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ValidateLongTermTokenRequest, output=public_dot_auth__pb2.ValidateLongTermTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.validate_long_term_token), '/textql.rpc.public.auth.PublicAuthService/ExchangeIntermediaryToken': EndpointSync.unary(method=MethodInfo(name='ExchangeIntermediaryToken', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ExchangeIntermediaryTokenRequest, output=auth__pb2.LongTermAccessTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.exchange_intermediary_token), '/textql.rpc.public.auth.PublicAuthService/Logout': EndpointSync.unary(method=MethodInfo(name='Logout', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.LogoutRequest, output=public_dot_auth__pb2.LogoutResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.logout), '/textql.rpc.public.auth.PublicAuthService/GetOIDCAuthUrl': EndpointSync.unary(method=MethodInfo(name='GetOIDCAuthUrl', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetOIDCAuthUrlRequest, output=public_dot_auth__pb2.GetOIDCAuthUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_o_i_d_c_auth_url), '/textql.rpc.public.auth.PublicAuthService/HandleOIDCCallback': EndpointSync.unary(method=MethodInfo(name='HandleOIDCCallback', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.HandleOIDCCallbackRequest, output=public_dot_auth__pb2.HandleOIDCCallbackResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.handle_o_i_d_c_callback), '/textql.rpc.public.auth.PublicAuthService/CreateSSOOrganization': EndpointSync.unary(method=MethodInfo(name='CreateSSOOrganization', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CreateSSOOrganizationRequest, output=public_dot_auth__pb2.CreateSSOOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_s_s_o_organization), '/textql.rpc.public.auth.PublicAuthService/ListOrganizations': EndpointSync.unary(method=MethodInfo(name='ListOrganizations', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ListOrganizationsRequest, output=public_dot_auth__pb2.ListOrganizationsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_organizations), '/textql.rpc.public.auth.PublicAuthService/GetMember': EndpointSync.unary(method=MethodInfo(name='GetMember', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetMemberRequest, output=public_dot_auth__pb2.GetMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_member), '/textql.rpc.public.auth.PublicAuthService/GetOrganization': EndpointSync.unary(method=MethodInfo(name='GetOrganization', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetOrganizationRequest, output=public_dot_auth__pb2.GetOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_organization), '/textql.rpc.public.auth.PublicAuthService/GetMemberInOrgById': EndpointSync.unary(method=MethodInfo(name='GetMemberInOrgById', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetMemberInOrgByIdRequest, output=public_dot_auth__pb2.GetMemberInOrgByIdResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_member_in_org_by_id), '/textql.rpc.public.auth.PublicAuthService/ExchangeSession': EndpointSync.unary(method=MethodInfo(name='ExchangeSession', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ExchangeSessionRequest, output=public_dot_auth__pb2.ExchangeSessionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.exchange_session), '/textql.rpc.public.auth.PublicAuthService/UpdateDefaultConnector': EndpointSync.unary(method=MethodInfo(name='UpdateDefaultConnector', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UpdateDefaultConnectorRequest, output=public_dot_auth__pb2.UpdateDefaultConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_default_connector), '/textql.rpc.public.auth.PublicAuthService/GetOIDCConfig': EndpointSync.unary(method=MethodInfo(name='GetOIDCConfig', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetOIDCConfigRequest, output=public_dot_auth__pb2.GetOIDCConfigResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_o_i_d_c_config), '/textql.rpc.public.auth.PublicAuthService/SaveOIDCConfig': EndpointSync.unary(method=MethodInfo(name='SaveOIDCConfig', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.SaveOIDCConfigRequest, output=public_dot_auth__pb2.SaveOIDCConfigResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.save_o_i_d_c_config), '/textql.rpc.public.auth.PublicAuthService/CheckDomainForOIDC': EndpointSync.unary(method=MethodInfo(name='CheckDomainForOIDC', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CheckDomainForOIDCRequest, output=public_dot_auth__pb2.CheckDomainForOIDCResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.check_domain_for_o_i_d_c), '/textql.rpc.public.auth.PublicAuthService/ListOIDCProviders': EndpointSync.unary(method=MethodInfo(name='ListOIDCProviders', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ListOIDCProvidersRequest, output=public_dot_auth__pb2.ListOIDCProvidersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_o_i_d_c_providers), '/textql.rpc.public.auth.PublicAuthService/CreateOIDCProvider': EndpointSync.unary(method=MethodInfo(name='CreateOIDCProvider', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CreateOIDCProviderRequest, output=public_dot_auth__pb2.CreateOIDCProviderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_o_i_d_c_provider), '/textql.rpc.public.auth.PublicAuthService/UpdateOIDCProvider': EndpointSync.unary(method=MethodInfo(name='UpdateOIDCProvider', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UpdateOIDCProviderRequest, output=public_dot_auth__pb2.UpdateOIDCProviderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_o_i_d_c_provider), '/textql.rpc.public.auth.PublicAuthService/DeleteOIDCProvider': EndpointSync.unary(method=MethodInfo(name='DeleteOIDCProvider', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.DeleteOIDCProviderRequest, output=public_dot_auth__pb2.DeleteOIDCProviderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_o_i_d_c_provider), '/textql.rpc.public.auth.PublicAuthService/AddOrgOIDCProvider': EndpointSync.unary(method=MethodInfo(name='AddOrgOIDCProvider', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.AddOrgOIDCProviderRequest, output=public_dot_auth__pb2.AddOrgOIDCProviderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.add_org_o_i_d_c_provider), '/textql.rpc.public.auth.PublicAuthService/RemoveOrgOIDCProvider': EndpointSync.unary(method=MethodInfo(name='RemoveOrgOIDCProvider', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.RemoveOrgOIDCProviderRequest, output=public_dot_auth__pb2.RemoveOrgOIDCProviderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.remove_org_o_i_d_c_provider), '/textql.rpc.public.auth.PublicAuthService/UpdateOrgOIDCProviders': EndpointSync.unary(method=MethodInfo(name='UpdateOrgOIDCProviders', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UpdateOrgOIDCProvidersRequest, output=public_dot_auth__pb2.UpdateOrgOIDCProvidersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_org_o_i_d_c_providers), '/textql.rpc.public.auth.PublicAuthService/GetOrgOIDCProviders': EndpointSync.unary(method=MethodInfo(name='GetOrgOIDCProviders', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetOrgOIDCProvidersRequest, output=public_dot_auth__pb2.GetOrgOIDCProvidersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_org_o_i_d_c_providers), '/textql.rpc.public.auth.PublicAuthService/GetGoogleOAuthUrl': EndpointSync.unary(method=MethodInfo(name='GetGoogleOAuthUrl', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetGoogleOAuthUrlRequest, output=public_dot_auth__pb2.GetGoogleOAuthUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_google_o_auth_url), '/textql.rpc.public.auth.PublicAuthService/HandleGoogleOAuthCallback': EndpointSync.unary(method=MethodInfo(name='HandleGoogleOAuthCallback', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.HandleGoogleOAuthCallbackRequest, output=public_dot_auth__pb2.HandleGoogleOAuthCallbackResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.handle_google_o_auth_callback), '/textql.rpc.public.auth.PublicAuthService/UpdateOrgTheme': EndpointSync.unary(method=MethodInfo(name='UpdateOrgTheme', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UpdateOrgThemeRequest, output=public_dot_auth__pb2.UpdateOrgThemeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_org_theme), '/textql.rpc.public.auth.PublicAuthService/UpdateOrgToolRestrictions': EndpointSync.unary(method=MethodInfo(name='UpdateOrgToolRestrictions', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UpdateOrgToolRestrictionsRequest, output=public_dot_auth__pb2.UpdateOrgToolRestrictionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_org_tool_restrictions), '/textql.rpc.public.auth.PublicAuthService/CreateLogoUploadPresignUrl': EndpointSync.unary(method=MethodInfo(name='CreateLogoUploadPresignUrl', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CreateLogoUploadPresignUrlRequest, output=public_dot_auth__pb2.CreateLogoUploadPresignUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_logo_upload_presign_url), '/textql.rpc.public.auth.PublicAuthService/ProcessLogoUploadPresignUrl': EndpointSync.unary(method=MethodInfo(name='ProcessLogoUploadPresignUrl', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ProcessLogoUploadPresignUrlRequest, output=public_dot_auth__pb2.ProcessLogoUploadPresignUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.process_logo_upload_presign_url), '/textql.rpc.public.auth.PublicAuthService/UploadMemberImage': EndpointSync.unary(method=MethodInfo(name='UploadMemberImage', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UploadMemberImageRequest, output=public_dot_auth__pb2.UploadMemberImageResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.upload_member_image), '/textql.rpc.public.auth.PublicAuthService/GenerateMagicLinkForUser': EndpointSync.unary(method=MethodInfo(name='GenerateMagicLinkForUser', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GenerateMagicLinkForUserRequest, output=public_dot_auth__pb2.GenerateMagicLinkForUserResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.generate_magic_link_for_user), '/textql.rpc.public.auth.PublicAuthService/GetConsoleAuthToken': EndpointSync.unary(method=MethodInfo(name='GetConsoleAuthToken', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetConsoleAuthTokenRequest, output=public_dot_auth__pb2.GetConsoleAuthTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_console_auth_token), '/textql.rpc.public.auth.PublicAuthService/CreateOrganization': EndpointSync.unary(method=MethodInfo(name='CreateOrganization', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CreateOrganizationRequest, output=public_dot_auth__pb2.CreateOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_organization), '/textql.rpc.public.auth.PublicAuthService/CreateSiblingOrganization': EndpointSync.unary(method=MethodInfo(name='CreateSiblingOrganization', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CreateSiblingOrganizationRequest, output=public_dot_auth__pb2.CreateSiblingOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_sibling_organization), '/textql.rpc.public.auth.PublicAuthService/VerifyApiKey': EndpointSync.unary(method=MethodInfo(name='VerifyApiKey', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.VerifyApiKeyRequest, output=public_dot_auth__pb2.VerifyApiKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.verify_api_key), '/textql.rpc.public.auth.PublicAuthService/ListOrgOAuthClients': EndpointSync.unary(method=MethodInfo(name='ListOrgOAuthClients', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ListOrgOAuthClientsRequest, output=public_dot_auth__pb2.ListOrgOAuthClientsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_org_o_auth_clients), '/textql.rpc.public.auth.PublicAuthService/CreateOrgOAuthClient': EndpointSync.unary(method=MethodInfo(name='CreateOrgOAuthClient', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CreateOrgOAuthClientRequest, output=public_dot_auth__pb2.CreateOrgOAuthClientResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_org_o_auth_client), '/textql.rpc.public.auth.PublicAuthService/UpdateOrgOAuthClient': EndpointSync.unary(method=MethodInfo(name='UpdateOrgOAuthClient', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UpdateOrgOAuthClientRequest, output=public_dot_auth__pb2.UpdateOrgOAuthClientResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_org_o_auth_client), '/textql.rpc.public.auth.PublicAuthService/RotateOrgOAuthClientSecret': EndpointSync.unary(method=MethodInfo(name='RotateOrgOAuthClientSecret', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.RotateOrgOAuthClientSecretRequest, output=public_dot_auth__pb2.RotateOrgOAuthClientSecretResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.rotate_org_o_auth_client_secret), '/textql.rpc.public.auth.PublicAuthService/RevokeOrgOAuthClient': EndpointSync.unary(method=MethodInfo(name='RevokeOrgOAuthClient', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.RevokeOrgOAuthClientRequest, output=public_dot_auth__pb2.RevokeOrgOAuthClientResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.revoke_org_o_auth_client), '/textql.rpc.public.auth.PublicAuthService/DeleteOrgOAuthClient': EndpointSync.unary(method=MethodInfo(name='DeleteOrgOAuthClient', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.DeleteOrgOAuthClientRequest, output=public_dot_auth__pb2.DeleteOrgOAuthClientResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_org_o_auth_client), '/textql.rpc.public.auth.PublicAuthService/ListMyAuthorizedApps': EndpointSync.unary(method=MethodInfo(name='ListMyAuthorizedApps', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ListMyAuthorizedAppsRequest, output=public_dot_auth__pb2.ListMyAuthorizedAppsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_my_authorized_apps), '/textql.rpc.public.auth.PublicAuthService/RevokeMyAuthorizedApp': EndpointSync.unary(method=MethodInfo(name='RevokeMyAuthorizedApp', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.RevokeMyAuthorizedAppRequest, output=public_dot_auth__pb2.RevokeMyAuthorizedAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.revoke_my_authorized_app), '/textql.rpc.public.auth.PublicAuthService/ListOAuthScopes': EndpointSync.unary(method=MethodInfo(name='ListOAuthScopes', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ListOAuthScopesRequest, output=public_dot_auth__pb2.ListOAuthScopesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_o_auth_scopes)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.auth.PublicAuthService'

class PublicAuthServiceClientSync(ConnectClientSync):

    def login_email_start(self, request: public_dot_auth__pb2.LoginEmailStartRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.LoginEmailStartResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='LoginEmailStart', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.LoginEmailStartRequest, output=public_dot_auth__pb2.LoginEmailStartResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def validate_intermediary_token(self, request: public_dot_auth__pb2.ValidateIntermediaryTokenRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.ValidateIntermediaryTokenResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ValidateIntermediaryToken', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ValidateIntermediaryTokenRequest, output=public_dot_auth__pb2.ValidateIntermediaryTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def validate_long_term_token(self, request: public_dot_auth__pb2.ValidateLongTermTokenRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.ValidateLongTermTokenResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ValidateLongTermToken', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ValidateLongTermTokenRequest, output=public_dot_auth__pb2.ValidateLongTermTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def exchange_intermediary_token(self, request: public_dot_auth__pb2.ExchangeIntermediaryTokenRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> auth__pb2.LongTermAccessTokenResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ExchangeIntermediaryToken', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ExchangeIntermediaryTokenRequest, output=auth__pb2.LongTermAccessTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def logout(self, request: public_dot_auth__pb2.LogoutRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.LogoutResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='Logout', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.LogoutRequest, output=public_dot_auth__pb2.LogoutResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_o_i_d_c_auth_url(self, request: public_dot_auth__pb2.GetOIDCAuthUrlRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.GetOIDCAuthUrlResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetOIDCAuthUrl', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetOIDCAuthUrlRequest, output=public_dot_auth__pb2.GetOIDCAuthUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def handle_o_i_d_c_callback(self, request: public_dot_auth__pb2.HandleOIDCCallbackRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.HandleOIDCCallbackResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='HandleOIDCCallback', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.HandleOIDCCallbackRequest, output=public_dot_auth__pb2.HandleOIDCCallbackResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def create_s_s_o_organization(self, request: public_dot_auth__pb2.CreateSSOOrganizationRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.CreateSSOOrganizationResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateSSOOrganization', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CreateSSOOrganizationRequest, output=public_dot_auth__pb2.CreateSSOOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_organizations(self, request: public_dot_auth__pb2.ListOrganizationsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.ListOrganizationsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListOrganizations', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ListOrganizationsRequest, output=public_dot_auth__pb2.ListOrganizationsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_member(self, request: public_dot_auth__pb2.GetMemberRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.GetMemberResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetMember', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetMemberRequest, output=public_dot_auth__pb2.GetMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_organization(self, request: public_dot_auth__pb2.GetOrganizationRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.GetOrganizationResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetOrganization', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetOrganizationRequest, output=public_dot_auth__pb2.GetOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_member_in_org_by_id(self, request: public_dot_auth__pb2.GetMemberInOrgByIdRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.GetMemberInOrgByIdResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetMemberInOrgById', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetMemberInOrgByIdRequest, output=public_dot_auth__pb2.GetMemberInOrgByIdResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def exchange_session(self, request: public_dot_auth__pb2.ExchangeSessionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.ExchangeSessionResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ExchangeSession', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ExchangeSessionRequest, output=public_dot_auth__pb2.ExchangeSessionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def update_default_connector(self, request: public_dot_auth__pb2.UpdateDefaultConnectorRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.UpdateDefaultConnectorResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateDefaultConnector', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UpdateDefaultConnectorRequest, output=public_dot_auth__pb2.UpdateDefaultConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_o_i_d_c_config(self, request: public_dot_auth__pb2.GetOIDCConfigRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.GetOIDCConfigResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetOIDCConfig', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetOIDCConfigRequest, output=public_dot_auth__pb2.GetOIDCConfigResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def save_o_i_d_c_config(self, request: public_dot_auth__pb2.SaveOIDCConfigRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.SaveOIDCConfigResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='SaveOIDCConfig', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.SaveOIDCConfigRequest, output=public_dot_auth__pb2.SaveOIDCConfigResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def check_domain_for_o_i_d_c(self, request: public_dot_auth__pb2.CheckDomainForOIDCRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.CheckDomainForOIDCResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CheckDomainForOIDC', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CheckDomainForOIDCRequest, output=public_dot_auth__pb2.CheckDomainForOIDCResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_o_i_d_c_providers(self, request: public_dot_auth__pb2.ListOIDCProvidersRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.ListOIDCProvidersResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListOIDCProviders', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ListOIDCProvidersRequest, output=public_dot_auth__pb2.ListOIDCProvidersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def create_o_i_d_c_provider(self, request: public_dot_auth__pb2.CreateOIDCProviderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.CreateOIDCProviderResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateOIDCProvider', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CreateOIDCProviderRequest, output=public_dot_auth__pb2.CreateOIDCProviderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def update_o_i_d_c_provider(self, request: public_dot_auth__pb2.UpdateOIDCProviderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.UpdateOIDCProviderResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateOIDCProvider', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UpdateOIDCProviderRequest, output=public_dot_auth__pb2.UpdateOIDCProviderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def delete_o_i_d_c_provider(self, request: public_dot_auth__pb2.DeleteOIDCProviderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.DeleteOIDCProviderResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteOIDCProvider', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.DeleteOIDCProviderRequest, output=public_dot_auth__pb2.DeleteOIDCProviderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def add_org_o_i_d_c_provider(self, request: public_dot_auth__pb2.AddOrgOIDCProviderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.AddOrgOIDCProviderResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='AddOrgOIDCProvider', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.AddOrgOIDCProviderRequest, output=public_dot_auth__pb2.AddOrgOIDCProviderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def remove_org_o_i_d_c_provider(self, request: public_dot_auth__pb2.RemoveOrgOIDCProviderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.RemoveOrgOIDCProviderResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RemoveOrgOIDCProvider', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.RemoveOrgOIDCProviderRequest, output=public_dot_auth__pb2.RemoveOrgOIDCProviderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def update_org_o_i_d_c_providers(self, request: public_dot_auth__pb2.UpdateOrgOIDCProvidersRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.UpdateOrgOIDCProvidersResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateOrgOIDCProviders', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UpdateOrgOIDCProvidersRequest, output=public_dot_auth__pb2.UpdateOrgOIDCProvidersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_org_o_i_d_c_providers(self, request: public_dot_auth__pb2.GetOrgOIDCProvidersRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.GetOrgOIDCProvidersResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetOrgOIDCProviders', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetOrgOIDCProvidersRequest, output=public_dot_auth__pb2.GetOrgOIDCProvidersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_google_o_auth_url(self, request: public_dot_auth__pb2.GetGoogleOAuthUrlRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.GetGoogleOAuthUrlResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetGoogleOAuthUrl', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetGoogleOAuthUrlRequest, output=public_dot_auth__pb2.GetGoogleOAuthUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def handle_google_o_auth_callback(self, request: public_dot_auth__pb2.HandleGoogleOAuthCallbackRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.HandleGoogleOAuthCallbackResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='HandleGoogleOAuthCallback', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.HandleGoogleOAuthCallbackRequest, output=public_dot_auth__pb2.HandleGoogleOAuthCallbackResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def update_org_theme(self, request: public_dot_auth__pb2.UpdateOrgThemeRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.UpdateOrgThemeResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateOrgTheme', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UpdateOrgThemeRequest, output=public_dot_auth__pb2.UpdateOrgThemeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def update_org_tool_restrictions(self, request: public_dot_auth__pb2.UpdateOrgToolRestrictionsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.UpdateOrgToolRestrictionsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateOrgToolRestrictions', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UpdateOrgToolRestrictionsRequest, output=public_dot_auth__pb2.UpdateOrgToolRestrictionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def create_logo_upload_presign_url(self, request: public_dot_auth__pb2.CreateLogoUploadPresignUrlRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.CreateLogoUploadPresignUrlResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateLogoUploadPresignUrl', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CreateLogoUploadPresignUrlRequest, output=public_dot_auth__pb2.CreateLogoUploadPresignUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def process_logo_upload_presign_url(self, request: public_dot_auth__pb2.ProcessLogoUploadPresignUrlRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.ProcessLogoUploadPresignUrlResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ProcessLogoUploadPresignUrl', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ProcessLogoUploadPresignUrlRequest, output=public_dot_auth__pb2.ProcessLogoUploadPresignUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def upload_member_image(self, request: public_dot_auth__pb2.UploadMemberImageRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.UploadMemberImageResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UploadMemberImage', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UploadMemberImageRequest, output=public_dot_auth__pb2.UploadMemberImageResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def generate_magic_link_for_user(self, request: public_dot_auth__pb2.GenerateMagicLinkForUserRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.GenerateMagicLinkForUserResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GenerateMagicLinkForUser', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GenerateMagicLinkForUserRequest, output=public_dot_auth__pb2.GenerateMagicLinkForUserResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_console_auth_token(self, request: public_dot_auth__pb2.GetConsoleAuthTokenRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.GetConsoleAuthTokenResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetConsoleAuthToken', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.GetConsoleAuthTokenRequest, output=public_dot_auth__pb2.GetConsoleAuthTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def create_organization(self, request: public_dot_auth__pb2.CreateOrganizationRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.CreateOrganizationResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateOrganization', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CreateOrganizationRequest, output=public_dot_auth__pb2.CreateOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def create_sibling_organization(self, request: public_dot_auth__pb2.CreateSiblingOrganizationRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.CreateSiblingOrganizationResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateSiblingOrganization', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CreateSiblingOrganizationRequest, output=public_dot_auth__pb2.CreateSiblingOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def verify_api_key(self, request: public_dot_auth__pb2.VerifyApiKeyRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.VerifyApiKeyResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='VerifyApiKey', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.VerifyApiKeyRequest, output=public_dot_auth__pb2.VerifyApiKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_org_o_auth_clients(self, request: public_dot_auth__pb2.ListOrgOAuthClientsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_auth__pb2.ListOrgOAuthClientsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListOrgOAuthClients', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ListOrgOAuthClientsRequest, output=public_dot_auth__pb2.ListOrgOAuthClientsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def create_org_o_auth_client(self, request: public_dot_auth__pb2.CreateOrgOAuthClientRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.CreateOrgOAuthClientResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateOrgOAuthClient', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.CreateOrgOAuthClientRequest, output=public_dot_auth__pb2.CreateOrgOAuthClientResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def update_org_o_auth_client(self, request: public_dot_auth__pb2.UpdateOrgOAuthClientRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.UpdateOrgOAuthClientResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateOrgOAuthClient', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.UpdateOrgOAuthClientRequest, output=public_dot_auth__pb2.UpdateOrgOAuthClientResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def rotate_org_o_auth_client_secret(self, request: public_dot_auth__pb2.RotateOrgOAuthClientSecretRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.RotateOrgOAuthClientSecretResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RotateOrgOAuthClientSecret', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.RotateOrgOAuthClientSecretRequest, output=public_dot_auth__pb2.RotateOrgOAuthClientSecretResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def revoke_org_o_auth_client(self, request: public_dot_auth__pb2.RevokeOrgOAuthClientRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.RevokeOrgOAuthClientResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RevokeOrgOAuthClient', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.RevokeOrgOAuthClientRequest, output=public_dot_auth__pb2.RevokeOrgOAuthClientResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def delete_org_o_auth_client(self, request: public_dot_auth__pb2.DeleteOrgOAuthClientRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.DeleteOrgOAuthClientResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteOrgOAuthClient', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.DeleteOrgOAuthClientRequest, output=public_dot_auth__pb2.DeleteOrgOAuthClientResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_my_authorized_apps(self, request: public_dot_auth__pb2.ListMyAuthorizedAppsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_auth__pb2.ListMyAuthorizedAppsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListMyAuthorizedApps', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ListMyAuthorizedAppsRequest, output=public_dot_auth__pb2.ListMyAuthorizedAppsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def revoke_my_authorized_app(self, request: public_dot_auth__pb2.RevokeMyAuthorizedAppRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_auth__pb2.RevokeMyAuthorizedAppResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RevokeMyAuthorizedApp', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.RevokeMyAuthorizedAppRequest, output=public_dot_auth__pb2.RevokeMyAuthorizedAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_o_auth_scopes(self, request: public_dot_auth__pb2.ListOAuthScopesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_auth__pb2.ListOAuthScopesResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListOAuthScopes', service_name='textql.rpc.public.auth.PublicAuthService', input=public_dot_auth__pb2.ListOAuthScopesRequest, output=public_dot_auth__pb2.ListOAuthScopesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)