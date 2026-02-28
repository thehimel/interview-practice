"""Test logic for list loop exercises."""

from importlib import import_module

from ..solutions.test_loop_solution import create_loop_test_class

loop_mod = import_module("06-lists.exercises.loop")

TestLoopExercise = create_loop_test_class(loop_mod)
