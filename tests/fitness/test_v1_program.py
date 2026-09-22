from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROFILE = ROOT / "docs" / "implementation" / "v1-program-profile.json"
REGISTRY = ROOT / "docs" / "authority" / "stable-reference-registry.json"


def test_v1_program_is_coarse_evidence_driven_and_not_a_version_promise() -> None:
    profile = json.loads(PROFILE.read_text(encoding="utf-8"))
    semantics = profile["program_label_semantics"]
    activation = profile["activation"]

    assert semantics["v1_is_program_label"] is True
    assert semantics["implies_package_version_1_0_0"] is False
    assert semantics["implies_public_release"] is False
    assert semantics["implies_production_provider_support"] is False
    assert semantics["implies_enterprise_scale_support"] is False

    assert activation["next_named_phase"] == "026"
    assert activation["successful_phase_025_outcomes"] == [
        "PASS",
        "PASS WITH CARRY-FORWARD",
    ]
    assert activation["phase_025_not_ready_allows_v1_activation"] is False
    assert activation["explicit_human_selection_required"] is True

    assert [item["id"] for item in profile["candidate_themes"]] == [
        f"V1-T{number:02d}" for number in range(1, 6)
    ]
    assert all(item["committed"] is False for item in profile["candidate_themes"])


def test_v1_program_preserves_m8_rediscovery_and_deferrals() -> None:
    profile = json.loads(PROFILE.read_text(encoding="utf-8"))

    assert profile["extension_classification"]["ordinary_extension"] == [
        "F-1",
        "F-2",
        "F-3",
        "F-4",
    ]
    assert profile["extension_classification"]["rediscovery"] == ["F-5"]
    assert [item["id"] for item in profile["m8_rediscovery"]] == [
        f"M8-R{number:02d}" for number in range(1, 5)
    ]
    assert all(profile["deferred_decisions"].values())

    phase_026 = profile["phase_026"]
    assert phase_026["product_implementation"] is False
    assert phase_026["derives_future_phase_graph"] is True
    assert phase_026["self_authorizes_phase_027"] is False


def test_v1_program_has_current_stable_reference() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    stable = next(
        item
        for item in registry["references"]
        if item["ref"] == "syngan://implementation/v1-program"
    )
    assert stable["status"] == "active"
    assert stable["owner_family"] == "v1_coarse_program"
