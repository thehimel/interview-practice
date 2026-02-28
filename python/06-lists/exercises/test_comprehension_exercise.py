"""Test logic for list comprehension exercises."""

from importlib import import_module

from ..solutions.test_comprehension_solution import create_comprehension_test_class

comp_mod = import_module("06-lists.exercises.comprehension")

TestComprehensionExercise = create_comprehension_test_class(comp_mod)
