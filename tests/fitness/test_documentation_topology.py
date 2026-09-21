from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
OWNERSHIP_JSON = DOCS / "authority" / "canonical-knowledge-ownership-map.json"


def test_completed_phases_are_separated_from_active_phase_space() -> None:
    for phase in range(1, 16):
        assert (DOCS / "history" / "phases" / f"{phase:03d}").is_dir()
        assert not (DOCS / "phases" / f"{phase:03d}").exists()

    assert (DOCS / "phases" / "016").is_dir()


def test_current_owner_map_resolves_to_existing_current_paths() -> None:
    data = json.loads(OWNERSHIP_JSON.read_text(encoding="utf-8"))

    for owner in data["owners"]:
        path = owner["path"]
        resolved = ROOT / path
        assert resolved.exists(), path
        if owner["family"] != "history":
            assert not path.startswith("docs/history/"), path


def test_history_roots_exist_and_are_not_current_authority() -> None:
    data = json.loads(OWNERSHIP_JSON.read_text(encoding="utf-8"))

    for path in data["history_roots"]:
        assert (ROOT / path).is_dir()

    history_index = (DOCS / "history" / "index.md").read_text(encoding="utf-8")
    assert "History is evidence, not current authority." in history_index


def test_progressive_disclosure_root_routes_to_current_owners_first() -> None:
    docs_index = (DOCS / "index.md").read_text(encoding="utf-8")
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")

    assert "Current Repository Status" in docs_index
    assert "Canonical Knowledge Ownership Map" in docs_index
    assert "Documentation History" in docs_index

    start_section = agents.split("## Start with", maxsplit=1)[1].split(
        "## Durable authority rules", maxsplit=1
    )[0]
    numbered_routes = [
        line for line in start_section.splitlines() if line.lstrip().startswith(("1.", "2.", "3.", "4."))
    ]
    assert len(numbered_routes) == 4


def test_phase_015_current_summary_replaces_completed_slice_authority_as_current_owner() -> None:
    assert (DOCS / "implementation" / "current-support-scope.md").is_file()
    assert (
        DOCS
        / "history"
        / "implementation"
        / "phase-015-j-cross-slice-integration-residual-risk-closure-implementation-consolidation-authority.md"
    ).is_file()
    assert not (
        DOCS
        / "implementation"
        / "phase-015-j-cross-slice-integration-residual-risk-closure-implementation-consolidation-authority.md"
    ).exists()
