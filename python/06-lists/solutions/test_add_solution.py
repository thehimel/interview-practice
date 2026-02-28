"""Test logic for list add topic."""

from importlib import import_module

add = import_module("06-lists.solutions.add")

NUMS = [2, 4, 6, 8, 10, 12, 14, 16]


def create_add_test_class(module):
    """Create a test class that runs add assertions against the given module."""

    class TestAdd:
        def test_add_items(self):
            assert module.add_items(NUMS) == [2, 4, 0, 6, 8, 10, 12, 14, 16, 8]
            assert NUMS == [2, 4, 6, 8, 10, 12, 14, 16]

        def test_concat_with_plus(self):
            assert module.concat_with_plus(NUMS, [8, 10]) == [2, 4, 6, 8, 10, 12, 14, 16, 8, 10]
            assert NUMS == [2, 4, 6, 8, 10, 12, 14, 16]

        def test_concat_with_extend(self):
            assert module.concat_with_extend(NUMS, [8, 10]) == [2, 4, 6, 8, 10, 12, 14, 16, 8, 10]
            assert module.concat_with_extend(NUMS, (8, 10)) == [2, 4, 6, 8, 10, 12, 14, 16, 8, 10]
            assert sorted(module.concat_with_extend(NUMS, {8, 10})) == [2, 4, 6, 8, 8, 10, 10, 12, 14, 16]
            assert module.concat_with_extend(NUMS, {8: "a", 10: "b"}) == [2, 4, 6, 8, 10, 12, 14, 16, 8, 10]
            assert NUMS == [2, 4, 6, 8, 10, 12, 14, 16]

    return TestAdd


TestAddSolution = create_add_test_class(add)
