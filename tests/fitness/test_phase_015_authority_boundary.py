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
RESIDUAL = IMPLEMENTATION / "phase-015-residual-risk-closure-support-scope-register.md"


def test_phase_015_completion_authority_is_discoverable() -> None:
    authority_text = CURRENT.read_text(encoding="utf-8")

    assert "status: complete-current" in authority_text
    assert "015-A..015-J  COMPLETE" in authority_text
    assert "Phase 015     COMPLETE" in authority_text
    assert "C9            ACTIVE / PASS" in authority_text
    assert "NEXT STAGE    NONE AUTHORIZED" in authority_text


def test_phase_015_index_is_complete_without_auto_authorizing_next_program() -> None:
    phase_text = PHASE.read_text(encoding="utf-8")

    assert "status: complete" in phase_text
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
        "015-J",
    ):
        assert phase_id in phase_text and "COMPLETE" in phase_text

    assert "POST-PHASE-015 START GATE — NOT AUTHORIZED" in phase_text


def test_agent_instructions_preserve_completed_phase_015_boundary() -> None:
    agent_text = AGENTS.read_text(encoding="utf-8")

    assert "Phase 015                             COMPLETE" in agent_text
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
        "015-J",
    ):
        assert phase_id in agent_text and "COMPLETE" in agent_text

    assert "POST-PHASE-015 START GATE — NOT AUTHORIZED" in agent_text


def test_015_j_c9_and_residual_closure_evidence_are_present() -> None:
    assert (
        ROOT / "tests" / "integration" / "cross_slice" / "test_phase_015_cross_slice.py"
    ).is_file()
    residual_text = RESIDUAL.read_text(encoding="utf-8")
    for risk in range(1, 9):
        assert f"RR-0{risk}" in residual_text
    assert "unresolved implementation READINESS-RISK for current Phase 015 scope   0" in (
        residual_text
    )
    assert "POST-PHASE-015" not in residual_text or "No post-Phase-015 stage is authorized" in (
        residual_text
    )
