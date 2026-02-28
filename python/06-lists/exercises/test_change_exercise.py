"""Test logic for list change exercises."""

from importlib import import_module

from ..solutions.test_change_solution import create_change_test_class

change = import_module("06-lists.exercises.change")

TestChangeExercise = create_change_test_class(change)
