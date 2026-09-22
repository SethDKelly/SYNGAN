from __future__ import annotations

import argparse
import re
from pathlib import Path

ACTIVE = "active"
CLOSED = "closed"


def _mode(current: str) -> str:
    if re.search(r"^016-J\s+AUTHORIZED / ACTIVE$", current, re.M):
        return ACTIVE
    if re.search(r"^016-J\s+COMPLETE$", current, re.M):
        return CLOSED
    raise ValueError("current status must declare 016-J AUTHORIZED / ACTIVE or COMPLETE")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    repo = Path(parser.parse_args().repo).resolve()
    errors: list[str] = []

    surfaces = {
        "status": repo / "docs" / "authority" / "current-repository-status.md",
        "phase_authority": (
            repo
            / "docs"
            / "authority"
            / "phase-016-documentation-okf-agentic-implementation-readiness-hardening-authority.md"
        ),
        "phase_index": repo / "docs" / "phases" / "016" / "index.md",
        "docs_index": repo / "docs" / "index.md",
        "agents": repo / "AGENTS.md",
    }
    texts: dict[str, str] = {}
    for name, path in surfaces.items():
        if not path.is_file():
            errors.append(f"missing required status surface: {path.relative_to(repo)}")
        else:
            texts[name] = path.read_text(encoding="utf-8")

    if errors:
        for error in errors:
            print("ERROR", error)
        return 1

    try:
        mode = _mode(texts["status"])
    except ValueError as exc:
        print("ERROR", exc)
        return 1

    required: dict[str, tuple[str, ...]]
    if mode == ACTIVE:
        required = {
            "phase_authority": ("016-J       AUTHORIZED / ACTIVE",),
            "phase_index": ("016-J       AUTHORIZED / ACTIVE",),
            "docs_index": ("016-J                               AUTHORIZED / ACTIVE",),
            "agents": (
                "016-A through 016-I are complete; 016-J is AUTHORIZED / ACTIVE.",
                "No post-Phase-016 implementation, product/provider/runtime delivery, or release program is authorized.",
            ),
        }
    else:
        required = {
            "phase_authority": (
                "Phase 016   COMPLETE",
                "016-J       COMPLETE",
                "NEXT PROGRAM  REQUIRES EXPLICIT START GATE / NOT AUTHORIZED",
            ),
            "phase_index": (
                "Phase 016   COMPLETE",
                "016-J       COMPLETE",
                "NEXT PROGRAM  REQUIRES EXPLICIT START GATE / NOT AUTHORIZED",
            ),
            "docs_index": (
                "Phase 016                           COMPLETE",
                "016-J                               COMPLETE",
                "next implementation program         REQUIRES EXPLICIT START GATE / NOT AUTHORIZED",
            ),
            "agents": (
                "Phase 016 pre-implementation hardening is COMPLETE.",
                "No next implementation, product/provider/runtime delivery, or release program is authorized.",
            ),
        }

    for surface, phrases in required.items():
        for phrase in phrases:
            if phrase not in texts[surface]:
                errors.append(f"{surface}: missing coherent Phase 016 exit state: {phrase}")

    for name, text in texts.items():
        if re.search(r"(Phase 017|next implementation program)[^\n]*(AUTHORIZED / ACTIVE|IN PROGRESS)", text):
            errors.append(f"{name}: Phase 016 exit must not self-authorize a next program")

    for error in errors:
        print("ERROR", error)
    print(f"Agentic status drift validation: {len(errors)} error(s); mode={mode}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
