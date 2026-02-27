from importlib import import_module

modify = import_module("04-strings.solutions.modify")


def create_modify_test_class(module):
    """Create a test class that runs modify assertions against the given module."""

    class TestModify:
        def test_to_upper(self):
            assert module.to_upper("hello") == "HELLO"

        def test_to_lower(self):
            assert module.to_lower("HELLO") == "hello"

        def test_casefold_str(self):
            assert module.casefold_str("Straße") == "strasse"

        def test_capitalized(self):
            assert module.capitalized("hello") == "Hello"

        def test_swap_case(self):
            assert module.swap_case("HeLLo") == "hEllO"

        def test_title_case(self):
            assert module.title_case("hello world") == "Hello World"

        def test_stripped(self):
            assert module.stripped("  Hello World  ") == "Hello World"

        def test_left_stripped(self):
            assert module.left_stripped("  Hello World  ") == "Hello World  "

        def test_right_stripped(self):
            assert module.right_stripped("  Hello World  ") == "  Hello World"

        def test_stripped_chars(self):
            assert module.stripped_chars("xxxhello worldxxx", "x") == "hello world"

        def test_replaced(self):
            assert module.replaced("aabb", "a", "x") == "xxbb"

        def test_replace_count(self):
            assert module.replace_count("one one one", "one", "two", 2) == "two two one"

        def test_split_str(self):
            assert module.split_str("a,b,c", ",") == ["a", "b", "c"]

        def test_rsplit_str(self):
            assert module.rsplit_str("a,b,c,d", ",", 2) == ["a,b", "c", "d"]

        def test_split_lines(self):
            assert module.split_lines("line0\nline2\nline4") == ["line0", "line2", "line4"]

        def test_remove_prefix(self):
            assert module.remove_prefix("https://example.com", "https://") == "example.com"

        def test_remove_suffix(self):
            assert module.remove_suffix("file.txt", ".txt") == "file"

        def test_partition_str(self):
            assert module.partition_str("a:b:c", ":") == ("a", ":", "b:c")

        def test_rpartition_str(self):
            assert module.rpartition_str("a:b:c", ":") == ("a:b", ":", "c")

    return TestModify


TestModifySolution = create_modify_test_class(modify)
