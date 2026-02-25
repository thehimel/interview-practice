from importlib import import_module

from test_variables_common import assert_assign_globals, assert_get_types

solution = import_module("02_variables.solution")
assign_globals = solution.assign_globals
get_types = solution.get_types


class TestSolution:
    def test_get_types(self):
        assert_get_types(get_types)

    def test_assign_globals(self):
        assert_assign_globals(assign_globals, solution)
