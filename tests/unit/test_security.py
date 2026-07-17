"""Unit tests for the Security model and utils.security auth-header helpers."""
import os

import pytest

from textql_sdk import models
from textql_sdk.utils.security import get_security, get_security_from_env


class TestSecurityHeaderGeneration:
    def test_api_key_produces_tql_api_key_header(self):
        security = models.Security(api_key="my-secret-key")
        headers, query_params = get_security(security)

        assert headers == {"tql_api_key": "my-secret-key"}
        assert query_params == {}

    def test_none_api_key_produces_no_headers(self):
        security = models.Security(api_key=None)
        headers, query_params = get_security(security)

        assert headers == {}
        assert query_params == {}

    def test_none_security_produces_no_headers(self):
        headers, query_params = get_security(None)
        assert headers == {}
        assert query_params == {}

    def test_non_basemodel_security_raises_type_error(self):
        with pytest.raises(TypeError):
            get_security({"api_key": "x"})

    def test_allowed_fields_restricts_which_fields_are_applied(self):
        security = models.Security(api_key="my-secret-key")
        headers, _ = get_security(security, allowed_fields=[])
        assert headers == {}


class TestSecurityFromEnv:
    def test_returns_existing_security_untouched(self, monkeypatch):
        monkeypatch.setenv("TEXTQL_API_KEY", "env-key")
        existing = models.Security(api_key="explicit-key")

        result = get_security_from_env(existing, models.Security)

        assert result is existing
        assert result.api_key == "explicit-key"

    def test_falls_back_to_env_var_when_none(self, monkeypatch):
        monkeypatch.setenv("TEXTQL_API_KEY", "env-key")

        result = get_security_from_env(None, models.Security)

        assert isinstance(result, models.Security)
        assert result.api_key == "env-key"

    def test_returns_none_when_no_security_and_no_env(self, monkeypatch):
        monkeypatch.delenv("TEXTQL_API_KEY", raising=False)

        result = get_security_from_env(None, models.Security)

        assert result is None

    def test_non_basemodel_class_raises_type_error(self):
        with pytest.raises(TypeError):
            get_security_from_env(None, dict)


class TestSecurityModelSerialization:
    def test_model_dump_omits_none_api_key(self):
        security = models.Security(api_key=None)
        dumped = security.model_dump(by_alias=True)
        assert dumped == {}

    def test_model_dump_includes_explicit_api_key(self):
        security = models.Security(api_key="abc123")
        dumped = security.model_dump(by_alias=True)
        assert dumped.get("api_key") == "abc123"

    def test_typed_dict_shape(self):
        d: models.SecurityTypedDict = {"api_key": "abc"}
        assert d["api_key"] == "abc"
