from exercise import hello_world

from test_solution import (
    _DIR,
    assert_hello_world_returns_expected_string,
    assert_main_prints_hello_world,
)

_SCRIPT_NAME = "exercise.py"


class TestExercise:
    def test_hello_world_returns_expected_string(self):
        assert_hello_world_returns_expected_string(hello_world)

    def test_main_prints_hello_world(self):
        assert_main_prints_hello_world(_DIR / _SCRIPT_NAME)
