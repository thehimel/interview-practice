"""Test logic for list change topic."""

from importlib import import_module

change = import_module("06-lists.solutions.change")

COLORS = ["red", "blue", "green", "yellow", "black", "white", "gray"]


def create_change_test_class(module):
    """Create a test class that runs change assertions against the given module."""

    class TestChange:
        def test_change_items(self):
            assert module.change_items(COLORS) == [
                "red", "mint", "olive", "navy", "cyan", "black", "white", "gray"
            ]
            assert COLORS == ["red", "blue", "green", "yellow", "black", "white", "gray"]

    return TestChange


TestChangeSolution = create_change_test_class(change)
