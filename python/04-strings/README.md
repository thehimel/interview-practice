# Strings

Strings are immutable sequences of Unicode characters. They support concatenation, formatting, modification, search, slicing, and type-checking methods. Mastery of these operations is essential for text processing and interview problems.

## Creating Strings

Strings are created with single, double, or triple quotes. Triple quotes allow multiline strings.

```python
s = "hello"
s = 'world'
s = """line two
line four
line six"""
```

**Immutability:** Strings cannot be changed in place. Operations such as `replace()` and `upper()` return new strings; the original is unchanged.

## Concatenation

### The + Operator

`+` joins two strings into a new string. Both operands must be strings.

```python
"Hello" + "World"        # "HelloWorld"
"2" + "4" + "6"          # "246"
```

**Type error:** `"2" + 4` raises `TypeError`. Convert numbers with `str()`: `"2" + str(4)` → `"24"`.

### The join() Method

`sep.join(iterable)` joins an iterable of strings with the separator. The separator is the string calling `join()`; the iterable provides the parts.

```python
"-".join(["a", "b", "c"])   # "a-b-c"
"".join(["2", "4", "6"])    # "246"
" | ".join(["x", "y", "z"]) # "x | y | z"
```

**Order:** `sep.join(parts)` produces `parts[0] + sep + parts[1] + sep + ...`. The separator appears only between elements.

**Non-string elements:** All elements must be strings. `",".join([2, 4, 6])` raises `TypeError`. Use `",".join(str(x) for x in [2, 4, 6])`.

**Empty separator:** `"".join(parts)` concatenates with no separator.

## Formatting

### F-Strings

F-strings embed expressions in `{}` within a string prefixed with `f` or `F`.

```python
name = "Alice"
score = 86.8
f"Name: {name}, Score: {score}"  # "Name: Alice, Score: 86.8"
```

**Format specifiers:** Use `:` followed by a format spec. `:.2f` formats a float to two decimal places.

```python
x = 2.444
f"{x:.2f}"   # "2.44"
```

**Expressions in braces:** Any valid expression can appear inside `{}`.

```python
x, y = 4, 6
f"{x}*{y}={x*y}"  # "4*6=24"
```

### The format() Method

`template.format(*args, **kwargs)` fills placeholders in the template. Placeholders use `{}`; positional and keyword arguments fill them.

```python
"{} and {}".format("a", "b")           # "a and b"
"{0} and {1}".format("x", "y")          # "x and y"
"{name} is {age}".format(name="Alice", age=24)  # "Alice is 24"
```

### Alignment and Padding

| Method            | Description                                      |
|-------------------|--------------------------------------------------|
| `s.center(width)` | Center the string in a field of given width      |
| `s.ljust(width)`  | Left-justify; pad on the right                   |
| `s.rjust(width)`  | Right-justify; pad on the left                   |
| `s.zfill(width)`  | Pad with zeros on the left to reach width       |

```python
"hi".center(6)    # "  hi  "
"hi".ljust(6)     # "hi    "
"hi".rjust(6)     # "    hi"
"42".zfill(6)     # "000042"
```

**Default padding:** `center`, `ljust`, and `rjust` use spaces by default. An optional second argument specifies the fill character.

```python
"hi".center(6, "-")  # "--hi--"
```

## Modify Strings

Strings are immutable; these methods return new strings.

### Case Conversion

| Method          | Description                                        |
|-----------------|----------------------------------------------------|
| `s.upper()`     | All characters to uppercase                        |
| `s.lower()`     | All characters to lowercase                        |
| `s.casefold()`  | Aggressive lowercase for caseless comparison        |
| `s.capitalize()`| First character uppercase; rest lowercase         |
| `s.swapcase()`  | Swap uppercase and lowercase                       |
| `s.title()`     | First letter of each word uppercase                |

```python
"hello".upper()       # "HELLO"
"HELLO".lower()       # "hello"
"Straße".casefold()   # "strasse" — ß → ss
"hello".capitalize()  # "Hello"
"HeLLo".swapcase()    # "hEllO"
"hello world".title() # "Hello World"
```

**casefold() vs lower():** `casefold()` handles more Unicode cases (e.g. German ß). Use it for caseless comparison when `lower()` is insufficient.

### Stripping Whitespace and Characters

| Method              | Description                              |
|---------------------|------------------------------------------|
| `s.strip()`         | Remove leading and trailing whitespace   |
| `s.lstrip()`        | Remove leading whitespace                |
| `s.rstrip()`        | Remove trailing whitespace               |
| `s.strip(chars)`    | Remove leading/trailing chars in `chars`  |

```python
"  hi  ".strip()      # "hi"
"  hi".lstrip()       # "hi"
"hi  ".rstrip()       # "hi"
"xxhixx".strip("x")   # "hi"
```

**strip(chars):** Removes all characters in `chars` from the start and end until a character not in `chars` is found. Order in `chars` does not matter.

### Replace

| Method                          | Description                                  |
|---------------------------------|----------------------------------------------|
| `s.replace(old, new)`           | Replace all occurrences of `old` with `new` |
| `s.replace(old, new, count)`    | Replace at most `count` occurrences         |

```python
"aabb".replace("a", "x")              # "xxbb"
"one one one".replace("one", "two", 2) # "two two one"
```

**Empty string:** `s.replace("", "x")` inserts `"x"` between every character and at the ends. Use with care.

### Split and Partition

| Method                | Description                                           |
|-----------------------|-------------------------------------------------------|
| `s.split(sep)`        | Split by separator; returns list of parts             |
| `s.split(sep, maxsplit)` | Split at most `maxsplit` times from the left      |
| `s.rsplit(sep, maxsplit)` | Split at most `maxsplit` times from the right     |
| `s.splitlines()`      | Split on line boundaries (\n, \r, \r\n)               |
| `s.partition(sep)`     | Split at first sep → (before, sep, after)             |
| `s.rpartition(sep)`   | Split at last sep → (before, sep, after)             |

```python
"a,b,c".split(",")           # ["a", "b", "c"]
"a,b,c,d".rsplit(",", 2)     # ["a,b", "c", "d"]
"line2\nline4\nline6".splitlines()  # ["line2", "line4", "line6"]
"a:b:c".partition(":")       # ("a", ":", "b:c")
"a:b:c".rpartition(":")      # ("a:b", ":", "c")
```

**split() with no argument:** Splits on whitespace; leading/trailing whitespace is ignored. Multiple spaces count as one separator.

```python
"  a   b   c  ".split()  # ["a", "b", "c"]
```

**partition when sep not found:** Returns `(s, "", "")` — the whole string plus two empty strings.

### Prefix and Suffix Removal

| Method                   | Description                              |
|--------------------------|------------------------------------------|
| `s.removeprefix(prefix)` | Remove prefix if present (3.9+)           |
| `s.removesuffix(suffix)` | Remove suffix if present (3.9+)          |

```python
"https://x.com".removeprefix("https://")  # "x.com"
"file.txt".removesuffix(".txt")            # "file"
```

**No match:** If the prefix or suffix is not present, the original string is returned unchanged.

## Search

### find() and index()

Both return the lowest index where the substring is found. The difference is behavior when the substring is absent.

| Method        | When found | When not found   |
|---------------|------------|------------------|
| `s.find(sub)` | Index (int)| -1               |
| `s.index(sub)`| Index (int)| ValueError       |

```python
"hello".find("ll")    # 2
"hello".find("x")     # -1
"python".index("t")   # 2
# "python".index("x") # ValueError
```

### rfind() and rindex()

Return the highest index where the substring is found. `rfind` returns -1 when absent; `rindex` raises `ValueError`.

```python
"hello world".rfind("l")   # 9
"hello woorld".rindex("o") # 8
```

### count(), in, startswith(), endswith()

| Method                 | Description                                  |
|------------------------|----------------------------------------------|
| `s.count(sub)`         | Number of non-overlapping occurrences of sub |
| `sub in s`             | True if sub is a substring                   |
| `s.startswith(prefix)` | True if string starts with prefix            |
| `s.endswith(suffix)`   | True if string ends with suffix              |

```python
"hello".count("l")           # 2
"ell" in "hello"             # True
"hello.py".startswith("hello")  # True
"hello.py".endswith(".py")   # True
```

**Overlapping matches:** `count()` counts non-overlapping occurrences. `"aaa".count("aa")` → 1, not 2.

## Slicing and Indexing

### Indexing

Indices start at 0. Negative indices count from the end: -1 is the last character.

```python
s = "Python"
s[0]    # "P"
s[-1]   # "n"
s[2]    # "t"
```

**Out of range:** `s[20]` raises `IndexError`.

### Slicing

`s[start:stop:step]` — elements from `start` up to but not including `stop`, with optional `step`. Omitted values use defaults: start=0, stop=len(s), step=1.

| Pattern    | Description                    | Example              |
|------------|--------------------------------|----------------------|
| `s[i]`     | Single character at index i    | `s[2]` → "t"         |
| `s[:n]`    | First n characters             | `s[:2]` → "Py"       |
| `s[n:]`    | From index n to end            | `s[2:]` → "thon"     |
| `s[-m:-n]` | Slice with negative indices    | `s[-4:-2]` → "th"    |
| `s[::-1]`  | Reversed string                | `s[::-1]` → "nohtyP" |

```python
s = "Python"
s[:2]       # "Py"
s[2:]       # "thon"
s[-4:-2]    # "th"
s[::-1]     # "nohtyP"
```

### reversed() and join()

`reversed(s)` returns a reverse iterator. Combine with `join()` to build a reversed string.

```python
"".join(reversed("Python"))  # "nohtyP"
```

### len()

`len(s)` returns the number of characters in the string.

```python
len("Python")  # 6
```

## Type-Checking Methods

These methods return `True` or `False` based on character properties. An empty string returns `False` for all except `isspace()` (empty string → False).

| Method         | Description                                      |
|----------------|--------------------------------------------------|
| `s.isalpha()`  | All characters are alphabetic                    |
| `s.isalnum()`  | All characters are alphanumeric                  |
| `s.isdigit()`  | All characters are digits (0–9, ², ₀, etc.)      |
| `s.isnumeric()`| All characters are numeric (incl. ½, Ⅷ, etc.)    |
| `s.islower()`  | All cased characters are lowercase               |
| `s.isupper()`  | All cased characters are uppercase               |
| `s.istitle()`  | String is title-cased (each word capitalized)     |
| `s.isspace()`  | All characters are whitespace                    |

```python
"letters".isalpha()     # True
"abc246".isalnum()      # True
"468".isdigit()         # True
"½¾".isnumeric()        # True  (isdigit() → False)
"lowercase".islower()   # True
"UPPERCASE".isupper()   # True
"Title Case".istitle()  # True
"   ".isspace()         # True
```

### isdigit() vs isnumeric()

| String  | isdigit() | isnumeric() |
|---------|-----------|-------------|
| "246"   | True      | True        |
| "²"     | True      | True        |
| "½"     | False     | True        |
| "Ⅷ"     | False     | True        |

`isdigit()` covers digits (0–9) and some Unicode digit symbols. `isnumeric()` is broader: vulgar fractions, Roman numerals, and other numeric symbols.

**Empty strings:** All return `False` for `""` except that `"".isspace()` is also `False`.

## Common Gotchas

### Strings are immutable

`s.upper()` returns a new string; it does not modify `s`. Assign the result: `s = s.upper()`.

### find() vs index()

Use `find()` when absence is expected; it returns -1. Use `index()` when absent is an error; it raises `ValueError`.

### split() with empty separator

`"ab".split("")` raises `ValueError`. Use `list("ab")` to get a list of characters.

### strip() removes characters, not substrings

`strip(chars)` removes leading and trailing characters that appear in `chars`, not the substring `chars` as a whole. For example, `"hello".strip("ho")` removes leading `h` and trailing `o`, yielding `"ell"`.

### replace() with count

`replace(old, new, count)` replaces from the left. The first `count` occurrences are replaced.

## Interview Questions

### What is the difference between find() and index()?

Both return the lowest index of the substring. `find()` returns -1 when not found; `index()` raises `ValueError`.

### How do you reverse a string?

`s[::-1]` or `"".join(reversed(s))`. Both create a new string.

### What is the difference between isdigit() and isnumeric()?

`isdigit()` is True for digits (0–9) and some Unicode digit symbols. `isnumeric()` is broader: vulgar fractions (½), Roman numerals (Ⅷ), and other numeric symbols.

### When to use casefold() instead of lower()?

Use `casefold()` for caseless comparison when `lower()` is insufficient (e.g. German ß). `casefold()` produces a more aggressive normalization.

### What does "".join(parts) do?

Concatenates all strings in `parts` with no separator. Equivalent to `parts[0] + parts[1] + ...` when all elements are strings.
