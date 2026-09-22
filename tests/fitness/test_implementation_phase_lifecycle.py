from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTRACT = ROOT / "docs" / "implementation" / "implementation-phase-lifecycle-gate-evidence-contract.md"
REGISTRY = ROOT / "docs" / "authority" / "stable-reference-registry.json"


def test_implementation_phase_lifecycle_contract_is_current_and_routed() -> None:
    text = CONTRACT.read_text(encoding="utf-8")
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))

    entry = next(
        item
        for item in registry["references"]
        if item["ref"] == "syngan://implementation/phase-lifecycle"
    )
    assert entry["status"] == "active"
    assert entry["path"] == (
        "docs/implementation/implementation-phase-lifecycle-gate-evidence-contract.md"
    )

    for phrase in (
        "mandatory start gate",
        "Visible normative success obligations",
        "Independent challenge layer",
        "### E0 — authority and traceability",
        "### E1 — static and deterministic correctness",
        "### E2 — behavioral and compositional correctness",
        "### E3 — negative, failure, security, and recovery correctness",
        "### E4 — reproducibility, history, compatibility, and candidate qualification",
        "### E5 — external/provider/scale/release qualification",
        "Candidate freeze",
        "Completion establishes eligibility, not authorization.",
        "does not authorize product implementation",
    ):
        assert phrase in text


def test_active_program_stable_reference_targets_phase_017() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    by_ref = {item["ref"]: item for item in registry["references"]}

    current = by_ref["syngan://program/phase-017"]
    assert current["status"] == "active"
    assert current["path"] == "docs/phases/017/index.md"
    assert current["owner_family"] == "active_phase"

    prior = by_ref["syngan://program/phase-016"]
    assert prior["status"] == "retired"
    assert "path" not in prior
    assert prior["replacement_ref"] == "syngan://program/phase-017"
