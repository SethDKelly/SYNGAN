from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROFILE = ROOT / "docs" / "phases" / "017" / "phase-017-exit-profile.json"
STATUS = ROOT / "docs" / "authority" / "current-repository-status.md"


def test_phase_017_exit_is_pass_with_explicit_phase_018_carry_forward() -> None:
    profile = json.loads(PROFILE.read_text(encoding="utf-8"))

    assert profile["status"] == "complete"
    assert profile["decision"] == "PASS WITH CARRY-FORWARD"
    assert profile["baseline"]["project_version"] == "0.0.0"
    assert profile["baseline"]["active_implementation_packages"] == 0
    assert profile["baseline"]["product_implementation_during_phase_017"] is False

    assert [item["id"] for item in profile["carry_forward"]] == [
        f"P18-CF-{number:02d}" for number in range(1, 6)
    ]
    assert all(item["blocking_for_phase_018_pass"] for item in profile["carry_forward"])


def test_phase_017_exit_does_not_authorize_phase_018_or_product_implementation() -> None:
    profile = json.loads(PROFILE.read_text(encoding="utf-8"))
    phase_018 = profile["phase_018"]

    assert phase_018["next_eligible_at_exit"] is True
    assert phase_018["authorized_at_exit"] is False
    assert phase_018["product_implementation"] is False
    assert phase_018["may_pass_with_open_carry_forward"] is False
    assert profile["phase_019"]["authorized_at_exit"] is False

    status = STATUS.read_text(encoding="utf-8")
    assert "Phase 017                           COMPLETE" in status
    assert "Phase 018                           NEXT ELIGIBLE / NOT AUTHORIZED" in status
    assert "product implementation execution   NOT AUTHORIZED" in status
