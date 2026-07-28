#!/usr/bin/env python3
"""Post-process the vendored Connect tree under src/textql_sdk/_connect.

Run by scripts/generate-connect.sh after codegen, and safe to re-run on an
already-processed tree (every step is idempotent). Three fixups, all of which
have to live here rather than in config, because pyproject.toml and pylintrc are
Speakeasy-managed and get overwritten on every `speakeasy run`:

1. Relative-ise absolute in-tree imports in the ``.pyi`` stubs. protoletariat
   only rewrites the ``.py`` files: its patterns are keyed on protoc's alias
   convention (``import auth_pb2 as auth__pb2``), while the pyi plugin emits
   ``import auth_pb2 as _auth_pb2``, so nothing matches and the stubs keep
   absolute imports that only resolve with the output dir on sys.path.
2. Drop dangling ``from . import <pkg>`` lines from the package stubs, for the
   subtrees generate-connect.sh deletes (platform/, demo/, google/protobuf/).
3. Prepend lint/typecheck opt-outs. Generated protobuf code is never clean
   under either tool (~64k pylint messages: no-member, abstract-method,
   protected-access; plus stub/types-protobuf mismatches under mypy).

``# mypy: ignore-errors`` only suppresses *reporting* inside these files — the
declared types are still used, so callers keep real protobuf types.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

HEADERS = ("# pylint: skip-file", "# mypy: ignore-errors")

# `import a.b.c_pb2 as _alias` / `from a.b import c_pb2 as _alias`. Bare
# `import x`/`from x import y` without an alias never appears in the generated
# stubs, so requiring one keeps the match tight. Both paths must start with a
# word character so an already-relative `from .. import x` is left alone —
# otherwise a re-run would prefix the dots a second time.
IMPORT_RE = re.compile(r"^import (?P<mod>\w[\w.]*) as (?P<alias>\w+)$")
FROM_RE = re.compile(r"^from (?P<pkg>\w[\w.]*) import (?P<mod>\w+) as (?P<alias>\w+)$")


def _in_tree(root: Path, dotted: str) -> bool:
    """Whether `dotted` names a module or package that exists under `root`.

    This is what keeps google.protobuf (deleted from the tree, resolved from the
    installed runtime) absolute while google.api (kept) becomes relative.
    """
    base = root.joinpath(*dotted.split("."))
    return base.is_dir() or base.with_suffix(".py").is_file() or base.with_suffix(".pyi").is_file()


def _relative_prefix(root: Path, stub: Path) -> str:
    """Dots needed to climb from `stub`'s package back to `root`.

    One dot for the stub's own package, plus one per directory between it and
    the root: `_connect/public/x_pb2.pyi` needs `..` to reach `_connect`.
    """
    return "." * len(stub.relative_to(root).parts)


def relativise_stub_imports(root: Path) -> int:
    changed = 0
    for stub in sorted(root.rglob("*.pyi")):
        dots = _relative_prefix(root, stub)
        lines = stub.read_text().splitlines(keepends=True)
        out = []
        dirty = False
        for line in lines:
            body, nl = line.rstrip("\n"), line[len(line.rstrip("\n")) :]
            new = body

            m = IMPORT_RE.match(body)
            if m and _in_tree(root, m["mod"]):
                pkg, _, mod = m["mod"].rpartition(".")
                new = f"from {dots}{pkg} import {mod} as {m['alias']}"
            else:
                m = FROM_RE.match(body)
                if m and _in_tree(root, f"{m['pkg']}.{m['mod']}"):
                    new = f"from {dots}{m['pkg']} import {m['mod']} as {m['alias']}"

            dirty |= new != body
            out.append(new + nl)
        if dirty:
            stub.write_text("".join(out))
            changed += 1
    return changed


def prune_package_stubs(root: Path) -> int:
    """Drop `from . import <name>` lines naming a subtree that no longer exists."""
    changed = 0
    for stub in sorted(root.rglob("__init__.pyi")):
        lines = stub.read_text().splitlines(keepends=True)
        kept = [
            line
            for line in lines
            if not (
                (m := re.match(r"^from \. import (\w+)$", line.strip()))
                and not _in_tree(stub.parent, m.group(1))
            )
        ]
        if len(kept) != len(lines):
            stub.write_text("".join(kept))
            changed += 1
    return changed


def add_lint_headers(root: Path) -> int:
    changed = 0
    for path in sorted([*root.rglob("*.py"), *root.rglob("*.pyi")]):
        text = path.read_text()
        existing = text.split("\n", len(HEADERS))[: len(HEADERS)]
        missing = [h for h in HEADERS if h not in existing]
        if missing:
            path.write_text("".join(f"{h}\n" for h in missing) + text)
            changed += 1
    return changed


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent.parent / "src/textql_sdk/_connect")
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 1

    print(f"relativised imports in {relativise_stub_imports(root)} stub(s)")
    print(f"pruned {prune_package_stubs(root)} package stub(s)")
    print(f"added lint headers to {add_lint_headers(root)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
