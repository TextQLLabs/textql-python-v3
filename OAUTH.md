# OAuth access and refresh tokens

`textql_sdk.oauth` lets the SDK authenticate the way first-party client apps do:
with an OAuth access token sent as `Authorization: Bearer`, refreshed with a
refresh token. It is hand-written and lives outside the Speakeasy-generated
surface, because the generated `api_key` option can only send `tql_api_key`.

## Signing users in

Register an OAuth application under **Settings > Security** with your tool's
redirect URI and the `api:read` scope (plus `api:write` to change anything). An
application with only `mcp:tools` gets tokens the SDK cannot use. Each user must
already be a member of the organization.

Then run the authorization code + PKCE flow once per user:

```python
from textql_sdk.oauth import authorization_url, exchange_code

# 1. Login route: remember state and code_verifier in the user's session.
req = authorization_url(CLIENT_ID, REDIRECT_URI, scopes=["api:read", "api:write"])
session["oauth"] = (req.state, req.code_verifier)
redirect(req.url)

# 2. Callback route: the user signed in and approved the app.
state, code_verifier = session.pop("oauth")
if request.args["state"] != state:
    abort(400)
tokens = exchange_code(
    request.args["code"],
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    code_verifier=code_verifier,
)
store.save(user, tokens)
```

## Usage

```python
from textql_sdk.oauth import OAuthTokens, from_tokens


def save(tokens: OAuthTokens) -> None:
    store.put(tokens.access_token, tokens.refresh_token, tokens.expires_at)


sdk = from_tokens(
    access_token=stored.access_token,
    refresh_token=stored.refresh_token,
    client_id="<oauth client id>",
    client_secret="<oauth client secret>",
    expires_at=stored.expires_at,  # or expires_in=3600 straight from /oauth/token
    on_tokens=save,
    server_url="https://app.textql.com",  # optional, same as Textql(server_url=...)
)

sdk.chats.create_chat(message="hi")
```

Every request, sync and async, gets a valid access token:

- The token is refreshed 60 seconds before `expires_at`. Without an expiry it
  is refreshed only when the server answers 401.
- A 401 triggers one refresh and one retry of the same request.
- Refreshes call `POST <server>/oauth/token` with `grant_type=refresh_token`.
  Pass `token_url=` to override it.

## Persist every refresh

Refresh tokens are single use. Each refresh returns a new refresh token and the
server rejects the old one with `invalid_grant`. Save the pair handed to
`on_tokens` every time, or the next process start fails to refresh.

One `TokenManager` serializes its refreshes, so share it instead of building one
per SDK instance:

```python
from textql_sdk.oauth import TokenManager, from_tokens

manager = TokenManager(access, refresh, client_id=..., client_secret=..., on_tokens=save)
a = from_tokens(manager=manager)
b = from_tokens(manager=manager, server_url=...)
```

Separate processes sharing one grant must coordinate their refreshes themselves.

## Your own httpx clients

`from_tokens` builds the httpx clients. To use your own (custom TLS, proxies,
transports), attach `TokenAuth` to them and leave `api_key` unset:

```python
import httpx
from textql_sdk import Textql
from textql_sdk.oauth import TokenAuth

auth = TokenAuth(manager)
sdk = Textql(
    client=httpx.Client(auth=auth, verify="corp-ca.pem"),
    async_client=httpx.AsyncClient(auth=auth, verify="corp-ca.pem"),
)
```

`TokenAuth` removes any `tql_api_key` header, including one filled from
`TEXTQL_API_KEY`, because the server prefers an API key over a Bearer token.

## Streaming

`create_streaming_client(sdk)` picks up the token manager from an SDK built this
way, or takes one directly with `tokens=manager`. Each call reads the current
token. A stream cannot be replayed after a 401, so the `unauthenticated` error
still reaches the caller, and the token is refreshed before the next call.

## Errors

A failed refresh raises `OAuthRefreshError` with the HTTP `status_code` and the
OAuth `error` (`invalid_grant` for an expired, revoked or already used refresh
token, `invalid_client` for bad client credentials). The user has to sign in
again to get a new pair.

## Server requirements

- The access token must carry a public API scope. Tokens issued only for MCP
  (`mcp:tools`) are rejected.
- Bearer tokens work on every `/rpc/public` Connect RPC this SDK calls. The
  `/v2` REST API and the `/rpc/public/chat/stream` SSE endpoint do not accept
  them.
- Refreshing requires the OAuth client secret, so keep this server-side.
