# None

`None` is a built-in constant that represents the absence of a value. It has its own type, `NoneType`, and there is only one `None` instance in the entire program — all references point to the same object.

## Type and Identity

```python
x = None
print(type(x))
print(x is None)
```

**Output:** `<class 'NoneType'>`, `True`

**Singleton:** `None` is a singleton. `id(None)` is the same everywhere. There is no way to create another `NoneType` instance.

## Comparing to None

Use `is` and `is not`, not `==` and `!=`. `is` checks object identity; since there is only one `None`, identity is the correct test. Style guides (e.g. PEP 8) recommend `is None` over `== None`.

```python
result = None
if result is None:
    print("No result yet")
else:
    print("Result is ready")

if result is not None:
    print("Result is ready")
else:
    print("No result yet")
```

**Output:** `No result yet`, `No result yet`

**Why `is`?** `x == None` works but can be overridden by `__eq__`. `x is None` cannot be overridden and is clearer. Use `is` for `None` checks.

## Truthiness

`None` is falsy. In a boolean context it evaluates to `False`.

```python
bool(None)
if None:
    print("truthy")
else:
    print("falsy")
```

**Output:** `False`, `falsy`

**Falsy values:** `None`, `False`, `0`, `0.0`, `""`, `[]`, `{}`, `()`, `set()`.

## Functions Returning None

A function without a `return` statement, or with `return` and no value, returns `None`.

```python
def do_something():
    x = 4

result = do_something()
print(result)
print(result is None)
```

**Output:** `None`, `True`

**Explicit return:** `return None` is valid but redundant. Use `return` alone when you want to exit early without a value.

## None as Default Parameter

`None` is commonly used as a default for optional parameters. Use it when the default is "no value" and you need to distinguish from falsy values like `0` or `[]`.

```python
def fetch(count=None):
    if count is None:
        count = 10
    return count

fetch()
fetch(4)
```

**Output:** `10`, `4`

**Mutable default gotcha:** Do not use `def f(x=None): x = x or []` if you need to accept `[]` as a valid argument. Use `if x is None: x = []` instead.

## None vs Other Falsy Values

`None` is not the same as `False`, `0`, or `""`. They are all falsy but represent different concepts.

| Value   | Type     | Use case                    |
|---------|----------|-----------------------------|
| `None`  | NoneType | Absence of value            |
| `False` | bool     | Boolean false               |
| `0`     | int      | Numeric zero                |
| `""`    | str      | Empty string                |
| `[]`    | list     | Empty list                  |

```python
x = None
x == False
x == 0
x is None
```

**Output:** `False`, `False`, `True`

## None in JSON

JSON has `null`, which maps to Python `None`. Round-trip preserves it.

```python
import json
data = {"a": 2, "b": None}
s = json.dumps(data)
loaded = json.loads(s)
print(loaded["b"] is None)
```

**Output:** `True`

## Optional Chaining Pattern

Use `or` to provide a fallback when a value might be `None`:

```python
name = None
display = name or "Guest"
print(display)
```

**Output:** `Guest`

**Caution:** `x or y` returns `y` when `x` is any falsy value (`None`, `0`, `""`, `[]`), not only `None`. Use `x if x is not None else y` when you need to preserve falsy-but-valid values like `0` or `""`.

## Common Gotchas

### None is not False

`None == False` is `False`. Use `is None` for `None` checks.

### Default argument with None

```python
def append_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

Using `lst=[]` as default would reuse the same list across calls. Use `None` and create a new list inside the function.

### Returning None implicitly

A function that reaches the end without `return` returns `None`. If callers expect a value, they may get `None` and fail later (e.g. `AttributeError` when calling a method on it).

## Interview Questions

### What is the type of None?

`NoneType`. `None` is the only instance of that type.

### Why use `is None` instead of `== None`?

`is` checks object identity. There is only one `None`, so identity is correct. `==` can be overridden; `is` cannot. PEP 8 recommends `is None`.

### Is None truthy or falsy?

Falsy. `bool(None)` is `False`.

### What does a function return if it has no return statement?

`None`.

### When to use None as a default parameter?

When the default means "no value" and you need to tell it apart from falsy values like `0`, `""`, or `[]`. Also to avoid mutable default gotchas: use `def f(x=None):` and set `x = []` inside when `x is None`.
