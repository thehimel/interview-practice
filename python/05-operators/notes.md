# Operators Topics

Operator categories and concepts to include when building the operators practice module.

## Arithmetic Operators

Apply these to numbers for basic math (add, subtract, multiply, divide, etc.).

| Operator | Name           |
|----------|----------------|
| `+`      | Addition       |
| `-`      | Subtraction    |
| `*`      | Multiplication |
| `/`      | Division       |
| `//`     | Floor division |
| `%`      | Modulus        |
| `**`     | Exponentiation |

## Assignment Operators

Perform a math operation and assign the result back to the variable in one step.

| Operator | Name                   | Example     | Equivalent   | Result |
|----------|------------------------|-------------|--------------|--------|
| `=`      | Assignment             | `z = 12`    | —            | `12`   |
| `+=`     | Addition assignment    | `z += 4`    | `z = z + 4`  | `16`   |
| `-=`     | Subtraction assignment | `z -= 2`    | `z = z - 2`  | `14`   |
| `*=`     | Multiplication assign. | `z *= 2`    | `z = z * 2`  | `28`   |
| `/=`     | Division assignment    | `z /= 4`    | `z = z / 4`  | `7.0`  |
| `%=`     | Modulus assignment     | `z %= 4`    | `z = z % 4`  | `3`    |
| `//=`    | Floor division assign. | `z //= 3`   | `z = z // 3` | `1`    |
| `**=`    | Exponentiation assign. | `z **= 2`   | `z = z ** 2` | `1`    |
| `:=`     | Walrus                 | `(z := 16)` | —            | `16`   |

## Comparison Operators

Evaluate whether two values satisfy a relation (equal, less than, greater than, etc.).

| Operator | Name                     |
|----------|--------------------------|
| `==`     | Equal                    |
| `!=`     | Not equal                |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

## Identity Operators

Check whether two references point to the same object in memory.

| Operator  |
|-----------|
| `is`      |
| `is not`  |

**Why use `is` and `is not`?**

- **`is`** checks **object identity** (same object in memory), not value equality
- **`==`** checks value equality; **`is`** checks object identity
- **`is not`** is the negation of `is`

**Key terms:**

- **Singleton** — A single object that exists only once in memory; all references point to the same instance (e.g. `None`, `True`, `False`).
- **Sentinel** — A unique placeholder object used when `None` is a valid value; you need a distinct "no value provided" marker (e.g. `MISSING = object()`).

**Typical uses:**

1. **`None` checks** — `if x is None` and `if x is not None` are the standard, idiomatic way
2. **Sentinels** — `object()` creates a unique instance; use `is` to detect "no value provided":
   ```python
   MISSING = object()
   def get(key, default=MISSING):
       if default is MISSING:
           return fetch(key)
       return default
   ```
3. **Boolean flags** — `if flag is True` or `if flag is False` when you need the exact boolean, not just truthiness
4. **Singletons** — e.g. small integers may share cached objects:
   ```python
   a = 256
   b = 256
   a is b   # True (same cached object)

   # In separate statements, 257 is above cache range
   x = 257
   y = 257
   x is y   # False (different objects; cache is -5 to 256)
   ```
   Note: `x, y = 257, 257` in one statement is `True` due to constant folding.

**`is` vs `==`:**

| Check          | `is`    | `==`   |
|----------------|---------|--------|
| `[] == []`     | `False` | `True` |
| `None is None` | `True`  | `True` |
| `1 == 1.0`     | `False` | `True` |

`==` can be overridden via `__eq__`; `is` cannot.

**Conventions:**

- Use **`is`** / **`is not`** for `None` and singletons (e.g. sentinels, `True`, `False`)
- Use **`==`** / **`!=`** for comparing values (numbers, strings, collections, custom objects)

**Example:**

```python
# is / is not — for None and singletons
if result is None:
    print("no result")
if value is not None:
    print(value)

# == / != — for values
if count == 0:
    print("empty")
if name == "admin":
    print("admin")
if items != []:
    print(items)
```

## Logical Operators

Chain or negate boolean conditions.

| Operator |
|----------|
| `and`    |
| `or`     |
| `not`    |

## Membership Operators

Check whether an element or substring exists in a string, list, tuple, or dict keys.

| Operator  |
|-----------|
| `in`      |
| `not in`  |
