from importlib import import_module

from test_variables_common import EXPECTED_TYPES

solution = import_module("02_variables.solution")
assign_globals = solution.assign_globals
get_types = solution.get_types


class TestSolution:
    def test_unpacked_values(self):
        name, quantity, weight = solution.name, solution.quantity, solution.weight

        assert name == "Apple"
        assert quantity == 2
        assert weight == 4.2

    def test_get_types(self):
        assert get_types() == EXPECTED_TYPES

    def test_assign_globals(self):
        assign_globals()
        assert solution.X == "Apple"
        assert solution.Y == 2
        assert solution.Z == 4.2
