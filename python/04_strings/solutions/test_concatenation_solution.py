from importlib import import_module

concatenation = import_module("04_strings.solutions.concatenation")


def create_concatenation_test_class(module):
    """Create a test class that runs concatenation assertions against the given module."""

    class TestConcatenation:
        def test_concat(self):
            assert module.concat("Hello", "World") == "HelloWorld"

        def test_join_str(self):
            assert module.join_str("-", ["a", "b", "c"]) == "a-b-c"

    return TestConcatenation


TestConcatenationSolution = create_concatenation_test_class(concatenation)
