"""Fixtures for the integration test suite."""
import os
import uuid

import pytest

from textql_sdk import Textql

API_KEY_ENV = "TEXTQL_API_KEY"
SERVER_URL_ENV = "TEXTQL_TEST_SERVER_URL"


def _require_live_server():
    api_key = os.getenv(API_KEY_ENV)
    server_url = os.getenv(SERVER_URL_ENV)
    if not api_key or not server_url:
        pytest.skip(
            f"integration tests require {API_KEY_ENV} and {SERVER_URL_ENV} to be set "
            "to point at a real (non-production) TextQL API server -- see tests/README.md"
        )
    return api_key, server_url


def pytest_collection_modifyitems(config, items):
    for item in items:
        if "integration" in str(item.fspath):
            item.add_marker(pytest.mark.integration)


@pytest.fixture(scope="session")
def live_server_config():
    return _require_live_server()


@pytest.fixture
def live_sdk(live_server_config):
    api_key, server_url = live_server_config
    with Textql(api_key=api_key, server_url=server_url, timeout_ms=30_000) as sdk:
        yield sdk


@pytest.fixture
async def live_sdk_async(live_server_config):
    api_key, server_url = live_server_config
    async with Textql(api_key=api_key, server_url=server_url, timeout_ms=30_000) as sdk:
        yield sdk


@pytest.fixture
def cleanup():
    """Stack of zero-arg teardown callbacks, run LIFO after the test regardless
    of pass/fail. Usage: cleanup.add(lambda: live_sdk.agents.delete(agent_id=x))"""

    callbacks = []

    class _Cleanup:
        def add(self, fn):
            callbacks.append(fn)

    yield _Cleanup()

    errors = []
    while callbacks:
        fn = callbacks.pop()
        try:
            fn()
        except Exception as e:  # noqa: BLE001 -- best-effort teardown
            errors.append(e)

    if errors:
        # Don't hide a real assertion failure behind a teardown error, but
        # do surface leaked-resource cleanup problems loudly.
        raise RuntimeError(f"{len(errors)} error(s) during integration test cleanup: {errors}")


@pytest.fixture
def unique_name():
    """Unique name/prefix for resources this test creates, to avoid
    collisions and make leaked resources easy to spot."""
    return f"sdk-test-{uuid.uuid4().hex[:10]}"
