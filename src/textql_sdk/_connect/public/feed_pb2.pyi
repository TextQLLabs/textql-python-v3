# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
# pylint: skip-file
# mypy: ignore-errors
import datetime
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ..public import options_pb2 as _options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FeedFilter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FEED_FILTER_HOT: _ClassVar[FeedFilter]
    FEED_FILTER_NEW: _ClassVar[FeedFilter]
    FEED_FILTER_TOP: _ClassVar[FeedFilter]
    FEED_FILTER_MINE: _ClassVar[FeedFilter]
    FEED_FILTER_FOLLOWING: _ClassVar[FeedFilter]

class FeedSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FEED_SOURCE_UNSPECIFIED: _ClassVar[FeedSource]
    FEED_SOURCE_PEOPLE: _ClassVar[FeedSource]
    FEED_SOURCE_AGENTS: _ClassVar[FeedSource]
    FEED_SOURCE_SYSTEM: _ClassVar[FeedSource]

class FeedTimeRange(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FEED_TIME_RANGE_UNSPECIFIED: _ClassVar[FeedTimeRange]
    FEED_TIME_RANGE_DAY: _ClassVar[FeedTimeRange]
    FEED_TIME_RANGE_WEEK: _ClassVar[FeedTimeRange]
    FEED_TIME_RANGE_MONTH: _ClassVar[FeedTimeRange]
    FEED_TIME_RANGE_QUARTER: _ClassVar[FeedTimeRange]
    FEED_TIME_RANGE_YEAR: _ClassVar[FeedTimeRange]

class VoteType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VOTE_TYPE_NONE: _ClassVar[VoteType]
    VOTE_TYPE_UPVOTE: _ClassVar[VoteType]
    VOTE_TYPE_DOWNVOTE: _ClassVar[VoteType]

class PostType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    POST_TYPE_TEXT: _ClassVar[PostType]
    POST_TYPE_DASHBOARD: _ClassVar[PostType]
    POST_TYPE_REPORT: _ClassVar[PostType]
    POST_TYPE_CHAT: _ClassVar[PostType]

class CommentSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMMENT_SORT_UNSPECIFIED: _ClassVar[CommentSort]
    COMMENT_SORT_CHRONOLOGICAL: _ClassVar[CommentSort]
    COMMENT_SORT_LATEST: _ClassVar[CommentSort]
    COMMENT_SORT_TOP: _ClassVar[CommentSort]

class FeedEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FEED_EVENT_TYPE_UNSPECIFIED: _ClassVar[FeedEventType]
    FEED_EVENT_TYPE_NEW_POST: _ClassVar[FeedEventType]
    FEED_EVENT_TYPE_POST_DELETED: _ClassVar[FeedEventType]
    FEED_EVENT_TYPE_VOTE_UPDATED: _ClassVar[FeedEventType]
    FEED_EVENT_TYPE_NEW_COMMENT: _ClassVar[FeedEventType]
    FEED_EVENT_TYPE_COMMENT_DELETED: _ClassVar[FeedEventType]
FEED_FILTER_HOT: FeedFilter
FEED_FILTER_NEW: FeedFilter
FEED_FILTER_TOP: FeedFilter
FEED_FILTER_MINE: FeedFilter
FEED_FILTER_FOLLOWING: FeedFilter
FEED_SOURCE_UNSPECIFIED: FeedSource
FEED_SOURCE_PEOPLE: FeedSource
FEED_SOURCE_AGENTS: FeedSource
FEED_SOURCE_SYSTEM: FeedSource
FEED_TIME_RANGE_UNSPECIFIED: FeedTimeRange
FEED_TIME_RANGE_DAY: FeedTimeRange
FEED_TIME_RANGE_WEEK: FeedTimeRange
FEED_TIME_RANGE_MONTH: FeedTimeRange
FEED_TIME_RANGE_QUARTER: FeedTimeRange
FEED_TIME_RANGE_YEAR: FeedTimeRange
VOTE_TYPE_NONE: VoteType
VOTE_TYPE_UPVOTE: VoteType
VOTE_TYPE_DOWNVOTE: VoteType
POST_TYPE_TEXT: PostType
POST_TYPE_DASHBOARD: PostType
POST_TYPE_REPORT: PostType
POST_TYPE_CHAT: PostType
COMMENT_SORT_UNSPECIFIED: CommentSort
COMMENT_SORT_CHRONOLOGICAL: CommentSort
COMMENT_SORT_LATEST: CommentSort
COMMENT_SORT_TOP: CommentSort
FEED_EVENT_TYPE_UNSPECIFIED: FeedEventType
FEED_EVENT_TYPE_NEW_POST: FeedEventType
FEED_EVENT_TYPE_POST_DELETED: FeedEventType
FEED_EVENT_TYPE_VOTE_UPDATED: FeedEventType
FEED_EVENT_TYPE_NEW_COMMENT: FeedEventType
FEED_EVENT_TYPE_COMMENT_DELETED: FeedEventType

class Post(_message.Message):
    __slots__ = ('id', 'title', 'content', 'post_type', 'creator_member_id', 'creator_agent_id', 'upvote_count', 'downvote_count', 'comment_count', 'my_vote', 'created_at', 'creator_member_name', 'creator_agent_name', 'chat_id', 'image_urls', 'dashboard_ids', 'report_ids', 'chat_ids', 'tagged_member_ids', 'tagged_agent_ids', 'is_demo', 'channel_ids', 'creator_agent_profile_image_url', 'creator_member_profile_image_url')
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    POST_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATOR_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATOR_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    UPVOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    DOWNVOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    MY_VOTE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATOR_MEMBER_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATOR_AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URLS_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_IDS_FIELD_NUMBER: _ClassVar[int]
    REPORT_IDS_FIELD_NUMBER: _ClassVar[int]
    CHAT_IDS_FIELD_NUMBER: _ClassVar[int]
    TAGGED_MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    TAGGED_AGENT_IDS_FIELD_NUMBER: _ClassVar[int]
    IS_DEMO_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
    CREATOR_AGENT_PROFILE_IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    CREATOR_MEMBER_PROFILE_IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    content: str
    post_type: PostType
    creator_member_id: str
    creator_agent_id: str
    upvote_count: int
    downvote_count: int
    comment_count: int
    my_vote: VoteType
    created_at: _timestamp_pb2.Timestamp
    creator_member_name: str
    creator_agent_name: str
    chat_id: str
    image_urls: _containers.RepeatedScalarFieldContainer[str]
    dashboard_ids: _containers.RepeatedScalarFieldContainer[str]
    report_ids: _containers.RepeatedScalarFieldContainer[str]
    chat_ids: _containers.RepeatedScalarFieldContainer[str]
    tagged_member_ids: _containers.RepeatedScalarFieldContainer[str]
    tagged_agent_ids: _containers.RepeatedScalarFieldContainer[str]
    is_demo: bool
    channel_ids: _containers.RepeatedScalarFieldContainer[str]
    creator_agent_profile_image_url: str
    creator_member_profile_image_url: str

    def __init__(self, id: _Optional[str]=..., title: _Optional[str]=..., content: _Optional[str]=..., post_type: _Optional[_Union[PostType, str]]=..., creator_member_id: _Optional[str]=..., creator_agent_id: _Optional[str]=..., upvote_count: _Optional[int]=..., downvote_count: _Optional[int]=..., comment_count: _Optional[int]=..., my_vote: _Optional[_Union[VoteType, str]]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., creator_member_name: _Optional[str]=..., creator_agent_name: _Optional[str]=..., chat_id: _Optional[str]=..., image_urls: _Optional[_Iterable[str]]=..., dashboard_ids: _Optional[_Iterable[str]]=..., report_ids: _Optional[_Iterable[str]]=..., chat_ids: _Optional[_Iterable[str]]=..., tagged_member_ids: _Optional[_Iterable[str]]=..., tagged_agent_ids: _Optional[_Iterable[str]]=..., is_demo: bool=..., channel_ids: _Optional[_Iterable[str]]=..., creator_agent_profile_image_url: _Optional[str]=..., creator_member_profile_image_url: _Optional[str]=...) -> None:
        ...

class Comment(_message.Message):
    __slots__ = ('id', 'content', 'post_id', 'parent_id', 'depth', 'creator_member_id', 'creator_agent_id', 'upvote_count', 'downvote_count', 'my_vote', 'created_at', 'replies', 'creator_member_name', 'creator_agent_name', 'creator_agent_profile_image_url', 'creator_member_profile_image_url')
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    CREATOR_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATOR_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    UPVOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    DOWNVOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MY_VOTE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    REPLIES_FIELD_NUMBER: _ClassVar[int]
    CREATOR_MEMBER_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATOR_AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATOR_AGENT_PROFILE_IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    CREATOR_MEMBER_PROFILE_IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    content: str
    post_id: str
    parent_id: str
    depth: int
    creator_member_id: str
    creator_agent_id: str
    upvote_count: int
    downvote_count: int
    my_vote: VoteType
    created_at: _timestamp_pb2.Timestamp
    replies: _containers.RepeatedCompositeFieldContainer[Comment]
    creator_member_name: str
    creator_agent_name: str
    creator_agent_profile_image_url: str
    creator_member_profile_image_url: str

    def __init__(self, id: _Optional[str]=..., content: _Optional[str]=..., post_id: _Optional[str]=..., parent_id: _Optional[str]=..., depth: _Optional[int]=..., creator_member_id: _Optional[str]=..., creator_agent_id: _Optional[str]=..., upvote_count: _Optional[int]=..., downvote_count: _Optional[int]=..., my_vote: _Optional[_Union[VoteType, str]]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., replies: _Optional[_Iterable[_Union[Comment, _Mapping]]]=..., creator_member_name: _Optional[str]=..., creator_agent_name: _Optional[str]=..., creator_agent_profile_image_url: _Optional[str]=..., creator_member_profile_image_url: _Optional[str]=...) -> None:
        ...

class LeaderboardEntry(_message.Message):
    __slots__ = ('member_id', 'agent_id', 'post_count', 'comment_count', 'received_upvotes', 'received_downvotes', 'net_score', 'member_name', 'agent_name', 'agent_chat_id')
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    POST_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_UPVOTES_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_DOWNVOTES_FIELD_NUMBER: _ClassVar[int]
    NET_SCORE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_NAME_FIELD_NUMBER: _ClassVar[int]
    AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    AGENT_CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    agent_id: str
    post_count: int
    comment_count: int
    received_upvotes: int
    received_downvotes: int
    net_score: int
    member_name: str
    agent_name: str
    agent_chat_id: str

    def __init__(self, member_id: _Optional[str]=..., agent_id: _Optional[str]=..., post_count: _Optional[int]=..., comment_count: _Optional[int]=..., received_upvotes: _Optional[int]=..., received_downvotes: _Optional[int]=..., net_score: _Optional[int]=..., member_name: _Optional[str]=..., agent_name: _Optional[str]=..., agent_chat_id: _Optional[str]=...) -> None:
        ...

class CreatePostRequest(_message.Message):
    __slots__ = ('title', 'content', 'post_type', 'image_urls', 'dashboard_ids', 'report_ids', 'chat_ids', 'mentioned_member_ids', 'mentioned_agent_ids', 'channel_ids')
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    POST_TYPE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URLS_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_IDS_FIELD_NUMBER: _ClassVar[int]
    REPORT_IDS_FIELD_NUMBER: _ClassVar[int]
    CHAT_IDS_FIELD_NUMBER: _ClassVar[int]
    MENTIONED_MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    MENTIONED_AGENT_IDS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
    title: str
    content: str
    post_type: PostType
    image_urls: _containers.RepeatedScalarFieldContainer[str]
    dashboard_ids: _containers.RepeatedScalarFieldContainer[str]
    report_ids: _containers.RepeatedScalarFieldContainer[str]
    chat_ids: _containers.RepeatedScalarFieldContainer[str]
    mentioned_member_ids: _containers.RepeatedScalarFieldContainer[str]
    mentioned_agent_ids: _containers.RepeatedScalarFieldContainer[str]
    channel_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, title: _Optional[str]=..., content: _Optional[str]=..., post_type: _Optional[_Union[PostType, str]]=..., image_urls: _Optional[_Iterable[str]]=..., dashboard_ids: _Optional[_Iterable[str]]=..., report_ids: _Optional[_Iterable[str]]=..., chat_ids: _Optional[_Iterable[str]]=..., mentioned_member_ids: _Optional[_Iterable[str]]=..., mentioned_agent_ids: _Optional[_Iterable[str]]=..., channel_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreatePostResponse(_message.Message):
    __slots__ = ('post',)
    POST_FIELD_NUMBER: _ClassVar[int]
    post: Post

    def __init__(self, post: _Optional[_Union[Post, _Mapping]]=...) -> None:
        ...

class GetPostRequest(_message.Message):
    __slots__ = ('post_id',)
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str

    def __init__(self, post_id: _Optional[str]=...) -> None:
        ...

class GetPostResponse(_message.Message):
    __slots__ = ('post',)
    POST_FIELD_NUMBER: _ClassVar[int]
    post: Post

    def __init__(self, post: _Optional[_Union[Post, _Mapping]]=...) -> None:
        ...

class GetFeedRequest(_message.Message):
    __slots__ = ('filter', 'limit', 'offset', 'author_member_id', 'author_agent_id', 'channel_id', 'author_agent_ids', 'channel_ids', 'sources', 'time_range', 'created_after')
    FILTER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_AGENT_IDS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AFTER_FIELD_NUMBER: _ClassVar[int]
    filter: FeedFilter
    limit: int
    offset: int
    author_member_id: str
    author_agent_id: str
    channel_id: str
    author_agent_ids: _containers.RepeatedScalarFieldContainer[str]
    channel_ids: _containers.RepeatedScalarFieldContainer[str]
    sources: _containers.RepeatedScalarFieldContainer[FeedSource]
    time_range: FeedTimeRange
    created_after: _timestamp_pb2.Timestamp

    def __init__(self, filter: _Optional[_Union[FeedFilter, str]]=..., limit: _Optional[int]=..., offset: _Optional[int]=..., author_member_id: _Optional[str]=..., author_agent_id: _Optional[str]=..., channel_id: _Optional[str]=..., author_agent_ids: _Optional[_Iterable[str]]=..., channel_ids: _Optional[_Iterable[str]]=..., sources: _Optional[_Iterable[_Union[FeedSource, str]]]=..., time_range: _Optional[_Union[FeedTimeRange, str]]=..., created_after: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GetFeedStatsResponse(_message.Message):
    __slots__ = ('posts_today', 'messages_today', 'messages_all_time', 'active_agents', 'dashboards_created', 'threads_created', 'playbooks_created', 'connectors_configured', 'connector_names', 'active_agent_names')
    POSTS_TODAY_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_TODAY_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_ALL_TIME_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_AGENTS_FIELD_NUMBER: _ClassVar[int]
    DASHBOARDS_CREATED_FIELD_NUMBER: _ClassVar[int]
    THREADS_CREATED_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOKS_CREATED_FIELD_NUMBER: _ClassVar[int]
    CONNECTORS_CONFIGURED_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_NAMES_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_AGENT_NAMES_FIELD_NUMBER: _ClassVar[int]
    posts_today: int
    messages_today: int
    messages_all_time: int
    active_agents: int
    dashboards_created: int
    threads_created: int
    playbooks_created: int
    connectors_configured: int
    connector_names: _containers.RepeatedScalarFieldContainer[str]
    active_agent_names: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, posts_today: _Optional[int]=..., messages_today: _Optional[int]=..., messages_all_time: _Optional[int]=..., active_agents: _Optional[int]=..., dashboards_created: _Optional[int]=..., threads_created: _Optional[int]=..., playbooks_created: _Optional[int]=..., connectors_configured: _Optional[int]=..., connector_names: _Optional[_Iterable[str]]=..., active_agent_names: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetFeedResponse(_message.Message):
    __slots__ = ('posts',)
    POSTS_FIELD_NUMBER: _ClassVar[int]
    posts: _containers.RepeatedCompositeFieldContainer[Post]

    def __init__(self, posts: _Optional[_Iterable[_Union[Post, _Mapping]]]=...) -> None:
        ...

class DeletePostRequest(_message.Message):
    __slots__ = ('post_id',)
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str

    def __init__(self, post_id: _Optional[str]=...) -> None:
        ...

class VoteThingRequest(_message.Message):
    __slots__ = ('thing_id', 'vote_type')
    THING_ID_FIELD_NUMBER: _ClassVar[int]
    VOTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    thing_id: str
    vote_type: VoteType

    def __init__(self, thing_id: _Optional[str]=..., vote_type: _Optional[_Union[VoteType, str]]=...) -> None:
        ...

class VoteThingResponse(_message.Message):
    __slots__ = ('upvote_count', 'downvote_count')
    UPVOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    DOWNVOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    upvote_count: int
    downvote_count: int

    def __init__(self, upvote_count: _Optional[int]=..., downvote_count: _Optional[int]=...) -> None:
        ...

class CreateCommentRequest(_message.Message):
    __slots__ = ('post_id', 'content', 'parent_id', 'mentioned_member_ids', 'mentioned_agent_ids')
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    MENTIONED_MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    MENTIONED_AGENT_IDS_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    content: str
    parent_id: str
    mentioned_member_ids: _containers.RepeatedScalarFieldContainer[str]
    mentioned_agent_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, post_id: _Optional[str]=..., content: _Optional[str]=..., parent_id: _Optional[str]=..., mentioned_member_ids: _Optional[_Iterable[str]]=..., mentioned_agent_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateCommentResponse(_message.Message):
    __slots__ = ('comment',)
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    comment: Comment

    def __init__(self, comment: _Optional[_Union[Comment, _Mapping]]=...) -> None:
        ...

class GetCommentsRequest(_message.Message):
    __slots__ = ('post_id', 'sort_by')
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    sort_by: CommentSort

    def __init__(self, post_id: _Optional[str]=..., sort_by: _Optional[_Union[CommentSort, str]]=...) -> None:
        ...

class GetCommentsResponse(_message.Message):
    __slots__ = ('comments',)
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    comments: _containers.RepeatedCompositeFieldContainer[Comment]

    def __init__(self, comments: _Optional[_Iterable[_Union[Comment, _Mapping]]]=...) -> None:
        ...

class ProfileComment(_message.Message):
    __slots__ = ('comment', 'post')
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    POST_FIELD_NUMBER: _ClassVar[int]
    comment: Comment
    post: Post

    def __init__(self, comment: _Optional[_Union[Comment, _Mapping]]=..., post: _Optional[_Union[Post, _Mapping]]=...) -> None:
        ...

class GetProfileCommentsRequest(_message.Message):
    __slots__ = ('author_member_id', 'author_agent_id', 'limit', 'offset')
    AUTHOR_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    author_member_id: str
    author_agent_id: str
    limit: int
    offset: int

    def __init__(self, author_member_id: _Optional[str]=..., author_agent_id: _Optional[str]=..., limit: _Optional[int]=..., offset: _Optional[int]=...) -> None:
        ...

class GetProfileCommentsResponse(_message.Message):
    __slots__ = ('comments',)
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    comments: _containers.RepeatedCompositeFieldContainer[ProfileComment]

    def __init__(self, comments: _Optional[_Iterable[_Union[ProfileComment, _Mapping]]]=...) -> None:
        ...

class DeleteCommentRequest(_message.Message):
    __slots__ = ('comment_id',)
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    comment_id: str

    def __init__(self, comment_id: _Optional[str]=...) -> None:
        ...

class GetLeaderboardRequest(_message.Message):
    __slots__ = ('timeframe', 'limit')
    TIMEFRAME_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    timeframe: str
    limit: int

    def __init__(self, timeframe: _Optional[str]=..., limit: _Optional[int]=...) -> None:
        ...

class GetLeaderboardResponse(_message.Message):
    __slots__ = ('entries',)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[LeaderboardEntry]

    def __init__(self, entries: _Optional[_Iterable[_Union[LeaderboardEntry, _Mapping]]]=...) -> None:
        ...

class StreamFeedRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class FeedEvent(_message.Message):
    __slots__ = ('event_type', 'post', 'comment', 'channel_ids')
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    POST_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
    event_type: FeedEventType
    post: Post
    comment: Comment
    channel_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, event_type: _Optional[_Union[FeedEventType, str]]=..., post: _Optional[_Union[Post, _Mapping]]=..., comment: _Optional[_Union[Comment, _Mapping]]=..., channel_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class MentionableUser(_message.Message):
    __slots__ = ('id', 'display_name', 'avatar_url', 'is_agent')
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_URL_FIELD_NUMBER: _ClassVar[int]
    IS_AGENT_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str
    avatar_url: str
    is_agent: bool

    def __init__(self, id: _Optional[str]=..., display_name: _Optional[str]=..., avatar_url: _Optional[str]=..., is_agent: bool=...) -> None:
        ...

class ListMentionableUsersResponse(_message.Message):
    __slots__ = ('users',)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[MentionableUser]

    def __init__(self, users: _Optional[_Iterable[_Union[MentionableUser, _Mapping]]]=...) -> None:
        ...

class FollowAgentRequest(_message.Message):
    __slots__ = ('agent_id',)
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str

    def __init__(self, agent_id: _Optional[str]=...) -> None:
        ...

class UnfollowAgentRequest(_message.Message):
    __slots__ = ('agent_id',)
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str

    def __init__(self, agent_id: _Optional[str]=...) -> None:
        ...

class ListFollowedAgentsResponse(_message.Message):
    __slots__ = ('agent_ids',)
    AGENT_IDS_FIELD_NUMBER: _ClassVar[int]
    agent_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, agent_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetDefaultSlackChannelResponse(_message.Message):
    __slots__ = ('slack_channel_id',)
    SLACK_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    slack_channel_id: str

    def __init__(self, slack_channel_id: _Optional[str]=...) -> None:
        ...

class SetDefaultSlackChannelRequest(_message.Message):
    __slots__ = ('slack_channel_id',)
    SLACK_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    slack_channel_id: str

    def __init__(self, slack_channel_id: _Optional[str]=...) -> None:
        ...

class GetDefaultTeamsChannelResponse(_message.Message):
    __slots__ = ('teams_channel_id',)
    TEAMS_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    teams_channel_id: str

    def __init__(self, teams_channel_id: _Optional[str]=...) -> None:
        ...

class SetDefaultTeamsChannelRequest(_message.Message):
    __slots__ = ('teams_channel_id',)
    TEAMS_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    teams_channel_id: str

    def __init__(self, teams_channel_id: _Optional[str]=...) -> None:
        ...

class FeedChannel(_message.Message):
    __slots__ = ('id', 'name', 'description', 'creator_id', 'created_at', 'updated_at', 'is_public', 'is_member', 'is_default')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATOR_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    IS_MEMBER_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    creator_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    is_public: bool
    is_member: bool
    is_default: bool

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., description: _Optional[str]=..., creator_id: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., is_public: bool=..., is_member: bool=..., is_default: bool=...) -> None:
        ...

class CreateFeedChannelRequest(_message.Message):
    __slots__ = ('name', 'description', 'is_public')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    is_public: bool

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., is_public: bool=...) -> None:
        ...

class CreateFeedChannelResponse(_message.Message):
    __slots__ = ('channel',)
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    channel: FeedChannel

    def __init__(self, channel: _Optional[_Union[FeedChannel, _Mapping]]=...) -> None:
        ...

class ListFeedChannelsRequest(_message.Message):
    __slots__ = ('include_unjoined',)
    INCLUDE_UNJOINED_FIELD_NUMBER: _ClassVar[int]
    include_unjoined: bool

    def __init__(self, include_unjoined: bool=...) -> None:
        ...

class ListFeedChannelsResponse(_message.Message):
    __slots__ = ('channels',)
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    channels: _containers.RepeatedCompositeFieldContainer[FeedChannel]

    def __init__(self, channels: _Optional[_Iterable[_Union[FeedChannel, _Mapping]]]=...) -> None:
        ...

class GetFeedChannelRequest(_message.Message):
    __slots__ = ('channel_id',)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str

    def __init__(self, channel_id: _Optional[str]=...) -> None:
        ...

class GetFeedChannelResponse(_message.Message):
    __slots__ = ('channel',)
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    channel: FeedChannel

    def __init__(self, channel: _Optional[_Union[FeedChannel, _Mapping]]=...) -> None:
        ...

class UpdateFeedChannelRequest(_message.Message):
    __slots__ = ('channel_id', 'name', 'description', 'is_public')
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    name: str
    description: str
    is_public: bool

    def __init__(self, channel_id: _Optional[str]=..., name: _Optional[str]=..., description: _Optional[str]=..., is_public: bool=...) -> None:
        ...

class DeleteFeedChannelRequest(_message.Message):
    __slots__ = ('channel_id',)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str

    def __init__(self, channel_id: _Optional[str]=...) -> None:
        ...

class JoinFeedChannelRequest(_message.Message):
    __slots__ = ('channel_id',)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str

    def __init__(self, channel_id: _Optional[str]=...) -> None:
        ...

class LeaveFeedChannelRequest(_message.Message):
    __slots__ = ('channel_id',)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str

    def __init__(self, channel_id: _Optional[str]=...) -> None:
        ...