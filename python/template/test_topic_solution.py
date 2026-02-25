from importlib import import_module

from test_topic_common import assert_main_returns_expected

solution = import_module("template.solution")
main = solution.main


class TestSolution:
    def test_main_returns_expected(self):
        assert_main_returns_expected(main)
