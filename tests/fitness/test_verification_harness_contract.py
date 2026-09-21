from __future__ import annotations

import tomllib
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "verification.toml"
PYPROJECT = ROOT / "pyproject.toml"
VERIFY = ROOT / "tools" / "verify.py"


def _load(path: Path) -> dict[str, Any]:
    with path.open("rb") as handle:
        return tomllib.load(handle)


def test_verification_manifest_has_current_lane_state() -> None:
    manifest = _load(MANIFEST)

    assert manifest["lanes"] == {
        "C0": "active",
        "C1": "active",
        "C2": "active",
        "C3": "active",
        "C4": "active",
        "C5": "active",
        "C6": "active",
        "C7": "active",
        "C8": "active",
        "C9": "defined",
    }


def test_phase_014_f_scenario_registry_is_complete() -> None:
    manifest = _load(MANIFEST)
    scenarios = manifest["scenarios"]

    assert set(scenarios) == {f"S{number:02d}" for number in range(1, 15)}


def test_pytest_marker_registry_covers_manifest_markers() -> None:
    manifest = _load(MANIFEST)
    project = _load(PYPROJECT)
    registered = {
        marker.split(":", maxsplit=1)[0]
        for marker in project["tool"]["pytest"]["ini_options"]["markers"]
    }

    assert set(manifest["markers"]).issubset(registered)


def test_portable_profile_excludes_explicit_nonportable_markers() -> None:
    manifest = _load(MANIFEST)
    excluded = set(manifest["profiles"]["portable"]["exclude_markers"])

    assert excluded == {
        "network",
        "external",
        "integration",
        "spark",
        "failure",
        "security",
        "provider",
        "scale",
        "stochastic",
    }


def test_repository_verifier_exposes_current_required_profiles() -> None:
    verifier = VERIFY.read_text(encoding="utf-8")

    for profile in (
        "authority",
        "static",
        "portable",
        "control",
        "data",
        "runtime",
        "execution",
        "evidence",
        "security",
        "platform",
    ):
        assert f'"{profile}"' in verifier

    assert "verify_all() -> None" in verifier
    assert "verify_portable()" in verifier
