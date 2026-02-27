# Hello World

## Problem Statement

Write a Python program that prints `Hello, World!` to the console.

**Requirements:**

- Use the `if __name__ == "__main__":` guard so that the print statement runs only when the script is executed directly (not when imported as a module)
- Output exactly: `Hello, World!`

## Example

**Input:** None (no input required)

**Output:**

```
Hello, World!
```

## File Structure

- `solution.py` – Reference implementation
- `exercise.py` – Stub for practice
- `test_hello_world_solution.py` – Test logic and solution tests
- `test_hello_world_exercise.py` – Exercise tests (uses logic from solution test file)

## Running Tests

```bash
# From project root
pytest python/01-hello-world/test_hello_world_solution.py -v   # Run solution tests
pytest python/01-hello-world/test_hello_world_exercise.py -v   # Run exercise tests
```

## PyCharm Import Warnings

If PyCharm underlines imports in red, mark this directory as a **Sources Root**:

1. Right-click `python/01-hello-world` in the Project tool window
2. **Mark Directory as** → **Sources Root**

This adds the directory to the Python path so PyCharm can resolve imports. Restart PyCharm if the warnings persist.

## Resources

- [Python Getting Started](https://www.w3schools.com/python/python_syntax.asp)
