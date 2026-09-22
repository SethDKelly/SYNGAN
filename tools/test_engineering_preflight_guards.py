from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from collections.abc import Callable
from pathlib import Path


def _run(repo: Path) -> int:
    return subprocess.run(
        [
            sys.executable,
            str(repo / "tools" / "validate_engineering_preflight.py"),
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
    rel: str,
    transform: Callable[[str], str],
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
        if _run(repo) == 0:
            errors.append(f"{label}: engineering preflight unexpectedly passed")
        else:
            print("PASS negative control:", label)
    finally:
        path.write_text(original, encoding="utf-8")


def _add_file(
    repo: Path,
    rel: str,
    content: str,
    label: str,
    errors: list[str],
) -> None:
    path = repo / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        errors.append(f"{label}: fixture path unexpectedly exists")
        return
    try:
        path.write_text(content, encoding="utf-8")
        if _run(repo) == 0:
            errors.append(f"{label}: engineering preflight unexpectedly passed")
        else:
            print("PASS negative control:", label)
    finally:
        path.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    source = Path(parser.parse_args().repo).resolve()
    errors: list[str] = []

    with tempfile.TemporaryDirectory(prefix="syngan-engineering-preflight-") as temp:
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
                ".mypy_cache",
                "dist",
                "build",
                "coverage.xml",
            ),
            symlinks=True,
        )

        _mutate(
            repo,
            ".github/workflows/verify.yml",
            lambda text: text.replace(
                "actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1",
                "actions/checkout@v7.0.1",
                1,
            ),
            "floating CI action reference",
            errors,
        )

        _mutate(
            repo,
            ".github/workflows/verify.yml",
            lambda text: text.replace(
                "3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1",
                "0000000000000000000000000000000000000000 # v7.0.1",
                1,
            ),
            "reviewed CI action SHA drift",
            errors,
        )

        _mutate(
            repo,
            "pyproject.toml",
            lambda text: text.replace('"pytest>=8.4,<10"', '"pytest>=8.4"', 1),
            "unbounded direct dependency constraint",
            errors,
        )

        _mutate(
            repo,
            "pyproject.toml",
            lambda text: text.replace(
                '"pytest>=8.4,<10"',
                '"pytest @ https://example.invalid/pytest.whl"',
                1,
            ),
            "arbitrary URL direct dependency",
            errors,
        )

        _mutate(
            repo,
            "uv.lock",
            lambda text: text.replace('hash = "sha256:', 'hash = "missing-sha256:', 1),
            "lock artifact without sha256 integrity",
            errors,
        )

        _mutate(
            repo,
            ".python-version",
            lambda text: "3.12\n",
            "unverified Python line substituted as repository baseline",
            errors,
        )

        _mutate(
            repo,
            "pyproject.toml",
            lambda text: text.replace('version = "0.0.0"', 'version = "1.0.0"', 1),
            "release version changed while release state remains unreleased",
            errors,
        )

        _mutate(
            repo,
            "docs/implementation/current-support-scope.md",
            lambda text: text.replace(
                "enterprise-scale qualification                        NOT CLAIMED",
                "enterprise-scale qualification                        SCALE QUALIFIED",
                1,
            ),
            "enterprise-scale support overclaim",
            errors,
        )

        _mutate(
            repo,
            "pyproject.toml",
            lambda text: text.replace(
                'readme = "README.md"',
                'readme = "README.md"\nlicense = "MIT"',
                1,
            ),
            "license choice added while EP-R01 remains unresolved",
            errors,
        )

        _add_file(
            repo,
            ".env",
            "EXAMPLE_ONLY=not-a-real-secret\n",
            "forbidden checked-in credential filename",
            errors,
        )

        token = "ghp_" + ("A" * 36)
        _add_file(
            repo,
            "secret-probe.txt",
            f"token={token}\n",
            "high-confidence credential pattern",
            errors,
        )

    for error in errors:
        print("ERROR", error)
    print(f"Engineering preflight negative controls: {len(errors)} error(s), 11 control(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
