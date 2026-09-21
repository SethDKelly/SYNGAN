from __future__ import annotations

import tomllib
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]


def _pyproject() -> dict[str, Any]:
    with (ROOT / "pyproject.toml").open("rb") as handle:
        return tomllib.load(handle)


def test_current_python_floor_build_backend_and_package_selection_are_retained() -> None:
    project = _pyproject()

    assert project["project"]["requires-python"] == ">=3.11"
    assert project["build-system"]["build-backend"] == "hatchling.build"
    assert project["tool"]["uv"]["required-version"] == ">=0.12,<0.13"
    assert project["tool"]["hatch"]["build"]["targets"]["wheel"]["packages"] == ["src/syngan"]


def test_base_runtime_dependency_closure_remains_empty_before_runtime_slices() -> None:
    project = _pyproject()

    assert project["project"]["dependencies"] == []


def test_retained_development_groups_contain_only_authorized_tool_families() -> None:
    project = _pyproject()
    groups = project["dependency-groups"]
    flattened = "\n".join(
        requirement
        for group_name in ("build", "test", "lint", "type", "fitness")
        for requirement in groups[group_name]
    ).lower()

    for required in (
        "hatchling",
        "editables",
        "pytest",
        "hypothesis",
        "pytest-socket",
        "pytest-cov",
        "ruff",
        "mypy",
        "import-linter",
    ):
        assert required in flattened

    for deferred in (
        "pyspark",
        "torch",
        "transformers",
        "databricks",
        "mlflow",
        "sqlalchemy",
        "opentelemetry",
    ):
        assert deferred not in flattened


def test_import_linter_contracts_preserve_current_inner_outer_boundaries() -> None:
    project = _pyproject()
    contracts = {
        contract["id"]: contract for contract in project["tool"]["importlinter"]["contracts"]
    }

    assert set(contracts) == {
        "semantic-core-stays-inward",
        "portable-core-no-outer-integration",
    }
    assert contracts["semantic-core-stays-inward"]["type"] == "forbidden"
    assert contracts["portable-core-no-outer-integration"]["type"] == "forbidden"

    assert set(contracts["semantic-core-stays-inward"]["source_modules"]) == {
        "syngan.foundation",
        "syngan.domain",
    }
    assert {"syngan.adapters", "syngan.bootstrap"}.issubset(
        contracts["portable-core-no-outer-integration"]["forbidden_modules"]
    )
