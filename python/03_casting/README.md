# Casting

## Problem Statement

Python uses constructor functions to convert between types. Given `DATA = ["222", 82.6, 66]` (a string, a float, and an int), create `cast()` that returns a tuple of the three elements cast to their natural types: first as int, second as float, third as string.

**Requirements:**

- `DATA = ["222", 82.6, 66]` at module level
- `cast()` returns `(int(DATA[0]), float(DATA[1]), str(DATA[2]))`

## Example

**Input:** `["222", 82.6, 66]`

**Output:** `(222, 82.6, "66")`

## File Structure

- `solution.py` – Reference implementation
- `exercise.py` – Stub for practice
- `test_casting_solution.py` – Test logic and solution tests
- `test_casting_exercise.py` – Exercise tests (uses logic from solution test file)

## Running Tests

```bash
# From project root
pytest python/03_casting/test_casting_solution.py -v   # Run solution tests
pytest python/03_casting/test_casting_exercise.py -v   # Run exercise tests
```

## PyCharm Import Warnings

If PyCharm underlines imports in red, mark this directory as a **Sources Root**:

1. Right-click `python/03_casting` in the Project tool window
2. **Mark Directory as** → **Sources Root**

This adds the directory to the Python path so PyCharm can resolve imports. Restart PyCharm if the warnings persist.

## Resources

- [Python Casting](https://www.w3schools.com/python/python_casting.asp)
