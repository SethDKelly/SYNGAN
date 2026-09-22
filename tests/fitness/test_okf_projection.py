from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _run(script: str, *args: str) -> None:
    subprocess.run([sys.executable, script, *args], cwd=ROOT, check=True)


def test_committed_okf_projection_matches_deterministic_generator() -> None:
    _run("tools/generate_okf_projection.py", "--check")


def test_generated_okf_projection_conforms_to_external_and_syngan_profile() -> None:
    _run("tools/validate_okf_projection.py")
