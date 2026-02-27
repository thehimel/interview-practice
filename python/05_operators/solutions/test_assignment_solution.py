import pytest

from .assignment import assignment, walrus


def create_assignment_test_class(assignment_fn, walrus_fn):
    """Create a test class that runs assignment assertions against the given functions."""

    class TestAssignment:
        def test_assign(self):
            assert assignment_fn(10, 10, "=") == 10

        def test_add(self):
            assert assignment_fn(10, 4, "+=") == 14

        def test_subtract(self):
            assert assignment_fn(10, 2, "-=") == 8

        def test_multiply(self):
            assert assignment_fn(10, 2, "*=") == 20

        def test_divide(self):
            assert assignment_fn(12, 4, "/=") == 3.0

        def test_modulus(self):
            assert assignment_fn(10, 4, "%=") == 2

        def test_floor_divide(self):
            assert assignment_fn(8, 4, "//=") == 2

        def test_exponentiate(self):
            assert assignment_fn(10, 2, "**=") == 100

        def test_unknown_operator_raises(self):
            with pytest.raises(ValueError, match="Unknown operator"):
                assignment_fn(2, 4, "?")

        def test_walrus(self):
            assert walrus_fn(12) == 12

    return TestAssignment


TestAssignmentSolution = create_assignment_test_class(assignment, walrus)
