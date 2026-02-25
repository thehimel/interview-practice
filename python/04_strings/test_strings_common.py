"""Shared test assertions for strings topic."""

def assert_first_char(fn):
    assert fn("Python") == "P"


def assert_last_char(fn):
    assert fn("Python") == "n"


def assert_first_n(fn):
    assert fn("Python", 2) == "Py"


def assert_n_to_last(fn):
    assert fn("Python", 2) == "thon"


def assert_reversed_str(fn):
    assert fn("Python") == "nohtyP"


def assert_reversed_str_reversed(fn):
    assert fn("Python") == "nohtyP"


def assert_negative_slice(fn):
    assert fn("Python", 4, 2) == "th"


def assert_string_length(fn):
    assert fn("Python") == 6


def assert_to_upper(fn):
    assert fn("hello") == "HELLO"


def assert_to_lower(fn):
    assert fn("HELLO") == "hello"


def assert_stripped(fn):
    assert fn("  Hello World  ") == "Hello World"


def assert_left_stripped(fn):
    assert fn("  Hello World  ") == "Hello World  "


def assert_right_stripped(fn):
    assert fn("  Hello World  ") == "  Hello World"


def assert_stripped_chars(fn):
    assert fn("xxxhello worldxxx", "x") == "hello world"


def assert_replaced(fn):
    assert fn("aabb", "a", "x") == "xxbb"


def assert_replace_count(fn):
    assert fn("one one one", "one", "two", 2) == "two two one"


def assert_split_str(fn):
    assert fn("a,b,c", ",") == ["a", "b", "c"]


def assert_rsplit_str(fn):
    assert fn("a,b,c,d", ",", 2) == ["a,b", "c", "d"]


def assert_split_lines(fn):
    assert fn("line0\nline2\nline4") == ["line0", "line2", "line4"]


def assert_capitalized(fn):
    assert fn("hello") == "Hello"


def assert_swap_case(fn):
    assert fn("HeLLo") == "hEllO"


def assert_title_case(fn):
    assert fn("hello world") == "Hello World"


def assert_remove_prefix(fn):
    assert fn("https://example.com", "https://") == "example.com"


def assert_remove_suffix(fn):
    assert fn("file.txt", ".txt") == "file"


def assert_partition_str(fn):
    assert fn("a:b:c", ":") == ("a", ":", "b:c")


def assert_rpartition_str(fn):
    assert fn("a:b:c", ":") == ("a:b", ":", "c")


def assert_casefold_str(fn):
    assert fn("Straße") == "strasse"


def assert_concat(fn):
    assert fn("Hello", "World") == "HelloWorld"


def assert_join_str(fn):
    assert fn("-", ["a", "b", "c"]) == "a-b-c"


def assert_fstring_example(fn):
    assert fn("Alice", 86.8) == "Name: Alice, Score: 86.8"


def assert_decimal_format(fn):
    assert fn(2.46) == "2.46"


def assert_expr_in_fstring(fn):
    assert fn(4, 6) == "4*6=24"


def assert_format_method(fn):
    assert fn("{} and {}", "a", "b") == "a and b"


def assert_zfill_str(fn):
    assert fn("42", 6) == "000042"


def assert_find_sub(fn):
    assert fn("hello world", "world") == 6


def assert_centered(fn):
    assert fn("hi", 6) == "  hi  "


def assert_left_justified(fn):
    assert fn("hi", 6) == "hi    "


def assert_right_justified(fn):
    assert fn("hi", 6) == "    hi"


def assert_contains_sub(fn):
    assert fn("hello world", "ell") is True


def assert_rfind_sub(fn):
    assert fn("hello world", "l") == 9


def assert_rindex_sub(fn):
    assert fn("hello woorld", "o") == 8


def assert_check_isalnum(fn):
    assert fn("abc246") is True


def assert_check_isalpha(fn):
    assert fn("letters") is True


def assert_check_isdigit(fn):
    assert fn("468") is True


def assert_check_islower(fn):
    assert fn("lowercase") is True


def assert_check_isupper(fn):
    assert fn("UPPERCASE") is True


def assert_check_isnumeric(fn):
    assert fn("½¾") is True


def assert_check_isspace(fn):
    assert fn("   ") is True


def assert_check_istitle(fn):
    assert fn("Title Case") is True


def assert_count_sub(fn):
    assert fn("hello", "l") == 2


def assert_index_sub(fn):
    assert fn("python", "t") == 2


def assert_starts_with(fn):
    assert fn("hello world", "hello") is True


def assert_ends_with(fn):
    assert fn("hello.py", ".py") is True
