from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
POLICY = (
    ROOT
    / "docs"
    / "implementation"
    / "engineering-preflight-dependency-supply-chain-secrets-compatibility-benchmark-versioning.md"
)
PROFILE = ROOT / "docs" / "implementation" / "engineering-preflight-profile.json"
SUPPORT = ROOT / "docs" / "implementation" / "current-support-scope.md"
REGISTRY = ROOT / "docs" / "authority" / "stable-reference-registry.json"
OWNERSHIP = ROOT / "docs" / "authority" / "canonical-knowledge-ownership-map.json"
MANIFEST = ROOT / "docs" / "authority" / "okf-projection-manifest.json"
VERIFY = ROOT / ".github" / "workflows" / "verify.yml"
AGENTIC = ROOT / ".github" / "workflows" / "agentic-conformance.yml"


def test_engineering_preflight_validator_passes_truthful_current_state() -> None:
    subprocess.run(
        [sys.executable, "tools/validate_engineering_preflight.py", "--repo", str(ROOT)],
        cwd=ROOT,
        check=True,
    )


def test_engineering_preflight_seeded_negative_controls_are_rejected() -> None:
    subprocess.run(
        [sys.executable, "tools/test_engineering_preflight_guards.py", "--repo", str(ROOT)],
        cwd=ROOT,
        check=True,
    )


def test_preflight_profile_preserves_nonclaim_and_release_boundaries() -> None:
    profile = json.loads(PROFILE.read_text(encoding="utf-8"))

    assert profile["project"]["version"] == "0.0.0"
    assert profile["project"]["release_state"] == "unreleased-pre-1.0-development"
    assert profile["project"]["verified_python"] == ["3.11"]
    assert profile["project"]["runtime_dependencies_expected"] == []
    assert profile["dependency_rules"]["lock_proves_vulnerability_freedom"] is False
    assert profile["benchmark"]["synthetic_test_fixture_is_real_scale_evidence"] is False
    assert profile["benchmark"]["current_real_scale_evidence"] is False
    assert profile["compatibility"]["enterprise_scale_support"] == "not-qualified"


def test_ci_actions_are_immutably_pinned_and_checkout_credentials_do_not_persist() -> None:
    expected = {
        "actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1",
        "actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97 # v7.0.0",
    }
    verify_text = VERIFY.read_text(encoding="utf-8")
    agentic_text = AGENTIC.read_text(encoding="utf-8")

    for item in expected:
        assert item in verify_text
        assert item in agentic_text
    assert (
        "astral-sh/setup-uv@20cfd1bf945f4377ade1205e4dbc17946fc9a30d # v10.0.1"
        in verify_text
    )
    assert "persist-credentials: false" in verify_text
    assert "persist-credentials: false" in agentic_text


def test_preflight_policy_keeps_deterministic_external_and_human_evidence_separate() -> None:
    text = POLICY.read_text(encoding="utf-8")

    for phrase in (
        "A deterministic repository PASS is necessary evidence for engineering hygiene",
        "lock integrity proves reproducible selection/integrity metadata, not current vulnerability",
        "Python 3.11 is the repository-verified Python line",
        "synthetic test fixture        != real benchmark evidence",
        "EP-R01 distribution license selection",
        "EP-R02 current vulnerability/advisory review",
        "016-I does not:",
    ):
        assert phrase in text


def test_current_support_scope_remains_conservative() -> None:
    text = SUPPORT.read_text(encoding="utf-8")

    for phrase in (
        "production generic-Spark adapter                      NOT CLAIMED",
        "production Databricks adapter                         NOT CLAIMED",
        "enterprise-scale qualification                        NOT CLAIMED",
        "release certification / SLO / SLA                     NOT CLAIMED",
    ):
        assert phrase in text


def test_engineering_preflight_is_current_owner_stable_reference_and_okf_route() -> None:
    ownership = json.loads(OWNERSHIP.read_text(encoding="utf-8"))
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    expected_path = (
        "docs/implementation/"
        "engineering-preflight-dependency-supply-chain-secrets-compatibility-benchmark-versioning.md"
    )

    owner = next(item for item in ownership["owners"] if item["family"] == "engineering_preflight")
    assert owner["path"] == expected_path

    ref = next(
        item
        for item in registry["references"]
        if item["ref"] == "syngan://implementation/engineering-preflight"
    )
    assert ref["status"] == "active"
    assert ref["path"] == expected_path

    group = next(item for item in manifest["groups"] if item["id"] == "implementation")
    route = next(item for item in group["routes"] if item["id"] == "engineering-preflight")
    assert route["ref"] == ref["ref"]
