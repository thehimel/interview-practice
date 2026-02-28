# Functions

A function is a named block of code. It is invoked when called, accepts data as arguments, and can return a result. Reusing that logic instead of copying it keeps code shorter and easier to change.

## Defining a Function

```
def function_name(parameters):
    body
```

Use the `def` keyword, then the name, parentheses with parameters (if any), and a colon. The body is indented. Python uses indentation to define blocks.

```python
def greet():
    print("Hello")
```

## Calling a Function

Call a function by writing its name followed by parentheses. Arguments go inside the parentheses.

```python
greet()
greet()
```

## Function Names

Names follow the same rules as variables: start with a letter or underscore; contain only letters, digits, underscores; case-sensitive. Use descriptive names.

## Return Values

Use `return` to send a value back. Execution stops at `return`; later code in the function does not run.

```python
def double(x):
    return x * 2

result = double(6)
print(result)  # 12
```

**No return:** If a function has no `return` or reaches the end without one, it returns `None`.

## The pass Statement

A function body cannot be empty. Use `pass` as a placeholder.

```python
def stub():
    pass
```

## Parameters vs Arguments

| Term          | Meaning                                                |
|---------------|--------------------------------------------------------|
| **Parameter** | Variable in the function definition (e.g. `def f(x):`) |
| **Argument**  | Value passed when calling (e.g. `f(4)`)                |

## Default Parameter Values

Assign a default in the definition. If the caller omits the argument, the default is used.

```python
def greet(name="friend"):
    print("Hello", name)

greet("Alice")
greet()
```

**Output:** `Hello Alice`, `Hello friend`

**Mutable defaults:** Do not use mutable objects (list, dict) as defaults. They are created once and shared across calls:

```python
# Wrong — same list reused for every call
def add_item(item, lst=[]):
    lst.append(item)
    return lst

# Correct — create a new list each time
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

## Positional and Keyword Arguments

**Positional:** Passed in order; matched to parameters by position.

```python
def f(a, b, c):
    return a + b + c

f(2, 4, 6)  # 12
```

**Keyword:** Passed as `name=value`; order does not matter.

```python
f(c=6, a=2, b=4)  # 12
```

**Mixing:** Positional arguments must come before keyword arguments.

```python
f(2, 4, c=6)
f(2, b=4, c=6)
# f(a=2, 4, 6)  # SyntaxError
```

## Positional-Only Parameters (`/`)

Parameters before `/` cannot be passed by keyword.

```python
def f(a, b, /):
    return a + b

f(2, 4)
# f(a=2, b=4)  # TypeError
```

## Keyword-Only Parameters (`*`)

Parameters after `*` must be passed by keyword.

```python
def f(*, a, b):
    return a + b

f(a=2, b=4)
# f(2, 4)  # TypeError
```

## Combining `/` and `*`

```python
def f(a, b, /, c, *, d, e):
    return a + b + c + d + e

f(2, 4, 6, d=8, e=10)   # c can be positional or keyword
f(2, 4, c=6, d=8, e=10)
```

Order: positional-only → regular → keyword-only.

## *args — Arbitrary Positional Arguments

`*args` collects extra positional arguments into a tuple.

```python
def sum_all(*nums):
    return sum(nums)

sum_all(2, 4, 6)
sum_all(2, 4, 6, 8, 10)
```

**Name:** `args` is conventional; any name works. The `*` is required.

**Order:** Regular parameters must come before `*args`.

## **kwargs — Arbitrary Keyword Arguments

`**kwargs` collects extra keyword arguments into a dict.

```python
def show(**data):
    for k, v in data.items():
        print(k, v)

show(a=2, b=4, c=6)
```

## Order of Parameters

When combining parameter types:

1. Positional-only (before `/`)
2. Regular positional/keyword
3. `*args`
4. Keyword-only (after `*`)
5. `**kwargs`

```python
def f(a, b, /, c, *args, d, e=20, **kwargs):
    pass
```

## Unpacking Arguments

**`*`** unpacks an iterable into positional arguments:

```python
def add(a, b, c):
    return a + b + c

vals = [2, 4, 6]
add(*vals)  # same as add(2, 4, 6)
```

**`**`** unpacks a dict into keyword arguments:

```python
def greet(name, age):
    print(name, age)

d = {"name": "Alice", "age": 24}
greet(**d)  # same as greet(name="Alice", age=24)
```

## Passing and Returning Data Types

Functions accept and return any type: int, float, str, list, tuple, dict, etc. The type is preserved.

```python
def first_two(items):
    return items[:2]

first_two([2, 4, 6, 8])
def make_pair():
    return (10, 20)
```

## Scope

A variable is visible only in the region where it is defined.

| Scope         | Where              | Visibility                         |
|---------------|--------------------|------------------------------------|
| **Local**     | Inside a function  | That function only                 |
| **Enclosing** | Nested function    | Inner function sees outer's locals |
| **Global**    | Module top level   | Everywhere in the module           |
| **Built-in**  | Python's built-ins | Everywhere                         |

## LEGB Rule

Python looks up names in this order: **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in.

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()

outer()  # local
```

## global Keyword

Use `global` to assign to a global variable from inside a function. Without it, assignment creates a local variable.

```python
count = 0

def increment():
    global count
    count += 2

increment()
print(count)  # 2
```

**Read vs write:** Reading a global does not require `global`; only assignment does.

## nonlocal Keyword

Use `nonlocal` to assign to a variable in an enclosing (non-global) scope.

```python
def outer():
    x = 2
    def inner():
        nonlocal x
        x = 4
    inner()
    return x

outer()  # 4
```

## Decorators

A decorator is a function that takes another function and returns a modified function. Apply with `@decorator` above the definition.

```python
def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase
def greet(name):
    return f"Hello {name}"

greet("Alice")  # "HELLO ALICE"
```

**Order:** Decorators run bottom-to-top when applied; the innermost runs first when the function is called.

**Decorator with arguments:** Use a decorator factory — a function that returns a decorator:

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(2)
def say_hi():
    print("Hi")
```

**Multiple decorators:** Applied bottom-to-top. The one closest to the function runs first when the function is called.

## Preserving Metadata with functools.wraps

Decorators replace the function, so `__name__` and `__doc__` are lost. Use `functools.wraps` to copy them:

```python
import functools

def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper
```

## Lambda Functions

A lambda is an anonymous function with a single expression. Syntax: `lambda args: expression`.

```python
double = lambda x: x * 2
double(6)  # 12

add = lambda a, b: a + b
add(2, 4)  # 6
```

**Limitation:** One expression only; no statements, no annotations.

**Common use:** Short callbacks for `sorted()`, `map()`, `filter()`:

```python
pairs = [(2, 4), (6, 2), (4, 8)]
sorted(pairs, key=lambda p: p[1])
```

## Recursion

A function that calls itself. Requires a **base case** (stops recursion) and a **recursive case** (calls itself with a smaller problem).

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

factorial(6)  # 720
```

**Stack limit:** Python limits recursion depth (~1000; check with `sys.getrecursionlimit()`). Deep recursion can raise `RecursionError`. Prefer iteration for very deep recursion.

## Generators

A generator is a function that uses `yield` instead of `return`. It produces values one at a time and pauses between yields.

```python
def count_up_to(n):
    i = 2
    while i <= n:
        yield i
        i += 2

list(count_up_to(8))  # [2, 4, 6, 8]
```

**Memory:** Generators are lazy; they do not build the full sequence in memory.

**Generator expression:** `(x * 2 for x in range(6))` — parentheses, not brackets. Returns a generator, not a list.

**Manual iteration:** Use `next(gen)` to get the next value. When exhausted, `next()` raises `StopIteration`.

## Interview Questions

### What does a function return if it has no return statement?

`None`.

### Why avoid mutable default arguments?

The default object is created once when the function is defined. Every call that uses the default shares the same object. Mutating it affects future calls.

### What is the order of parameter types in a function definition?

Positional-only (before `/`) → regular → `*args` → keyword-only (after `*`) → `**kwargs`.

### What does `*args` collect? `**kwargs`?

`*args` collects extra positional arguments into a tuple. `**kwargs` collects extra keyword arguments into a dict.

### When is `global` needed?

When you assign to a global variable inside a function. Reading a global does not require it.

### What does `nonlocal` do?

It allows assignment to a variable in an enclosing (non-global) scope, typically in a nested function.

### What is the LEGB rule?

Python looks up names in order: Local → Enclosing → Global → Built-in.

### How does a decorator work?

A decorator is a function that takes another function and returns a new function. `@decorator` is equivalent to `func = decorator(func)`.

### What can a lambda contain?

A single expression. No statements, no `return`, no annotations.

### When does recursion cause a RecursionError?

When the call stack exceeds Python's recursion limit (~1000) or when there is no base case and recursion never stops.
