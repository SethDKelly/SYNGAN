from __future__ import annotations

import argparse
import importlib
import importlib.resources
import shutil
import subprocess
import sys
import tomllib
import zipfile
from collections.abc import Sequence
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERIFICATION_MANIFEST = ROOT / "verification.toml"


def _verification_manifest() -> dict[str, object]:
    with VERIFICATION_MANIFEST.open("rb") as handle:
        return tomllib.load(handle)


def _portable_marker_expression() -> str:
    manifest = _verification_manifest()
    profiles = manifest["profiles"]
    if not isinstance(profiles, dict):
        raise SystemExit("verification.toml profiles must be a table")
    portable = profiles["portable"]
    if not isinstance(portable, dict):
        raise SystemExit("verification.toml profiles.portable must be a table")
    excluded = portable["exclude_markers"]
    if not isinstance(excluded, list) or not all(isinstance(item, str) for item in excluded):
        raise SystemExit("verification.toml portable exclusions must be a list of marker names")
    return " and ".join(f"not {marker}" for marker in excluded)


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
        VERIFICATION_MANIFEST,
        ROOT / "src" / "syngan" / "__init__.py",
        ROOT / "src" / "syngan" / "py.typed",
        ROOT / "docs" / "authority" / "current-repository-status.md",
        ROOT / "docs" / "authority" / "canonical-knowledge-ownership-map.md",
        ROOT / "docs" / "authority" / "okf-v0.2-producer-profile.md",
        ROOT / "docs" / "authority" / "okf-projection-manifest.json",
        ROOT / "docs" / "authority" / "stable-reference-resolution-drift-control.md",
        ROOT / "docs" / "authority" / "stable-reference-registry.json",
        ROOT / "docs" / "authority" / "agent-authority-human-directed-scope-security-trust.md",
        ROOT / "docs" / "authority" / "agent-context-portable-workflows-tool-adapters.md",
        ROOT / "docs" / "authority" / "agent-context-budget.json",
        ROOT / "docs" / "authority" / "agent-tool-compatibility.json",
        ROOT / "docs" / "authority" / "agentic-conformance-policy.md",
        ROOT
        / "docs"
        / "implementation"
        / "implementation-package-traceability-adr-change-control.md",
        ROOT / "docs" / "implementation" / "implementation-package-profile.json",
        ROOT
        / "docs"
        / "implementation"
        / (
            "engineering-preflight-dependency-supply-chain-secrets-"
            "compatibility-benchmark-versioning.md"
        ),
        ROOT / "docs" / "implementation" / "engineering-preflight-profile.json",
        ROOT / "docs" / "implementation" / "packages" / "index.md",
        ROOT / ".agents" / "skills" / "update-traceability" / "SKILL.md",
        ROOT / "tools" / "run_agentic_conformance.py",
        ROOT / "tools" / "scan_repository_secrets.py",
        ROOT / "tools" / "validate_engineering_preflight.py",
        ROOT / ".github" / "workflows" / "agentic-conformance.yml",
        ROOT / ".agents" / "skills" / "resolve-context" / "SKILL.md",
        ROOT / "knowledge" / "index.md",
        ROOT / "docs" / "implementation" / "current-support-scope.md",
        ROOT / "docs" / "phases" / "016" / "index.md",
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


def verify_unit(marker_expression: str | None = None) -> None:
    command = [sys.executable, "-m", "pytest", "tests/unit"]
    if marker_expression is not None:
        command.extend(["-m", marker_expression])
    _run(command)


def verify_architecture() -> None:
    _run([_tool("lint-imports"), "--no-cache"])


def verify_fitness(marker_expression: str | None = None) -> None:
    command = [sys.executable, "-m", "pytest", "tests/fitness"]
    if marker_expression is not None:
        command.extend(["-m", marker_expression])
    _run(command)


def verify_references() -> None:
    _run([sys.executable, "-m", "pytest", "tests/fitness/test_stable_references.py"])


def verify_okf() -> None:
    _run([sys.executable, "-m", "pytest", "tests/fitness/test_okf_projection.py"])


def verify_agentic() -> None:
    _run([sys.executable, "tools/run_agentic_conformance.py"])


def verify_preflight() -> None:
    _run([sys.executable, "-m", "pytest", "tests/fitness/test_engineering_preflight.py"])


def verify_authority() -> None:
    _run(
        [
            sys.executable,
            "-m",
            "pytest",
            "tests/fitness/test_phase_015_authority_boundary.py",
            "tests/fitness/test_documentation_topology.py",
            "tests/fitness/test_documentation_links.py",
            "tests/fitness/test_verification_harness_contract.py",
            "tests/fitness/test_agent_authority_policy.py",
            "tests/fitness/test_agent_context_workflows.py",
            "tests/fitness/test_implementation_package_contract.py",
            "tests/fitness/test_engineering_preflight.py",
            "tests/unit/test_bootstrap_metadata.py",
        ]
    )
    verify_references()
    verify_okf()


def verify_static() -> None:
    verify_bootstrap()
    verify_lint()
    verify_format()
    verify_type()
    verify_architecture()
    verify_authority()


def verify_control() -> None:
    _run(
        [
            sys.executable,
            "-m",
            "pytest",
            "tests/integration/control",
            "-m",
            "integration",
        ]
    )


def verify_data() -> None:
    _run(
        [
            sys.executable,
            "-m",
            "pytest",
            "tests/integration/data",
            "-m",
            "integration",
        ]
    )


def verify_runtime() -> None:
    _run(
        [
            sys.executable,
            "-m",
            "pytest",
            "tests/integration/runtime",
            "-m",
            "integration",
        ]
    )


def verify_execution() -> None:
    _run(
        [
            sys.executable,
            "-m",
            "pytest",
            "tests/integration/execution",
            "-m",
            "integration",
        ]
    )


def verify_evidence() -> None:
    _run(
        [
            sys.executable,
            "-m",
            "pytest",
            "tests/integration/evidence",
            "-m",
            "integration",
        ]
    )


def verify_security() -> None:
    _run(
        [
            sys.executable,
            "-m",
            "pytest",
            "tests/security",
            "-m",
            "security",
        ]
    )


def verify_platform() -> None:
    _run(
        [
            sys.executable,
            "-m",
            "pytest",
            "tests/platform",
            "-m",
            "provider or scale",
        ]
    )


def verify_cross_slice() -> None:
    _run(
        [
            sys.executable,
            "-m",
            "pytest",
            "tests/integration/cross_slice",
            "-m",
            "integration",
        ]
    )


def verify_package() -> None:
    package = importlib.import_module("syngan")
    if package.__name__ != "syngan":
        raise SystemExit("Installed package root did not resolve as 'syngan'")

    package_root = ROOT / "src" / "syngan"
    current_subpackages = sorted(
        path.name
        for path in package_root.iterdir()
        if path.is_dir() and (path / "__init__.py").is_file()
    )
    for package_name in current_subpackages:
        importlib.import_module(f"syngan.{package_name}")

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
            *(f"syngan/{package_name}/__init__.py" for package_name in current_subpackages),
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


def verify_portable() -> None:
    marker_expression = _portable_marker_expression()
    verify_static()
    verify_unit(marker_expression)
    verify_fitness(marker_expression)
    verify_package()


def verify_all() -> None:
    verify_portable()
    verify_control()
    verify_data()
    verify_runtime()
    verify_execution()
    verify_evidence()
    verify_security()
    verify_platform()
    verify_cross_slice()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run repository-owned SYNGAN verification gates.")
    parser.add_argument(
        "profile",
        choices=(
            "bootstrap",
            "authority",
            "okf",
            "references",
            "agentic",
            "preflight",
            "static",
            "portable",
            "control",
            "data",
            "runtime",
            "execution",
            "evidence",
            "security",
            "platform",
            "cross-slice",
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
        "authority": verify_authority,
        "okf": verify_okf,
        "references": verify_references,
        "agentic": verify_agentic,
        "preflight": verify_preflight,
        "static": verify_static,
        "portable": verify_portable,
        "control": verify_control,
        "data": verify_data,
        "runtime": verify_runtime,
        "execution": verify_execution,
        "evidence": verify_evidence,
        "security": verify_security,
        "platform": verify_platform,
        "cross-slice": verify_cross_slice,
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
