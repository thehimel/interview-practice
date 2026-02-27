# Variables

## Problem Statement

Given the list `DATA = ["Apple", 2, 4.2]`:

1. Define global variables `X`, `Y`, and `Z` initialized to `None`.
2. Create a function `get_types()` that unpacks `DATA` and returns the types of the three elements.
3. Create a function `assign_globals()` that assigns the list elements to global variables `X`, `Y`, and `Z` (first element to `X`, second to `Y`, third to `Z`).

**Requirements:**

- `DATA = ["Apple", 2, 4.2]` and `X = Y = Z = None` at module level
- `get_types()` unpacks `DATA` and returns `(type(elem1), type(elem2), type(elem3))`
- `assign_globals()` assigns `DATA[0]` to `X`, `DATA[1]` to `Y`, `DATA[2]` to `Z` using the `global` keyword

## Example

**Input:** `["Apple", 2, 4.2]`

**Output (types):** `(str, int, float)`

**Global variables after assignment:** `X == "Apple"`, `Y == 2`, `Z == 4.2`

## File Structure

- `solution.py` – Reference implementation
- `exercise.py` – Stub for practice
- `test_variables_solution.py` – Test logic and solution tests
- `test_variables_exercise.py` – Exercise tests (uses logic from solution test file)

## Running Tests

```bash
# From project root
pytest python/02_variables/test_variables_solution.py -v   # Run solution tests
pytest python/02_variables/test_variables_exercise.py -v   # Run exercise tests
```

## PyCharm Import Warnings

If PyCharm underlines imports in red, mark this directory as a **Sources Root**:

1. Right-click `python/02_variables` in the Project tool window
2. **Mark Directory as** → **Sources Root**

This adds the directory to the Python path so PyCharm can resolve imports. Restart PyCharm if the warnings persist.

## Resources

- [Python Variables](https://www.w3schools.com/python/python_variables_multiple.asp)
