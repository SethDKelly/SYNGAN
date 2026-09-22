from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tomllib
from pathlib import Path
from typing import Any, cast

ACTION_RE = re.compile(r"^\s*uses:\s*([^@\s]+)@([0-9a-f]{40})\s*#\s*(v[^\s#]+)\s*$")
ANY_USES_RE = re.compile(r"^\s*uses:\s*([^@\s]+)@([^\s#]+)")
BOUNDED_LOWER = re.compile(r"(?:>=|>)\s*[^,;\s]+")
BOUNDED_UPPER = re.compile(r"<\s*[^,;\s]+")
EXACT_VERSION = re.compile(r"==\s*[^,;\s]+")


def _load_json(path: Path) -> dict[str, Any]:
    return cast(dict[str, Any], json.loads(path.read_text(encoding="utf-8")))


def _load_toml(path: Path) -> dict[str, Any]:
    return tomllib.loads(path.read_text(encoding="utf-8"))


def _requirement_strings(pyproject: dict[str, Any]) -> list[str]:
    requirements: list[str] = []

    build = pyproject.get("build-system", {})
    if isinstance(build, dict):
        values = build.get("requires", [])
        if isinstance(values, list):
            requirements.extend(item for item in values if isinstance(item, str))

    project = pyproject.get("project", {})
    if isinstance(project, dict):
        values = project.get("dependencies", [])
        if isinstance(values, list):
            requirements.extend(item for item in values if isinstance(item, str))
        optional = project.get("optional-dependencies", {})
        if isinstance(optional, dict):
            for group in optional.values():
                if isinstance(group, list):
                    requirements.extend(item for item in group if isinstance(item, str))

    groups = pyproject.get("dependency-groups", {})
    if isinstance(groups, dict):
        for entries in groups.values():
            if not isinstance(entries, list):
                continue
            requirements.extend(item for item in entries if isinstance(item, str))

    return requirements


def _validate_requirement(raw: str, errors: list[str]) -> None:
    lowered = raw.lower()
    if any(marker in lowered for marker in (" @ ", "git+", "http://", "https://", "file:")):
        errors.append(f"direct dependency uses unsupported non-registry source: {raw}")
        return

    if EXACT_VERSION.search(raw):
        return
    if not BOUNDED_LOWER.search(raw) or not BOUNDED_UPPER.search(raw):
        errors.append(f"direct dependency constraint is not lower/upper bounded: {raw}")


def _validate_lock(
    repo: Path,
    profile: dict[str, Any],
    pyproject: dict[str, Any],
    errors: list[str],
) -> int:
    lock = _load_toml(repo / "uv.lock")
    packages = lock.get("package", [])
    if not isinstance(packages, list):
        errors.append("uv.lock package table is missing")
        return 0

    allowed_registry = profile["dependency_rules"]["allowed_registry"]
    hashed_artifacts = 0
    project_name = profile["project"]["name"]

    lock_requires = lock.get("requires-python")
    if lock_requires != pyproject["project"]["requires-python"]:
        errors.append("uv.lock requires-python drifts from pyproject")

    for package in packages:
        if not isinstance(package, dict):
            errors.append("uv.lock contains a non-object package entry")
            continue

        name = package.get("name")
        source = package.get("source")
        if not isinstance(source, dict):
            errors.append(f"uv.lock package {name!r} has no explicit source")
            continue

        if "editable" in source:
            if name != project_name or source.get("editable") != ".":
                errors.append(f"unexpected editable/local dependency source for {name!r}")
            continue

        registry = source.get("registry")
        if registry != allowed_registry:
            errors.append(f"uv.lock package {name!r} uses unsupported registry/source: {source!r}")
            continue

        artifacts: list[dict[str, Any]] = []
        sdist = package.get("sdist")
        if isinstance(sdist, dict):
            artifacts.append(sdist)
        wheels = package.get("wheels", [])
        if isinstance(wheels, list):
            artifacts.extend(item for item in wheels if isinstance(item, dict))

        if not artifacts:
            errors.append(f"uv.lock registry package {name!r} has no integrity-bearing artifacts")
            continue

        for artifact in artifacts:
            digest = artifact.get("hash")
            if not isinstance(digest, str) or not digest.startswith("sha256:"):
                errors.append(f"uv.lock package {name!r} artifact lacks sha256 integrity")
            else:
                hashed_artifacts += 1

    return hashed_artifacts


def _validate_workflows(
    repo: Path,
    profile: dict[str, Any],
    errors: list[str],
) -> int:
    expected = profile["ci_actions"]
    seen: set[str] = set()
    uses_count = 0

    workflows = sorted((repo / ".github" / "workflows").glob("*.yml"))
    workflows.extend(sorted((repo / ".github" / "workflows").glob("*.yaml")))

    for path in workflows:
        text = path.read_text(encoding="utf-8")
        if "permissions:\n  contents: read" not in text:
            errors.append(
                f"{path.relative_to(repo)}: workflow must retain contents: read permissions"
            )
        if "persist-credentials: false" not in text:
            errors.append(f"{path.relative_to(repo)}: checkout credentials must not persist")
        if "${{ secrets." in text:
            errors.append(
                f"{path.relative_to(repo)}: repository verification workflow uses secrets"
            )

        for line in text.splitlines():
            broad = ANY_USES_RE.match(line)
            if broad is None:
                continue
            action, ref = broad.groups()
            if action.startswith("./"):
                continue
            uses_count += 1

            exact = ACTION_RE.match(line)
            if exact is None:
                errors.append(
                    f"{path.relative_to(repo)}: external action must use immutable SHA "
                    "plus release comment: "
                    f"{action}@{ref}"
                )
                continue

            action, sha, release = exact.groups()
            expected_action = expected.get(action)
            if not isinstance(expected_action, dict):
                errors.append(f"{path.relative_to(repo)}: unreviewed external action {action}")
                continue

            if sha != expected_action.get("sha") or release != expected_action.get("release"):
                errors.append(
                    f"{path.relative_to(repo)}: action provenance drift for {action}: "
                    f"{release}@{sha}"
                )
            seen.add(action)

    missing = sorted(set(expected) - seen)
    if missing:
        errors.append(f"reviewed CI actions not observed at exact provenance: {', '.join(missing)}")

    return uses_count


def _validate_project_profile(
    repo: Path,
    profile: dict[str, Any],
    pyproject: dict[str, Any],
    errors: list[str],
) -> None:
    project = pyproject.get("project")
    if not isinstance(project, dict):
        errors.append("pyproject project table missing")
        return

    expected = profile["project"]
    for key in ("name", "version", "requires-python"):
        profile_key = key.replace("-", "_")
        expected_value = expected.get(profile_key)
        if project.get(key) != expected_value:
            errors.append(f"pyproject {key} drifts from engineering preflight profile")

    dependencies = project.get("dependencies", [])
    if dependencies != expected.get("runtime_dependencies_expected"):
        errors.append("runtime project dependency set drifts from engineering preflight profile")

    version = project.get("version")
    release_state = expected.get("release_state")
    if version == "0.0.0" and release_state != "unreleased-pre-1.0-development":
        errors.append("0.0.0 must remain explicitly classified as unreleased development")
    if version != "0.0.0" and release_state == "unreleased-pre-1.0-development":
        errors.append("non-placeholder project version conflicts with unreleased development state")

    python_file = (
        (repo / profile["toolchain"]["python_version_file"]).read_text(encoding="utf-8").strip()
    )
    verified = expected.get("verified_python")
    if not isinstance(verified, list) or python_file not in verified:
        errors.append(".python-version is not represented in verified Python evidence")

    uv = pyproject.get("tool", {}).get("uv", {})
    if (
        not isinstance(uv, dict)
        or uv.get("required-version") != profile["toolchain"]["uv_required"]
    ):
        errors.append("pyproject uv required-version drifts from engineering preflight profile")

    license_declared = "license" in project or "license-files" in project
    residuals = {item["id"]: item for item in profile["residuals"]}
    license_residual = residuals.get("EP-R01", {})
    if license_declared and license_residual.get("state") == "unresolved":
        errors.append("license metadata exists while EP-R01 still says unresolved")
    if not license_declared and license_residual.get("state") != "unresolved":
        errors.append("missing distribution license must remain explicit in EP-R01")


def _validate_support_claims(repo: Path, profile: dict[str, Any], errors: list[str]) -> None:
    text = (repo / "docs" / "implementation" / "current-support-scope.md").read_text(
        encoding="utf-8"
    )

    required_nonclaims = (
        "production generic-Spark adapter                      NOT CLAIMED",
        "production Databricks adapter                         NOT CLAIMED",
        "enterprise-scale qualification                        NOT CLAIMED",
        "release certification / SLO / SLA                     NOT CLAIMED",
    )
    for phrase in required_nonclaims:
        if phrase not in text:
            errors.append(f"current support non-claim missing: {phrase.strip()}")

    benchmark = profile["benchmark"]
    compatibility = profile["compatibility"]
    if benchmark.get("current_real_scale_evidence") is not False:
        errors.append("current real scale evidence must not be fabricated by 016-I")
    if compatibility.get("enterprise_scale_support") != "not-qualified":
        errors.append("enterprise-scale support must remain not-qualified without real evidence")
    if compatibility.get("production_spark_support") != "not-claimed":
        errors.append("production Spark support must remain not-claimed")
    if compatibility.get("production_databricks_support") != "not-claimed":
        errors.append("production Databricks support must remain not-claimed")


def _validate_residuals(profile: dict[str, Any], errors: list[str]) -> int:
    residuals = profile.get("residuals")
    if not isinstance(residuals, list):
        errors.append("engineering preflight residual list missing")
        return 0

    by_id = {
        item.get("id"): item
        for item in residuals
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }
    expected_states = {
        "EP-R01": "unresolved",
        "EP-R02": "external-evidence-required",
        "EP-R03": "not-declared",
        "EP-R04": "not-established",
        "EP-R05": "not-established",
        "EP-R06": "not-established",
    }
    for residual_id, state in expected_states.items():
        item = by_id.get(residual_id)
        if not isinstance(item, dict) or item.get("state") != state:
            errors.append(f"{residual_id} must remain explicit with state {state!r}")

    return sum(
        1 for item in by_id.values() if item.get("consequence") == "release-candidate-blocker"
    )


def _run_secret_scan(repo: Path, errors: list[str]) -> None:
    result = subprocess.run(
        [
            sys.executable,
            str(repo / "tools" / "scan_repository_secrets.py"),
            "--repo",
            str(repo),
        ],
        cwd=repo,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        details = (result.stdout + result.stderr).strip()
        errors.append(f"repository secret scan failed:\n{details}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    repo = Path(parser.parse_args().repo).resolve()

    errors: list[str] = []
    profile_path = repo / "docs" / "implementation" / "engineering-preflight-profile.json"
    profile = _load_json(profile_path)
    authority = repo / str(profile["authority"])
    if not authority.is_file():
        errors.append("engineering preflight canonical authority is missing")

    pyproject = _load_toml(repo / "pyproject.toml")
    _validate_project_profile(repo, profile, pyproject, errors)

    requirements = _requirement_strings(pyproject)
    for requirement in requirements:
        _validate_requirement(requirement, errors)

    hashed_artifacts = _validate_lock(repo, profile, pyproject, errors)
    action_uses = _validate_workflows(repo, profile, errors)
    _validate_support_claims(repo, profile, errors)
    release_blockers = _validate_residuals(profile, errors)
    _run_secret_scan(repo, errors)

    for error in errors:
        print("ERROR", error)
    print(
        "Engineering preflight validation: "
        f"{len(errors)} error(s), {len(requirements)} direct constraint(s), "
        f"{hashed_artifacts} hashed lock artifact(s), {action_uses} external action use(s), "
        f"{release_blockers} declared release-candidate blocker(s)"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
