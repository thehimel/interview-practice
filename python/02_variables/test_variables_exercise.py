from importlib import import_module

from test_variables_common import assert_assign_globals, assert_get_types

exercise = import_module("02_variables.exercise")
assign_globals = exercise.assign_globals
get_types = exercise.get_types


class TestExercise:
    def test_get_types(self):
        assert_get_types(get_types)

    def test_assign_globals(self):
        assert_assign_globals(assign_globals, exercise)
