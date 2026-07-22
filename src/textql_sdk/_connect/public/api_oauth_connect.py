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
from . import api_oauth_pb2 as public_dot_api__oauth__pb2

class ApiOAuthService(Protocol):

    async def get_api_o_auth_u_r_l(self, request: public_dot_api__oauth__pb2.GetApiOAuthURLRequest, ctx: RequestContext) -> public_dot_api__oauth__pb2.GetApiOAuthURLResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def exchange_api_o_auth_code(self, request: public_dot_api__oauth__pb2.ExchangeApiOAuthCodeRequest, ctx: RequestContext) -> public_dot_api__oauth__pb2.ExchangeApiOAuthCodeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def exchange_api_o_auth_client_credentials(self, request: public_dot_api__oauth__pb2.ExchangeApiOAuthClientCredentialsRequest, ctx: RequestContext) -> public_dot_api__oauth__pb2.ExchangeApiOAuthCodeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def exchange_api_o_auth_jwt_bearer(self, request: public_dot_api__oauth__pb2.ExchangeApiOAuthJwtBearerRequest, ctx: RequestContext) -> public_dot_api__oauth__pb2.ExchangeApiOAuthCodeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def initiate_device_authorization(self, request: public_dot_api__oauth__pb2.InitiateDeviceAuthorizationRequest, ctx: RequestContext) -> public_dot_api__oauth__pb2.InitiateDeviceAuthorizationResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def poll_device_code_token(self, request: public_dot_api__oauth__pb2.PollDeviceCodeTokenRequest, ctx: RequestContext) -> public_dot_api__oauth__pb2.PollDeviceCodeTokenResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_api_o_auth_status(self, request: public_dot_api__oauth__pb2.GetApiOAuthStatusRequest, ctx: RequestContext) -> public_dot_api__oauth__pb2.GetApiOAuthStatusResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def revoke_api_o_auth_token(self, request: public_dot_api__oauth__pb2.RevokeApiOAuthTokenRequest, ctx: RequestContext) -> public_dot_api__oauth__pb2.RevokeApiOAuthTokenResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def upsert_api_o_auth_config(self, request: public_dot_api__oauth__pb2.UpsertApiOAuthConfigRequest, ctx: RequestContext) -> public_dot_api__oauth__pb2.UpsertApiOAuthConfigResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_api_o_auth_config(self, request: public_dot_api__oauth__pb2.GetApiOAuthConfigRequest, ctx: RequestContext) -> public_dot_api__oauth__pb2.GetApiOAuthConfigResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class ApiOAuthServiceASGIApplication(ConnectASGIApplication[ApiOAuthService]):

    def __init__(self, service: ApiOAuthService | AsyncGenerator[ApiOAuthService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.api_oauth.ApiOAuthService/GetApiOAuthURL': Endpoint.unary(method=MethodInfo(name='GetApiOAuthURL', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.GetApiOAuthURLRequest, output=public_dot_api__oauth__pb2.GetApiOAuthURLResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_api_o_auth_u_r_l), '/textql.rpc.public.api_oauth.ApiOAuthService/ExchangeApiOAuthCode': Endpoint.unary(method=MethodInfo(name='ExchangeApiOAuthCode', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.ExchangeApiOAuthCodeRequest, output=public_dot_api__oauth__pb2.ExchangeApiOAuthCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.exchange_api_o_auth_code), '/textql.rpc.public.api_oauth.ApiOAuthService/ExchangeApiOAuthClientCredentials': Endpoint.unary(method=MethodInfo(name='ExchangeApiOAuthClientCredentials', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.ExchangeApiOAuthClientCredentialsRequest, output=public_dot_api__oauth__pb2.ExchangeApiOAuthCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.exchange_api_o_auth_client_credentials), '/textql.rpc.public.api_oauth.ApiOAuthService/ExchangeApiOAuthJwtBearer': Endpoint.unary(method=MethodInfo(name='ExchangeApiOAuthJwtBearer', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.ExchangeApiOAuthJwtBearerRequest, output=public_dot_api__oauth__pb2.ExchangeApiOAuthCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.exchange_api_o_auth_jwt_bearer), '/textql.rpc.public.api_oauth.ApiOAuthService/InitiateDeviceAuthorization': Endpoint.unary(method=MethodInfo(name='InitiateDeviceAuthorization', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.InitiateDeviceAuthorizationRequest, output=public_dot_api__oauth__pb2.InitiateDeviceAuthorizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.initiate_device_authorization), '/textql.rpc.public.api_oauth.ApiOAuthService/PollDeviceCodeToken': Endpoint.unary(method=MethodInfo(name='PollDeviceCodeToken', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.PollDeviceCodeTokenRequest, output=public_dot_api__oauth__pb2.PollDeviceCodeTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.poll_device_code_token), '/textql.rpc.public.api_oauth.ApiOAuthService/GetApiOAuthStatus': Endpoint.unary(method=MethodInfo(name='GetApiOAuthStatus', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.GetApiOAuthStatusRequest, output=public_dot_api__oauth__pb2.GetApiOAuthStatusResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_api_o_auth_status), '/textql.rpc.public.api_oauth.ApiOAuthService/RevokeApiOAuthToken': Endpoint.unary(method=MethodInfo(name='RevokeApiOAuthToken', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.RevokeApiOAuthTokenRequest, output=public_dot_api__oauth__pb2.RevokeApiOAuthTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.revoke_api_o_auth_token), '/textql.rpc.public.api_oauth.ApiOAuthService/UpsertApiOAuthConfig': Endpoint.unary(method=MethodInfo(name='UpsertApiOAuthConfig', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.UpsertApiOAuthConfigRequest, output=public_dot_api__oauth__pb2.UpsertApiOAuthConfigResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.upsert_api_o_auth_config), '/textql.rpc.public.api_oauth.ApiOAuthService/GetApiOAuthConfig': Endpoint.unary(method=MethodInfo(name='GetApiOAuthConfig', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.GetApiOAuthConfigRequest, output=public_dot_api__oauth__pb2.GetApiOAuthConfigResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_api_o_auth_config)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.api_oauth.ApiOAuthService'

class ApiOAuthServiceClient(ConnectClient):

    async def get_api_o_auth_u_r_l(self, request: public_dot_api__oauth__pb2.GetApiOAuthURLRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_api__oauth__pb2.GetApiOAuthURLResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetApiOAuthURL', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.GetApiOAuthURLRequest, output=public_dot_api__oauth__pb2.GetApiOAuthURLResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def exchange_api_o_auth_code(self, request: public_dot_api__oauth__pb2.ExchangeApiOAuthCodeRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_api__oauth__pb2.ExchangeApiOAuthCodeResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ExchangeApiOAuthCode', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.ExchangeApiOAuthCodeRequest, output=public_dot_api__oauth__pb2.ExchangeApiOAuthCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def exchange_api_o_auth_client_credentials(self, request: public_dot_api__oauth__pb2.ExchangeApiOAuthClientCredentialsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_api__oauth__pb2.ExchangeApiOAuthCodeResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ExchangeApiOAuthClientCredentials', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.ExchangeApiOAuthClientCredentialsRequest, output=public_dot_api__oauth__pb2.ExchangeApiOAuthCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def exchange_api_o_auth_jwt_bearer(self, request: public_dot_api__oauth__pb2.ExchangeApiOAuthJwtBearerRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_api__oauth__pb2.ExchangeApiOAuthCodeResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ExchangeApiOAuthJwtBearer', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.ExchangeApiOAuthJwtBearerRequest, output=public_dot_api__oauth__pb2.ExchangeApiOAuthCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def initiate_device_authorization(self, request: public_dot_api__oauth__pb2.InitiateDeviceAuthorizationRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_api__oauth__pb2.InitiateDeviceAuthorizationResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='InitiateDeviceAuthorization', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.InitiateDeviceAuthorizationRequest, output=public_dot_api__oauth__pb2.InitiateDeviceAuthorizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def poll_device_code_token(self, request: public_dot_api__oauth__pb2.PollDeviceCodeTokenRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_api__oauth__pb2.PollDeviceCodeTokenResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='PollDeviceCodeToken', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.PollDeviceCodeTokenRequest, output=public_dot_api__oauth__pb2.PollDeviceCodeTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_api_o_auth_status(self, request: public_dot_api__oauth__pb2.GetApiOAuthStatusRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_api__oauth__pb2.GetApiOAuthStatusResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetApiOAuthStatus', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.GetApiOAuthStatusRequest, output=public_dot_api__oauth__pb2.GetApiOAuthStatusResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def revoke_api_o_auth_token(self, request: public_dot_api__oauth__pb2.RevokeApiOAuthTokenRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_api__oauth__pb2.RevokeApiOAuthTokenResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RevokeApiOAuthToken', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.RevokeApiOAuthTokenRequest, output=public_dot_api__oauth__pb2.RevokeApiOAuthTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def upsert_api_o_auth_config(self, request: public_dot_api__oauth__pb2.UpsertApiOAuthConfigRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_api__oauth__pb2.UpsertApiOAuthConfigResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpsertApiOAuthConfig', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.UpsertApiOAuthConfigRequest, output=public_dot_api__oauth__pb2.UpsertApiOAuthConfigResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_api_o_auth_config(self, request: public_dot_api__oauth__pb2.GetApiOAuthConfigRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_api__oauth__pb2.GetApiOAuthConfigResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetApiOAuthConfig', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.GetApiOAuthConfigRequest, output=public_dot_api__oauth__pb2.GetApiOAuthConfigResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

class ApiOAuthServiceSync(Protocol):

    def get_api_o_auth_u_r_l(self, request: public_dot_api__oauth__pb2.GetApiOAuthURLRequest, ctx: RequestContext) -> public_dot_api__oauth__pb2.GetApiOAuthURLResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def exchange_api_o_auth_code(self, request: public_dot_api__oauth__pb2.ExchangeApiOAuthCodeRequest, ctx: RequestContext) -> public_dot_api__oauth__pb2.ExchangeApiOAuthCodeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def exchange_api_o_auth_client_credentials(self, request: public_dot_api__oauth__pb2.ExchangeApiOAuthClientCredentialsRequest, ctx: RequestContext) -> public_dot_api__oauth__pb2.ExchangeApiOAuthCodeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def exchange_api_o_auth_jwt_bearer(self, request: public_dot_api__oauth__pb2.ExchangeApiOAuthJwtBearerRequest, ctx: RequestContext) -> public_dot_api__oauth__pb2.ExchangeApiOAuthCodeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def initiate_device_authorization(self, request: public_dot_api__oauth__pb2.InitiateDeviceAuthorizationRequest, ctx: RequestContext) -> public_dot_api__oauth__pb2.InitiateDeviceAuthorizationResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def poll_device_code_token(self, request: public_dot_api__oauth__pb2.PollDeviceCodeTokenRequest, ctx: RequestContext) -> public_dot_api__oauth__pb2.PollDeviceCodeTokenResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_api_o_auth_status(self, request: public_dot_api__oauth__pb2.GetApiOAuthStatusRequest, ctx: RequestContext) -> public_dot_api__oauth__pb2.GetApiOAuthStatusResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def revoke_api_o_auth_token(self, request: public_dot_api__oauth__pb2.RevokeApiOAuthTokenRequest, ctx: RequestContext) -> public_dot_api__oauth__pb2.RevokeApiOAuthTokenResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def upsert_api_o_auth_config(self, request: public_dot_api__oauth__pb2.UpsertApiOAuthConfigRequest, ctx: RequestContext) -> public_dot_api__oauth__pb2.UpsertApiOAuthConfigResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_api_o_auth_config(self, request: public_dot_api__oauth__pb2.GetApiOAuthConfigRequest, ctx: RequestContext) -> public_dot_api__oauth__pb2.GetApiOAuthConfigResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class ApiOAuthServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: ApiOAuthServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.api_oauth.ApiOAuthService/GetApiOAuthURL': EndpointSync.unary(method=MethodInfo(name='GetApiOAuthURL', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.GetApiOAuthURLRequest, output=public_dot_api__oauth__pb2.GetApiOAuthURLResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_api_o_auth_u_r_l), '/textql.rpc.public.api_oauth.ApiOAuthService/ExchangeApiOAuthCode': EndpointSync.unary(method=MethodInfo(name='ExchangeApiOAuthCode', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.ExchangeApiOAuthCodeRequest, output=public_dot_api__oauth__pb2.ExchangeApiOAuthCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.exchange_api_o_auth_code), '/textql.rpc.public.api_oauth.ApiOAuthService/ExchangeApiOAuthClientCredentials': EndpointSync.unary(method=MethodInfo(name='ExchangeApiOAuthClientCredentials', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.ExchangeApiOAuthClientCredentialsRequest, output=public_dot_api__oauth__pb2.ExchangeApiOAuthCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.exchange_api_o_auth_client_credentials), '/textql.rpc.public.api_oauth.ApiOAuthService/ExchangeApiOAuthJwtBearer': EndpointSync.unary(method=MethodInfo(name='ExchangeApiOAuthJwtBearer', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.ExchangeApiOAuthJwtBearerRequest, output=public_dot_api__oauth__pb2.ExchangeApiOAuthCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.exchange_api_o_auth_jwt_bearer), '/textql.rpc.public.api_oauth.ApiOAuthService/InitiateDeviceAuthorization': EndpointSync.unary(method=MethodInfo(name='InitiateDeviceAuthorization', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.InitiateDeviceAuthorizationRequest, output=public_dot_api__oauth__pb2.InitiateDeviceAuthorizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.initiate_device_authorization), '/textql.rpc.public.api_oauth.ApiOAuthService/PollDeviceCodeToken': EndpointSync.unary(method=MethodInfo(name='PollDeviceCodeToken', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.PollDeviceCodeTokenRequest, output=public_dot_api__oauth__pb2.PollDeviceCodeTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.poll_device_code_token), '/textql.rpc.public.api_oauth.ApiOAuthService/GetApiOAuthStatus': EndpointSync.unary(method=MethodInfo(name='GetApiOAuthStatus', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.GetApiOAuthStatusRequest, output=public_dot_api__oauth__pb2.GetApiOAuthStatusResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_api_o_auth_status), '/textql.rpc.public.api_oauth.ApiOAuthService/RevokeApiOAuthToken': EndpointSync.unary(method=MethodInfo(name='RevokeApiOAuthToken', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.RevokeApiOAuthTokenRequest, output=public_dot_api__oauth__pb2.RevokeApiOAuthTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.revoke_api_o_auth_token), '/textql.rpc.public.api_oauth.ApiOAuthService/UpsertApiOAuthConfig': EndpointSync.unary(method=MethodInfo(name='UpsertApiOAuthConfig', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.UpsertApiOAuthConfigRequest, output=public_dot_api__oauth__pb2.UpsertApiOAuthConfigResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.upsert_api_o_auth_config), '/textql.rpc.public.api_oauth.ApiOAuthService/GetApiOAuthConfig': EndpointSync.unary(method=MethodInfo(name='GetApiOAuthConfig', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.GetApiOAuthConfigRequest, output=public_dot_api__oauth__pb2.GetApiOAuthConfigResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_api_o_auth_config)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.api_oauth.ApiOAuthService'

class ApiOAuthServiceClientSync(ConnectClientSync):

    def get_api_o_auth_u_r_l(self, request: public_dot_api__oauth__pb2.GetApiOAuthURLRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_api__oauth__pb2.GetApiOAuthURLResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetApiOAuthURL', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.GetApiOAuthURLRequest, output=public_dot_api__oauth__pb2.GetApiOAuthURLResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def exchange_api_o_auth_code(self, request: public_dot_api__oauth__pb2.ExchangeApiOAuthCodeRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_api__oauth__pb2.ExchangeApiOAuthCodeResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ExchangeApiOAuthCode', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.ExchangeApiOAuthCodeRequest, output=public_dot_api__oauth__pb2.ExchangeApiOAuthCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def exchange_api_o_auth_client_credentials(self, request: public_dot_api__oauth__pb2.ExchangeApiOAuthClientCredentialsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_api__oauth__pb2.ExchangeApiOAuthCodeResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ExchangeApiOAuthClientCredentials', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.ExchangeApiOAuthClientCredentialsRequest, output=public_dot_api__oauth__pb2.ExchangeApiOAuthCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def exchange_api_o_auth_jwt_bearer(self, request: public_dot_api__oauth__pb2.ExchangeApiOAuthJwtBearerRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_api__oauth__pb2.ExchangeApiOAuthCodeResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ExchangeApiOAuthJwtBearer', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.ExchangeApiOAuthJwtBearerRequest, output=public_dot_api__oauth__pb2.ExchangeApiOAuthCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def initiate_device_authorization(self, request: public_dot_api__oauth__pb2.InitiateDeviceAuthorizationRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_api__oauth__pb2.InitiateDeviceAuthorizationResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='InitiateDeviceAuthorization', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.InitiateDeviceAuthorizationRequest, output=public_dot_api__oauth__pb2.InitiateDeviceAuthorizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def poll_device_code_token(self, request: public_dot_api__oauth__pb2.PollDeviceCodeTokenRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_api__oauth__pb2.PollDeviceCodeTokenResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='PollDeviceCodeToken', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.PollDeviceCodeTokenRequest, output=public_dot_api__oauth__pb2.PollDeviceCodeTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_api_o_auth_status(self, request: public_dot_api__oauth__pb2.GetApiOAuthStatusRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_api__oauth__pb2.GetApiOAuthStatusResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetApiOAuthStatus', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.GetApiOAuthStatusRequest, output=public_dot_api__oauth__pb2.GetApiOAuthStatusResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def revoke_api_o_auth_token(self, request: public_dot_api__oauth__pb2.RevokeApiOAuthTokenRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_api__oauth__pb2.RevokeApiOAuthTokenResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RevokeApiOAuthToken', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.RevokeApiOAuthTokenRequest, output=public_dot_api__oauth__pb2.RevokeApiOAuthTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def upsert_api_o_auth_config(self, request: public_dot_api__oauth__pb2.UpsertApiOAuthConfigRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_api__oauth__pb2.UpsertApiOAuthConfigResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpsertApiOAuthConfig', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.UpsertApiOAuthConfigRequest, output=public_dot_api__oauth__pb2.UpsertApiOAuthConfigResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_api_o_auth_config(self, request: public_dot_api__oauth__pb2.GetApiOAuthConfigRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_api__oauth__pb2.GetApiOAuthConfigResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetApiOAuthConfig', service_name='textql.rpc.public.api_oauth.ApiOAuthService', input=public_dot_api__oauth__pb2.GetApiOAuthConfigRequest, output=public_dot_api__oauth__pb2.GetApiOAuthConfigResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)