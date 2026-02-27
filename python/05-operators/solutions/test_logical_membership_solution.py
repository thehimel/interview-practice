from importlib import import_module

check = import_module("05-operators.solutions.logical_membership").check


def create_logical_membership_test_class(fn):
    """Create a test class that runs logical membership assertions against the given function."""

    class TestLogicalMembership:
        def test_unavailable_not_in_nums(self):
            assert fn([8, 12, 14], 4, 10) == -1

        def test_unavailable_none(self):
            assert fn([8, 12, 14], None, 10) == -1

        def test_appropriate(self):
            assert fn([8, 12, 14], 12, 10) is True

        def test_inappropriate(self):
            assert fn([8, 12, 14], 8, 10) is False

        def test_inappropriate_equal(self):
            assert fn([8, 10, 12], 10, 10) is False

    return TestLogicalMembership


TestLogicalMembershipSolution = create_logical_membership_test_class(check)
