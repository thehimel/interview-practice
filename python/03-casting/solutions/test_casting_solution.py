"""Test logic for casting topic."""

from importlib import import_module

EXPECTED = (222, 82.6, "66")


def create_casting_test_class(cast_fn):
    """Create a test class that runs casting assertions against the given function."""

    class TestCasting:
        def test_cast(self):
            assert cast_fn() == EXPECTED

    return TestCasting


casting = import_module("03-casting.solutions.casting")
TestCastingSolution = create_casting_test_class(casting.cast)
