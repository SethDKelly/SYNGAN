from __future__ import annotations

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / "src" / "syngan"
EXPECTED_PACKAGES = {
    "foundation",
    "domain",
    "ports",
    "application",
    "api",
    "adapters",
    "bootstrap",
}


def test_exact_top_level_responsibility_packages_are_present() -> None:
    actual = {
        path.name
        for path in PACKAGE.iterdir()
        if path.is_dir() and (path / "__init__.py").is_file()
    }

    assert actual == EXPECTED_PACKAGES


def test_007_c_does_not_create_generic_god_owner_packages() -> None:
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
    }
    actual = {path.name for path in PACKAGE.iterdir() if path.is_dir()}

    assert actual.isdisjoint(prohibited)


def test_root_package_remains_import_free_during_structural_slice() -> None:
    root_module = ast.parse((PACKAGE / "__init__.py").read_text(encoding="utf-8"))
    import_nodes = [
        node for node in ast.walk(root_module) if isinstance(node, (ast.Import, ast.ImportFrom))
    ]

    assert import_nodes == []


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
