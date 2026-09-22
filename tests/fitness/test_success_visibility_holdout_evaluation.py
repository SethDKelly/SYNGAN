from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROFILE = ROOT / "docs" / "implementation" / "evaluation-method-profile.json"
REGISTRY = ROOT / "docs" / "authority" / "stable-reference-registry.json"
MANIFEST = ROOT / "docs" / "authority" / "okf-projection-manifest.json"


def test_split_visibility_profile_is_bounded_and_non_gamable() -> None:
    profile = json.loads(PROFILE.read_text(encoding="utf-8"))

    assert profile["stable_ref"] == "syngan://implementation/evaluation-method"
    assert profile["invariant"] == "requirements_visible_challenge_realization_holdout"
    assert profile["visibility_classes"]["V0"]["implementer_visible"] is True
    assert profile["visibility_classes"]["V0"]["frozen_before_implementation"] is True
    assert profile["visibility_classes"]["H1"]["implementer_visible_pre_evaluation"] is False
    assert (
        profile["visibility_classes"]["H1"]["generated_or_selected_after_candidate_freeze"]
        is True
    )
    assert profile["minimum_agent_assisted_phase_exit_independence"] == "EI1"
    assert [x["id"] for x in profile["challenge_families"]] == [
        f"CH-{n:02d}" for n in range(1, 9)
    ]
    assert profile["anti_gaming_controls"] == [f"AG-{n:02d}" for n in range(1, 13)]

    rules = profile["decision_rules"]
    assert rules["hidden_requirements_allowed"] is False
    assert rules["blocking_obligation_non_compensatory"] is True
    assert rules["aggregate_score_may_override_blocking_failure"] is False
    assert rules["post_hoc_thresholds_allowed"] is False

    assert (
        profile["contamination"]["exposed_holdout_case_becomes"]
        == "representative_regression_evidence"
    )
    assert profile["contamination"]["fresh_holdout_required_after_repair"] is True


def test_evaluation_method_has_current_stable_and_okf_routes() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    stable = next(
        x for x in registry["references"]
        if x["ref"] == "syngan://implementation/evaluation-method"
    )
    assert stable["status"] == "active"
    assert stable["owner_family"] == "success_visibility_holdout_evaluation"
    assert stable["path"] == (
        "docs/implementation/success-visibility-holdout-evaluation-anti-gaming.md"
    )

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    implementation = next(x for x in manifest["groups"] if x["id"] == "implementation")
    route = next(
        x for x in implementation["routes"]
        if x["id"] == "success-visibility-holdout-evaluation"
    )
    assert route["ref"] == stable["ref"]
