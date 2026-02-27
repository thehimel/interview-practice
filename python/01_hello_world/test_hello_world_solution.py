"""Test logic for hello_world topic."""

import subprocess
import sys
from importlib import import_module
from pathlib import Path

_DIR = Path(__file__).resolve().parent
EXPECTED_OUTPUT = "Hello, World!"


def create_hello_world_test_class(hello_world_fn, script_path: Path):
    """Create a test class that runs hello_world assertions against the given function and script."""

    class TestHelloWorld:
        def test_hello_world_returns_expected_string(self):
            assert hello_world_fn() == EXPECTED_OUTPUT

        def test_main_prints_hello_world(self):
            result = subprocess.run(
                [sys.executable, script_path],
                capture_output=True,
                text=True,
                cwd=script_path.parent,
            )
            assert result.returncode == 0
            assert result.stdout.strip() == EXPECTED_OUTPUT

    return TestHelloWorld


solution = import_module("01_hello_world.solution")
TestHelloWorldSolution = create_hello_world_test_class(
    solution.hello_world,
    _DIR / "solution.py",
)
