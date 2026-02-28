"""Test logic for list access topic."""

from importlib import import_module

access = import_module("06-lists.solutions.access")

NUMS = [2, 4, 6, 8, 10, 12, 14, 16]


def create_access_test_class(module):
    """Create a test class that runs access assertions against the given module."""

    class TestAccess:
        def test_01_first_last_and_at_2(self):
            assert module.first_last_and_at_2(NUMS) == (2, 16, 6)

        def test_02_split_at_4(self):
            assert module.split_at_4(NUMS) == ([2, 4, 6, 8], [10, 12, 14, 16])

        def test_03_slices_2_to_6_and_negative(self):
            assert module.slices_2_to_6_and_negative(NUMS) == ([6, 8, 10, 12], [10, 12])

        def test_04_nums_reversed_slice(self):
            assert module.nums_reversed_slice(NUMS) == [16, 14, 12, 10, 8, 6, 4, 2]

        def test_05_nums_reversed_builtin(self):
            assert module.nums_reversed_builtin(NUMS) == [16, 14, 12, 10, 8, 6, 4, 2]

        def test_06_nums_reversed_method(self):
            assert module.nums_reversed_method(NUMS) == [16, 14, 12, 10, 8, 6, 4, 2]
            assert NUMS == [2, 4, 6, 8, 10, 12, 14, 16]

        def test_07_count_six_and_find_eight(self):
            assert module.count_six_and_find_eight(NUMS) == (1, 3)
            assert module.count_six_and_find_eight([6, 6, 6]) == (3, -1)
            assert module.count_six_and_find_eight([1, 2, 3]) == (0, -1)

    return TestAccess


TestAccessSolution = create_access_test_class(access)
