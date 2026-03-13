# Strings

## Overview

This exercise covers Python string operations in six topics. Each function has a docstring describing what to implement. Sample data is in `constants.py`.

**File structure:**

- `solutions/` – Reference implementations by subtopic: `concatenation.py`, `format.py`, `modify.py`, `search.py`, `slicing.py`, `types.py`
- `exercises/` – Stub implementations in the same structure for practice
- `solutions/test_*_solution.py` – Per-topic test logic and solution tests
- `exercises/test_*_exercise.py` – Per-topic exercise tests (use logic from solution test files)

**Topics:**

1. **Concatenation** – `+` operator, `join()`
2. **Format** – F-strings, `:.2f`, expressions in braces, `format()`, `center()`, `ljust()`, `rjust()`, `zfill()`
3. **Modify** – `upper()`, `lower()`, `strip()`, `lstrip()`, `rstrip()`, `strip(chars)`, `replace()`, `replace(..., count)`, `split()`, `rsplit()`, `splitlines()`, `capitalize()`, `swapcase()`, `title()`, `removeprefix()`, `removesuffix()`, `partition()`, `rpartition()`, `casefold()`
4. **Search** – `find()`, `index()`, `rfind()`, `rindex()`, `count()`, `in`, `startswith()`, `endswith()`
5. **Slicing** – Indexing, slicing, `[::-1]`, `reversed()`, negative indices, `len()`
6. **Types** – `isalnum()`, `isalpha()`, `isdigit()`, `islower()`, `isupper()`, `isnumeric()`, `isspace()`, `istitle()`

## Example Use Cases

Using `constants.SLICE_STR = "Python"`, `constants.MODIFY_STR = "  Hello World  "`, etc.

### 1. Concatenation

| Function Call                    | Output         | Method            |
|----------------------------------|----------------|-------------------|
| `concat("Hello", "World")`       | `"HelloWorld"` | `a + b`           |
| `join_str("-", ["a", "b", "c"])` | `"a-b-c"`      | `sep.join(parts)` |

### 2. Format

| Function Call                          | Output                       | Method                            |
|----------------------------------------|------------------------------|-----------------------------------|
| `fstring_example("Alice", 86.8)`       | `"Name: Alice, Score: 86.8"` | `f"Name: {name}, Score: {score}"` |
| `decimal_format(2.46)`                 | `"2.46"`                     | `f"{x:.2f}"`                      |
| `expr_in_fstring(4, 6)`                | `"4*6=24"`                   | `f"{x}*{y}={x*y}"`                |
| `format_method("{} and {}", "a", "b")` | `"a and b"`                  | `template.format(a, b)`           |
| `centered("hi", 6)`                    | `"  hi  "`                   | `s.center(width)`                 |
| `left_justified("hi", 6)`              | `"hi    "`                   | `s.ljust(width)`                  |
| `right_justified("hi", 6)`             | `"    hi"`                   | `s.rjust(width)`                  |
| `zfill_str("42", 6)`                   | `"000042"`                   | `s.zfill(width)`                  |

### 3. Modify

| Function Call                                   | Output                        | Method                       |
|-------------------------------------------------|-------------------------------|------------------------------|
| `to_upper("hello")`                             | `"HELLO"`                     | `s.upper()`                  |
| `to_lower("HELLO")`                             | `"hello"`                     | `s.lower()`                  |
| `casefold_str("Straße")`                        | `"strasse"`                   | `s.casefold()`               |
| `capitalized("hello")`                          | `"Hello"`                     | `s.capitalize()`             |
| `swap_case("HeLLo")`                            | `"hEllO"`                     | `s.swapcase()`               |
| `title_case("hello world")`                     | `"Hello World"`               | `s.title()`                  |
| `stripped("  hi  ")`                            | `"hi"`                        | `s.strip()`                  |
| `left_stripped("  hi")`                         | `"hi"`                        | `s.lstrip()`                 |
| `right_stripped("hi  ")`                        | `"hi"`                        | `s.rstrip()`                 |
| `stripped_chars("xxhixx", "x")`                 | `"hi"`                        | `s.strip(chars)`             |
| `replaced("aabb", "a", "x")`                    | `"xxbb"`                      | `s.replace(old, new)`        |
| `replace_count("one one one", "one", "two", 2)` | `"two two one"`               | `s.replace(old, new, count)` |
| `split_str("a,b,c", ",")`                       | `["a", "b", "c"]`             | `s.split(sep)`               |
| `rsplit_str("a,b,c,d", ",", 2)`                 | `["a,b", "c", "d"]`           | `s.rsplit(sep, maxsplit)`    |
| `split_lines("line0\nline2\nline4")`            | `["line0", "line2", "line4"]` | `s.splitlines()`             |
| `remove_prefix("https://x.com", "https://")`    | `"x.com"`                     | `s.removeprefix(prefix)`     |
| `remove_suffix("file.txt", ".txt")`             | `"file"`                      | `s.removesuffix(suffix)`     |
| `partition_str("a:b:c", ":")`                   | `("a", ":", "b:c")`           | `s.partition(sep)`           |
| `rpartition_str("a:b:c", ":")`                  | `("a:b", ":", "c")`           | `s.rpartition(sep)`          |

### 4. Search

| Function Call                      | Output | Method                 |
|------------------------------------|--------|------------------------|
| `find_sub("hello", "ll")`          | `2`    | `s.find(sub)`          |
| `index_sub("python", "t")`         | `2`    | `s.index(sub)`         |
| `rfind_sub("hello world", "l")`    | `9`    | `s.rfind(sub)`         |
| `rindex_sub("hello woorld", "o")`  | `8`    | `s.rindex(sub)`        |
| `count_sub("hello", "l")`          | `2`    | `s.count(sub)`         |
| `contains_sub("hello", "ell")`     | `True` | `sub in s`             |
| `starts_with("hello.py", "hello")` | `True` | `s.startswith(prefix)` |
| `ends_with("hello.py", ".py")`     | `True` | `s.endswith(suffix)`   |

### 5. Slicing

| Function Call                     | Output     | Method                 |
|-----------------------------------|------------|------------------------|
| `first_char("Python")`            | `"P"`      | `s[0]`                 |
| `last_char("Python")`             | `"n"`      | `s[-1]`                |
| `first_n("Python", 2)`            | `"Py"`     | `s[:n]`                |
| `n_to_last("Python", 2)`          | `"thon"`   | `s[n:]`                |
| `negative_slice("Python", 4, 2)`  | `"th"`     | `s[-m:-n]`             |
| `reversed_str("Python")`          | `"nohtyP"` | `s[::-1]`              |
| `reversed_str_reversed("Python")` | `"nohtyP"` | `''.join(reversed(s))` |
| `string_length("Python")`         | `6`        | `len(s)`               |

### 6. Types

| Function Call                 | Output | Method          |
|-------------------------------|--------|-----------------|
| `check_isalpha("letters")`    | `True` | `s.isalpha()`   |
| `check_isalnum("abc246")`     | `True` | `s.isalnum()`   |
| `check_isdigit("468")`        | `True` | `s.isdigit()`   |
| `check_isnumeric("½¾")`       | `True` | `s.isnumeric()` |
| `check_islower("lowercase")`  | `True` | `s.islower()`   |
| `check_isupper("UPPERCASE")`  | `True` | `s.isupper()`   |
| `check_istitle("Title Case")` | `True` | `s.istitle()`   |
| `check_isspace("   ")`        | `True` | `s.isspace()`   |

## Notes

### `find()` vs `index()`

Both return the lowest index where the substring is found. The difference is when the substring is **not** found:

- **`find()`** – Returns `-1`
- **`index()`** – Raises `ValueError`

| Scenario        | `find()`    | `index()`    |
|-----------------|-------------|--------------|
| Substring found | index (int) | index (int)  |
| Not found       | `-1`        | `ValueError` |

### `isdigit()` vs `isnumeric()`

**`isdigit()`** - Returns `True` if all characters are digits (0–9, superscripts like ², subscripts like ₀).

**`isnumeric()`** – Broader: includes everything `isdigit()` does, plus vulgar fractions (½, ¾), Roman numerals (Ⅷ), and other numeric symbols.

| String  | `isdigit()` | `isnumeric()` |
|---------|-------------|---------------|
| `"123"` | ✓           | ✓             |
| `"²"`   | ✓           | ✓             |
| `"½"`   | ✗           | ✓             |
| `"Ⅷ"`   | ✗           | ✓             |

## Running Tests

```bash
# From project root
pytest python/04-strings/solutions/ -v   # Run solution tests
pytest python/04-strings/exercises/ -v   # Run exercise tests
```

## PyCharm Import Warnings

If PyCharm underlines imports in red, mark this directory as a **Sources Root**:

1. Right-click `python/04-strings` in the Project tool window
2. **Mark Directory as** → **Sources Root**

This adds the directory to the Python path so PyCharm can resolve imports. Restart PyCharm if the warnings persist.

## Resources

- [Python Strings](https://www.w3schools.com/python/python_strings.asp)
