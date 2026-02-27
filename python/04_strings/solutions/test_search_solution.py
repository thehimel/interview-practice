from importlib import import_module

search = import_module("04_strings.solutions.search")


def create_search_test_class(module):
    """Create a test class that runs search assertions against the given module."""

    class TestSearch:
        def test_find_sub(self):
            assert module.find_sub("hello world", "world") == 6

        def test_index_sub(self):
            assert module.index_sub("python", "t") == 2

        def test_rfind_sub(self):
            assert module.rfind_sub("hello world", "l") == 9

        def test_rindex_sub(self):
            assert module.rindex_sub("hello woorld", "o") == 8

        def test_count_sub(self):
            assert module.count_sub("hello", "l") == 2

        def test_contains_sub(self):
            assert module.contains_sub("hello world", "ell") is True

        def test_starts_with(self):
            assert module.starts_with("hello world", "hello") is True

        def test_ends_with(self):
            assert module.ends_with("hello.py", ".py") is True

    return TestSearch


TestSearchSolution = create_search_test_class(search)
