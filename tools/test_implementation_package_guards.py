from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from collections.abc import Callable
from pathlib import Path
from typing import Any, cast


def _run(repo: Path) -> int:
    return subprocess.run(
        [sys.executable, str(repo / "tools" / "validate_implementation_packages.py")],
        cwd=repo,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    ).returncode


def _base_package(repo: Path) -> dict[str, Any]:
    fixture = repo / "tests" / "fixtures" / "implementation-package-valid.json"
    data = cast(dict[str, Any], json.loads(fixture.read_text(encoding="utf-8")))
    data["package_id"] = "IPKG-0001"
    data["title"] = "Temporary negative-control package"
    data["authorization_basis"] = "temporary conformance fixture"
    return data


def _mutate(
    repo: Path,
    transform: Callable[[dict[str, Any]], None],
    label: str,
    errors: list[str],
) -> None:
    package = _base_package(repo)
    transform(package)
    path = repo / "docs" / "implementation" / "packages" / "IPKG-0001.json"
    path.write_text(json.dumps(package, indent=2) + "\n", encoding="utf-8")
    try:
        if _run(repo) == 0:
            errors.append(f"{label}: validator unexpectedly passed")
        else:
            print("PASS negative control:", label)
    finally:
        path.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    source = Path(parser.parse_args().repo).resolve()
    errors: list[str] = []

    with tempfile.TemporaryDirectory(prefix="syngan-implementation-package-") as temp:
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
            lambda data: data.update({"authorization_basis": "not authorized"}),
            "complete package without selected authorization basis",
            errors,
        )

        def unknown_ref(data: dict[str, Any]) -> None:
            data["authority_refs"][0] = "syngan://implementation/not-real"
            data["obligations"][0]["authority_ref"] = "syngan://implementation/not-real"

        _mutate(
            repo,
            unknown_ref,
            "unknown current authority reference",
            errors,
        )

        _mutate(
            repo,
            lambda data: data["obligations"][0].update({"evidence_state": "implemented"}),
            "complete package with unverified obligation",
            errors,
        )

        _mutate(
            repo,
            lambda data: data["obligations"][0].update(
                {"verification_paths": ["tests/not-a-real-test.py"]}
            ),
            "verified obligation with missing evidence path",
            errors,
        )

        def class_two_unassessed(data: dict[str, Any]) -> None:
            data["change_class"] = 2
            data["compatibility"]["assessment"] = "not_assessed"

        _mutate(
            repo,
            class_two_unassessed,
            "Class 2 without compatibility assessment",
            errors,
        )

        def class_three_continues(data: dict[str, Any]) -> None:
            data["change_class"] = 3
            data["status"] = "complete"
            data["reopen_ref"] = "syngan://design/architecture"
            data["unresolved"] = ["architecture conflict deliberately left unresolved"]

        _mutate(
            repo,
            class_three_continues,
            "Class 3 conflict continuing as ordinary completed implementation",
            errors,
        )

        _mutate(
            repo,
            lambda data: data.update({"adr_refs": ["ADR-9999"]}),
            "unknown architecture ADR reference",
            errors,
        )

        _mutate(
            repo,
            lambda data: data.update({"unresolved": ["blocking item"]}),
            "complete package retaining unresolved blocking work",
            errors,
        )

        _mutate(
            repo,
            lambda data: data["obligations"][0].update(
                {"implementation_paths": ["docs/history/index.md"]}
            ),
            "history substituted for current implementation evidence",
            errors,
        )

    for error in errors:
        print("ERROR", error)
    print(f"Implementation package negative controls: {len(errors)} error(s), 9 control(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
