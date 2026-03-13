# For Loops

A `for` loop iterates over an **iterable** — a list, tuple, set, string, dict, or any object that yields items one by one. Unlike C-style `for`, Python's `for` does not use an index variable; it assigns each item directly to the loop variable.

## Basic Syntax

```
for item in iterable:
    body
```

Each iteration assigns the next item to `item` and runs the body. The loop ends when the iterable is exhausted.

## Iterating Over Sequences

**Lists, tuples, sets:** The loop variable receives each element.

```python
items = ["alpha", "beta", "gamma"]
for x in items:
    print(x)
```

**Output:** `alpha`, `beta`, `gamma`

**No index variable:** You do not need to manage an index or call `len()`. Use `enumerate()` when you need the index.

## Iterating Over Strings

Strings are iterables of characters. Each iteration yields one character.

```python
for ch in "loop":
    print(ch)
```

**Output:** `l`, `o`, `o`, `p`

## Iterating Over Dictionaries

Iterating over a dict yields its **keys**. Use `.values()` for values and `.items()` for key-value pairs.

```python
d = {"a": 2, "b": 4, "c": 6}
for k in d:
    print(k)           # a, b, c
for v in d.values():
    print(v)           # 2, 4, 6
for k, v in d.items():
    print(k, v)        # a 2, b 4, c 6
```

## break — Exit the Loop

`break` stops the loop immediately. Control moves to the first statement after the loop.

```python
items = ["alpha", "beta", "gamma"]
for x in items:
    print(x)
    if x == "beta":
        break
```

**Output:** `alpha`, `beta`

**Position matters:** If `break` comes before other statements, those statements are skipped for that iteration and the loop exits:

```python
items = ["alpha", "beta", "gamma"]
for x in items:
    if x == "beta":
        break
    print(x)
```

**Output:** `alpha` — `beta` is never printed because `break` runs first.

## continue — Skip to Next Iteration

`continue` skips the rest of the current iteration and moves to the next item.

```python
items = ["alpha", "beta", "gamma"]
for x in items:
    if x == "beta":
        continue
    print(x)
```

**Output:** `alpha`, `gamma`

## The range() Function

`range()` produces a sequence of integers. Use it when you need to loop a fixed number of times or over numeric indices.

| Form                       | Values produced      | Example                            |
|----------------------------|----------------------|------------------------------------|
| `range(stop)`              | 0 to stop−1          | `range(6)` → 0, 1, 2, 3, 4, 5      |
| `range(start, stop)`       | start to stop−1      | `range(2, 8)` → 2, 3, 4, 5, 6, 7   |
| `range(start, stop, step)` | start, start+step, … | `range(2, 12, 2)` → 2, 4, 6, 8, 10 |

**Exclusive stop:** The stop value is never included. `range(6)` yields 0 through 5, not 6.

```python
for i in range(2, 10, 2):
    print(i)
```

**Output:** `2`, `4`, `6`, `8`

**Memory:** `range` does not build a list; it produces values on demand. `range(10⁶)` uses little memory.

## else Clause

A `for` loop can have an `else` block. It runs only when the loop finishes normally — **not** when the loop exits via `break`.

```python
for i in range(2, 8, 2):
    print(i)
else:
    print("Loop finished")
```

**Output:** `2`, `4`, `6`, `Loop finished`

**When `else` does not run:** If `break` exits the loop, the `else` block is skipped:

```python
for i in range(2, 10, 2):
    if i == 6:
        break
    print(i)
else:
    print("This never runs")
```

**Output:** `2`, `4`

**Use case:** Use `else` for "no break" logic — e.g. "searched the whole sequence and didn't find it."

## Nested Loops

A loop inside another loop runs its full cycle for each iteration of the outer loop.

```python
rows = ["A", "B"]
cols = [2, 4, 6]
for r in rows:
    for c in cols:
        print(r, c)
```

**Output:** `A 2`, `A 4`, `A 6`, `B 2`, `B 4`, `B 6`

**Order:** The inner loop completes all its iterations before the outer loop advances.

## The pass Statement

A `for` block cannot be empty. Use `pass` as a placeholder when you need the structure but no action yet.

```python
for x in [2, 4, 6]:
    pass
```

**When to use:** Placeholder during development; empty loop body; stub for code you will add later.

## for vs while

| Aspect               | `for`                            | `while`                    |
|----------------------|----------------------------------|----------------------------|
| **Iteration source** | Iterable (sequence, range, etc.) | Boolean condition          |
| **Loop variable**    | Provided by the loop             | You define and update it   |
| **Typical use**      | Known sequence or fixed count    | Condition-based repetition |

Use `for` when you iterate over a known iterable. Use `while` when the stopping condition is not tied to a fixed sequence.

## Common Gotchas

### range stop is exclusive

`range(8)` yields 0 through 7, not 8. To include 8, use `range(9)` or `range(0, 9)`.

### Modifying the iterable during iteration

Changing a list while iterating over it can skip items or raise errors. Iterate over a copy: `for x in lst.copy():` or `for x in lst[:]:`.

### else with break

`else` on a `for` loop runs only when the loop completes without `break`. This is the opposite of `if`-`else`; it means "run when no break occurred."

### Dict iteration yields keys

`for x in d` iterates over keys, not values or pairs. Use `d.values()` or `d.items()` for the others.

## Interview Questions

### When does the `else` block of a `for` loop run?

Only when the loop finishes by exhausting the iterable. It does **not** run when the loop exits via `break`.

### What does `range(2, 10, 2)` produce?

The integers 2, 4, 6, 8. Start 2, stop 10 (exclusive), step 2.

### Why is `range` memory-efficient?

`range` does not build a list; it yields values one at a time. `range(10⁶)` uses a small, fixed amount of memory.

### What does iterating over a dict yield?

Keys only. Use `.values()` for values and `.items()` for key-value pairs.

### When to use `for` instead of `while`?

Use `for` when iterating over a known iterable (list, range, string, etc.). Use `while` when the number of iterations depends on a condition.
