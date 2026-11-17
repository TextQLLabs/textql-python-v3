"""Run only against a disposable org with a SQL fixture connector (never customer data)."""
import json
import os

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
    return tables[0]


def test_sql_result_numbers_and_null(live_sdk):
    table = result_table(live_sdk, "SELECT 42 AS answer, 12.5 AS amount, NULL AS missing")
    rows = table_rows(table)
    assert rows == [[42, 12.5, None]]
    assert type(rows[0][0]) is int
    assert type(rows[0][1]) is float
    assert table.preview is not True


@pytest.mark.parametrize("sql, expected", [
    ("SELECT x FROM UNNEST(GENERATE_ARRAY(1, 101)) AS x ORDER BY x", 100),
    ("SELECT REPEAT('x', 70000) AS wide", 0),
])
def test_sql_result_cap(live_sdk, sql, expected):
    table = result_table(live_sdk, sql)
    assert table.df is not None
    assert len(table_rows(table)) == expected
    assert table.preview is True
    assert len(json.dumps(table.model_dump(exclude_none=True)).encode()) <= 65536
