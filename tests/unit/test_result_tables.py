"""Existing SQL results are available only after the asynchronous run finishes."""
import pytest

from tests.conftest import json_response
from textql_sdk import errors, helpers


def sql_cell(*, preview=False, complete=True, error=None):
    return {
        "id": "sql-1", "complete": complete, "execError": error,
        "sqlCell": {"query": "SELECT 42, 12.5, NULL", "dataframe": {
            "df": {"schema": [{"columnName": "answer", "columnType": "int64", "columnIndex": 0}],
                   "records": [{"columns": [{"int64": {"values": [42]}}]}]},
            "preview": preview,
        }},
    }


def test_waits_for_completion_then_returns_existing_typed_tables(make_sdk):
    polls = iter([
        {"running": True, "cursor": "1-0", "generation": "3",
         "events": [{"cell": sql_cell(complete=False)}]},
        {"running": False, "cursor": "2-0", "generation": "3",
         "events": [{"runComplete": {}}]},
    ])
    def handle(req):
        if req.url.path.endswith('/PollChatEvents'):
            return json_response(200, next(polls))
        assert req.url.path.endswith('/GetChatHistory')
        return json_response(200, {"cells": [sql_cell(preview=True)], "hasMore": True})
    bundle = make_sdk(handle)
    tables = helpers.wait_for_tables(bundle.sdk, 'chat-1')
    assert len(tables) == 1
    assert tables[0].preview is True
    assert tables[0].df.records[0].columns[0].int64.values == [42]
    assert helpers.table_rows(tables[0]) == [[42]]
    assert bundle.transport.body_json(1) == {
        "chatId": "chat-1", "resumeCursor": "1-0", "minGeneration": "3"}
    assert bundle.transport.body_json(2) == {"chatId": "chat-1", "limit": 1}


def test_run_error_does_not_return_partial_tables(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {
        "running": False, "events": [{"runError": {"error": "model unavailable"}}]}))
    with pytest.raises(RuntimeError, match='model unavailable'):
        helpers.wait_for_tables(bundle.sdk, 'chat-1')
    assert len(bundle.transport.requests) == 1


@pytest.mark.parametrize('cell', [sql_cell(error='query failed'), sql_cell(complete=False)])
def test_failed_or_unfinished_sql_does_not_look_like_success(make_sdk, cell):
    def handle(req):
        if req.url.path.endswith('/PollChatEvents'):
            return json_response(200, {"running": False, "events": [{"runComplete": {}}]})
        return json_response(200, {"cells": [cell]})
    bundle = make_sdk(handle)
    with pytest.raises(RuntimeError):
        helpers.wait_for_tables(bundle.sdk, 'chat-1')


def test_text_only_completion_returns_no_tables(make_sdk):
    def handle(req):
        if req.url.path.endswith('/PollChatEvents'):
            return json_response(200, {"events": [{"runComplete": {}}]})
        return json_response(200, {"cells": [{"mdCell": {"content": "42"}, "complete": True}]})
    assert helpers.wait_for_tables(make_sdk(handle).sdk, 'chat-1') == []


def test_timeout_does_not_return_incomplete_results(make_sdk, monkeypatch):
    clock = iter([0, 0, 2])
    monkeypatch.setattr(helpers.time, 'monotonic', lambda: next(clock))
    bundle = make_sdk(lambda req: json_response(200, {"running": True}))
    with pytest.raises(TimeoutError):
        helpers.wait_for_tables(bundle.sdk, 'chat-1', timeout=1)


def test_auth_error_is_not_retried_as_a_running_chat(make_sdk):
    bundle = make_sdk(lambda req: json_response(401, {"code": "unauthenticated", "message": "bad key"}))
    with pytest.raises(errors.TextqlDefaultError, match='bad key'):
        helpers.wait_for_tables(bundle.sdk, 'chat-1')
    assert len(bundle.transport.requests) == 1



def test_decimal_rows_keep_all_digits_and_budget_exhaustion_is_empty():
    from decimal import Decimal
    from textql_sdk.models import TextqlRPCPublicDataframeDataFrameWithInfo as Table
    table = Table.model_validate({"df": {
        "schema": [{"columnName": "id", "columnType": "decimal128"}],
        "records": [{"columns": [{"strings": {"values": ["9007199254740993.25"]}}]}],
    }})
    assert helpers.table_rows(table) == [[Decimal("9007199254740993.25")]]
    assert helpers.table_rows(Table(preview=True)) == []
