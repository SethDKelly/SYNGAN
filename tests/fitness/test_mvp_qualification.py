from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROFILE = ROOT / "docs" / "implementation" / "mvp-qualification-profile.json"
REGISTRY = ROOT / "docs" / "authority" / "stable-reference-registry.json"


def test_mvp_qualification_is_non_compensatory_and_independent() -> None:
    profile = json.loads(PROFILE.read_text(encoding="utf-8"))

    assert profile["mode"] == "independent_non_compensatory_by_blocking_obligation"
    assert profile["minimum_independence"] == "EI1"
    assert profile["preferred_independence"] == "EI2"
    assert profile["e5_required_for_bounded_mvp"] is False
    assert [item["id"] for item in profile["qualification_layers"]] == [
        f"QL-{number:02d}" for number in range(1, 11)
    ]

    challenge = profile["challenge_policy"]
    assert challenge["budgets_frozen_before_holdout"] is True
    assert challenge["thresholds_may_be_set_post_hoc"] is False
    assert challenge["failed_generated_cases_preserved"] is True
    assert challenge["cherry_picked_retries_allowed"] is False
    assert challenge["aggregate_score_can_override_blocking_failure"] is False
    assert challenge["universal_mutation_percentage_threshold"] is None


def test_mvp_qualification_repairs_require_new_candidate_and_fresh_h1() -> None:
    profile = json.loads(PROFILE.read_text(encoding="utf-8"))
    candidate = profile["candidate_rules"]
    decision = profile["decision_rules"]

    assert candidate["evaluator_may_modify_frozen_candidate"] is False
    assert candidate["product_change_invalidates_candidate"] is True
    assert candidate["affected_evidence_must_rerun"] is True
    assert candidate["exposed_h1_becomes_v1_regression"] is True
    assert candidate["fresh_h1_for_affected_obligations"] is True
    assert candidate["unaffected_evidence_reuse_requires_impact_justification"] is True

    assert decision["pass_requires_all_blocking_obligations"] is True
    assert decision["pass_with_carry_forward_requires_all_blocking_obligations"] is True
    assert decision["carry_forward_only_nonblocking"] is True
    assert decision["blocking_candidate_defect_requires_not_ready"] is True
    assert decision["evaluator_repair_authorizes_pass"] is False


def test_mvp_qualification_has_current_stable_reference() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    stable = next(
        item
        for item in registry["references"]
        if item["ref"] == "syngan://implementation/mvp-qualification"
    )
    assert stable["status"] == "active"
    assert stable["owner_family"] == "mvp_completion_qualification"
