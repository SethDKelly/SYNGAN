from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
POLICY = ROOT / "docs" / "authority" / "agentic-conformance-policy.md"
WORKFLOW = ROOT / ".github" / "workflows" / "agentic-conformance.yml"


def test_agentic_positive_conformance_path_passes() -> None:
    subprocess.run(
        [
            sys.executable,
            "tools/run_agentic_conformance.py",
            "--skip-negative-controls",
        ],
        cwd=ROOT,
        check=True,
    )


def test_agentic_seeded_negative_controls_are_rejected() -> None:
    subprocess.run(
        [
            sys.executable,
            "tools/test_agentic_conformance_guards.py",
            "--repo",
            str(ROOT),
        ],
        cwd=ROOT,
        check=True,
    )


def test_agentic_ci_runs_the_canonical_dependency_free_command() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")

    assert "python tools/run_agentic_conformance.py --report agentic-conformance-report.md" in text
    assert "actions/checkout@v7.0.1" in text
    assert "actions/setup-python@v7.0.0" in text
    assert "uv " not in text
    assert "secrets:" not in text


def test_agentic_conformance_policy_preserves_scope_separation() -> None:
    text = POLICY.read_text(encoding="utf-8")

    for phrase in (
        "PASS means only that the checked repository agentic/documentation configuration conforms",
        "PASS does not prove:",
        "provider runtime certification",
        "Agentic conformance never authorizes phase progression.",
        "implementation-package/traceability conformance",
    ):
        assert phrase in text
