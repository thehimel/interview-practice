import pytest
from importlib import import_module

comparison = import_module("05_operators.solutions.comparison").comparison


def create_comparison_test_class(fn):
    """Create a test class that runs comparison assertions against the given function."""

    class TestComparison:
        def test_equal(self):
            assert fn(8, 8, "==") == "equal"

        def test_equal_false(self):
            assert fn(8, 4, "==") == "not equal"

        def test_not_equal(self):
            assert fn(8, 4, "!=") == "not equal"

        def test_greater(self):
            assert fn(8, 4, ">") == "greater"

        def test_less(self):
            assert fn(4, 8, "<") == "less"

        def test_greater_or_equal(self):
            assert fn(8, 8, ">=") == "greater or equal"

        def test_less_or_equal(self):
            assert fn(4, 8, "<=") == "less or equal"

        def test_unknown_operator_raises(self):
            with pytest.raises(ValueError, match="Unknown operator"):
                fn(2, 4, "?")

    return TestComparison


TestComparisonSolution = create_comparison_test_class(comparison)
