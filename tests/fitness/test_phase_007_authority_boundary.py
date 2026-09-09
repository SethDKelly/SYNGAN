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


def test_007_c_execution_authority_is_bounded() -> None:
    authority_text = C_AUTHORITY.read_text(encoding="utf-8")

    assert "**007-C: AUTHORIZED / ACTIVE.**" in authority_text
    assert "**007-D through 007-K: NOT AUTHORIZED.**" in authority_text
    assert "does not authorize concept behavior" in authority_text
    assert "Import Linter SHALL become an executed verification gate" in authority_text


def test_phase_007_index_records_007_c_as_active_only() -> None:
    phase_text = PHASE.read_text(encoding="utf-8")

    assert "status: active" in phase_text
    assert "007-B" in phase_text and "COMPLETE" in phase_text
    assert "007-C" in phase_text and "AUTHORIZED / ACTIVE" in phase_text
    assert "007-D" in phase_text and "NOT AUTHORIZED" in phase_text


def test_production_source_tree_exists_only_after_007_c_authorization() -> None:
    assert (ROOT / "src" / "syngan").is_dir()
