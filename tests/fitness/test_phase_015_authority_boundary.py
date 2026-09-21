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
METHODOLOGY = ROOT / "docs" / "authority" / "jackson-methodology-completion-matrix.md"
CONCEPTUAL_RESIDUAL = ROOT / "docs" / "authority" / "residual-conceptual-misfit-register.md"
POST_015 = (
    ROOT / "docs" / "authority" / "post-phase-015-methodology-documentation-reconciliation.md"
)


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



def test_post_phase_015_methodology_reconciliation_is_current() -> None:
    methodology_text = METHODOLOGY.read_text(encoding="utf-8")
    residual_text = CONCEPTUAL_RESIDUAL.read_text(encoding="utf-8")
    reconciliation_text = POST_015.read_text(encoding="utf-8")

    assert "JACKSON CONCEPT DESIGN              COMPLETE FOR CURRENT PRODUCT SCOPE" in (
        methodology_text
    )
    assert "PHASE 015                           COMPLETE" in methodology_text
    assert "PHASE 016                           NOT DEFINED" in methodology_text

    assert "M8 FUTURE REDISCOVERY GROUPS                    4 / DORMANT" in (residual_text)
    assert "PHASE 015                                        COMPLETE" in residual_text
    assert "PHASE 016                                        NOT DEFINED" in residual_text

    assert "PHASE 016                       NOT DEFINED" in reconciliation_text
    assert "POST-PHASE-015 DELIVERY AUTHORITY   NONE" in reconciliation_text


def test_no_phase_016_authority_is_created_by_reconciliation() -> None:
    assert not (ROOT / "docs" / "phases" / "016").exists()
    assert not list((ROOT / "docs" / "authority").glob("*phase-016*"))
    assert not list((ROOT / "docs" / "implementation").glob("*phase-016*"))
