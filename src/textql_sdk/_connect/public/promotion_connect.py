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
from . import promotion_pb2 as public_dot_promotion__pb2

class PromotionService(Protocol):

    async def list_promotions(self, request: public_dot_promotion__pb2.ListPromotionsRequest, ctx: RequestContext) -> public_dot_promotion__pb2.ListPromotionsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def create_promotion(self, request: public_dot_promotion__pb2.CreatePromotionRequest, ctx: RequestContext) -> public_dot_promotion__pb2.CreatePromotionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_promotion(self, request: public_dot_promotion__pb2.UpdatePromotionRequest, ctx: RequestContext) -> public_dot_promotion__pb2.UpdatePromotionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_promotion(self, request: public_dot_promotion__pb2.DeletePromotionRequest, ctx: RequestContext) -> public_dot_promotion__pb2.DeletePromotionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_promotion_grants(self, request: public_dot_promotion__pb2.ListPromotionGrantsRequest, ctx: RequestContext) -> public_dot_promotion__pb2.ListPromotionGrantsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_event_categories(self, request: public_dot_promotion__pb2.ListEventCategoriesRequest, ctx: RequestContext) -> public_dot_promotion__pb2.ListEventCategoriesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class PromotionServiceASGIApplication(ConnectASGIApplication[PromotionService]):

    def __init__(self, service: PromotionService | AsyncGenerator[PromotionService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.promotion.PromotionService/ListPromotions': Endpoint.unary(method=MethodInfo(name='ListPromotions', service_name='textql.rpc.public.promotion.PromotionService', input=public_dot_promotion__pb2.ListPromotionsRequest, output=public_dot_promotion__pb2.ListPromotionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_promotions), '/textql.rpc.public.promotion.PromotionService/CreatePromotion': Endpoint.unary(method=MethodInfo(name='CreatePromotion', service_name='textql.rpc.public.promotion.PromotionService', input=public_dot_promotion__pb2.CreatePromotionRequest, output=public_dot_promotion__pb2.CreatePromotionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_promotion), '/textql.rpc.public.promotion.PromotionService/UpdatePromotion': Endpoint.unary(method=MethodInfo(name='UpdatePromotion', service_name='textql.rpc.public.promotion.PromotionService', input=public_dot_promotion__pb2.UpdatePromotionRequest, output=public_dot_promotion__pb2.UpdatePromotionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_promotion), '/textql.rpc.public.promotion.PromotionService/DeletePromotion': Endpoint.unary(method=MethodInfo(name='DeletePromotion', service_name='textql.rpc.public.promotion.PromotionService', input=public_dot_promotion__pb2.DeletePromotionRequest, output=public_dot_promotion__pb2.DeletePromotionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_promotion), '/textql.rpc.public.promotion.PromotionService/ListPromotionGrants': Endpoint.unary(method=MethodInfo(name='ListPromotionGrants', service_name='textql.rpc.public.promotion.PromotionService', input=public_dot_promotion__pb2.ListPromotionGrantsRequest, output=public_dot_promotion__pb2.ListPromotionGrantsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_promotion_grants), '/textql.rpc.public.promotion.PromotionService/ListEventCategories': Endpoint.unary(method=MethodInfo(name='ListEventCategories', service_name='textql.rpc.public.promotion.PromotionService', input=public_dot_promotion__pb2.ListEventCategoriesRequest, output=public_dot_promotion__pb2.ListEventCategoriesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_event_categories)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.promotion.PromotionService'

class PromotionServiceClient(ConnectClient):

    async def list_promotions(self, request: public_dot_promotion__pb2.ListPromotionsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_promotion__pb2.ListPromotionsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListPromotions', service_name='textql.rpc.public.promotion.PromotionService', input=public_dot_promotion__pb2.ListPromotionsRequest, output=public_dot_promotion__pb2.ListPromotionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def create_promotion(self, request: public_dot_promotion__pb2.CreatePromotionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_promotion__pb2.CreatePromotionResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreatePromotion', service_name='textql.rpc.public.promotion.PromotionService', input=public_dot_promotion__pb2.CreatePromotionRequest, output=public_dot_promotion__pb2.CreatePromotionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def update_promotion(self, request: public_dot_promotion__pb2.UpdatePromotionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_promotion__pb2.UpdatePromotionResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdatePromotion', service_name='textql.rpc.public.promotion.PromotionService', input=public_dot_promotion__pb2.UpdatePromotionRequest, output=public_dot_promotion__pb2.UpdatePromotionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def delete_promotion(self, request: public_dot_promotion__pb2.DeletePromotionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_promotion__pb2.DeletePromotionResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeletePromotion', service_name='textql.rpc.public.promotion.PromotionService', input=public_dot_promotion__pb2.DeletePromotionRequest, output=public_dot_promotion__pb2.DeletePromotionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_promotion_grants(self, request: public_dot_promotion__pb2.ListPromotionGrantsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_promotion__pb2.ListPromotionGrantsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListPromotionGrants', service_name='textql.rpc.public.promotion.PromotionService', input=public_dot_promotion__pb2.ListPromotionGrantsRequest, output=public_dot_promotion__pb2.ListPromotionGrantsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_event_categories(self, request: public_dot_promotion__pb2.ListEventCategoriesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_promotion__pb2.ListEventCategoriesResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListEventCategories', service_name='textql.rpc.public.promotion.PromotionService', input=public_dot_promotion__pb2.ListEventCategoriesRequest, output=public_dot_promotion__pb2.ListEventCategoriesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class PromotionServiceSync(Protocol):

    def list_promotions(self, request: public_dot_promotion__pb2.ListPromotionsRequest, ctx: RequestContext) -> public_dot_promotion__pb2.ListPromotionsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def create_promotion(self, request: public_dot_promotion__pb2.CreatePromotionRequest, ctx: RequestContext) -> public_dot_promotion__pb2.CreatePromotionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_promotion(self, request: public_dot_promotion__pb2.UpdatePromotionRequest, ctx: RequestContext) -> public_dot_promotion__pb2.UpdatePromotionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_promotion(self, request: public_dot_promotion__pb2.DeletePromotionRequest, ctx: RequestContext) -> public_dot_promotion__pb2.DeletePromotionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_promotion_grants(self, request: public_dot_promotion__pb2.ListPromotionGrantsRequest, ctx: RequestContext) -> public_dot_promotion__pb2.ListPromotionGrantsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_event_categories(self, request: public_dot_promotion__pb2.ListEventCategoriesRequest, ctx: RequestContext) -> public_dot_promotion__pb2.ListEventCategoriesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class PromotionServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: PromotionServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.promotion.PromotionService/ListPromotions': EndpointSync.unary(method=MethodInfo(name='ListPromotions', service_name='textql.rpc.public.promotion.PromotionService', input=public_dot_promotion__pb2.ListPromotionsRequest, output=public_dot_promotion__pb2.ListPromotionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_promotions), '/textql.rpc.public.promotion.PromotionService/CreatePromotion': EndpointSync.unary(method=MethodInfo(name='CreatePromotion', service_name='textql.rpc.public.promotion.PromotionService', input=public_dot_promotion__pb2.CreatePromotionRequest, output=public_dot_promotion__pb2.CreatePromotionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_promotion), '/textql.rpc.public.promotion.PromotionService/UpdatePromotion': EndpointSync.unary(method=MethodInfo(name='UpdatePromotion', service_name='textql.rpc.public.promotion.PromotionService', input=public_dot_promotion__pb2.UpdatePromotionRequest, output=public_dot_promotion__pb2.UpdatePromotionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_promotion), '/textql.rpc.public.promotion.PromotionService/DeletePromotion': EndpointSync.unary(method=MethodInfo(name='DeletePromotion', service_name='textql.rpc.public.promotion.PromotionService', input=public_dot_promotion__pb2.DeletePromotionRequest, output=public_dot_promotion__pb2.DeletePromotionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_promotion), '/textql.rpc.public.promotion.PromotionService/ListPromotionGrants': EndpointSync.unary(method=MethodInfo(name='ListPromotionGrants', service_name='textql.rpc.public.promotion.PromotionService', input=public_dot_promotion__pb2.ListPromotionGrantsRequest, output=public_dot_promotion__pb2.ListPromotionGrantsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_promotion_grants), '/textql.rpc.public.promotion.PromotionService/ListEventCategories': EndpointSync.unary(method=MethodInfo(name='ListEventCategories', service_name='textql.rpc.public.promotion.PromotionService', input=public_dot_promotion__pb2.ListEventCategoriesRequest, output=public_dot_promotion__pb2.ListEventCategoriesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_event_categories)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.promotion.PromotionService'

class PromotionServiceClientSync(ConnectClientSync):

    def list_promotions(self, request: public_dot_promotion__pb2.ListPromotionsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_promotion__pb2.ListPromotionsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListPromotions', service_name='textql.rpc.public.promotion.PromotionService', input=public_dot_promotion__pb2.ListPromotionsRequest, output=public_dot_promotion__pb2.ListPromotionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def create_promotion(self, request: public_dot_promotion__pb2.CreatePromotionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_promotion__pb2.CreatePromotionResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreatePromotion', service_name='textql.rpc.public.promotion.PromotionService', input=public_dot_promotion__pb2.CreatePromotionRequest, output=public_dot_promotion__pb2.CreatePromotionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def update_promotion(self, request: public_dot_promotion__pb2.UpdatePromotionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_promotion__pb2.UpdatePromotionResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdatePromotion', service_name='textql.rpc.public.promotion.PromotionService', input=public_dot_promotion__pb2.UpdatePromotionRequest, output=public_dot_promotion__pb2.UpdatePromotionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def delete_promotion(self, request: public_dot_promotion__pb2.DeletePromotionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_promotion__pb2.DeletePromotionResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DeletePromotion', service_name='textql.rpc.public.promotion.PromotionService', input=public_dot_promotion__pb2.DeletePromotionRequest, output=public_dot_promotion__pb2.DeletePromotionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_promotion_grants(self, request: public_dot_promotion__pb2.ListPromotionGrantsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_promotion__pb2.ListPromotionGrantsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListPromotionGrants', service_name='textql.rpc.public.promotion.PromotionService', input=public_dot_promotion__pb2.ListPromotionGrantsRequest, output=public_dot_promotion__pb2.ListPromotionGrantsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_event_categories(self, request: public_dot_promotion__pb2.ListEventCategoriesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_promotion__pb2.ListEventCategoriesResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListEventCategories', service_name='textql.rpc.public.promotion.PromotionService', input=public_dot_promotion__pb2.ListEventCategoriesRequest, output=public_dot_promotion__pb2.ListEventCategoriesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)