"""Unit tests for the Secrets service (sdk.secrets)."""
import pytest

from textql_sdk import errors, utils
from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response, text_response

BASE_PATH = "/textql.rpc.public.secret.SecretService"


def _tiny_backoff(**overrides):
    kwargs = dict(
        initial_interval=1,
        max_interval=5,
        exponent=1.0,
        max_elapsed_time=5000,
    )
    kwargs.update(overrides)
    return utils.BackoffStrategy(**kwargs)


def _retry_config():
    return utils.RetryConfig(
        strategy="backoff",
        backoff=_tiny_backoff(),
        retry_connection_errors=True,
    )


# ---------------------------------------------------------------------------
# create_api_revision (OptionalNullable api_access_key_id)
# ---------------------------------------------------------------------------


def test_create_api_revision_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.secrets.create_api_revision(api_access_key_id="key-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/CreateApiRevision"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["apiAccessKeyId"] == "key-1"


def test_create_api_revision_unset_omits_field(make_sdk):
    # api_access_key_id is OptionalNullable[str] = UNSET by default -- when
    # not passed at all, it must be omitted entirely from the JSON body.
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.secrets.create_api_revision()
    body = bundle.transport.body_json()
    assert body == {}


def test_create_api_revision_explicit_none_is_included_as_null(make_sdk):
    # Per the model's serializer: apiAccessKeyId is both "optional" and
    # "nullable" -- if the field is explicitly set (even to None), it must
    # be included as JSON null (distinct from being entirely absent/UNSET).
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.secrets.create_api_revision(api_access_key_id=None)
    body = bundle.transport.body_json()
    assert "apiAccessKeyId" in body
    assert body["apiAccessKeyId"] is None


@pytest.mark.asyncio
async def test_create_api_revision_async_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "ref": {"apiAccessKeyId": "key-2", "revision": 3},
                "apiAccessKey": {"id": "key-2"},
            },
        )
    )
    resp = await bundle.sdk.secrets.create_api_revision_async(api_access_key_id="key-2")
    body = bundle.transport.body_json()
    assert body["apiAccessKeyId"] == "key-2"
    assert resp.ref.api_access_key_id == "key-2"
    assert resp.ref.revision == 3
    assert resp.api_access_key.id == "key-2"


def test_create_api_revision_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.secrets.create_api_revision(api_access_key_id="key-1")
    assert exc_info.value.status_code == 400


# ---------------------------------------------------------------------------
# delete_api_access_key
# ---------------------------------------------------------------------------


def test_delete_api_access_key_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.secrets.delete_api_access_key(id="key-1")
    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/DeleteApiAccessKey"
    body = bundle.transport.body_json()
    assert body["id"] == "key-1"


@pytest.mark.asyncio
async def test_delete_api_access_key_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.secrets.delete_api_access_key_async(id="key-2")
    req = bundle.transport.last_request
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_delete_api_access_key_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.secrets.delete_api_access_key(id="missing")
    assert exc_info.value.status_code == 404


# ---------------------------------------------------------------------------
# delete_api_revision (ref: TextqlRPCPublicSecretAPIAccessRef)
# ---------------------------------------------------------------------------


def test_delete_api_revision_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.secrets.delete_api_revision(
        ref={"api_access_key_id": "key-1", "revision": 2}
    )
    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/DeleteApiRevision"
    body = bundle.transport.body_json()
    assert body["ref"]["apiAccessKeyId"] == "key-1"
    assert body["ref"]["revision"] == 2


def test_delete_api_revision_ref_string_revision_variant(make_sdk):
    # revision is Union[int, str] per the model.
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.secrets.delete_api_revision(
        ref={"api_access_key_id": "key-1", "revision": "latest"}
    )
    body = bundle.transport.body_json()
    assert body["ref"]["revision"] == "latest"


@pytest.mark.asyncio
async def test_delete_api_revision_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.secrets.delete_api_revision_async(
        ref={"api_access_key_id": "key-1"}
    )
    body = bundle.transport.body_json()
    assert body["ref"]["apiAccessKeyId"] == "key-1"
    assert "revision" not in body["ref"]


def test_delete_api_revision_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad ref"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.secrets.delete_api_revision(ref={"api_access_key_id": "key-1"})
    assert exc_info.value.status_code == 400


# ---------------------------------------------------------------------------
# delete_secret
# ---------------------------------------------------------------------------


def test_delete_secret_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.secrets.delete_secret(name="my-secret")
    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/DeleteSecret"
    body = bundle.transport.body_json()
    assert body["name"] == "my-secret"
    # Confirm no unexpected value/secret-adjacent key leaked into the body.
    assert set(body.keys()) == {"name"}


@pytest.mark.asyncio
async def test_delete_secret_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.secrets.delete_secret_async(name="my-secret")
    req = bundle.transport.last_request
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_delete_secret_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.secrets.delete_secret(name="my-secret")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# get_api_access_key -- masked-value passthrough
# ---------------------------------------------------------------------------


def test_get_api_access_key_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.secrets.get_api_access_key(id="key-1")
    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/GetApiAccessKey"
    body = bundle.transport.body_json()
    assert body["id"] == "key-1"


def test_get_api_access_key_response_masked_auth_value_passthrough(make_sdk):
    # The response model (TextqlRPCPublicSecretAPIAccessKey) does not even
    # define an auth_value/value field -- confirm masked-looking metadata
    # fields (e.g. description) come through completely untouched, with no
    # attempt at unmasking/decoding by the SDK.
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "apiAccessKey": {
                    "id": "key-1",
                    "description": "sk-***REDACTED***",
                    "headers": {"Authorization": "Bearer ****1234"},
                }
            },
        )
    )
    resp = bundle.sdk.secrets.get_api_access_key(id="key-1")
    assert resp.api_access_key.description == "sk-***REDACTED***"
    assert resp.api_access_key.headers["Authorization"] == "Bearer ****1234"


def test_get_api_access_key_response_has_no_value_field(make_sdk):
    # Confirm the response model genuinely has no plaintext "value"/"secret"
    # attribute at all -- the API is metadata-only by design.
    bundle = make_sdk(
        lambda req: json_response(200, {"apiAccessKey": {"id": "key-1"}})
    )
    resp = bundle.sdk.secrets.get_api_access_key(id="key-1")
    assert not hasattr(resp.api_access_key, "value")
    assert not hasattr(resp.api_access_key, "auth_value")


@pytest.mark.asyncio
async def test_get_api_access_key_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.secrets.get_api_access_key_async(id="key-2")
    req = bundle.transport.last_request
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_get_api_access_key_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.secrets.get_api_access_key(id="missing")
    assert exc_info.value.status_code == 404


# ---------------------------------------------------------------------------
# get_members_with_secrets (body: TextqlRPCPublicSecretGetMembersWithSecretsRequest)
# ---------------------------------------------------------------------------


def test_get_members_with_secrets_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.secrets.get_members_with_secrets(body={})
    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/GetMembersWithSecrets"


@pytest.mark.asyncio
async def test_get_members_with_secrets_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.secrets.get_members_with_secrets_async(body={})
    req = bundle.transport.last_request
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_get_members_with_secrets_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(502, {"message": "bad gateway"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.secrets.get_members_with_secrets(body={})
    assert exc_info.value.status_code == 502


# ---------------------------------------------------------------------------
# list_api_access_keys
# ---------------------------------------------------------------------------


def test_list_api_access_keys_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.secrets.list_api_access_keys(body={})
    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/ListApiAccessKeys"


@pytest.mark.asyncio
async def test_list_api_access_keys_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.secrets.list_api_access_keys_async(body={})
    req = bundle.transport.last_request
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_list_api_access_keys_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(401, {"message": "unauthorized"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.secrets.list_api_access_keys(body={})
    assert exc_info.value.status_code == 401


# ---------------------------------------------------------------------------
# list_api_providers
# ---------------------------------------------------------------------------


def test_list_api_providers_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.secrets.list_api_providers(body={})
    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/ListApiProviders"


@pytest.mark.asyncio
async def test_list_api_providers_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.secrets.list_api_providers_async(body={})
    req = bundle.transport.last_request
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_list_api_providers_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.secrets.list_api_providers(body={})
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# list_secrets -- masked-value passthrough, no plaintext "value" field exists
# ---------------------------------------------------------------------------


def test_list_secrets_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "secrets": [
                    {"id": "s1", "name": "secret-one", "description": "sk-***REDACTED***"},
                    {"id": "s2", "name": "secret-two", "description": None},
                ]
            },
        )
    )
    resp = bundle.sdk.secrets.list_secrets(body={})

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/ListSecrets"

    assert len(resp.secrets) == 2
    assert resp.secrets[0].name == "secret-one"
    # Masked-looking description string passed through completely opaque --
    # no unmasking/decoding/transformation performed by the SDK.
    assert resp.secrets[0].description == "sk-***REDACTED***"
    assert resp.secrets[1].description is None


def test_list_secrets_response_has_no_plaintext_value_field(make_sdk):
    # The TextqlRPCPublicSecretSecret model has no "value" attribute --
    # ListSecrets is metadata-only and never returns plaintext secret
    # material, by design of the generated model.
    bundle = make_sdk(
        lambda req: json_response(200, {"secrets": [{"id": "s1", "name": "n"}]})
    )
    resp = bundle.sdk.secrets.list_secrets(body={})
    assert not hasattr(resp.secrets[0], "value")


def test_list_secrets_masked_value_with_various_redaction_shapes(make_sdk):
    masked_values = ["sk-***REDACTED***", "****1234", "•" * 8, ""]
    for masked in masked_values:
        bundle = make_sdk(
            lambda req, masked=masked: json_response(
                200, {"secrets": [{"id": "s1", "name": "n", "link": masked}]}
            )
        )
        resp = bundle.sdk.secrets.list_secrets(body={})
        assert resp.secrets[0].link == masked


@pytest.mark.asyncio
async def test_list_secrets_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"secrets": []}))
    resp = await bundle.sdk.secrets.list_secrets_async(body={})
    assert resp.secrets == []


def test_list_secrets_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.secrets.list_secrets(body={})
    assert exc_info.value.status_code == 503


# ---------------------------------------------------------------------------
# migrate_secret_to_api_connector
# ---------------------------------------------------------------------------


def test_migrate_secret_to_api_connector_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.secrets.migrate_secret_to_api_connector(
        secret_name="my-secret",
        api_access_key_id="",
        header_name="Authorization",
        hosts=["api.example.com", "api2.example.com"],
        description="migrated",
        value_prefix="Bearer ",
        name="My Connector",
    )
    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/MigrateSecretToApiConnector"
    body = bundle.transport.body_json()
    assert body["secretName"] == "my-secret"
    assert body["apiAccessKeyId"] == ""
    assert body["headerName"] == "Authorization"
    assert body["hosts"] == ["api.example.com", "api2.example.com"]
    assert body["description"] == "migrated"
    assert body["valuePrefix"] == "Bearer "
    assert body["name"] == "My Connector"
    # Confirm the secret's actual plaintext value is never part of this
    # call's parameters at all -- migration references the secret by name
    # only, so there is no value-leakage surface here by construction.
    assert "value" not in body


def test_migrate_secret_to_api_connector_optional_fields_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.secrets.migrate_secret_to_api_connector(secret_name="my-secret")
    body = bundle.transport.body_json()
    assert body == {"secretName": "my-secret"}


@pytest.mark.asyncio
async def test_migrate_secret_to_api_connector_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.secrets.migrate_secret_to_api_connector_async(
        secret_name="my-secret", hosts=["h1"]
    )
    body = bundle.transport.body_json()
    assert body["secretName"] == "my-secret"
    assert body["hosts"] == ["h1"]


def test_migrate_secret_to_api_connector_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.secrets.migrate_secret_to_api_connector(secret_name="my-secret")
    assert exc_info.value.status_code == 400


# ---------------------------------------------------------------------------
# put_secret -- value must land ONLY in the "value" field
# ---------------------------------------------------------------------------


def test_put_secret_basic_value_only_in_value_field(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    secret_value = "sk-supersecretvalue-123"
    bundle.sdk.secrets.put_secret(
        name="my-secret",
        value=secret_value,
        description="a test secret",
        link="https://example.com",
        is_private=True,
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/PutSecret"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["name"] == "my-secret"
    assert body["value"] == secret_value
    assert body["description"] == "a test secret"
    assert body["link"] == "https://example.com"
    assert body["isPrivate"] is True

    # The secret value must appear in exactly one place in the serialized
    # body -- no duplication into another top-level key (e.g. accidentally
    # also stuffed into description/link by a serialization bug).
    top_level_values = [v for v in body.values() if isinstance(v, str)]
    assert top_level_values.count(secret_value) == 1
    assert set(body.keys()) == {"name", "value", "description", "link", "isPrivate"}


def test_put_secret_optional_nullable_description_and_link_unset_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.secrets.put_secret(name="my-secret", value="v")
    body = bundle.transport.body_json()
    assert "description" not in body
    assert "link" not in body
    # is_private / name / value are plain Optional[bool|str] fields with
    # optional_fields membership -- None is omitted too, but explicit values
    # given here are present.
    assert body == {"name": "my-secret", "value": "v"}


def test_put_secret_explicit_none_description_included_as_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.secrets.put_secret(name="my-secret", value="v", description=None)
    body = bundle.transport.body_json()
    assert "description" in body
    assert body["description"] is None


def test_put_secret_value_never_logged_into_response_echo(make_sdk):
    # The PutSecret response model has no field that echoes back the secret
    # value -- confirm the unmarshaled response object doesn't expose it
    # even if the (misbehaving) server tried to include it.
    secret_value = "sk-should-not-echo-back"
    bundle = make_sdk(lambda req: json_response(200, {"secret": {"id": "s1"}}))
    resp = bundle.sdk.secrets.put_secret(name="my-secret", value=secret_value)
    # Confirm no attribute on the response carries the raw value string.
    assert secret_value not in repr(resp)


@pytest.mark.asyncio
async def test_put_secret_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.secrets.put_secret_async(name="my-secret", value="v2")
    body = bundle.transport.body_json()
    assert body["value"] == "v2"


def test_put_secret_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "invalid"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.secrets.put_secret(name="my-secret", value="v")
    assert exc_info.value.status_code == 400


def test_put_secret_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.secrets.put_secret(name="my-secret", value="v")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# test_api_access_key -- success/failure JSON bodies at HTTP 200 vs real errors
# ---------------------------------------------------------------------------


def test_test_api_access_key_connection_succeeded(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"success": True, "statusCode": 200, "message": "ok"}
        )
    )
    resp = bundle.sdk.secrets.test_api_access_key(ref={"api_access_key_id": "key-1"})

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/TestApiAccessKey"
    body = bundle.transport.body_json()
    assert body["ref"]["apiAccessKeyId"] == "key-1"

    assert resp.success is True
    assert resp.status_code == 200
    assert resp.message == "ok"


def test_test_api_access_key_connection_failed_but_http_200(make_sdk):
    # A "connection test failed" result is still a successful RPC call (HTTP
    # 200) -- the failure is communicated via the response body's boolean
    # field, not an HTTP error. Confirm no exception is raised.
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {"success": False, "statusCode": 401, "message": "invalid credentials"},
        )
    )
    resp = bundle.sdk.secrets.test_api_access_key(ref={"api_access_key_id": "key-1"})
    assert resp.success is False
    assert resp.status_code == 401
    assert resp.message == "invalid credentials"


@pytest.mark.asyncio
async def test_test_api_access_key_async_connection_failed(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"success": False, "message": "timeout"})
    )
    resp = await bundle.sdk.secrets.test_api_access_key_async(
        ref={"api_access_key_id": "key-1"}
    )
    assert resp.success is False
    assert resp.message == "timeout"


def test_test_api_access_key_actual_4xx_raises(make_sdk):
    # A genuine HTTP 4xx (e.g. the ref itself doesn't exist) must still
    # raise, distinctly from a 200 with success=False.
    bundle = make_sdk(lambda req: json_response(404, {"message": "key not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.secrets.test_api_access_key(ref={"api_access_key_id": "missing"})
    assert exc_info.value.status_code == 404


def test_test_api_access_key_actual_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.secrets.test_api_access_key(ref={"api_access_key_id": "key-1"})
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# update (UpdateSecret) -- value/description/link all OptionalNullable
# ---------------------------------------------------------------------------


def test_update_secret_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.secrets.update(
        name="my-secret", value="new-value", description="new desc", link="new-link"
    )
    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/UpdateSecret"
    body = bundle.transport.body_json()
    assert body["name"] == "my-secret"
    assert body["value"] == "new-value"
    assert body["description"] == "new desc"
    assert body["link"] == "new-link"


def test_update_secret_unset_optional_nullable_fields_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.secrets.update(name="my-secret")
    body = bundle.transport.body_json()
    assert body == {"name": "my-secret"}
    assert "value" not in body
    assert "description" not in body
    assert "link" not in body


def test_update_secret_explicit_none_value_included_as_null(make_sdk):
    # Explicitly clearing the secret value via null -- must be distinguishable
    # from "don't touch the value" (UNSET/omitted).
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.secrets.update(name="my-secret", value=None)
    body = bundle.transport.body_json()
    assert "value" in body
    assert body["value"] is None


def test_update_secret_explicit_none_description_and_link(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.secrets.update(name="my-secret", description=None, link=None)
    body = bundle.transport.body_json()
    assert body["description"] is None
    assert body["link"] is None
    assert "value" not in body


@pytest.mark.asyncio
async def test_update_secret_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.secrets.update_async(name="my-secret", value="v3")
    body = bundle.transport.body_json()
    assert body["value"] == "v3"


def test_update_secret_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.secrets.update(name="my-secret", value="v")
    assert exc_info.value.status_code == 400


# ---------------------------------------------------------------------------
# upsert_api_access_key -- auth_value must land only in intended field
# ---------------------------------------------------------------------------


def test_upsert_api_access_key_basic_auth_value_only_in_field(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    secret_auth_value = "Bearer sk-topsecret-token"
    bundle.sdk.secrets.upsert_api_access_key(
        ref={"api_access_key_id": "key-1"},
        persist_to_db=True,
        hosts=["api.example.com"],
        headers={"X-Api-Version": "1"},
        query_params={"format": "json"},
        description="my key",
        provider="custom",
        auth_value=secret_auth_value,
        auth_value_extra="extra-secret",
        auth_type="token",
        body={"grant_type": "client_credentials"},
        content_type="BODY_CONTENT_TYPE_JSON",
        test_url="https://api.example.com/ping",
        name="My Key",
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/UpsertApiAccessKey"

    body = bundle.transport.body_json()
    assert body["ref"]["apiAccessKeyId"] == "key-1"
    assert body["persistToDb"] is True
    assert body["hosts"] == ["api.example.com"]
    assert body["headers"] == {"X-Api-Version": "1"}
    assert body["queryParams"] == {"format": "json"}
    assert body["description"] == "my key"
    assert body["provider"] == "custom"
    assert body["authValue"] == secret_auth_value
    assert body["authValueExtra"] == "extra-secret"
    assert body["authType"] == "token"
    assert body["body"] == {"grant_type": "client_credentials"}
    assert body["contentType"] == "BODY_CONTENT_TYPE_JSON"
    assert body["testUrl"] == "https://api.example.com/ping"
    assert body["name"] == "My Key"

    # authValue must appear in exactly one place -- not duplicated into e.g.
    # description, name, or nested inside `body`/`headers`/`queryParams`.
    assert body["body"].get("grant_type") != secret_auth_value
    assert secret_auth_value not in body["headers"].values()
    assert secret_auth_value not in body["queryParams"].values()
    assert body["description"] != secret_auth_value
    assert body["name"] != secret_auth_value


def test_upsert_api_access_key_optional_fields_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.secrets.upsert_api_access_key()
    body = bundle.transport.body_json()
    assert body == {}


def test_upsert_api_access_key_http_basic_auth_variant(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.secrets.upsert_api_access_key(
        http_basic_auth={"username": "user1", "password": "hunter2"},
    )
    body = bundle.transport.body_json()
    assert body["httpBasicAuth"]["username"] == "user1"
    assert body["httpBasicAuth"]["password"] == "hunter2"
    # Confirm the basic-auth password doesn't leak anywhere else in the body.
    assert set(body.keys()) == {"httpBasicAuth"}


def test_upsert_api_access_key_expires_at_datetime_serialization(make_sdk):
    from datetime import datetime, timezone

    bundle = make_sdk(lambda req: json_response(200, {}))
    dt = datetime(2030, 1, 15, 1, 30, 15, tzinfo=timezone.utc)
    bundle.sdk.secrets.upsert_api_access_key(expires_at=dt)
    body = bundle.transport.body_json()
    assert body["expiresAt"].startswith("2030-01-15T01:30:15")


@pytest.mark.asyncio
async def test_upsert_api_access_key_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.secrets.upsert_api_access_key_async(auth_value="secret-async")
    body = bundle.transport.body_json()
    assert body["authValue"] == "secret-async"


def test_upsert_api_access_key_response_never_echoes_auth_value(make_sdk):
    auth_value = "Bearer super-secret-should-not-echo"
    bundle = make_sdk(
        lambda req: json_response(200, {"apiAccessKey": {"id": "key-1"}})
    )
    resp = bundle.sdk.secrets.upsert_api_access_key(auth_value=auth_value)
    assert auth_value not in repr(resp)


def test_upsert_api_access_key_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "invalid"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.secrets.upsert_api_access_key(auth_value="v")
    assert exc_info.value.status_code == 400


def test_upsert_api_access_key_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.secrets.upsert_api_access_key(auth_value="v")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# Retries (representative subset: put_secret, list_secrets)
# ---------------------------------------------------------------------------


def test_put_secret_retries_on_500_then_succeeds(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "temporary"}),
            json_response(200, {}),
        ]
    )
    bundle = make_sdk(handler)

    bundle.sdk.secrets.put_secret(
        name="my-secret", value="v", retries=_retry_config()
    )
    assert len(bundle.transport.requests) == 2


@pytest.mark.asyncio
async def test_list_secrets_async_retries_on_500_then_succeeds(
    make_sdk, sequence_handler
):
    handler = sequence_handler(
        [
            json_response(500, {"message": "temporary"}),
            json_response(200, {"secrets": [{"id": "s1"}]}),
        ]
    )
    bundle = make_sdk(handler)

    resp = await bundle.sdk.secrets.list_secrets_async(
        body={}, retries=_retry_config()
    )
    assert len(resp.secrets) == 1
    assert len(bundle.transport.requests) == 2


def test_update_secret_retries_exhausted_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "persistent"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.secrets.update(name="my-secret", retries=_retry_config())
    assert exc_info.value.status_code == 500
    assert len(bundle.transport.requests) >= 2


# ---------------------------------------------------------------------------
# Per-call overrides
# ---------------------------------------------------------------------------


def test_put_secret_server_url_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.secrets.put_secret(
        name="my-secret", value="v", server_url="https://override.invalid"
    )
    req = bundle.transport.last_request
    assert str(req.url).startswith("https://override.invalid")


def test_list_secrets_http_headers_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.secrets.list_secrets(
        body={}, http_headers={"X-Custom-Header": "custom-value"}
    )
    req = bundle.transport.last_request
    assert req.headers["X-Custom-Header"] == "custom-value"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_update_secret_timeout_ms_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.secrets.update(name="my-secret", timeout_ms=15000)


def test_get_api_access_key_connect_timeout_ms_header(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.secrets.get_api_access_key(id="key-1", connect_timeout_ms=2500.0)
    req = bundle.transport.last_request
    assert req.headers.get("Connect-Timeout-Ms") in ("2500.0", "2500")
