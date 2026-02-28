"""Test logic for list remove exercises."""

from importlib import import_module

from ..solutions.test_remove_solution import create_remove_test_class

remove = import_module("06-lists.exercises.remove")

TestRemoveExercise = create_remove_test_class(remove)
