import pytest
from importlib import import_module

identity_module = import_module("05_operators.solutions.identity")
identity_check = identity_module.identity_check
equality_check = identity_module.equality_check


def create_identity_test_class(identity_fn, equality_fn):
    """Create a test class that runs identity and equality assertions against the given functions."""

    class TestIdentity:
        def test_is_none(self):
            assert identity_fn(None, "is") == "is none"

        def test_is_not_none(self):
            assert identity_fn(8, "is not") == "is not none"

        def test_is_not_same(self):
            assert identity_fn(None, "is not") == "is none"

        def test_is_true(self):
            assert identity_fn(True, "is true") == "is true"

        def test_is_not_true(self):
            assert identity_fn(False, "is not true") == "is not true"

        def test_is_not_true_when_true(self):
            assert identity_fn(True, "is not true") == "is true"

        def test_identity_unknown_operator_raises(self):
            with pytest.raises(ValueError, match="Unknown operator"):
                identity_fn(None, "?")

        def test_equals_values(self):
            assert equality_fn(8, 8, "==") == "same"

        def test_equals_different(self):
            assert equality_fn(8, 4, "==") == "different"

        def test_equals_lists(self):
            assert equality_fn([], [], "==") == "same"

        def test_not_equals(self):
            assert equality_fn(8, 4, "!=") == "same"

        def test_not_equals_same(self):
            assert equality_fn(8, 8, "!=") == "different"

        def test_equality_unknown_operator_raises(self):
            with pytest.raises(ValueError, match="Unknown operator"):
                equality_fn(2, 4, "?")

    return TestIdentity


TestIdentitySolution = create_identity_test_class(identity_check, equality_check)
