from importlib import import_module

from test_variables_solution import create_variables_test_class

exercise = import_module("02-variables.exercise")

TestVariablesExercise = create_variables_test_class(exercise)
