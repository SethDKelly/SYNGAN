from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from collections.abc import Sequence
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _run(command: Sequence[str]) -> None:
    printable = " ".join(command)
    print(f"+ {printable}", flush=True)
    subprocess.run(command, cwd=ROOT, check=True)


def _tool(name: str) -> str:
    resolved = shutil.which(name)
    if resolved is None:
        raise SystemExit(
            f"Required verification tool '{name}' is not available. "
            "Provision the locked development environment first."
        )
    return resolved


def verify_bootstrap() -> None:
    # This script may be invoked outside the managed uv environment, so retain
    # a runtime floor check even though Ruff's target version is Python 3.11.
    if sys.version_info < (3, 11):  # noqa: UP036
        raise SystemExit("SYNGAN development requires Python >= 3.11")

    required_paths = (
        ROOT / "pyproject.toml",
        ROOT / "uv.lock",
        ROOT / "docs" / "implementation" / "phase-007-implementation-authority-lock.md",
    )
    missing = [str(path.relative_to(ROOT)) for path in required_paths if not path.exists()]
    if missing:
        raise SystemExit(f"Missing required repository bootstrap files: {', '.join(missing)}")

    _run([_tool("uv"), "lock", "--check"])


def verify_lint() -> None:
    _run([_tool("ruff"), "check", "tools", "tests"])


def verify_format() -> None:
    _run([_tool("ruff"), "format", "--check", "tools", "tests"])


def verify_type() -> None:
    _run([sys.executable, "-m", "mypy", "tools", "tests"])


def verify_unit() -> None:
    _run([sys.executable, "-m", "pytest", "tests/unit"])


def verify_fitness() -> None:
    _run([sys.executable, "-m", "pytest", "tests/fitness"])


def verify_coverage() -> None:
    _run(
        [
            sys.executable,
            "-m",
            "pytest",
            "tests/unit",
            "tests/fitness",
            "--cov=tools",
            "--cov-report=term-missing",
            "--cov-report=xml",
        ]
    )


def verify_all() -> None:
    verify_bootstrap()
    verify_lint()
    verify_format()
    verify_type()
    verify_unit()
    verify_fitness()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run repository-owned SYNGAN verification gates.")
    parser.add_argument(
        "profile",
        choices=("bootstrap", "lint", "format", "type", "unit", "fitness", "coverage", "all"),
        nargs="?",
        default="all",
    )
    args = parser.parse_args(argv)

    profiles = {
        "bootstrap": verify_bootstrap,
        "lint": verify_lint,
        "format": verify_format,
        "type": verify_type,
        "unit": verify_unit,
        "fitness": verify_fitness,
        "coverage": verify_coverage,
        "all": verify_all,
    }
    profiles[args.profile]()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
