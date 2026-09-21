from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
IMPLEMENTATION = ROOT / "docs" / "implementation"
CURRENT = IMPLEMENTATION / "phase-015-d-distributed-data-topology-generation-promotion-authority.md"
PHASE = ROOT / "docs" / "phases" / "015" / "index.md"
AGENTS = ROOT / "AGENTS.md"


def test_phase_015_current_authority_is_discoverable() -> None:
    authority_text = CURRENT.read_text(encoding="utf-8")

    assert "status: active-current" in authority_text
    assert "015-A        COMPLETE" in authority_text
    assert "015-B        COMPLETE" in authority_text
    assert "015-C        COMPLETE" in authority_text
    assert "015-D        AUTHORIZED / ACTIVE" in authority_text
    assert "015-E..015-J NOT AUTHORIZED" in authority_text


def test_phase_015_index_exposes_015_d_as_active() -> None:
    phase_text = PHASE.read_text(encoding="utf-8")

    assert "status: active" in phase_text
    assert "015-A" in phase_text and "COMPLETE" in phase_text
    assert "015-B" in phase_text and "COMPLETE" in phase_text
    assert "015-C" in phase_text and "COMPLETE" in phase_text
    assert "015-D" in phase_text and "AUTHORIZED / ACTIVE" in phase_text

    locked_phases = (
        "015-E",
        "015-F",
        "015-G",
        "015-H",
        "015-I",
        "015-J",
    )
    for phase_id in locked_phases:
        assert f"{phase_id}  NOT AUTHORIZED" in phase_text


def test_agent_instructions_preserve_active_015_d_authority_boundary() -> None:
    agent_text = AGENTS.read_text(encoding="utf-8")

    assert "015-A                                 COMPLETE" in agent_text
    assert "015-B                                 COMPLETE" in agent_text
    assert "015-C                                 COMPLETE" in agent_text
    assert "015-D                                 AUTHORIZED / ACTIVE" in agent_text
    assert "015-E..015-J                          NOT AUTHORIZED" in agent_text


def test_015_c_foundation_is_present_without_later_slice_implementation() -> None:
    assert (ROOT / "src" / "syngan" / "foundation" / "identity.py").is_file()
    assert (ROOT / "src" / "syngan" / "foundation" / "representation.py").is_file()
    assert (ROOT / "src" / "syngan" / "ports" / "control_store.py").is_file()
    assert (ROOT / "src" / "syngan" / "adapters" / "sqlite_control_store.py").is_file()
