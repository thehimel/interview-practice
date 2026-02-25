"""Shared test constants and assertions for casting topic."""

EXPECTED = (222, 82.6, "66")


def assert_cast(cast_fn):
    assert cast_fn() == EXPECTED
