from importlib import import_module

from ..solutions.test_variables_solution import create_variables_test_class

variables = import_module("02-variables.exercises.variables")

TestVariablesExercise = create_variables_test_class(variables)
