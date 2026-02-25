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
