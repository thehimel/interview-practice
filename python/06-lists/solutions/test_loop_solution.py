"""Test logic for list loop topic."""

from importlib import import_module

loop_mod = import_module("06-lists.solutions.loop")

VALS = [2, 4, 6, 8]


def create_loop_test_class(module):
    """Create a test class that runs loop assertions against the given module."""

    class TestLoop:
        def test_collect_direct(self):
            assert module.collect_direct(VALS) == [2, 4, 6, 8]
            assert VALS == [2, 4, 6, 8]

        def test_collect_by_index(self):
            assert module.collect_by_index(VALS) == [2, 4, 6, 8]
            assert VALS == [2, 4, 6, 8]

        def test_collect_while_step(self):
            assert module.collect_while_step(VALS, 2) == [2, 6]
            assert module.collect_while_step(VALS, 1) == [2, 4, 6, 8]
            assert module.collect_while_step([1, 2, 3, 4, 5], 3) == [1, 4]

        def test_collect_reversed(self):
            assert module.collect_reversed(VALS) == [8, 6, 4, 2]
            assert VALS == [2, 4, 6, 8]

        def test_collect_reversed_slice(self):
            assert module.collect_reversed_slice(VALS) == [8, 6, 4, 2]
            assert VALS == [2, 4, 6, 8]

        def test_collect_reversed_by_index(self):
            assert module.collect_reversed_by_index(VALS) == [8, 6, 4, 2]
            assert VALS == [2, 4, 6, 8]

    return TestLoop


TestLoopSolution = create_loop_test_class(loop_mod)
