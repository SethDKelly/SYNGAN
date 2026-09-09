from __future__ import annotations

import argparse
import importlib
import importlib.resources
import shutil
import subprocess
import sys
import zipfile
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
        ROOT / "src" / "syngan" / "__init__.py",
        ROOT / "src" / "syngan" / "py.typed",
        ROOT / "docs" / "implementation" / "phase-007-implementation-authority-lock.md",
        ROOT
        / "docs"
        / "implementation"
        / "phase-007-c-source-package-topology-execution-authority.md",
    )
    missing = [str(path.relative_to(ROOT)) for path in required_paths if not path.exists()]
    if missing:
        raise SystemExit(f"Missing required repository bootstrap files: {', '.join(missing)}")

    _run([_tool("uv"), "lock", "--check"])


def verify_lint() -> None:
    _run([_tool("ruff"), "check", "src", "tools", "tests"])


def verify_format() -> None:
    _run([_tool("ruff"), "format", "--check", "src", "tools", "tests"])


def verify_type() -> None:
    _run([sys.executable, "-m", "mypy", "src", "tools", "tests"])


def verify_unit() -> None:
    _run([sys.executable, "-m", "pytest", "tests/unit"])


def verify_architecture() -> None:
    _run([_tool("lint-imports"), "--no-cache"])


def verify_fitness() -> None:
    _run([sys.executable, "-m", "pytest", "tests/fitness"])


def verify_package() -> None:
    package = importlib.import_module("syngan")
    if package.__name__ != "syngan":
        raise SystemExit("Installed package root did not resolve as 'syngan'")

    for module_name in (
        "syngan.foundation",
        "syngan.domain",
        "syngan.ports",
        "syngan.application",
        "syngan.api",
        "syngan.adapters",
        "syngan.bootstrap",
    ):
        importlib.import_module(module_name)

    marker = importlib.resources.files("syngan").joinpath("py.typed")
    if not marker.is_file():
        raise SystemExit("Installed SYNGAN package is missing its py.typed marker")

    dist = ROOT / "dist"
    shutil.rmtree(dist, ignore_errors=True)
    try:
        _run([_tool("uv"), "build", "--no-build-isolation"])

        wheels = sorted(dist.glob("*.whl"))
        sdists = sorted(dist.glob("*.tar.gz"))
        if len(wheels) != 1 or len(sdists) != 1:
            raise SystemExit(
                "Package verification expected exactly one wheel and one source distribution"
            )

        expected_wheel_paths = {
            "syngan/__init__.py",
            "syngan/py.typed",
            "syngan/foundation/__init__.py",
            "syngan/domain/__init__.py",
            "syngan/ports/__init__.py",
            "syngan/application/__init__.py",
            "syngan/api/__init__.py",
            "syngan/adapters/__init__.py",
            "syngan/bootstrap/__init__.py",
        }
        with zipfile.ZipFile(wheels[0]) as wheel:
            members = set(wheel.namelist())
        missing = sorted(expected_wheel_paths - members)
        if missing:
            raise SystemExit(f"Built wheel is missing expected package paths: {', '.join(missing)}")
    finally:
        shutil.rmtree(dist, ignore_errors=True)


def verify_coverage() -> None:
    _run(
        [
            sys.executable,
            "-m",
            "pytest",
            "tests/unit",
            "tests/fitness",
            "--cov=syngan",
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
    verify_architecture()
    verify_fitness()
    verify_package()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run repository-owned SYNGAN verification gates.")
    parser.add_argument(
        "profile",
        choices=(
            "bootstrap",
            "lint",
            "format",
            "type",
            "unit",
            "architecture",
            "fitness",
            "package",
            "coverage",
            "all",
        ),
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
        "architecture": verify_architecture,
        "fitness": verify_fitness,
        "package": verify_package,
        "coverage": verify_coverage,
        "all": verify_all,
    }
    profiles[args.profile]()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
