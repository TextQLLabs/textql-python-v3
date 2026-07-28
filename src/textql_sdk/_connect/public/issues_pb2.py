# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
# pylint: skip-file
# mypy: ignore-errors
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/issues.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ..public import common_pb2 as public_dot_common__pb2
from ..public import options_pb2 as public_dot_options__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13public/issues.proto\x12\x18textql.rpc.public.issues\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x13public/common.proto\x1a\x14public/options.proto"\xe5\x05\n\x05Issue\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x10\n\x03seq\x18\x10 \x01(\x03R\x03seq\x12\x1f\n\x0bissue_class\x18\x03 \x01(\tR\nissueClass\x12!\n\x0csubject_type\x18\x04 \x01(\tR\x0bsubjectType\x12\x1d\n\nsubject_id\x18\x05 \x01(\tR\tsubjectId\x12(\n\rsubject_label\x18\x06 \x01(\tH\x00R\x0csubjectLabel\x88\x01\x01\x12\x14\n\x05title\x18\x07 \x01(\tR\x05title\x12:\n\x05state\x18\x08 \x01(\x0e2$.textql.rpc.public.issues.IssueStateR\x05state\x12C\n\x08severity\x18\t \x01(\x0e2\'.textql.rpc.public.issues.IssueSeverityR\x08severity\x129\n\ncreated_at\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt\x129\n\nupdated_at\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampR\tupdatedAt\x12@\n\x0bresolved_at\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampH\x01R\nresolvedAt\x88\x01\x01\x12*\n\x11open_report_count\x18\r \x01(\x05R\x0fopenReportCount\x12,\n\x12total_report_count\x18\x0e \x01(\x05R\x10totalReportCount\x12K\n\x0bassignments\x18\x0f \x03(\x0b2).textql.rpc.public.issues.IssueAssignmentR\x0bassignmentsB\x10\n\x0e_subject_labelB\x0e\n\x0c_resolved_at"\xed\x03\n\x0bIssueReport\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x19\n\x08issue_id\x18\x03 \x01(\tR\x07issueId\x12\x1a\n\x08reporter\x18\x04 \x01(\tR\x08reporter\x12\x1d\n\nsource_key\x18\x05 \x01(\tR\tsourceKey\x12\x1b\n\x06detail\x18\x06 \x01(\tH\x00R\x06detail\x88\x01\x01\x12;\n\x05state\x18\x07 \x01(\x0e2%.textql.rpc.public.issues.ReportStateR\x05state\x12@\n\x0bresolved_at\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampH\x01R\nresolvedAt\x88\x01\x01\x12$\n\x0bresolved_by\x18\t \x01(\tH\x02R\nresolvedBy\x88\x01\x01\x129\n\ncreated_at\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt\x129\n\nupdated_at\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampR\tupdatedAtB\t\n\x07_detailB\x0e\n\x0c_resolved_atB\x0e\n\x0c_resolved_by"\x8c\x03\n\x0fIssueAssignment\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x19\n\x08issue_id\x18\x03 \x01(\tR\x07issueId\x12K\n\rassignee_kind\x18\x04 \x01(\x0e2&.textql.rpc.public.issues.AssigneeKindR\x0cassigneeKind\x12\x1f\n\x0bassignee_id\x18\x05 \x01(\tR\nassigneeId\x12$\n\x0bassigned_by\x18\x06 \x01(\tH\x00R\nassignedBy\x88\x01\x01\x12;\n\x0bassigned_at\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampR\nassignedAt\x12D\n\runassigned_at\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampH\x01R\x0cunassignedAt\x88\x01\x01B\x0e\n\x0c_assigned_byB\x10\n\x0e_unassigned_at"\xb6\x04\n\x11ListIssuesRequest\x12<\n\x06states\x18\x01 \x03(\x0e2$.textql.rpc.public.issues.IssueStateR\x06states\x12O\n\x0cmin_severity\x18\x02 \x01(\x0e2\'.textql.rpc.public.issues.IssueSeverityH\x00R\x0bminSeverity\x88\x01\x01\x12&\n\x0csubject_type\x18\x03 \x01(\tH\x01R\x0bsubjectType\x88\x01\x01\x12$\n\x0bissue_class\x18\x04 \x01(\tH\x02R\nissueClass\x88\x01\x01\x12 \n\tpage_size\x18\x05 \x01(\rH\x03R\x08pageSize\x88\x01\x01\x12"\n\npage_token\x18\x06 \x01(\tH\x04R\tpageToken\x88\x01\x01\x12S\n\x0esort_direction\x18\x07 \x01(\x0e2\'.textql.rpc.public.common.SortDirectionH\x05R\rsortDirection\x88\x01\x01\x12G\n\ntime_range\x18\x08 \x01(\x0e2(.textql.rpc.public.issues.IssueTimeRangeR\ttimeRangeB\x0f\n\r_min_severityB\x0f\n\r_subject_typeB\x0e\n\x0c_issue_classB\x0c\n\n_page_sizeB\r\n\x0b_page_tokenB\x11\n\x0f_sort_direction"\x8e\x01\n\x12ListIssuesResponse\x127\n\x06issues\x18\x01 \x03(\x0b2\x1f.textql.rpc.public.issues.IssueR\x06issues\x12+\n\x0fnext_page_token\x18\x02 \x01(\tH\x00R\rnextPageToken\x88\x01\x01B\x12\n\x10_next_page_token",\n\x0fGetIssueRequest\x12\x19\n\x08issue_id\x18\x01 \x01(\tR\x07issueId"\xb3\x02\n\x10GetIssueResponse\x125\n\x05issue\x18\x01 \x01(\x0b2\x1f.textql.rpc.public.issues.IssueR\x05issue\x12?\n\x07reports\x18\x02 \x03(\x0b2%.textql.rpc.public.issues.IssueReportR\x07reports\x12X\n\x12assignment_history\x18\x03 \x03(\x0b2).textql.rpc.public.issues.IssueAssignmentR\x11assignmentHistory\x12M\n\x0eaffected_roles\x18\x04 \x03(\x0b2&.textql.rpc.public.issues.AffectedRoleR\raffectedRoles"\\\n\x0cAffectedRole\x12\x17\n\x07role_id\x18\x01 \x01(\tR\x06roleId\x12\x1b\n\trole_name\x18\x02 \x01(\tR\x08roleName\x12\x16\n\x06source\x18\x03 \x01(\tR\x06source"I\n\x14GetIssueStatsRequest\x12"\n\ntrend_days\x18\x01 \x01(\x05H\x00R\ttrendDays\x88\x01\x01B\r\n\x0b_trend_days"6\n\nDailyCount\x12\x12\n\x04date\x18\x01 \x01(\tR\x04date\x12\x14\n\x05count\x18\x02 \x01(\x05R\x05count"\xcd\x01\n\nIssueStats\x12\x1d\n\nopen_total\x18\x01 \x01(\x05R\topenTotal\x12\x1b\n\topen_high\x18\x02 \x01(\x05R\x08openHigh\x12\x1f\n\x0bopen_medium\x18\x03 \x01(\x05R\nopenMedium\x12\x19\n\x08open_low\x18\x04 \x01(\x05R\x07openLow\x12G\n\x0copened_daily\x18\x05 \x03(\x0b2$.textql.rpc.public.issues.DailyCountR\x0bopenedDaily"S\n\x15GetIssueStatsResponse\x12:\n\x05stats\x18\x01 \x01(\x0b2$.textql.rpc.public.issues.IssueStatsR\x05stats"p\n\x17UpdateIssueStateRequest\x12\x19\n\x08issue_id\x18\x01 \x01(\tR\x07issueId\x12:\n\x05state\x18\x02 \x01(\x0e2$.textql.rpc.public.issues.IssueStateR\x05state"Q\n\x18UpdateIssueStateResponse\x125\n\x05issue\x18\x01 \x01(\x0b2\x1f.textql.rpc.public.issues.IssueR\x05issue"t\n\x18UpdateReportStateRequest\x12\x1b\n\treport_id\x18\x01 \x01(\tR\x08reportId\x12;\n\x05state\x18\x02 \x01(\x0e2%.textql.rpc.public.issues.ReportStateR\x05state"Z\n\x19UpdateReportStateResponse\x12=\n\x06report\x18\x01 \x01(\x0b2%.textql.rpc.public.issues.IssueReportR\x06report"\x9d\x01\n\x12AssignIssueRequest\x12\x19\n\x08issue_id\x18\x01 \x01(\tR\x07issueId\x12K\n\rassignee_kind\x18\x02 \x01(\x0e2&.textql.rpc.public.issues.AssigneeKindR\x0cassigneeKind\x12\x1f\n\x0bassignee_id\x18\x03 \x01(\tR\nassigneeId"`\n\x13AssignIssueResponse\x12I\n\nassignment\x18\x01 \x01(\x0b2).textql.rpc.public.issues.IssueAssignmentR\nassignment"\xcb\x01\n\x14UnassignIssueRequest\x12\x19\n\x08issue_id\x18\x01 \x01(\tR\x07issueId\x12P\n\rassignee_kind\x18\x02 \x01(\x0e2&.textql.rpc.public.issues.AssigneeKindH\x00R\x0cassigneeKind\x88\x01\x01\x12$\n\x0bassignee_id\x18\x03 \x01(\tH\x01R\nassigneeId\x88\x01\x01B\x10\n\x0e_assignee_kindB\x0e\n\x0c_assignee_id"\xa4\x01\n\x17BulkAssignIssuesRequest\x12\x1b\n\tissue_ids\x18\x01 \x03(\tR\x08issueIds\x12K\n\rassignee_kind\x18\x02 \x01(\x0e2&.textql.rpc.public.issues.AssigneeKindR\x0cassigneeKind\x12\x1f\n\x0bassignee_id\x18\x03 \x01(\tR\nassigneeId"A\n\x18BulkAssignIssuesResponse\x12%\n\x0eaffected_count\x18\x01 \x01(\x05R\raffectedCount"8\n\x19BulkUnassignIssuesRequest\x12\x1b\n\tissue_ids\x18\x01 \x03(\tR\x08issueIds"C\n\x1aBulkUnassignIssuesResponse\x12%\n\x0eaffected_count\x18\x01 \x01(\x05R\raffectedCount*q\n\nIssueState\x12\x1b\n\x17ISSUE_STATE_UNSPECIFIED\x10\x00\x12\x14\n\x10ISSUE_STATE_OPEN\x10\x01\x12\x18\n\x14ISSUE_STATE_RESOLVED\x10\x02\x12\x16\n\x12ISSUE_STATE_CLOSED\x10\x03*{\n\rIssueSeverity\x12\x1e\n\x1aISSUE_SEVERITY_UNSPECIFIED\x10\x00\x12\x16\n\x12ISSUE_SEVERITY_LOW\x10\x01\x12\x19\n\x15ISSUE_SEVERITY_MEDIUM\x10\x02\x12\x17\n\x13ISSUE_SEVERITY_HIGH\x10\x03*v\n\x0bReportState\x12\x1c\n\x18REPORT_STATE_UNSPECIFIED\x10\x00\x12\x15\n\x11REPORT_STATE_OPEN\x10\x01\x12\x19\n\x15REPORT_STATE_RESOLVED\x10\x02\x12\x17\n\x13REPORT_STATE_CLOSED\x10\x03*\xbc\x01\n\x0eIssueTimeRange\x12 \n\x1cISSUE_TIME_RANGE_UNSPECIFIED\x10\x00\x12\x18\n\x14ISSUE_TIME_RANGE_DAY\x10\x01\x12\x19\n\x15ISSUE_TIME_RANGE_WEEK\x10\x02\x12\x1a\n\x16ISSUE_TIME_RANGE_MONTH\x10\x03\x12\x1c\n\x18ISSUE_TIME_RANGE_QUARTER\x10\x04\x12\x19\n\x15ISSUE_TIME_RANGE_YEAR\x10\x05*\x96\x01\n\x0cAssigneeKind\x12\x1d\n\x19ASSIGNEE_KIND_UNSPECIFIED\x10\x00\x12\x18\n\x14ASSIGNEE_KIND_MEMBER\x10\x01\x12\x16\n\x12ASSIGNEE_KIND_ROLE\x10\x02\x12\x1c\n\x18ASSIGNEE_KIND_SCIM_GROUP\x10\x03\x12\x17\n\x13ASSIGNEE_KIND_AGENT\x10\x042\x95\x08\n\x0cIssueService\x12l\n\nListIssues\x12+.textql.rpc.public.issues.ListIssuesRequest\x1a,.textql.rpc.public.issues.ListIssuesResponse"\x03\x90\x02\x01\x12f\n\x08GetIssue\x12).textql.rpc.public.issues.GetIssueRequest\x1a*.textql.rpc.public.issues.GetIssueResponse"\x03\x90\x02\x01\x12u\n\rGetIssueStats\x12..textql.rpc.public.issues.GetIssueStatsRequest\x1a/.textql.rpc.public.issues.GetIssueStatsResponse"\x03\x90\x02\x01\x12y\n\x10UpdateIssueState\x121.textql.rpc.public.issues.UpdateIssueStateRequest\x1a2.textql.rpc.public.issues.UpdateIssueStateResponse\x12|\n\x11UpdateReportState\x122.textql.rpc.public.issues.UpdateReportStateRequest\x1a3.textql.rpc.public.issues.UpdateReportStateResponse\x12j\n\x0bAssignIssue\x12,.textql.rpc.public.issues.AssignIssueRequest\x1a-.textql.rpc.public.issues.AssignIssueResponse\x12W\n\rUnassignIssue\x12..textql.rpc.public.issues.UnassignIssueRequest\x1a\x16.google.protobuf.Empty\x12y\n\x10BulkAssignIssues\x121.textql.rpc.public.issues.BulkAssignIssuesRequest\x1a2.textql.rpc.public.issues.BulkAssignIssuesResponse\x12\x7f\n\x12BulkUnassignIssues\x123.textql.rpc.public.issues.BulkUnassignIssuesRequest\x1a4.textql.rpc.public.issues.BulkUnassignIssuesResponseB\x0c\x92\xb5\x18\x08INTERNALb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.issues_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\x92\xb5\x18\x08INTERNAL'
    _globals['_ISSUESERVICE'].methods_by_name['ListIssues']._loaded_options = None
    _globals['_ISSUESERVICE'].methods_by_name['ListIssues']._serialized_options = b'\x90\x02\x01'
    _globals['_ISSUESERVICE'].methods_by_name['GetIssue']._loaded_options = None
    _globals['_ISSUESERVICE'].methods_by_name['GetIssue']._serialized_options = b'\x90\x02\x01'
    _globals['_ISSUESERVICE'].methods_by_name['GetIssueStats']._loaded_options = None
    _globals['_ISSUESERVICE'].methods_by_name['GetIssueStats']._serialized_options = b'\x90\x02\x01'
    _globals['_ISSUESTATE']._serialized_start = 4613
    _globals['_ISSUESTATE']._serialized_end = 4726
    _globals['_ISSUESEVERITY']._serialized_start = 4728
    _globals['_ISSUESEVERITY']._serialized_end = 4851
    _globals['_REPORTSTATE']._serialized_start = 4853
    _globals['_REPORTSTATE']._serialized_end = 4971
    _globals['_ISSUETIMERANGE']._serialized_start = 4974
    _globals['_ISSUETIMERANGE']._serialized_end = 5162
    _globals['_ASSIGNEEKIND']._serialized_start = 5165
    _globals['_ASSIGNEEKIND']._serialized_end = 5315
    _globals['_ISSUE']._serialized_start = 155
    _globals['_ISSUE']._serialized_end = 896
    _globals['_ISSUEREPORT']._serialized_start = 899
    _globals['_ISSUEREPORT']._serialized_end = 1392
    _globals['_ISSUEASSIGNMENT']._serialized_start = 1395
    _globals['_ISSUEASSIGNMENT']._serialized_end = 1791
    _globals['_LISTISSUESREQUEST']._serialized_start = 1794
    _globals['_LISTISSUESREQUEST']._serialized_end = 2360
    _globals['_LISTISSUESRESPONSE']._serialized_start = 2363
    _globals['_LISTISSUESRESPONSE']._serialized_end = 2505
    _globals['_GETISSUEREQUEST']._serialized_start = 2507
    _globals['_GETISSUEREQUEST']._serialized_end = 2551
    _globals['_GETISSUERESPONSE']._serialized_start = 2554
    _globals['_GETISSUERESPONSE']._serialized_end = 2861
    _globals['_AFFECTEDROLE']._serialized_start = 2863
    _globals['_AFFECTEDROLE']._serialized_end = 2955
    _globals['_GETISSUESTATSREQUEST']._serialized_start = 2957
    _globals['_GETISSUESTATSREQUEST']._serialized_end = 3030
    _globals['_DAILYCOUNT']._serialized_start = 3032
    _globals['_DAILYCOUNT']._serialized_end = 3086
    _globals['_ISSUESTATS']._serialized_start = 3089
    _globals['_ISSUESTATS']._serialized_end = 3294
    _globals['_GETISSUESTATSRESPONSE']._serialized_start = 3296
    _globals['_GETISSUESTATSRESPONSE']._serialized_end = 3379
    _globals['_UPDATEISSUESTATEREQUEST']._serialized_start = 3381
    _globals['_UPDATEISSUESTATEREQUEST']._serialized_end = 3493
    _globals['_UPDATEISSUESTATERESPONSE']._serialized_start = 3495
    _globals['_UPDATEISSUESTATERESPONSE']._serialized_end = 3576
    _globals['_UPDATEREPORTSTATEREQUEST']._serialized_start = 3578
    _globals['_UPDATEREPORTSTATEREQUEST']._serialized_end = 3694
    _globals['_UPDATEREPORTSTATERESPONSE']._serialized_start = 3696
    _globals['_UPDATEREPORTSTATERESPONSE']._serialized_end = 3786
    _globals['_ASSIGNISSUEREQUEST']._serialized_start = 3789
    _globals['_ASSIGNISSUEREQUEST']._serialized_end = 3946
    _globals['_ASSIGNISSUERESPONSE']._serialized_start = 3948
    _globals['_ASSIGNISSUERESPONSE']._serialized_end = 4044
    _globals['_UNASSIGNISSUEREQUEST']._serialized_start = 4047
    _globals['_UNASSIGNISSUEREQUEST']._serialized_end = 4250
    _globals['_BULKASSIGNISSUESREQUEST']._serialized_start = 4253
    _globals['_BULKASSIGNISSUESREQUEST']._serialized_end = 4417
    _globals['_BULKASSIGNISSUESRESPONSE']._serialized_start = 4419
    _globals['_BULKASSIGNISSUESRESPONSE']._serialized_end = 4484
    _globals['_BULKUNASSIGNISSUESREQUEST']._serialized_start = 4486
    _globals['_BULKUNASSIGNISSUESREQUEST']._serialized_end = 4542
    _globals['_BULKUNASSIGNISSUESRESPONSE']._serialized_start = 4544
    _globals['_BULKUNASSIGNISSUESRESPONSE']._serialized_end = 4611
    _globals['_ISSUESERVICE']._serialized_start = 5318
    _globals['_ISSUESERVICE']._serialized_end = 6363