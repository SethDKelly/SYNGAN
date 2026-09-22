from __future__ import annotations

import argparse
import json
from pathlib import Path


EXPECTED_PHASES = [f"{number:03d}" for number in range(18, 26)]
EXPECTED_EDGES = [[EXPECTED_PHASES[i], EXPECTED_PHASES[i + 1]] for i in range(7)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    repo = Path(parser.parse_args().repo).resolve()
    errors: list[str] = []

    profile_path = repo / "docs" / "implementation" / "v0x-program-profile.json"
    registry_path = repo / "docs" / "authority" / "stable-reference-registry.json"
    manifest_path = repo / "docs" / "authority" / "okf-projection-manifest.json"
    status_path = repo / "docs" / "authority" / "current-repository-status.md"

    for path in (profile_path, registry_path, manifest_path, status_path):
        if not path.is_file():
            errors.append(f"missing v0.x program surface: {path.relative_to(repo)}")

    for phase in EXPECTED_PHASES:
        definition = repo / "docs" / "phases" / phase / "phase-definition.md"
        if not definition.is_file():
            errors.append(f"missing planned phase definition: {definition.relative_to(repo)}")

    if errors:
        for error in errors:
            print("ERROR", error)
        return 1

    profile = json.loads(profile_path.read_text(encoding="utf-8"))
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    status = status_path.read_text(encoding="utf-8")

    if profile.get("stable_ref") != "syngan://implementation/v0x-program":
        errors.append("profile: stable-ref drift")
    if profile.get("phase_order") != EXPECTED_PHASES:
        errors.append("profile: phase order must be 018..025")
    if profile.get("phase_level_dependency_mode") != "strict_sequential":
        errors.append("profile: initial v0.x phase dependency must remain strict sequential")
    if profile.get("dependency_edges") != EXPECTED_EDGES:
        errors.append("profile: dependency edges must preserve 018 -> ... -> 025")
    if profile.get("cross_phase_concurrency") is not False:
        errors.append("profile: cross-phase implementation concurrency must remain disabled")

    phases = {item.get("phase"): item for item in profile.get("phases", [])}
    expected_milestones = {
        "018": "MVP-M0",
        "019": "MVP-M1",
        "020": "MVP-M2",
        "021": "MVP-M3",
        "022": "MVP-M4",
        "023": "MVP-M5",
        "024": "MVP-M6",
        "025": "MVP-M7",
    }
    if set(phases) != set(EXPECTED_PHASES):
        errors.append("profile: phase definitions must cover exactly 018..025")
    else:
        for phase, milestone in expected_milestones.items():
            if phases[phase].get("milestone") != milestone:
                errors.append(f"profile: Phase {phase} milestone drift")

    package = profile.get("package_strategy", {})
    required_true = (
        "package_is_smaller_than_phase",
        "actual_packages_derived_by_selected_phase_start_gate",
        "one_branch_per_package_default",
    )
    for key in required_true:
        if package.get(key) is not True:
            errors.append(f"profile: package strategy must keep {key}=true")
    required_false = (
        "phase_is_package",
        "roadmap_package_families_are_authorization",
        "package_creation_authorizes_work",
        "concurrent_packages_default",
        "cross_phase_packages_allowed",
        "package_completion_authorizes_next",
        "phase_completion_authorizes_next",
    )
    for key in required_false:
        if package.get(key) is not False:
            errors.append(f"profile: package strategy must keep {key}=false")

    repair = profile.get("qualification_repair", {})
    if repair.get("phase_025_evaluator_may_modify_frozen_candidate") is not False:
        errors.append("profile: Phase 025 evaluator must not modify frozen candidate")
    if repair.get("phase_025_contains_product_implementation_packages") is not False:
        errors.append("profile: Phase 025 must remain evaluation-only")
    if repair.get("repair_requires_explicit_human_authorization") is not True:
        errors.append("profile: Phase 025 repair must require explicit authorization")
    if repair.get("new_candidate_freeze_required_after_repair") is not True:
        errors.append("profile: repair must produce a new candidate freeze")
    if repair.get("fresh_holdout_required_after_repair") is not True:
        errors.append("profile: repair must require fresh holdout")

    stable = next(
        (
            item
            for item in registry.get("references", [])
            if item.get("ref") == "syngan://implementation/v0x-program"
        ),
        None,
    )
    expected_path = (
        "docs/implementation/"
        "v0x-implementation-program-phase-018-025-dependency-package-strategy.md"
    )
    if not stable or stable.get("status") != "active":
        errors.append("stable reference: missing/inactive v0.x program")
    elif stable.get("path") != expected_path:
        errors.append("stable reference: v0.x program path drift")

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
                if item.get("id") == "v0x-implementation-program"
            ),
            None,
        )
    )
    if not route or route.get("ref") != "syngan://implementation/v0x-program":
        errors.append("OKF manifest: v0.x implementation-program route drift")

    for phrase in (
        "017-F                               COMPLETE",
        "product implementation execution   NOT AUTHORIZED",
        "active implementation packages     0",
    ):
        if phrase not in status:
            errors.append(f"current status: missing {phrase}")

    for error in errors:
        print("ERROR", error)
    print(f"v0.x implementation-program conformance: {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
