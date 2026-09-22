from __future__ import annotations

import argparse
import re
from pathlib import Path

ACTIVE = "active"
CLOSED = "closed"


def _mode(current: str) -> str:
    if re.search(r"^016-G\s+AUTHORIZED / ACTIVE$", current, re.M):
        return ACTIVE
    if re.search(r"^016-G\s+COMPLETE$", current, re.M):
        return CLOSED
    raise ValueError("current status must declare 016-G AUTHORIZED / ACTIVE or COMPLETE")


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

    if mode == ACTIVE:
        required = {
            "phase_authority": ("016-G       AUTHORIZED / ACTIVE", "016-H..J    NOT AUTHORIZED"),
            "phase_index": ("016-G       AUTHORIZED / ACTIVE", "016-H       NOT AUTHORIZED"),
            "agents": (
                "016-A through 016-F are complete; 016-G is AUTHORIZED / ACTIVE.",
                "016-H and later groups remain NOT AUTHORIZED.",
            ),
        }
        if not re.search(r"^016-H\.\.016-J\s+NOT AUTHORIZED$", texts["status"], re.M):
            errors.append(
                "current status must keep 016-H..016-J NOT AUTHORIZED while 016-G is active"
            )
    else:
        required = {
            "phase_authority": (
                "016-G       COMPLETE",
                "016-H       NEXT ELIGIBLE / NOT AUTHORIZED",
            ),
            "phase_index": ("016-G       COMPLETE", "016-H       NEXT ELIGIBLE / NOT AUTHORIZED"),
            "agents": (
                "016-A through 016-G are complete; 016-H is NEXT ELIGIBLE / NOT AUTHORIZED.",
                "016-I and later groups remain NOT AUTHORIZED.",
            ),
        }
        if not re.search(r"^016-H\s+NEXT ELIGIBLE / NOT AUTHORIZED$", texts["status"], re.M):
            errors.append("current status must make only 016-H next eligible after 016-G closes")
        if not re.search(r"^016-I\.\.016-J\s+NOT AUTHORIZED$", texts["status"], re.M):
            errors.append("current status must keep 016-I..016-J NOT AUTHORIZED after 016-G closes")

    for surface, phrases in required.items():
        for phrase in phrases:
            if phrase not in texts[surface]:
                errors.append(f"{surface}: missing coherent Phase 016 state: {phrase}")

    for name, text in texts.items():
        if re.search(r"016-H[^\n]*(AUTHORIZED / ACTIVE|IN PROGRESS)", text):
            errors.append(f"{name}: 016-H must not be active during 016-G conformance work")
        if re.search(r"016-I[^\n]*(AUTHORIZED / ACTIVE|IN PROGRESS)", text):
            errors.append(f"{name}: 016-I must not be active during 016-G conformance work")

    for error in errors:
        print("ERROR", error)
    print(f"Agentic status drift validation: {len(errors)} error(s); mode={mode}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
