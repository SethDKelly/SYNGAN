from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

EXPECTED_SKILLS = {
    "resolve-context",
    "resolve-reference",
    "execute-selected-work",
    "review-change",
    "run-verification",
}
ALWAYS_TRUE = re.compile(r"^\s*alwaysApply\s*:\s*true\s*$", re.M | re.I)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    repo = Path(parser.parse_args().repo).resolve()
    errors: list[str] = []

    budget = json.loads(
        (repo / "docs" / "authority" / "agent-context-budget.json").read_text(encoding="utf-8")
    )
    limits = budget["limits"]

    for forbidden in (
        repo / "CLAUDE.md",
        repo / "CODEX.md",
        repo / ".codex" / "AGENTS.md",
        repo / ".claude" / "skills",
    ):
        if forbidden.exists():
            errors.append(
                f"competing provider semantic surface is not allowed: {forbidden.relative_to(repo)}"
            )

    claude = repo / ".claude" / "CLAUDE.md"
    if not claude.is_file():
        errors.append("missing .claude/CLAUDE.md compatibility bridge")
    else:
        text = claude.read_text(encoding="utf-8")
        for token in ("@../AGENTS.md", "../.agents/skills/", "compatibility bridge only"):
            if token not in text:
                errors.append(f".claude/CLAUDE.md must preserve shared routing token: {token}")
        if claude.stat().st_size > int(limits["claude_md"]):
            errors.append(".claude/CLAUDE.md exceeds the configured thin-bridge budget")

    commands = repo / ".claude" / "commands"
    actual_commands = {path.stem for path in commands.glob("*.md")} if commands.is_dir() else set()
    if actual_commands != EXPECTED_SKILLS:
        errors.append(
            "Claude command bridge set drift: "
            f"expected {sorted(EXPECTED_SKILLS)}, found {sorted(actual_commands)}"
        )
    for name in EXPECTED_SKILLS:
        path = commands / f"{name}.md"
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        expected = f"../../.agents/skills/{name}/SKILL.md"
        if expected not in text:
            errors.append(f"{path.relative_to(repo)} must route to {expected}")
        if "adds no permission, scope, semantics" not in text:
            errors.append(f"{path.relative_to(repo)} must preserve the no-authority bridge rule")
        if path.stat().st_size > int(limits["claude_command_each"]):
            errors.append(f"{path.relative_to(repo)} exceeds the configured bridge budget")

    cursor_rules = repo / ".cursor" / "rules"
    if cursor_rules.exists():
        total = 0
        for path in sorted(cursor_rules.glob("*.mdc")):
            text = path.read_text(encoding="utf-8")
            total += path.stat().st_size
            if ALWAYS_TRUE.search(text):
                errors.append(
                    f"{path.relative_to(repo)}: alwaysApply true is not authorized by current policy"
                )
            if path.stat().st_size > int(limits["cursor_rule_each"]):
                errors.append(f"{path.relative_to(repo)} exceeds the configured Cursor rule budget")
        if total > int(limits["cursor_rules_aggregate"]):
            errors.append("Cursor project rules exceed the configured aggregate budget")

    manifest_path = repo / "docs" / "authority" / "agent-tool-compatibility.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid tool compatibility manifest: {exc}")
        manifest = {}

    if manifest.get("semantics") != "documented_compatibility_is_not_runtime_certification":
        errors.append("tool compatibility manifest must separate documentation from runtime proof")

    tools = manifest.get("tools", {})
    for name in ("cursor", "codex", "claude_code"):
        entry = tools.get(name)
        if not isinstance(entry, dict):
            errors.append(f"tool compatibility manifest missing {name}")
            continue
        if entry.get("documented_state") != "compatible":
            errors.append(f"{name}: documented_state must remain compatible")
        if entry.get("runtime_state") != "unverified":
            errors.append(
                f"{name}: runtime_state must remain unverified without separate runtime evidence"
            )
        if entry.get("workflow_source") != ".agents/skills/":
            errors.append(f"{name}: workflow_source must remain .agents/skills/")

    if tools.get("cursor", {}).get("adapter") != "none_required":
        errors.append("Cursor must not acquire a duplicate semantic adapter")
    if tools.get("codex", {}).get("adapter") != "none_required":
        errors.append("Codex must not acquire a duplicate semantic adapter")
    if "thin bridges" not in str(tools.get("claude_code", {}).get("adapter", "")):
        errors.append("Claude Code adapter must remain thin bridges to canonical skills")

    ordinary = tools.get("ordinary_ide_cli", {})
    if ordinary.get("runtime_state") != "available_without_agent_provider":
        errors.append("ordinary IDE/CLI fallback must remain available without an agent provider")

    for error in errors:
        print("ERROR", error)
    print(f"Agent adapter validation: {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
