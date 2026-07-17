"""Integration tests probing the SDK under concurrent load against a REAL TextQL API server."""
import asyncio
import concurrent.futures

import pytest

pytestmark = pytest.mark.integration

N_CONCURRENT = 20


class TestAsyncConcurrency:
    @pytest.mark.asyncio
    async def test_many_concurrent_async_requests_on_one_client(self, live_sdk_async):
        """A single Textql instance's async_client is a single httpx
        connection pool -- confirm N concurrent calls all complete correctly
        rather than one silently reusing/corrupting another's response."""
        results = await asyncio.gather(
            *(live_sdk_async.agents.list_async(include_inactive=True) for _ in range(N_CONCURRENT)),
            return_exceptions=True,
        )

        errors = [r for r in results if isinstance(r, BaseException)]
        assert not errors, f"{len(errors)}/{N_CONCURRENT} concurrent async requests raised: {errors[:3]}"

    @pytest.mark.asyncio
    async def test_concurrent_create_and_delete_do_not_interfere(self, live_sdk_async, unique_name):
        """Interleave creates and deletes across many agents concurrently
        and confirm each create's response corresponds to its own request
        (i.e. no cross-talk between concurrently in-flight requests sharing
        one httpx.AsyncClient)."""

        async def create_and_verify(i):
            name = f"{unique_name}-{i}"
            resp = await live_sdk_async.agents.create_async(name=name, prompt="concurrency test")
            assert resp.agent.name == name, "response for one request returned another request's data"
            return resp.agent.id

        agent_ids = await asyncio.gather(*(create_and_verify(i) for i in range(N_CONCURRENT)))
        assert len(set(agent_ids)) == N_CONCURRENT, "expected N distinct agent ids, got collisions"

        await asyncio.gather(*(live_sdk_async.agents.delete_async(agent_id=aid) for aid in agent_ids))


class TestSyncConcurrencyAcrossThreads:
    def test_many_threads_sharing_one_sync_client(self, live_sdk):
        """httpx.Client is documented as thread-safe for concurrent .send()
        calls -- confirm the SDK doesn't break that guarantee (e.g. via
        shared mutable state in BaseSDK/SDKConfiguration read during request
        building)."""

        def call():
            return live_sdk.agents.list(include_inactive=True)

        with concurrent.futures.ThreadPoolExecutor(max_workers=N_CONCURRENT) as pool:
            futures = [pool.submit(call) for _ in range(N_CONCURRENT)]
            results = []
            errors = []
            for f in concurrent.futures.as_completed(futures):
                try:
                    results.append(f.result())
                except Exception as e:  # noqa: BLE001
                    errors.append(e)

        assert not errors, f"{len(errors)}/{N_CONCURRENT} threaded requests raised: {errors[:3]}"
        assert len(results) == N_CONCURRENT
