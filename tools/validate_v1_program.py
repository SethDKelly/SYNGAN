from __future__ import annotations

import argparse
import json
from pathlib import Path

EXPECTED_THEMES = [f"V1-T{number:02d}" for number in range(1, 6)]
EXPECTED_M8 = [f"M8-R{number:02d}" for number in range(1, 5)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    repo = Path(parser.parse_args().repo).resolve()
    errors: list[str] = []

    profile_path = repo / "docs" / "implementation" / "v1-program-profile.json"
    registry_path = repo / "docs" / "authority" / "stable-reference-registry.json"
    manifest_path = repo / "docs" / "authority" / "okf-projection-manifest.json"
    status_path = repo / "docs" / "authority" / "current-repository-status.md"
    phase_026_path = repo / "docs" / "phases" / "026" / "phase-definition.md"

    for path in (profile_path, registry_path, manifest_path, status_path, phase_026_path):
        if not path.is_file():
            errors.append(f"missing v1 program surface: {path.relative_to(repo)}")

    if errors:
        for error in errors:
            print("ERROR", error)
        return 1

    profile = json.loads(profile_path.read_text(encoding="utf-8"))
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    status = status_path.read_text(encoding="utf-8")
    phase_026 = phase_026_path.read_text(encoding="utf-8")

    if profile.get("stable_ref") != "syngan://implementation/v1-program":
        errors.append("profile: stable-ref drift")

    semantics = profile.get("program_label_semantics", {})
    if semantics.get("v1_is_program_label") is not True:
        errors.append("profile: v1 must remain a program label")
    for key in (
        "implies_package_version_1_0_0",
        "implies_public_release",
        "implies_production_provider_support",
        "implies_enterprise_scale_support",
    ):
        if semantics.get(key) is not False:
            errors.append(f"profile: v1 label must not imply {key}")

    activation = profile.get("activation", {})
    if activation.get("next_named_phase") != "026":
        errors.append("profile: Phase 026 must remain the only named v1 re-entry phase")
    if activation.get("successful_phase_025_outcomes") != [
        "PASS",
        "PASS WITH CARRY-FORWARD",
    ]:
        errors.append("profile: v1 activation must follow successful Phase 025 outcome")
    if activation.get("phase_025_not_ready_allows_v1_activation") is not False:
        errors.append("profile: Phase 025 NOT READY must not activate v1")
    if activation.get("explicit_human_selection_required") is not True:
        errors.append("profile: Phase 026 must require explicit human selection")

    themes = [item.get("id") for item in profile.get("candidate_themes", [])]
    if themes != EXPECTED_THEMES:
        errors.append("profile: candidate themes must be V1-T01..V1-T05")
    if any(item.get("committed") is not False for item in profile.get("candidate_themes", [])):
        errors.append("profile: candidate v1 themes must remain uncommitted in Phase 017")

    classes = profile.get("extension_classification", {})
    if classes.get("ordinary_extension") != ["F-1", "F-2", "F-3", "F-4"]:
        errors.append("profile: ordinary extension classification drift")
    if classes.get("rediscovery") != ["F-5"]:
        errors.append("profile: F-5 must remain the rediscovery class")
    if classes.get("external_non_goal") != ["F-6"]:
        errors.append("profile: F-6 must remain external/non-goal")
    if classes.get("insufficient_evidence") != ["F-7"]:
        errors.append("profile: F-7 must remain deferred for insufficient evidence")

    m8 = [item.get("id") for item in profile.get("m8_rediscovery", [])]
    if m8 != EXPECTED_M8:
        errors.append("profile: four M8 rediscovery triggers must remain explicit")
    if profile["m8_rediscovery"][0].get("classification") != "F-5":
        errors.append("profile: formal composable privacy must remain F-5")
    if profile["m8_rediscovery"][1].get("classification") != "F-5":
        errors.append("profile: governance/publication lifecycle must remain F-5")
    if profile["m8_rediscovery"][3].get("classification") != "F-5":
        errors.append("profile: product-owned resource/economic lifecycle must remain F-5")

    deferred = profile.get("deferred_decisions", {})
    for key, value in deferred.items():
        if value is not True:
            errors.append(f"profile: deferred decision became prematurely fixed: {key}")

    phase_026_profile = profile.get("phase_026", {})
    if phase_026_profile.get("product_implementation") is not False:
        errors.append("profile: Phase 026 must remain planning-only")
    if phase_026_profile.get("self_authorizes_phase_027") is not False:
        errors.append("profile: Phase 026 must not self-authorize Phase 027")

    stable = next(
        (
            item
            for item in registry.get("references", [])
            if item.get("ref") == "syngan://implementation/v1-program"
        ),
        None,
    )
    expected_path = "docs/implementation/v1-coarse-program-deferrals-rediscovery-triggers.md"
    if not stable or stable.get("status") != "active":
        errors.append("stable reference: missing/inactive v1 program")
    elif stable.get("path") != expected_path:
        errors.append("stable reference: v1 program path drift")

    implementation = next(
        (group for group in manifest.get("groups", []) if group.get("id") == "implementation"),
        None,
    )
    route = (
        None
        if not implementation
        else next(
            (
                item
                for item in implementation.get("routes", [])
                if item.get("id") == "v1-program"
            ),
            None,
        )
    )
    if not route or route.get("ref") != "syngan://implementation/v1-program":
        errors.append("OKF manifest: v1 program route drift")

    for phrase in (
        "017-H                               COMPLETE",
        "product implementation execution   NOT AUTHORIZED",
        "active implementation packages     0",
    ):
        if phrase not in status:
            errors.append(f"current status: missing {phrase}")

    if "planned-not-authorized" not in phase_026:
        errors.append("Phase 026: planned-not-authorized status missing")
    if "Passing Phase 026 never authorizes Phase 027." not in phase_026:
        errors.append("Phase 026: no-self-progression boundary missing")

    for error in errors:
        print("ERROR", error)
    print(f"v1 coarse-program conformance: {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
