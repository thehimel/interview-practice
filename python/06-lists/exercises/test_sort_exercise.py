"""Test logic for list sort exercises."""

from importlib import import_module

from ..solutions.test_sort_solution import create_sort_test_class

sort = import_module("06-lists.exercises.sort")

TestSortExercise = create_sort_test_class(sort)
