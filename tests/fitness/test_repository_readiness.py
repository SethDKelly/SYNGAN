from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
READINESS = ROOT / "docs" / "implementation" / "repository-implementation-readiness-residual-risk.md"
SCORECARD = ROOT / "docs" / "implementation" / "repository-readiness-scorecard.json"
REGISTRY = ROOT / "docs" / "authority" / "stable-reference-registry.json"
OWNERSHIP = ROOT / "docs" / "authority" / "canonical-knowledge-ownership-map.json"
MANIFEST = ROOT / "docs" / "authority" / "okf-projection-manifest.json"


def test_repository_readiness_validator_passes_fixed_scorecard() -> None:
    subprocess.run(
        [sys.executable, "tools/validate_repository_readiness.py", "--repo", str(ROOT)],
        cwd=ROOT,
        check=True,
    )


def test_repository_readiness_negative_controls_are_rejected() -> None:
    subprocess.run(
        [sys.executable, "tools/test_repository_readiness_guards.py", "--repo", str(ROOT)],
        cwd=ROOT,
        check=True,
    )


def test_readiness_scorecard_is_fixed_complete_and_non_authorizing() -> None:
    data = json.loads(SCORECARD.read_text(encoding="utf-8"))

    assert data["total_weight"] == 100
    assert data["total_score"] == 100
    assert sum(item["weight"] for item in data["dimensions"]) == 100
    assert sum(item["score"] for item in data["dimensions"]) == 100
    assert data["decision"] == "ready-for-separately-authorized-start-gate"
    assert data["blockers_to_program_entry"] == []
    assert data["phase_016_exit_requires_new_program_authorization"] is True
    assert data["next_program_authorized"] is False


def test_readiness_authority_separates_program_entry_from_release_support_claims() -> None:
    text = READINESS.read_text(encoding="utf-8")

    for phrase in (
        "Phase 016 fixed scorecard                    100 / 100",
        "public release                                 NOT READY / NOT AUTHORIZED",
        "production provider support                    NOT QUALIFIED",
        "enterprise-scale support                       NOT QUALIFIED",
        "None of RR-016-01 through RR-016-06 blocks entry to a new implementation program",
        "new explicitly authorized start gate",
        "any next numbered phase or product program is authorized",
    ):
        assert phrase in text


def test_readiness_is_current_owner_stable_reference_and_okf_route() -> None:
    ownership = json.loads(OWNERSHIP.read_text(encoding="utf-8"))
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    expected = "docs/implementation/repository-implementation-readiness-residual-risk.md"

    owner = next(
        item
        for item in ownership["owners"]
        if item["family"] == "repository_implementation_readiness"
    )
    assert owner["path"] == expected

    ref = next(
        item
        for item in registry["references"]
        if item["ref"] == "syngan://implementation/readiness"
    )
    assert ref["status"] == "active"
    assert ref["path"] == expected

    group = next(item for item in manifest["groups"] if item["id"] == "implementation")
    route = next(item for item in group["routes"] if item["id"] == "repository-readiness")
    assert route["ref"] == ref["ref"]
