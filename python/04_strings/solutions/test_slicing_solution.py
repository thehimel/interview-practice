from importlib import import_module

slicing = import_module("04_strings.solutions.slicing")


def create_slicing_test_class(module):
    """Create a test class that runs slicing assertions against the given module."""

    class TestSlicing:
        def test_first_char(self):
            assert module.first_char("Python") == "P"

        def test_last_char(self):
            assert module.last_char("Python") == "n"

        def test_first_n(self):
            assert module.first_n("Python", 2) == "Py"

        def test_n_to_last(self):
            assert module.n_to_last("Python", 2) == "thon"

        def test_negative_slice(self):
            assert module.negative_slice("Python", 4, 2) == "th"

        def test_reversed_str(self):
            assert module.reversed_str("Python") == "nohtyP"

        def test_reversed_str_reversed(self):
            assert module.reversed_str_reversed("Python") == "nohtyP"

        def test_string_length(self):
            assert module.string_length("Python") == 6

    return TestSlicing


TestSlicingSolution = create_slicing_test_class(slicing)
