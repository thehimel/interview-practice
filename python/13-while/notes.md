# While Loops

A `while` loop runs a block of code repeatedly while a condition is truthy. Python also has `for` loops; use `while` when the number of iterations depends on a condition rather than a known iterable.

## Basic Syntax

```
while condition:
    body
```

The condition is evaluated before each iteration. If it is truthy, the body runs; then the condition is checked again. The loop stops when the condition becomes falsy.

## Simple Example

```python
i = 2
while i < 8:
    print(i)
    i += 2
```

**Output:** `2`, `4`, `6`

**Important:** You must update the loop variable inside the body. If the condition never becomes falsy, the loop runs forever (infinite loop).

## Loop Variable Setup

The condition uses variables that must exist before the loop. Initialize them so the first evaluation is valid.

```python
count = 0
total = 0
while count < 4:
    total += count * 2
    count += 1
print(total)  # 0 + 2 + 4 + 6 = 12
```

## break — Exit the Loop

`break` stops the loop immediately, even if the condition is still truthy. Control moves to the first statement after the loop.

```python
i = 2
while i < 10:
    print(i)
    if i == 6:
        break
    i += 2
```

**Output:** `2`, `4`, `6`

**Use case:** Exit early when a target is found or a special case is hit.

## continue — Skip to Next Iteration

`continue` skips the rest of the current iteration and jumps back to the condition check. The loop variable must be updated before `continue`, or the loop may never progress.

```python
i = 0
while i < 8:
    i += 2
    if i == 4:
        continue
    print(i)
```

**Output:** `2`, `6`, `8`

Here, `i` is incremented first. When `i == 4`, `continue` skips `print(i)`, so 4 is not printed.

**Gotcha:** If the increment is after `continue`, it is skipped and the loop can become infinite:

```python
# Infinite loop — i stays 4 forever
i = 0
while i < 8:
    if i == 4:
        continue
    print(i)
    i += 2
```

## else Clause

A `while` loop can have an `else` block. It runs only when the loop ends because the condition became falsy — **not** when the loop exits via `break`.

```python
i = 2
while i < 6:
    print(i)
    i += 2
else:
    print("Loop finished normally")
```

**Output:** `2`, `4`, `Loop finished normally`

**When `else` does not run:** If `break` exits the loop, the `else` block is skipped:

```python
i = 2
while i < 8:
    print(i)
    if i == 4:
        break
    i += 2
else:
    print("This never runs")
```

**Output:** `2`, `4`

**Use case:** Use `else` for "no break" logic — e.g. "searched the whole list and didn't find it."

## while vs for

| Aspect              | `while`                         | `for`                          |
|---------------------|---------------------------------|--------------------------------|
| **Iteration count** | Unknown; depends on condition   | Known or bounded by iterable   |
| **Index variable**  | You manage it                   | Loop variable provided         |
| **Typical use**     | User input, search, event loops | Iterate over sequences, ranges |

Use `for` when you iterate over a sequence or a known range. Use `while` when the stopping condition is not tied to a fixed iterable.

## Common Gotchas

### Infinite loop

Forgetting to update the loop variable (or updating it incorrectly) can make the condition always truthy:

```python
i = 2
while i < 8:
    print(i)
    # Missing: i += 2 — infinite loop
```

### Off-by-one

Ensure the condition and update match your intent. `i < 8` with `i += 2` yields 2, 4, 6. To include 8, use `i <= 8` or `i < 10`.

### continue and increment order

If you use `continue`, place any updates to the loop variable **before** `continue`, or that iteration will not update it.

### else with break

`else` on a `while` runs only when the loop exits normally. If you `break`, `else` is skipped. This is the opposite of `if`-`else`; it means "run when no break occurred."

## Interview Questions

### When does the `else` block of a `while` loop run?

Only when the loop exits because the condition became falsy. It does **not** run when the loop exits via `break`.

### What happens if you forget to update the loop variable in a `while`?

The condition may stay truthy forever, causing an infinite loop. The program will not terminate until interrupted.

### How does `continue` differ from `break`?

`continue` skips the rest of the current iteration and goes back to the condition. `break` exits the loop entirely and continues execution after the loop.

### Why put the increment before `continue`?

If the increment is after `continue`, it is skipped when `continue` runs. The loop variable never changes, which can cause an infinite loop.

### When to use `while` instead of `for`?

Use `while` when the number of iterations depends on a condition (user input, search until found, event loop). Use `for` when iterating over a known sequence or range.
