from importlib import import_module

from test_topic_common import assert_main_returns_expected

exercise = import_module("template.exercise")
main = exercise.main


class TestExercise:
    def test_main_returns_expected(self):
        assert_main_returns_expected(main)
