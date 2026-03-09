from importlib import import_module

from ..solutions.test_casting_solution import create_casting_test_class

casting = import_module("03-casting.exercises.casting")

TestCastingExercise = create_casting_test_class(casting.cast)
