# If-Else

Conditional execution in Python uses `if`, `elif`, and `else`. Conditions are boolean expressions; the block runs when the condition is truthy.

## Comparison Operators

Use these in conditions to compare values:

| Operator | Meaning               |
|----------|-----------------------|
| `==`     | Equal                 |
| `!=`     | Not equal             |
| `<`      | Less than             |
| `<=`     | Less than or equal    |
| `>`      | Greater than          |
| `>=`     | Greater than or equal |

## if, elif, else

**`if`** — run a block when the condition is truthy.

**`elif`** — check another condition if the previous ones were falsy. You can have multiple `elif` branches.

**`else`** — run when all preceding `if` and `elif` conditions are falsy. Must come last; no `elif` after `else`.

```python
a = 20
b = 6
if b > a:
    print("b is greater")
elif a == b:
    print("equal")
else:
    print("a is greater")
```

**Order:** `if` → zero or more `elif` → at most one `else`.

## Truthiness

Python treats many types as **truthy** or **falsy** in conditions. Falsy values: `0`, `0.0`, `""`, `None`, `[]`, `{}`, `()`, `set()`, `False`. Everything else is truthy.

```python
if 0:           # falsy — block skipped
    pass
if 4:           # truthy — block runs
    pass
if "":          # falsy
    pass
if "hi":        # truthy — non-empty string
    pass
if []:          # falsy
    pass
if [2, 4]:      # truthy — non-empty list
    pass
```

**Note:** The string `"False"` is truthy (non-empty). Only the boolean `False` is falsy.

## if-else (No elif)

You can use `if` and `else` without `elif`:

```python
a = 20
b = 6
if b > a:
    print("b is greater")
else:
    print("b is not greater")
```

## Example: Even or Odd

```python
n = 8
if n % 2 == 0:
    print("even")
else:
    print("odd")
```

## Example: Multi-Branch

```python
temp = 22
if temp > 30:
    print("hot")
elif temp > 20:
    print("warm")
elif temp > 10:
    print("cool")
else:
    print("cold")
```

## Logical Operators in Conditions

Combine conditions with `and`, `or`, `not`. Precedence: `not` → `and` → `or`. Use parentheses to clarify.

| Operator | Meaning                        |
|----------|--------------------------------|
| `and`    | Both conditions must be truthy |
| `or`     | At least one must be truthy    |
| `not`    | Negates the result             |

```python
a, b, c = 20, 6, 50
if b < a and a < c:
    print("both true")

# Equivalent with chained comparison
if b < a < c:
    print("both true")

if a > b or a > c:
    print("at least one true")

if not a > b:
    print("a is not greater than b")
```

**Truth tables:**

| Condition 1 | Condition 2 | `and` result |
|-------------|-------------|--------------|
| True        | True        | True         |
| True        | False       | False        |
| False       | True        | False        |
| False       | False       | False        |

| Condition 1 | Condition 2 | `or` result  |
|-------------|-------------|--------------|
| True        | True        | True         |
| True        | False       | True         |
| False       | True        | True         |
| False       | False       | False        |

**Python vs other languages:** Python uses keywords, not symbols. There is no `&&`, `||`, or `!`:

| Python | C/Java/JS equivalent | Notes                          |
|--------|------------------------|--------------------------------|
| `and`  | `&&`                  | Logical AND                    |
| `or`   | `\|\|`                 | Logical OR                     |
| `not`  | `!`                    | Logical negation               |

**Invalid in Python:** `&&`, `||`, and `!` cause syntax errors. Use `and`, `or`, and `not`:

```python
# SyntaxError - use 'and' instead
# if a > b && c > a:

# SyntaxError - use 'or' instead
# if a > b || a > c:

# SyntaxError - use 'not' instead
# if !(a > b):
```

## Combining Multiple Operators

Use parentheses to control evaluation order:

```python
age = 24
is_student = False
has_code = True

if (age < 18 or age > 64) and not is_student or has_code:
    print("discount applies")
```

## Shorthand if (One-Line)

For a single statement, you can put it on the same line as the condition. The colon is required.

```python
a = 6
b = 2
if a > b: print("a is greater")
```

## Conditional Expression (Ternary)

Use `value_if_true if condition else value_if_false` for a one-line choice. Returns a value; use for assignments or returns.

```python
a = 10
b = 20
bigger = a if a > b else b
print(bigger)  # 20
```

**Pattern:** `x = val_true if cond else val_false`

**Chained ternary:** Possible but avoid for readability.

```python
a, b = 20, 20
result = "A" if a > b else "=" if a == b else "B"
```

**Default value:** Use for fallback when a value might be falsy.

```python
name = ""
display = name if name else "Guest"
print(display)  # Guest
```

## When to Use Shorthand

Use shorthand when the condition and actions are simple. Prefer full `if`-`else` for multi-line blocks or complex logic.

## Nested if

Place `if` blocks inside other `if` blocks. Avoid deep nesting; use `and` when conditions are independent.

```python
x = 42
if x > 10:
    print("above 10")
    if x > 20:
        print("and above 20")
    else:
        print("but not above 20")
```

**Nested vs `and`:** These are equivalent when conditions are independent:

```python
temp = 24
is_sunny = True

# Nested
if temp > 20:
    if is_sunny:
        print("beach weather")

# With and
if temp > 20 and is_sunny:
    print("beach weather")
```

## The pass Statement

`if` blocks cannot be empty. Use `pass` as a placeholder when no action is needed.

```python
a = 6
b = 20
if b > a:
    pass
```

**When to use `pass`:** Placeholder during development; syntactically required but no action; empty functions or classes you will implement later.

## Interview Questions

### What values are falsy in Python?

`0`, `0.0`, `""`, `None`, `[]`, `{}`, `()`, `set()`, `False`. Everything else is truthy.

### What is the order of evaluation for `and`, `or`, `not`?

`not` first, then `and`, then `or`. Use parentheses to clarify.

### When to use a conditional expression vs full if-else?

Use conditional expression for simple one-line assignments or returns. Use full `if`-`else` for multi-line blocks or complex logic.

### Can you have `elif` after `else`?

No. `else` must come last. The order is `if` → `elif`(s) → `else`.

### Why use `pass` in an if block?

Python requires a non-empty block. `pass` is a no-op placeholder when you need the structure but no action yet.

### Nested if vs `and` — when to use each?

Use `and` when conditions are independent and you want a flat structure. Use nested `if` when the inner check depends on the outer (e.g. checking a key exists before accessing a nested value).
