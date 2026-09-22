from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROFILE = ROOT / "docs" / "implementation" / "v0x-program-profile.json"
REGISTRY = ROOT / "docs" / "authority" / "stable-reference-registry.json"


def test_v0x_program_is_phase_sequential_and_package_bounded() -> None:
    profile = json.loads(PROFILE.read_text(encoding="utf-8"))

    assert profile["phase_order"] == [f"{number:03d}" for number in range(18, 26)]
    assert profile["phase_level_dependency_mode"] == "strict_sequential"
    assert profile["cross_phase_concurrency"] is False

    package = profile["package_strategy"]
    assert package["phase_is_package"] is False
    assert package["package_is_smaller_than_phase"] is True
    assert package["actual_packages_derived_by_selected_phase_start_gate"] is True
    assert package["roadmap_package_families_are_authorization"] is False
    assert package["package_creation_authorizes_work"] is False
    assert package["one_branch_per_package_default"] is True
    assert package["concurrent_packages_default"] is False
    assert package["cross_phase_packages_allowed"] is False
    assert package["package_completion_authorizes_next"] is False
    assert package["phase_completion_authorizes_next"] is False


def test_phase_025_is_evaluation_only_and_repairs_require_reentry() -> None:
    profile = json.loads(PROFILE.read_text(encoding="utf-8"))
    repair = profile["qualification_repair"]

    assert repair["phase_025_evaluator_may_modify_frozen_candidate"] is False
    assert repair["phase_025_contains_product_implementation_packages"] is False
    assert repair["defect_requires_not_ready_disposition"] is True
    assert repair["repair_requires_explicit_human_authorization"] is True
    assert repair["repair_routes_to_smallest_owning_phase_or_package"] is True
    assert repair["class_3_4_reopen_rules_apply"] is True
    assert repair["new_candidate_freeze_required_after_repair"] is True
    assert repair["fresh_holdout_required_after_repair"] is True


def test_v0x_program_has_current_stable_reference() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    stable = next(
        item
        for item in registry["references"]
        if item["ref"] == "syngan://implementation/v0x-program"
    )
    assert stable["status"] == "active"
    assert stable["owner_family"] == "v0x_implementation_program"
