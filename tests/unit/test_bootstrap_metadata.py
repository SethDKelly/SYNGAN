from __future__ import annotations

import tomllib
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]


def _pyproject() -> dict[str, Any]:
    with (ROOT / "pyproject.toml").open("rb") as handle:
        return tomllib.load(handle)


def test_python_floor_and_build_backend_are_locked() -> None:
    project = _pyproject()

    assert project["project"]["requires-python"] == ">=3.11"
    assert project["build-system"]["build-backend"] == "hatchling.build"
    assert project["tool"]["uv"]["required-version"] == ">=0.12,<0.13"


def test_base_runtime_dependency_closure_is_empty_in_007_b() -> None:
    project = _pyproject()

    assert project["project"]["dependencies"] == []


def test_locked_development_groups_contain_only_authorized_tool_families() -> None:
    project = _pyproject()
    groups = project["dependency-groups"]
    flattened = "\n".join(
        requirement
        for group_name in ("test", "lint", "type", "fitness")
        for requirement in groups[group_name]
    ).lower()

    for required in (
        "pytest",
        "hypothesis",
        "pytest-socket",
        "pytest-cov",
        "ruff",
        "mypy",
        "import-linter",
    ):
        assert required in flattened

    for prohibited in (
        "pyspark",
        "torch",
        "transformers",
        "databricks",
        "mlflow",
        "sqlalchemy",
        "opentelemetry",
    ):
        assert prohibited not in flattened


def test_007_b_does_not_create_production_package_early() -> None:
    assert not (ROOT / "src" / "syngan").exists()
