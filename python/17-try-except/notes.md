# Try Except

When code raises an error (an **exception**), Python normally stops and prints a traceback. The `try`/`except` construct catches exceptions so the program can handle them and continue.

**Imports:** Built-in exceptions (`ValueError`, `TypeError`, `ZeroDivisionError`, etc.) require no imports. For logging in handlers, use `import logging`.

## Basic Syntax

```python
try:
    risky_code()
except SomeError:
    handle_error()
```

The `try` block runs first. If an exception occurs and matches the `except` clause, that handler runs. If no exception occurs, the handler is skipped.

## try, except, else, finally

| Block     | When it runs                                      |
|-----------|---------------------------------------------------|
| `try`     | Code that might raise an exception                |
| `except`  | When a matching exception is raised               |
| `else`    | When no exception was raised (must follow except) |
| `finally` | Always, whether or not an exception occurred      |

**Order:** `try` → `except`(s) → `else` → `finally`

```python
for divisor in [2, 4, 0, 6]:
    try:
        result = 10 / divisor
    except ZeroDivisionError:
        print("Division by zero")
    else:
        print("No error:", result)
    finally:
        print("Cleanup runs always")
```

**Output:**
```
No error: 5.0
Cleanup runs always
No error: 2.5
Cleanup runs always
Division by zero
Cleanup runs always
No error: 1.666...
Cleanup runs always
```

## Catching Specific Exceptions

Use specific exception types to handle different errors differently. The first matching `except` runs; later ones are ignored.

```python
try:
    vals = [2, 4, 6]
    x = vals[10]
except IndexError:
    print("Index out of range")
except KeyError:
    print("Key not found")
except (TypeError, ValueError):
    print("Type or value error")
```

**Catching multiple in one clause:** Use a tuple: `except (TypeError, ValueError):`.

## Catching the Exception Object

Use `except E as e` to bind the exception instance. Useful for logging or inspecting the error message.

```python
try:
    int("not a number")
except ValueError as e:
    print(type(e).__name__, str(e))
```

**Output:** `ValueError invalid literal for int() with base 10: 'not a number'`

## Bare except — Avoid It

`except:` without a type catches **all** exceptions, including `KeyboardInterrupt` and `SystemExit`. That can hide bugs and make Ctrl+C ineffective.

```python
# Avoid — catches everything
try:
    risky()
except:
    pass

# Prefer — catch Exception (not SystemExit, KeyboardInterrupt)
try:
    risky()
except Exception:
    pass
```

**Best practice:** Catch `Exception` or more specific types. Use `except Exception as e` when the exception message is needed.

## else Block

Runs only when the `try` block completes without raising. Keeps the success path separate from the error path.

```python
try:
    data = fetch_data()
except ConnectionError:
    data = None
else:
    process(data)
```

## finally Block

Runs whether or not an exception occurred. Use for cleanup: closing files, releasing locks, etc.

```python
f = open("data.txt")
try:
    content = f.read()
except OSError:
    print("Read failed")
finally:
    f.close()
```

**Note:** `finally` runs even when `return` or `break` is used in `try` or `except`. It also runs when an exception is re-raised.

## raise — Raising Exceptions

Use `raise` to trigger an exception:

```python
raise ValueError("Invalid value")
raise TypeError("Expected int, got str")
```

**Re-raising:** Use `raise` without arguments inside an `except` block to re-raise the current exception (e.g. after logging or cleanup).

```python
import logging

try:
    risky()
except ValueError as e:
    logging.exception("Caught: %s", e)
    raise
```

## raise from — Exception Chaining

`raise X from e` preserves the original exception as the cause. The traceback shows both.

```python
try:
    int("x")
except ValueError as e:
    raise RuntimeError("Parse failed") from e
```

**Output:** `RuntimeError: Parse failed` with `ValueError: ...` as the cause.

## Custom Exceptions

Subclass `Exception` (or a built-in exception) for domain-specific errors:

```python
class InsufficientFundsError(Exception):
    pass

def withdraw(amount, balance):
    if amount > balance:
        raise InsufficientFundsError(f"Need {amount}, have {balance}")
    return balance - amount
```

**Passing data:** Store extra info in the exception:

```python
class ValidationError(Exception):
    def __init__(self, message, field):
        super().__init__(message)
        self.field = field
```

## Commonly Used Built-in Exceptions

| Exception           | When it occurs           | Example                           | Explanation                                      |
|---------------------|--------------------------|-----------------------------------|--------------------------------------------------|
| `ValueError`        | Invalid value            | `int("x")`, `range(0, 10, 0)`     | `"x"` cannot be parsed as int; step 0 is invalid |
| `TypeError`         | Wrong type               | `"a" + 2`, `len(42)`              | str cannot add int; int has no `len`             |
| `IndexError`        | Index out of range       | `[2, 4, 6][10]`                   | List has 3 elements; index 10 does not exist     |
| `KeyError`          | Key not found in dict    | `{"a": 2}["b"]`                   | Dict has key `"a"` only; `"b"` is missing        |
| `AttributeError`    | Missing attribute/method | `"hi".foo`, `None.split()`        | str has no `foo`; None has no `split`            |
| `NameError`         | Name not defined         | `print(undefined_var)`            | `undefined_var` was never assigned or imported   |
| `ZeroDivisionError` | Division by zero         | `10 / 0`                          | Dividing by 0 is undefined                       |
| `FileNotFoundError` | File not found           | `open("missing.txt")`             | No file named `missing.txt` in current path      |
| `ConnectionError`   | Connection failed        | Socket/network connection failure | Remote host unreachable or connection refused    |
| `ImportError`       | Import fails             | `import nonexistent_module`       | No module named `nonexistent_module` on sys.path |
| `StopIteration`     | Iterator exhausted       | `next(iter([]))`                  | Empty list yields no items; `next()` has nothing |
| `AssertionError`    | `assert` fails           | `assert False`                    | Assertion `False` is falsy, so it fails          |
| `RuntimeError`      | Generic runtime error    | `raise RuntimeError("msg")`       | Explicitly raised with the given message         |
| `RecursionError`    | Recursion limit exceeded | Infinite recursion                | Function keeps calling itself indefinitely       |

## Exception Hierarchy

| Base              | Subclasses                                                                                    |
|-------------------|-----------------------------------------------------------------------------------------------|
| `BaseException`   | Root of all exceptions                                                                        |
| `Exception`       | Most built-in and user exceptions (except `SystemExit`, `KeyboardInterrupt`, `GeneratorExit`) |
| `LookupError`     | `IndexError`, `KeyError`                                                                      |
| `OSError`         | `FileNotFoundError`, `PermissionError`, etc.                                                  |
| `ArithmeticError` | `ZeroDivisionError`, `OverflowError`                                                          |

**Catching a base class:** Catches that class and all subclasses. `except OSError` catches `FileNotFoundError` etc.

## Context Managers

`with` handles setup and cleanup without explicit `try`/`finally`:

```python
with open("data.txt") as f:
    content = f.read()
# File is closed automatically, even if an exception occurs
```

**Equivalent to:**

```python
f = open("data.txt")
try:
    content = f.read()
finally:
    f.close()
```

## assert vs raise

| Use case                                                      | Tool                                  |
|---------------------------------------------------------------|---------------------------------------|
| **Development/debug** — invariants that should never be false | `assert condition, "message"`         |
| **Runtime validation** — user input, external data            | `if not valid: raise ValueError(...)` |

`assert` raises `AssertionError` when the condition is falsy. It can be disabled with `python -O`. Do not use `assert` for input validation; use `raise` instead.

## Common Gotchas

### except order matters

Put more specific exceptions before broader ones. `except ValueError` before `except Exception`; otherwise `except Exception` would catch `ValueError` and the specific handler would never run.

### else vs finally

`else` runs only when no exception occurred. `finally` always runs. Use `else` for success-only logic; use `finally` for cleanup.

### Swallowing exceptions

`except: pass` hides all errors. At minimum, log the exception. Prefer catching specific types.

### Modifying a list while iterating

Iterating and mutating the same list can raise `RuntimeError` or produce unexpected behavior. Iterate over a copy or use a different strategy.

## Interview Questions

### What is the order of try, except, else, finally?

`try` → `except`(s) → `else` → `finally`. The `else` runs when no exception occurred; `finally` always runs.

### Why avoid bare except?

It catches `KeyboardInterrupt`, `SystemExit`, and other system exceptions. Use `except Exception` to catch normal errors while allowing Ctrl+C and system exit to work.

### When does the else block run?

Only when the `try` block completes without raising an exception. It does not run when an exception is caught and handled.

### What is the difference between else and finally?

`else` runs only on success; `finally` runs in all cases (success, handled exception, or unhandled exception before propagation).

### How do you re-raise an exception?

Use `raise` with no arguments inside an `except` block. The original exception is re-raised with its traceback preserved.

### What does raise X from e do?

Raises `X` with `e` as the cause. The traceback shows both exceptions, which helps debugging.

### When to use custom exceptions?

When the built-in types do not express the domain error clearly. Subclass `Exception` and raise it for cases like invalid business rules or validation failures.

### assert vs raise — when to use each?

Use `assert` for internal invariants during development; it can be disabled with `-O`. Use `raise` for runtime validation (user input, external data) because it always runs and gives explicit control over the exception type.
