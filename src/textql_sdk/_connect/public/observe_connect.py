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
from . import observe_pb2 as public_dot_observe__pb2

class ObservabilityService(Protocol):

    async def get_thread_warnings(self, request: public_dot_observe__pb2.GetThreadWarningsRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetThreadWarningsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def fix_warning(self, request: public_dot_observe__pb2.FixWarningRequest, ctx: RequestContext) -> public_dot_observe__pb2.FixWarningResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def fix_check_record(self, request: public_dot_observe__pb2.FixCheckRecordRequest, ctx: RequestContext) -> public_dot_observe__pb2.FixCheckRecordResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_check_record_fix(self, request: public_dot_observe__pb2.GetCheckRecordFixRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetCheckRecordFixResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_observability_stats(self, request: public_dot_observe__pb2.GetObservabilityStatsRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetObservabilityStatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_backfill_preview(self, request: public_dot_observe__pb2.GetBackfillPreviewRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetBackfillPreviewResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def backfill_thread_warnings(self, request: public_dot_observe__pb2.BackfillThreadWarningsRequest, ctx: RequestContext) -> public_dot_observe__pb2.BackfillThreadWarningsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_backfill_status(self, request: public_dot_observe__pb2.GetBackfillStatusRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetBackfillStatusResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_billing_stats(self, request: public_dot_observe__pb2.GetBillingStatsRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetBillingStatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_active_people_stats(self, request: public_dot_observe__pb2.GetActivePeopleStatsRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetActivePeopleStatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_chat_source_stats(self, request: public_dot_observe__pb2.GetChatSourceStatsRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetChatSourceStatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_active_people_trend(self, request: public_dot_observe__pb2.GetActivePeopleTrendRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetActivePeopleTrendResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_engagement_spectrum(self, request: public_dot_observe__pb2.GetEngagementSpectrumRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetEngagementSpectrumResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_access_method_stats(self, request: public_dot_observe__pb2.GetAccessMethodStatsRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetAccessMethodStatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_member_activity(self, request: public_dot_observe__pb2.GetMemberActivityRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetMemberActivityResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_member_signal_trend(self, request: public_dot_observe__pb2.GetMemberSignalTrendRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetMemberSignalTrendResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def export_observability_csv(self, request: public_dot_observe__pb2.ExportObservabilityCsvRequest, ctx: RequestContext) -> public_dot_observe__pb2.ExportObservabilityCsvResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def refine_topic_draft(self, request: public_dot_observe__pb2.RefineTopicDraftRequest, ctx: RequestContext) -> public_dot_observe__pb2.RefineTopicDraftResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def create_custom_topic(self, request: public_dot_observe__pb2.CreateCustomTopicRequest, ctx: RequestContext) -> public_dot_observe__pb2.CustomTopicResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def backfill_custom_topic(self, request: public_dot_observe__pb2.BackfillCustomTopicRequest, ctx: RequestContext) -> public_dot_observe__pb2.BackfillCustomTopicResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_custom_topic(self, request: public_dot_observe__pb2.GetCustomTopicRequest, ctx: RequestContext) -> public_dot_observe__pb2.CustomTopicResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_custom_topics(self, request: public_dot_observe__pb2.ListCustomTopicsRequest, ctx: RequestContext) -> public_dot_observe__pb2.ListCustomTopicsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_custom_topic_threads(self, request: public_dot_observe__pb2.GetCustomTopicThreadsRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetCustomTopicThreadsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_custom_topic_people(self, request: public_dot_observe__pb2.GetCustomTopicPeopleRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetCustomTopicPeopleResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_chat_topics(self, request: public_dot_observe__pb2.GetChatTopicsRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetChatTopicsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_custom_topic(self, request: public_dot_observe__pb2.UpdateCustomTopicRequest, ctx: RequestContext) -> public_dot_observe__pb2.CustomTopicResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def set_topic_tag_feedback(self, request: public_dot_observe__pb2.SetTopicTagFeedbackRequest, ctx: RequestContext) -> public_dot_observe__pb2.SetTopicTagFeedbackResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def activate_custom_topic(self, request: public_dot_observe__pb2.TopicLifecycleRequest, ctx: RequestContext) -> public_dot_observe__pb2.TopicLifecycleResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def deactivate_custom_topic(self, request: public_dot_observe__pb2.TopicLifecycleRequest, ctx: RequestContext) -> public_dot_observe__pb2.TopicLifecycleResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_custom_topic(self, request: public_dot_observe__pb2.TopicLifecycleRequest, ctx: RequestContext) -> public_dot_observe__pb2.TopicLifecycleResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class ObservabilityServiceASGIApplication(ConnectASGIApplication[ObservabilityService]):

    def __init__(self, service: ObservabilityService | AsyncGenerator[ObservabilityService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.observe.ObservabilityService/GetThreadWarnings': Endpoint.unary(method=MethodInfo(name='GetThreadWarnings', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetThreadWarningsRequest, output=public_dot_observe__pb2.GetThreadWarningsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_thread_warnings), '/textql.rpc.public.observe.ObservabilityService/FixWarning': Endpoint.unary(method=MethodInfo(name='FixWarning', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.FixWarningRequest, output=public_dot_observe__pb2.FixWarningResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.fix_warning), '/textql.rpc.public.observe.ObservabilityService/FixCheckRecord': Endpoint.unary(method=MethodInfo(name='FixCheckRecord', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.FixCheckRecordRequest, output=public_dot_observe__pb2.FixCheckRecordResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.fix_check_record), '/textql.rpc.public.observe.ObservabilityService/GetCheckRecordFix': Endpoint.unary(method=MethodInfo(name='GetCheckRecordFix', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetCheckRecordFixRequest, output=public_dot_observe__pb2.GetCheckRecordFixResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_check_record_fix), '/textql.rpc.public.observe.ObservabilityService/GetObservabilityStats': Endpoint.unary(method=MethodInfo(name='GetObservabilityStats', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetObservabilityStatsRequest, output=public_dot_observe__pb2.GetObservabilityStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_observability_stats), '/textql.rpc.public.observe.ObservabilityService/GetBackfillPreview': Endpoint.unary(method=MethodInfo(name='GetBackfillPreview', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetBackfillPreviewRequest, output=public_dot_observe__pb2.GetBackfillPreviewResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_backfill_preview), '/textql.rpc.public.observe.ObservabilityService/BackfillThreadWarnings': Endpoint.unary(method=MethodInfo(name='BackfillThreadWarnings', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.BackfillThreadWarningsRequest, output=public_dot_observe__pb2.BackfillThreadWarningsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.backfill_thread_warnings), '/textql.rpc.public.observe.ObservabilityService/GetBackfillStatus': Endpoint.unary(method=MethodInfo(name='GetBackfillStatus', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetBackfillStatusRequest, output=public_dot_observe__pb2.GetBackfillStatusResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_backfill_status), '/textql.rpc.public.observe.ObservabilityService/GetBillingStats': Endpoint.unary(method=MethodInfo(name='GetBillingStats', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetBillingStatsRequest, output=public_dot_observe__pb2.GetBillingStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_billing_stats), '/textql.rpc.public.observe.ObservabilityService/GetActivePeopleStats': Endpoint.unary(method=MethodInfo(name='GetActivePeopleStats', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetActivePeopleStatsRequest, output=public_dot_observe__pb2.GetActivePeopleStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_active_people_stats), '/textql.rpc.public.observe.ObservabilityService/GetChatSourceStats': Endpoint.unary(method=MethodInfo(name='GetChatSourceStats', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetChatSourceStatsRequest, output=public_dot_observe__pb2.GetChatSourceStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_chat_source_stats), '/textql.rpc.public.observe.ObservabilityService/GetActivePeopleTrend': Endpoint.unary(method=MethodInfo(name='GetActivePeopleTrend', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetActivePeopleTrendRequest, output=public_dot_observe__pb2.GetActivePeopleTrendResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_active_people_trend), '/textql.rpc.public.observe.ObservabilityService/GetEngagementSpectrum': Endpoint.unary(method=MethodInfo(name='GetEngagementSpectrum', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetEngagementSpectrumRequest, output=public_dot_observe__pb2.GetEngagementSpectrumResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_engagement_spectrum), '/textql.rpc.public.observe.ObservabilityService/GetAccessMethodStats': Endpoint.unary(method=MethodInfo(name='GetAccessMethodStats', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetAccessMethodStatsRequest, output=public_dot_observe__pb2.GetAccessMethodStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_access_method_stats), '/textql.rpc.public.observe.ObservabilityService/GetMemberActivity': Endpoint.unary(method=MethodInfo(name='GetMemberActivity', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetMemberActivityRequest, output=public_dot_observe__pb2.GetMemberActivityResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_member_activity), '/textql.rpc.public.observe.ObservabilityService/GetMemberSignalTrend': Endpoint.unary(method=MethodInfo(name='GetMemberSignalTrend', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetMemberSignalTrendRequest, output=public_dot_observe__pb2.GetMemberSignalTrendResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_member_signal_trend), '/textql.rpc.public.observe.ObservabilityService/ExportObservabilityCsv': Endpoint.unary(method=MethodInfo(name='ExportObservabilityCsv', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.ExportObservabilityCsvRequest, output=public_dot_observe__pb2.ExportObservabilityCsvResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.export_observability_csv), '/textql.rpc.public.observe.ObservabilityService/RefineTopicDraft': Endpoint.unary(method=MethodInfo(name='RefineTopicDraft', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.RefineTopicDraftRequest, output=public_dot_observe__pb2.RefineTopicDraftResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.refine_topic_draft), '/textql.rpc.public.observe.ObservabilityService/CreateCustomTopic': Endpoint.unary(method=MethodInfo(name='CreateCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.CreateCustomTopicRequest, output=public_dot_observe__pb2.CustomTopicResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_custom_topic), '/textql.rpc.public.observe.ObservabilityService/BackfillCustomTopic': Endpoint.unary(method=MethodInfo(name='BackfillCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.BackfillCustomTopicRequest, output=public_dot_observe__pb2.BackfillCustomTopicResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.backfill_custom_topic), '/textql.rpc.public.observe.ObservabilityService/GetCustomTopic': Endpoint.unary(method=MethodInfo(name='GetCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetCustomTopicRequest, output=public_dot_observe__pb2.CustomTopicResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_custom_topic), '/textql.rpc.public.observe.ObservabilityService/ListCustomTopics': Endpoint.unary(method=MethodInfo(name='ListCustomTopics', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.ListCustomTopicsRequest, output=public_dot_observe__pb2.ListCustomTopicsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_custom_topics), '/textql.rpc.public.observe.ObservabilityService/GetCustomTopicThreads': Endpoint.unary(method=MethodInfo(name='GetCustomTopicThreads', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetCustomTopicThreadsRequest, output=public_dot_observe__pb2.GetCustomTopicThreadsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_custom_topic_threads), '/textql.rpc.public.observe.ObservabilityService/GetCustomTopicPeople': Endpoint.unary(method=MethodInfo(name='GetCustomTopicPeople', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetCustomTopicPeopleRequest, output=public_dot_observe__pb2.GetCustomTopicPeopleResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_custom_topic_people), '/textql.rpc.public.observe.ObservabilityService/GetChatTopics': Endpoint.unary(method=MethodInfo(name='GetChatTopics', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetChatTopicsRequest, output=public_dot_observe__pb2.GetChatTopicsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_chat_topics), '/textql.rpc.public.observe.ObservabilityService/UpdateCustomTopic': Endpoint.unary(method=MethodInfo(name='UpdateCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.UpdateCustomTopicRequest, output=public_dot_observe__pb2.CustomTopicResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_custom_topic), '/textql.rpc.public.observe.ObservabilityService/SetTopicTagFeedback': Endpoint.unary(method=MethodInfo(name='SetTopicTagFeedback', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.SetTopicTagFeedbackRequest, output=public_dot_observe__pb2.SetTopicTagFeedbackResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.set_topic_tag_feedback), '/textql.rpc.public.observe.ObservabilityService/ActivateCustomTopic': Endpoint.unary(method=MethodInfo(name='ActivateCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.TopicLifecycleRequest, output=public_dot_observe__pb2.TopicLifecycleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.activate_custom_topic), '/textql.rpc.public.observe.ObservabilityService/DeactivateCustomTopic': Endpoint.unary(method=MethodInfo(name='DeactivateCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.TopicLifecycleRequest, output=public_dot_observe__pb2.TopicLifecycleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.deactivate_custom_topic), '/textql.rpc.public.observe.ObservabilityService/DeleteCustomTopic': Endpoint.unary(method=MethodInfo(name='DeleteCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.TopicLifecycleRequest, output=public_dot_observe__pb2.TopicLifecycleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_custom_topic)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.observe.ObservabilityService'

class ObservabilityServiceClient(ConnectClient):

    async def get_thread_warnings(self, request: public_dot_observe__pb2.GetThreadWarningsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetThreadWarningsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetThreadWarnings', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetThreadWarningsRequest, output=public_dot_observe__pb2.GetThreadWarningsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def fix_warning(self, request: public_dot_observe__pb2.FixWarningRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_observe__pb2.FixWarningResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='FixWarning', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.FixWarningRequest, output=public_dot_observe__pb2.FixWarningResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def fix_check_record(self, request: public_dot_observe__pb2.FixCheckRecordRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_observe__pb2.FixCheckRecordResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='FixCheckRecord', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.FixCheckRecordRequest, output=public_dot_observe__pb2.FixCheckRecordResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_check_record_fix(self, request: public_dot_observe__pb2.GetCheckRecordFixRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetCheckRecordFixResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetCheckRecordFix', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetCheckRecordFixRequest, output=public_dot_observe__pb2.GetCheckRecordFixResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_observability_stats(self, request: public_dot_observe__pb2.GetObservabilityStatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetObservabilityStatsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetObservabilityStats', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetObservabilityStatsRequest, output=public_dot_observe__pb2.GetObservabilityStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_backfill_preview(self, request: public_dot_observe__pb2.GetBackfillPreviewRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetBackfillPreviewResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetBackfillPreview', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetBackfillPreviewRequest, output=public_dot_observe__pb2.GetBackfillPreviewResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def backfill_thread_warnings(self, request: public_dot_observe__pb2.BackfillThreadWarningsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_observe__pb2.BackfillThreadWarningsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='BackfillThreadWarnings', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.BackfillThreadWarningsRequest, output=public_dot_observe__pb2.BackfillThreadWarningsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_backfill_status(self, request: public_dot_observe__pb2.GetBackfillStatusRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetBackfillStatusResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetBackfillStatus', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetBackfillStatusRequest, output=public_dot_observe__pb2.GetBackfillStatusResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_billing_stats(self, request: public_dot_observe__pb2.GetBillingStatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetBillingStatsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetBillingStats', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetBillingStatsRequest, output=public_dot_observe__pb2.GetBillingStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_active_people_stats(self, request: public_dot_observe__pb2.GetActivePeopleStatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetActivePeopleStatsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetActivePeopleStats', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetActivePeopleStatsRequest, output=public_dot_observe__pb2.GetActivePeopleStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_chat_source_stats(self, request: public_dot_observe__pb2.GetChatSourceStatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetChatSourceStatsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetChatSourceStats', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetChatSourceStatsRequest, output=public_dot_observe__pb2.GetChatSourceStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_active_people_trend(self, request: public_dot_observe__pb2.GetActivePeopleTrendRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetActivePeopleTrendResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetActivePeopleTrend', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetActivePeopleTrendRequest, output=public_dot_observe__pb2.GetActivePeopleTrendResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_engagement_spectrum(self, request: public_dot_observe__pb2.GetEngagementSpectrumRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetEngagementSpectrumResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetEngagementSpectrum', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetEngagementSpectrumRequest, output=public_dot_observe__pb2.GetEngagementSpectrumResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_access_method_stats(self, request: public_dot_observe__pb2.GetAccessMethodStatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetAccessMethodStatsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetAccessMethodStats', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetAccessMethodStatsRequest, output=public_dot_observe__pb2.GetAccessMethodStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_member_activity(self, request: public_dot_observe__pb2.GetMemberActivityRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetMemberActivityResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetMemberActivity', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetMemberActivityRequest, output=public_dot_observe__pb2.GetMemberActivityResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_member_signal_trend(self, request: public_dot_observe__pb2.GetMemberSignalTrendRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetMemberSignalTrendResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetMemberSignalTrend', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetMemberSignalTrendRequest, output=public_dot_observe__pb2.GetMemberSignalTrendResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def export_observability_csv(self, request: public_dot_observe__pb2.ExportObservabilityCsvRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_observe__pb2.ExportObservabilityCsvResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ExportObservabilityCsv', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.ExportObservabilityCsvRequest, output=public_dot_observe__pb2.ExportObservabilityCsvResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def refine_topic_draft(self, request: public_dot_observe__pb2.RefineTopicDraftRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_observe__pb2.RefineTopicDraftResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RefineTopicDraft', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.RefineTopicDraftRequest, output=public_dot_observe__pb2.RefineTopicDraftResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def create_custom_topic(self, request: public_dot_observe__pb2.CreateCustomTopicRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_observe__pb2.CustomTopicResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.CreateCustomTopicRequest, output=public_dot_observe__pb2.CustomTopicResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def backfill_custom_topic(self, request: public_dot_observe__pb2.BackfillCustomTopicRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_observe__pb2.BackfillCustomTopicResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='BackfillCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.BackfillCustomTopicRequest, output=public_dot_observe__pb2.BackfillCustomTopicResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_custom_topic(self, request: public_dot_observe__pb2.GetCustomTopicRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.CustomTopicResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetCustomTopicRequest, output=public_dot_observe__pb2.CustomTopicResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def list_custom_topics(self, request: public_dot_observe__pb2.ListCustomTopicsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.ListCustomTopicsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListCustomTopics', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.ListCustomTopicsRequest, output=public_dot_observe__pb2.ListCustomTopicsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_custom_topic_threads(self, request: public_dot_observe__pb2.GetCustomTopicThreadsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetCustomTopicThreadsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetCustomTopicThreads', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetCustomTopicThreadsRequest, output=public_dot_observe__pb2.GetCustomTopicThreadsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_custom_topic_people(self, request: public_dot_observe__pb2.GetCustomTopicPeopleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetCustomTopicPeopleResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetCustomTopicPeople', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetCustomTopicPeopleRequest, output=public_dot_observe__pb2.GetCustomTopicPeopleResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_chat_topics(self, request: public_dot_observe__pb2.GetChatTopicsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetChatTopicsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetChatTopics', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetChatTopicsRequest, output=public_dot_observe__pb2.GetChatTopicsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def update_custom_topic(self, request: public_dot_observe__pb2.UpdateCustomTopicRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_observe__pb2.CustomTopicResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.UpdateCustomTopicRequest, output=public_dot_observe__pb2.CustomTopicResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def set_topic_tag_feedback(self, request: public_dot_observe__pb2.SetTopicTagFeedbackRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_observe__pb2.SetTopicTagFeedbackResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='SetTopicTagFeedback', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.SetTopicTagFeedbackRequest, output=public_dot_observe__pb2.SetTopicTagFeedbackResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def activate_custom_topic(self, request: public_dot_observe__pb2.TopicLifecycleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_observe__pb2.TopicLifecycleResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ActivateCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.TopicLifecycleRequest, output=public_dot_observe__pb2.TopicLifecycleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def deactivate_custom_topic(self, request: public_dot_observe__pb2.TopicLifecycleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_observe__pb2.TopicLifecycleResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeactivateCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.TopicLifecycleRequest, output=public_dot_observe__pb2.TopicLifecycleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def delete_custom_topic(self, request: public_dot_observe__pb2.TopicLifecycleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_observe__pb2.TopicLifecycleResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.TopicLifecycleRequest, output=public_dot_observe__pb2.TopicLifecycleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class ObservabilityServiceSync(Protocol):

    def get_thread_warnings(self, request: public_dot_observe__pb2.GetThreadWarningsRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetThreadWarningsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def fix_warning(self, request: public_dot_observe__pb2.FixWarningRequest, ctx: RequestContext) -> public_dot_observe__pb2.FixWarningResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def fix_check_record(self, request: public_dot_observe__pb2.FixCheckRecordRequest, ctx: RequestContext) -> public_dot_observe__pb2.FixCheckRecordResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_check_record_fix(self, request: public_dot_observe__pb2.GetCheckRecordFixRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetCheckRecordFixResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_observability_stats(self, request: public_dot_observe__pb2.GetObservabilityStatsRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetObservabilityStatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_backfill_preview(self, request: public_dot_observe__pb2.GetBackfillPreviewRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetBackfillPreviewResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def backfill_thread_warnings(self, request: public_dot_observe__pb2.BackfillThreadWarningsRequest, ctx: RequestContext) -> public_dot_observe__pb2.BackfillThreadWarningsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_backfill_status(self, request: public_dot_observe__pb2.GetBackfillStatusRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetBackfillStatusResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_billing_stats(self, request: public_dot_observe__pb2.GetBillingStatsRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetBillingStatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_active_people_stats(self, request: public_dot_observe__pb2.GetActivePeopleStatsRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetActivePeopleStatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_chat_source_stats(self, request: public_dot_observe__pb2.GetChatSourceStatsRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetChatSourceStatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_active_people_trend(self, request: public_dot_observe__pb2.GetActivePeopleTrendRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetActivePeopleTrendResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_engagement_spectrum(self, request: public_dot_observe__pb2.GetEngagementSpectrumRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetEngagementSpectrumResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_access_method_stats(self, request: public_dot_observe__pb2.GetAccessMethodStatsRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetAccessMethodStatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_member_activity(self, request: public_dot_observe__pb2.GetMemberActivityRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetMemberActivityResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_member_signal_trend(self, request: public_dot_observe__pb2.GetMemberSignalTrendRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetMemberSignalTrendResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def export_observability_csv(self, request: public_dot_observe__pb2.ExportObservabilityCsvRequest, ctx: RequestContext) -> public_dot_observe__pb2.ExportObservabilityCsvResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def refine_topic_draft(self, request: public_dot_observe__pb2.RefineTopicDraftRequest, ctx: RequestContext) -> public_dot_observe__pb2.RefineTopicDraftResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def create_custom_topic(self, request: public_dot_observe__pb2.CreateCustomTopicRequest, ctx: RequestContext) -> public_dot_observe__pb2.CustomTopicResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def backfill_custom_topic(self, request: public_dot_observe__pb2.BackfillCustomTopicRequest, ctx: RequestContext) -> public_dot_observe__pb2.BackfillCustomTopicResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_custom_topic(self, request: public_dot_observe__pb2.GetCustomTopicRequest, ctx: RequestContext) -> public_dot_observe__pb2.CustomTopicResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_custom_topics(self, request: public_dot_observe__pb2.ListCustomTopicsRequest, ctx: RequestContext) -> public_dot_observe__pb2.ListCustomTopicsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_custom_topic_threads(self, request: public_dot_observe__pb2.GetCustomTopicThreadsRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetCustomTopicThreadsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_custom_topic_people(self, request: public_dot_observe__pb2.GetCustomTopicPeopleRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetCustomTopicPeopleResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_chat_topics(self, request: public_dot_observe__pb2.GetChatTopicsRequest, ctx: RequestContext) -> public_dot_observe__pb2.GetChatTopicsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_custom_topic(self, request: public_dot_observe__pb2.UpdateCustomTopicRequest, ctx: RequestContext) -> public_dot_observe__pb2.CustomTopicResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def set_topic_tag_feedback(self, request: public_dot_observe__pb2.SetTopicTagFeedbackRequest, ctx: RequestContext) -> public_dot_observe__pb2.SetTopicTagFeedbackResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def activate_custom_topic(self, request: public_dot_observe__pb2.TopicLifecycleRequest, ctx: RequestContext) -> public_dot_observe__pb2.TopicLifecycleResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def deactivate_custom_topic(self, request: public_dot_observe__pb2.TopicLifecycleRequest, ctx: RequestContext) -> public_dot_observe__pb2.TopicLifecycleResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_custom_topic(self, request: public_dot_observe__pb2.TopicLifecycleRequest, ctx: RequestContext) -> public_dot_observe__pb2.TopicLifecycleResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class ObservabilityServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: ObservabilityServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.observe.ObservabilityService/GetThreadWarnings': EndpointSync.unary(method=MethodInfo(name='GetThreadWarnings', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetThreadWarningsRequest, output=public_dot_observe__pb2.GetThreadWarningsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_thread_warnings), '/textql.rpc.public.observe.ObservabilityService/FixWarning': EndpointSync.unary(method=MethodInfo(name='FixWarning', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.FixWarningRequest, output=public_dot_observe__pb2.FixWarningResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.fix_warning), '/textql.rpc.public.observe.ObservabilityService/FixCheckRecord': EndpointSync.unary(method=MethodInfo(name='FixCheckRecord', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.FixCheckRecordRequest, output=public_dot_observe__pb2.FixCheckRecordResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.fix_check_record), '/textql.rpc.public.observe.ObservabilityService/GetCheckRecordFix': EndpointSync.unary(method=MethodInfo(name='GetCheckRecordFix', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetCheckRecordFixRequest, output=public_dot_observe__pb2.GetCheckRecordFixResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_check_record_fix), '/textql.rpc.public.observe.ObservabilityService/GetObservabilityStats': EndpointSync.unary(method=MethodInfo(name='GetObservabilityStats', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetObservabilityStatsRequest, output=public_dot_observe__pb2.GetObservabilityStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_observability_stats), '/textql.rpc.public.observe.ObservabilityService/GetBackfillPreview': EndpointSync.unary(method=MethodInfo(name='GetBackfillPreview', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetBackfillPreviewRequest, output=public_dot_observe__pb2.GetBackfillPreviewResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_backfill_preview), '/textql.rpc.public.observe.ObservabilityService/BackfillThreadWarnings': EndpointSync.unary(method=MethodInfo(name='BackfillThreadWarnings', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.BackfillThreadWarningsRequest, output=public_dot_observe__pb2.BackfillThreadWarningsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.backfill_thread_warnings), '/textql.rpc.public.observe.ObservabilityService/GetBackfillStatus': EndpointSync.unary(method=MethodInfo(name='GetBackfillStatus', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetBackfillStatusRequest, output=public_dot_observe__pb2.GetBackfillStatusResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_backfill_status), '/textql.rpc.public.observe.ObservabilityService/GetBillingStats': EndpointSync.unary(method=MethodInfo(name='GetBillingStats', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetBillingStatsRequest, output=public_dot_observe__pb2.GetBillingStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_billing_stats), '/textql.rpc.public.observe.ObservabilityService/GetActivePeopleStats': EndpointSync.unary(method=MethodInfo(name='GetActivePeopleStats', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetActivePeopleStatsRequest, output=public_dot_observe__pb2.GetActivePeopleStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_active_people_stats), '/textql.rpc.public.observe.ObservabilityService/GetChatSourceStats': EndpointSync.unary(method=MethodInfo(name='GetChatSourceStats', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetChatSourceStatsRequest, output=public_dot_observe__pb2.GetChatSourceStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_chat_source_stats), '/textql.rpc.public.observe.ObservabilityService/GetActivePeopleTrend': EndpointSync.unary(method=MethodInfo(name='GetActivePeopleTrend', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetActivePeopleTrendRequest, output=public_dot_observe__pb2.GetActivePeopleTrendResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_active_people_trend), '/textql.rpc.public.observe.ObservabilityService/GetEngagementSpectrum': EndpointSync.unary(method=MethodInfo(name='GetEngagementSpectrum', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetEngagementSpectrumRequest, output=public_dot_observe__pb2.GetEngagementSpectrumResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_engagement_spectrum), '/textql.rpc.public.observe.ObservabilityService/GetAccessMethodStats': EndpointSync.unary(method=MethodInfo(name='GetAccessMethodStats', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetAccessMethodStatsRequest, output=public_dot_observe__pb2.GetAccessMethodStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_access_method_stats), '/textql.rpc.public.observe.ObservabilityService/GetMemberActivity': EndpointSync.unary(method=MethodInfo(name='GetMemberActivity', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetMemberActivityRequest, output=public_dot_observe__pb2.GetMemberActivityResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_member_activity), '/textql.rpc.public.observe.ObservabilityService/GetMemberSignalTrend': EndpointSync.unary(method=MethodInfo(name='GetMemberSignalTrend', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetMemberSignalTrendRequest, output=public_dot_observe__pb2.GetMemberSignalTrendResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_member_signal_trend), '/textql.rpc.public.observe.ObservabilityService/ExportObservabilityCsv': EndpointSync.unary(method=MethodInfo(name='ExportObservabilityCsv', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.ExportObservabilityCsvRequest, output=public_dot_observe__pb2.ExportObservabilityCsvResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.export_observability_csv), '/textql.rpc.public.observe.ObservabilityService/RefineTopicDraft': EndpointSync.unary(method=MethodInfo(name='RefineTopicDraft', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.RefineTopicDraftRequest, output=public_dot_observe__pb2.RefineTopicDraftResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.refine_topic_draft), '/textql.rpc.public.observe.ObservabilityService/CreateCustomTopic': EndpointSync.unary(method=MethodInfo(name='CreateCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.CreateCustomTopicRequest, output=public_dot_observe__pb2.CustomTopicResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_custom_topic), '/textql.rpc.public.observe.ObservabilityService/BackfillCustomTopic': EndpointSync.unary(method=MethodInfo(name='BackfillCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.BackfillCustomTopicRequest, output=public_dot_observe__pb2.BackfillCustomTopicResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.backfill_custom_topic), '/textql.rpc.public.observe.ObservabilityService/GetCustomTopic': EndpointSync.unary(method=MethodInfo(name='GetCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetCustomTopicRequest, output=public_dot_observe__pb2.CustomTopicResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_custom_topic), '/textql.rpc.public.observe.ObservabilityService/ListCustomTopics': EndpointSync.unary(method=MethodInfo(name='ListCustomTopics', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.ListCustomTopicsRequest, output=public_dot_observe__pb2.ListCustomTopicsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_custom_topics), '/textql.rpc.public.observe.ObservabilityService/GetCustomTopicThreads': EndpointSync.unary(method=MethodInfo(name='GetCustomTopicThreads', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetCustomTopicThreadsRequest, output=public_dot_observe__pb2.GetCustomTopicThreadsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_custom_topic_threads), '/textql.rpc.public.observe.ObservabilityService/GetCustomTopicPeople': EndpointSync.unary(method=MethodInfo(name='GetCustomTopicPeople', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetCustomTopicPeopleRequest, output=public_dot_observe__pb2.GetCustomTopicPeopleResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_custom_topic_people), '/textql.rpc.public.observe.ObservabilityService/GetChatTopics': EndpointSync.unary(method=MethodInfo(name='GetChatTopics', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetChatTopicsRequest, output=public_dot_observe__pb2.GetChatTopicsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_chat_topics), '/textql.rpc.public.observe.ObservabilityService/UpdateCustomTopic': EndpointSync.unary(method=MethodInfo(name='UpdateCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.UpdateCustomTopicRequest, output=public_dot_observe__pb2.CustomTopicResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_custom_topic), '/textql.rpc.public.observe.ObservabilityService/SetTopicTagFeedback': EndpointSync.unary(method=MethodInfo(name='SetTopicTagFeedback', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.SetTopicTagFeedbackRequest, output=public_dot_observe__pb2.SetTopicTagFeedbackResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.set_topic_tag_feedback), '/textql.rpc.public.observe.ObservabilityService/ActivateCustomTopic': EndpointSync.unary(method=MethodInfo(name='ActivateCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.TopicLifecycleRequest, output=public_dot_observe__pb2.TopicLifecycleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.activate_custom_topic), '/textql.rpc.public.observe.ObservabilityService/DeactivateCustomTopic': EndpointSync.unary(method=MethodInfo(name='DeactivateCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.TopicLifecycleRequest, output=public_dot_observe__pb2.TopicLifecycleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.deactivate_custom_topic), '/textql.rpc.public.observe.ObservabilityService/DeleteCustomTopic': EndpointSync.unary(method=MethodInfo(name='DeleteCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.TopicLifecycleRequest, output=public_dot_observe__pb2.TopicLifecycleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_custom_topic)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.observe.ObservabilityService'

class ObservabilityServiceClientSync(ConnectClientSync):

    def get_thread_warnings(self, request: public_dot_observe__pb2.GetThreadWarningsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetThreadWarningsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetThreadWarnings', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetThreadWarningsRequest, output=public_dot_observe__pb2.GetThreadWarningsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def fix_warning(self, request: public_dot_observe__pb2.FixWarningRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_observe__pb2.FixWarningResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='FixWarning', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.FixWarningRequest, output=public_dot_observe__pb2.FixWarningResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def fix_check_record(self, request: public_dot_observe__pb2.FixCheckRecordRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_observe__pb2.FixCheckRecordResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='FixCheckRecord', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.FixCheckRecordRequest, output=public_dot_observe__pb2.FixCheckRecordResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_check_record_fix(self, request: public_dot_observe__pb2.GetCheckRecordFixRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetCheckRecordFixResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetCheckRecordFix', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetCheckRecordFixRequest, output=public_dot_observe__pb2.GetCheckRecordFixResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_observability_stats(self, request: public_dot_observe__pb2.GetObservabilityStatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetObservabilityStatsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetObservabilityStats', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetObservabilityStatsRequest, output=public_dot_observe__pb2.GetObservabilityStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_backfill_preview(self, request: public_dot_observe__pb2.GetBackfillPreviewRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetBackfillPreviewResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetBackfillPreview', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetBackfillPreviewRequest, output=public_dot_observe__pb2.GetBackfillPreviewResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def backfill_thread_warnings(self, request: public_dot_observe__pb2.BackfillThreadWarningsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_observe__pb2.BackfillThreadWarningsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='BackfillThreadWarnings', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.BackfillThreadWarningsRequest, output=public_dot_observe__pb2.BackfillThreadWarningsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_backfill_status(self, request: public_dot_observe__pb2.GetBackfillStatusRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetBackfillStatusResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetBackfillStatus', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetBackfillStatusRequest, output=public_dot_observe__pb2.GetBackfillStatusResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_billing_stats(self, request: public_dot_observe__pb2.GetBillingStatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetBillingStatsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetBillingStats', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetBillingStatsRequest, output=public_dot_observe__pb2.GetBillingStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_active_people_stats(self, request: public_dot_observe__pb2.GetActivePeopleStatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetActivePeopleStatsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetActivePeopleStats', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetActivePeopleStatsRequest, output=public_dot_observe__pb2.GetActivePeopleStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_chat_source_stats(self, request: public_dot_observe__pb2.GetChatSourceStatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetChatSourceStatsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetChatSourceStats', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetChatSourceStatsRequest, output=public_dot_observe__pb2.GetChatSourceStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_active_people_trend(self, request: public_dot_observe__pb2.GetActivePeopleTrendRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetActivePeopleTrendResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetActivePeopleTrend', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetActivePeopleTrendRequest, output=public_dot_observe__pb2.GetActivePeopleTrendResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_engagement_spectrum(self, request: public_dot_observe__pb2.GetEngagementSpectrumRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetEngagementSpectrumResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetEngagementSpectrum', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetEngagementSpectrumRequest, output=public_dot_observe__pb2.GetEngagementSpectrumResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_access_method_stats(self, request: public_dot_observe__pb2.GetAccessMethodStatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetAccessMethodStatsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetAccessMethodStats', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetAccessMethodStatsRequest, output=public_dot_observe__pb2.GetAccessMethodStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_member_activity(self, request: public_dot_observe__pb2.GetMemberActivityRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetMemberActivityResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetMemberActivity', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetMemberActivityRequest, output=public_dot_observe__pb2.GetMemberActivityResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_member_signal_trend(self, request: public_dot_observe__pb2.GetMemberSignalTrendRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetMemberSignalTrendResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetMemberSignalTrend', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetMemberSignalTrendRequest, output=public_dot_observe__pb2.GetMemberSignalTrendResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def export_observability_csv(self, request: public_dot_observe__pb2.ExportObservabilityCsvRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_observe__pb2.ExportObservabilityCsvResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ExportObservabilityCsv', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.ExportObservabilityCsvRequest, output=public_dot_observe__pb2.ExportObservabilityCsvResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def refine_topic_draft(self, request: public_dot_observe__pb2.RefineTopicDraftRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_observe__pb2.RefineTopicDraftResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RefineTopicDraft', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.RefineTopicDraftRequest, output=public_dot_observe__pb2.RefineTopicDraftResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def create_custom_topic(self, request: public_dot_observe__pb2.CreateCustomTopicRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_observe__pb2.CustomTopicResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.CreateCustomTopicRequest, output=public_dot_observe__pb2.CustomTopicResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def backfill_custom_topic(self, request: public_dot_observe__pb2.BackfillCustomTopicRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_observe__pb2.BackfillCustomTopicResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='BackfillCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.BackfillCustomTopicRequest, output=public_dot_observe__pb2.BackfillCustomTopicResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_custom_topic(self, request: public_dot_observe__pb2.GetCustomTopicRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.CustomTopicResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetCustomTopicRequest, output=public_dot_observe__pb2.CustomTopicResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def list_custom_topics(self, request: public_dot_observe__pb2.ListCustomTopicsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.ListCustomTopicsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListCustomTopics', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.ListCustomTopicsRequest, output=public_dot_observe__pb2.ListCustomTopicsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_custom_topic_threads(self, request: public_dot_observe__pb2.GetCustomTopicThreadsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetCustomTopicThreadsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetCustomTopicThreads', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetCustomTopicThreadsRequest, output=public_dot_observe__pb2.GetCustomTopicThreadsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_custom_topic_people(self, request: public_dot_observe__pb2.GetCustomTopicPeopleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetCustomTopicPeopleResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetCustomTopicPeople', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetCustomTopicPeopleRequest, output=public_dot_observe__pb2.GetCustomTopicPeopleResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_chat_topics(self, request: public_dot_observe__pb2.GetChatTopicsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_observe__pb2.GetChatTopicsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetChatTopics', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.GetChatTopicsRequest, output=public_dot_observe__pb2.GetChatTopicsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def update_custom_topic(self, request: public_dot_observe__pb2.UpdateCustomTopicRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_observe__pb2.CustomTopicResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.UpdateCustomTopicRequest, output=public_dot_observe__pb2.CustomTopicResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def set_topic_tag_feedback(self, request: public_dot_observe__pb2.SetTopicTagFeedbackRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_observe__pb2.SetTopicTagFeedbackResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='SetTopicTagFeedback', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.SetTopicTagFeedbackRequest, output=public_dot_observe__pb2.SetTopicTagFeedbackResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def activate_custom_topic(self, request: public_dot_observe__pb2.TopicLifecycleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_observe__pb2.TopicLifecycleResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ActivateCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.TopicLifecycleRequest, output=public_dot_observe__pb2.TopicLifecycleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def deactivate_custom_topic(self, request: public_dot_observe__pb2.TopicLifecycleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_observe__pb2.TopicLifecycleResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DeactivateCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.TopicLifecycleRequest, output=public_dot_observe__pb2.TopicLifecycleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def delete_custom_topic(self, request: public_dot_observe__pb2.TopicLifecycleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_observe__pb2.TopicLifecycleResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteCustomTopic', service_name='textql.rpc.public.observe.ObservabilityService', input=public_dot_observe__pb2.TopicLifecycleRequest, output=public_dot_observe__pb2.TopicLifecycleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)