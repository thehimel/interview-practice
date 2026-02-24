from exercise import main

from test_solution import assert_main_returns_expected


class TestExercise:
    def test_main_returns_expected(self):
        assert_main_returns_expected(main)
