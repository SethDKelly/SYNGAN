from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

from stable_refs import StableReferenceError, load_registry, resolve_reference

ROOT = Path(__file__).resolve().parents[1]
DOCS = (ROOT / "docs").resolve()
KNOWLEDGE = ROOT / "knowledge"

_TOP_KEY = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?$")
_MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
_REQUIRED = {
    "type",
    "title",
    "description",
    "syngan_ref",
    "resource",
    "tags",
    "status",
    "syngan_authority",
}
_VALID_STATUS = {"draft", "stable", "deprecated"}


def _scalar(raw: str) -> str:
    value = raw.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def _frontmatter(text: str) -> tuple[dict[str, str], str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text
    try:
        end = next(index for index in range(1, len(lines)) if lines[index].strip() == "---")
    except StopIteration as exc:
        raise ValueError("frontmatter opening delimiter has no closing delimiter") from exc

    data: dict[str, str] = {}
    for line in lines[1:end]:
        if not line or line[0].isspace() or line.lstrip().startswith("#"):
            continue
        match = _TOP_KEY.match(line)
        if match:
            data[match.group(1)] = _scalar(match.group(2) or "")
    return data, "\n".join(lines[end + 1 :])


def _local_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().split("#", maxsplit=1)[0].strip()
    if not target or target.startswith(("http://", "https://", "mailto:")):
        return None
    parsed = urlparse(target)
    if parsed.scheme:
        return None
    if target.startswith("/"):
        return (KNOWLEDGE / target.lstrip("/")).resolve()
    return (source.parent / target).resolve()


def main() -> int:
    errors: list[str] = []
    registry = load_registry()
    seen_refs: set[str] = set()

    if not KNOWLEDGE.is_dir():
        print("ERROR knowledge/ directory is missing")
        return 1

    for path in KNOWLEDGE.rglob("*"):
        if path.is_file() and path.suffix != ".md":
            rel = path.relative_to(ROOT).as_posix()
            errors.append(f"{rel}: producer profile permits generated Markdown files only")

    for path in sorted(KNOWLEDGE.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        try:
            meta, body = _frontmatter(text)
        except ValueError as exc:
            errors.append(f"{rel}: {exc}")
            continue

        if path.name == "index.md":
            if path == KNOWLEDGE / "index.md":
                if meta != {"okf_version": "0.2"}:
                    errors.append(
                        'knowledge/index.md frontmatter must contain only okf_version: "0.2"'
                    )
            elif meta:
                errors.append(f"{rel}: non-root index.md must not contain frontmatter")
        elif path.name == "log.md":
            if meta:
                errors.append(f"{rel}: log.md must not contain frontmatter")
        else:
            if not meta:
                errors.append(f"{rel}: OKF concept requires YAML frontmatter")
                continue

            missing = sorted(key for key in _REQUIRED if not meta.get(key, "").strip())
            if missing:
                errors.append(f"{rel}: missing SYNGAN producer fields: {', '.join(missing)}")
            if _scalar(meta.get("type", "")) != "SYNGAN Knowledge Route":
                errors.append(f"{rel}: unexpected route type {meta.get('type')!r}")

            status = _scalar(meta.get("status", ""))
            if status and status not in _VALID_STATUS:
                errors.append(f"{rel}: invalid OKF lifecycle status {status!r}")
            if _scalar(meta.get("syngan_authority", "")) != "projection-only":
                errors.append(f"{rel}: generated route must remain projection-only")

            tags = meta.get("tags", "").strip()
            if tags and not (tags.startswith("[") and tags.endswith("]")):
                errors.append(f"{rel}: tags must be an inline YAML list")
            for prohibited in ("generated", "verified"):
                if prohibited in meta:
                    errors.append(f"{rel}: routing projection must not assert {prohibited}")

            stable_ref = _scalar(meta.get("syngan_ref", ""))
            if stable_ref in seen_refs:
                errors.append(f"{rel}: duplicate generated stable reference: {stable_ref}")
            seen_refs.add(stable_ref)

            try:
                entry = resolve_reference(stable_ref, registry)
            except StableReferenceError as exc:
                errors.append(f"{rel}: {exc}")
                entry = None

            resource = _scalar(meta.get("resource", ""))
            target = _local_target(path, resource)
            if target is None or not target.exists():
                errors.append(f"{rel}: resource target does not exist: {resource}")
            elif not target.is_relative_to(DOCS):
                errors.append(f"{rel}: resource must resolve under docs/: {resource}")
            elif entry is not None:
                expected = (ROOT / entry["path"]).resolve()
                if target != expected:
                    errors.append(
                        f"{rel}: stable-reference/resource drift: "
                        f"{stable_ref} -> {entry['path']}, resource={resource}"
                    )

        for raw_link in _MARKDOWN_LINK.findall(body):
            target = _local_target(path, raw_link)
            if target is not None and not target.exists():
                errors.append(f"{rel}: local Markdown link target does not exist: {raw_link}")

    for error in errors:
        print(f"ERROR {error}")
    print(f"OKF v0.2 / SYNGAN producer-profile validation: {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
