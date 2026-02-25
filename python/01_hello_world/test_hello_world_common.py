"""Shared test constants and assertions for hello_world topic."""

import subprocess
import sys
from pathlib import Path

_DIR = Path(__file__).resolve().parent
EXPECTED_OUTPUT = "Hello, World!"


def assert_hello_world_returns_expected_string(hello_world_fn):
    assert hello_world_fn() == EXPECTED_OUTPUT


def assert_main_prints_hello_world(script_path: Path):
    result = subprocess.run(
        [sys.executable, script_path],
        capture_output=True,
        text=True,
        cwd=script_path.parent,
    )
    assert result.returncode == 0
    assert result.stdout.strip() == EXPECTED_OUTPUT
