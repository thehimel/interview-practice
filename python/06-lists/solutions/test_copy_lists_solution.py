"""Test logic for list copy topic."""

from importlib import import_module

copy_mod = import_module("06-lists.solutions.copy_lists")

FLAT = [2, 4, 6]
NESTED = [[1, 2], [3, 4]]


def create_copy_test_class(module):
    """Create a test class that runs copy assertions against the given module."""

    class TestCopy:
        def test_copy_with_copy(self):
            result = module.copy_with_copy(FLAT)
            assert result == [2, 4, 6, 8]
            assert result is not FLAT
            assert FLAT == [2, 4, 6]

        def test_copy_with_list(self):
            result = module.copy_with_list(FLAT)
            assert result == [2, 4, 6, 8]
            assert result is not FLAT
            assert FLAT == [2, 4, 6]

        def test_copy_with_slice(self):
            result = module.copy_with_slice(FLAT)
            assert result == [2, 4, 6, 8]
            assert result is not FLAT
            assert FLAT == [2, 4, 6]

        def test_shallow_nested_append(self):
            original = [[1, 2], [3, 4]]
            result = module.shallow_nested_append(original)
            assert result == [[1, 2, 99], [3, 4]]
            assert original == [[1, 2, 99], [3, 4]]  # mutated (shared)

        def test_shallow_first_level_append(self):
            original = [[1, 2], [3, 4]]
            result = module.shallow_first_level_append(original)
            assert result == [[1, 2], [3, 4], [5, 6]]
            assert original == [[1, 2], [3, 4]]

        def test_shallow_first_level_pop(self):
            original = [[1, 2], [3, 4]]
            result = module.shallow_first_level_pop(original)
            assert result == [[1, 2]]
            assert original == [[1, 2], [3, 4]]

        def test_copy_with_deepcopy(self):
            original = [[1, 2], [3, 4]]
            result = module.copy_with_deepcopy(original)
            assert result == [[1, 2], [3, 4], [5, 6]]
            assert result is not original
            assert result[0] is not original[0]
            assert original == [[1, 2], [3, 4]]

        def test_deep_nested_append(self):
            original = [[1, 2], [3, 4]]
            result = module.deep_nested_append(original)
            assert result == [[1, 2, 100], [3, 4]]
            assert original == [[1, 2], [3, 4]]

        def test_deep_first_level_append(self):
            original = [[1, 2], [3, 4]]
            result = module.deep_first_level_append(original)
            assert result == [[1, 2], [3, 4], [5, 6]]
            assert original == [[1, 2], [3, 4]]

        def test_deep_first_level_pop(self):
            original = [[1, 2], [3, 4]]
            result = module.deep_first_level_pop(original)
            assert result == [[1, 2]]
            assert original == [[1, 2], [3, 4]]

    return TestCopy


TestCopySolution = create_copy_test_class(copy_mod)
