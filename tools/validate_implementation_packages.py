from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

PACKAGE_ID = re.compile(r"^IPKG-[0-9]{4}$")
OBLIGATION_ID = re.compile(r"^O-[0-9]{3}$")
ADR_ID = re.compile(r"^ADR-[0-9]{4}$")


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _active_refs(repo: Path) -> set[str]:
    registry = _load_json(repo / "docs" / "authority" / "stable-reference-registry.json")
    return {str(item["ref"]) for item in registry["references"] if item.get("status") == "active"}


def _adr_ids(repo: Path, errors: list[str]) -> set[str]:
    root = repo / "docs" / "decisions"
    index = root / "index.md"
    index_text = index.read_text(encoding="utf-8") if index.is_file() else ""
    ids: set[str] = set()

    for path in sorted(root.glob("ADR-*.md")):
        match = re.match(r"^(ADR-[0-9]{4})-", path.name)
        if match is None:
            errors.append(f"invalid ADR filename: {path.relative_to(repo)}")
            continue
        adr_id = match.group(1)
        ids.add(adr_id)
        text = path.read_text(encoding="utf-8")
        if "type: Architecture Decision Record" not in text:
            errors.append(f"{path.relative_to(repo)}: ADR type frontmatter is missing")
        if "## Governing authority" not in text:
            errors.append(f"{path.relative_to(repo)}: governing authority section is missing")
        if "## Supersession" not in text:
            errors.append(f"{path.relative_to(repo)}: supersession section is missing")
        if adr_id not in index_text:
            errors.append(
                f"{path.relative_to(repo)}: ADR is not routed from docs/decisions/index.md"
            )

    return ids


def _path_exists(repo: Path, raw: str) -> bool:
    if not raw or raw.startswith(("/", "~")):
        return False
    path = (repo / raw).resolve()
    try:
        path.relative_to(repo)
    except ValueError:
        return False
    return path.exists()


def _require_list(value: Any) -> list[Any] | None:
    return value if isinstance(value, list) else None


def _validate_manifest(
    repo: Path,
    path: Path,
    data: dict[str, Any],
    profile: dict[str, Any],
    active_refs: set[str],
    adr_ids: set[str],
    fixture: bool,
) -> list[str]:
    errors: list[str] = []
    label = path.relative_to(repo) if path.is_relative_to(repo) else path

    required = set(profile["required_fields"])
    missing = sorted(required - set(data))
    if missing:
        errors.append(f"{label}: missing required fields: {', '.join(missing)}")
        return errors

    if data.get("schema_version") != profile["schema_version"]:
        errors.append(f"{label}: schema_version must equal {profile['schema_version']}")

    package_id = data.get("package_id")
    if not isinstance(package_id, str) or PACKAGE_ID.fullmatch(package_id) is None:
        errors.append(f"{label}: invalid package_id")
    if not fixture and path.name != f"{package_id}.json":
        errors.append(f"{label}: filename must match package_id")

    status = data.get("status")
    if status not in profile["lifecycle"]:
        errors.append(f"{label}: invalid lifecycle status {status!r}")

    change_class = data.get("change_class")
    if change_class not in profile["change_classes"]:
        errors.append(f"{label}: invalid change_class {change_class!r}")

    auth = data.get("authorization_basis")
    if not isinstance(auth, str) or not auth.strip():
        errors.append(f"{label}: authorization_basis must be a non-empty string")
    if status in {"in_progress", "complete"} and isinstance(auth, str):
        if auth.strip().lower() in {"none", "not authorized", "unselected"}:
            errors.append(f"{label}: active/complete package lacks a selected authorization basis")

    authority_refs = _require_list(data.get("authority_refs"))
    if authority_refs is None or not authority_refs:
        errors.append(f"{label}: authority_refs must be a non-empty list")
        authority_refs = []
    else:
        if len(set(authority_refs)) != len(authority_refs):
            errors.append(f"{label}: authority_refs must be unique")
        for ref in authority_refs:
            if not isinstance(ref, str) or not ref.startswith("syngan://"):
                errors.append(f"{label}: invalid current authority reference {ref!r}")
            elif ref not in active_refs:
                errors.append(f"{label}: unknown/non-active current authority reference {ref}")
        for required_ref in (
            "syngan://implementation/governance",
            "syngan://implementation/package-contract",
        ):
            if required_ref not in authority_refs:
                errors.append(f"{label}: package must include {required_ref}")

    scope = data.get("scope")
    if not isinstance(scope, dict):
        errors.append(f"{label}: scope must be an object")
    else:
        included = _require_list(scope.get("included_paths"))
        excluded = _require_list(scope.get("excluded"))
        if included is None:
            errors.append(f"{label}: scope.included_paths must be a list")
            included = []
        if excluded is None:
            errors.append(f"{label}: scope.excluded must be a list")
        if status == "complete":
            for raw in included:
                if not isinstance(raw, str) or not _path_exists(repo, raw):
                    errors.append(f"{label}: completed scope path does not exist: {raw!r}")

    obligations = _require_list(data.get("obligations"))
    if obligations is None or not obligations:
        errors.append(f"{label}: obligations must be a non-empty list")
        obligations = []

    seen_obligations: set[str] = set()
    evidence_states = set(profile["evidence_states"])
    required_obligation = set(profile["obligation_required_fields"])
    for item in obligations:
        if not isinstance(item, dict):
            errors.append(f"{label}: obligation entries must be objects")
            continue
        missing_obligation = sorted(required_obligation - set(item))
        if missing_obligation:
            errors.append(f"{label}: obligation missing fields: {', '.join(missing_obligation)}")
            continue

        obligation_id = item.get("id")
        if not isinstance(obligation_id, str) or OBLIGATION_ID.fullmatch(obligation_id) is None:
            errors.append(f"{label}: invalid obligation id {obligation_id!r}")
        elif obligation_id in seen_obligations:
            errors.append(f"{label}: duplicate obligation id {obligation_id}")
        else:
            seen_obligations.add(obligation_id)

        ref = item.get("authority_ref")
        if ref not in authority_refs:
            errors.append(f"{label}: obligation authority_ref must be declared by package: {ref!r}")
        if ref not in active_refs:
            errors.append(f"{label}: obligation authority_ref is not active: {ref!r}")

        section = item.get("section")
        if not isinstance(section, str) or not section.strip():
            errors.append(f"{label}: obligation section/proposition locator is required")

        state = item.get("evidence_state")
        if state not in evidence_states:
            errors.append(f"{label}: invalid evidence_state {state!r}")

        implementation_paths = _require_list(item.get("implementation_paths"))
        verification_paths = _require_list(item.get("verification_paths"))
        if implementation_paths is None:
            errors.append(f"{label}: implementation_paths must be a list")
            implementation_paths = []
        if verification_paths is None:
            errors.append(f"{label}: verification_paths must be a list")
            verification_paths = []

        if state == "verified":
            if not implementation_paths or not verification_paths:
                errors.append(
                    f"{label}: verified obligation requires implementation and verification paths"
                )
            for raw in [*implementation_paths, *verification_paths]:
                if not isinstance(raw, str) or not _path_exists(repo, raw):
                    errors.append(f"{label}: verified evidence path does not exist: {raw!r}")
                elif raw.startswith("docs/history/"):
                    errors.append(
                        f"{label}: history cannot substitute for current implementation evidence"
                    )

        if state == "not_applicable":
            note = item.get("note")
            if not isinstance(note, str) or not note.strip():
                errors.append(f"{label}: not_applicable obligation requires a justification note")

    verification = data.get("verification")
    if not isinstance(verification, dict):
        errors.append(f"{label}: verification must be an object")
        verification = {}
    commands = _require_list(verification.get("commands"))
    evidence = _require_list(verification.get("ci_evidence"))
    if commands is None:
        errors.append(f"{label}: verification.commands must be a list")
        commands = []
    if evidence is None:
        errors.append(f"{label}: verification.ci_evidence must be a list")
        evidence = []

    compatibility = data.get("compatibility")
    required_compat = set(profile["compatibility_required_fields"])
    if not isinstance(compatibility, dict):
        errors.append(f"{label}: compatibility must be an object")
        compatibility = {}
    missing_compat = sorted(required_compat - set(compatibility))
    if missing_compat:
        errors.append(f"{label}: compatibility missing fields: {', '.join(missing_compat)}")

    if change_class == 2:
        for key in ("assessment", "migration_strategy"):
            value = compatibility.get(key)
            if not isinstance(value, str) or value.strip().lower() in {
                "",
                "unknown",
                "not_assessed",
                "not assessed",
            }:
                errors.append(f"{label}: Class 2 requires explicit compatibility.{key}")

    adr_refs = _require_list(data.get("adr_refs"))
    if adr_refs is None:
        errors.append(f"{label}: adr_refs must be a list")
        adr_refs = []
    for adr in adr_refs:
        if not isinstance(adr, str) or ADR_ID.fullmatch(adr) is None:
            errors.append(f"{label}: invalid ADR reference {adr!r}")
        elif adr not in adr_ids:
            errors.append(f"{label}: unknown ADR reference {adr}")

    unresolved = _require_list(data.get("unresolved"))
    if unresolved is None:
        errors.append(f"{label}: unresolved must be a list")
        unresolved = []

    non_claims = _require_list(data.get("non_claims"))
    if non_claims is None or not non_claims:
        errors.append(f"{label}: non_claims must be a non-empty list")

    if change_class in {3, 4}:
        if status != "blocked":
            errors.append(
                f"{label}: Class 3/4 package must be blocked, not ordinary implementation"
            )
        reopen_ref = data.get("reopen_ref")
        if not isinstance(reopen_ref, str) or reopen_ref not in active_refs:
            errors.append(f"{label}: Class 3/4 package requires an active reopen_ref")
        if not unresolved:
            errors.append(f"{label}: Class 3/4 blocked package must record the unresolved conflict")

    if status == "complete":
        unresolved_states = [
            item.get("evidence_state")
            for item in obligations
            if isinstance(item, dict)
            and item.get("evidence_state") not in {"verified", "not_applicable"}
        ]
        if unresolved_states:
            errors.append(
                f"{label}: complete package contains unresolved obligation evidence states"
            )
        if unresolved:
            errors.append(f"{label}: complete package must not retain unresolved blocking items")
        if not commands or not evidence:
            errors.append(f"{label}: complete package requires verification commands and evidence")

    if status == "superseded":
        successor = data.get("successor_package")
        if not isinstance(successor, str) or PACKAGE_ID.fullmatch(successor) is None:
            errors.append(f"{label}: superseded package requires successor_package")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    parser.add_argument("--fixture")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    errors: list[str] = []

    profile_path = repo / "docs" / "implementation" / "implementation-package-profile.json"
    try:
        profile = _load_json(profile_path)
    except (OSError, json.JSONDecodeError) as exc:
        print("ERROR invalid implementation package profile:", exc)
        return 1

    expected_authority = (
        "docs/implementation/implementation-package-traceability-adr-change-control.md"
    )
    if profile.get("authority") != expected_authority:
        errors.append("implementation-package profile authority path drift")
    if not (repo / expected_authority).is_file():
        errors.append("implementation-package canonical authority is missing")

    active_refs = _active_refs(repo)
    adr_ids = _adr_ids(repo, errors)

    package_root = repo / str(profile["package_root"])
    if not package_root.is_dir():
        errors.append("implementation package root is missing")
        package_files: list[Path] = []
    else:
        package_files = sorted(package_root.glob("IPKG-*.json"))

    for path in package_files:
        try:
            data = _load_json(path)
        except json.JSONDecodeError as exc:
            errors.append(f"{path.relative_to(repo)}: invalid JSON: {exc}")
            continue
        errors.extend(
            _validate_manifest(
                repo,
                path,
                data,
                profile,
                active_refs,
                adr_ids,
                fixture=False,
            )
        )

    if args.fixture:
        fixture = Path(args.fixture)
        if not fixture.is_absolute():
            fixture = repo / fixture
        try:
            data = _load_json(fixture)
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid fixture: {exc}")
        else:
            errors.extend(
                _validate_manifest(
                    repo,
                    fixture,
                    data,
                    profile,
                    active_refs,
                    adr_ids,
                    fixture=True,
                )
            )

    for error in errors:
        print("ERROR", error)
    print(
        "Implementation package validation: "
        f"{len(errors)} error(s), {len(package_files)} active package manifest(s), "
        f"{len(adr_ids)} ADR(s)"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
