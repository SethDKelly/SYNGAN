from __future__ import annotations

import argparse
import json
from pathlib import Path

EXPECTED_LAYERS = [f"QL-{number:02d}" for number in range(1, 11)]
EXPECTED_CAPABILITIES = [f"MVP-C{number:02d}" for number in range(1, 9)]
REQUIRED_CHALLENGES = ["CH-01", "CH-02", "CH-03", "CH-04", "CH-05", "CH-07", "CH-08"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    repo = Path(parser.parse_args().repo).resolve()
    errors: list[str] = []

    profile_path = repo / "docs" / "implementation" / "mvp-qualification-profile.json"
    registry_path = repo / "docs" / "authority" / "stable-reference-registry.json"
    manifest_path = repo / "docs" / "authority" / "okf-projection-manifest.json"
    status_path = repo / "docs" / "authority" / "current-repository-status.md"
    phase_025_path = repo / "docs" / "phases" / "025" / "phase-definition.md"

    for path in (profile_path, registry_path, manifest_path, status_path, phase_025_path):
        if not path.is_file():
            errors.append(f"missing MVP qualification surface: {path.relative_to(repo)}")

    if errors:
        for error in errors:
            print("ERROR", error)
        return 1

    profile = json.loads(profile_path.read_text(encoding="utf-8"))
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    status = status_path.read_text(encoding="utf-8")
    phase_025 = phase_025_path.read_text(encoding="utf-8")

    if profile.get("stable_ref") != "syngan://implementation/mvp-qualification":
        errors.append("profile: stable-ref drift")
    if profile.get("execution_phase") != "025":
        errors.append("profile: qualification must execute in Phase 025")
    if profile.get("candidate_source_phase") != "024":
        errors.append("profile: qualification candidate must come from Phase 024")
    if profile.get("mode") != "independent_non_compensatory_by_blocking_obligation":
        errors.append("profile: qualification mode drift")
    if profile.get("required_mvp_capabilities") != EXPECTED_CAPABILITIES:
        errors.append("profile: MVP-C01..MVP-C08 coverage drift")
    if profile.get("minimum_independence") != "EI1":
        errors.append("profile: EI1 must remain the minimum independence level")
    if profile.get("e5_required_for_bounded_mvp") is not False:
        errors.append("profile: E5 must not become mandatory for the bounded MVP")

    layers = [item.get("id") for item in profile.get("qualification_layers", [])]
    if layers != EXPECTED_LAYERS:
        errors.append("profile: qualification layers must be QL-01..QL-10")

    challenge = profile.get("challenge_policy", {})
    if challenge.get("required_families") != REQUIRED_CHALLENGES:
        errors.append("profile: required challenge-family portfolio drift")
    if challenge.get("conditional_families") != ["CH-06"]:
        errors.append("profile: CH-06 must remain conditional on a legitimate oracle")
    if challenge.get("budgets_frozen_before_holdout") is not True:
        errors.append("profile: challenge budgets must freeze before holdout")
    if challenge.get("thresholds_may_be_set_post_hoc") is not False:
        errors.append("profile: post-hoc thresholds must remain forbidden")
    if challenge.get("failed_generated_cases_preserved") is not True:
        errors.append("profile: failed generated cases must remain evidence")
    if challenge.get("cherry_picked_retries_allowed") is not False:
        errors.append("profile: cherry-picked retries must remain forbidden")
    if challenge.get("aggregate_score_can_override_blocking_failure") is not False:
        errors.append("profile: aggregate score must never override a blocking failure")
    if challenge.get("universal_mutation_percentage_threshold") is not None:
        errors.append("profile: Phase 017-G must not invent a universal mutation threshold")

    candidate = profile.get("candidate_rules", {})
    if candidate.get("evaluator_may_modify_frozen_candidate") is not False:
        errors.append("profile: evaluator must not modify the frozen candidate")
    if candidate.get("product_change_invalidates_candidate") is not True:
        errors.append("profile: product change must invalidate candidate identity")
    if candidate.get("affected_evidence_must_rerun") is not True:
        errors.append("profile: affected evidence must rerun after repair")
    if candidate.get("fresh_h1_for_affected_obligations") is not True:
        errors.append("profile: repaired obligations require fresh H1")
    expected_anchor = [
        "candidate_identity_build_install",
        "repository_verification_baseline",
        "minimal_end_to_end_package_workflow",
    ]
    if candidate.get("anchor_suite_after_any_candidate_change") != expected_anchor:
        errors.append("profile: mandatory post-repair anchor suite drift")

    decision = profile.get("decision_rules", {})
    if decision.get("allowed_outcomes") != [
        "PASS",
        "PASS WITH CARRY-FORWARD",
        "NOT READY TO EXIT",
    ]:
        errors.append("profile: lifecycle decision outcomes drift")
    if decision.get("pass_requires_all_blocking_obligations") is not True:
        errors.append("profile: PASS must require all blocking obligations")
    if decision.get("pass_with_carry_forward_requires_all_blocking_obligations") is not True:
        errors.append("profile: carry-forward pass must still satisfy all blocking obligations")
    if decision.get("carry_forward_only_nonblocking") is not True:
        errors.append("profile: carry-forward must remain non-blocking only")
    if decision.get("blocking_candidate_defect_requires_not_ready") is not True:
        errors.append("profile: blocking candidate defect must require NOT READY")
    if decision.get("evaluator_repair_authorizes_pass") is not False:
        errors.append("profile: evaluator repair must never authorize PASS")

    stable = next(
        (
            item
            for item in registry.get("references", [])
            if item.get("ref") == "syngan://implementation/mvp-qualification"
        ),
        None,
    )
    expected_path = (
        "docs/implementation/"
        "v0x-mvp-completion-testing-qualification-independent-exit.md"
    )
    if not stable or stable.get("status") != "active":
        errors.append("stable reference: missing/inactive MVP qualification authority")
    elif stable.get("path") != expected_path:
        errors.append("stable reference: MVP qualification path drift")

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
                if item.get("id") == "mvp-qualification"
            ),
            None,
        )
    )
    if not route or route.get("ref") != "syngan://implementation/mvp-qualification":
        errors.append("OKF manifest: MVP qualification route drift")

    if "syngan://implementation/mvp-qualification" not in phase_025:
        errors.append("Phase 025: qualification authority is not bound")
    if "evaluation-only" not in phase_025:
        errors.append("Phase 025: evaluation-only boundary missing")

    for phrase in (
        "017-G                               COMPLETE",
        "product implementation execution   NOT AUTHORIZED",
        "active implementation packages     0",
    ):
        if phrase not in status:
            errors.append(f"current status: missing {phrase}")

    for error in errors:
        print("ERROR", error)
    print(f"MVP qualification conformance: {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
