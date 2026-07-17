"""Integration tests: full Agents CRUD lifecycle against a REAL TextQL API server."""
import pytest

pytestmark = pytest.mark.integration


class TestAgentLifecycle:
    def test_create_get_update_delete_roundtrip(self, live_sdk, cleanup, unique_name):
        create_resp = live_sdk.agents.create(
            name=unique_name,
            prompt="You are a helpful test agent created by the SDK integration suite.",
        )
        assert create_resp.agent is not None
        agent_id = create_resp.agent.id
        assert agent_id

        cleanup.add(lambda: live_sdk.agents.delete(agent_id=agent_id))

        got = live_sdk.agents.get_agent(agent_id=agent_id)
        assert got.agent is not None
        assert got.agent.id == agent_id
        assert got.agent.name == unique_name

        updated_name = unique_name + "-updated"
        live_sdk.agents.update(agent_id=agent_id, name=updated_name)

        refetched = live_sdk.agents.get_agent(agent_id=agent_id)
        assert refetched.agent.name == updated_name

    def test_list_includes_newly_created_agent(self, live_sdk, cleanup, unique_name):
        create_resp = live_sdk.agents.create(name=unique_name, prompt="test")
        agent_id = create_resp.agent.id
        cleanup.add(lambda: live_sdk.agents.delete(agent_id=agent_id))

        listing = live_sdk.agents.list(include_inactive=True, include_all_org=False)
        ids = [a.id for a in (listing.agents or [])]
        assert agent_id in ids

    def test_duplicate_creates_independent_copy(self, live_sdk, cleanup, unique_name):
        original = live_sdk.agents.create(name=unique_name, prompt="original prompt")
        original_id = original.agent.id
        cleanup.add(lambda: live_sdk.agents.delete(agent_id=original_id))

        dup = live_sdk.agents.duplicate(agent_id=original_id)
        dup_id = dup.agent.id
        assert dup_id != original_id
        cleanup.add(lambda: live_sdk.agents.delete(agent_id=dup_id))

        # Mutating the duplicate must not affect the original.
        live_sdk.agents.update(agent_id=dup_id, name=unique_name + "-dup-renamed")
        refetched_original = live_sdk.agents.get_agent(agent_id=original_id)
        assert refetched_original.agent.name == unique_name

    def test_delete_is_idempotent_or_errors_cleanly_on_second_call(self, live_sdk, unique_name):
        from textql_sdk import errors

        create_resp = live_sdk.agents.create(name=unique_name, prompt="test")
        agent_id = create_resp.agent.id

        live_sdk.agents.delete(agent_id=agent_id)

        # Second delete of an already-deleted agent: the SDK should surface
        # this as a clean TextqlDefaultError (4xx), not hang or raise an
        # unrelated exception type.
        with pytest.raises(errors.TextqlDefaultError) as exc_info:
            live_sdk.agents.delete(agent_id=agent_id)
        assert 400 <= exc_info.value.status_code < 500

    @pytest.mark.asyncio
    async def test_async_create_and_get(self, live_sdk_async, cleanup, unique_name):
        create_resp = await live_sdk_async.agents.create_async(name=unique_name, prompt="async test")
        agent_id = create_resp.agent.id
        cleanup.add(lambda: live_sdk_async.agents.delete(agent_id=agent_id))

        got = await live_sdk_async.agents.get_agent_async(agent_id=agent_id)
        assert got.agent.id == agent_id


class TestAgentRunsLifecycle:
    def test_trigger_and_list_runs(self, live_sdk, cleanup, unique_name):
        create_resp = live_sdk.agents.create(name=unique_name, prompt="Say hello.")
        agent_id = create_resp.agent.id
        cleanup.add(lambda: live_sdk.agents.delete(agent_id=agent_id))

        trigger_resp = live_sdk.agents.trigger_agent(agent_id=agent_id)
        assert trigger_resp is not None

        runs = live_sdk.agents.list_runs(agent_id=agent_id, limit=10, offset=0)
        assert runs.runs is not None

        if runs.runs:
            run_id = runs.runs[0].id
            single_run = live_sdk.agents.get_run(run_id=run_id)
            assert single_run is not None

    def test_list_runs_pagination_edge_values(self, live_sdk, cleanup, unique_name):
        """Push pagination params to their boundaries against a real server
        to see how it actually behaves (the SDK itself does zero client-side
        validation on these -- see tests/unit/test_agents_service.py)."""
        create_resp = live_sdk.agents.create(name=unique_name, prompt="test")
        agent_id = create_resp.agent.id
        cleanup.add(lambda: live_sdk.agents.delete(agent_id=agent_id))

        # limit=0 should return an empty page, not error and not "all rows".
        zero_limit = live_sdk.agents.list_runs(agent_id=agent_id, limit=0, offset=0)
        assert not zero_limit.runs

        # Negative offset: confirm the server rejects it cleanly (4xx) rather
        # than the SDK crashing with an unrelated exception, OR that it's
        # treated as 0 -- either is acceptable, an unhandled 500/timeout is not.
        from textql_sdk import errors

        try:
            live_sdk.agents.list_runs(agent_id=agent_id, limit=10, offset=-1)
        except errors.TextqlDefaultError as e:
            assert e.status_code < 500, "negative offset should not cause a server-side crash"
