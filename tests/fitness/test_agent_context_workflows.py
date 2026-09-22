from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
POLICY = ROOT / "docs" / "authority" / "agent-context-portable-workflows-tool-adapters.md"
BUDGET = ROOT / "docs" / "authority" / "agent-context-budget.json"
COMPAT = ROOT / "docs" / "authority" / "agent-tool-compatibility.json"
SKILLS = ROOT / ".agents" / "skills"
CLAUDE = ROOT / ".claude" / "CLAUDE.md"
COMMANDS = ROOT / ".claude" / "commands"
OWNERSHIP = ROOT / "docs" / "authority" / "canonical-knowledge-ownership-map.json"
REGISTRY = ROOT / "docs" / "authority" / "stable-reference-registry.json"
MANIFEST = ROOT / "docs" / "authority" / "okf-projection-manifest.json"

EXPECTED_SKILLS = {
    "resolve-context": "A1",
    "resolve-reference": "A1",
    "execute-selected-work": "A2",
    "review-change": "A1",
    "run-verification": "A1",
    "update-traceability": "A2",
}


def _frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "---"
    end = lines.index("---", 1)
    data: dict[str, str] = {}
    for line in lines[1:end]:
        key, value = line.split(":", maxsplit=1)
        data[key.strip()] = value.strip()
    return data


def test_context_budget_measurement_passes() -> None:
    subprocess.run(
        [sys.executable, "tools/measure_agent_context.py"],
        cwd=ROOT,
        check=True,
    )


def test_context_budget_is_provider_neutral_and_bounded() -> None:
    budget = json.loads(BUDGET.read_text(encoding="utf-8"))

    assert budget["unit"] == "utf8_bytes"
    assert budget["semantics"]["unit_is_provider_neutral"] is True
    assert budget["semantics"]["token_counts_are_normative"] is False
    assert budget["limits"]["agents_md"] <= 16 * 1024
    assert budget["limits"]["skill_each"] <= 8 * 1024
    assert budget["limits"]["claude_md"] <= 2 * 1024


def test_portable_skill_set_and_frontmatter_are_canonical() -> None:
    actual = {path.parent.name for path in SKILLS.glob("*/SKILL.md")}
    assert actual == set(EXPECTED_SKILLS)

    for name, action_class in EXPECTED_SKILLS.items():
        path = SKILLS / name / "SKILL.md"
        meta = _frontmatter(path)
        text = path.read_text(encoding="utf-8")

        assert set(meta) == {"name", "description"}
        assert meta["name"] == name
        assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)
        assert meta["description"]
        assert "## Boundary" in text
        assert "## Stop conditions" in text
        assert action_class in text


def test_claude_adapter_is_thin_and_routes_to_shared_sources() -> None:
    bridge = CLAUDE.read_text(encoding="utf-8")
    assert "@../AGENTS.md" in bridge
    assert "../.agents/skills/" in bridge
    assert "compatibility bridge only" in bridge

    for name in EXPECTED_SKILLS:
        command = (COMMANDS / f"{name}.md").read_text(encoding="utf-8")
        assert f"../../.agents/skills/{name}/SKILL.md" in command
        assert "adds no permission, scope, semantics" in command


def test_tool_compatibility_separates_documented_and_runtime_state() -> None:
    data = json.loads(COMPAT.read_text(encoding="utf-8"))
    providers = ("cursor", "codex", "claude_code")

    assert data["semantics"] == "documented_compatibility_is_not_runtime_certification"
    for provider in providers:
        entry = data["tools"][provider]
        assert entry["documented_state"] == "compatible"
        assert entry["runtime_state"] == "unverified"

    assert data["tools"]["cursor"]["workflow_source"] == ".agents/skills/"
    assert data["tools"]["codex"]["workflow_source"] == ".agents/skills/"
    assert "thin bridges" in data["tools"]["claude_code"]["adapter"]


def test_context_policy_preserves_progressive_disclosure_and_manual_fallback() -> None:
    text = POLICY.read_text(encoding="utf-8")

    for phrase in (
        "Loading another file requires a concrete question it answers.",
        "A known stable reference should bypass broad search",
        "Skills define how to perform a bounded human-selected task.",
        "Documented capability is not provider-runtime certification.",
        "do not fork or duplicate SYNGAN semantics to obtain UX parity",
        "016-F does not establish the full executable agentic conformance",
    ):
        assert phrase in text


def test_context_authority_is_canonical_stable_and_okf_routed() -> None:
    ownership = json.loads(OWNERSHIP.read_text(encoding="utf-8"))
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    owner = next(
        item
        for item in ownership["owners"]
        if item["family"] == "agent_context_workflows_tool_adapters"
    )
    expected_path = "docs/authority/agent-context-portable-workflows-tool-adapters.md"
    assert owner["path"] == expected_path

    stable = next(
        item
        for item in registry["references"]
        if item["ref"] == "syngan://authority/agent-context-workflows"
    )
    assert stable["status"] == "active"
    assert stable["owner_family"] == "agent_context_workflows_tool_adapters"
    assert stable["path"] == expected_path

    authority = next(group for group in manifest["groups"] if group["id"] == "authority")
    route = next(item for item in authority["routes"] if item["id"] == "agent-context-workflows")
    assert route["ref"] == stable["ref"]
