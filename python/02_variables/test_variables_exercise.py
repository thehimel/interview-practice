from importlib import import_module

from test_variables_common import EXPECTED_TYPES

exercise = import_module("02_variables.exercise")
assign_globals = exercise.assign_globals
get_types = exercise.get_types


class TestExercise:
    def test_unpacked_values(self):
        name, quantity, weight = exercise.name, exercise.quantity, exercise.weight

        assert name == "Apple"
        assert quantity == 2
        assert weight == 4.2

    def test_get_types(self):
        assert get_types() == EXPECTED_TYPES

    def test_assign_globals(self):
        assign_globals()
        assert exercise.X == "Apple"
        assert exercise.Y == 2
        assert exercise.Z == 4.2
