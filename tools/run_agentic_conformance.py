from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

CHECKS: tuple[tuple[str, tuple[str, ...]], ...] = (
    (
        "program agentic status drift",
        ("tools/validate_agent_status.py", "--repo", "{repo}"),
    ),
    (
        "portable agent skills",
        ("tools/validate_agent_skills.py", "--repo", "{repo}"),
    ),
    (
        "tool adapters and compatibility state",
        ("tools/validate_agent_adapters.py", "--repo", "{repo}"),
    ),
    (
        "agent-facing local links",
        ("tools/validate_agentic_links.py", "--repo", "{repo}"),
    ),
    ("stable references and canonical ownership", ("tools/validate_stable_references.py",)),
    ("deterministic OKF projection drift", ("tools/generate_okf_projection.py", "--check")),
    ("OKF structure and stable-resource binding", ("tools/validate_okf_projection.py",)),
    ("deterministic context budgets", ("tools/measure_agent_context.py",)),
    ("implementation package traceability", ("tools/validate_implementation_packages.py",)),
    ("engineering preflight", ("tools/validate_engineering_preflight.py", "--repo", "{repo}")),
    (
        "success visibility and holdout evaluation methodology",
        ("tools/validate_evaluation_method.py", "--repo", "{repo}"),
    ),
    (
        "v0.x package-MVP scope and release boundary",
        ("tools/validate_v0x_mvp_boundary.py", "--repo", "{repo}"),
    ),
    (
        "v0.x Phase 018-025 implementation program",
        ("tools/validate_v0x_program.py", "--repo", "{repo}"),
    ),
    (
        "v0.x MVP completion qualification",
        ("tools/validate_mvp_qualification.py", "--repo", "{repo}"),
    ),
    (
        "v1 coarse program and rediscovery boundary",
        ("tools/validate_v1_program.py", "--repo", "{repo}"),
    ),
    (
        "Phase 017 exit and Phase 018 handoff",
        ("tools/validate_phase_017_exit.py", "--repo", "{repo}"),
    ),
    (
        "repository readiness scorecard",
        ("tools/validate_repository_readiness.py", "--repo", "{repo}"),
    ),
)


def _run(repo: Path, parts: tuple[str, ...]) -> tuple[int, str]:
    expanded = [part.format(repo=str(repo)) for part in parts]
    command = [sys.executable, str(repo / expanded[0]), *expanded[1:]]
    result = subprocess.run(
        command,
        cwd=repo,
        text=True,
        capture_output=True,
        check=False,
    )
    output = (result.stdout + result.stderr).strip()
    return result.returncode, output


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run deterministic SYNGAN agentic/documentation conformance."
    )
    parser.add_argument("--repo", default=".")
    parser.add_argument("--report")
    parser.add_argument("--skip-negative-controls", action="store_true")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    results: list[tuple[str, int, str]] = []

    for name, parts in CHECKS:
        code, output = _run(repo, parts)
        results.append((name, code, output))
        print("PASS" if code == 0 else "FAIL", name)
        if output:
            print(output)

    if not args.skip_negative_controls:
        name = "repository readiness seeded negative controls"
        code, output = _run(
            repo,
            (
                "tools/test_repository_readiness_guards.py",
                "--repo",
                "{repo}",
            ),
        )
        results.append((name, code, output))
        print("PASS" if code == 0 else "FAIL", name)
        if output:
            print(output)

        name = "engineering preflight seeded negative controls"
        code, output = _run(
            repo,
            (
                "tools/test_engineering_preflight_guards.py",
                "--repo",
                "{repo}",
            ),
        )
        results.append((name, code, output))
        print("PASS" if code == 0 else "FAIL", name)
        if output:
            print(output)

        name = "implementation package seeded negative controls"
        code, output = _run(
            repo,
            (
                "tools/test_implementation_package_guards.py",
                "--repo",
                "{repo}",
            ),
        )
        results.append((name, code, output))
        print("PASS" if code == 0 else "FAIL", name)
        if output:
            print(output)

        name = "cross-cutting seeded negative controls"
        code, output = _run(
            repo,
            (
                "tools/test_agentic_conformance_guards.py",
                "--repo",
                "{repo}",
            ),
        )
        results.append((name, code, output))
        print("PASS" if code == 0 else "FAIL", name)
        if output:
            print(output)

    registry = json.loads(
        (repo / "docs" / "authority" / "stable-reference-registry.json").read_text(encoding="utf-8")
    )
    active_refs = sum(1 for entry in registry["references"] if entry.get("status") == "active")
    knowledge_files = sum(1 for path in (repo / "knowledge").rglob("*") if path.is_file())

    compatibility = json.loads(
        (repo / "docs" / "authority" / "agent-tool-compatibility.json").read_text(encoding="utf-8")
    )

    overall = "PASS" if all(code == 0 for _, code, _ in results) else "FAIL"
    lines = [
        "# SYNGAN Agentic Conformance Report",
        "",
        f"**Repository agentic/documentation conformance:** {overall}",
        "",
        "> This report covers repository agentic/documentation configuration only. "
        "It is not product C0-C9 health, provider-runtime certification, production "
        "readiness, security certification, deployment readiness, or external-system health.",
        "",
        "## Checks",
        "",
        "| Check | Result |",
        "|---|---|",
    ]
    lines.extend(f"| {name} | {'PASS' if code == 0 else 'FAIL'} |" for name, code, _ in results)
    lines.extend(["", "## Tool compatibility state", ""])
    for name, data in compatibility["tools"].items():
        lines.append(
            f"- **{name}:** documented {data.get('documented_state', 'unknown')} / "
            f"runtime {data.get('runtime_state', 'unknown')}"
        )

    lines.extend(
        [
            "",
            "## Deterministic routing state",
            "",
            f"- Active stable references: **{active_refs}**",
            f"- Generated knowledge files: **{knowledge_files}**",
            "",
            "## Scope notes",
            "",
            "- Passing this report never authorizes a next phase, package, backlog item, "
            "or delivery task.",
            "- Provider runtime state remains evidence-controlled and is not inferred "
            "from documentation.",
            "- Negative controls operate only on an isolated temporary copy.",
            "- Phase 017 planning is complete; Phase 018 remains next-eligible/not-authorized and "
            "product/provider/runtime delivery remains unauthorized.",
            "- Engineering-preflight PASS is not release, legal, vulnerability, provider, "
            "or scale approval.",
            "",
        ]
    )

    report = "\n".join(lines)
    if args.report:
        target = Path(args.report)
        if not target.is_absolute():
            target = repo / target
        target.write_text(report, encoding="utf-8")
    print(report)
    return 0 if overall == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
