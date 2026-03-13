# OOP Part 2 — Encapsulation, Abstraction, Inheritance, Polymorphism

## Encapsulation

Encapsulation bundles data and behavior in a class and limits how the data is read or changed from outside. That reduces accidental changes and hides implementation details.

### Private Attributes: `__` Prefix

A leading double underscore `__` (with at most one trailing underscore) triggers **name mangling**. Python rewrites `__attr` to `_ClassName__attr` to avoid name collisions in inheritance. A side effect: `obj.__attr` from outside raises `AttributeError` because the stored name is the mangled one.

```python
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

a = Account("Alice", 1000)
print(a.owner)     # Alice
# a.__balance      # AttributeError
```

### Getter and Setter

Use methods to expose or change private data. Getters return the value; setters can validate before updating.

```python
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")

a = Account("Alice", 1000)
print(a.get_balance())  # 1000
a.set_balance(1200)
print(a.get_balance())  # 1200
a.set_balance(-100)     # Balance cannot be negative
```

### Protected Attributes: `_` Prefix

A single underscore `_` is a convention meaning "internal use." Python does not enforce it; it is a signal to other developers.

```python
class Worker:
    def __init__(self, name, rate):
        self.name = name
        self._rate = rate

w = Worker("Bob", 24)
print(w._rate)  # 24 — access works; convention says avoid
```

**Accessing a protected member from an instance:** It works. `obj._attr` returns the value. Python does nothing to block it. The underscore is a hint to developers, not a runtime restriction.

### Private vs Protected

| Aspect           | Private (`__attr`)           | Protected (`_attr`)        |
|------------------|------------------------------|----------------------------|
| **Enforcement**  | Name mangling; `obj.__attr` → `AttributeError` | No enforcement; `obj._attr` works |
| **Access from outside** | Use getter or mangled name `_Class__attr` | Direct `obj._attr` works |
| **Convention**   | Strong "do not touch"        | "Internal; use with care"  |
| **Inheritance**  | Child cannot access `__attr` by that name (mangled differently per class) | Child can access `_attr` directly |

**Which is convention?** Only `_attr` is convention. Python does nothing to it. `__attr` triggers real name mangling — a language mechanism, not just a style choice.

**When to use `_attr`:** When you want to mark "internal" but allow subclasses or tests to reach it. Common in libraries and frameworks. Use when the attribute may be useful to subclasses.

**When to use `__attr`:** When you want to avoid inheritance name collisions, or when you want `obj.__attr` to fail from outside. Use sparingly; it can surprise developers who expect subclasses to access parent internals.

### Private Methods

Methods can use `__` too. They are meant for internal use only.

```python
class Accumulator:
    def __init__(self):
        self.total = 0

    def __check(self, x):
        return isinstance(x, (int, float))

    def add(self, x):
        if self.__check(x):
            self.total += x
        return self.total

acc = Accumulator()
print(acc.add(4))   # 4
print(acc.add(6))   # 10
# acc.__check(4)    # AttributeError
```

### Name Mangling

Python rewrites `__name` to `_ClassName__name`. You can still access it with the mangled name, but that bypasses encapsulation.

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance

a = Account(1000)
print(a._Account__balance)  # 1000 — works but avoid
```

### Why Encapsulation?

| Benefit      | Description                                      |
|--------------|--------------------------------------------------|
| **Protection** | Reduces accidental changes to internal state     |
| **Validation** | Setters can enforce rules before updating       |
| **Flexibility** | Internal structure can change without breaking callers |
| **Control**    | You decide how data is read and written         |

## Inheritance

Inheritance lets a class reuse another class's attributes and methods. The **parent** (base) class is inherited from; the **child** (derived) class inherits.

### Basic Inheritance

Put the parent class in parentheses when defining the child.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    pass

d = Dog("Rex")
d.speak()  # Rex makes a sound
```

### Overriding __init__

If the child defines `__init__`, it replaces the parent's. Call the parent's `__init__` explicitly to keep its setup.

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed

d = Dog("Rex", "Lab")
print(d.name, d.breed)  # Rex Lab
```

### super()

`super()` refers to the parent class. Use it to call parent methods without naming the parent.

```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

**Why super()?** It works with multiple inheritance and stays correct if the parent class name changes.

### Adding Properties and Methods

The child can add new attributes and methods.

```python
class Student(Animal):
    def __init__(self, name, year):
        super().__init__(name)
        self.year = year

    def greet(self):
        print(f"Hi, I'm {self.name}, class of {self.year}")

s = Student("Alex", 2024)
s.greet()  # Hi, I'm Alex, class of 2024
```

### Method Overriding

A child method with the same name as a parent method overrides it. The child's version runs when called on a child instance.

```python
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

d = Dog("Rex")
d.speak()  # Rex barks (overrides Animal.speak)
```

---

## Polymorphism

Polymorphism means the same interface (e.g. method name) can behave differently depending on the object. Callers use one interface; each type implements it its own way.

### Built-in Polymorphism

`len()` works on strings, lists, dicts, etc. Each type defines how length is computed.

```python
len("hello")           # 5
len([2, 4, 6])         # 3
len({"a": 2, "b": 4})  # 2
```

### Class Polymorphism

Different classes can define the same method name. A loop over a mix of types can call that method on each.

```python
class Car:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print("Driving")

class Boat:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print("Sailing")

class Plane:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print("Flying")

items = [Car("Toyota"), Boat("Yacht"), Plane("Boeing")]
for x in items:
    x.move()  # Driving, Sailing, Flying
```

### Inheritance and Polymorphism

A parent can define a method; children override it. Code that works with the parent type can work with any child.

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print("Moving")

class Car(Vehicle):
    def move(self):
        print("Driving")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

v1 = Car("Toyota")
v2 = Boat("Yacht")
for v in [v1, v2]:
    v.move()  # Driving, Sailing
```

`Car` inherits `move` but overrides it. `Boat` does the same. The loop does not need to know the concrete type.

## Abstraction

Abstraction hides implementation details and exposes only what callers need. You define a contract (what methods exist) without specifying how they work. Subclasses provide the implementation.

### Abstract Base Classes (ABCs)

Use the `abc` module to define abstract classes. Mark methods with `@abstractmethod`; subclasses must implement them. You cannot instantiate an abstract class directly.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

r = Rectangle(3, 4)
print(r.area())       # 12
print(r.perimeter())  # 14
# s = Shape()         # TypeError: Can't instantiate abstract class Shape
```

### Why Use Abstraction?

| Benefit        | Description                                              |
|----------------|----------------------------------------------------------|
| **Contract**   | Forces subclasses to implement required methods          |
| **Flexibility**| Callers depend on the interface, not concrete classes    |
| **Clarity**    | Makes the expected API explicit                          |

### Abstraction vs Encapsulation

- **Encapsulation:** Hides data and internal logic; controls access via getters/setters.
- **Abstraction:** Hides implementation; defines a contract (interface) that subclasses must fulfill.

## Common Gotchas

### Name mangling is not true privacy

You can still use `_ClassName__attr`. It is a convention, not a security barrier.

### Forgetting super() in __init__

If the child defines `__init__` and does not call the parent's, the parent's attributes are never set.

### Overriding vs extending

Override: replace the parent method. Extend: call `super().method()` and add more logic.

## Interview Questions

### What is encapsulation?

Bundling data and behavior in a class and controlling access. Private/protected attributes and getters/setters help limit how data is read or changed.

### What does `__` do to an attribute name?

It triggers name mangling. Python rewrites it to `_ClassName__attr`. It signals "internal" and makes accidental access from outside harder.

### What is the difference between `_` and `__`?

`_` is a convention only; Python does nothing. `obj._attr` works. `__` triggers name mangling; `obj.__attr` raises `AttributeError`, though you can still use the mangled name.

### Why use super() instead of Parent.__init__(self, ...)?

`super()` works with multiple inheritance and stays correct if the parent class is renamed or the hierarchy changes.

### What is polymorphism?

The same interface (e.g. method name) behaving differently for different types. Callers use one interface; each type implements it its own way.

### How does inheritance relate to polymorphism?

A parent defines an interface; children override methods. Code written for the parent type can work with any child without knowing the concrete type.

### What is abstraction?

Hiding implementation details and exposing only what callers need. Abstract base classes (ABCs) define a contract via `@abstractmethod`; subclasses must implement those methods. You cannot instantiate an abstract class.
