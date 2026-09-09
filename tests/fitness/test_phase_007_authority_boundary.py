from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOCK = ROOT / "docs" / "implementation" / "phase-007-implementation-authority-lock.md"
C_AUTHORITY = (
    ROOT / "docs" / "implementation" / "phase-007-c-source-package-topology-execution-authority.md"
)
PHASE = ROOT / "docs" / "phases" / "007" / "index.md"


def test_phase_007_lock_preserves_incremental_authority_model() -> None:
    lock_text = LOCK.read_text(encoding="utf-8")

    assert "Phase 007 uses **incremental authority**" in lock_text
    assert "Class 3" in lock_text
    assert "Class 4" in lock_text


def test_007_c_completed_authority_preserves_topology_and_locks_007_d() -> None:
    authority_text = C_AUTHORITY.read_text(encoding="utf-8")

    assert "**007-C: COMPLETE — TOPOLOGY CONTRACT REMAINS ACTIVE.**" in authority_text
    assert "**007-D: NOT YET AUTHORIZED — NEXT ELIGIBLE.**" in authority_text
    assert "Import Linter is the executable architecture-fitness mechanism" in authority_text
    assert "This contract does not itself authorize later behavior" in authority_text


def test_phase_007_index_records_007_c_complete_and_007_d_locked() -> None:
    phase_text = PHASE.read_text(encoding="utf-8")

    assert "status: active" in phase_text
    assert "007-B" in phase_text and "COMPLETE" in phase_text
    assert "007-C" in phase_text and "COMPLETE" in phase_text
    assert "007-D  NOT AUTHORIZED — NEXT ELIGIBLE" in phase_text
    assert (
        "An explicit proceed decision is required before 007-D implementation begins" in phase_text
    )


def test_production_source_tree_exists_after_completed_007_c() -> None:
    assert (ROOT / "src" / "syngan").is_dir()
