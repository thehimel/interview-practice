# Sets Topics

Sets are unordered, unindexed collections of unique elements. Items cannot be changed after creation, but you can add and remove items.

**Creating a set:** Use curly braces or `set()`. Empty sets must use `set()` — `{}` creates an empty dict.

```python
nums = {2, 4, 6, 8, 10}
built = set([2, 4, 6, 8])     # from list
built = set((2, 4, 6, 8))     # from tuple — note double parentheses
empty = set()                 # use set(); {} creates a dict
```

**Length:** Use `len(s)` to get the number of elements.

**Type:** `type(nums)` → `<class 'set'>`.

## Set Properties

- **Unordered** — elements have no fixed position; iteration order can change between runs.
- **Unindexed** — no `s[i]` or slicing; use loops or membership tests instead.
- **Unique** — duplicate values are dropped; each value appears at most once.
- **Unchangeable items** — elements must be hashable; you cannot mutate an element in place, but you can remove and add new ones.

**Boolean–int equivalence:** `True` and `1` are treated as the same value; so are `False` and `0`. Only one of each pair is kept.

```python
s = {2, 4, True, 1, 6}   # {True, 2, 4, 6} — 1 removed
s = {2, 4, False, 0, 6}  # {False, 2, 4, 6} — 0 removed
```

**Mixed types:** Sets can hold strings, numbers, booleans, tuples, and other hashable types in the same set.

## Set Methods

| Method                               | Shortcut   | Description                                                              |
|--------------------------------------|------------|--------------------------------------------------------------------------|
| `add(x)`                             |            | Add element `x`                                                          |
| `clear()`                            |            | Remove all elements                                                      |
| `copy()`                             |            | Return a shallow copy                                                    |
| `difference(other, ...)`             | `-`        | Elements in this set but not in others                                   |
| `difference_update(...)`             | `-=`       | Remove elements that appear in others                                    |
| `discard(x)`                         |            | Remove `x` if present; no error if missing                               |
| `intersection(other, ...)`           | `&`        | Elements in all sets                                                     |
| `intersection_update(...)`           | `&=`       | Keep only elements in all sets                                           |
| `isdisjoint(other)`                  |            | `True` if no elements in common; takes one other                         |
| `issubset(other)`                    | `<=` / `<` | `True` if every element of this set is in `other`; `<` = proper subset   |
| `issuperset(other)`                  | `>=` / `>` | `True` if every element of `other` is in this set; `>` = proper superset |
| `pop()`                              |            | Remove and return an arbitrary element; raises if empty                  |
| `remove(x)`                          |            | Remove `x`; raises `KeyError` if missing                                 |
| `symmetric_difference(other)`        | `^`        | Elements in exactly one set; takes one other (chain for 3+)              |
| `symmetric_difference_update(other)` | `^=`       | Replace with symmetric difference; takes one other (chain for 3+)        |
| `union(other, ...)`                  | `\|`       | All elements from all sets                                               |
| `update(*iterables)`                 | `\|=`      | Add all elements from one or more iterables                              |

**Operator vs method:** `|`, `&`, `-`, `^` work only between sets. `union()`, `intersection()`, `difference()` accept multiple iterables; `symmetric_difference()` takes one other (chain for 3+).

## Access Set Items

No indexing. Use a **loop** or **membership** tests.

```python
nums = {2, 4, 6, 8, 10}
for x in nums:
    print(x)  # order varies

4 in nums      # True
12 not in nums # True
```

## Add Set Items

**`add(x)`** — add a single element.

```python
nums = {2, 4, 6, 8}
nums.add(10)
print(nums)  # {2, 4, 6, 8, 10}
```

**`update(*iterables)`** — add all elements from one or more iterables (sets, lists, tuples, dicts — dict adds keys). Modifies in place; does not return a new set. Duplicates are excluded.

```python
nums = {2, 4, 6}
nums.update({8, 10})        # from set
nums.update([12, 14])       # from list
nums.update((16, 18))       # from tuple
nums.update({20, 22}, [24], {26: "x", 28: "y"})  # dict adds keys
print(nums)  # {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28}
```

## Remove Set Items

| Method       | Behavior                                                          |
|--------------|-------------------------------------------------------------------|
| `remove(x)`  | Remove `x`; raises `KeyError` if `x` not in set                   |
| `discard(x)` | Remove `x` if present; no error if missing                        |
| `pop()`      | Remove and return an arbitrary element; raises if empty           |
| `clear()`    | Remove all elements; leaves an empty set                          |
| `del s`      | Delete the variable; name is undefined; access raises `NameError` |

```python
nums = {2, 4, 6, 8, 10}
nums.remove(6)   # {2, 4, 8, 10}; KeyError if 6 not present
nums.discard(8)  # {2, 4, 10}; no error if 8 not present

x = nums.pop()   # removes one element; which one is undefined
nums.clear()     # set()
```

**`pop()` and order:** Sets are unordered; you cannot predict which element `pop()` removes.

## Loop Sets

Iterate directly over elements. Order is not guaranteed.

```python
nums = {2, 4, 6, 8}
for x in nums:
    print(x)  # 2, 4, 6, 8 — order may vary
```

## Sort Sets

Sets have no `sort()` method. **Why:** Sets are unordered; they have no index or position. There is no "first" or "last" element to define a sort order.

To get sorted output, convert to a list or tuple and sort:

```python
nums = {10, 4, 8, 2, 6}
sorted(nums)           # [2, 4, 6, 8, 10] — returns a list
tuple(sorted(nums))   # (2, 4, 6, 8, 10) — sorted tuple
```

## Reverse Sets

Sets have no `reverse()` method. **Why:** Reversing implies a fixed order (first → last). Sets are unordered, so there is nothing to reverse.

To iterate in descending order, sort first to impose an order, then reverse:

```python
nums = {2, 4, 6, 8}
for x in reversed(sorted(nums)):  # 8, 6, 4, 2 — descending; order is deterministic
    print(x)
```

## Join Sets

### Union

All elements from all sets. Use `union()` or `|`. `union()` accepts multiple iterables (including lists, tuples); `|` only works between sets. Duplicates are excluded.

```python
a = {2, 4, 6}
b = {4, 6, 8, 10}
c = {8, 10, 12}
a.union(b)              # {2, 4, 6, 8, 10}
a.union(b, c)            # {2, 4, 6, 8, 10, 12} — 3+ iterables
a.union(b, c, [14, 16])  # iterables can be sets, lists, tuples, etc.
a | b | c                # {2, 4, 6, 8, 10, 12} — operator chains
```

**`update()`** — like `union()` but modifies in place and returns `None`. Accepts multiple iterables.

```python
a = {2, 4, 6}
a.update({8, 10}, [12, 14])
print(a)  # {2, 4, 6, 8, 10, 12, 14}
```

### Intersection

Elements present in all sets. Use `intersection()` or `&`. Both accept multiple iterables.

```python
a = {2, 4, 6, 8}
b = {4, 6, 8, 10}
c = {4, 6, 12}
a.intersection(b)       # {4, 6, 8}
a.intersection(b, c)    # {4, 6} — elements in all three
a & b & c               # {4, 6} — operator chains
```

**Note:** `True`/`1` and `False`/`0` are treated as duplicates in intersection (see Set Properties).

**`intersection_update()`** — keep only elements in all sets; modifies in place. Accepts multiple iterables.

```python
a = {2, 4, 6, 8}
b = {4, 6, 8, 10}
c = {4, 6}
a.intersection_update(b, c)
print(a)  # {4, 6}
```

### Difference

Elements in the first set but not in the others. Use `difference()` or `-`. Both accept multiple iterables.

```python
a = {2, 4, 6, 8, 10}
b = {4, 6}
c = {8, 10}
a.difference(b)       # {2, 8, 10} — remove b's elements
a.difference(b, c)    # {2} — remove elements in b or c
a - b - c             # {2} — operator chains (left-associative)
```

**`difference_update()`** — remove elements that appear in others; modifies in place. Accepts multiple iterables.

```python
a = {2, 4, 6, 8, 10}
b = {4, 6}
c = {8}
a.difference_update(b, c)
print(a)  # {2, 10}
```

### Symmetric Difference

Elements in exactly one set (not in both). Use `symmetric_difference()` or `^`. The method takes one other; for 3+ sets, chain or use the operator.

```python
a = {2, 4, 6}
b = {4, 6, 8}
c = {6, 8, 10}
a.symmetric_difference(b)                    # {2, 8} — one other
a.symmetric_difference(b).symmetric_difference(c)  # chain for 3+
a ^ b ^ c                                    # {2, 6, 10} — operator chains
```

**`symmetric_difference_update()`** — replace set with symmetric difference; modifies in place. Takes one other; chain for 3+.

```python
a = {2, 4, 6, 8}
b = {4, 6, 8, 10}
a.symmetric_difference_update(b)
print(a)  # {2, 10}

a = {2, 4, 6}
a.symmetric_difference_update({4, 6, 8})
a.symmetric_difference_update({6, 8, 10})  # chain for 3+
print(a)  # {2, 6, 10}
```

## Compare Sets

These methods take **one** `other` argument. For 3+ sets, chain with `and` or combine sets first.

**`isdisjoint(other)`** — `True` if no elements in common.

```python
a = {2, 4, 6}
b = {4, 6, 8}
c = {8, 10, 12}
a.isdisjoint(b)   # False — 4, 6 in common
a.isdisjoint(c)   # True — no overlap
# 3+ sets: a.isdisjoint(b | c) or a.isdisjoint(b) and a.isdisjoint(c)
```

**`issubset(other)`** — `True` if every element of this set is in `other`. Use `<=` or `<` (proper subset). No method for proper subset; use `a < b` or `a.issubset(b) and a != b`.

```python
a = {2, 4, 6}
b = {2, 4, 6, 8}
a.issubset(b)   # True
a <= b          # True
a < b           # True — proper subset (a ≠ b); no dedicated method
a < {2, 4, 6}   # False — not proper
# 3+ sets: a <= b and a <= c (subset of all); a <= b | c (subset of union)
```

**`issuperset(other)`** — `True` if every element of `other` is in this set. Use `>=` or `>` (proper superset). No method for proper superset; use `a > b` or `a.issuperset(b) and a != b`.

```python
a = {2, 4, 6, 8}
b = {4, 6}
a.issuperset(b)   # True
a >= b            # True
a > b             # True — proper superset; no dedicated method
# 3+ sets: a >= b and a >= c (superset of all); a >= b | c (contains union of b, c)
```

## Frozenset

**`frozenset`** is an immutable set. Elements cannot be added or removed.

**Creating:** Use `frozenset()` with any iterable.

```python
nums = frozenset({2, 4, 6, 8})
print(type(nums))  # <class 'frozenset'>
```

**Frozenset methods:** Immutable means no add or remove. Frozensets support all non-mutating set operations.

| Method                        | Shortcut   | Description                                              |
|-------------------------------|------------|----------------------------------------------------------|
| `copy()`                      |            | Return a shallow copy                                    |
| `difference(other, ...)`      | `-`        | Return a frozenset with elements not in others           |
| `intersection(other, ...)`    | `&`        | Return a frozenset with elements in all sets             |
| `isdisjoint(other)`           |            | Return `True` if no elements in common                   |
| `issubset(other)`             | `<=` / `<` | Return `True` if every element of this set is in `other` |
| `issuperset(other)`           | `>=` / `>` | Return `True` if every element of `other` is in this set |
| `symmetric_difference(other)` | `^`        | Return a frozenset with elements in exactly one set      |
| `union(other, ...)`           | `\|`       | Return a frozenset with all elements from all sets       |

```python
a = frozenset({2, 4, 6})
b = frozenset({4, 6, 8})
c = frozenset({6, 8, 10})

a.copy()                          # frozenset({2, 4, 6})
a - b                             # frozenset({2}); a.difference(b, c) # frozenset({2})
a & b                             # frozenset({4, 6}); a.intersection(b, c) # frozenset({6})
frozenset({2, 4}).isdisjoint({6, 8})   # True; a.isdisjoint(b) # False
frozenset({2, 4}).issubset({2, 4, 6})  # True; a <= b # False
frozenset({2, 4, 6, 8}).issuperset({4, 6})  # True; a >= b # False
a ^ b                             # frozenset({2, 8}); a.symmetric_difference(b)
a | b                             # frozenset({2, 4, 6, 8}); a.union(b, c) # frozenset({2, 4, 6, 8, 10})
```

**Use case:** Use `frozenset` when you need a hashable set (e.g., as a dict key or set element).

## Interview Questions

### Why can't you use a list as a set element or dict key?

Sets and dicts use hash tables for O(1) lookup. Keys and set elements must be hashable. Lists are mutable and unhashable; use tuples or frozensets instead.

### What is the time complexity of set membership (`in`)?

O(1) average — hash table lookup.

### `remove()` vs `discard()` — when to use each?

`remove(x)` raises `KeyError` if `x` not in set. `discard(x)` does nothing if missing. Use `discard()` when absence is acceptable.

### Why don't sets have `sort()` or `reverse()`?

Sets are unordered; they have no index or position. There is no "first" or "last" element. To get sorted output, use `sorted(s)` or `tuple(sorted(s))`.

### `union()` vs `|` — can you use iterables with both?

`union()` accepts multiple iterables (lists, tuples, etc.). `|` works only between sets. Use `union()` when merging with non‑sets.

### When does shallow vs deep copy matter for sets?

Same as dicts: shallow copy shares nested mutable values. Sets typically hold hashable (immutable) elements, so shallow copy is usually sufficient. Use `copy.deepcopy()` if you have nested mutables.

### `isdisjoint`, `issubset`, `issuperset` — do they accept multiple sets?

No — each takes one `other` argument. For 3+ sets, chain with `and` or combine: `a.isdisjoint(b | c)` or `a <= b and a <= c`.
