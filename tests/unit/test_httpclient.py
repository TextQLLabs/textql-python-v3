"""Unit tests for textql_sdk.httpclient -- HttpClient/AsyncHttpClient protocols and the close_clients finalizer."""
import httpx
import pytest

from textql_sdk.httpclient import AsyncHttpClient, HttpClient, close_clients


class TestProtocolConformance:
    def test_httpx_client_satisfies_http_client_protocol(self):
        client = httpx.Client()
        try:
            assert isinstance(client, HttpClient)
        finally:
            client.close()

    def test_httpx_async_client_satisfies_async_http_client_protocol(self):
        client = httpx.AsyncClient()
        assert isinstance(client, AsyncHttpClient)

    def test_arbitrary_object_does_not_satisfy_protocol(self):
        assert not isinstance(object(), HttpClient)
        assert not isinstance(object(), AsyncHttpClient)


class _FakeOwner:
    def __init__(self, client, async_client):
        self.client = client
        self.async_client = async_client


class TestCloseClients:
    def test_owned_sync_client_is_closed_and_unset(self):
        client = httpx.Client()
        owner = _FakeOwner(client=client, async_client=None)

        close_clients(owner, client, sync_client_supplied=False, async_client=None, async_client_supplied=False)

        assert owner.client is None
        assert client.is_closed

    def test_supplied_sync_client_is_not_closed_but_unset(self):
        client = httpx.Client()
        owner = _FakeOwner(client=client, async_client=None)

        close_clients(owner, client, sync_client_supplied=True, async_client=None, async_client_supplied=True)

        assert owner.client is None
        assert not client.is_closed
        client.close()

    def test_close_is_best_effort_and_swallows_exceptions(self):
        class ExplodingClient:
            def close(self):
                raise RuntimeError("already closed")

        client = ExplodingClient()
        owner = _FakeOwner(client=client, async_client=None)

        # Must not raise even though close() throws.
        close_clients(owner, client, sync_client_supplied=False, async_client=None, async_client_supplied=False)
        assert owner.client is None

    def test_none_clients_are_a_no_op(self):
        owner = _FakeOwner(client=None, async_client=None)
        close_clients(owner, None, sync_client_supplied=False, async_client=None, async_client_supplied=False)
        assert owner.client is None
        assert owner.async_client is None

    @pytest.mark.asyncio
    async def test_owned_async_client_is_scheduled_for_close_within_running_loop(self):
        async_client = httpx.AsyncClient()
        owner = _FakeOwner(client=None, async_client=async_client)

        close_clients(owner, None, sync_client_supplied=False, async_client=async_client, async_client_supplied=False)

        assert owner.async_client is None
        # Give the scheduled aclose() coroutine a chance to run before the
        # test process exits, to avoid "coroutine was never awaited" noise.
        import asyncio

        await asyncio.sleep(0)
