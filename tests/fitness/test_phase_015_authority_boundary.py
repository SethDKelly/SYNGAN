from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
IMPLEMENTATION = ROOT / "docs" / "implementation"
CURRENT = IMPLEMENTATION / (
    "phase-015-i-platform-capability-portability-observability-scale-performance-"
    "support-qualification-authority.md"
)
PHASE = ROOT / "docs" / "phases" / "015" / "index.md"
AGENTS = ROOT / "AGENTS.md"


def test_phase_015_current_authority_is_discoverable() -> None:
    authority_text = CURRENT.read_text(encoding="utf-8")

    assert "status: active-current" in authority_text
    assert "015-A..015-H  COMPLETE" in authority_text
    assert "015-I         AUTHORIZED / ACTIVE" in authority_text
    assert "015-J         NOT AUTHORIZED" in authority_text


def test_phase_015_index_exposes_015_i_as_active() -> None:
    phase_text = PHASE.read_text(encoding="utf-8")

    assert "status: active" in phase_text
    for phase_id in (
        "015-A",
        "015-B",
        "015-C",
        "015-D",
        "015-E",
        "015-F",
        "015-G",
        "015-H",
    ):
        assert phase_id in phase_text and "COMPLETE" in phase_text

    assert "015-I" in phase_text and "AUTHORIZED / ACTIVE" in phase_text
    assert "015-J  NOT AUTHORIZED" in phase_text


def test_agent_instructions_preserve_active_015_i_authority_boundary() -> None:
    agent_text = AGENTS.read_text(encoding="utf-8")

    assert "015-A                                 COMPLETE" in agent_text
    assert "015-B                                 COMPLETE" in agent_text
    assert "015-C                                 COMPLETE" in agent_text
    assert "015-D                                 COMPLETE" in agent_text
    assert "015-E                                 COMPLETE" in agent_text
    assert "015-F                                 COMPLETE" in agent_text
    assert "015-G                                 COMPLETE" in agent_text
    assert "015-H                                 COMPLETE" in agent_text
    assert "015-I                                 AUTHORIZED / ACTIVE" in agent_text
    assert "015-J                                 NOT AUTHORIZED" in agent_text


def test_015_i_platform_qualification_foundation_is_present_without_provider_claims() -> None:
    assert (ROOT / "src" / "syngan" / "foundation" / "platform.py").is_file()
    assert (ROOT / "src" / "syngan" / "foundation" / "observability.py").is_file()
    assert (ROOT / "src" / "syngan" / "ports" / "platform.py").is_file()
    assert (ROOT / "src" / "syngan" / "ports" / "observability.py").is_file()
    assert (ROOT / "src" / "syngan" / "application" / "platform_qualification.py").is_file()
    assert (ROOT / "src" / "syngan" / "application" / "observability.py").is_file()
    assert (ROOT / "src" / "syngan" / "adapters" / "reference_platform.py").is_file()
    assert (ROOT / "tests" / "platform" / "test_platform_qualification.py").is_file()
