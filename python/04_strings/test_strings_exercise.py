from importlib import import_module

from test_strings_common import (
    assert_casefold_str,
    assert_capitalized,
    assert_centered,
    assert_check_isalnum,
    assert_check_isalpha,
    assert_check_isdigit,
    assert_check_islower,
    assert_check_isnumeric,
    assert_check_isspace,
    assert_check_istitle,
    assert_check_isupper,
    assert_concat,
    assert_contains_sub,
    assert_count_sub,
    assert_decimal_format,
    assert_ends_with,
    assert_expr_in_fstring,
    assert_first_char,
    assert_first_n,
    assert_find_sub,
    assert_format_method,
    assert_fstring_example,
    assert_index_sub,
    assert_join_str,
    assert_last_char,
    assert_left_justified,
    assert_left_stripped,
    assert_negative_slice,
    assert_n_to_last,
    assert_partition_str,
    assert_remove_prefix,
    assert_remove_suffix,
    assert_replace_count,
    assert_replaced,
    assert_reversed_str,
    assert_reversed_str_reversed,
    assert_right_justified,
    assert_right_stripped,
    assert_rfind_sub,
    assert_rindex_sub,
    assert_rsplit_str,
    assert_rpartition_str,
    assert_split_lines,
    assert_split_str,
    assert_starts_with,
    assert_string_length,
    assert_stripped,
    assert_stripped_chars,
    assert_swap_case,
    assert_title_case,
    assert_to_lower,
    assert_to_upper,
    assert_zfill_str,
)

exercise = import_module("04_strings.exercise")


class TestExercise:
    def test_concat(self):
        assert_concat(exercise.concat)

    def test_join_str(self):
        assert_join_str(exercise.join_str)

    def test_fstring_example(self):
        assert_fstring_example(exercise.fstring_example)

    def test_decimal_format(self):
        assert_decimal_format(exercise.decimal_format)

    def test_expr_in_fstring(self):
        assert_expr_in_fstring(exercise.expr_in_fstring)

    def test_format_method(self):
        assert_format_method(exercise.format_method)

    def test_centered(self):
        assert_centered(exercise.centered)

    def test_left_justified(self):
        assert_left_justified(exercise.left_justified)

    def test_right_justified(self):
        assert_right_justified(exercise.right_justified)

    def test_zfill_str(self):
        assert_zfill_str(exercise.zfill_str)

    def test_to_upper(self):
        assert_to_upper(exercise.to_upper)

    def test_to_lower(self):
        assert_to_lower(exercise.to_lower)

    def test_casefold_str(self):
        assert_casefold_str(exercise.casefold_str)

    def test_capitalized(self):
        assert_capitalized(exercise.capitalized)

    def test_swap_case(self):
        assert_swap_case(exercise.swap_case)

    def test_title_case(self):
        assert_title_case(exercise.title_case)

    def test_stripped(self):
        assert_stripped(exercise.stripped)

    def test_left_stripped(self):
        assert_left_stripped(exercise.left_stripped)

    def test_right_stripped(self):
        assert_right_stripped(exercise.right_stripped)

    def test_stripped_chars(self):
        assert_stripped_chars(exercise.stripped_chars)

    def test_replaced(self):
        assert_replaced(exercise.replaced)

    def test_replace_count(self):
        assert_replace_count(exercise.replace_count)

    def test_split_str(self):
        assert_split_str(exercise.split_str)

    def test_rsplit_str(self):
        assert_rsplit_str(exercise.rsplit_str)

    def test_split_lines(self):
        assert_split_lines(exercise.split_lines)

    def test_remove_prefix(self):
        assert_remove_prefix(exercise.remove_prefix)

    def test_remove_suffix(self):
        assert_remove_suffix(exercise.remove_suffix)

    def test_partition_str(self):
        assert_partition_str(exercise.partition_str)

    def test_rpartition_str(self):
        assert_rpartition_str(exercise.rpartition_str)

    def test_find_sub(self):
        assert_find_sub(exercise.find_sub)

    def test_index_sub(self):
        assert_index_sub(exercise.index_sub)

    def test_rfind_sub(self):
        assert_rfind_sub(exercise.rfind_sub)

    def test_rindex_sub(self):
        assert_rindex_sub(exercise.rindex_sub)

    def test_count_sub(self):
        assert_count_sub(exercise.count_sub)

    def test_contains_sub(self):
        assert_contains_sub(exercise.contains_sub)

    def test_starts_with(self):
        assert_starts_with(exercise.starts_with)

    def test_ends_with(self):
        assert_ends_with(exercise.ends_with)

    def test_first_char(self):
        assert_first_char(exercise.first_char)

    def test_last_char(self):
        assert_last_char(exercise.last_char)

    def test_first_n(self):
        assert_first_n(exercise.first_n)

    def test_n_to_last(self):
        assert_n_to_last(exercise.n_to_last)

    def test_negative_slice(self):
        assert_negative_slice(exercise.negative_slice)

    def test_reversed_str(self):
        assert_reversed_str(exercise.reversed_str)

    def test_reversed_str_reversed(self):
        assert_reversed_str_reversed(exercise.reversed_str_reversed)

    def test_string_length(self):
        assert_string_length(exercise.string_length)

    def test_check_isalpha(self):
        assert_check_isalpha(exercise.check_isalpha)

    def test_check_isalnum(self):
        assert_check_isalnum(exercise.check_isalnum)

    def test_check_isdigit(self):
        assert_check_isdigit(exercise.check_isdigit)

    def test_check_isnumeric(self):
        assert_check_isnumeric(exercise.check_isnumeric)

    def test_check_islower(self):
        assert_check_islower(exercise.check_islower)

    def test_check_isupper(self):
        assert_check_isupper(exercise.check_isupper)

    def test_check_istitle(self):
        assert_check_istitle(exercise.check_istitle)

    def test_check_isspace(self):
        assert_check_isspace(exercise.check_isspace)
