from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BUDGET_PATH = ROOT / "docs" / "authority" / "agent-context-budget.json"


def _size(path: Path) -> int:
    return path.stat().st_size if path.is_file() else 0


def _check(errors: list[str], label: str, observed: int, limit: int) -> None:
    state = "PASS" if observed <= limit else "FAIL"
    print(f"{state} {label}: {observed} / {limit} bytes")
    if observed > limit:
        errors.append(f"{label}: {observed} exceeds {limit} bytes")


def main() -> int:
    config: dict[str, Any] = json.loads(BUDGET_PATH.read_text(encoding="utf-8"))
    limits: dict[str, int] = config["limits"]
    errors: list[str] = []

    agents = ROOT / "AGENTS.md"
    claude = ROOT / ".claude" / "CLAUDE.md"
    cursor_rules = sorted((ROOT / ".cursor" / "rules").glob("*.mdc"))
    skills = sorted((ROOT / ".agents" / "skills").glob("*/SKILL.md"))
    commands = sorted((ROOT / ".claude" / "commands").glob("*.md"))
    knowledge = ROOT / "knowledge"

    _check(errors, "AGENTS.md", _size(agents), limits["agents_md"])
    _check(errors, ".claude/CLAUDE.md", _size(claude), limits["claude_md"])

    for path in cursor_rules:
        _check(
            errors,
            path.relative_to(ROOT).as_posix(),
            _size(path),
            limits["cursor_rule_each"],
        )
    _check(
        errors,
        "Cursor rules aggregate",
        sum(_size(path) for path in cursor_rules),
        limits["cursor_rules_aggregate"],
    )

    for path in skills:
        _check(
            errors,
            path.relative_to(ROOT).as_posix(),
            _size(path),
            limits["skill_each"],
        )
    _check(
        errors,
        "skills aggregate",
        sum(_size(path) for path in skills),
        limits["skills_aggregate"],
    )

    for path in commands:
        _check(
            errors,
            path.relative_to(ROOT).as_posix(),
            _size(path),
            limits["claude_command_each"],
        )
    _check(
        errors,
        "Claude commands aggregate",
        sum(_size(path) for path in commands),
        limits["claude_commands_aggregate"],
    )

    _check(
        errors,
        "Cursor/Codex persistent baseline",
        _size(agents),
        limits["cursor_codex_persistent_baseline"],
    )
    _check(
        errors,
        "Claude persistent baseline",
        _size(agents) + _size(claude),
        limits["claude_persistent_baseline"],
    )

    root_index = knowledge / "index.md"
    _check(
        errors,
        "knowledge/index.md",
        _size(root_index),
        limits["knowledge_root_index"],
    )

    for path in sorted(knowledge.rglob("*.md")):
        if path == root_index:
            continue
        if path.name == "index.md":
            limit = limits["knowledge_nested_index_each"]
        else:
            limit = limits["knowledge_concept_each"]
        _check(errors, path.relative_to(ROOT).as_posix(), _size(path), limit)

    for error in errors:
        print(f"ERROR {error}")
    print(f"Agent context budget check: {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
