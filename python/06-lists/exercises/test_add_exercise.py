"""Test logic for list add exercises."""

from importlib import import_module

from ..solutions.test_add_solution import create_add_test_class

add = import_module("06-lists.exercises.add")

TestAddExercise = create_add_test_class(add)
