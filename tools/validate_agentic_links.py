from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import urlparse

LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def _target(source: Path, raw: str, repo: Path) -> Path | None:
    value = raw.strip().split("#", maxsplit=1)[0].strip()
    if not value or value.startswith(("http://", "https://", "mailto:")):
        return None
    if urlparse(value).scheme:
        return None
    return (
        (repo / value.lstrip("/")).resolve()
        if value.startswith("/")
        else (source.parent / value).resolve()
    )


def _files(repo: Path) -> list[Path]:
    paths = [
        repo / "AGENTS.md",
        repo / "docs" / "index.md",
        repo / "docs" / "authority" / "current-repository-status.md",
        repo / "docs" / "authority" / "agent-authority-human-directed-scope-security-trust.md",
        repo / "docs" / "authority" / "agent-context-portable-workflows-tool-adapters.md",
        repo / "docs" / "authority" / "agentic-conformance-policy.md",
        repo / "docs" / "phases" / "016" / "index.md",
    ]
    for root in (repo / ".agents", repo / ".claude"):
        if root.exists():
            paths.extend(path for path in root.rglob("*.md") if path.is_file())
    return sorted(set(paths))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    repo = Path(parser.parse_args().repo).resolve()
    errors: list[str] = []

    for path in _files(repo):
        if not path.is_file():
            errors.append(f"missing agent-facing current file: {path.relative_to(repo)}")
            continue
        text = path.read_text(encoding="utf-8")
        for raw in LINK.findall(text):
            target = _target(path, raw, repo)
            if target is not None and not target.exists():
                errors.append(f"{path.relative_to(repo)}: broken local Markdown link target: {raw}")

    for error in errors:
        print("ERROR", error)
    print(f"Agent-facing link validation: {len(errors)} error(s), {len(_files(repo))} file(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
