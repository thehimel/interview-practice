"""Shared test constants and assertions for variables topic."""

EXPECTED_TYPES = (str, int, float)

EXPECTED_NAME = "Apple"
EXPECTED_QUANTITY = 2
EXPECTED_WEIGHT = 4.2


def assert_get_types(get_types_fn):
    assert get_types_fn() == EXPECTED_TYPES


def assert_assign_globals(assign_globals_fn, module):
    assign_globals_fn()
    assert module.X == EXPECTED_NAME
    assert module.Y == EXPECTED_QUANTITY
    assert module.Z == EXPECTED_WEIGHT
