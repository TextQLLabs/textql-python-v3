"""Integration tests: Connectors service against a REAL TextQL API server."""
import os

import pytest

pytestmark = pytest.mark.integration

TEST_CONNECTOR_ID_ENV = "TEXTQL_TEST_CONNECTOR_ID"


@pytest.fixture
def existing_connector_id():
    connector_id = os.getenv(TEST_CONNECTOR_ID_ENV)
    if not connector_id:
        pytest.skip(
            f"set {TEST_CONNECTOR_ID_ENV} to a real, working connector id in your "
            "target org to run connector read/query integration tests"
        )
    return int(connector_id)


class TestConnectorReadOnly:
    def test_get_connectors_returns_a_list(self, live_sdk):
        resp = live_sdk.connectors.get_connectors()
        assert resp is not None

    def test_get_specific_connector(self, live_sdk, existing_connector_id):
        resp = live_sdk.connectors.get(connector_id=existing_connector_id)
        assert resp is not None

    def test_list_tables(self, live_sdk, existing_connector_id):
        resp = live_sdk.connectors.list_tables(connector_id=existing_connector_id)
        assert resp is not None

    def test_test_connection_succeeds_for_known_good_connector(self, live_sdk, existing_connector_id):
        resp = live_sdk.connectors.test(connector_id=existing_connector_id)
        assert resp is not None


class TestExecuteQuery:
    def test_simple_select_returns_rows(self, live_sdk, existing_connector_id):
        resp = live_sdk.connectors.execute_query(
            connector_id=existing_connector_id, query="SELECT 1 AS one"
        )
        assert resp is not None

    def test_query_with_special_characters_and_unicode(self, live_sdk, existing_connector_id):
        resp = live_sdk.connectors.execute_query(
            connector_id=existing_connector_id,
            query="SELECT 'héllo \"world\" \\n ☃' AS greeting",
        )
        assert resp is not None

    def test_empty_query_string_errors_cleanly(self, live_sdk, existing_connector_id):
        from textql_sdk import errors

        with pytest.raises(errors.TextqlDefaultError) as exc_info:
            live_sdk.connectors.execute_query(connector_id=existing_connector_id, query="")
        assert exc_info.value.status_code < 500

    def test_malformed_sql_errors_cleanly_not_as_500(self, live_sdk, existing_connector_id):
        from textql_sdk import errors

        with pytest.raises(errors.TextqlDefaultError) as exc_info:
            live_sdk.connectors.execute_query(
                connector_id=existing_connector_id, query="SELEKT this is not valid sql !!!"
            )
        assert exc_info.value.status_code < 500, (
            "a malformed query should be reported as a client-facing error, "
            "not surfaced as an unhandled server crash"
        )

    def test_limit_zero_returns_no_rows(self, live_sdk, existing_connector_id):
        resp = live_sdk.connectors.execute_query(
            connector_id=existing_connector_id, query="SELECT 1", limit=0
        )
        assert resp is not None

    @pytest.mark.asyncio
    async def test_async_execute_query(self, live_sdk_async, existing_connector_id):
        resp = await live_sdk_async.connectors.execute_query_async(
            connector_id=existing_connector_id, query="SELECT 1"
        )
        assert resp is not None


class TestConnectorErrorPaths:
    def test_nonexistent_connector_id_raises_client_error(self, live_sdk):
        from textql_sdk import errors

        with pytest.raises(errors.TextqlDefaultError) as exc_info:
            live_sdk.connectors.get(connector_id=999_999_999)
        assert 400 <= exc_info.value.status_code < 500
