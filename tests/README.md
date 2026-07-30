# textql_sdk test suite

Pytest suite for the `textql_sdk` Python client, two layers:

- **`tests/unit/`** — fully mocked, no network I/O. Every service operation
  (all 22 services) plus the shared request/retry/hooks/error/serialization core.
- **`tests/integration/`** — real network calls against a live TextQL API
  server. Opt-in, skipped by default.

## Setup

Either package manager works.

```bash
# pip
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -e .
pip install pytest pytest-asyncio pytest-xdist

# uv
uv venv --python 3.11        # first time only
uv sync --group dev
```

## Running unit tests (fast, safe, no credentials needed)

Under pip, activate the venv and run `pytest` directly; under uv, prefix with
`uv run`. The rest of this doc shows the `uv run` form.

```bash
uv run pytest tests/unit -v
uv run pytest tests/unit -n auto           # parallelized across CPU cores (pytest-xdist)
uv run pytest tests/unit/test_agents_service.py -v   # a single service
```

No network I/O — every `Textql` instance here uses a mock `httpx` transport
(`tests/conftest.py`) that records requests and returns scripted responses.

## Running integration tests (real server, opt-in)

Skipped automatically unless both env vars below are set — there's no
fallback to the SDK's built-in production server, since these tests create
and delete real resources.

```bash
export TEXTQL_API_KEY=<a real API key for a non-production org>
export TEXTQL_TEST_SERVER_URL=http://localhost:8080   # wherever your compute-engine listens

uv run pytest tests/integration -v
```

To point at the demo2 local dev stack, start it from the demo2 repo first
(e.g. `sudo docker-compose -f compose.dev.yml --env-file .env.development up --build compute-engine`,
or via mprocs.yaml/Tiltfile).

A few tests need pre-existing fixtures that can't be safely provisioned from
scratch (a real connector, a real dataset) — skipped individually unless set:

```bash
export TEXTQL_TEST_CONNECTOR_ID=123
export TEXTQL_TEST_DATASET_ID=<uuid>
```

**Note:** these were written directly against the SDK's model shapes but not
executed against a live server (none was reachable while writing this suite)
— treat a first run as a validation pass.

## Current status

```
uv run pytest tests/ -q -n auto
# 2349 passed, 48 skipped (integration tests skip without live-server credentials)
```

55 unit test files covering all 22 SDK services (~450 operations, sync +
async) plus 8 core-infra files (retries, errors, security, hooks, request
building, serialization, sdk lifecycle, httpclient). 6 integration test
files (opt-in, real network) + shared fixtures.

## Layout

```
tests/
  conftest.py                    # shared mock-transport harness for unit tests
  unit/
    test_harness_smoke.py        # sanity-checks the harness itself
    test_sdk_init.py             # Textql() constructor, lazy sub-SDK loading, context manager lifecycle
    test_basesdk_request_building.py  # BaseSDK._build_request / do_request core, headers, timeouts, retries
    test_retries.py              # utils.retries: backoff, Retry-After parsing, connection-error handling
    test_errors.py               # TextqlError / TextqlDefaultError / ResponseValidationError / NoResponseError
    test_security.py             # Security model + auth header derivation
    test_hooks.py                # SDKHooks before_request/after_success/after_error chains
    test_utils_serialization.py  # marshal/unmarshal, match_response, query params, url templating
    test_httpclient.py           # HttpClient/AsyncHttpClient protocols, close_clients finalizer
    test_<service>_service.py / test_<service>_*.py   # per-service operation coverage (22 services)
  integration/
    conftest.py                  # live_sdk / live_sdk_async / cleanup / unique_name fixtures, skip guard
    test_agents_lifecycle.py
    test_chats_lifecycle.py
    test_connectors_lifecycle.py
    test_datasets_lifecycle.py
    test_error_handling.py       # bad auth, malformed payloads, timeouts, unreachable hosts
    test_concurrency.py          # concurrent async/thread-pool load against one SDK instance
```

## Suspected real SDK bugs found

Not fixed in `src/` (generated code — see `CONTRIBUTING.md`). Each is pinned
by a passing test documenting the actual behavior.

1. `utils/retries.py` — `Retry-After: 0` is ignored (strict `> 0` check), so
   the SDK falls back to full backoff shaping instead of retrying instantly.
   `test_retries.py::test_retry_after_zero_falls_back_to_backoff_shaping_bug`
2. `models/security.py` — `Security.serialize_model`'s None-omission checks
   alias `"apiKey"`, but the field has no alias (real key `"api_key"`), so
   `None` is never actually omitted. Harmless today (headers are built from
   the Python attribute directly), but latent.
   `test_security.py::test_model_dump_none_api_key_is_not_actually_omitted_bug`
3. `basesdk.py` — `http_headers={"accept": ...}` (lowercase) doesn't cleanly
   override the SDK's own `"Accept"`; both survive in a plain dict and httpx
   merges them into one comma-joined value.
   `test_basesdk_request_building.py::test_http_headers_with_different_case_does_not_override_bug`
4. `observability.py` `export_csv` — the 200 branch only matches
   `application/json`; a real `text/csv` response would raise
   `TextqlDefaultError` despite succeeding. Worth confirming against the real API.
5. Cosmetic: some library-service models set `request_has_query_params=True`
   for a field that's actually sent as a header; `get_ontology_usage_summary`'s
   `observation_period` serializes as ISO-8601 duration, not the `"90s"`
   format its docstring describes — round-trips fine either way.

No other genuine bugs found across the ~450 operations covered.
