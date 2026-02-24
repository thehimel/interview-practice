import subprocess
import sys
from pathlib import Path

from solution import hello_world

_DIR = Path(__file__).resolve().parent
EXPECTED_OUTPUT = "Hello, World!"
_SCRIPT_NAME = "solution.py"


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


class TestSolution:
    def test_hello_world_returns_expected_string(self):
        assert_hello_world_returns_expected_string(hello_world)

    def test_main_prints_hello_world(self):
        assert_main_prints_hello_world(_DIR / _SCRIPT_NAME)
