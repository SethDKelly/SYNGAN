from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROFILE = ROOT / "docs" / "implementation" / "v0x-mvp-boundary-profile.json"
REGISTRY = ROOT / "docs" / "authority" / "stable-reference-registry.json"
MANIFEST = ROOT / "docs" / "authority" / "okf-projection-manifest.json"


def test_v0x_mvp_profile_separates_capability_from_release_and_support() -> None:
    profile = json.loads(PROFILE.read_text(encoding="utf-8"))

    assert profile["definition"] == "qualified_package_capability_not_public_release"
    assert profile["required_capabilities"] == [f"MVP-C{number:02d}" for number in range(1, 9)]
    assert profile["baseline_support"]["verified_python"] == ["3.11"]
    assert profile["baseline_support"]["bounded_spark_capable_path_required"] is True
    assert profile["baseline_support"]["production_provider_support_required"] is False
    assert profile["baseline_support"]["enterprise_scale_support_required"] is False

    assert [item["id"] for item in profile["capability_milestones"]] == [
        f"MVP-M{number}" for number in range(8)
    ]

    version = profile["version_policy"]
    assert version["phase_number_is_package_version"] is False
    assert version["placeholder_version"] == "0.0.0"
    assert version["change_placeholder_during_phase_017"] is False
    assert version["non_placeholder_required_by"] == "MVP-M6"
    assert version["exact_candidate_version_selected_by_phase"] == "024"
    assert version["non_placeholder_version_implies_release_candidate"] is False

    for number in range(1, 7):
        assert profile["residual_mapping"][f"RR-016-{number:02d}"]["blocks_package_mvp"] is False


def test_v0x_mvp_boundary_is_current_routed_authority() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    stable = next(
        item
        for item in registry["references"]
        if item["ref"] == "syngan://implementation/v0x-mvp-boundary"
    )
    assert stable["status"] == "active"
    assert stable["owner_family"] == "v0x_mvp_scope_version_release_boundary"
    assert stable["path"] == (
        "docs/implementation/v0x-package-mvp-scope-version-release-boundaries.md"
    )

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    implementation = next(group for group in manifest["groups"] if group["id"] == "implementation")
    route = next(item for item in implementation["routes"] if item["id"] == "v0x-mvp-boundary")
    assert route["ref"] == stable["ref"]
