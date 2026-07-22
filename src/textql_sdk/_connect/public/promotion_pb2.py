"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/promotion.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ..public import options_pb2 as public_dot_options__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16public/promotion.proto\x12\x1btextql.rpc.public.promotion\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14public/options.proto"\x9c\x06\n\tPromotion\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0bdescription\x18\x03 \x01(\tR\x0bdescription\x12%\n\x0eevent_category\x18\x04 \x01(\tR\reventCategory\x12!\n\x0camount_cents\x18\x05 \x01(\x03R\x0bamountCents\x12+\n\x12max_grants_per_org\x18\x06 \x01(\x05R\x0fmaxGrantsPerOrg\x121\n\x15max_grants_per_member\x18\x07 \x01(\x05R\x12maxGrantsPerMember\x12$\n\x0etarget_org_ids\x18\x08 \x03(\tR\x0ctargetOrgIds\x12,\n\x12target_user_groups\x18\t \x03(\tR\x10targetUserGroups\x12\x1b\n\tis_active\x18\n \x01(\x08R\x08isActive\x12<\n\tstarts_at\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampH\x00R\x08startsAt\x88\x01\x01\x128\n\x07ends_at\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampH\x01R\x06endsAt\x88\x01\x01\x12\x1d\n\ngrant_memo\x18\r \x01(\tR\tgrantMemo\x12!\n\x0cgrants_count\x18\x0e \x01(\x05R\x0bgrantsCount\x12!\n\x0cemail_events\x18\x0f \x03(\tR\x0bemailEvents\x12(\n\x10max_grants_total\x18\x10 \x01(\x05R\x0emaxGrantsTotal\x12*\n\x11target_plan_types\x18\x11 \x03(\tR\x0ftargetPlanTypes\x12K\n\x11credit_expires_at\x18\x12 \x01(\x0b2\x1a.google.protobuf.TimestampH\x02R\x0fcreditExpiresAt\x88\x01\x01B\x0c\n\n_starts_atB\n\n\x08_ends_atB\x14\n\x12_credit_expires_at"\xd0\x02\n\x0ePromotionGrant\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12!\n\x0cpromotion_id\x18\x02 \x01(\tR\x0bpromotionId\x12\x15\n\x06org_id\x18\x03 \x01(\tR\x05orgId\x12\x1b\n\tmember_id\x18\x04 \x01(\tR\x08memberId\x12\x19\n\x08event_id\x18\x05 \x01(\tR\x07eventId\x12+\n\x11idempotency_token\x18\x06 \x01(\tR\x10idempotencyToken\x12\x16\n\x06status\x18\x07 \x01(\tR\x06status\x12!\n\x0cmember_email\x18\x08 \x01(\tR\x0bmemberEmail\x12\x19\n\x08org_name\x18\t \x01(\tR\x07orgName\x129\n\ncreated_at\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt"\x17\n\x15ListPromotionsRequest"`\n\x16ListPromotionsResponse\x12F\n\npromotions\x18\x01 \x03(\x0b2&.textql.rpc.public.promotion.PromotionR\npromotions"\xf6\x05\n\x16CreatePromotionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0bdescription\x18\x02 \x01(\tR\x0bdescription\x12%\n\x0eevent_category\x18\x03 \x01(\tR\reventCategory\x12!\n\x0camount_cents\x18\x04 \x01(\x03R\x0bamountCents\x12+\n\x12max_grants_per_org\x18\x05 \x01(\x05R\x0fmaxGrantsPerOrg\x121\n\x15max_grants_per_member\x18\x06 \x01(\x05R\x12maxGrantsPerMember\x12$\n\x0etarget_org_ids\x18\x07 \x03(\tR\x0ctargetOrgIds\x12,\n\x12target_user_groups\x18\x08 \x03(\tR\x10targetUserGroups\x12\x1b\n\tis_active\x18\t \x01(\x08R\x08isActive\x12<\n\tstarts_at\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampH\x00R\x08startsAt\x88\x01\x01\x128\n\x07ends_at\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampH\x01R\x06endsAt\x88\x01\x01\x12\x1d\n\ngrant_memo\x18\x0c \x01(\tR\tgrantMemo\x12!\n\x0cemail_events\x18\r \x03(\tR\x0bemailEvents\x12(\n\x10max_grants_total\x18\x0e \x01(\x05R\x0emaxGrantsTotal\x12*\n\x11target_plan_types\x18\x0f \x03(\tR\x0ftargetPlanTypes\x12K\n\x11credit_expires_at\x18\x10 \x01(\x0b2\x1a.google.protobuf.TimestampH\x02R\x0fcreditExpiresAt\x88\x01\x01B\x0c\n\n_starts_atB\n\n\x08_ends_atB\x14\n\x12_credit_expires_at"_\n\x17CreatePromotionResponse\x12D\n\tpromotion\x18\x01 \x01(\x0b2&.textql.rpc.public.promotion.PromotionR\tpromotion"\x86\x06\n\x16UpdatePromotionRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0bdescription\x18\x03 \x01(\tR\x0bdescription\x12%\n\x0eevent_category\x18\x04 \x01(\tR\reventCategory\x12!\n\x0camount_cents\x18\x05 \x01(\x03R\x0bamountCents\x12+\n\x12max_grants_per_org\x18\x06 \x01(\x05R\x0fmaxGrantsPerOrg\x121\n\x15max_grants_per_member\x18\x07 \x01(\x05R\x12maxGrantsPerMember\x12$\n\x0etarget_org_ids\x18\x08 \x03(\tR\x0ctargetOrgIds\x12,\n\x12target_user_groups\x18\t \x03(\tR\x10targetUserGroups\x12\x1b\n\tis_active\x18\n \x01(\x08R\x08isActive\x12<\n\tstarts_at\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampH\x00R\x08startsAt\x88\x01\x01\x128\n\x07ends_at\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampH\x01R\x06endsAt\x88\x01\x01\x12\x1d\n\ngrant_memo\x18\r \x01(\tR\tgrantMemo\x12!\n\x0cemail_events\x18\x0e \x03(\tR\x0bemailEvents\x12(\n\x10max_grants_total\x18\x0f \x01(\x05R\x0emaxGrantsTotal\x12*\n\x11target_plan_types\x18\x10 \x03(\tR\x0ftargetPlanTypes\x12K\n\x11credit_expires_at\x18\x11 \x01(\x0b2\x1a.google.protobuf.TimestampH\x02R\x0fcreditExpiresAt\x88\x01\x01B\x0c\n\n_starts_atB\n\n\x08_ends_atB\x14\n\x12_credit_expires_at"_\n\x17UpdatePromotionResponse\x12D\n\tpromotion\x18\x01 \x01(\x0b2&.textql.rpc.public.promotion.PromotionR\tpromotion"?\n\x1aListPromotionGrantsRequest\x12!\n\x0cpromotion_id\x18\x01 \x01(\tR\x0bpromotionId"b\n\x1bListPromotionGrantsResponse\x12C\n\x06grants\x18\x01 \x03(\x0b2+.textql.rpc.public.promotion.PromotionGrantR\x06grants"(\n\x16DeletePromotionRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x19\n\x17DeletePromotionResponse"\x1c\n\x1aListEventCategoriesRequest"=\n\x1bListEventCategoriesResponse\x12\x1e\n\ncategories\x18\x01 \x03(\tR\ncategories2\x9d\x06\n\x10PromotionService\x12y\n\x0eListPromotions\x122.textql.rpc.public.promotion.ListPromotionsRequest\x1a3.textql.rpc.public.promotion.ListPromotionsResponse\x12|\n\x0fCreatePromotion\x123.textql.rpc.public.promotion.CreatePromotionRequest\x1a4.textql.rpc.public.promotion.CreatePromotionResponse\x12|\n\x0fUpdatePromotion\x123.textql.rpc.public.promotion.UpdatePromotionRequest\x1a4.textql.rpc.public.promotion.UpdatePromotionResponse\x12|\n\x0fDeletePromotion\x123.textql.rpc.public.promotion.DeletePromotionRequest\x1a4.textql.rpc.public.promotion.DeletePromotionResponse\x12\x88\x01\n\x13ListPromotionGrants\x127.textql.rpc.public.promotion.ListPromotionGrantsRequest\x1a8.textql.rpc.public.promotion.ListPromotionGrantsResponse\x12\x88\x01\n\x13ListEventCategories\x127.textql.rpc.public.promotion.ListEventCategoriesRequest\x1a8.textql.rpc.public.promotion.ListEventCategoriesResponseB\x0c\x92\xb5\x18\x08INTERNALb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.promotion_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\x92\xb5\x18\x08INTERNAL'
    _globals['_PROMOTION']._serialized_start = 111
    _globals['_PROMOTION']._serialized_end = 907
    _globals['_PROMOTIONGRANT']._serialized_start = 910
    _globals['_PROMOTIONGRANT']._serialized_end = 1246
    _globals['_LISTPROMOTIONSREQUEST']._serialized_start = 1248
    _globals['_LISTPROMOTIONSREQUEST']._serialized_end = 1271
    _globals['_LISTPROMOTIONSRESPONSE']._serialized_start = 1273
    _globals['_LISTPROMOTIONSRESPONSE']._serialized_end = 1369
    _globals['_CREATEPROMOTIONREQUEST']._serialized_start = 1372
    _globals['_CREATEPROMOTIONREQUEST']._serialized_end = 2130
    _globals['_CREATEPROMOTIONRESPONSE']._serialized_start = 2132
    _globals['_CREATEPROMOTIONRESPONSE']._serialized_end = 2227
    _globals['_UPDATEPROMOTIONREQUEST']._serialized_start = 2230
    _globals['_UPDATEPROMOTIONREQUEST']._serialized_end = 3004
    _globals['_UPDATEPROMOTIONRESPONSE']._serialized_start = 3006
    _globals['_UPDATEPROMOTIONRESPONSE']._serialized_end = 3101
    _globals['_LISTPROMOTIONGRANTSREQUEST']._serialized_start = 3103
    _globals['_LISTPROMOTIONGRANTSREQUEST']._serialized_end = 3166
    _globals['_LISTPROMOTIONGRANTSRESPONSE']._serialized_start = 3168
    _globals['_LISTPROMOTIONGRANTSRESPONSE']._serialized_end = 3266
    _globals['_DELETEPROMOTIONREQUEST']._serialized_start = 3268
    _globals['_DELETEPROMOTIONREQUEST']._serialized_end = 3308
    _globals['_DELETEPROMOTIONRESPONSE']._serialized_start = 3310
    _globals['_DELETEPROMOTIONRESPONSE']._serialized_end = 3335
    _globals['_LISTEVENTCATEGORIESREQUEST']._serialized_start = 3337
    _globals['_LISTEVENTCATEGORIESREQUEST']._serialized_end = 3365
    _globals['_LISTEVENTCATEGORIESRESPONSE']._serialized_start = 3367
    _globals['_LISTEVENTCATEGORIESRESPONSE']._serialized_end = 3428
    _globals['_PROMOTIONSERVICE']._serialized_start = 3431
    _globals['_PROMOTIONSERVICE']._serialized_end = 4228