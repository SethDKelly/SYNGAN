from __future__ import annotations

import argparse
import json
import tomllib
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    repo = Path(parser.parse_args().repo).resolve()
    errors: list[str] = []

    profile_path = repo / "docs" / "implementation" / "v0x-mvp-boundary-profile.json"
    registry_path = repo / "docs" / "authority" / "stable-reference-registry.json"
    manifest_path = repo / "docs" / "authority" / "okf-projection-manifest.json"
    status_path = repo / "docs" / "authority" / "current-repository-status.md"
    project_path = repo / "pyproject.toml"

    for path in (profile_path, registry_path, manifest_path, status_path, project_path):
        if not path.is_file():
            errors.append(f"missing v0.x MVP boundary surface: {path.relative_to(repo)}")

    if errors:
        for error in errors:
            print("ERROR", error)
        return 1

    profile = json.loads(profile_path.read_text(encoding="utf-8"))
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    status = status_path.read_text(encoding="utf-8")
    project = tomllib.loads(project_path.read_text(encoding="utf-8"))

    if profile.get("stable_ref") != "syngan://implementation/v0x-mvp-boundary":
        errors.append("profile: stable-ref drift")
    if profile.get("definition") != "qualified_package_capability_not_public_release":
        errors.append("profile: MVP definition drift")

    expected_capabilities = [f"MVP-C{number:02d}" for number in range(1, 9)]
    if profile.get("required_capabilities") != expected_capabilities:
        errors.append("profile: required capabilities must be MVP-C01..MVP-C08")

    baseline = profile.get("baseline_support", {})
    if baseline.get("verified_python") != ["3.11"]:
        errors.append("profile: bounded verified Python baseline must remain 3.11")
    if baseline.get("bounded_spark_capable_path_required") is not True:
        errors.append("profile: bounded Spark-capable path must remain an MVP obligation")
    if baseline.get("production_provider_support_required") is not False:
        errors.append("profile: production provider support must not be an MVP requirement")
    if baseline.get("enterprise_scale_support_required") is not False:
        errors.append("profile: enterprise scale must not be an MVP requirement")

    milestones = [item.get("id") for item in profile.get("capability_milestones", [])]
    if milestones != [f"MVP-M{number}" for number in range(8)]:
        errors.append("profile: capability milestones must be MVP-M0..MVP-M7")

    version = profile.get("version_policy", {})
    if version.get("phase_number_is_package_version") is not False:
        errors.append("profile: phases must not mechanically map to package versions")
    if version.get("placeholder_version") != "0.0.0":
        errors.append("profile: placeholder version must remain 0.0.0")
    if version.get("change_placeholder_during_phase_017") is not False:
        errors.append("profile: Phase 017 must not bump the project version")
    if version.get("non_placeholder_required_by") != "MVP-M6":
        errors.append("profile: candidate freeze must require non-placeholder version")
    if version.get("exact_candidate_version_selected_by_phase") != "024":
        errors.append("profile: Phase 024 must select exact MVP-candidate version")
    if version.get("non_placeholder_version_implies_release_candidate") is not False:
        errors.append("profile: non-placeholder version must not imply release-candidate state")

    if project.get("project", {}).get("version") != "0.0.0":
        errors.append("project: Phase 017 planning must retain version 0.0.0")

    residuals = profile.get("residual_mapping", {})
    for number in range(1, 7):
        key = f"RR-016-{number:02d}"
        entry = residuals.get(key)
        if not entry:
            errors.append(f"profile: missing residual mapping {key}")
        elif entry.get("blocks_package_mvp") is not False:
            errors.append(f"profile: {key} must not become an MVP blocker")

    stable = next(
        (
            item
            for item in registry.get("references", [])
            if item.get("ref") == "syngan://implementation/v0x-mvp-boundary"
        ),
        None,
    )
    expected_path = "docs/implementation/v0x-package-mvp-scope-version-release-boundaries.md"
    if not stable or stable.get("status") != "active":
        errors.append("stable reference: missing/inactive v0.x MVP boundary")
    elif stable.get("path") != expected_path:
        errors.append("stable reference: v0.x MVP boundary path drift")

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
                if item.get("id") == "v0x-mvp-boundary"
            ),
            None,
        )
    )
    if not route or route.get("ref") != "syngan://implementation/v0x-mvp-boundary":
        errors.append("OKF manifest: v0.x MVP boundary route drift")

    for phrase in (
        "017-E                               COMPLETE",
        "017-F                               NEXT ELIGIBLE / NOT AUTHORIZED",
        "product implementation execution   NOT AUTHORIZED",
        "active implementation packages     0",
    ):
        if phrase not in status:
            errors.append(f"current status: missing {phrase}")

    for error in errors:
        print("ERROR", error)
    print(f"v0.x MVP boundary conformance: {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
