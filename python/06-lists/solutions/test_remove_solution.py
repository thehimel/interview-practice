"""Test logic for list remove topic."""

from importlib import import_module

remove = import_module("06-lists.solutions.remove")

COLORS = ["red", "blue", "green", "yellow", "black", "white", "gray"]
COLORS_WITH_DUPES = ["red", "blue", "green", "blue", "black", "white", "blue"]


def create_remove_test_class(module):
    """Create a test class that runs remove assertions against the given module."""

    class TestRemove:
        def test_remove_items(self):
            assert module.remove_items(COLORS) == []
            assert COLORS == ["red", "blue", "green", "yellow", "black", "white", "gray"]

        def test_remove_all_occurrences(self):
            result = module.remove_all_occurrences(COLORS_WITH_DUPES, "blue")
            assert result == ["red", "green", "black", "white"]
            assert COLORS_WITH_DUPES == ["red", "blue", "green", "blue", "black", "white", "blue"]

        def test_remove_all_occurrences_in_place(self):
            data = COLORS_WITH_DUPES.copy()
            result = module.remove_all_occurrences_in_place(data, "blue")
            assert result == ["red", "green", "black", "white"]
            assert data == ["red", "green", "black", "white"]
            assert COLORS_WITH_DUPES == ["red", "blue", "green", "blue", "black", "white", "blue"]

    return TestRemove


TestRemoveSolution = create_remove_test_class(remove)
