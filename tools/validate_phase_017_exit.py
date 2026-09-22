from __future__ import annotations

import argparse
import json
from pathlib import Path


EXPECTED_OUTPUTS = [
    "syngan://implementation/phase-lifecycle",
    "syngan://implementation/agent-delivery",
    "syngan://implementation/evaluation-method",
    "syngan://implementation/v0x-mvp-boundary",
    "syngan://implementation/v0x-program",
    "syngan://implementation/mvp-qualification",
    "syngan://implementation/v1-program",
]
EXPECTED_CARRY_FORWARD = [f"P18-CF-{number:02d}" for number in range(1, 6)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    repo = Path(parser.parse_args().repo).resolve()
    errors: list[str] = []

    profile_path = repo / "docs" / "phases" / "017" / "phase-017-exit-profile.json"
    record_path = (
        repo
        / "docs"
        / "phases"
        / "017"
        / "017-I-phase-017-consolidation-documentation-audit-exit-decision-phase-018-handoff.md"
    )
    phase_index_path = repo / "docs" / "phases" / "017" / "index.md"
    status_path = repo / "docs" / "authority" / "current-repository-status.md"
    registry_path = repo / "docs" / "authority" / "stable-reference-registry.json"
    template_path = repo / "docs" / "phases" / "017" / "exit-review-template.md"

    for path in (
        profile_path,
        record_path,
        phase_index_path,
        status_path,
        registry_path,
        template_path,
    ):
        if not path.is_file():
            errors.append(f"missing Phase 017 exit surface: {path.relative_to(repo)}")

    if errors:
        for error in errors:
            print("ERROR", error)
        return 1

    profile = json.loads(profile_path.read_text(encoding="utf-8"))
    phase_index = phase_index_path.read_text(encoding="utf-8")
    status = status_path.read_text(encoding="utf-8")
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    template = template_path.read_text(encoding="utf-8")

    if profile.get("status") != "complete":
        errors.append("profile: Phase 017 exit must remain complete")
    if profile.get("decision") != "PASS WITH CARRY-FORWARD":
        errors.append("profile: Phase 017 exit decision drift")
    if profile.get("durable_outputs") != EXPECTED_OUTPUTS:
        errors.append("profile: durable Phase 017 output mapping drift")

    baseline = profile.get("baseline", {})
    if baseline.get("project_version") != "0.0.0":
        errors.append("profile: Phase 017 must not claim a version bump")
    if baseline.get("active_implementation_packages") != 0:
        errors.append("profile: Phase 017 exit must preserve zero active implementation packages")
    if baseline.get("product_implementation_during_phase_017") is not False:
        errors.append("profile: Phase 017 must not claim product implementation")

    audit = profile.get("documentation_audit", {})
    if audit.get("duplicate_current_owner_conflicts") != 0:
        errors.append("profile: unresolved duplicate current owner conflict")
    if audit.get("semantic_reopens") != 0 or audit.get("architecture_reopens") != 0:
        errors.append("profile: unresolved semantic/architecture reopen at Phase 017 exit")
    if audit.get("stale_progression_surfaces_reconciled") is not True:
        errors.append("profile: stale progression surfaces must be reconciled")
    if audit.get("exit_review_template") != "superseded_by_017_I":
        errors.append("profile: exit template supersession drift")

    carry = profile.get("carry_forward", [])
    if [item.get("id") for item in carry] != EXPECTED_CARRY_FORWARD:
        errors.append("profile: Phase 018 carry-forward register drift")
    if any(item.get("blocking_for_phase_018_pass") is not True for item in carry):
        errors.append("profile: every recorded Phase 018 carry-forward must block Phase 018 PASS")

    phase_018 = profile.get("phase_018", {})
    if phase_018.get("next_eligible_at_exit") is not True:
        errors.append("profile: Phase 018 should be next eligible at Phase 017 exit")
    if phase_018.get("authorized_at_exit") is not False:
        errors.append("profile: Phase 017 exit must not authorize Phase 018")
    if phase_018.get("product_implementation") is not False:
        errors.append("profile: Phase 018 must remain non-product implementation")
    if phase_018.get("may_pass_with_open_carry_forward") is not False:
        errors.append("profile: Phase 018 must not pass with open operational blockers")

    for phrase in (
        "Phase 017                           COMPLETE",
        "017-I                               COMPLETE",
        "product implementation execution   NOT AUTHORIZED",
        "active implementation packages     0",
    ):
        if phrase not in status:
            errors.append(f"current status: missing {phrase}")

    for phrase in (
        "Phase 017                           COMPLETE",
        "017-I                               COMPLETE",
        "PASS WITH CARRY-FORWARD",
    ):
        if phrase not in phase_index:
            errors.append(f"Phase 017 index: missing {phrase}")

    if "status: superseded" not in template:
        errors.append("exit review template must be superseded after 017-I")

    by_ref = {item.get("ref"): item for item in registry.get("references", [])}
    for ref in EXPECTED_OUTPUTS:
        entry = by_ref.get(ref)
        if not entry or entry.get("status") != "active":
            errors.append(f"durable output stable reference missing/inactive: {ref}")

    phase_ref = by_ref.get("syngan://program/phase-017")
    if not phase_ref:
        errors.append("Phase 017 program reference missing")
    elif phase_ref.get("status") == "active":
        if phase_ref.get("path") != "docs/phases/017/index.md":
            errors.append("active Phase 017 program reference path drift")
    elif phase_ref.get("status") == "retired":
        if not phase_ref.get("replacement_ref"):
            errors.append("retired Phase 017 program reference requires replacement_ref")
    else:
        errors.append("Phase 017 program reference has invalid status")

    for error in errors:
        print("ERROR", error)
    print(f"Phase 017 exit conformance: {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
