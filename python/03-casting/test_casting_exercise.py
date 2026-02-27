from importlib import import_module

from test_casting_solution import create_casting_test_class

exercise = import_module("03-casting.exercise")

TestCastingExercise = create_casting_test_class(exercise.cast)
