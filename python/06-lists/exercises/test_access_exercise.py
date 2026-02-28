"""Test logic for list access exercises."""

from importlib import import_module

from ..solutions.test_access_solution import create_access_test_class

access = import_module("06-lists.exercises.access")

TestAccessExercise = create_access_test_class(access)
