from __future__ import annotations

import argparse
import re
from pathlib import Path

P16_ACTIVE = "phase-016-active"
P16_CLOSED = "phase-016-closed"
P17_PLANNING = "phase-017-planning"


def _mode(current: str) -> str:
    if re.search(r"^016-J\s+AUTHORIZED / ACTIVE$", current, re.M):
        return P16_ACTIVE
    if re.search(
        r"^Phase 017\s+AUTHORIZED / ACTIVE — PLANNING ONLY$",
        current,
        re.M,
    ):
        return P17_PLANNING
    if re.search(r"^016-J\s+COMPLETE$", current, re.M):
        return P16_CLOSED
    raise ValueError(
        "current status must declare 016-J active/complete or Phase 017 planning-only active"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    repo = Path(parser.parse_args().repo).resolve()
    errors: list[str] = []

    surfaces = {
        "status": repo / "docs" / "authority" / "current-repository-status.md",
        "phase_016_authority": (
            repo
            / "docs"
            / "authority"
            / "phase-016-documentation-okf-agentic-implementation-readiness-hardening-authority.md"
        ),
        "phase_016_index": repo / "docs" / "phases" / "016" / "index.md",
        "docs_index": repo / "docs" / "index.md",
        "agents": repo / "AGENTS.md",
    }
    phase_017 = repo / "docs" / "phases" / "017" / "index.md"
    if phase_017.is_file():
        surfaces["phase_017_index"] = phase_017

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

    # Phase 016 closure must remain coherent after any later planning phase begins.
    if mode != P16_ACTIVE:
        closure_required = {
            "phase_016_authority": (
                "Phase 016   COMPLETE",
                "016-J       COMPLETE",
                "NEXT PROGRAM  REQUIRES EXPLICIT START GATE / NOT AUTHORIZED",
            ),
            "phase_016_index": (
                "Phase 016   COMPLETE",
                "016-J       COMPLETE",
                "NEXT PROGRAM  REQUIRES EXPLICIT START GATE / NOT AUTHORIZED",
            ),
        }
        for surface, phrases in closure_required.items():
            for phrase in phrases:
                if phrase not in texts[surface]:
                    errors.append(f"{surface}: missing coherent Phase 016 closure: {phrase}")

    if mode == P16_ACTIVE:
        required = {
            "phase_016_authority": ("016-J       AUTHORIZED / ACTIVE",),
            "phase_016_index": ("016-J       AUTHORIZED / ACTIVE",),
            "docs_index": ("016-J                               AUTHORIZED / ACTIVE",),
        }
    elif mode == P16_CLOSED:
        required = {
            "docs_index": (
                "Phase 016                           COMPLETE",
                "product implementation execution   NOT AUTHORIZED",
            ),
            "agents": (
                "Phase 016 pre-implementation hardening is COMPLETE.",
            ),
        }
    else:
        required = {
            "status": (
                "Phase 017                           AUTHORIZED / ACTIVE — PLANNING ONLY",
                "017-A                               COMPLETE",
                "017-B                               NEXT ELIGIBLE / NOT AUTHORIZED",
                "product implementation execution   NOT AUTHORIZED",
                "active implementation packages     0",
            ),
            "phase_017_index": (
                "Phase 017                           AUTHORIZED / ACTIVE — PLANNING ONLY",
                "017-A                               COMPLETE",
                "017-B                               NEXT ELIGIBLE / NOT AUTHORIZED",
                "product implementation execution   NOT AUTHORIZED",
            ),
            "docs_index": (
                "Phase 017                           AUTHORIZED / ACTIVE — PLANNING ONLY",
                "017-A                               COMPLETE",
                "017-B                               NEXT ELIGIBLE / NOT AUTHORIZED",
                "product implementation execution   NOT AUTHORIZED",
            ),
            "agents": (
                "Phase 017 implementation-program planning is AUTHORIZED / ACTIVE — PLANNING ONLY.",
                "Product implementation execution, Phase 018+, product/provider/runtime delivery, "
                "and release remain NOT AUTHORIZED.",
            ),
        }

    for surface, phrases in required.items():
        for phrase in phrases:
            if phrase not in texts.get(surface, ""):
                errors.append(f"{surface}: missing coherent current state: {phrase}")

    for name, text in texts.items():
        if re.search(
            r"(Phase 018|product implementation execution|next implementation program)[^\n]*"
            r"(AUTHORIZED / ACTIVE|IN PROGRESS|STARTED)",
            text,
        ):
            errors.append(
                f"{name}: planning state must not self-authorize implementation execution"
            )
        if re.search(r"Phase 017[^\n]*AUTHORIZED / ACTIVE(?! — PLANNING ONLY)", text):
            errors.append(f"{name}: Phase 017 may be active only with explicit PLANNING ONLY scope")

    for error in errors:
        print("ERROR", error)
    print(f"Agentic status drift validation: {len(errors)} error(s); mode={mode}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
