from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    repo = Path(parser.parse_args().repo).resolve()
    errors: list[str] = []

    profile_path = repo / "docs" / "implementation" / "evaluation-method-profile.json"
    authority_path = (
        repo / "docs" / "implementation" / "success-visibility-holdout-evaluation-anti-gaming.md"
    )
    registry_path = repo / "docs" / "authority" / "stable-reference-registry.json"
    manifest_path = repo / "docs" / "authority" / "okf-projection-manifest.json"
    status_path = repo / "docs" / "authority" / "current-repository-status.md"

    for path in (profile_path, authority_path, registry_path, manifest_path, status_path):
        if not path.is_file():
            errors.append(f"missing evaluation-method surface: {path.relative_to(repo)}")
    if errors:
        for error in errors:
            print("ERROR", error)
        return 1

    profile = json.loads(profile_path.read_text(encoding="utf-8"))
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    status = status_path.read_text(encoding="utf-8")

    if profile.get("stable_ref") != "syngan://implementation/evaluation-method":
        errors.append("profile: stable_ref drift")
    if profile.get("invariant") != "requirements_visible_challenge_realization_holdout":
        errors.append("profile: split-visibility invariant drift")

    visibility = profile.get("visibility_classes", {})
    if visibility.get("V0", {}).get("implementer_visible") is not True:
        errors.append("profile: V0 must remain visible")
    if visibility.get("V0", {}).get("frozen_before_implementation") is not True:
        errors.append("profile: V0 must freeze before implementation")
    if visibility.get("H1", {}).get("implementer_visible_pre_evaluation") is not False:
        errors.append("profile: H1 must remain withheld pre-evaluation")
    if visibility.get("H1", {}).get("generated_or_selected_after_candidate_freeze") is not True:
        errors.append("profile: H1 must follow candidate freeze")
    if visibility.get("H2", {}).get("simulated_secrecy_forbidden") is not True:
        errors.append("profile: pretend secrecy must remain forbidden")

    if profile.get("minimum_agent_assisted_phase_exit_independence") != "EI1":
        errors.append("profile: phase exit requires at least EI1")

    if [x.get("id") for x in profile.get("challenge_families", [])] != [
        f"CH-{n:02d}" for n in range(1, 9)
    ]:
        errors.append("profile: challenge families must be CH-01..CH-08")

    if profile.get("anti_gaming_controls") != [f"AG-{n:02d}" for n in range(1, 13)]:
        errors.append("profile: anti-gaming controls must be AG-01..AG-12")

    rules = profile.get("decision_rules", {})
    if rules.get("hidden_requirements_allowed") is not False:
        errors.append("profile: hidden requirements must be forbidden")
    if rules.get("blocking_obligation_non_compensatory") is not True:
        errors.append("profile: blocking obligations must be non-compensatory")
    if rules.get("aggregate_score_may_override_blocking_failure") is not False:
        errors.append("profile: aggregate score cannot override blocking failure")
    if rules.get("post_hoc_thresholds_allowed") is not False:
        errors.append("profile: post-hoc thresholds must be forbidden")
    if rules.get("evaluator_may_silently_repair_candidate") is not False:
        errors.append("profile: evaluator may not silently repair candidate")
    if rules.get("failed_generated_cases_must_be_retained") is not True:
        errors.append("profile: failed generated cases must be retained")

    contamination = profile.get("contamination", {})
    if contamination.get("exposed_holdout_case_becomes") != "representative_regression_evidence":
        errors.append("profile: exposed holdout must become regression evidence")
    if contamination.get("fresh_holdout_required_after_repair") is not True:
        errors.append("profile: fresh holdout must follow repair")

    stable = next(
        (
            x
            for x in registry.get("references", [])
            if x.get("ref") == "syngan://implementation/evaluation-method"
        ),
        None,
    )
    if not stable or stable.get("status") != "active":
        errors.append("stable reference: missing/ inactive evaluation-method ref")
    elif stable.get("path") != (
        "docs/implementation/success-visibility-holdout-evaluation-anti-gaming.md"
    ):
        errors.append("stable reference: evaluation-method path drift")

    group = next((x for x in manifest.get("groups", []) if x.get("id") == "implementation"), None)
    route = (
        None
        if not group
        else next(
            (
                x
                for x in group.get("routes", [])
                if x.get("id") == "success-visibility-holdout-evaluation"
            ),
            None,
        )
    )
    if not route or route.get("ref") != "syngan://implementation/evaluation-method":
        errors.append("OKF manifest: evaluation-method route drift")

    for phrase in (
        "017-D                               COMPLETE",
        "017-E                               NEXT ELIGIBLE / NOT AUTHORIZED",
        "product implementation execution   NOT AUTHORIZED",
    ):
        if phrase not in status:
            errors.append(f"current status: missing {phrase}")

    for error in errors:
        print("ERROR", error)
    print(f"Evaluation-method conformance: {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
