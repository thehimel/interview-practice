from importlib import import_module

from test_casting_common import assert_cast

solution = import_module("03_casting.solution")
cast = solution.cast


class TestSolution:
    def test_cast(self):
        assert_cast(cast)
