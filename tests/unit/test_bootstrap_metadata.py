from __future__ import annotations

import tomllib
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]


def _pyproject() -> dict[str, Any]:
    with (ROOT / "pyproject.toml").open("rb") as handle:
        return tomllib.load(handle)


def test_python_floor_build_backend_and_package_selection_are_locked() -> None:
    project = _pyproject()

    assert project["project"]["requires-python"] == ">=3.11"
    assert project["build-system"]["build-backend"] == "hatchling.build"
    assert project["tool"]["uv"]["required-version"] == ">=0.12,<0.13"
    assert project["tool"]["hatch"]["build"]["targets"]["wheel"]["packages"] == [
        "src/syngan"
    ]


def test_base_runtime_dependency_closure_remains_empty_in_007_c() -> None:
    project = _pyproject()

    assert project["project"]["dependencies"] == []


def test_locked_development_groups_contain_only_authorized_tool_families() -> None:
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


def test_import_linter_contracts_cover_required_topology_boundaries() -> None:
    project = _pyproject()
    contracts = {
        contract["id"]: contract for contract in project["tool"]["importlinter"]["contracts"]
    }

    assert set(contracts) == {
        "core-layers",
        "core-no-outer-dependencies",
        "adapters-stay-outside-coordination",
    }
    assert contracts["core-layers"]["type"] == "layers"
    assert contracts["core-no-outer-dependencies"]["type"] == "forbidden"
    assert contracts["adapters-stay-outside-coordination"]["type"] == "forbidden"
