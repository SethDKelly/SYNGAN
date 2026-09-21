from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
IMPLEMENTATION = ROOT / "docs" / "implementation"
PHASE_015_CURRENT = IMPLEMENTATION / (
    "phase-015-j-cross-slice-integration-residual-risk-closure-"
    "implementation-consolidation-authority.md"
)
PHASE_015 = ROOT / "docs" / "phases" / "015" / "index.md"
PHASE_016_AUTHORITY = ROOT / "docs" / "authority" / (
    "phase-016-documentation-okf-agentic-implementation-readiness-"
    "hardening-authority.md"
)
PHASE_016 = ROOT / "docs" / "phases" / "016" / "index.md"
PHASE_016_A = ROOT / "docs" / "phases" / "016" / (
    "016-A-documentation-corpus-current-owner-duplication-supersession-audit.md"
)
PHASE_016_INVENTORY = (
    ROOT / "docs" / "phases" / "016" / "016-A-documentation-corpus-inventory.json"
)
AGENTS = ROOT / "AGENTS.md"
RESIDUAL = IMPLEMENTATION / "phase-015-residual-risk-closure-support-scope-register.md"
METHODOLOGY = ROOT / "docs" / "authority" / "jackson-methodology-completion-matrix.md"
CONCEPTUAL_RESIDUAL = ROOT / "docs" / "authority" / "residual-conceptual-misfit-register.md"
POST_015 = (
    ROOT / "docs" / "authority" / "post-phase-015-methodology-documentation-reconciliation.md"
)


def test_phase_015_completion_authority_remains_closed() -> None:
    authority_text = PHASE_015_CURRENT.read_text(encoding="utf-8")
    phase_text = PHASE_015.read_text(encoding="utf-8")

    assert "status: complete-current" in authority_text
    assert "015-A..015-J  COMPLETE" in authority_text
    assert "Phase 015     COMPLETE" in authority_text
    assert "C9            ACTIVE / PASS" in authority_text
    assert "status: complete" in phase_text


def test_phase_016_hardening_authority_is_current() -> None:
    authority_text = PHASE_016_AUTHORITY.read_text(encoding="utf-8")
    phase_text = PHASE_016.read_text(encoding="utf-8")

    assert "status: active" in authority_text
    assert "Phase 016   AUTHORIZED / ACTIVE" in authority_text
    assert "016-A       COMPLETE" in authority_text
    assert "016-B       NEXT ELIGIBLE / NOT AUTHORIZED" in authority_text

    assert "status: active" in phase_text
    assert "016-A       COMPLETE" in phase_text
    assert "016-B       NEXT ELIGIBLE / NOT AUTHORIZED" in phase_text


def test_016_a_documentation_audit_evidence_is_present() -> None:
    audit_text = PHASE_016_A.read_text(encoding="utf-8")

    assert PHASE_016_INVENTORY.is_file()
    assert "full Markdown path inventory             COMPLETE" in audit_text
    assert "P16-3 semantic findings                  0" in audit_text
    assert "P16-4 product-scope findings             0" in audit_text
    assert "245 initial history candidates" in audit_text


def test_agent_instructions_preserve_phase_016_scope_boundary() -> None:
    agent_text = AGENTS.read_text(encoding="utf-8")

    assert "Phase 015                             COMPLETE" in agent_text
    assert "pre-implementation hardening          PHASE 016 ACTIVE" in agent_text
    assert "016-A                                 COMPLETE" in agent_text
    assert "016-B                                 NEXT ELIGIBLE / NOT AUTHORIZED" in agent_text
    assert "product/provider/runtime next          NOT AUTHORIZED" in agent_text


def test_phase_015_residual_closure_evidence_remains_present() -> None:
    assert (
        ROOT / "tests" / "integration" / "cross_slice" / "test_phase_015_cross_slice.py"
    ).is_file()
    residual_text = RESIDUAL.read_text(encoding="utf-8")
    for risk in range(1, 9):
        assert f"RR-0{risk}" in residual_text
    assert "unresolved implementation READINESS-RISK for current Phase 015 scope   0" in (
        residual_text
    )


def test_jackson_completion_remains_closed_during_phase_016() -> None:
    methodology_text = METHODOLOGY.read_text(encoding="utf-8")
    residual_text = CONCEPTUAL_RESIDUAL.read_text(encoding="utf-8")

    assert "JACKSON CONCEPT DESIGN              COMPLETE FOR CURRENT PRODUCT SCOPE" in (
        methodology_text
    )
    assert "PHASE 016                           ACTIVE — PRE-IMPLEMENTATION HARDENING" in (
        methodology_text
    )
    assert "M8 FUTURE REDISCOVERY GROUPS                    4 / DORMANT" in (
        residual_text
    )
    expected_phase_016 = (
        "PHASE 016                                        "
        "ACTIVE — PRE-IMPLEMENTATION HARDENING"
    )
    assert expected_phase_016 in residual_text


def test_post_phase_015_record_is_preserved_as_superseded_boundary_history() -> None:
    reconciliation_text = POST_015.read_text(encoding="utf-8")

    assert "status: superseded" in reconciliation_text
    assert "Subsequent Phase 016 state" in reconciliation_text
    assert "016-A       COMPLETE" in reconciliation_text
    assert "016-B       NEXT ELIGIBLE / NOT AUTHORIZED" in reconciliation_text
