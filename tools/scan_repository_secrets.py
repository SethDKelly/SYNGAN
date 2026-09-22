from __future__ import annotations

import argparse
import fnmatch
import re
from collections.abc import Iterator
from pathlib import Path

TEXT_SUFFIXES = {
    ".json",
    ".lock",
    ".md",
    ".mdc",
    ".py",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}
SKIP_PARTS = {
    ".git",
    ".hypothesis",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "htmlcov",
}
FORBIDDEN_FILE_PATTERNS = (
    ".env",
    ".env.*",
    "*.pem",
    "*.key",
    "*.p12",
    "*.pfx",
    "credentials.json",
    "secrets.json",
    "secrets.yaml",
    "secrets.yml",
    "id_rsa",
    "id_ed25519",
)
ALLOWED_FORBIDDEN_NAME_EXCEPTIONS = {".env.example"}
SECRET_PATTERNS = (
    (
        "private key",
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    ),
    ("AWS access key", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    ("GitHub classic token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b")),
    (
        "GitHub fine-grained token",
        re.compile(r"\bgithub_pat_[A-Za-z0-9_]{40,}\b"),
    ),
    (
        "OpenAI-style secret key",
        re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b"),
    ),
    ("Anthropic secret key", re.compile(r"\bsk-ant-[A-Za-z0-9_-]{20,}\b")),
    ("Slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_-]{30,}\b")),
    (
        "credential-bearing URL",
        re.compile(r"https?://[^\s/:]+:[^\s/@]+@[^\s]+"),
    ),
)


def _iter_files(repo: Path) -> Iterator[Path]:
    for path in sorted(repo.rglob("*")):
        if not path.is_file():
            continue
        try:
            rel = path.relative_to(repo)
        except ValueError:
            continue
        if any(part in SKIP_PARTS for part in rel.parts):
            continue
        yield path


def _forbidden_name(path: Path) -> bool:
    if path.name in ALLOWED_FORBIDDEN_NAME_EXCEPTIONS:
        return False
    return any(fnmatch.fnmatch(path.name, pattern) for pattern in FORBIDDEN_FILE_PATTERNS)


def scan_repository(repo: Path) -> tuple[list[str], int]:
    errors: list[str] = []
    scanned = 0

    for path in _iter_files(repo):
        rel = path.relative_to(repo)
        if _forbidden_name(path):
            errors.append(f"{rel}: forbidden credential/secret-bearing filename")
            continue

        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {
            "AGENTS.md",
            "CLAUDE.md",
        }:
            continue

        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        scanned += 1
        for label, pattern in SECRET_PATTERNS:
            if pattern.search(content):
                errors.append(f"{rel}: high-confidence {label} pattern detected")

    return errors, scanned


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    repo = Path(parser.parse_args().repo).resolve()

    errors, scanned = scan_repository(repo)
    for error in errors:
        print("ERROR", error)
    print(f"Repository secret scan: {len(errors)} error(s), {scanned} text file(s) scanned")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
