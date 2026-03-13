# Range

The built-in `range()` function returns an immutable sequence of integers. It is commonly used to loop a fixed number of times or to produce numeric sequences without building a list in memory.

## What range Returns

`range` is its own type — a sequence that yields integers on demand. It is **immutable**: once created, it cannot be changed. Values are computed when iterated, not stored.

## Creating Ranges

`range()` accepts 1, 2, or 3 arguments:

| Form                       | Parameters        | Defaults        | Example                            |
|----------------------------|-------------------|-----------------|------------------------------------|
| `range(stop)`              | stop              | start=0, step=1 | `range(8)` → 0, 1, 2, …, 7         |
| `range(start, stop)`       | start, stop       | step=1          | `range(2, 10)` → 2, 3, …, 9        |
| `range(start, stop, step)` | start, stop, step | —               | `range(2, 12, 2)` → 2, 4, 6, 8, 10 |

**Exclusive stop:** The stop value is never included. `range(8)` yields 0 through 7, not 8.

### One Argument: `range(stop)`

The single argument is the stop value. Start defaults to 0, step to 1.

```python
list(range(8))
```

**Output:** `[0, 1, 2, 3, 4, 5, 6, 7]`

### Two Arguments: `range(start, stop)`

First is start, second is stop. Step defaults to 1.

```python
list(range(2, 10))
```

**Output:** `[2, 3, 4, 5, 6, 7, 8, 9]`

### Three Arguments: `range(start, stop, step)`

Step is the increment between values. Can be negative for a decreasing sequence.

```python
list(range(2, 12, 2))
list(range(10, 2, -2))
```

**Output:** `[2, 4, 6, 8, 10]`, `[10, 8, 6, 4]`

**Negative step:** When step is negative, start should be greater than stop. Otherwise the range is empty.

```python
list(range(2, 10, -2))  # []
list(range(10, 2, -2))   # [10, 8, 6, 4]
```

## Using range in Loops

`range` is often used in `for` loops when a numeric index or count is needed:

```python
for i in range(2, 10, 2):
    print(i)
```

**Output:** `2`, `4`, `6`, `8`

## Converting to List

A `range` object does not print as a list. Convert with `list()` to see the values:

```python
print(range(6))
print(list(range(6)))
print(list(range(2, 10)))
print(list(range(2, 14, 2)))
```

**Output:** `range(0, 6)`, `[0, 1, 2, 3, 4, 5]`, `[2, 3, 4, 5, 6, 7, 8, 9]`, `[2, 4, 6, 8, 10, 12]`

## Indexing and Slicing

Ranges support indexing and slicing like other sequences. Slicing returns a new `range` object, not a list.

```python
r = range(2, 12, 2)
r[2]      # 6
r[-1]     # 10
r[:3]     # range(2, 8, 2)
list(r[:3])  # [2, 4, 6]
```

## Membership Testing

Use `in` to check whether an integer is in the range. Python computes membership from start, stop, and step without iterating the whole sequence.

```python
r = range(0, 12, 2)
6 in r   # True
7 in r   # False
```

## Length

`len(range(start, stop, step))` returns the number of elements. The formula is based on start, stop, and step; the range does not need to be materialized.

```python
r = range(2, 12, 2)
len(r)   # 5
```

## Memory Efficiency

`range` does not store all values. It computes them on demand during iteration. `range(10⁶)` uses a small, fixed amount of memory regardless of the size.

**When to use:** Prefer `range` over `list(range(...))` when iterating; avoid converting to a list unless the values need to be stored or indexed multiple times.

## Common Gotchas

### Stop is exclusive

`range(8)` ends at 7. To include 8, use `range(9)` or `range(0, 9)`.

### Empty range

`range(10, 2)` with default step 1 is empty — start is already past stop. Same for `range(2, 10, -2)`.

### Zero step

`range(2, 10, 0)` raises `ValueError`. Step cannot be zero.

### Slicing returns range

`r[2:6]` on a range returns a `range` object, not a list. Use `list(r[2:6])` if a list is needed.

## Interview Questions

### Is the stop value in range inclusive or exclusive?

Exclusive. `range(8)` yields 0 through 7, not 8.

### What does range(2, 10, 2) produce?

The integers 2, 4, 6, 8. Start 2, stop 10 (exclusive), step 2.

### Why is range memory-efficient?

It does not store all values. It computes them on demand during iteration, so memory use is constant regardless of the range size.

### Can range have a negative step?

Yes. Use `range(10, 2, -2)` for a decreasing sequence. Start must be greater than stop when step is negative.

### What does slicing a range return?

A new `range` object, not a list. The slice follows the same rules as list slicing.
