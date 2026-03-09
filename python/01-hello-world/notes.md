# Hello World

A minimal Python program prints output to the console. Understanding script execution and the main guard prepares one for writing reusable modules and executable scripts.

## The print() Function

`print()` sends text to standard output. It accepts one or more arguments and converts them to strings before writing.

```python
print("Hello, World!")
```

**Output:** `Hello, World!`

**Multiple arguments:** Arguments are separated by spaces by default. The `sep` parameter controls the separator.

```python
print("Hello", "World", "!")
```

**Output:** `Hello World !`

```python
print("2", "4", "6", sep="-")
```

**Output:** `2-4-6`

**End parameter:** The `end` parameter controls what is printed after the last argument. The default is a newline (`\n`).

```python
print("Line one", end="")
print("Line two")
```

**Output:** `Line oneLine two`

**No arguments:** `print()` with no arguments prints a single newline.

```python
print()
```

## Script vs Module Execution

A Python file can be run in two ways:

1. **Direct execution** — The file is passed to the interpreter: `python script.py`
2. **Import as module** — The file is imported by another script: `import script`

When a file is executed directly, the special variable `__name__` is set to `"__main__"`. When the file is imported, `__name__` is set to the module name (e.g. `"script"`).

```python
# script.py
print(__name__)
```

**When run directly:** `__main__`

**When imported:** `script` (or the module name)

## The if __name__ == "__main__": Guard

Code placed under `if __name__ == "__main__":` runs only when the file is executed directly, not when it is imported.

```python
def greet():
    print("Hello, World!")

if __name__ == "__main__":
    greet()
```

**Direct execution:** Prints `Hello, World!`

**Import:** Nothing is printed; `greet` is available for other modules to call.

**Purpose:** Allows a file to serve both as a reusable module (with functions and classes) and as a runnable script. Tests, demos, or main logic go inside the guard; definitions stay at module level.

## Common Patterns

**Minimal executable script:**

```python
if __name__ == "__main__":
    print("Hello, World!")
```

**Function plus main block:**

```python
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
```

**Why use a `main()` function:** Encapsulates script logic; makes it easier to test or call from elsewhere. The guard calls `main()` only when the file is run directly.

## Python Syntax Basics

**Indentation:** Python uses indentation to define blocks. Four spaces per level is conventional. Mixing tabs and spaces can cause errors.

**Colon:** A colon (`:`) starts a block. The block must be indented.

```python
if __name__ == "__main__":
    print("indented block")
```

**Comments:** Lines starting with `#` are comments and are ignored.

```python
# This is a comment
print("Hello")  # inline comment
```

## Common Gotchas

### Forgetting the guard

Without the guard, importing a module runs all top-level code, including `print()` calls. This can produce unwanted output when the module is used as a library.

### Wrong __name__ comparison

The comparison must be `__name__ == "__main__"` (two underscores on each side of `main`). Typos such as `_name_` or `__main_` cause the guard to fail silently.

### Indentation errors

The block under `if __name__ == "__main__":` must be indented. Inconsistent indentation raises `IndentationError`.

## Interview Questions

### What does `if __name__ == "__main__":` do?

It ensures the block runs only when the file is executed directly, not when imported. `__name__` is `"__main__"` for the top-level script and the module name when imported.

### When would you omit the main guard?

When the file is intended only as a script and never imported. Even then, adding the guard is good practice for future reuse.

### What is the default value of `end` in `print()`?

A newline character (`\n`). Use `end=""` to suppress the trailing newline.

### How do you pass multiple values to `print()`?

Pass them as separate arguments: `print("a", "b", "c")`. They are separated by spaces by default; use `sep` to change this.
