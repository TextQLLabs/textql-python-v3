"""Create and configure a scheduled playbook.

Playbooks are recurring AI reports. This example exercises the full
update API surface: scheduling, model, output style, Slack/email
delivery, access controls, and concurrency settings.

    uv run python examples/create_playbook.py
"""

import os
from dotenv import load_dotenv
from textql_sdk import Textql
from textql_sdk.models import ConnectError, TextqlRPCPublicPlaybookStringList

load_dotenv()

sdk = Textql(api_key=os.environ["TEXTQL_API_KEY"])

# Step 1: create an empty playbook shell
resp = sdk.playbooks.create_playbook(body={})
if isinstance(resp, ConnectError):
    raise RuntimeError(f"create_playbook failed: {resp}")
assert resp.playbook is not None
playbook_id = resp.playbook.id
assert isinstance(playbook_id, str), "create_playbook returned no playbook ID"
print(f"Playbook created: {playbook_id}")

# Step 2: configure — name, prompt, schedule, model, delivery
update = sdk.playbooks.update(
    playbook_id=playbook_id,
    name="Daily Revenue Report",
    prompt="Summarize yesterday's revenue by product line. Highlight anomalies and week-over-week changes.",
    trigger_type="TRIGGER_TYPE_CRON",
    cron_string="0 9 * * *",            # 9 AM UTC every day
    llm_model="MODEL_SONNET_5",
    slack_channel_id="C04NV2UABCD", # replace with your slack channel ID
    tagged_slack_user_ids=TextqlRPCPublicPlaybookStringList(items=["U03RABC1234"]), # replace with your slack user ID
    email_addresses=TextqlRPCPublicPlaybookStringList(items=["test@textql.com"]), # replace with your email address
)
if isinstance(update, ConnectError):
    raise RuntimeError(f"update failed: {update}")
print(f"Playbook configured: model={update.playbook.llm_model if update.playbook else 'n/a'}  "
      f"cron='{update.playbook.cron_string if update.playbook else 'n/a'}'")

# Step 3: deploy (activates scheduling)
deploy = sdk.playbooks.deploy(playbook_id=playbook_id)
if isinstance(deploy, ConnectError):
    raise RuntimeError(f"deploy failed: {deploy}")
print(f"Playbook deployed — runs daily at 9 AM UTC. ID: {playbook_id}")
