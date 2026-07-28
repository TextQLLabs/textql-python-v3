# pylint: skip-file
# mypy: ignore-errors
import datetime
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ..public import options_pb2 as _options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Promotion(_message.Message):
    __slots__ = ('id', 'name', 'description', 'event_category', 'amount_cents', 'max_grants_per_org', 'max_grants_per_member', 'target_org_ids', 'target_user_groups', 'is_active', 'starts_at', 'ends_at', 'grant_memo', 'grants_count', 'email_events', 'max_grants_total', 'target_plan_types', 'credit_expires_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EVENT_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_CENTS_FIELD_NUMBER: _ClassVar[int]
    MAX_GRANTS_PER_ORG_FIELD_NUMBER: _ClassVar[int]
    MAX_GRANTS_PER_MEMBER_FIELD_NUMBER: _ClassVar[int]
    TARGET_ORG_IDS_FIELD_NUMBER: _ClassVar[int]
    TARGET_USER_GROUPS_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    STARTS_AT_FIELD_NUMBER: _ClassVar[int]
    ENDS_AT_FIELD_NUMBER: _ClassVar[int]
    GRANT_MEMO_FIELD_NUMBER: _ClassVar[int]
    GRANTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_EVENTS_FIELD_NUMBER: _ClassVar[int]
    MAX_GRANTS_TOTAL_FIELD_NUMBER: _ClassVar[int]
    TARGET_PLAN_TYPES_FIELD_NUMBER: _ClassVar[int]
    CREDIT_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    event_category: str
    amount_cents: int
    max_grants_per_org: int
    max_grants_per_member: int
    target_org_ids: _containers.RepeatedScalarFieldContainer[str]
    target_user_groups: _containers.RepeatedScalarFieldContainer[str]
    is_active: bool
    starts_at: _timestamp_pb2.Timestamp
    ends_at: _timestamp_pb2.Timestamp
    grant_memo: str
    grants_count: int
    email_events: _containers.RepeatedScalarFieldContainer[str]
    max_grants_total: int
    target_plan_types: _containers.RepeatedScalarFieldContainer[str]
    credit_expires_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., description: _Optional[str]=..., event_category: _Optional[str]=..., amount_cents: _Optional[int]=..., max_grants_per_org: _Optional[int]=..., max_grants_per_member: _Optional[int]=..., target_org_ids: _Optional[_Iterable[str]]=..., target_user_groups: _Optional[_Iterable[str]]=..., is_active: bool=..., starts_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., ends_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., grant_memo: _Optional[str]=..., grants_count: _Optional[int]=..., email_events: _Optional[_Iterable[str]]=..., max_grants_total: _Optional[int]=..., target_plan_types: _Optional[_Iterable[str]]=..., credit_expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class PromotionGrant(_message.Message):
    __slots__ = ('id', 'promotion_id', 'org_id', 'member_id', 'event_id', 'idempotency_token', 'status', 'member_email', 'org_name', 'created_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    ORG_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    promotion_id: str
    org_id: str
    member_id: str
    event_id: str
    idempotency_token: str
    status: str
    member_email: str
    org_name: str
    created_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., promotion_id: _Optional[str]=..., org_id: _Optional[str]=..., member_id: _Optional[str]=..., event_id: _Optional[str]=..., idempotency_token: _Optional[str]=..., status: _Optional[str]=..., member_email: _Optional[str]=..., org_name: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListPromotionsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListPromotionsResponse(_message.Message):
    __slots__ = ('promotions',)
    PROMOTIONS_FIELD_NUMBER: _ClassVar[int]
    promotions: _containers.RepeatedCompositeFieldContainer[Promotion]

    def __init__(self, promotions: _Optional[_Iterable[_Union[Promotion, _Mapping]]]=...) -> None:
        ...

class CreatePromotionRequest(_message.Message):
    __slots__ = ('name', 'description', 'event_category', 'amount_cents', 'max_grants_per_org', 'max_grants_per_member', 'target_org_ids', 'target_user_groups', 'is_active', 'starts_at', 'ends_at', 'grant_memo', 'email_events', 'max_grants_total', 'target_plan_types', 'credit_expires_at')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EVENT_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_CENTS_FIELD_NUMBER: _ClassVar[int]
    MAX_GRANTS_PER_ORG_FIELD_NUMBER: _ClassVar[int]
    MAX_GRANTS_PER_MEMBER_FIELD_NUMBER: _ClassVar[int]
    TARGET_ORG_IDS_FIELD_NUMBER: _ClassVar[int]
    TARGET_USER_GROUPS_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    STARTS_AT_FIELD_NUMBER: _ClassVar[int]
    ENDS_AT_FIELD_NUMBER: _ClassVar[int]
    GRANT_MEMO_FIELD_NUMBER: _ClassVar[int]
    EMAIL_EVENTS_FIELD_NUMBER: _ClassVar[int]
    MAX_GRANTS_TOTAL_FIELD_NUMBER: _ClassVar[int]
    TARGET_PLAN_TYPES_FIELD_NUMBER: _ClassVar[int]
    CREDIT_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    event_category: str
    amount_cents: int
    max_grants_per_org: int
    max_grants_per_member: int
    target_org_ids: _containers.RepeatedScalarFieldContainer[str]
    target_user_groups: _containers.RepeatedScalarFieldContainer[str]
    is_active: bool
    starts_at: _timestamp_pb2.Timestamp
    ends_at: _timestamp_pb2.Timestamp
    grant_memo: str
    email_events: _containers.RepeatedScalarFieldContainer[str]
    max_grants_total: int
    target_plan_types: _containers.RepeatedScalarFieldContainer[str]
    credit_expires_at: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., event_category: _Optional[str]=..., amount_cents: _Optional[int]=..., max_grants_per_org: _Optional[int]=..., max_grants_per_member: _Optional[int]=..., target_org_ids: _Optional[_Iterable[str]]=..., target_user_groups: _Optional[_Iterable[str]]=..., is_active: bool=..., starts_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., ends_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., grant_memo: _Optional[str]=..., email_events: _Optional[_Iterable[str]]=..., max_grants_total: _Optional[int]=..., target_plan_types: _Optional[_Iterable[str]]=..., credit_expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CreatePromotionResponse(_message.Message):
    __slots__ = ('promotion',)
    PROMOTION_FIELD_NUMBER: _ClassVar[int]
    promotion: Promotion

    def __init__(self, promotion: _Optional[_Union[Promotion, _Mapping]]=...) -> None:
        ...

class UpdatePromotionRequest(_message.Message):
    __slots__ = ('id', 'name', 'description', 'event_category', 'amount_cents', 'max_grants_per_org', 'max_grants_per_member', 'target_org_ids', 'target_user_groups', 'is_active', 'starts_at', 'ends_at', 'grant_memo', 'email_events', 'max_grants_total', 'target_plan_types', 'credit_expires_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EVENT_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_CENTS_FIELD_NUMBER: _ClassVar[int]
    MAX_GRANTS_PER_ORG_FIELD_NUMBER: _ClassVar[int]
    MAX_GRANTS_PER_MEMBER_FIELD_NUMBER: _ClassVar[int]
    TARGET_ORG_IDS_FIELD_NUMBER: _ClassVar[int]
    TARGET_USER_GROUPS_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    STARTS_AT_FIELD_NUMBER: _ClassVar[int]
    ENDS_AT_FIELD_NUMBER: _ClassVar[int]
    GRANT_MEMO_FIELD_NUMBER: _ClassVar[int]
    EMAIL_EVENTS_FIELD_NUMBER: _ClassVar[int]
    MAX_GRANTS_TOTAL_FIELD_NUMBER: _ClassVar[int]
    TARGET_PLAN_TYPES_FIELD_NUMBER: _ClassVar[int]
    CREDIT_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    event_category: str
    amount_cents: int
    max_grants_per_org: int
    max_grants_per_member: int
    target_org_ids: _containers.RepeatedScalarFieldContainer[str]
    target_user_groups: _containers.RepeatedScalarFieldContainer[str]
    is_active: bool
    starts_at: _timestamp_pb2.Timestamp
    ends_at: _timestamp_pb2.Timestamp
    grant_memo: str
    email_events: _containers.RepeatedScalarFieldContainer[str]
    max_grants_total: int
    target_plan_types: _containers.RepeatedScalarFieldContainer[str]
    credit_expires_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., description: _Optional[str]=..., event_category: _Optional[str]=..., amount_cents: _Optional[int]=..., max_grants_per_org: _Optional[int]=..., max_grants_per_member: _Optional[int]=..., target_org_ids: _Optional[_Iterable[str]]=..., target_user_groups: _Optional[_Iterable[str]]=..., is_active: bool=..., starts_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., ends_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., grant_memo: _Optional[str]=..., email_events: _Optional[_Iterable[str]]=..., max_grants_total: _Optional[int]=..., target_plan_types: _Optional[_Iterable[str]]=..., credit_expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class UpdatePromotionResponse(_message.Message):
    __slots__ = ('promotion',)
    PROMOTION_FIELD_NUMBER: _ClassVar[int]
    promotion: Promotion

    def __init__(self, promotion: _Optional[_Union[Promotion, _Mapping]]=...) -> None:
        ...

class ListPromotionGrantsRequest(_message.Message):
    __slots__ = ('promotion_id',)
    PROMOTION_ID_FIELD_NUMBER: _ClassVar[int]
    promotion_id: str

    def __init__(self, promotion_id: _Optional[str]=...) -> None:
        ...

class ListPromotionGrantsResponse(_message.Message):
    __slots__ = ('grants',)
    GRANTS_FIELD_NUMBER: _ClassVar[int]
    grants: _containers.RepeatedCompositeFieldContainer[PromotionGrant]

    def __init__(self, grants: _Optional[_Iterable[_Union[PromotionGrant, _Mapping]]]=...) -> None:
        ...

class DeletePromotionRequest(_message.Message):
    __slots__ = ('id',)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str

    def __init__(self, id: _Optional[str]=...) -> None:
        ...

class DeletePromotionResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListEventCategoriesRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListEventCategoriesResponse(_message.Message):
    __slots__ = ('categories',)
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    categories: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, categories: _Optional[_Iterable[str]]=...) -> None:
        ...