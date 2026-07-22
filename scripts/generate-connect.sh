#!/usr/bin/env bash
set -euo pipefail

# Regenerates the vendored Connect-RPC client under src/textql_sdk/_connect from
# the platform protos. This is NOT produced by Speakeasy — it survives
# `speakeasy run` (Speakeasy only owns the files it generates). Mirrors the TS
# SDK's scripts/generate-connect.sh.
#
#   DEMO2_DIR=/path/to/demo2 ./scripts/generate-connect.sh
#
# Plugin versions are pinned to match the `connect-python` runtime declared in
# pyproject.toml. Bump them together.

SDK_DIR="$(cd "$(dirname "$0")/.." && pwd)"
DEMO2_DIR="${DEMO2_DIR:-$SDK_DIR/../demo2}"
PROTO_DIR="$DEMO2_DIR/proto/api"
OUT_DIR="$SDK_DIR/src/textql_sdk/_connect"

CONNECT_PLUGIN_VERSION="v0.9.0"   # keep in sync with connect-python in pyproject.toml
PROTOBUF_PLUGIN_VERSION="v31.1"   # keep in sync with the protobuf runtime range

TEMPLATE_DIR="$(mktemp -d)"
trap 'rm -rf "$TEMPLATE_DIR"' EXIT
TEMPLATE="$TEMPLATE_DIR/buf.gen.yaml"
cat > "$TEMPLATE" <<EOF
version: v2
clean: true
plugins:
  - remote: buf.build/protocolbuffers/python:$PROTOBUF_PLUGIN_VERSION
    out: $OUT_DIR
  - remote: buf.build/protocolbuffers/pyi:$PROTOBUF_PLUGIN_VERSION
    out: $OUT_DIR
  - remote: buf.build/connectrpc/python:$CONNECT_PLUGIN_VERSION
    out: $OUT_DIR
EOF

cd "$PROTO_DIR"
buf generate --include-imports --template "$TEMPLATE"

# protoc/connect emit absolute imports (`import public.chat_pb2`), which only
# resolve if the output dir is on sys.path. Rewrite them to package-relative so
# _connect works as a plain subpackage of textql_sdk. google.protobuf is left
# absolute so the well-known types resolve from the installed protobuf runtime.
FDS="$TEMPLATE_DIR/fds.binpb"
buf build --as-file-descriptor-set -o "$FDS"
# Run isolated (uvx, not `uv run`): protoletariat pins protobuf<6, which clashes
# with the SDK's runtime protobuf. It's a build-time text rewriter, never imported.
uvx --from protoletariat protol \
  --python-out "$OUT_DIR" --in-place --create-package --exclude-google-imports \
  -s _pb2.py -s _pb2.pyi -s _connect.py \
  raw "$FDS"

# protoletariat doesn't rewrite the `import x.y as z` form that connect-python
# emits in *_connect.py. Every service lives under public/, so its sibling
# message imports become relative; google.protobuf stays absolute (runtime).
find "$OUT_DIR/public" -name '*_connect.py' -exec \
  sed -i.bak -E 's/^import public\.([A-Za-z0-9_]+) as /from . import \1 as /' {} +
find "$OUT_DIR" -name '*.bak' -delete

# Trim internal-only proto trees (not part of the public SDK surface) and the
# vendored google/protobuf well-known types (we use the runtime's — a second
# copy would double-register in the descriptor pool).
rm -rf "$OUT_DIR/platform" "$OUT_DIR/demo" "$OUT_DIR/google/protobuf"

echo "regenerated $OUT_DIR"
