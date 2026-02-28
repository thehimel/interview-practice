"""Test logic for list copy exercises."""

from importlib import import_module

from ..solutions.test_copy_lists_solution import create_copy_test_class

copy_mod = import_module("06-lists.exercises.copy_lists")

TestCopyExercise = create_copy_test_class(copy_mod)
