from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTRACT = (
    ROOT / "docs" / "implementation" / "implementation-package-traceability-adr-change-control.md"
)
PROFILE = ROOT / "docs" / "implementation" / "implementation-package-profile.json"
PACKAGES = ROOT / "docs" / "implementation" / "packages"
FIXTURE = ROOT / "tests" / "fixtures" / "implementation-package-valid.json"
ADR_INDEX = ROOT / "docs" / "decisions" / "index.md"
SKILL = ROOT / ".agents" / "skills" / "update-traceability" / "SKILL.md"
CLAUDE_COMMAND = ROOT / ".claude" / "commands" / "update-traceability.md"
PR_TEMPLATE = ROOT / ".github" / "pull_request_template.md"
OWNERSHIP = ROOT / "docs" / "authority" / "canonical-knowledge-ownership-map.json"
REGISTRY = ROOT / "docs" / "authority" / "stable-reference-registry.json"
MANIFEST = ROOT / "docs" / "authority" / "okf-projection-manifest.json"


def test_implementation_package_validator_accepts_profile_and_fixture() -> None:
    subprocess.run(
        [
            sys.executable,
            "tools/validate_implementation_packages.py",
            "--fixture",
            str(FIXTURE.relative_to(ROOT)),
        ],
        cwd=ROOT,
        check=True,
    )


def test_implementation_package_seeded_negative_controls_are_rejected() -> None:
    subprocess.run(
        [
            sys.executable,
            "tools/test_implementation_package_guards.py",
            "--repo",
            str(ROOT),
        ],
        cwd=ROOT,
        check=True,
    )


def test_016_h_does_not_create_a_real_implementation_package() -> None:
    manifests = sorted(PACKAGES.glob("IPKG-*.json"))
    assert manifests == []


def test_package_profile_preserves_authority_and_stop_rules() -> None:
    profile = json.loads(PROFILE.read_text(encoding="utf-8"))

    assert profile["package_id_pattern"] == r"^IPKG-[0-9]{4}$"
    assert profile["rules"]["package_is_authorization_source"] is False
    assert profile["rules"]["class_2_requires_compatibility_migration_assessment"] is True
    assert profile["rules"]["class_3_4_may_not_be_in_progress_or_complete"] is True
    assert (
        profile["rules"]["architecture_adrs_are_reference_only_for_implementation_packages"] is True
    )


def test_package_contract_preserves_traceability_and_adr_boundary() -> None:
    text = CONTRACT.read_text(encoding="utf-8")

    for phrase in (
        "An implementation package is a bounded scope/evidence container.",
        "Package creation, a package status change, code existence, a passing test, or an ADR",
        "Class 3 and Class 4 conflicts MUST NOT proceed as ordinary implementation packages.",
        "Stable-reference resolution proves identity/routing only.",
        "Class 0–2 implementation work MUST NOT modify architecture ADR meaning",
        "016-H creates no active package instance.",
        "016-H does not authorize a post-Phase-016 implementation program.",
    ):
        assert phrase in text


def test_current_adr_index_is_reconciled_and_all_adrs_are_routed() -> None:
    text = ADR_INDEX.read_text(encoding="utf-8")
    adr_files = sorted((ROOT / "docs" / "decisions").glob("ADR-*.md"))

    assert len(adr_files) == 10
    assert "Phase 016 pre-implementation hardening  ACTIVE" in text
    assert "016-H package/traceability hardening    AUTHORIZED / ACTIVE" in text
    assert "Implementation remains **NOT READY / NOT STARTED / NOT YET**." not in text
    for path in adr_files:
        assert path.name.split("-", maxsplit=2)[0] == "ADR"
        adr_id = "-".join(path.stem.split("-")[:2])
        assert adr_id in text


def test_traceability_workflow_is_bounded_and_shared() -> None:
    skill = SKILL.read_text(encoding="utf-8")
    bridge = CLAUDE_COMMAND.read_text(encoding="utf-8")

    assert "This is an A2 supporting workflow." in skill
    assert "Resolver success proves routing only, not implementation." in skill
    assert "If a Class 3/4 conflict appears" in skill
    assert "Do not:" in skill
    assert "../../.agents/skills/update-traceability/SKILL.md" in bridge
    assert "adds no permission, scope, semantics, package authorization" in bridge


def test_pr_template_is_current_program_neutral_and_package_aware() -> None:
    text = PR_TEMPLATE.read_text(encoding="utf-8")

    assert "IPKG-####" in text
    assert "Human authorization basis" in text
    assert "Any Class 3/4 conflict was stopped" in text
    assert "ADR addition/material change/supersession" in text
    assert "Phase 007 subgroup" not in text


def test_package_contract_is_canonical_stable_and_okf_routed() -> None:
    ownership = json.loads(OWNERSHIP.read_text(encoding="utf-8"))
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    owner = next(
        item
        for item in ownership["owners"]
        if item["family"] == "implementation_package_traceability_change_control"
    )
    expected = "docs/implementation/implementation-package-traceability-adr-change-control.md"
    assert owner["path"] == expected

    stable = next(
        item
        for item in registry["references"]
        if item["ref"] == "syngan://implementation/package-contract"
    )
    assert stable["status"] == "active"
    assert stable["path"] == expected

    implementation = next(group for group in manifest["groups"] if group["id"] == "implementation")
    route = next(
        item for item in implementation["routes"] if item["id"] == "implementation-package-contract"
    )
    assert route["ref"] == stable["ref"]
