from __future__ import annotations

import argparse
import json
import os
import shutil
from pathlib import Path
from typing import TypedDict, cast

from stable_refs import StableReferenceError, load_registry, resolve_reference

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "docs" / "authority" / "okf-projection-manifest.json"
GENERATED_ROOT = ROOT / "knowledge"


class Route(TypedDict):
    id: str
    title: str
    description: str
    ref: str


class Group(TypedDict):
    id: str
    title: str
    description: str
    routes: list[Route]


class Manifest(TypedDict):
    schema_version: int
    okf_version: str
    status: str
    producer_profile: str
    authored_root: str
    generated_root: str
    authority: str
    concept_type: str
    groups: list[Group]


def _manifest() -> Manifest:
    data = cast(Manifest, json.loads(MANIFEST_PATH.read_text(encoding="utf-8")))
    if data["schema_version"] != 1:
        raise ValueError("unsupported OKF projection manifest schema")
    if data["okf_version"] != "0.2":
        raise ValueError("projection manifest must target OKF v0.2")
    if data["status"] != "active":
        raise ValueError("projection manifest must be active")
    if data["authored_root"] != "docs/index.md":
        raise ValueError("authored discovery root drifted")
    if data["generated_root"] != "knowledge":
        raise ValueError("generated root drifted")
    if data["authority"] != "DERIVED ROUTING ONLY — NOT SEMANTIC AUTHORITY":
        raise ValueError("projection authority classification drifted")
    if data["concept_type"] != "SYNGAN Knowledge Route":
        raise ValueError("projection concept type drifted")
    return data


def _relative_link(output: str, target: str) -> str:
    start = Path(output).parent.as_posix() or "."
    return os.path.relpath(target, start=start).replace(os.sep, "/")


def _resource_path(reference: str) -> str:
    entry = resolve_reference(reference, load_registry())
    return cast(str, entry["path"])


def _route_frontmatter(
    manifest: Manifest,
    group: Group,
    route: Route,
    output: str,
    resource_path: str,
) -> str:
    tags = ["syngan", group["id"], "generated", "routing"]
    tags_text = ", ".join(json.dumps(tag) for tag in tags)
    return (
        "---\n"
        f"type: {json.dumps(manifest['concept_type'])}\n"
        f"title: {json.dumps(route['title'])}\n"
        f"description: {json.dumps(route['description'])}\n"
        f"syngan_ref: {json.dumps(route['ref'])}\n"
        f"resource: {json.dumps(_relative_link(output, resource_path))}\n"
        f"tags: [{tags_text}]\n"
        'status: "stable"\n'
        'syngan_authority: "projection-only"\n'
        "---\n"
    )


def _render_route(manifest: Manifest, group: Group, route: Route, output: str) -> str:
    resource_path = _resource_path(route["ref"])
    resource = _relative_link(output, resource_path)
    return (
        _route_frontmatter(manifest, group, route, output, resource_path)
        + "\n# Route\n\n"
        + "**GENERATED OKF PROJECTION — DO NOT HAND-EDIT.**\n\n"
        + f"Stable reference: `{route['ref']}`.\n\n"
        + f"Canonical source: [{route['title']}]({resource}).\n\n"
        + "This file is a compatibility route only. It cannot establish or override "
        + "SYNGAN semantic, architecture, implementation, or program authority.\n"
    )


def _root_index(manifest: Manifest) -> str:
    lines = [
        "---",
        'okf_version: "0.2"',
        "---",
        "",
        "# SYNGAN OKF v0.2 Compatibility Projection",
        "",
        "**GENERATED OKF PROJECTION — DO NOT HAND-EDIT.**",
        "",
        "The authored discovery and authority root is [docs/index.md](../docs/index.md).",
        "This bundle exists only for OKF v0.2 compatibility and progressive routing.",
        "Generated content cannot establish or override SYNGAN authority.",
        "",
        "## Routes",
        "",
    ]
    for group in manifest["groups"]:
        lines.append(f"- [{group['title']}]({group['id']}/index.md) - {group['description']}")
    lines.extend(
        [
            "",
            "Producer contract: "
            "[OKF v0.2 Producer Profile]"
            "(../docs/authority/okf-v0.2-producer-profile.md).",
            "",
        ]
    )
    return "\n".join(lines)


def _group_index(group: Group) -> str:
    lines = [
        f"# {group['title']}",
        "",
        "**GENERATED OKF PROJECTION — DO NOT HAND-EDIT.**",
        "",
        group["description"],
        "",
    ]
    for route in group["routes"]:
        lines.append(f"- [{route['title']}]({route['id']}.md) - {route['description']}")
    lines.append("")
    return "\n".join(lines)


def render_all() -> dict[str, str]:
    manifest = _manifest()
    files: dict[str, str] = {"index.md": _root_index(manifest)}
    group_ids: set[str] = set()
    route_refs: set[str] = set()

    for group in manifest["groups"]:
        group_id = group["id"]
        if group_id in group_ids:
            raise ValueError(f"duplicate OKF group id: {group_id}")
        group_ids.add(group_id)
        files[f"{group_id}/index.md"] = _group_index(group)

        route_ids: set[str] = set()
        for route in group["routes"]:
            route_id = route["id"]
            if route_id in route_ids:
                raise ValueError(f"duplicate route id in {group_id}: {route_id}")
            route_ids.add(route_id)
            if route["ref"] in route_refs:
                raise ValueError(f"duplicate OKF stable reference: {route['ref']}")
            route_refs.add(route["ref"])

            resource_path = _resource_path(route["ref"])
            source = ROOT / resource_path
            if not source.exists():
                raise ValueError(
                    f"projection resource does not exist: {route['ref']} -> {resource_path}"
                )
            rel = f"{group_id}/{route_id}.md"
            files[rel] = _render_route(manifest, group, route, f"knowledge/{rel}")

    return files


def check(files: dict[str, str]) -> int:
    errors: list[str] = []
    expected = set(files)
    actual: set[str] = set()
    if GENERATED_ROOT.is_dir():
        actual = {
            path.relative_to(GENERATED_ROOT).as_posix()
            for path in GENERATED_ROOT.rglob("*")
            if path.is_file()
        }

    for rel in sorted(expected - actual):
        errors.append(f"missing generated OKF file: knowledge/{rel}")
    for rel in sorted(actual - expected):
        errors.append(f"unexpected generated OKF file: knowledge/{rel}")
    for rel in sorted(expected & actual):
        if (GENERATED_ROOT / rel).read_text(encoding="utf-8") != files[rel]:
            errors.append(f"generated OKF drift: knowledge/{rel}")

    for error in errors:
        print(f"ERROR {error}")
    print(f"OKF projection generation check: {len(errors)} error(s), {len(files)} tracked file(s)")
    return 1 if errors else 0


def write(files: dict[str, str]) -> int:
    if GENERATED_ROOT.exists():
        shutil.rmtree(GENERATED_ROOT)
    GENERATED_ROOT.mkdir(parents=True)
    for rel, content in files.items():
        path = GENERATED_ROOT / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(f"Generated {len(files)} OKF projection file(s) under knowledge/")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate/check the SYNGAN OKF projection.")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()

    try:
        files = render_all()
    except (OSError, ValueError, json.JSONDecodeError, StableReferenceError) as exc:
        print(f"ERROR {exc}")
        return 1

    return write(files) if args.write else check(files)


if __name__ == "__main__":
    raise SystemExit(main())
