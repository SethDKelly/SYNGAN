from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

EXPECTED = {
    "resolve-context": "A1",
    "resolve-reference": "A1",
    "execute-selected-work": "A2",
    "review-change": "A1",
    "run-verification": "A1",
}
TOP_KEY = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$")
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def _frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing YAML frontmatter")
    try:
        end = next(index for index in range(1, len(lines)) if lines[index].strip() == "---")
    except StopIteration as exc:
        raise ValueError("unterminated YAML frontmatter") from exc
    data: dict[str, str] = {}
    for line in lines[1:end]:
        match = TOP_KEY.match(line)
        if match:
            data[match.group(1)] = match.group(2).strip().strip("\"'")
    return data


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    repo = Path(parser.parse_args().repo).resolve()
    errors: list[str] = []

    budget = json.loads(
        (repo / "docs" / "authority" / "agent-context-budget.json").read_text(encoding="utf-8")
    )
    max_bytes = int(budget["limits"]["skill_each"])
    root = repo / ".agents" / "skills"
    actual = {path.parent.name for path in root.glob("*/SKILL.md")} if root.is_dir() else set()

    if actual != set(EXPECTED):
        errors.append(
            "canonical skill set drift: "
            f"expected {sorted(EXPECTED)}, found {sorted(actual)}"
        )

    for name, action_class in EXPECTED.items():
        path = root / name / "SKILL.md"
        if not path.is_file():
            errors.append(f"missing canonical skill: {path.relative_to(repo)}")
            continue
        text = path.read_text(encoding="utf-8")
        try:
            meta = _frontmatter(text)
        except ValueError as exc:
            errors.append(f"{path.relative_to(repo)}: {exc}")
            continue

        if set(meta) != {"name", "description"}:
            errors.append(
                f"{path.relative_to(repo)}: frontmatter must contain only name and description"
            )
        if meta.get("name") != name or NAME.fullmatch(name) is None:
            errors.append(f"{path.relative_to(repo)}: invalid canonical skill name")
        if not meta.get("description"):
            errors.append(f"{path.relative_to(repo)}: description is required")
        if path.stat().st_size > max_bytes:
            errors.append(
                f"{path.relative_to(repo)}: {path.stat().st_size} exceeds {max_bytes} bytes"
            )
        for token in ("## Boundary", "## Stop conditions", action_class):
            if token not in text:
                errors.append(f"{path.relative_to(repo)}: missing required token {token!r}")

    execute = root / "execute-selected-work" / "SKILL.md"
    if execute.is_file():
        text = execute.read_text(encoding="utf-8")
        for phrase in (
            "Report the next eligible dependency as information only and stop.",
            "Do not choose the next phase/backlog item",
            "If an A3 action becomes necessary, stop for task-specific authorization",
            "If P16-3/P16-4 or another A4 conflict appears",
        ):
            if phrase not in text:
                errors.append(f"execute-selected-work: missing completion/scope guard: {phrase}")

    review = root / "review-change" / "SKILL.md"
    if review.is_file() and "Finding a defect does not authorize repository edits" not in review.read_text(
        encoding="utf-8"
    ):
        errors.append("review-change must preserve review-only non-edit authority")

    for path in root.glob("*/SKILL.md"):
        lower = path.read_text(encoding="utf-8").lower()
        for forbidden in (
            "automatically start the next",
            "autonomously start the next",
            "auto-deploy",
            "bypass branch protection",
        ):
            if forbidden in lower:
                errors.append(f"{path.relative_to(repo)}: forbidden autonomous/privileged wording")

    for error in errors:
        print("ERROR", error)
    print(f"Agent skill validation: {len(errors)} error(s), {len(EXPECTED)} registered skill(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
