from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
IMPLEMENTATION = ROOT / "docs" / "implementation"
CURRENT = IMPLEMENTATION / (
    "phase-015-j-cross-slice-integration-residual-risk-closure-"
    "implementation-consolidation-authority.md"
)
PHASE = ROOT / "docs" / "phases" / "015" / "index.md"
AGENTS = ROOT / "AGENTS.md"


def test_phase_015_current_authority_is_discoverable() -> None:
    authority_text = CURRENT.read_text(encoding="utf-8")

    assert "status: active-current" in authority_text
    assert "015-A..015-I  COMPLETE" in authority_text
    assert "015-J         AUTHORIZED / ACTIVE" in authority_text
    assert "Phase 015     ACTIVE" in authority_text


def test_phase_015_index_exposes_015_j_as_active() -> None:
    phase_text = PHASE.read_text(encoding="utf-8")

    assert "status: active" in phase_text
    for phase_id in (
        "015-A",
        "015-B",
        "015-C",
        "015-D",
        "015-E",
        "015-F",
        "015-G",
        "015-H",
        "015-I",
    ):
        assert phase_id in phase_text and "COMPLETE" in phase_text

    assert "015-J" in phase_text and "AUTHORIZED / ACTIVE" in phase_text


def test_agent_instructions_preserve_active_015_j_authority_boundary() -> None:
    agent_text = AGENTS.read_text(encoding="utf-8")

    assert "015-A                                 COMPLETE" in agent_text
    assert "015-B                                 COMPLETE" in agent_text
    assert "015-C                                 COMPLETE" in agent_text
    assert "015-D                                 COMPLETE" in agent_text
    assert "015-E                                 COMPLETE" in agent_text
    assert "015-F                                 COMPLETE" in agent_text
    assert "015-G                                 COMPLETE" in agent_text
    assert "015-H                                 COMPLETE" in agent_text
    assert "015-I                                 COMPLETE" in agent_text
    assert "015-J                                 AUTHORIZED / ACTIVE" in agent_text


def test_015_j_c9_cross_slice_replay_is_present() -> None:
    assert (
        ROOT / "tests" / "integration" / "cross_slice" / "test_phase_015_cross_slice.py"
    ).is_file()
