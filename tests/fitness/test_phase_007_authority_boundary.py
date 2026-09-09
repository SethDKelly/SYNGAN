from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOCK = ROOT / "docs" / "implementation" / "phase-007-implementation-authority-lock.md"
PHASE = ROOT / "docs" / "phases" / "007" / "index.md"


def test_phase_007_lock_authorizes_007_b_only() -> None:
    lock_text = LOCK.read_text(encoding="utf-8")

    assert "**007-B: AUTHORIZED.**" in lock_text
    assert "**007-C through 007-K: NOT YET AUTHORIZED.**" in lock_text
    assert "007-B MUST NOT create `src/syngan/`" in lock_text


def test_phase_007_index_points_to_007_b_as_current_authorized_group() -> None:
    phase_text = PHASE.read_text(encoding="utf-8")

    assert "status: active" in phase_text
    assert "007-A" in phase_text
    assert "007-B" in phase_text
    assert "007-C" in phase_text
    assert "007-B" in phase_text and "authorized" in phase_text.lower()


def test_no_production_source_tree_exists_before_007_c() -> None:
    assert not (ROOT / "src" / "syngan").exists()
