"""Unit tests for low-level textql_sdk.utils helpers: marshal/unmarshal, response matching, query params, URL templating."""
from typing import List, Optional

import httpx
import pytest
from pydantic import Field
from typing_extensions import Annotated

from textql_sdk import errors
from textql_sdk.types import BaseModel
from textql_sdk.utils.metadata import FieldMetadata, QueryParamMetadata
from textql_sdk.utils.queryparams import get_query_params
from textql_sdk.utils.requestbodies import serialize_request_body
from textql_sdk.utils.serializers import marshal_json, unmarshal, unmarshal_json
from textql_sdk.utils.unmarshal_json_response import unmarshal_json_response
from textql_sdk.utils.url import generate_url, remove_suffix, template_url
from textql_sdk.utils.values import match_content_type, match_response, match_status_codes


class _SamplePayload(BaseModel):
    name: str
    count: int


class _QueryModel(BaseModel):
    q: Annotated[Optional[str], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    tags: Annotated[Optional[List[str]], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    no_metadata_field: Optional[str] = None


class TestMarshalUnmarshalJson:
    def test_round_trips_a_simple_model(self):
        raw = marshal_json(_SamplePayload(name="a", count=1), _SamplePayload)
        restored = unmarshal_json(raw, _SamplePayload)
        assert restored == _SamplePayload(name="a", count=1)

    def test_unmarshal_coerces_dict_into_model(self):
        result = unmarshal({"name": "b", "count": 2}, _SamplePayload, coerce_iterables=False)
        assert isinstance(result, _SamplePayload)
        assert result.name == "b"
        assert result.count == 2

    def test_unmarshal_wrong_shape_raises(self):
        with pytest.raises(Exception):
            unmarshal_json('{"name": "x"}', _SamplePayload)  # missing required `count`


class TestUnmarshalJsonResponse:
    def test_valid_response_unmarshals(self):
        resp = httpx.Response(200, json={"name": "ok", "count": 5})
        result = unmarshal_json_response(_SamplePayload, resp)
        assert result == _SamplePayload(name="ok", count=5)

    def test_invalid_json_raises_response_validation_error(self):
        resp = httpx.Response(200, content="not json at all {{{")
        with pytest.raises(errors.ResponseValidationError) as exc_info:
            unmarshal_json_response(_SamplePayload, resp)
        assert exc_info.value.raw_response is resp

    def test_wrong_shape_json_raises_response_validation_error(self):
        resp = httpx.Response(200, json={"name": "ok"})  # missing `count`
        with pytest.raises(errors.ResponseValidationError):
            unmarshal_json_response(_SamplePayload, resp)

    def test_explicit_body_overrides_response_text(self):
        resp = httpx.Response(200, json={"name": "ignored", "count": 0})
        result = unmarshal_json_response(_SamplePayload, resp, body='{"name": "explicit", "count": 9}')
        assert result == _SamplePayload(name="explicit", count=9)


class TestSerializeRequestBody:
    def test_json_media_type_produces_json_content(self):
        result = serialize_request_body(
            _SamplePayload(name="x", count=1), nullable=False, optional=False,
            serialization_method="json", request_body_type=_SamplePayload,
        )
        assert result.media_type == "application/json"
        content = result.content
        if isinstance(content, bytes):
            content = content.decode()
        assert '"name":"x"' in content or '"name": "x"' in content

    def test_optional_none_body_returns_none(self):
        result = serialize_request_body(
            None, nullable=False, optional=True, serialization_method="json", request_body_type=_SamplePayload
        )
        assert result is None

    def test_raw_bytes_body_passthrough(self):
        result = serialize_request_body(
            b"raw-bytes", nullable=False, optional=False, serialization_method="raw", request_body_type=bytes
        )
        assert result.media_type == "application/octet-stream"
        assert result.content == b"raw-bytes"

    def test_invalid_body_type_for_media_type_raises_type_error(self):
        with pytest.raises(TypeError):
            serialize_request_body(
                12345, nullable=False, optional=False, serialization_method="raw", request_body_type=int
            )


class TestMatchStatusCodesAndContentType:
    @pytest.mark.parametrize(
        "codes,status,expected",
        [
            (["200"], 200, True),
            (["200"], 201, False),
            (["2XX"], 204, True),
            (["4XX"], 404, True),
            (["4XX"], 500, False),
            (["default"], 999, True),
            (["4XX", "5XX"], 503, True),
        ],
    )
    def test_match_status_codes(self, codes, status, expected):
        assert match_status_codes(codes, status) is expected

    @pytest.mark.parametrize(
        "content_type,pattern,expected",
        [
            ("application/json", "application/json", True),
            ("application/json; charset=utf-8", "application/json", True),
            ("application/json", "*", True),
            ("application/json", "*/*", True),
            ("application/json", "application/*", True),
            ("text/plain", "application/json", False),
            ("image/png", "*/png", True),
        ],
    )
    def test_match_content_type(self, content_type, pattern, expected):
        assert match_content_type(content_type, pattern) is expected

    def test_match_response_combines_status_and_content_type(self):
        resp = httpx.Response(200, json={}, headers={"content-type": "application/json"})
        assert match_response(resp, "200", "application/json") is True
        assert match_response(resp, "200", "text/plain") is False
        assert match_response(resp, ["4XX", "200"], "application/json") is True

    def test_match_response_defaults_missing_content_type_to_octet_stream(self):
        resp = httpx.Response(200, content=b"")
        assert "content-type" not in resp.headers
        assert match_response(resp, "200", "application/octet-stream") is True


class TestUrlHelpers:
    def test_remove_suffix_strips_when_present(self):
        assert remove_suffix("https://example.com/", "/") == "https://example.com"

    def test_remove_suffix_no_op_when_absent(self):
        assert remove_suffix("https://example.com", "/") == "https://example.com"

    def test_template_url_replaces_placeholders(self):
        result = template_url("https://{tenant}.example.com/{region}", {"tenant": "acme", "region": "us"})
        assert result == "https://acme.example.com/us"

    def test_template_url_leaves_unmatched_placeholders(self):
        result = template_url("https://{tenant}.example.com", {"other": "x"})
        assert result == "https://{tenant}.example.com"

    def test_generate_url_joins_server_and_path_with_no_path_params(self):
        result = generate_url("https://example.com/", "/rpc/Foo", None, None)
        assert result == "https://example.com/rpc/Foo"


class TestQueryParams:
    def test_none_query_params_returns_empty_dict(self):
        assert get_query_params(None) == {}

    def test_field_without_query_metadata_is_ignored(self):
        model = _QueryModel(no_metadata_field="ignored")
        assert get_query_params(model) == {}

    def test_scalar_and_list_fields_with_metadata_are_populated(self):
        model = _QueryModel(q="hello", tags=["a", "b"])
        params = get_query_params(model)
        assert params.get("q") == ["hello"]
        assert params.get("tags") == ["a", "b"]

    def test_unset_optional_query_field_is_omitted(self):
        model = _QueryModel(q=None, tags=None)
        params = get_query_params(model)
        assert "q" not in params
        assert "tags" not in params
