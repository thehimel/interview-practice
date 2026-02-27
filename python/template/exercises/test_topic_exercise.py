from importlib import import_module

from ..solutions.test_topic_solution import create_topic_test_class

topic = import_module("template.exercises.topic")

TestTopicExercise = create_topic_test_class(topic.main)
