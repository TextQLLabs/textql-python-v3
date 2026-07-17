"""Unit tests for textql_sdk.errors -- the exception hierarchy raised for non-2xx responses and validation failures."""
import httpx
import pytest

from textql_sdk import errors


def _response(status_code=500, text="", headers=None):
    hdrs = {"content-type": "application/json"}
    if headers:
        hdrs.update(headers)
    return httpx.Response(status_code, content=text, headers=hdrs)


class TestTextqlError:
    def test_extracts_fields_from_response(self):
        resp = _response(status_code=404, text='{"message": "nope"}')
        err = errors.TextqlError("Not found", resp)

        assert err.message == "Not found"
        assert err.status_code == 404
        assert err.body == '{"message": "nope"}'
        assert err.headers is resp.headers
        assert err.raw_response is resp

    def test_explicit_body_overrides_response_text(self):
        resp = _response(status_code=500, text="actual body")
        err = errors.TextqlError("boom", resp, body="explicit body")
        assert err.body == "explicit body"

    def test_str_returns_message(self):
        resp = _response()
        err = errors.TextqlError("custom message", resp)
        assert str(err) == "custom message"

    def test_is_hashable(self):
        # `@dataclass(unsafe_hash=True)` -- confirm instances can go in a set.
        resp = _response()
        err = errors.TextqlError("m", resp)
        {err}  # must not raise


class TestTextqlDefaultError:
    def test_message_includes_status_code(self):
        resp = _response(status_code=503, text="service down")
        err = errors.TextqlDefaultError("API error occurred", resp)
        assert "Status 503" in err.message
        assert "service down" in err.message

    def test_message_includes_non_json_content_type(self):
        resp = _response(status_code=500, text="oops", headers={"content-type": "text/plain"})
        err = errors.TextqlDefaultError("API error occurred", resp)
        assert "Content-Type" in err.message
        assert "text/plain" in err.message

    def test_message_omits_content_type_note_for_json(self):
        resp = _response(status_code=500, text='{"a": 1}', headers={"content-type": "application/json"})
        err = errors.TextqlDefaultError("API error occurred", resp)
        assert "Content-Type" not in err.message

    def test_content_type_with_space_is_quoted(self):
        resp = _response(
            status_code=500,
            text="oops",
            headers={"content-type": "text/plain; charset=utf-8"},
        )
        err = errors.TextqlDefaultError("API error occurred", resp)
        assert '"text/plain; charset=utf-8"' in err.message

    def test_empty_body_displays_as_empty_string_literal(self):
        resp = _response(status_code=500, text="")
        err = errors.TextqlDefaultError("API error occurred", resp)
        assert 'Body: ""' in err.message

    def test_long_body_is_truncated(self):
        huge_body = "x" * 20_000
        resp = _response(status_code=500, text=huge_body)
        err = errors.TextqlDefaultError("API error occurred", resp)

        assert "...and 10000 more chars" in err.message
        # The truncated prefix (10_000 chars) should appear in the message.
        assert "x" * 10_000 in err.message
        # But the full 20_000-char body should NOT appear verbatim.
        assert huge_body not in err.message

    def test_body_at_exactly_max_length_is_not_truncated(self):
        body = "x" * 10_000
        resp = _response(status_code=500, text=body)
        err = errors.TextqlDefaultError("API error occurred", resp)
        assert "more chars" not in err.message

    def test_empty_message_prefix_has_no_leading_colon(self):
        resp = _response(status_code=500, text="body")
        err = errors.TextqlDefaultError("", resp)
        assert not err.message.startswith(":")
        assert err.message.startswith("Status 500")

    def test_explicit_body_used_over_response_text(self):
        resp = _response(status_code=500, text="raw response text")
        err = errors.TextqlDefaultError("msg", resp, body="explicit body wins")
        assert "explicit body wins" in err.message
        assert "raw response text" not in err.message


class TestResponseValidationError:
    def test_cause_property_returns_dunder_cause(self):
        resp = _response(status_code=200, text="not json{{{")
        original = ValueError("invalid json")
        try:
            try:
                raise original
            except ValueError as e:
                raise errors.ResponseValidationError("Response validation failed", resp, e) from e
        except errors.ResponseValidationError as rve:
            assert rve.cause is original
            assert "invalid json" in str(rve)

    def test_message_includes_cause(self):
        resp = _response()
        cause = TypeError("bad type")
        err = errors.ResponseValidationError("Response validation failed", resp, cause)
        assert "bad type" in err.message


class TestNoResponseError:
    def test_default_message(self):
        err = errors.NoResponseError()
        assert str(err) == "No response received"

    def test_custom_message(self):
        err = errors.NoResponseError("custom")
        assert str(err) == "custom"
        assert err.message == "custom"
