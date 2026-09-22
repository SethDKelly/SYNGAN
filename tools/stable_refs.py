from __future__ import annotations

import json
import re
from pathlib import Path
from typing import NotRequired, TypedDict, cast

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "docs" / "authority" / "stable-reference-registry.json"

REF_PATTERN = re.compile(
    r"^syngan://(?:authority|design|implementation|program|history)/"
    r"[a-z0-9][a-z0-9-]*(?:/[a-z0-9][a-z0-9-]*)*$"
)


class StableReferenceError(ValueError):
    pass


class ReferenceEntry(TypedDict):
    ref: str
    status: str
    authority_class: str
    owner_family: str
    path: NotRequired[str]
    replacement_ref: NotRequired[str]


class Registry(TypedDict):
    schema_version: str
    status: str
    authority: str
    namespace: str
    rules: dict[str, object]
    references: list[ReferenceEntry]


def load_registry(path: Path = REGISTRY_PATH) -> Registry:
    return cast(Registry, json.loads(path.read_text(encoding="utf-8")))


def validate_reference_syntax(reference: str) -> None:
    if REF_PATTERN.fullmatch(reference) is None:
        raise StableReferenceError(f"malformed stable reference: {reference}")


def _entries_by_ref(registry: Registry) -> dict[str, ReferenceEntry]:
    entries: dict[str, ReferenceEntry] = {}
    for entry in registry["references"]:
        reference = entry["ref"]
        if reference in entries:
            raise StableReferenceError(f"duplicate stable reference: {reference}")
        entries[reference] = entry
    return entries


def resolve_reference(
    reference: str,
    registry: Registry | None = None,
    *,
    root: Path = ROOT,
) -> ReferenceEntry:
    validate_reference_syntax(reference)
    current = load_registry() if registry is None else registry
    entry = _entries_by_ref(current).get(reference)
    if entry is None:
        raise StableReferenceError(f"unknown stable reference: {reference}")
    if entry["status"] != "active":
        replacement = entry.get("replacement_ref")
        suffix = f"; replacement: {replacement}" if replacement else ""
        raise StableReferenceError(f"retired stable reference: {reference}{suffix}")
    path = entry.get("path")
    if not path:
        raise StableReferenceError(f"active stable reference has no path: {reference}")
    resolved = (root / path).resolve()
    if not resolved.exists():
        raise StableReferenceError(
            f"stable reference target does not exist: {reference} -> {path}"
        )
    return entry


def reference_for_path(
    path: str,
    registry: Registry | None = None,
    *,
    root: Path = ROOT,
) -> ReferenceEntry:
    current = load_registry() if registry is None else registry
    candidate = Path(path)
    resolved = candidate.resolve() if candidate.is_absolute() else (root / candidate).resolve()

    matches: list[ReferenceEntry] = []
    for entry in current["references"]:
        if entry["status"] != "active":
            continue
        entry_path = entry.get("path")
        if entry_path and (root / entry_path).resolve() == resolved:
            matches.append(entry)

    if not matches:
        raise StableReferenceError(f"no active stable reference for path: {path}")
    if len(matches) != 1:
        refs = ", ".join(sorted(entry["ref"] for entry in matches))
        raise StableReferenceError(f"ambiguous stable reference for path {path}: {refs}")
    return matches[0]
