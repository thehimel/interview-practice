from importlib import import_module
from pathlib import Path

from test_hello_world_solution import create_hello_world_test_class

exercise = import_module("01_hello_world.exercise")
_dir = Path(__file__).resolve().parent

TestHelloWorldExercise = create_hello_world_test_class(
    exercise.hello_world,
    _dir / "exercise.py",
)
