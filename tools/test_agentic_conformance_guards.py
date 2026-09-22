from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from collections.abc import Callable
from pathlib import Path


def _run(repo: Path, script: str, *args: str) -> int:
    command = [sys.executable, str(repo / script), *args]
    return subprocess.run(
        command,
        cwd=repo,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    ).returncode


def _mutate(
    repo: Path,
    rel: str,
    transform: Callable[[str], str],
    script: str,
    args: tuple[str, ...],
    label: str,
    errors: list[str],
) -> None:
    path = repo / rel
    original = path.read_text(encoding="utf-8")
    try:
        changed = transform(original)
        if changed == original:
            errors.append(f"{label}: mutation was a no-op")
            return
        path.write_text(changed, encoding="utf-8")
        if _run(repo, script, *args) == 0:
            errors.append(f"{label}: owning validator unexpectedly passed")
        else:
            print("PASS negative control:", label)
    finally:
        path.write_text(original, encoding="utf-8")


def _unauthorized_progression(text: str) -> str:
    return text + "\nnext implementation program  AUTHORIZED / ACTIVE\n"


def _budget_overflow(text: str) -> str:
    data = json.loads(text)
    data["limits"]["agents_md"] = 1
    data["limits"]["cursor_codex_persistent_baseline"] = 1
    data["limits"]["claude_persistent_baseline"] = 1
    return json.dumps(data, indent=2) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    source = Path(parser.parse_args().repo).resolve()
    errors: list[str] = []

    with tempfile.TemporaryDirectory(prefix="syngan-agentic-conformance-") as temp:
        repo = Path(temp) / "repo"
        shutil.copytree(
            source,
            repo,
            ignore=shutil.ignore_patterns(
                ".git",
                ".venv",
                "__pycache__",
                ".pytest_cache",
                ".ruff_cache",
                "dist",
                "coverage.xml",
            ),
            symlinks=True,
        )

        _mutate(
            repo,
            "docs/authority/current-repository-status.md",
            _unauthorized_progression,
            "tools/validate_agent_status.py",
            ("--repo", str(repo)),
            "unauthorized implementation self-progression",
            errors,
        )

        _mutate(
            repo,
            "docs/authority/stable-reference-registry.json",
            lambda text: text.replace(
                '"path": "docs/authority/agent-context-portable-workflows-tool-adapters.md"',
                '"path": "docs/authority/not-a-real-current-owner.md"',
                1,
            ),
            "tools/validate_stable_references.py",
            (),
            "stable-reference target drift",
            errors,
        )

        _mutate(
            repo,
            "knowledge/authority/agent-context-workflows.md",
            lambda text: text.replace(
                (
                    'resource: "../../docs/authority/'
                    'agent-context-portable-workflows-tool-adapters.md"'
                ),
                'resource: "../../docs/index.md"',
                1,
            ),
            "tools/validate_okf_projection.py",
            (),
            "generated OKF stable-reference/resource drift",
            errors,
        )

        _mutate(
            repo,
            "docs/authority/agent-context-budget.json",
            _budget_overflow,
            "tools/measure_agent_context.py",
            (),
            "persistent context-budget overflow",
            errors,
        )

        _mutate(
            repo,
            ".agents/skills/resolve-context/SKILL.md",
            lambda text: text.replace(
                "name: resolve-context\n",
                "name: resolve-context\nmodel: provider-specific-model\n",
                1,
            ),
            "tools/validate_agent_skills.py",
            ("--repo", str(repo)),
            "provider-specific portable-skill metadata",
            errors,
        )

        _mutate(
            repo,
            ".claude/CLAUDE.md",
            lambda text: text.replace("@../AGENTS.md", "@../docs/index.md", 1),
            "tools/validate_agent_adapters.py",
            ("--repo", str(repo)),
            "Claude shared-authority import drift",
            errors,
        )

        _mutate(
            repo,
            "docs/authority/agent-tool-compatibility.json",
            lambda text: text.replace(
                '"runtime_state": "unverified"',
                '"runtime_state": "supported"',
                1,
            ),
            "tools/validate_agent_adapters.py",
            ("--repo", str(repo)),
            "fabricated provider-runtime support",
            errors,
        )

        _mutate(
            repo,
            "docs/implementation/agent-runtime-qualification-profile.json",
            lambda text: text.replace(
                '"runtime_state": "pending_tool_in_loop"',
                '"runtime_state": "qualified"',
                1,
            ),
            "tools/validate_agent_adapters.py",
            ("--repo", str(repo)),
            "fabricated runtime qualification without evidence",
            errors,
        )

        _mutate(
            repo,
            "docs/implementation/evaluation-method-profile.json",
            lambda text: text.replace(
                '"hidden_requirements_allowed": false',
                '"hidden_requirements_allowed": true',
                1,
            ),
            "tools/validate_evaluation_method.py",
            ("--repo", str(repo)),
            "hidden blocking requirements permitted",
            errors,
        )

        _mutate(
            repo,
            "docs/implementation/v0x-mvp-boundary-profile.json",
            lambda text: text.replace(
                '"production_provider_support_required": false',
                '"production_provider_support_required": true',
                1,
            ),
            "tools/validate_v0x_mvp_boundary.py",
            ("--repo", str(repo)),
            "production provider support conflated with package MVP",
            errors,
        )

        _mutate(
            repo,
            "docs/implementation/v0x-program-profile.json",
            lambda text: text.replace(
                '"cross_phase_concurrency": false',
                '"cross_phase_concurrency": true',
                1,
            ),
            "tools/validate_v0x_program.py",
            ("--repo", str(repo)),
            "cross-phase implementation concurrency enabled",
            errors,
        )

        _mutate(
            repo,
            "docs/implementation/mvp-qualification-profile.json",
            lambda text: text.replace(
                '"aggregate_score_can_override_blocking_failure": false',
                '"aggregate_score_can_override_blocking_failure": true',
                1,
            ),
            "tools/validate_mvp_qualification.py",
            ("--repo", str(repo)),
            "aggregate score allowed to compensate for blocking MVP failure",
            errors,
        )

        _mutate(
            repo,
            "docs/implementation/v1-program-profile.json",
            lambda text: text.replace(
                '"phase_025_not_ready_allows_v1_activation": false',
                '"phase_025_not_ready_allows_v1_activation": true',
                1,
            ),
            "tools/validate_v1_program.py",
            ("--repo", str(repo)),
            "v1 allowed to bypass NOT READY MVP qualification",
            errors,
        )

        _mutate(
            repo,
            "AGENTS.md",
            lambda text: (
                text + "\n[Broken agentic route](docs/authority/not-a-real-agentic-owner.md)\n"
            ),
            "tools/validate_agentic_links.py",
            ("--repo", str(repo)),
            "broken current agent-facing link",
            errors,
        )

    for error in errors:
        print("ERROR", error)
    print(f"Agentic conformance negative controls: {len(errors)} error(s), 14 control(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
