"""Test logic for variables topic."""

from importlib import import_module

EXPECTED_TYPES = (str, int, float)
EXPECTED_NAME = "Apple"
EXPECTED_QUANTITY = 2
EXPECTED_WEIGHT = 4.2


def create_variables_test_class(module):
    """Create a test class that runs variables assertions against the given module."""

    class TestVariables:
        def test_get_types(self):
            assert module.get_types() == EXPECTED_TYPES

        def test_assign_globals(self):
            module.assign_globals()
            assert module.X == EXPECTED_NAME
            assert module.Y == EXPECTED_QUANTITY
            assert module.Z == EXPECTED_WEIGHT

    return TestVariables


solution = import_module("02-variables.solution")
TestVariablesSolution = create_variables_test_class(solution)
