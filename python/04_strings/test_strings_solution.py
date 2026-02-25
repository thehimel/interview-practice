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

solution = import_module("04_strings.solution")


class TestSolution:
    def test_concat(self):
        assert_concat(solution.concat)

    def test_join_str(self):
        assert_join_str(solution.join_str)

    def test_fstring_example(self):
        assert_fstring_example(solution.fstring_example)

    def test_decimal_format(self):
        assert_decimal_format(solution.decimal_format)

    def test_expr_in_fstring(self):
        assert_expr_in_fstring(solution.expr_in_fstring)

    def test_format_method(self):
        assert_format_method(solution.format_method)

    def test_centered(self):
        assert_centered(solution.centered)

    def test_left_justified(self):
        assert_left_justified(solution.left_justified)

    def test_right_justified(self):
        assert_right_justified(solution.right_justified)

    def test_zfill_str(self):
        assert_zfill_str(solution.zfill_str)

    def test_to_upper(self):
        assert_to_upper(solution.to_upper)

    def test_to_lower(self):
        assert_to_lower(solution.to_lower)

    def test_casefold_str(self):
        assert_casefold_str(solution.casefold_str)

    def test_capitalized(self):
        assert_capitalized(solution.capitalized)

    def test_swap_case(self):
        assert_swap_case(solution.swap_case)

    def test_title_case(self):
        assert_title_case(solution.title_case)

    def test_stripped(self):
        assert_stripped(solution.stripped)

    def test_left_stripped(self):
        assert_left_stripped(solution.left_stripped)

    def test_right_stripped(self):
        assert_right_stripped(solution.right_stripped)

    def test_stripped_chars(self):
        assert_stripped_chars(solution.stripped_chars)

    def test_replaced(self):
        assert_replaced(solution.replaced)

    def test_replace_count(self):
        assert_replace_count(solution.replace_count)

    def test_split_str(self):
        assert_split_str(solution.split_str)

    def test_rsplit_str(self):
        assert_rsplit_str(solution.rsplit_str)

    def test_split_lines(self):
        assert_split_lines(solution.split_lines)

    def test_remove_prefix(self):
        assert_remove_prefix(solution.remove_prefix)

    def test_remove_suffix(self):
        assert_remove_suffix(solution.remove_suffix)

    def test_partition_str(self):
        assert_partition_str(solution.partition_str)

    def test_rpartition_str(self):
        assert_rpartition_str(solution.rpartition_str)

    def test_find_sub(self):
        assert_find_sub(solution.find_sub)

    def test_index_sub(self):
        assert_index_sub(solution.index_sub)

    def test_rfind_sub(self):
        assert_rfind_sub(solution.rfind_sub)

    def test_rindex_sub(self):
        assert_rindex_sub(solution.rindex_sub)

    def test_count_sub(self):
        assert_count_sub(solution.count_sub)

    def test_contains_sub(self):
        assert_contains_sub(solution.contains_sub)

    def test_starts_with(self):
        assert_starts_with(solution.starts_with)

    def test_ends_with(self):
        assert_ends_with(solution.ends_with)

    def test_first_char(self):
        assert_first_char(solution.first_char)

    def test_last_char(self):
        assert_last_char(solution.last_char)

    def test_first_n(self):
        assert_first_n(solution.first_n)

    def test_n_to_last(self):
        assert_n_to_last(solution.n_to_last)

    def test_negative_slice(self):
        assert_negative_slice(solution.negative_slice)

    def test_reversed_str(self):
        assert_reversed_str(solution.reversed_str)

    def test_reversed_str_reversed(self):
        assert_reversed_str_reversed(solution.reversed_str_reversed)

    def test_string_length(self):
        assert_string_length(solution.string_length)

    def test_check_isalpha(self):
        assert_check_isalpha(solution.check_isalpha)

    def test_check_isalnum(self):
        assert_check_isalnum(solution.check_isalnum)

    def test_check_isdigit(self):
        assert_check_isdigit(solution.check_isdigit)

    def test_check_isnumeric(self):
        assert_check_isnumeric(solution.check_isnumeric)

    def test_check_islower(self):
        assert_check_islower(solution.check_islower)

    def test_check_isupper(self):
        assert_check_isupper(solution.check_isupper)

    def test_check_istitle(self):
        assert_check_istitle(solution.check_istitle)

    def test_check_isspace(self):
        assert_check_isspace(solution.check_isspace)
