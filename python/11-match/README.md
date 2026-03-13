# Match Statement

The `match` statement runs different code blocks based on the value of an expression. It replaces long `if`-`elif`-`else` chains when you compare a single value against many options. Requires **Python 3.10+**.

## Basic Syntax

```python
match expression:
    case x:
        code block
    case y:
        code block
    case z:
        code block
```

**Flow:**
1. The expression is evaluated once.
2. Its value is compared with each `case` in order.
3. The first matching `case` runs; then the `match` ends.
4. No fall-through — only one block executes.

## Simple Example

```python
day = 4
match day:
    case 2:
        print("Monday")
    case 4:
        print("Wednesday")
    case 6:
        print("Friday")
    case 8:
        print("Sunday")
```

**Output:** `Wednesday`

## Default Case with `_`

Use `_` as the last `case` to handle any value that did not match earlier cases. It behaves like `default` in other languages.

```python
day = 10
match day:
    case 6:
        print("Today is Saturday")
    case 8:
        print("Today is Sunday")
    case _:
        print("Looking forward to the weekend")
```

**Output:** `Looking forward to the weekend`

**Order matters:** `_` matches everything. Put it last so earlier cases can match first. If `_` is first, no later case will run.

```python
# Wrong — _ matches first, so 4 never matches
match 4:
    case _:
        print("default")
    case 4:
        print("four")  # never runs
```

## Combining Values with `|`

Use `|` to match any of several values in one `case`. Acts like logical OR.

```python
day = 4
match day:
    case 2 | 4 | 6 | 8 | 10:
        print("Weekday")
    case 12 | 14:
        print("Weekend")
```

**Output:** `Weekday`

**Note:** `|` in `case` is pattern syntax, not the bitwise `|` operator. It only works inside `case` patterns.

## Guards: `if` in `case`

Add an `if` after the pattern to require an extra condition. The pattern must match **and** the guard must be truthy.

```python
month = 6
day = 4
match day:
    case 2 | 4 | 6 | 8 if month == 4:
        print("Weekday in April")
    case 2 | 4 | 6 | 8 if month == 6:
        print("Weekday in June")
    case _:
        print("No match")
```

**Output:** `Weekday in June`

**Guard syntax:** The `if` comes after the pattern (and after `|` if present). The guard is evaluated only when the pattern matches.

```python
x = 4
match x:
    case 2 | 4 if x > 2:
        print("matched")  # 4 matches and 4 > 2
    case _:
        print("default")
```

## match vs if-elif-else

| Aspect           | `match` / `case`              | `if` / `elif` / `else`        |
|------------------|-------------------------------|-------------------------------|
| **Use case**     | One value, many options       | Arbitrary conditions          |
| **Fall-through** | No                            | N/A                           |
| **Default**      | `case _:`                     | `else:`                       |
| **OR**           | `case 2 \| 4 \| 6:`           | `if x in (2, 4, 6):` or `or`  |
| **Extra checks** | Guard: `case x if cond:`      | `if x and cond:`              |

Use `match` when you branch on a single expression. Use `if`-`elif` when conditions are unrelated or complex.

## Common Gotchas

### `_` is a wildcard, not a variable

In `case _:`, the underscore does not capture the value. It just means "match anything." To capture, use a variable name:

```python
match 4:
    case _:
        print("matched")  # _ doesn't store 4
```

### Case order

Cases are checked top to bottom. Put more specific cases before broader ones. Put `case _:` last.

### No fall-through

Unlike C-style `switch`, only one `case` runs. No `break` needed.

### Empty case

A `case` with no body is invalid. Use `pass` if you need a no-op:

```python
match 4:
    case 2:
        pass
    case 4:
        print("four")
```

## Interview Questions

### What Python version is required for `match`?

Python 3.10 or later. Earlier versions raise a syntax error.

### What does `case _:` do?

It matches any value and acts as the default. It must be last; otherwise it catches everything and later cases never run.

### How do you match multiple values in one case?

Use `|`: `case 2 | 4 | 6:` matches 2, 4, or 6.

### What is a guard in `match`?

An `if` condition after the pattern. The case runs only when the pattern matches **and** the guard is truthy. Example: `case 4 if x > 0:`.

### When to use `match` instead of `if`-`elif`-`else`?

Use `match` when branching on a single expression against many literal or simple values. Use `if`-`elif` when conditions are complex, unrelated, or involve multiple variables.

### Does `match` have fall-through like C `switch`?

No. Only the first matching `case` runs. No `break` is needed.
