from importlib import import_module

from test_hello_world_common import (
    _DIR,
    assert_hello_world_returns_expected_string,
    assert_main_prints_hello_world,
)

solution = import_module("01_hello_world.solution")
hello_world = solution.hello_world

_SCRIPT_NAME = "solution.py"


class TestSolution:
    def test_hello_world_returns_expected_string(self):
        assert_hello_world_returns_expected_string(hello_world)

    def test_main_prints_hello_world(self):
        assert_main_prints_hello_world(_DIR / _SCRIPT_NAME)
