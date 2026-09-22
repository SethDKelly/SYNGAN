from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"

_LINK = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
_FENCE = re.compile(r"~~~.*?~~~|\x60\x60\x60.*?\x60\x60\x60", re.DOTALL)


def _target_path(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]

    if re.match(r"^(?:https?|mailto|tel):", target, flags=re.IGNORECASE):
        return None
    if target.startswith("#"):
        return None

    title_match = re.match(r"""^(\S+?)\s+(?:"[^"]*"|'[^']*')$""", target)
    if title_match:
        target = title_match.group(1)

    target = unquote(target.split("#", maxsplit=1)[0].split("?", maxsplit=1)[0])
    if not target:
        return None

    if target.startswith("/"):
        return ROOT / target.lstrip("/")
    return (source.parent / target).resolve()


def test_repository_markdown_relative_links_resolve() -> None:
    broken: list[str] = []

    for source in sorted(DOCS.rglob("*.md")):
        content = source.read_text(encoding="utf-8")
        content = _FENCE.sub("", content)

        for match in _LINK.finditer(content):
            raw_target = match.group(1)
            target = _target_path(source, raw_target)
            if target is None:
                continue

            if target.is_dir():
                continue
            if target.exists():
                continue
            if (target / "index.md").exists():
                continue

            broken.append(
                f"{source.relative_to(ROOT)} -> {raw_target} "
                f"(resolved {target.relative_to(ROOT) if target.is_relative_to(ROOT) else target})"
            )

    assert not broken, "Broken repository-local Markdown links:\n" + "\n".join(broken)
