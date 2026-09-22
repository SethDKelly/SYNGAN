from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from collections.abc import Callable
from pathlib import Path
from typing import Any


def _run(repo: Path) -> int:
    return subprocess.run(
        [
            sys.executable,
            str(repo / "tools" / "validate_repository_readiness.py"),
            "--repo",
            str(repo),
        ],
        cwd=repo,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    ).returncode


def _mutate(
    repo: Path,
    transform: Callable[[dict[str, Any]], None],
    label: str,
    errors: list[str],
) -> None:
    path = repo / "docs" / "implementation" / "repository-readiness-scorecard.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    transform(data)
    original = path.read_text(encoding="utf-8")
    try:
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        if _run(repo) == 0:
            errors.append(f"{label}: readiness validator unexpectedly passed")
        else:
            print("PASS negative control:", label)
    finally:
        path.write_text(original, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    source = Path(parser.parse_args().repo).resolve()
    errors: list[str] = []

    with tempfile.TemporaryDirectory(prefix="syngan-readiness-exit-") as temp:
        repo = Path(temp) / "repo"
        shutil.copytree(
            source,
            repo,
            ignore=shutil.ignore_patterns(
                ".git", ".venv", "__pycache__", ".pytest_cache", ".ruff_cache"
            ),
            symlinks=True,
        )

        _mutate(
            repo,
            lambda data: data["dimensions"][0].update({"weight": 14}),
            "post-hoc scorecard weight change",
            errors,
        )
        _mutate(
            repo,
            lambda data: data.update({"next_program_authorized": True}),
            "readiness evidence self-authorizes next program",
            errors,
        )
        _mutate(
            repo,
            lambda data: data["residuals"][0].update({"state": "resolved"}),
            "unresolved release residual silently closed",
            errors,
        )
        _mutate(
            repo,
            lambda data: data["residuals"][4].update({"blocks": []}),
            "residual loses exact blocked claim",
            errors,
        )
        _mutate(
            repo,
            lambda data: data["dimensions"][-1].update({"score": 7}),
            "dimension score exceeds fixed weight",
            errors,
        )

    for error in errors:
        print("ERROR", error)
    print(f"Repository readiness negative controls: {len(errors)} error(s), 5 control(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
