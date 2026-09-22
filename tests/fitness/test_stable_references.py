from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "docs" / "authority" / "stable-reference-registry.json"
OWNERSHIP = ROOT / "docs" / "authority" / "canonical-knowledge-ownership-map.json"


def _run(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "tools/resolve_knowledge_ref.py", *args],
        cwd=ROOT,
        check=check,
        capture_output=True,
        text=True,
    )


def test_stable_reference_registry_passes_drift_validation() -> None:
    subprocess.run(
        [sys.executable, "tools/validate_stable_references.py"],
        cwd=ROOT,
        check=True,
    )


def test_every_canonical_owner_has_exact_stable_reference() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    ownership = json.loads(OWNERSHIP.read_text(encoding="utf-8"))

    active = [entry for entry in registry["references"] if entry["status"] == "active"]
    by_family = {entry["owner_family"]: entry for entry in active}

    assert set(by_family) == {owner["family"] for owner in ownership["owners"]}
    for owner in ownership["owners"]:
        entry = by_family[owner["family"]]
        assert entry["path"] == owner["path"]


def test_forward_and_reverse_resolution_are_exact() -> None:
    forward = _run("syngan://design/concepts")
    assert forward.stdout.strip() == "docs/concepts/index.md"

    reverse = _run("docs/concepts/index.md", "--from-path")
    assert reverse.stdout.strip() == "syngan://design/concepts"


def test_json_resolution_is_deterministic() -> None:
    first = _run("syngan://implementation/support-scope", "--json").stdout
    second = _run("syngan://implementation/support-scope", "--json").stdout
    assert first == second
    payload = json.loads(first)
    assert payload["path"] == "docs/implementation/current-support-scope.md"
    assert payload["authority_class"] == "current"


def test_unknown_reference_fails_without_search_fallback() -> None:
    result = _run("syngan://design/not-a-real-owner", check=False)
    assert result.returncode == 2
    assert "unknown stable reference" in result.stdout


def test_malformed_reference_fails_without_slug_guessing() -> None:
    result = _run("concepts", check=False)
    assert result.returncode == 2
    assert "malformed stable reference" in result.stdout


def test_unregistered_path_fails_reverse_resolution() -> None:
    result = _run("README.md", "--from-path", check=False)
    assert result.returncode == 2
    assert "no active stable reference" in result.stdout
