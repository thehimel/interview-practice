from importlib import import_module

from test_casting_common import assert_cast

exercise = import_module("03_casting.exercise")
cast = exercise.cast


class TestExercise:
    def test_cast(self):
        assert_cast(cast)
