"""Run only against a disposable org with a SQL fixture connector (never customer data)."""
import json
import os
import uuid

from textql_sdk import Textql

import pytest

from textql_sdk.helpers import table_rows, wait_for_tables
from textql_sdk.models import ConnectError


def result_table(sdk, sql):
    connector = int(os.environ["TEXTQL_SQL_CONNECTOR_ID"])
    result = sdk.chats.query_one_shot(
        question=f"Run exactly this SQL with connector {connector}: {sql}. Use SQL once. Do not use Python. Then stop.",
        model=os.environ.get("TEXTQL_SQL_MODEL", "MODEL_GPT_6_1_SOL"),
        paradigm={"type": "TYPE_UNIVERSAL", "version": 1, "options": {
            "universal": {"sqlEnabled": True, "connectorIds": [connector]}}},
    )
    assert not isinstance(result, ConnectError)
    tables = wait_for_tables(sdk, result.chat_id, timeout=120)
    assert len(tables) == 1
    return tables[0], result.chat_id


def test_sql_result_numbers_and_null(live_sdk, live_server_config, cleanup):
    table, chat_id = result_table(live_sdk, "SELECT 42 AS answer, 12.5 AS amount, NULL AS missing")
    rows = table_rows(table)
    assert rows == [[42, 12.5, None]]
    assert type(rows[0][0]) is int
    assert type(rows[0][1]) is float
    assert table.preview is not True
    # A reader may see the chat, but cannot obtain its typed rows by copying it.
    role = live_sdk.rbac.create_role(name="sql-reader-" + uuid.uuid4().hex).role
    cleanup.add(lambda: live_sdk.rbac.delete_role(role_id=role.id))
    for permission in ({"chat": "CHAT_ACTION_READ"}, {"chat": "CHAT_ACTION_WRITE"},
                       {"connector": "CONNECTOR_ACTION_READ"}):
        live_sdk.rbac.assign_permission_to_role(role_id=role.id, permission=permission)
    member = live_sdk.rbac.create_service_account(name="sql-reader", role_ids=[role.id])
    cleanup.add(lambda: live_sdk.rbac.delete_service_account(member_id=member.member_id))
    key = live_sdk.rbac.create_service_account_api_key(
        service_account_member_id=member.member_id, assumed_roles=[role.id], expiry_seconds=600)
    cleanup.add(lambda: live_sdk.rbac.revoke_api_key(api_key_id=key.api_key.id))
    live_sdk.rbac.share_object(object_type="chat", object_id=chat_id,
                              member_id=member.member_id, access_type="viewer")
    connector = os.environ["TEXTQL_SQL_CONNECTOR_ID"]
    live_sdk.rbac.share_object_with_role(object_type="connector", object_id=connector,
                                       role_id=role.id, access_type="viewer")
    with Textql(api_key=key.api_key_secret, server_url=live_server_config[1]) as peer:
        for target in (chat_id, peer.chats.duplicate_chat(chat_id=chat_id).chat.id):
            history = peer.chats.get_history(chat_id=target)
            tables = [cell.sql_cell.dataframe for cell in history.cells or []
                      if getattr(cell, "sql_cell", None)]
            assert tables and all(result.df is None for result in tables)


@pytest.mark.parametrize("sql, expected", [
    ("SELECT x FROM UNNEST(GENERATE_ARRAY(1, 101)) AS x ORDER BY x", 100),
    ("SELECT REPEAT('x', 70000) AS wide", 0),
])
def test_sql_result_cap(live_sdk, sql, expected):
    table, _ = result_table(live_sdk, sql)
    assert table.df is not None
    assert len(table_rows(table)) == expected
    assert table.preview is True
    assert len(json.dumps(table.model_dump(exclude_none=True)).encode()) <= 65536
