# pylint: skip-file
# mypy: ignore-errors
import datetime
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ..public import common_pb2 as _common_pb2
from ..public import options_pb2 as _options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class IssueState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ISSUE_STATE_UNSPECIFIED: _ClassVar[IssueState]
    ISSUE_STATE_OPEN: _ClassVar[IssueState]
    ISSUE_STATE_RESOLVED: _ClassVar[IssueState]
    ISSUE_STATE_CLOSED: _ClassVar[IssueState]

class IssueSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ISSUE_SEVERITY_UNSPECIFIED: _ClassVar[IssueSeverity]
    ISSUE_SEVERITY_LOW: _ClassVar[IssueSeverity]
    ISSUE_SEVERITY_MEDIUM: _ClassVar[IssueSeverity]
    ISSUE_SEVERITY_HIGH: _ClassVar[IssueSeverity]

class ReportState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPORT_STATE_UNSPECIFIED: _ClassVar[ReportState]
    REPORT_STATE_OPEN: _ClassVar[ReportState]
    REPORT_STATE_RESOLVED: _ClassVar[ReportState]
    REPORT_STATE_CLOSED: _ClassVar[ReportState]

class IssueTimeRange(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ISSUE_TIME_RANGE_UNSPECIFIED: _ClassVar[IssueTimeRange]
    ISSUE_TIME_RANGE_DAY: _ClassVar[IssueTimeRange]
    ISSUE_TIME_RANGE_WEEK: _ClassVar[IssueTimeRange]
    ISSUE_TIME_RANGE_MONTH: _ClassVar[IssueTimeRange]
    ISSUE_TIME_RANGE_QUARTER: _ClassVar[IssueTimeRange]
    ISSUE_TIME_RANGE_YEAR: _ClassVar[IssueTimeRange]

class AssigneeKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASSIGNEE_KIND_UNSPECIFIED: _ClassVar[AssigneeKind]
    ASSIGNEE_KIND_MEMBER: _ClassVar[AssigneeKind]
    ASSIGNEE_KIND_ROLE: _ClassVar[AssigneeKind]
    ASSIGNEE_KIND_SCIM_GROUP: _ClassVar[AssigneeKind]
    ASSIGNEE_KIND_AGENT: _ClassVar[AssigneeKind]
ISSUE_STATE_UNSPECIFIED: IssueState
ISSUE_STATE_OPEN: IssueState
ISSUE_STATE_RESOLVED: IssueState
ISSUE_STATE_CLOSED: IssueState
ISSUE_SEVERITY_UNSPECIFIED: IssueSeverity
ISSUE_SEVERITY_LOW: IssueSeverity
ISSUE_SEVERITY_MEDIUM: IssueSeverity
ISSUE_SEVERITY_HIGH: IssueSeverity
REPORT_STATE_UNSPECIFIED: ReportState
REPORT_STATE_OPEN: ReportState
REPORT_STATE_RESOLVED: ReportState
REPORT_STATE_CLOSED: ReportState
ISSUE_TIME_RANGE_UNSPECIFIED: IssueTimeRange
ISSUE_TIME_RANGE_DAY: IssueTimeRange
ISSUE_TIME_RANGE_WEEK: IssueTimeRange
ISSUE_TIME_RANGE_MONTH: IssueTimeRange
ISSUE_TIME_RANGE_QUARTER: IssueTimeRange
ISSUE_TIME_RANGE_YEAR: IssueTimeRange
ASSIGNEE_KIND_UNSPECIFIED: AssigneeKind
ASSIGNEE_KIND_MEMBER: AssigneeKind
ASSIGNEE_KIND_ROLE: AssigneeKind
ASSIGNEE_KIND_SCIM_GROUP: AssigneeKind
ASSIGNEE_KIND_AGENT: AssigneeKind

class Issue(_message.Message):
    __slots__ = ('id', 'org_id', 'seq', 'issue_class', 'subject_type', 'subject_id', 'subject_label', 'title', 'state', 'severity', 'created_at', 'updated_at', 'resolved_at', 'open_report_count', 'total_report_count', 'assignments')
    ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    SEQ_FIELD_NUMBER: _ClassVar[int]
    ISSUE_CLASS_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_LABEL_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_AT_FIELD_NUMBER: _ClassVar[int]
    OPEN_REPORT_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_REPORT_COUNT_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    org_id: str
    seq: int
    issue_class: str
    subject_type: str
    subject_id: str
    subject_label: str
    title: str
    state: IssueState
    severity: IssueSeverity
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    resolved_at: _timestamp_pb2.Timestamp
    open_report_count: int
    total_report_count: int
    assignments: _containers.RepeatedCompositeFieldContainer[IssueAssignment]

    def __init__(self, id: _Optional[str]=..., org_id: _Optional[str]=..., seq: _Optional[int]=..., issue_class: _Optional[str]=..., subject_type: _Optional[str]=..., subject_id: _Optional[str]=..., subject_label: _Optional[str]=..., title: _Optional[str]=..., state: _Optional[_Union[IssueState, str]]=..., severity: _Optional[_Union[IssueSeverity, str]]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., resolved_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., open_report_count: _Optional[int]=..., total_report_count: _Optional[int]=..., assignments: _Optional[_Iterable[_Union[IssueAssignment, _Mapping]]]=...) -> None:
        ...

class IssueReport(_message.Message):
    __slots__ = ('id', 'org_id', 'issue_id', 'reporter', 'source_key', 'detail', 'state', 'resolved_at', 'resolved_by', 'created_at', 'updated_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    ISSUE_ID_FIELD_NUMBER: _ClassVar[int]
    REPORTER_FIELD_NUMBER: _ClassVar[int]
    SOURCE_KEY_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_AT_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    org_id: str
    issue_id: str
    reporter: str
    source_key: str
    detail: str
    state: ReportState
    resolved_at: _timestamp_pb2.Timestamp
    resolved_by: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., org_id: _Optional[str]=..., issue_id: _Optional[str]=..., reporter: _Optional[str]=..., source_key: _Optional[str]=..., detail: _Optional[str]=..., state: _Optional[_Union[ReportState, str]]=..., resolved_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., resolved_by: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class IssueAssignment(_message.Message):
    __slots__ = ('id', 'org_id', 'issue_id', 'assignee_kind', 'assignee_id', 'assigned_by', 'assigned_at', 'unassigned_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    ISSUE_ID_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEE_KIND_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEE_ID_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_BY_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_AT_FIELD_NUMBER: _ClassVar[int]
    UNASSIGNED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    org_id: str
    issue_id: str
    assignee_kind: AssigneeKind
    assignee_id: str
    assigned_by: str
    assigned_at: _timestamp_pb2.Timestamp
    unassigned_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., org_id: _Optional[str]=..., issue_id: _Optional[str]=..., assignee_kind: _Optional[_Union[AssigneeKind, str]]=..., assignee_id: _Optional[str]=..., assigned_by: _Optional[str]=..., assigned_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., unassigned_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListIssuesRequest(_message.Message):
    __slots__ = ('states', 'min_severity', 'subject_type', 'issue_class', 'page_size', 'page_token', 'sort_direction', 'time_range')
    STATES_FIELD_NUMBER: _ClassVar[int]
    MIN_SEVERITY_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ISSUE_CLASS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SORT_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    states: _containers.RepeatedScalarFieldContainer[IssueState]
    min_severity: IssueSeverity
    subject_type: str
    issue_class: str
    page_size: int
    page_token: str
    sort_direction: _common_pb2.SortDirection
    time_range: IssueTimeRange

    def __init__(self, states: _Optional[_Iterable[_Union[IssueState, str]]]=..., min_severity: _Optional[_Union[IssueSeverity, str]]=..., subject_type: _Optional[str]=..., issue_class: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., sort_direction: _Optional[_Union[_common_pb2.SortDirection, str]]=..., time_range: _Optional[_Union[IssueTimeRange, str]]=...) -> None:
        ...

class ListIssuesResponse(_message.Message):
    __slots__ = ('issues', 'next_page_token')
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    issues: _containers.RepeatedCompositeFieldContainer[Issue]
    next_page_token: str

    def __init__(self, issues: _Optional[_Iterable[_Union[Issue, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetIssueRequest(_message.Message):
    __slots__ = ('issue_id',)
    ISSUE_ID_FIELD_NUMBER: _ClassVar[int]
    issue_id: str

    def __init__(self, issue_id: _Optional[str]=...) -> None:
        ...

class GetIssueResponse(_message.Message):
    __slots__ = ('issue', 'reports', 'assignment_history', 'affected_roles')
    ISSUE_FIELD_NUMBER: _ClassVar[int]
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_HISTORY_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_ROLES_FIELD_NUMBER: _ClassVar[int]
    issue: Issue
    reports: _containers.RepeatedCompositeFieldContainer[IssueReport]
    assignment_history: _containers.RepeatedCompositeFieldContainer[IssueAssignment]
    affected_roles: _containers.RepeatedCompositeFieldContainer[AffectedRole]

    def __init__(self, issue: _Optional[_Union[Issue, _Mapping]]=..., reports: _Optional[_Iterable[_Union[IssueReport, _Mapping]]]=..., assignment_history: _Optional[_Iterable[_Union[IssueAssignment, _Mapping]]]=..., affected_roles: _Optional[_Iterable[_Union[AffectedRole, _Mapping]]]=...) -> None:
        ...

class AffectedRole(_message.Message):
    __slots__ = ('role_id', 'role_name', 'source')
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    role_id: str
    role_name: str
    source: str

    def __init__(self, role_id: _Optional[str]=..., role_name: _Optional[str]=..., source: _Optional[str]=...) -> None:
        ...

class GetIssueStatsRequest(_message.Message):
    __slots__ = ('trend_days',)
    TREND_DAYS_FIELD_NUMBER: _ClassVar[int]
    trend_days: int

    def __init__(self, trend_days: _Optional[int]=...) -> None:
        ...

class DailyCount(_message.Message):
    __slots__ = ('date', 'count')
    DATE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    date: str
    count: int

    def __init__(self, date: _Optional[str]=..., count: _Optional[int]=...) -> None:
        ...

class IssueStats(_message.Message):
    __slots__ = ('open_total', 'open_high', 'open_medium', 'open_low', 'opened_daily')
    OPEN_TOTAL_FIELD_NUMBER: _ClassVar[int]
    OPEN_HIGH_FIELD_NUMBER: _ClassVar[int]
    OPEN_MEDIUM_FIELD_NUMBER: _ClassVar[int]
    OPEN_LOW_FIELD_NUMBER: _ClassVar[int]
    OPENED_DAILY_FIELD_NUMBER: _ClassVar[int]
    open_total: int
    open_high: int
    open_medium: int
    open_low: int
    opened_daily: _containers.RepeatedCompositeFieldContainer[DailyCount]

    def __init__(self, open_total: _Optional[int]=..., open_high: _Optional[int]=..., open_medium: _Optional[int]=..., open_low: _Optional[int]=..., opened_daily: _Optional[_Iterable[_Union[DailyCount, _Mapping]]]=...) -> None:
        ...

class GetIssueStatsResponse(_message.Message):
    __slots__ = ('stats',)
    STATS_FIELD_NUMBER: _ClassVar[int]
    stats: IssueStats

    def __init__(self, stats: _Optional[_Union[IssueStats, _Mapping]]=...) -> None:
        ...

class UpdateIssueStateRequest(_message.Message):
    __slots__ = ('issue_id', 'state')
    ISSUE_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    issue_id: str
    state: IssueState

    def __init__(self, issue_id: _Optional[str]=..., state: _Optional[_Union[IssueState, str]]=...) -> None:
        ...

class UpdateIssueStateResponse(_message.Message):
    __slots__ = ('issue',)
    ISSUE_FIELD_NUMBER: _ClassVar[int]
    issue: Issue

    def __init__(self, issue: _Optional[_Union[Issue, _Mapping]]=...) -> None:
        ...

class UpdateReportStateRequest(_message.Message):
    __slots__ = ('report_id', 'state')
    REPORT_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    report_id: str
    state: ReportState

    def __init__(self, report_id: _Optional[str]=..., state: _Optional[_Union[ReportState, str]]=...) -> None:
        ...

class UpdateReportStateResponse(_message.Message):
    __slots__ = ('report',)
    REPORT_FIELD_NUMBER: _ClassVar[int]
    report: IssueReport

    def __init__(self, report: _Optional[_Union[IssueReport, _Mapping]]=...) -> None:
        ...

class AssignIssueRequest(_message.Message):
    __slots__ = ('issue_id', 'assignee_kind', 'assignee_id')
    ISSUE_ID_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEE_KIND_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEE_ID_FIELD_NUMBER: _ClassVar[int]
    issue_id: str
    assignee_kind: AssigneeKind
    assignee_id: str

    def __init__(self, issue_id: _Optional[str]=..., assignee_kind: _Optional[_Union[AssigneeKind, str]]=..., assignee_id: _Optional[str]=...) -> None:
        ...

class AssignIssueResponse(_message.Message):
    __slots__ = ('assignment',)
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    assignment: IssueAssignment

    def __init__(self, assignment: _Optional[_Union[IssueAssignment, _Mapping]]=...) -> None:
        ...

class UnassignIssueRequest(_message.Message):
    __slots__ = ('issue_id', 'assignee_kind', 'assignee_id')
    ISSUE_ID_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEE_KIND_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEE_ID_FIELD_NUMBER: _ClassVar[int]
    issue_id: str
    assignee_kind: AssigneeKind
    assignee_id: str

    def __init__(self, issue_id: _Optional[str]=..., assignee_kind: _Optional[_Union[AssigneeKind, str]]=..., assignee_id: _Optional[str]=...) -> None:
        ...

class BulkAssignIssuesRequest(_message.Message):
    __slots__ = ('issue_ids', 'assignee_kind', 'assignee_id')
    ISSUE_IDS_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEE_KIND_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEE_ID_FIELD_NUMBER: _ClassVar[int]
    issue_ids: _containers.RepeatedScalarFieldContainer[str]
    assignee_kind: AssigneeKind
    assignee_id: str

    def __init__(self, issue_ids: _Optional[_Iterable[str]]=..., assignee_kind: _Optional[_Union[AssigneeKind, str]]=..., assignee_id: _Optional[str]=...) -> None:
        ...

class BulkAssignIssuesResponse(_message.Message):
    __slots__ = ('affected_count',)
    AFFECTED_COUNT_FIELD_NUMBER: _ClassVar[int]
    affected_count: int

    def __init__(self, affected_count: _Optional[int]=...) -> None:
        ...

class BulkUnassignIssuesRequest(_message.Message):
    __slots__ = ('issue_ids',)
    ISSUE_IDS_FIELD_NUMBER: _ClassVar[int]
    issue_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, issue_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class BulkUnassignIssuesResponse(_message.Message):
    __slots__ = ('affected_count',)
    AFFECTED_COUNT_FIELD_NUMBER: _ClassVar[int]
    affected_count: int

    def __init__(self, affected_count: _Optional[int]=...) -> None:
        ...