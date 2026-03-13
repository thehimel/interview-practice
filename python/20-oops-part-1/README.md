# OOP Part 1 — Classes and Objects

OOP organizes code into **classes** (templates) and **objects** (instances). Benefits: clearer structure, simpler maintenance, less duplication, and reusable pieces you can plug into different parts of a program.

## Classes and Objects

A **class** is the template; an **object** is a concrete instance. One class can spawn many objects, each with its own attribute values. For example, a `Vehicle` class can yield `Vehicle("Toyota", 2024)` and `Vehicle("Honda", 2022)` as separate objects.

## Defining a Class

Use the `class` keyword. The body is indented. An empty body needs `pass`.

```python
class Vehicle:
    pass
```

## What Is a Constructor?

In OOP, a constructor is the logic that runs when an object is created. In C++ or Java it typically allocates memory and sets up the object.

**In Python:** `__new__` builds the object; `__init__` then runs to set its attributes. So `__init__` is the initializer, not the allocator. The object already exists when `__init__` is called. You almost always use `__init__`; `__new__` is for edge cases like singletons.

## Instance Attributes and __init__

`__init__(self, ...)` is the **initializer**. It runs when an object is created. Use it to set instance attributes.

```python
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

v = Vehicle("Toyota", 2024)
print(v.brand, v.year)  # Toyota 2024
```

**Manual setup without __init__:** You could do `p = Vehicle()` then `p.brand = "Toyota"` and `p.year = 2024` for every object. `__init__` avoids that repetition by running setup automatically on creation.

**First parameter:** It holds the instance. Most code uses `self`; you could name it `obj` or `me`, but `self` is the usual choice and what others expect.

## The self Parameter

`self` refers to the current instance. Methods receive it as the first argument; Python passes the instance automatically when you call `obj.method()`.

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def describe(self):
        return f"This is a {self.brand}"

v = Vehicle("Honda")
v.describe()
```

**Why self?** Without it, a method cannot access or modify the instance's attributes. Each call is bound to a specific object.

## Default Values in __init__

Parameters can have defaults. Use them for optional attributes.

```python
class Vehicle:
    def __init__(self, brand, year=2024):
        self.brand = brand
        self.year = year

v1 = Vehicle("Toyota")
v2 = Vehicle("Honda", 2022)
print(v1.year, v2.year)  # 2024 2022
```

## Class Attributes vs Instance Attributes

| Type         | Where defined  | Shared? | Example               |
|--------------|----------------|---------|-----------------------|
| **Instance** | In `__init__`  | No      | `self.brand = brand`  |
| **Class**    | At class level | Yes     | `species = "Vehicle"` |

**Class attributes** — Shared by all instances. Every instance reads the same value; changing it affects all.

**Instance attributes** — Each object has its own copy. Changing one object's attribute does not affect others.

```python
class Vehicle:
    wheels = 4

    def __init__(self, brand):
        self.brand = brand

v1 = Vehicle("Toyota")
v2 = Vehicle("Honda")

# Instance: each object has its own brand
print(v1.brand, v2.brand)  # Toyota Honda
v1.brand = "Lexus"
print(v1.brand, v2.brand)  # Lexus Honda

# Class: both share the same wheels
print(v1.wheels, v2.wheels)  # 4 4
Vehicle.wheels = 6
print(v1.wheels, v2.wheels)  # 6 6
```

Changing `v1.brand` only affects `v1`. Changing `Vehicle.wheels` affects both `v1` and `v2` because they share that attribute.

```python
class Vehicle:
    count = 0

    def __init__(self, brand):
        self.brand = brand
        Vehicle.count += 1

v1 = Vehicle("Toyota")
v2 = Vehicle("Honda")
print(Vehicle.count)       # 2
print(v1.brand, v2.brand)  # Toyota Honda
```

**Shadowing:** Assigning `v1.count = 4` creates an instance attribute that shadows the class attribute for that object only. The class attribute is unchanged for others.

**Adding a new attribute:** `v1.other = "something"` creates a new instance attribute on `v1` only. No class attribute exists; `v2` has no `other`. Only `v1` gets it. Python allows adding attributes to instances at any time.

## Reading and Updating Attributes

Read and write attributes with `obj.attr`. No special syntax.

```python
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

v = Vehicle("Toyota", 2024)
v.year = 2026
print(v.year)  # 2026
```

**New attributes on the fly:** Assign to `obj.new_attr = value` and that instance gains the attribute. Other instances are unchanged.

```python
v = Vehicle("Toyota", 2024)
v.color = "blue"
print(v.color)  # blue
```

## Deleting Attributes and Objects

`del obj.attr` drops that attribute from the object. `del obj` unbinds the variable; the object stays in memory if something else still references it.

```python
v = Vehicle("Toyota", 2024)
del v.year
# v.year  # AttributeError
del v
# v  # NameError
```

## Methods

Methods are functions attached to a class. They take `self` first so they can work with the instance. They can read attributes, change them, or call other methods.

```python
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

calc = Calculator()
print(calc.add(2, 4))        # 6
print(calc.multiply(6, 8))   # 48
```

**Methods that change state:** A method can update instance attributes. For example, a counter that increments:

```python
class Counter:
    def __init__(self, start=0):
        self.value = start

    def step(self, n=2):
        self.value += n

c = Counter(4)
c.step()
print(c.value)  # 6
```

**Chaining method calls:** From inside one method, call another with `self.other_method()`.

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        return self.brand

    def display(self):
        print(self.info())
```

**Adding methods at runtime:** Assign a function to the class: `Vehicle.extra_info = some_func`. Every instance (current and future) gets that method. The function must accept `self` as the first argument, since Python passes the instance when you call it.

```python
def extra_info(self):
    return f"Extra: {self.brand}"

Vehicle.extra_info = extra_info
v = Vehicle("Toyota")
print(v.extra_info())  # Extra: Toyota
```

**Removing methods:** `del ClassName.method_name` removes the method from the class. All instances lose it.

```python
del Vehicle.extra_info
# v.extra_info()  # AttributeError
```

## @classmethod and @staticmethod

Instance methods take `self` and work with the instance. **Class methods** take `cls` and work with the class. **Static methods** take neither; they are plain functions that live in the class namespace.

```python
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def is_valid(n):
        return isinstance(n, int) and n >= 0

c = Counter()
print(Counter.get_count())   # 1
print(Counter.is_valid(4))   # True
print(Counter.is_valid(-1))  # False
```

### When to Use @staticmethod

Use `@staticmethod` when the method:

- **Does not need `self` or `cls`** — It is a utility tied to the class by name only, not by instance or class state.
- **Is a pure function** — Same inputs always give the same outputs; no side effects on instance or class.
- **Belongs logically to the class** — E.g. validation, formatting, or conversion helpers that are grouped with the class for organization.

**Example:** A `Date` class with `Date.parse("2024-01-15")` that returns a `Date` instance. The logic does not need instance or class state.

```python
class Date:
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    @staticmethod
    def from_string(s):
        parts = s.split("-")
        return Date(int(parts[0]), int(parts[1]), int(parts[2]))

d = Date.from_string("2024-01-15")
```

### When to Use @classmethod

Use `@classmethod` when the method:

- **Needs `cls`** — To create instances, access class attributes, or call other class methods.
- **Is an alternate constructor** — Factory methods like `from_dict`, `from_json` that return instances of the class.
- **Operates on class-level state** — E.g. `get_count()` above.

```python
class Date:
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    @classmethod
    def from_string(cls, s):
        parts = s.split("-")
        return cls(int(parts[0]), int(parts[1]), int(parts[2]))

d = Date.from_string("2024-01-15")  # cls is Date
```

Using `cls` instead of `Date` keeps it correct for subclasses; a `Timestamp(Date)` would return a `Timestamp`, not a `Date`.

### Quick Comparison

| Decorator       | First param | Use when                                          |
|-----------------|-------------|---------------------------------------------------|
| (none)          | `self`      | Method needs instance attributes                  |
| `@classmethod`  | `cls`       | Method needs class or is an alternate constructor |
| `@staticmethod` | none        | Utility; no instance or class state needed        |

## __str__ and __repr__

`__str__` defines what `print(obj)` and `str(obj)` show. `__repr__` is for the interpreter and `repr(obj)`; ideally it returns a string that looks like valid Python to recreate the object.

```python
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def __str__(self):
        return f"{self.brand} ({self.year})"

    def __repr__(self):
        return f"Vehicle('{self.brand}', {self.year})"

v = Vehicle("Toyota", 2024)
print(v)        # Toyota (2024)
print(repr(v))  # Vehicle('Toyota', 2024)
```

**Without __str__:** `print(v)` uses `__repr__` as a fallback, which often shows something like `<__main__.Vehicle object at 0x...>`.

## The pass Statement

Python requires a non-empty body. Use `pass` when you need the structure but no logic yet.

```python
class Placeholder:
    pass
```

## Multiple Objects

Each `ClassName(...)` call creates a new object. Instance attributes live on that object; changing one does not touch the others.

```python
v1 = Vehicle("Toyota", 2024)
v2 = Vehicle("Honda", 2022)
v1.year = 2026
print(v2.year)  # 2022 — changing v1 does not affect v2
```

## Inner Classes

You can define a class inside another. That inner class sits in the outer class's namespace and is handy when the logic belongs to one context. The inner class does not get a reference to the outer instance by default; you hand it over yourself if needed.

### Defining an Inner Class

Put the class definition in the outer class body. It becomes an attribute on the outer class.

```python
class Enclosing:
    def __init__(self):
        self.label = "Enclosing"

    class Nested:
        def __init__(self):
            self.label = "Nested"

        def show(self):
            print("From nested")

e = Enclosing()
print(e.label)  # Enclosing
```

### Accessing the Inner Class from Outside

Instantiate the outer class first, then call the inner class through it: `outer.Inner()`.

```python
e = Enclosing()
n = e.Nested()
n.show()        # From nested
print(n.label)  # Nested
```

`Enclosing.Nested()` works too — the inner class is attached to the outer. `e.Nested()` just makes the relationship to `e` explicit.

### No Automatic Access to the Outer Instance

The inner class never receives the outer instance automatically. It has no built-in way to reach the outer object unless you pass it in.

```python
class Enclosing:
    def __init__(self):
        self.value = 42

    class Nested:
        def show(self):
            pass
            # No way to access Enclosing's value from here
```

### Passing the Outer Instance to the Inner Class

Hand the outer instance into the inner class (e.g. in `__init__`) so the inner can use it.

```python
class Enclosing:
    def __init__(self):
        self.value = 24

    class Nested:
        def __init__(self, enclosing):
            self.enclosing = enclosing

        def show(self):
            print(self.enclosing.value)

e = Enclosing()
n = e.Nested(e)
n.show()  # 24
```

The inner object keeps a reference to the outer and can read or call its attributes.

### Practical Use: Helper Components

Use inner classes for pieces that only make sense inside the outer — e.g. a vehicle's engine, or a device's config.

```python
class Device:
    def __init__(self, name):
        self.name = name
        self.config = self.Config()

    class Config:
        def __init__(self):
            self.port = 8080
            self.enabled = True

        def toggle(self):
            self.enabled = not self.enabled

    def status(self):
        s = "on" if self.config.enabled else "off"
        print(f"{self.name} is {s}")

d = Device("Server")
d.status()          # Server is on
d.config.toggle()
d.status()          # Server is off
print(d.config.port)  # 8080
```

### Multiple Inner Classes

You can nest more than one class. Each is its own component.

```python
class DataPipeline:
    def __init__(self):
        self.reader = self.Reader()
        self.writer = self.Writer()

    class Reader:
        def read(self):
            print("Reading...")

    class Writer:
        def write(self):
            print("Writing...")

p = DataPipeline()
p.reader.read()    # Reading...
p.writer.write()   # Writing...
```

### When to Use Inner Classes

| Use an inner class when                     | Use a top-level class when              |
|---------------------------------------------|-----------------------------------------|
| The class is only used in one outer context | The class is reused across the codebase |
| It represents a part of the outer object    | It is a standalone concept              |
| You want related code in one place          | The logic is independent                |

### Inner Class Gotchas

**No built-in outer reference:** The inner class does not get the outer instance automatically. Pass it in if the inner needs it.

**Namespace:** The inner class lives under the outer. Use `Outer.Inner` to refer to it. Don't give an attribute and an inner class the same name.

**Testing:** Inner classes are trickier to unit test on their own. If you need to reuse or test a component separately, a top-level class is often simpler.

## Common Gotchas

### Forgetting self

If a method uses instance attributes, it must take `self` as the first parameter. Omitting it leads to `TypeError` when the method is called.

### Mutable class attributes

A class attribute like `items = []` is shared by all instances. Appending to it changes it for everyone. Use instance attributes in `__init__` for per-object state.

### self naming

The first parameter can be named anything (`me`, `obj`, etc.). `self` is the norm; straying from it makes code harder for others to follow.

## Interview Questions

### What is the difference between a class and an object?

The class is the template; the object is a concrete instance. One class can produce many objects, each with its own attribute values.

### What is a constructor? How does __init__ relate to it?

A constructor is code that runs when an object is created. In Python, `__new__` creates the object; `__init__` then runs to set its state. `__init__` is often called the constructor, but it is the initializer — the object already exists when it runs. Override `__new__` only for special cases (e.g. singletons).

### Why is self the first parameter of instance methods?

Python passes the instance as the first argument when you call `obj.method()`. That argument is `self`. It lets the method access and modify that instance's attributes.

### What is the difference between class and instance attributes?

Class attributes live on the class and are shared by all instances. Instance attributes are set in `__init__` (or later) and belong to each object.

### When is __str__ used vs __repr__?

`__str__` is for user-facing output (`print`, `str()`). `__repr__` is for debugging and the interpreter; it should ideally be unambiguous and look like valid Python.

### What is an inner class?

A class defined inside another. It is accessed as `Outer.Inner` and lives in the outer class's namespace.

### Does an inner class automatically have access to the outer instance?

No. You have to pass the outer instance in (e.g. via `__init__`) if the inner needs it.

### When would you use an inner class?

When the class is used only in one place, represents a component of the outer object, and you want to keep the code together. E.g. Engine inside Vehicle, Config inside Device.

### When to use @staticmethod?

When the method does not need `self` or `cls` — it is a utility or pure function that belongs logically to the class. Use for validation, formatting, parsing, or conversion helpers that do not touch instance or class state.
