"""Create an agent and trigger it.

Agents are persistent AI assistants configured with a system prompt.
Triggering an agent generates a fresh report based on its prompt.

    uv run python examples/create_agent.py
"""

import os
from dotenv import load_dotenv
from textql_sdk import Textql
from textql_sdk.models import ConnectError, SQL, TextqlRPCPublicParadigmSQLOptions

load_dotenv()
sdk = Textql(api_key=os.environ["TEXTQL_API_KEY"])

# Create the agent
resp = sdk.agents.create(
    name="Weekly Revenue Summary",
    prompt="Summarize total revenue by region for the past 7 days.",
    posting_frequency_crons=["0 9 * * *"], # Run every day at 9 AM UTC
    paradigm_options=SQL(sql=TextqlRPCPublicParadigmSQLOptions(
        connector_ids=[1234, 5678],  # replace with your connector IDs
    ))
)
if isinstance(resp, ConnectError):
    raise RuntimeError(f"create agent failed: {resp}")
assert resp.agent is not None
agent_id = resp.agent.id
assert isinstance(agent_id, str), "create_agent returned no agent ID"
print(f"Agent created: {agent_id}")

# Trigger a run (generates a new report)
trigger = sdk.agents.trigger_agent(agent_id=agent_id)
if isinstance(trigger, ConnectError):
    raise RuntimeError(f"trigger_agent failed: {trigger}")
print("Agent triggered — check the TextQL UI for the report.")

# List recent runs
runs = sdk.agents.list_runs(agent_id=agent_id)
if isinstance(runs, ConnectError):
    raise RuntimeError(f"list_runs failed: {runs}")
print(f"\nRecent runs: {len(runs.runs or [])} run(s)")
for run in (runs.runs or [])[:3]:
    print(f"  {run.id}  status={run.status}")

# Clean up
sdk.agents.delete(agent_id=agent_id)
print(f"\nAgent {agent_id} deleted.")
