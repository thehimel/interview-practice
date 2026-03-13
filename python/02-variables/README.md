# Variables

Variables store values in named references. Python is dynamically typed: a variable can hold any type, and the type can change during execution. Understanding assignment, unpacking, and scope is essential for writing correct code.

## Variable Assignment

A variable is created by assigning a value to a name. No explicit declaration is required.

```python
x = 2
name = "Alice"
items = [2, 4, 6, 8]
```

**Naming rules:** Names must start with a letter or underscore; the rest may be letters, digits, or underscores. Names are case-sensitive: `count` and `Count` are different.

**Reassignment:** A variable can be reassigned to a new value of any type.

```python
x = 2
x = "two"
x = [2, 4]
```

## Multiple Assignment

**Chained assignment:** Several variables can be bound to the same value in one statement.

```python
x = y = z = None
```

All three names refer to the same object. For immutable values (e.g. `None`, integers), this is safe. For mutable values (e.g. lists), all names share the same object; mutating one affects all.

```python
a = b = c = []
a.append(2)
# b and c also see [2]
```

**Parallel assignment:** Assign different values to multiple variables in one line.

```python
a, b, c = 2, 4, 6
```

The right-hand side is evaluated first, then values are assigned left to right. The number of names must match the number of values.

## Unpacking

**Tuple or list unpacking:** Assign elements of a sequence to multiple variables.

```python
data = ["Apple", 2, 4.2]
x, y, z = data
# x = "Apple", y = 2, z = 4.2
```

**Equivalent to:** `x = data[0]`, `y = data[1]`, `z = data[2]`.

**Return value unpacking:** Functions that return tuples or lists can be unpacked directly.

```python
def get_values():
    return (2, 4, 6)

a, b, c = get_values()
```

**Asterisk unpacking:** Use `*` to collect remaining elements into a list.

```python
first, *rest = [2, 4, 6, 8, 10]
# first = 2, rest = [4, 6, 8, 10]
```

**Mismatched count:** The number of targets must match the number of values, unless `*` is used.

```python
a, b = [2, 4, 6]   # ValueError: too many values to unpack
a, b, c = [2, 4]   # ValueError: not enough values to unpack
```

## type() and isinstance()

### type()

`type(obj)` returns the exact type of an object. It is useful for introspection and for exercises that require returning types.

```python
type(2)       # <class 'int'>
type(4.2)     # <class 'float'>
type("hi")    # <class 'str'>
type([2, 4])  # <class 'list'>
```

**Returning types from unpacked data:**

```python
data = ["Apple", 2, 4.2]
a, b, c = data
result = (type(a), type(b), type(c))  # (str, int, float)
```

### isinstance()

`isinstance(obj, type)` returns `True` if the object is an instance of the given type or of a subclass of that type. It is the preferred way to check types before conversion or branching.

```python
isinstance(2, int)       # True
isinstance(4.2, float)    # True
isinstance("hi", str)    # True
isinstance(2, (int, float))  # True — tuple of types
```

**Subclass handling:** `isinstance()` returns `True` for subclasses; `type()` checks only the exact type.

```python
class Child(list):
    pass

c = Child()
type(c) == list       # False — exact type is Child
isinstance(c, list)   # True  — Child is a subclass of list
```

**Multiple types:** Pass a tuple of types to check against any of them.

```python
isinstance(2, (int, float))   # True
isinstance("hi", (int, float))  # False
```

### type() vs isinstance()

| Aspect           | type(x) == T      | isinstance(x, T)        |
|------------------|-------------------|--------------------------|
| **Exact match**  | Yes               | Yes                      |
| **Subclasses**   | No                | Yes                      |
| **Use when**      | Need exact type   | Type check before convert |

Use `isinstance()` for type checks in most code; it respects inheritance and is more flexible. Use `type()` when the exact type must be distinguished from subclasses.

## Global Variables and the global Keyword

Variables defined at module level are **global**. They are visible everywhere in the module. Reading a global variable inside a function does not require any special keyword.

**Assignment creates a local:** Assigning to a name inside a function creates a **local** variable by default, even if a global with the same name exists. The local shadows the global.

```python
x = 2

def set_local():
    x = 4  # local x; global x unchanged
    print(x)

set_local()  # 4
print(x)    # 2
```

**The global keyword:** Use `global name` to assign to a global variable from inside a function. Without it, assignment creates a local.

```python
x = y = z = None
data = ["Apple", 2, 4.2]

def assign_globals():
    global x, y, z
    x, y, z = data[0], data[1], data[2]

assign_globals()
# x == "Apple", y == 2, z == 4.2
```

**Read vs write:** Reading a global does not require `global`. Only assignment does.

```python
count = 0

def read_global():
    print(count)  # OK — reads global

def write_global():
    global count
    count += 2    # OK — modifies global
```

## Scope Overview

| Scope      | Where defined        | Visibility                    |
|------------|----------------------|-------------------------------|
| **Local**  | Inside a function   | That function only            |
| **Global** | Module top level    | Entire module                 |
| **Built-in** | Python built-ins  | Everywhere                    |

**LEGB rule:** Python looks up names in order: Local → Enclosing → Global → Built-in.

## Common Gotchas

### Unpacking count mismatch

The number of variables must match the number of values. Use `*` to absorb extras: `a, *rest = [2, 4, 6]`.

### Forgetting global for assignment

Assigning to a global name without `global` creates a local. The global remains unchanged. Use `global` when the function must modify the global.

### Chained assignment with mutables

`a = b = []` makes both names refer to the same list. Appending to `a` also affects `b`. Use `a = []; b = []` when independent lists are needed.

### type() returns the type object

`type(x)` returns `<class 'int'>`, not the string `"int"`. For a string name, use `type(x).__name__` → `"int"`.

## Interview Questions

### When is the global keyword required?

When assigning to a global variable inside a function. Reading a global does not require it.

### What happens if you unpack a sequence with the wrong number of elements?

`ValueError: too many values to unpack` or `ValueError: not enough values to unpack`. Use `*` to collect extras.

### What does type() return?

The type object of the argument (e.g. `<class 'int'>`). It is not a string; use `type(x).__name__` for the type name as a string.

### Why does x = y = [] create shared references?

Chained assignment binds all names to the same object. For mutable types, mutating through one name affects all. Use separate assignments for independent objects.

### What is the difference between type() and isinstance()?

`type(x)` returns the exact type of `x`; `type(x) == int` is `True` only when `x` is precisely an `int`. `isinstance(x, int)` returns `True` when `x` is an `int` or a subclass of `int`. Use `isinstance()` for type checks in most code; use `type()` when subclasses must be excluded.

```python
x = 4
type(x) == int        # True
isinstance(x, int)    # True

# bool is a subclass of int
type(True) == int     # False — exact type is bool
isinstance(True, int)  # True  — bool subclasses int

# Custom subclass
class MyInt(int):
    pass
y = MyInt(6)
type(y) == int        # False — exact type is MyInt
isinstance(y, int)     # True  — MyInt subclasses int
```
