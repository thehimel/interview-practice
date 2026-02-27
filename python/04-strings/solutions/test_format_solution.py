from importlib import import_module

format_module = import_module("04-strings.solutions.format")


def create_format_test_class(module):
    """Create a test class that runs format assertions against the given module."""

    class TestFormat:
        def test_fstring_example(self):
            assert module.fstring_example("Alice", 86.8) == "Name: Alice, Score: 86.8"

        def test_decimal_format(self):
            assert module.decimal_format(2.46) == "2.46"

        def test_expr_in_fstring(self):
            assert module.expr_in_fstring(4, 6) == "4*6=24"

        def test_format_method(self):
            assert module.format_method("{} and {}", "a", "b") == "a and b"

        def test_centered(self):
            assert module.centered("hi", 6) == "  hi  "

        def test_left_justified(self):
            assert module.left_justified("hi", 6) == "hi    "

        def test_right_justified(self):
            assert module.right_justified("hi", 6) == "    hi"

        def test_zfill_str(self):
            assert module.zfill_str("42", 6) == "000042"

    return TestFormat


TestFormatSolution = create_format_test_class(format_module)
