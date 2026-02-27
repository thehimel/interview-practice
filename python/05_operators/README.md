# Operators

Practice Python operators: arithmetic, assignment, comparison, identity, logical, and membership.

## How to Use

1. **Read [notes.md](./notes.md)** — Understand the concepts and conventions for each operator type.
2. **Practice** — Implement the exercises in [exercises](exercises). Reference implementations are in [solutions](solutions).

## File Structure

- `solutions/` – Reference implementations: `arithmetic.py`, `assignment.py`, `comparison.py`, `identity.py`, `logical_membership.py`
- `exercises/` – Stub implementations in the same structure for practice
- `solutions/test_*_solution.py` – Per-topic test logic and solution tests
- `exercises/test_*_exercise.py` – Per-topic exercise tests (use logic from solution test files)

## Exercises

| Exercise                 | Function                                            | Description                                                      |
|--------------------------|-----------------------------------------------------|------------------------------------------------------------------|
| **Arithmetic**           | `arithmetic(x, y, op)`                              | Apply `+`, `-`, `*`, `/`, `%`, `**`, `//` to numbers             |
| **Assignment**           | `assignment(x, n, op)`, `walrus(value)`             | Walrus `:=` and compound assignment (`+=`, `-=`, etc.)           |
| **Comparison**           | `comparison(x, y, op)`                              | Apply `==`, `!=`, `>`, `<`, `>=`, `<=` and return result strings |
| **Identity**             | `identity_check(x, op)`, `equality_check(x, y, op)` | `is`/`is not` for None and True; `==`/`!=` for values            |
| **Logical & Membership** | `check(nums, x, y)`                                 | Combine `in`, `not in`, `and`, `or`, `is None` with conditionals |

## Running Tests

```bash
# From project root
pytest python/05_operators/solutions/ -v   # Run solution tests
pytest python/05_operators/exercises/ -v   # Run exercise tests
```

## PyCharm Import Warnings

If PyCharm underlines imports in red, mark this directory as a **Sources Root**:

1. Right-click `python/05_operators` in the Project tool window
2. **Mark Directory as** → **Sources Root**

This adds the directory to the Python path so PyCharm can resolve imports. Restart PyCharm if the warnings persist.

## Resources

- [notes.md](./notes.md) — Operator categories, conventions, and examples
- [Python Operators](https://www.w3schools.com/python/python_operators.asp)
