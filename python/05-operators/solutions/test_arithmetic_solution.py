import pytest
from importlib import import_module

arithmetic = import_module("05-operators.solutions.arithmetic").arithmetic


def create_arithmetic_test_class(fn):
    """Create a test class that runs arithmetic assertions against the given function."""

    class TestArithmetic:
        def test_add(self):
            assert fn(8, 4, "+") == 12

        def test_subtract(self):
            assert fn(10, 6, "-") == 4

        def test_multiply(self):
            assert fn(6, 8, "*") == 48

        def test_divide(self):
            assert fn(12, 4, "/") == 3.0

        def test_modulus(self):
            assert fn(18, 4, "%") == 2

        def test_exponentiate(self):
            assert fn(2, 4, "**") == 16

        def test_floor_divide(self):
            assert fn(18, 4, "//") == 4

        def test_unknown_operator_raises(self):
            with pytest.raises(ValueError, match="Unknown operator"):
                fn(2, 4, "?")

    return TestArithmetic


TestArithmeticSolution = create_arithmetic_test_class(arithmetic)
