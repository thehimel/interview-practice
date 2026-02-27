from importlib import import_module
from pathlib import Path

from ..solutions.test_hello_world_solution import create_hello_world_test_class

hello_world_module = import_module("01-hello-world.exercises.hello_world")
_dir = Path(__file__).resolve().parent

TestHelloWorldExercise = create_hello_world_test_class(
    hello_world_module.hello_world,
    _dir / "hello_world.py",
)
