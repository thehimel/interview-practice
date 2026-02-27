"""Test logic for template topic."""

from importlib import import_module

EXPECTED_OUTPUT = ""


def create_topic_test_class(main_fn):
    """Create a test class that runs topic assertions against the given function."""

    class TestTopic:
        def test_main_returns_expected(self):
            assert main_fn() == EXPECTED_OUTPUT

    return TestTopic


topic = import_module("template.solutions.topic")
TestTopicSolution = create_topic_test_class(topic.main)
