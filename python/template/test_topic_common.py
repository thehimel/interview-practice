"""Shared test constants and assertions for template topic."""

EXPECTED_OUTPUT = ""


def assert_main_returns_expected(main_fn):
    assert main_fn() == EXPECTED_OUTPUT
