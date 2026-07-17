"""Unit tests for textql_sdk.utils.retries: the backoff/retry engine shared by every SDK operation."""
import asyncio
import time

import httpx
import pytest

from textql_sdk.utils.retries import (
    BackoffStrategy,
    PermanentError,
    RetryConfig,
    Retries,
    TemporaryError,
    _parse_retry_after_ms_header,  # private but no public equivalent for this helper
    retry,
    retry_async,
)


def _tiny_backoff(**overrides):
    defaults = dict(
        initial_interval=1,
        max_interval=5,
        exponent=1.0,
        max_elapsed_time=2000,
        jitter_ms=0,
    )
    defaults.update(overrides)
    return BackoffStrategy(**defaults)


def _response(status_code, headers=None):
    return httpx.Response(status_code, headers=headers or {})


class TestBackoffStrategyValidation:
    def test_negative_jitter_raises(self):
        with pytest.raises(ValueError):
            BackoffStrategy(
                initial_interval=1, max_interval=5, exponent=1.0, max_elapsed_time=100, jitter_ms=-1
            )

    def test_none_jitter_allowed(self):
        strategy = BackoffStrategy(
            initial_interval=1, max_interval=5, exponent=1.0, max_elapsed_time=100, jitter_ms=None
        )
        assert strategy.jitter_ms is None


class TestRetryStrategyNone:
    def test_none_strategy_calls_once_even_on_error_status(self):
        calls = {"n": 0}

        def do():
            calls["n"] += 1
            return _response(500)

        config = RetryConfig("none", _tiny_backoff(), retry_connection_errors=False)
        result = retry(do, Retries(config, ["500"]))

        assert calls["n"] == 1
        assert result.status_code == 500

    @pytest.mark.asyncio
    async def test_none_strategy_async(self):
        calls = {"n": 0}

        async def do():
            calls["n"] += 1
            return _response(500)

        config = RetryConfig("none", _tiny_backoff(), retry_connection_errors=False)
        result = await retry_async(do, Retries(config, ["500"]))

        assert calls["n"] == 1
        assert result.status_code == 500


class TestRetryBackoffStatusCodes:
    def test_retries_until_success_on_matching_wildcard_code(self):
        responses = iter([_response(500), _response(502), _response(200)])
        calls = {"n": 0}

        def do():
            calls["n"] += 1
            return next(responses)

        config = RetryConfig("backoff", _tiny_backoff(), retry_connection_errors=False)
        result = retry(do, Retries(config, ["5XX"]))

        assert calls["n"] == 3
        assert result.status_code == 200

    def test_does_not_retry_non_matching_status_code(self):
        calls = {"n": 0}

        def do():
            calls["n"] += 1
            return _response(404)

        config = RetryConfig("backoff", _tiny_backoff(), retry_connection_errors=False)
        result = retry(do, Retries(config, ["429", "500"]))

        assert calls["n"] == 1
        assert result.status_code == 404

    def test_literal_status_code_matches_exactly(self):
        responses = iter([_response(429), _response(200)])
        calls = {"n": 0}

        def do():
            calls["n"] += 1
            return next(responses)

        config = RetryConfig("backoff", _tiny_backoff(), retry_connection_errors=False)
        result = retry(do, Retries(config, ["429"]))

        assert calls["n"] == 2
        assert result.status_code == 200

    def test_status_codes_override_takes_precedence(self):
        # status_codes_override should win over the per-operation defaults
        # passed into Retries(config, status_codes).
        responses = iter([_response(403), _response(200)])
        calls = {"n": 0}

        def do():
            calls["n"] += 1
            return next(responses)

        config = RetryConfig(
            "backoff", _tiny_backoff(), retry_connection_errors=False, status_codes_override=["403"]
        )
        retries = Retries(config, ["500"])
        assert retries.status_codes == ["403"]

        result = retry(do, retries)
        # 403 now matches thanks to the override (500 alone would not have
        # triggered a retry), then the second call succeeds.
        assert calls["n"] == 2
        assert result.status_code == 200

    def test_max_elapsed_time_exhausted_returns_last_temporary_response(self):
        def do():
            return _response(500)

        config = RetryConfig(
            "backoff",
            _tiny_backoff(initial_interval=1, max_interval=2, max_elapsed_time=5),
            retry_connection_errors=False,
        )
        result = retry(do, Retries(config, ["500"]))
        # Exhausting max_elapsed_time with an always-failing (but not raising)
        # temporary error should return the last response rather than raise.
        assert result.status_code == 500


class TestRetryConnectionErrors:
    def test_connection_error_propagates_when_not_configured_to_retry(self):
        def do():
            raise httpx.ConnectError("boom")

        config = RetryConfig("backoff", _tiny_backoff(), retry_connection_errors=False)
        with pytest.raises(httpx.ConnectError):
            retry(do, Retries(config, ["500"]))

    def test_connection_error_retried_then_succeeds(self):
        calls = {"n": 0}

        def do():
            calls["n"] += 1
            if calls["n"] < 3:
                raise httpx.ConnectTimeout("boom")
            return _response(200)

        config = RetryConfig("backoff", _tiny_backoff(), retry_connection_errors=True)
        result = retry(do, Retries(config, ["500"]))

        assert calls["n"] == 3
        assert result.status_code == 200

    def test_non_network_exception_is_permanent_and_reraised(self):
        def do():
            raise ValueError("not a network error")

        config = RetryConfig("backoff", _tiny_backoff(), retry_connection_errors=True)
        with pytest.raises(ValueError):
            retry(do, Retries(config, ["500"]))


class TestRetryAfterHeaderParsing:
    def test_seconds_form(self):
        resp = _response(429, headers={"retry-after": "2"})
        assert TemporaryError(resp).retry_after == 2000

    def test_http_date_form(self):
        from email.utils import format_datetime
        from datetime import datetime, timedelta, timezone

        future = datetime.now(timezone.utc) + timedelta(seconds=5)
        resp = _response(429, headers={"retry-after": format_datetime(future)})
        parsed = TemporaryError(resp).retry_after
        assert parsed is not None
        # Allow ±1 s slack for test execution time; 0 would indicate a
        # date-in-past misparse (max(0, negative_delta)), not a valid result.
        assert 4000 <= parsed <= 6000

    def test_missing_header_returns_none(self):
        resp = _response(429)
        assert TemporaryError(resp).retry_after is None

    def test_garbage_header_returns_none(self):
        resp = _response(429, headers={"retry-after": "not-a-date-or-number"})
        assert TemporaryError(resp).retry_after is None

    def test_retry_after_ms_header(self):
        resp = _response(429, headers={"retry-after-ms": "1500"})
        assert _parse_retry_after_ms_header(resp) == 1500

    def test_retry_after_ms_negative_ignored(self):
        resp = _response(429, headers={"retry-after-ms": "-5"})
        assert _parse_retry_after_ms_header(resp) is None

    def test_retry_after_header_takes_priority_over_backoff_shaping(self):
        # A TemporaryError populated with a *positive* retry_after should
        # sleep almost exactly that long regardless of backoff shaping.
        responses = iter([_response(429, headers={"retry-after": "1"}), _response(200)])
        calls = {"n": 0}
        start = time.monotonic()

        def do():
            calls["n"] += 1
            return next(responses)

        config = RetryConfig(
            "backoff",
            _tiny_backoff(initial_interval=5000, max_interval=10000, exponent=2.0),
            retry_connection_errors=False,
        )
        result = retry(do, Retries(config, ["429"]))
        elapsed = time.monotonic() - start

        assert calls["n"] == 2
        assert result.status_code == 200
        # retry-after: 1s means ~1s, not the ~5s big backoff shaping value.
        assert elapsed < 3.0

    def test_retry_after_zero_retries_immediately(self):
        """Retry-After: 0 means retry now — the SDK should honor it with a
        near-zero sleep rather than falling back to backoff shaping."""
        responses = iter([_response(429, headers={"retry-after": "0"}), _response(200)])
        calls = {"n": 0}
        start = time.monotonic()

        def do():
            calls["n"] += 1
            return next(responses)

        config = RetryConfig(
            "backoff",
            _tiny_backoff(initial_interval=5000, max_interval=10000, exponent=1.0),
            retry_connection_errors=False,
        )
        result = retry(do, Retries(config, ["429"]))
        elapsed = time.monotonic() - start

        assert calls["n"] == 2
        assert result.status_code == 200
        # Retry-After: 0 → sleep(0/1000 = 0s), not the 5s backoff value.
        assert elapsed < 0.5


class TestRetryAsyncBackoff:
    @pytest.mark.asyncio
    async def test_retries_until_success(self):
        responses = iter([_response(500), _response(200)])
        calls = {"n": 0}

        async def do():
            calls["n"] += 1
            await asyncio.sleep(0)
            return next(responses)

        config = RetryConfig("backoff", _tiny_backoff(), retry_connection_errors=False)
        result = await retry_async(do, Retries(config, ["5XX"]))

        assert calls["n"] == 2
        assert result.status_code == 200

    @pytest.mark.asyncio
    async def test_connection_error_propagates_when_not_configured(self):
        async def do():
            raise httpx.ConnectError("boom")

        config = RetryConfig("backoff", _tiny_backoff(), retry_connection_errors=False)
        with pytest.raises(httpx.ConnectError):
            await retry_async(do, Retries(config, ["500"]))


class TestPermanentAndTemporaryErrorWrappers:
    def test_permanent_error_wraps_inner(self):
        inner = ValueError("boom")
        err = PermanentError(inner)
        assert err.inner is inner

    def test_temporary_error_extracts_retry_after(self):
        resp = _response(429, headers={"retry-after": "3"})
        err = TemporaryError(resp)
        assert err.retry_after == 3000
        assert err.response is resp
