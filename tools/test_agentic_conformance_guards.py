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
            "unauthorized Phase 016 self-progression",
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
    print(f"Agentic conformance negative controls: {len(errors)} error(s), 8 control(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
