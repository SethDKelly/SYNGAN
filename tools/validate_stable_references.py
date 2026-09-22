from __future__ import annotations

import json
from pathlib import Path

from stable_refs import REF_PATTERN, ROOT, load_registry

OWNERSHIP_PATH = ROOT / "docs" / "authority" / "canonical-knowledge-ownership-map.json"
DOCS = (ROOT / "docs").resolve()

_ALLOWED_CLASSES = {
    "current",
    "current-program",
    "future-non-authoritative",
    "history-provenance",
}


def main() -> int:
    errors: list[str] = []
    registry = load_registry()
    ownership = json.loads(OWNERSHIP_PATH.read_text(encoding="utf-8"))

    if registry["schema_version"] != "1.0":
        errors.append("stable-reference registry schema_version must be 1.0")
    if registry["status"] != "active":
        errors.append("stable-reference registry must be active")
    if registry["namespace"] != "syngan://":
        errors.append("stable-reference namespace must be syngan://")

    owner_paths = {owner["family"]: owner["path"] for owner in ownership["owners"]}
    seen_refs: set[str] = set()
    active_paths: dict[str, str] = {}
    owner_refs: dict[str, str] = {}

    for entry in registry["references"]:
        reference = entry.get("ref", "")
        status = entry.get("status", "")
        authority_class = entry.get("authority_class", "")
        owner_family = entry.get("owner_family", "")
        path = entry.get("path")

        if REF_PATTERN.fullmatch(reference) is None:
            errors.append(f"malformed stable reference: {reference}")
        if reference in seen_refs:
            errors.append(f"duplicate stable reference: {reference}")
        seen_refs.add(reference)

        if status not in {"active", "retired"}:
            errors.append(f"{reference}: invalid lifecycle status {status!r}")
        if authority_class not in _ALLOWED_CLASSES:
            errors.append(f"{reference}: invalid authority_class {authority_class!r}")

        if status == "active":
            if not isinstance(path, str) or not path:
                errors.append(f"{reference}: active entry requires path")
                continue
            if path in active_paths:
                errors.append(
                    f"duplicate active path binding: {path} -> "
                    f"{active_paths[path]}, {reference}"
                )
            active_paths[path] = reference

            resolved = (ROOT / path).resolve()
            if not resolved.exists():
                errors.append(f"{reference}: target path does not exist: {path}")
            elif not resolved.is_relative_to(DOCS):
                errors.append(f"{reference}: active target must resolve under docs/: {path}")

            if owner_family not in owner_paths:
                errors.append(f"{reference}: unknown owner_family {owner_family!r}")
            elif owner_paths[owner_family] != path:
                errors.append(
                    f"{reference}: owner-family drift for {owner_family}: "
                    f"registry={path}, ownership={owner_paths[owner_family]}"
                )

            if owner_family in owner_refs:
                errors.append(
                    f"owner family has multiple active stable refs: {owner_family} -> "
                    f"{owner_refs[owner_family]}, {reference}"
                )
            owner_refs[owner_family] = reference
        else:
            if path:
                errors.append(f"{reference}: retired entry must not keep an active path")
            replacement = entry.get("replacement_ref")
            if replacement and replacement == reference:
                errors.append(f"{reference}: replacement_ref cannot point to itself")

    for family in sorted(owner_paths):
        if family not in owner_refs:
            errors.append(f"ownership family lacks active stable reference: {family}")

    for family in sorted(owner_refs):
        if family not in owner_paths:
            errors.append(f"stable reference owner family is not canonical: {family}")

    for error in errors:
        print(f"ERROR {error}")
    print(
        f"Stable-reference validation: {len(errors)} error(s), "
        f"{len(registry['references'])} registry entry(ies)"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
