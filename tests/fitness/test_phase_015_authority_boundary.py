from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
IMPLEMENTATION = ROOT / "docs" / "implementation"
AUTHORITY = IMPLEMENTATION / "phase-015-current-implementation-authority-start-gate.md"
PHASE = ROOT / "docs" / "phases" / "015" / "index.md"
AGENTS = ROOT / "AGENTS.md"


def test_phase_015_current_authority_is_discoverable() -> None:
    authority_text = AUTHORITY.read_text(encoding="utf-8")

    assert "status: complete-current" in authority_text
    assert "015-A  AUTHORIZED" in authority_text
    assert "015-B..015-J  NOT AUTHORIZED" in authority_text
    assert "No domain implementation is authorized by this start gate." in authority_text


def test_phase_015_index_exposes_only_015_a_as_authorized_next_slice() -> None:
    phase_text = PHASE.read_text(encoding="utf-8")

    assert "status: active" in phase_text
    assert "015-A  AUTHORIZED / NEXT" in phase_text
    locked_phases = (
        "015-B",
        "015-C",
        "015-D",
        "015-E",
        "015-F",
        "015-G",
        "015-H",
        "015-I",
        "015-J",
    )
    for phase_id in locked_phases:
        assert f"{phase_id}  NOT AUTHORIZED" in phase_text


def test_agent_instructions_preserve_slice_bounded_authority() -> None:
    agent_text = AGENTS.read_text(encoding="utf-8")

    assert "015-A                                 AUTHORIZED / NEXT ELIGIBLE" in agent_text
    assert "015-B..015-J                          NOT AUTHORIZED" in agent_text
    assert "domain implementation remains NOT STARTED" in agent_text


def test_production_source_tree_exists_for_scaffold_reconciliation() -> None:
    assert (ROOT / "src" / "syngan").is_dir()
