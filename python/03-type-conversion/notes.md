# Casting

Type conversion (casting) transforms a value from one type to another. Python provides constructor functions such as `int()`, `float()`, and `str()` for explicit conversion. Understanding conversion rules and edge cases avoids subtle bugs.

## Constructor Functions

| Function   | Converts to | Typical input types        |
|------------|-------------|----------------------------|
| `int(x)`   | Integer     | str, float, bool           |
| `float(x)` | Float       | str, int, bool             |
| `str(x)`   | String      | Any type                   |

## int() Conversion

**From string:** Parses a string as an integer. Leading and trailing whitespace is ignored. The string must represent a valid integer literal.

```python
int("222")    # 222
int("  42  ") # 42
int("-8")     # -8
```

**From float:** Truncates toward zero. The fractional part is discarded.

```python
int(82.6)   # 82
int(82.2)   # 82
int(-4.8)   # -4
```

**From bool:** `True` → 1, `False` → 0.

```python
int(True)   # 1
int(False)  # 0
```

**Base parameter:** `int(s, base)` parses a string in the given base (2–36).

```python
int("10", 2)   # 2 (binary)
int("24", 8)   # 20 (octal)
int("2A", 16)  # 42 (hexadecimal)
```

**Invalid input:** Non-numeric strings raise `ValueError`.

```python
# int("abc")   # ValueError
# int("42.6")  # ValueError — use float() first
```

**Float then int:** To convert a numeric string with a decimal point, use `float()` first, then `int()`.

```python
int(float("82.6"))  # 82
```

## float() Conversion

**From string:** Parses a string as a floating-point number. Accepts integers and decimals.

```python
float("82.6")   # 82.6
float("42")     # 42.0
float("-2.4")   # -2.4
float("  6.8 ") # 6.8
```

**From int:** Produces a float with a decimal part of zero.

```python
float(66)   # 66.0
float(-4)   # -4.0
```

**From bool:** `True` → 1.0, `False` → 0.0.

```python
float(True)   # 1.0
float(False)  # 0.0
```

**Special strings:** `"inf"`, `"-inf"`, `"nan"` produce special float values.

```python
float("inf")   # inf
float("nan")   # nan
```

**Invalid input:** Non-numeric strings raise `ValueError`.

```python
# float("abc")  # ValueError
```

## str() Conversion

**From any type:** Produces a string representation of the value. Every built-in type supports this.

```python
str(66)      # "66"
str(82.6)    # "82.6"
str(True)    # "True"
str([2, 4])  # "[2, 4]"
str(None)    # "None"
```

**Numeric precision:** `str()` uses a default representation. For controlled formatting (e.g. fixed decimal places), use f-strings or `format()`.

```python
str(2.468)       # "2.468"
f"{2.468:.2f}"   # "2.47"
```

## Common Casting Patterns

**String → int:** `int("222")` → 222.

**Float → int:** `int(82.6)` → 82 (truncation).

**Int → float:** `float(66)` → 66.0.

**Any → string:** `str(x)` for any `x`.

**Exercise pattern:** Given `DATA = ["222", 82.6, 66]`, cast each element to its natural type:

```python
DATA = ["222", 82.6, 66]

def cast():
    return (int(DATA[0]), float(DATA[1]), str(DATA[2]))
# (222, 82.6, "66")
```

## Implicit vs Explicit Conversion

**Explicit:** Using `int()`, `float()`, `str()` — clear and controlled.

**Implicit:** Python converts automatically in some contexts (e.g. `2 + 4.0` → 6.0). Relying on implicit conversion can obscure intent; explicit casting is often clearer.

## Edge Cases and Gotchas

### Float precision

Floats use binary representation; some decimals cannot be stored exactly. `0.1 + 0.2` may not equal `0.3` exactly. For financial or exact decimal math, consider `decimal.Decimal`.

### Truncation vs rounding

`int(8.6)` truncates to 8; it does not round. Use `round(8.6)` for rounding, then `int()` if needed.

### Empty string

`int("")` and `float("")` raise `ValueError`. Check for empty strings before converting if input may be empty.

### str() and repr()

`str(x)` aims for readability; `repr(x)` aims for an unambiguous representation. For many types they differ: `str("hi")` → `"hi"`, `repr("hi")` → `"'hi'"`.

### Boolean as numeric

`int(True)` is 1 and `int(False)` is 0. This can be useful but may surprise those from languages where booleans are not numeric.

## Interview Questions

### What does int(82.6) return?

82. `int()` truncates toward zero; it does not round.

### How do you convert "42.8" to an integer?

`int(float("42.8"))` — `int()` cannot parse strings with decimal points directly.

### What is the difference between int() and round()?

`int()` truncates; `round()` rounds to the nearest integer. `int(4.8)` → 4, `round(4.8)` → 5.

### Does str() work on all types?

Yes. Every object has a string representation. Custom classes can override `__str__` to control it.

### When does int("x") raise an error?

When the string does not represent a valid integer. `ValueError` is raised for non-numeric strings or strings with decimal points.
