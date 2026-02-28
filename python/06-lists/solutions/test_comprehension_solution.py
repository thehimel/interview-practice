"""Test logic for list comprehension topic."""

from importlib import import_module

comp_mod = import_module("06-lists.solutions.comprehension")

EVENS = [2, 4, 6, 8, 10]


def create_comprehension_test_class(module):
    """Create a test class that runs comprehension assertions against the given module."""

    class TestComprehension:
        def test_double_elements(self):
            assert module.double_elements(EVENS) == [4, 8, 12, 16, 20]

        def test_filter_greater_than(self):
            assert module.filter_greater_than(EVENS, 4) == [6, 8, 10]
            assert module.filter_greater_than(EVENS, 10) == []

        def test_evens_from_range(self):
            assert module.evens_from_range(10) == [0, 2, 4, 6, 8]
            assert module.evens_from_range(0) == []

        def test_square_elements(self):
            assert module.square_elements(EVENS) == [4, 16, 36, 64, 100]

    return TestComprehension


TestComprehensionSolution = create_comprehension_test_class(comp_mod)
