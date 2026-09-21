from __future__ import annotations

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / "src" / "syngan"


def test_scaffold_does_not_create_generic_hidden_owner_packages() -> None:
    prohibited = {
        "utils",
        "context",
        "config",
        "manager",
        "registry",
        "metadata",
        "state",
        "result",
        "relationship",
        "data_topology",
        "workflow",
    }
    actual = {path.name for path in PACKAGE.iterdir() if path.is_dir()}

    assert actual.isdisjoint(prohibited)


def test_root_package_does_not_eagerly_import_outer_integrations() -> None:
    root_module = ast.parse((PACKAGE / "__init__.py").read_text(encoding="utf-8"))
    prohibited_imports = {
        "syngan.adapters",
        "syngan.bootstrap",
        "pyspark",
        "torch",
        "transformers",
        "databricks",
        "mlflow",
        "sqlalchemy",
        "opentelemetry",
    }
    violations: list[str] = []

    for node in ast.walk(root_module):
        if isinstance(node, ast.Import):
            imported = [alias.name for alias in node.names]
        elif isinstance(node, ast.ImportFrom) and node.module is not None:
            imported = [node.module]
        else:
            continue

        for name in imported:
            if any(name == candidate or name.startswith(f"{candidate}.") for candidate in prohibited_imports):
                violations.append(name)

    assert violations == []


def test_production_source_never_imports_test_support() -> None:
    violations: list[str] = []

    for source_file in PACKAGE.rglob("*.py"):
        module = ast.parse(source_file.read_text(encoding="utf-8"))
        for node in ast.walk(module):
            if isinstance(node, ast.Import):
                imported = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module is not None:
                imported = [node.module]
            else:
                continue

            if any(name == "tests" or name.startswith("tests.") for name in imported):
                violations.append(str(source_file.relative_to(ROOT)))

    assert violations == []


def test_package_root_and_typing_marker_remain_present() -> None:
    assert (PACKAGE / "__init__.py").is_file()
    assert (PACKAGE / "py.typed").is_file()
