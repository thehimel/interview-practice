"""Test logic for list sort topic."""

from importlib import import_module

sort = import_module("06-lists.solutions.sort")

NUMS = [2, 4, 6, 8, 10, 12, 14, 16]
COLORS = ["red", "blue", "green", "yellow", "black", "white", "gray"]
VALS = ["2", "10", "1"]
NUMS_ABS = [-3, 2, -1]
LABELS = ["Beta", "alpha", "Gamma"]
ITEMS = ["  red", "blue  ", " green "]


def create_sort_test_class(module):
    """Create a test class that runs sort assertions against the given module."""

    class TestSort:
        def test_sort_ascending(self):
            result = module.sort_ascending(NUMS)
            assert result == [2, 4, 6, 8, 10, 12, 14, 16]
            assert NUMS == [2, 4, 6, 8, 10, 12, 14, 16]

        def test_sort_descending(self):
            result = module.sort_descending(NUMS)
            assert result == [16, 14, 12, 10, 8, 6, 4, 2]
            assert NUMS == [2, 4, 6, 8, 10, 12, 14, 16]

        def test_reverse_items(self):
            result = module.reverse_items(NUMS)
            assert result == [16, 14, 12, 10, 8, 6, 4, 2]
            assert NUMS == [2, 4, 6, 8, 10, 12, 14, 16]

        def test_reversed_new_list(self):
            result = module.reversed_new_list(NUMS)
            assert result == [16, 14, 12, 10, 8, 6, 4, 2]
            assert NUMS == [2, 4, 6, 8, 10, 12, 14, 16]

        def test_sort_by_len(self):
            result = module.sort_by_len(COLORS)
            assert result == ["red", "blue", "gray", "green", "black", "white", "yellow"]
            assert COLORS == ["red", "blue", "green", "yellow", "black", "white", "gray"]

        def test_sort_by_str(self):
            result = module.sort_by_str(NUMS)
            assert result == [10, 12, 14, 16, 2, 4, 6, 8]
            assert NUMS == [2, 4, 6, 8, 10, 12, 14, 16]

        def test_sort_by_int(self):
            result = module.sort_by_int(VALS)
            assert result == ["1", "2", "10"]
            assert VALS == ["2", "10", "1"]

        def test_sort_by_abs(self):
            result = module.sort_by_abs(NUMS_ABS)
            assert result == [-1, 2, -3]
            assert NUMS_ABS == [-3, 2, -1]

        def test_sort_by_str_lower(self):
            result = module.sort_by_str_lower(LABELS)
            assert result == ["alpha", "Beta", "Gamma"]
            assert LABELS == ["Beta", "alpha", "Gamma"]

        def test_sort_by_str_strip(self):
            result = module.sort_by_str_strip(ITEMS)
            assert result == ["blue  ", " green ", "  red"]
            assert ITEMS == ["  red", "blue  ", " green "]

        def test_sort_by_distance_from_12(self):
            result = module.sort_by_distance_from_12(NUMS)
            assert result == [12, 10, 14, 8, 16, 6, 4, 2]
            assert NUMS == [2, 4, 6, 8, 10, 12, 14, 16]

    return TestSort


TestSortSolution = create_sort_test_class(sort)
