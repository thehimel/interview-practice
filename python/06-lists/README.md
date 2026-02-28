# Lists

Practice Python lists: access, add, change, comprehension, copy, loop, remove, and sort.

## How to Use

1. **Read [notes.md](./notes.md)** — Understand the concepts and conventions for each list topic.
2. **Practice** — Implement the exercises in [exercises](exercises). Reference implementations are in [solutions](solutions).

## File Structure

- `solutions/` – Reference implementations: `access.py`, `add.py`, `change.py`, `comprehension.py`, `copy_lists.py`, `loop.py`, `remove.py`, `sort.py`
- `exercises/` – Stub implementations in the same structure for practice
- `solutions/test_*_solution.py` – Per-topic test logic and solution tests
- `exercises/test_*_exercise.py` – Per-topic exercise tests (use logic from solution test files)

## Exercises

| Exercise        | Key Functions                                                       | Description                                              |
|-----------------|---------------------------------------------------------------------|----------------------------------------------------------|
| **Access**      | `first_last_and_at_2`, `split_at_4`, `slices_2_to_6_and_negative`, `nums_reversed_*`, `count_six_and_find_eight` | Indexing, slicing, reversing, count, index              |
| **Add**         | `add_items`, `concat_with_plus`, `concat_with_extend`               | append, insert, extend, `+` vs extend                     |
| **Change**      | `change_items`                                                      | Index assignment, slice replace, insert                   |
| **Comprehension** | `double_elements`, `evens_from_range`, `square_elements`           | List comprehension with expr, filter, iterable            |
| **Copy**        | `copy_with_copy`, `copy_with_list`, `copy_with_slice`, `copy_with_deepcopy`, `shallow_*`, `deep_*` | Shallow copy, deep copy, nested vs first-level behavior   |
| **Loop**        | `collect_direct`, `collect_by_index`, `collect_while_step`, `collect_reversed`, `collect_reversed_slice`, `collect_reversed_by_index` | Direct iteration, index-based, while with step, loop in reverse |
| **Remove**      | `remove_items`, `remove_all_occurrences`, `remove_all_occurrences_in_place` | remove, pop, del, clear, remove all occurrences           |
| **Sort**        | `sort_ascending`, `sort_descending`, `reverse_items`, `reversed_new_list`, `sort_by_*` | sort, reverse, reversed, key parameter                   |

## Running Tests

```bash
# From project root
pytest python/06-lists/solutions/ -v   # Run solution tests
pytest python/06-lists/exercises/ -v   # Run exercise tests
```

## PyCharm Import Warnings

If PyCharm underlines imports in red, mark this directory as a **Sources Root**:

1. Right-click `python/06-lists` in the Project tool window
2. **Mark Directory as** → **Sources Root**

This adds the directory to the Python path so PyCharm can resolve imports. Restart PyCharm if the warnings persist.

## Resources

- [notes.md](./notes.md) — List topics, methods, and examples
- [Python Lists](https://www.w3schools.com/python/python_lists.asp)
