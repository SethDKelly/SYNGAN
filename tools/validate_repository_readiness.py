from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, cast

EXPECTED_WEIGHTS = {
    "design_semantic_completion": 15,
    "architecture_realization_fitness": 12,
    "verification_evidence_discipline": 12,
    "authority_change_control_discipline": 8,
    "documentation_topology_ownership": 10,
    "documentation_concision_indexing": 8,
    "okf_routing_conformance": 7,
    "agentic_development_foundation": 10,
    "implementation_package_traceability": 7,
    "dependency_supply_chain_development_security": 5,
    "compatibility_benchmark_release_preflight": 6,
}
EXPECTED_RESIDUALS = {
    "RR-016-01": ("EP-R01", "unresolved"),
    "RR-016-02": ("EP-R02", "external-evidence-required"),
    "RR-016-03": ("EP-R03", "not-declared"),
    "RR-016-04": ("EP-R04", "not-established"),
    "RR-016-05": ("EP-R05", "not-established"),
    "RR-016-06": ("EP-R06", "not-established"),
}


def _load(path: Path) -> dict[str, Any]:
    return cast(dict[str, Any], json.loads(path.read_text(encoding="utf-8")))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    repo = Path(parser.parse_args().repo).resolve()
    errors: list[str] = []

    scorecard = _load(repo / "docs" / "implementation" / "repository-readiness-scorecard.json")
    preflight = _load(repo / "docs" / "implementation" / "engineering-preflight-profile.json")

    if scorecard.get("total_weight") != 100:
        errors.append("readiness total_weight must remain 100")
    if scorecard.get("total_score") != 100:
        errors.append("readiness total_score must remain 100 for the recorded exit decision")
    if scorecard.get("decision") != "ready-for-separately-authorized-start-gate":
        errors.append("readiness decision must preserve separately authorized start-gate semantics")
    if scorecard.get("phase_016_exit_requires_new_program_authorization") is not True:
        errors.append("Phase 016 exit must require separate next-program authorization")
    if scorecard.get("next_program_authorized") is not False:
        errors.append("readiness evidence must not authorize the next program")
    if scorecard.get("blockers_to_program_entry") != []:
        errors.append("recorded Phase 016 exit currently expects zero implementation-program-entry blockers")

    dims = scorecard.get("dimensions")
    if not isinstance(dims, list):
        errors.append("scorecard dimensions must be a list")
        dims = []
    actual_weights: dict[str, int] = {}
    total_score = 0
    for item in dims:
        if not isinstance(item, dict):
            errors.append("scorecard dimension entries must be objects")
            continue
        ident = item.get("id")
        weight = item.get("weight")
        score = item.get("score")
        if not isinstance(ident, str) or not isinstance(weight, int) or not isinstance(score, int):
            errors.append("scorecard dimension id/weight/score types are invalid")
            continue
        actual_weights[ident] = weight
        if score < 0 or score > weight:
            errors.append(f"{ident}: score must be between 0 and its fixed weight")
        total_score += score

    if actual_weights != EXPECTED_WEIGHTS:
        errors.append("scorecard weights drift from the Phase 016 start-gate model")
    if sum(actual_weights.values()) != 100:
        errors.append("fixed readiness weights no longer sum to 100")
    if total_score != scorecard.get("total_score"):
        errors.append("dimension score sum drifts from total_score")

    preflight_by_id = {
        item["id"]: item
        for item in preflight.get("residuals", [])
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }
    residuals = scorecard.get("residuals")
    if not isinstance(residuals, list):
        errors.append("readiness residual list must be a list")
        residuals = []

    seen: set[str] = set()
    for item in residuals:
        if not isinstance(item, dict):
            errors.append("readiness residual entries must be objects")
            continue
        ident = item.get("id")
        if not isinstance(ident, str):
            errors.append("readiness residual id missing")
            continue
        seen.add(ident)
        expected = EXPECTED_RESIDUALS.get(ident)
        if expected is None:
            errors.append(f"unexpected readiness residual {ident}")
            continue
        source, state = expected
        if item.get("source") != source or item.get("state") != state:
            errors.append(f"{ident}: source/state drifts from 016-I residual evidence")
        source_item = preflight_by_id.get(source)
        if not isinstance(source_item, dict) or source_item.get("state") != state:
            errors.append(f"{ident}: 016-I source residual no longer matches readiness register")
        if item.get("blocks_program_entry") is not False:
            errors.append(f"{ident}: current evidence classifies this as not blocking program entry")
        blocks = item.get("blocks")
        if not isinstance(blocks, list) or not blocks:
            errors.append(f"{ident}: exact blocked claim/action must remain explicit")

    if seen != set(EXPECTED_RESIDUALS):
        errors.append("readiness residual set drifts from the Phase 016 exit register")

    not_scoring = scorecard.get("not_scoring")
    required_non_scoring = {
        "public-release-readiness",
        "provider-certification",
        "enterprise-scale-qualification",
        "deployment-readiness",
        "legal-license-approval",
    }
    if not isinstance(not_scoring, list) or not required_non_scoring.issubset(set(not_scoring)):
        errors.append("scorecard must explicitly exclude downstream release/provider/scale/legal readiness")

    for error in errors:
        print("ERROR", error)
    print(
        "Repository readiness validation: "
        f"{len(errors)} error(s), score={scorecard.get('total_score')}/100, "
        f"residuals={len(residuals)}, program-entry-blockers="
        f"{len(scorecard.get('blockers_to_program_entry', []))}"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
