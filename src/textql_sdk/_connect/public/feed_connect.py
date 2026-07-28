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
from . import feed_pb2 as public_dot_feed__pb2

class FeedService(Protocol):

    async def create_post(self, request: public_dot_feed__pb2.CreatePostRequest, ctx: RequestContext) -> public_dot_feed__pb2.CreatePostResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_post(self, request: public_dot_feed__pb2.GetPostRequest, ctx: RequestContext) -> public_dot_feed__pb2.GetPostResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_feed(self, request: public_dot_feed__pb2.GetFeedRequest, ctx: RequestContext) -> public_dot_feed__pb2.GetFeedResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_post(self, request: public_dot_feed__pb2.DeletePostRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def vote_thing(self, request: public_dot_feed__pb2.VoteThingRequest, ctx: RequestContext) -> public_dot_feed__pb2.VoteThingResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def create_comment(self, request: public_dot_feed__pb2.CreateCommentRequest, ctx: RequestContext) -> public_dot_feed__pb2.CreateCommentResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_comments(self, request: public_dot_feed__pb2.GetCommentsRequest, ctx: RequestContext) -> public_dot_feed__pb2.GetCommentsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_profile_comments(self, request: public_dot_feed__pb2.GetProfileCommentsRequest, ctx: RequestContext) -> public_dot_feed__pb2.GetProfileCommentsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_comment(self, request: public_dot_feed__pb2.DeleteCommentRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_leaderboard(self, request: public_dot_feed__pb2.GetLeaderboardRequest, ctx: RequestContext) -> public_dot_feed__pb2.GetLeaderboardResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_feed_stats(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_feed__pb2.GetFeedStatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_mentionable_users(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_feed__pb2.ListMentionableUsersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_default_slack_channel(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_feed__pb2.GetDefaultSlackChannelResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def set_default_slack_channel(self, request: public_dot_feed__pb2.SetDefaultSlackChannelRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_default_teams_channel(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_feed__pb2.GetDefaultTeamsChannelResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def set_default_teams_channel(self, request: public_dot_feed__pb2.SetDefaultTeamsChannelRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def stream_feed(self, request: public_dot_feed__pb2.StreamFeedRequest, ctx: RequestContext) -> AsyncIterator[public_dot_feed__pb2.FeedEvent]:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def follow_agent(self, request: public_dot_feed__pb2.FollowAgentRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def unfollow_agent(self, request: public_dot_feed__pb2.UnfollowAgentRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_followed_agents(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_feed__pb2.ListFollowedAgentsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def create_feed_channel(self, request: public_dot_feed__pb2.CreateFeedChannelRequest, ctx: RequestContext) -> public_dot_feed__pb2.CreateFeedChannelResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_feed_channels(self, request: public_dot_feed__pb2.ListFeedChannelsRequest, ctx: RequestContext) -> public_dot_feed__pb2.ListFeedChannelsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_feed_channel(self, request: public_dot_feed__pb2.GetFeedChannelRequest, ctx: RequestContext) -> public_dot_feed__pb2.GetFeedChannelResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_feed_channel(self, request: public_dot_feed__pb2.UpdateFeedChannelRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_feed_channel(self, request: public_dot_feed__pb2.DeleteFeedChannelRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def join_feed_channel(self, request: public_dot_feed__pb2.JoinFeedChannelRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def leave_feed_channel(self, request: public_dot_feed__pb2.LeaveFeedChannelRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class FeedServiceASGIApplication(ConnectASGIApplication[FeedService]):

    def __init__(self, service: FeedService | AsyncGenerator[FeedService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.feed.FeedService/CreatePost': Endpoint.unary(method=MethodInfo(name='CreatePost', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.CreatePostRequest, output=public_dot_feed__pb2.CreatePostResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_post), '/textql.rpc.public.feed.FeedService/GetPost': Endpoint.unary(method=MethodInfo(name='GetPost', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.GetPostRequest, output=public_dot_feed__pb2.GetPostResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_post), '/textql.rpc.public.feed.FeedService/GetFeed': Endpoint.unary(method=MethodInfo(name='GetFeed', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.GetFeedRequest, output=public_dot_feed__pb2.GetFeedResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_feed), '/textql.rpc.public.feed.FeedService/DeletePost': Endpoint.unary(method=MethodInfo(name='DeletePost', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.DeletePostRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_post), '/textql.rpc.public.feed.FeedService/VoteThing': Endpoint.unary(method=MethodInfo(name='VoteThing', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.VoteThingRequest, output=public_dot_feed__pb2.VoteThingResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.vote_thing), '/textql.rpc.public.feed.FeedService/CreateComment': Endpoint.unary(method=MethodInfo(name='CreateComment', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.CreateCommentRequest, output=public_dot_feed__pb2.CreateCommentResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_comment), '/textql.rpc.public.feed.FeedService/GetComments': Endpoint.unary(method=MethodInfo(name='GetComments', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.GetCommentsRequest, output=public_dot_feed__pb2.GetCommentsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_comments), '/textql.rpc.public.feed.FeedService/GetProfileComments': Endpoint.unary(method=MethodInfo(name='GetProfileComments', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.GetProfileCommentsRequest, output=public_dot_feed__pb2.GetProfileCommentsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_profile_comments), '/textql.rpc.public.feed.FeedService/DeleteComment': Endpoint.unary(method=MethodInfo(name='DeleteComment', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.DeleteCommentRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_comment), '/textql.rpc.public.feed.FeedService/GetLeaderboard': Endpoint.unary(method=MethodInfo(name='GetLeaderboard', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.GetLeaderboardRequest, output=public_dot_feed__pb2.GetLeaderboardResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_leaderboard), '/textql.rpc.public.feed.FeedService/GetFeedStats': Endpoint.unary(method=MethodInfo(name='GetFeedStats', service_name='textql.rpc.public.feed.FeedService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_feed__pb2.GetFeedStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_feed_stats), '/textql.rpc.public.feed.FeedService/ListMentionableUsers': Endpoint.unary(method=MethodInfo(name='ListMentionableUsers', service_name='textql.rpc.public.feed.FeedService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_feed__pb2.ListMentionableUsersResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_mentionable_users), '/textql.rpc.public.feed.FeedService/GetDefaultSlackChannel': Endpoint.unary(method=MethodInfo(name='GetDefaultSlackChannel', service_name='textql.rpc.public.feed.FeedService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_feed__pb2.GetDefaultSlackChannelResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_default_slack_channel), '/textql.rpc.public.feed.FeedService/SetDefaultSlackChannel': Endpoint.unary(method=MethodInfo(name='SetDefaultSlackChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.SetDefaultSlackChannelRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.set_default_slack_channel), '/textql.rpc.public.feed.FeedService/GetDefaultTeamsChannel': Endpoint.unary(method=MethodInfo(name='GetDefaultTeamsChannel', service_name='textql.rpc.public.feed.FeedService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_feed__pb2.GetDefaultTeamsChannelResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_default_teams_channel), '/textql.rpc.public.feed.FeedService/SetDefaultTeamsChannel': Endpoint.unary(method=MethodInfo(name='SetDefaultTeamsChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.SetDefaultTeamsChannelRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.set_default_teams_channel), '/textql.rpc.public.feed.FeedService/StreamFeed': Endpoint.server_stream(method=MethodInfo(name='StreamFeed', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.StreamFeedRequest, output=public_dot_feed__pb2.FeedEvent, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.stream_feed), '/textql.rpc.public.feed.FeedService/FollowAgent': Endpoint.unary(method=MethodInfo(name='FollowAgent', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.FollowAgentRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.follow_agent), '/textql.rpc.public.feed.FeedService/UnfollowAgent': Endpoint.unary(method=MethodInfo(name='UnfollowAgent', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.UnfollowAgentRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.unfollow_agent), '/textql.rpc.public.feed.FeedService/ListFollowedAgents': Endpoint.unary(method=MethodInfo(name='ListFollowedAgents', service_name='textql.rpc.public.feed.FeedService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_feed__pb2.ListFollowedAgentsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_followed_agents), '/textql.rpc.public.feed.FeedService/CreateFeedChannel': Endpoint.unary(method=MethodInfo(name='CreateFeedChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.CreateFeedChannelRequest, output=public_dot_feed__pb2.CreateFeedChannelResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_feed_channel), '/textql.rpc.public.feed.FeedService/ListFeedChannels': Endpoint.unary(method=MethodInfo(name='ListFeedChannels', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.ListFeedChannelsRequest, output=public_dot_feed__pb2.ListFeedChannelsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_feed_channels), '/textql.rpc.public.feed.FeedService/GetFeedChannel': Endpoint.unary(method=MethodInfo(name='GetFeedChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.GetFeedChannelRequest, output=public_dot_feed__pb2.GetFeedChannelResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_feed_channel), '/textql.rpc.public.feed.FeedService/UpdateFeedChannel': Endpoint.unary(method=MethodInfo(name='UpdateFeedChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.UpdateFeedChannelRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_feed_channel), '/textql.rpc.public.feed.FeedService/DeleteFeedChannel': Endpoint.unary(method=MethodInfo(name='DeleteFeedChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.DeleteFeedChannelRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_feed_channel), '/textql.rpc.public.feed.FeedService/JoinFeedChannel': Endpoint.unary(method=MethodInfo(name='JoinFeedChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.JoinFeedChannelRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.join_feed_channel), '/textql.rpc.public.feed.FeedService/LeaveFeedChannel': Endpoint.unary(method=MethodInfo(name='LeaveFeedChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.LeaveFeedChannelRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.leave_feed_channel)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.feed.FeedService'

class FeedServiceClient(ConnectClient):

    async def create_post(self, request: public_dot_feed__pb2.CreatePostRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_feed__pb2.CreatePostResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreatePost', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.CreatePostRequest, output=public_dot_feed__pb2.CreatePostResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_post(self, request: public_dot_feed__pb2.GetPostRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_feed__pb2.GetPostResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetPost', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.GetPostRequest, output=public_dot_feed__pb2.GetPostResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_feed(self, request: public_dot_feed__pb2.GetFeedRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_feed__pb2.GetFeedResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetFeed', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.GetFeedRequest, output=public_dot_feed__pb2.GetFeedResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def delete_post(self, request: public_dot_feed__pb2.DeletePostRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeletePost', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.DeletePostRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def vote_thing(self, request: public_dot_feed__pb2.VoteThingRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_feed__pb2.VoteThingResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='VoteThing', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.VoteThingRequest, output=public_dot_feed__pb2.VoteThingResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def create_comment(self, request: public_dot_feed__pb2.CreateCommentRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_feed__pb2.CreateCommentResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateComment', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.CreateCommentRequest, output=public_dot_feed__pb2.CreateCommentResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_comments(self, request: public_dot_feed__pb2.GetCommentsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_feed__pb2.GetCommentsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetComments', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.GetCommentsRequest, output=public_dot_feed__pb2.GetCommentsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_profile_comments(self, request: public_dot_feed__pb2.GetProfileCommentsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_feed__pb2.GetProfileCommentsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetProfileComments', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.GetProfileCommentsRequest, output=public_dot_feed__pb2.GetProfileCommentsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def delete_comment(self, request: public_dot_feed__pb2.DeleteCommentRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteComment', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.DeleteCommentRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_leaderboard(self, request: public_dot_feed__pb2.GetLeaderboardRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_feed__pb2.GetLeaderboardResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetLeaderboard', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.GetLeaderboardRequest, output=public_dot_feed__pb2.GetLeaderboardResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_feed_stats(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_feed__pb2.GetFeedStatsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetFeedStats', service_name='textql.rpc.public.feed.FeedService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_feed__pb2.GetFeedStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def list_mentionable_users(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_feed__pb2.ListMentionableUsersResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListMentionableUsers', service_name='textql.rpc.public.feed.FeedService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_feed__pb2.ListMentionableUsersResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_default_slack_channel(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_feed__pb2.GetDefaultSlackChannelResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetDefaultSlackChannel', service_name='textql.rpc.public.feed.FeedService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_feed__pb2.GetDefaultSlackChannelResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def set_default_slack_channel(self, request: public_dot_feed__pb2.SetDefaultSlackChannelRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='SetDefaultSlackChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.SetDefaultSlackChannelRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_default_teams_channel(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_feed__pb2.GetDefaultTeamsChannelResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetDefaultTeamsChannel', service_name='textql.rpc.public.feed.FeedService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_feed__pb2.GetDefaultTeamsChannelResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def set_default_teams_channel(self, request: public_dot_feed__pb2.SetDefaultTeamsChannelRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='SetDefaultTeamsChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.SetDefaultTeamsChannelRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def stream_feed(self, request: public_dot_feed__pb2.StreamFeedRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> AsyncIterator[public_dot_feed__pb2.FeedEvent]:
        return self.execute_server_stream(request=request, method=MethodInfo(name='StreamFeed', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.StreamFeedRequest, output=public_dot_feed__pb2.FeedEvent, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def follow_agent(self, request: public_dot_feed__pb2.FollowAgentRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='FollowAgent', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.FollowAgentRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def unfollow_agent(self, request: public_dot_feed__pb2.UnfollowAgentRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='UnfollowAgent', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.UnfollowAgentRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_followed_agents(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_feed__pb2.ListFollowedAgentsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListFollowedAgents', service_name='textql.rpc.public.feed.FeedService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_feed__pb2.ListFollowedAgentsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def create_feed_channel(self, request: public_dot_feed__pb2.CreateFeedChannelRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_feed__pb2.CreateFeedChannelResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateFeedChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.CreateFeedChannelRequest, output=public_dot_feed__pb2.CreateFeedChannelResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_feed_channels(self, request: public_dot_feed__pb2.ListFeedChannelsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_feed__pb2.ListFeedChannelsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListFeedChannels', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.ListFeedChannelsRequest, output=public_dot_feed__pb2.ListFeedChannelsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_feed_channel(self, request: public_dot_feed__pb2.GetFeedChannelRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_feed__pb2.GetFeedChannelResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetFeedChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.GetFeedChannelRequest, output=public_dot_feed__pb2.GetFeedChannelResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def update_feed_channel(self, request: public_dot_feed__pb2.UpdateFeedChannelRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateFeedChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.UpdateFeedChannelRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def delete_feed_channel(self, request: public_dot_feed__pb2.DeleteFeedChannelRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteFeedChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.DeleteFeedChannelRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def join_feed_channel(self, request: public_dot_feed__pb2.JoinFeedChannelRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='JoinFeedChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.JoinFeedChannelRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def leave_feed_channel(self, request: public_dot_feed__pb2.LeaveFeedChannelRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='LeaveFeedChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.LeaveFeedChannelRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class FeedServiceSync(Protocol):

    def create_post(self, request: public_dot_feed__pb2.CreatePostRequest, ctx: RequestContext) -> public_dot_feed__pb2.CreatePostResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_post(self, request: public_dot_feed__pb2.GetPostRequest, ctx: RequestContext) -> public_dot_feed__pb2.GetPostResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_feed(self, request: public_dot_feed__pb2.GetFeedRequest, ctx: RequestContext) -> public_dot_feed__pb2.GetFeedResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_post(self, request: public_dot_feed__pb2.DeletePostRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def vote_thing(self, request: public_dot_feed__pb2.VoteThingRequest, ctx: RequestContext) -> public_dot_feed__pb2.VoteThingResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def create_comment(self, request: public_dot_feed__pb2.CreateCommentRequest, ctx: RequestContext) -> public_dot_feed__pb2.CreateCommentResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_comments(self, request: public_dot_feed__pb2.GetCommentsRequest, ctx: RequestContext) -> public_dot_feed__pb2.GetCommentsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_profile_comments(self, request: public_dot_feed__pb2.GetProfileCommentsRequest, ctx: RequestContext) -> public_dot_feed__pb2.GetProfileCommentsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_comment(self, request: public_dot_feed__pb2.DeleteCommentRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_leaderboard(self, request: public_dot_feed__pb2.GetLeaderboardRequest, ctx: RequestContext) -> public_dot_feed__pb2.GetLeaderboardResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_feed_stats(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_feed__pb2.GetFeedStatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_mentionable_users(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_feed__pb2.ListMentionableUsersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_default_slack_channel(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_feed__pb2.GetDefaultSlackChannelResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def set_default_slack_channel(self, request: public_dot_feed__pb2.SetDefaultSlackChannelRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_default_teams_channel(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_feed__pb2.GetDefaultTeamsChannelResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def set_default_teams_channel(self, request: public_dot_feed__pb2.SetDefaultTeamsChannelRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def stream_feed(self, request: public_dot_feed__pb2.StreamFeedRequest, ctx: RequestContext) -> Iterator[public_dot_feed__pb2.FeedEvent]:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def follow_agent(self, request: public_dot_feed__pb2.FollowAgentRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def unfollow_agent(self, request: public_dot_feed__pb2.UnfollowAgentRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_followed_agents(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_feed__pb2.ListFollowedAgentsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def create_feed_channel(self, request: public_dot_feed__pb2.CreateFeedChannelRequest, ctx: RequestContext) -> public_dot_feed__pb2.CreateFeedChannelResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_feed_channels(self, request: public_dot_feed__pb2.ListFeedChannelsRequest, ctx: RequestContext) -> public_dot_feed__pb2.ListFeedChannelsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_feed_channel(self, request: public_dot_feed__pb2.GetFeedChannelRequest, ctx: RequestContext) -> public_dot_feed__pb2.GetFeedChannelResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_feed_channel(self, request: public_dot_feed__pb2.UpdateFeedChannelRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_feed_channel(self, request: public_dot_feed__pb2.DeleteFeedChannelRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def join_feed_channel(self, request: public_dot_feed__pb2.JoinFeedChannelRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def leave_feed_channel(self, request: public_dot_feed__pb2.LeaveFeedChannelRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class FeedServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: FeedServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.feed.FeedService/CreatePost': EndpointSync.unary(method=MethodInfo(name='CreatePost', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.CreatePostRequest, output=public_dot_feed__pb2.CreatePostResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_post), '/textql.rpc.public.feed.FeedService/GetPost': EndpointSync.unary(method=MethodInfo(name='GetPost', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.GetPostRequest, output=public_dot_feed__pb2.GetPostResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_post), '/textql.rpc.public.feed.FeedService/GetFeed': EndpointSync.unary(method=MethodInfo(name='GetFeed', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.GetFeedRequest, output=public_dot_feed__pb2.GetFeedResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_feed), '/textql.rpc.public.feed.FeedService/DeletePost': EndpointSync.unary(method=MethodInfo(name='DeletePost', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.DeletePostRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_post), '/textql.rpc.public.feed.FeedService/VoteThing': EndpointSync.unary(method=MethodInfo(name='VoteThing', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.VoteThingRequest, output=public_dot_feed__pb2.VoteThingResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.vote_thing), '/textql.rpc.public.feed.FeedService/CreateComment': EndpointSync.unary(method=MethodInfo(name='CreateComment', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.CreateCommentRequest, output=public_dot_feed__pb2.CreateCommentResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_comment), '/textql.rpc.public.feed.FeedService/GetComments': EndpointSync.unary(method=MethodInfo(name='GetComments', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.GetCommentsRequest, output=public_dot_feed__pb2.GetCommentsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_comments), '/textql.rpc.public.feed.FeedService/GetProfileComments': EndpointSync.unary(method=MethodInfo(name='GetProfileComments', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.GetProfileCommentsRequest, output=public_dot_feed__pb2.GetProfileCommentsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_profile_comments), '/textql.rpc.public.feed.FeedService/DeleteComment': EndpointSync.unary(method=MethodInfo(name='DeleteComment', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.DeleteCommentRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_comment), '/textql.rpc.public.feed.FeedService/GetLeaderboard': EndpointSync.unary(method=MethodInfo(name='GetLeaderboard', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.GetLeaderboardRequest, output=public_dot_feed__pb2.GetLeaderboardResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_leaderboard), '/textql.rpc.public.feed.FeedService/GetFeedStats': EndpointSync.unary(method=MethodInfo(name='GetFeedStats', service_name='textql.rpc.public.feed.FeedService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_feed__pb2.GetFeedStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_feed_stats), '/textql.rpc.public.feed.FeedService/ListMentionableUsers': EndpointSync.unary(method=MethodInfo(name='ListMentionableUsers', service_name='textql.rpc.public.feed.FeedService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_feed__pb2.ListMentionableUsersResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_mentionable_users), '/textql.rpc.public.feed.FeedService/GetDefaultSlackChannel': EndpointSync.unary(method=MethodInfo(name='GetDefaultSlackChannel', service_name='textql.rpc.public.feed.FeedService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_feed__pb2.GetDefaultSlackChannelResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_default_slack_channel), '/textql.rpc.public.feed.FeedService/SetDefaultSlackChannel': EndpointSync.unary(method=MethodInfo(name='SetDefaultSlackChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.SetDefaultSlackChannelRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.set_default_slack_channel), '/textql.rpc.public.feed.FeedService/GetDefaultTeamsChannel': EndpointSync.unary(method=MethodInfo(name='GetDefaultTeamsChannel', service_name='textql.rpc.public.feed.FeedService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_feed__pb2.GetDefaultTeamsChannelResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_default_teams_channel), '/textql.rpc.public.feed.FeedService/SetDefaultTeamsChannel': EndpointSync.unary(method=MethodInfo(name='SetDefaultTeamsChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.SetDefaultTeamsChannelRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.set_default_teams_channel), '/textql.rpc.public.feed.FeedService/StreamFeed': EndpointSync.server_stream(method=MethodInfo(name='StreamFeed', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.StreamFeedRequest, output=public_dot_feed__pb2.FeedEvent, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.stream_feed), '/textql.rpc.public.feed.FeedService/FollowAgent': EndpointSync.unary(method=MethodInfo(name='FollowAgent', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.FollowAgentRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.follow_agent), '/textql.rpc.public.feed.FeedService/UnfollowAgent': EndpointSync.unary(method=MethodInfo(name='UnfollowAgent', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.UnfollowAgentRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.unfollow_agent), '/textql.rpc.public.feed.FeedService/ListFollowedAgents': EndpointSync.unary(method=MethodInfo(name='ListFollowedAgents', service_name='textql.rpc.public.feed.FeedService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_feed__pb2.ListFollowedAgentsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_followed_agents), '/textql.rpc.public.feed.FeedService/CreateFeedChannel': EndpointSync.unary(method=MethodInfo(name='CreateFeedChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.CreateFeedChannelRequest, output=public_dot_feed__pb2.CreateFeedChannelResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_feed_channel), '/textql.rpc.public.feed.FeedService/ListFeedChannels': EndpointSync.unary(method=MethodInfo(name='ListFeedChannels', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.ListFeedChannelsRequest, output=public_dot_feed__pb2.ListFeedChannelsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_feed_channels), '/textql.rpc.public.feed.FeedService/GetFeedChannel': EndpointSync.unary(method=MethodInfo(name='GetFeedChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.GetFeedChannelRequest, output=public_dot_feed__pb2.GetFeedChannelResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_feed_channel), '/textql.rpc.public.feed.FeedService/UpdateFeedChannel': EndpointSync.unary(method=MethodInfo(name='UpdateFeedChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.UpdateFeedChannelRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_feed_channel), '/textql.rpc.public.feed.FeedService/DeleteFeedChannel': EndpointSync.unary(method=MethodInfo(name='DeleteFeedChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.DeleteFeedChannelRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_feed_channel), '/textql.rpc.public.feed.FeedService/JoinFeedChannel': EndpointSync.unary(method=MethodInfo(name='JoinFeedChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.JoinFeedChannelRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.join_feed_channel), '/textql.rpc.public.feed.FeedService/LeaveFeedChannel': EndpointSync.unary(method=MethodInfo(name='LeaveFeedChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.LeaveFeedChannelRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.leave_feed_channel)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.feed.FeedService'

class FeedServiceClientSync(ConnectClientSync):

    def create_post(self, request: public_dot_feed__pb2.CreatePostRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_feed__pb2.CreatePostResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreatePost', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.CreatePostRequest, output=public_dot_feed__pb2.CreatePostResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_post(self, request: public_dot_feed__pb2.GetPostRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_feed__pb2.GetPostResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetPost', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.GetPostRequest, output=public_dot_feed__pb2.GetPostResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_feed(self, request: public_dot_feed__pb2.GetFeedRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_feed__pb2.GetFeedResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetFeed', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.GetFeedRequest, output=public_dot_feed__pb2.GetFeedResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def delete_post(self, request: public_dot_feed__pb2.DeletePostRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='DeletePost', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.DeletePostRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def vote_thing(self, request: public_dot_feed__pb2.VoteThingRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_feed__pb2.VoteThingResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='VoteThing', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.VoteThingRequest, output=public_dot_feed__pb2.VoteThingResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def create_comment(self, request: public_dot_feed__pb2.CreateCommentRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_feed__pb2.CreateCommentResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateComment', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.CreateCommentRequest, output=public_dot_feed__pb2.CreateCommentResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_comments(self, request: public_dot_feed__pb2.GetCommentsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_feed__pb2.GetCommentsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetComments', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.GetCommentsRequest, output=public_dot_feed__pb2.GetCommentsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_profile_comments(self, request: public_dot_feed__pb2.GetProfileCommentsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_feed__pb2.GetProfileCommentsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetProfileComments', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.GetProfileCommentsRequest, output=public_dot_feed__pb2.GetProfileCommentsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def delete_comment(self, request: public_dot_feed__pb2.DeleteCommentRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteComment', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.DeleteCommentRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_leaderboard(self, request: public_dot_feed__pb2.GetLeaderboardRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_feed__pb2.GetLeaderboardResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetLeaderboard', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.GetLeaderboardRequest, output=public_dot_feed__pb2.GetLeaderboardResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_feed_stats(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_feed__pb2.GetFeedStatsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetFeedStats', service_name='textql.rpc.public.feed.FeedService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_feed__pb2.GetFeedStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def list_mentionable_users(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_feed__pb2.ListMentionableUsersResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListMentionableUsers', service_name='textql.rpc.public.feed.FeedService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_feed__pb2.ListMentionableUsersResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_default_slack_channel(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_feed__pb2.GetDefaultSlackChannelResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetDefaultSlackChannel', service_name='textql.rpc.public.feed.FeedService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_feed__pb2.GetDefaultSlackChannelResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def set_default_slack_channel(self, request: public_dot_feed__pb2.SetDefaultSlackChannelRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='SetDefaultSlackChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.SetDefaultSlackChannelRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_default_teams_channel(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_feed__pb2.GetDefaultTeamsChannelResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetDefaultTeamsChannel', service_name='textql.rpc.public.feed.FeedService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_feed__pb2.GetDefaultTeamsChannelResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def set_default_teams_channel(self, request: public_dot_feed__pb2.SetDefaultTeamsChannelRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='SetDefaultTeamsChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.SetDefaultTeamsChannelRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def stream_feed(self, request: public_dot_feed__pb2.StreamFeedRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> Iterator[public_dot_feed__pb2.FeedEvent]:
        return self.execute_server_stream(request=request, method=MethodInfo(name='StreamFeed', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.StreamFeedRequest, output=public_dot_feed__pb2.FeedEvent, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def follow_agent(self, request: public_dot_feed__pb2.FollowAgentRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='FollowAgent', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.FollowAgentRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def unfollow_agent(self, request: public_dot_feed__pb2.UnfollowAgentRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='UnfollowAgent', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.UnfollowAgentRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_followed_agents(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_feed__pb2.ListFollowedAgentsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListFollowedAgents', service_name='textql.rpc.public.feed.FeedService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_feed__pb2.ListFollowedAgentsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def create_feed_channel(self, request: public_dot_feed__pb2.CreateFeedChannelRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_feed__pb2.CreateFeedChannelResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateFeedChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.CreateFeedChannelRequest, output=public_dot_feed__pb2.CreateFeedChannelResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_feed_channels(self, request: public_dot_feed__pb2.ListFeedChannelsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_feed__pb2.ListFeedChannelsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListFeedChannels', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.ListFeedChannelsRequest, output=public_dot_feed__pb2.ListFeedChannelsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_feed_channel(self, request: public_dot_feed__pb2.GetFeedChannelRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_feed__pb2.GetFeedChannelResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetFeedChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.GetFeedChannelRequest, output=public_dot_feed__pb2.GetFeedChannelResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def update_feed_channel(self, request: public_dot_feed__pb2.UpdateFeedChannelRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateFeedChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.UpdateFeedChannelRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def delete_feed_channel(self, request: public_dot_feed__pb2.DeleteFeedChannelRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteFeedChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.DeleteFeedChannelRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def join_feed_channel(self, request: public_dot_feed__pb2.JoinFeedChannelRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='JoinFeedChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.JoinFeedChannelRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def leave_feed_channel(self, request: public_dot_feed__pb2.LeaveFeedChannelRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='LeaveFeedChannel', service_name='textql.rpc.public.feed.FeedService', input=public_dot_feed__pb2.LeaveFeedChannelRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)