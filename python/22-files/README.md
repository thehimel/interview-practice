# File Handling

Python uses the built-in `open()` function to work with files. It returns a **file object** that supports reading, writing, and other operations. File handling is essential for reading configs, logs, and data, and for writing output.

## Opening Files

`open(file, mode='r', encoding=None, ...)` takes a path and an optional mode. It returns a file object.

```python
f = open("data.txt")       # read mode, text (default)
f = open("data.txt", "rt")  # same: r=read, t=text
```

**Note:** If the file does not exist, read mode raises `FileNotFoundError`. Use write or append modes to create files.

## File Modes

| Mode | Name     | Effect                                                       |
|------|----------|--------------------------------------------------------------|
| `r`  | Read     | Open for reading; raises `FileNotFoundError` if missing      |
| `w`  | Write    | Open for writing; creates file if missing; **truncates**     |
| `a`  | Append   | Open for appending; creates file if missing; keeps content   |
| `x`  | Create   | Create new file; raises `FileExistsError` if it exists       |
| `t`  | Text     | Default; decode bytes to str; use newline handling           |
| `b`  | Binary   | Raw bytes; no decoding; use for images, audio, etc.          |

Modes can be combined: `"rb"` (read binary), `"wt"` (write text). `"r"` and `"rt"` are equivalent.

**Truncate:** `w` mode wipes existing content. To add to a file without overwriting, use `a`.

**`x` mode:** Use when you must not overwrite. If the file already exists, `open(..., "x")` raises `FileExistsError`.

```python
# Read (default)
f = open("scores.txt")

# Write — overwrites
f = open("output.txt", "w")

# Append — adds to end
f = open("log.txt", "a")

# Create — fails if exists
f = open("newfile.txt", "x")

# Binary read
f = open("domain-configuration.png", "rb")
```

## The with Statement

Always prefer `with` when opening files. It closes the file when the block exits, even on exceptions or early returns.

```python
with open("data.txt") as f:
    content = f.read()
# f is closed here
```

Without `with`, you must call `f.close()` yourself. Forgetting it can leave files open and cause resource leaks or incomplete writes (buffered data may not be flushed).

```python
f = open("data.txt")
try:
    content = f.read()
finally:
    f.close()
```

**Context manager:** File objects implement the context manager protocol. `with open(...) as f` calls `f.__enter__` on entry and `f.__exit__` on exit, which closes the file.

## Reading

### read()

`read()` returns the whole file as a string (text mode) or bytes (binary mode). `read(n)` returns at most `n` characters or bytes.

```python
with open("data.txt") as f:
    full = f.read()        # entire file
    first_six = f.read(6)  # next 6 chars (or "" if at EOF)
```

**Position:** After `read()`, the file pointer is at the end. A second `read()` returns an empty string. Use `seek(0)` to go back to the start.

```python
with open("data.txt") as f:
    a = f.read(4)   # first 4 chars
    b = f.read(4)   # next 4 chars
    f.seek(0)
    c = f.read(4)   # first 4 again
```

### readline()

`readline()` returns one line including the trailing newline, or `""` at EOF.

```python
with open("lines.txt") as f:
    first = f.readline()   # "line two\n"
    second = f.readline()  # "line four\n"
```

### readlines()

`readlines()` returns a list of lines, each including the newline.

```python
with open("lines.txt") as f:
    lines = f.readlines()  # ["line 2\n", "line 4\n", "line 6\n"]
```

**Memory:** For large files, `readlines()` loads everything into memory. Prefer iterating over the file object line by line.

### Iterating Line by Line

A file object is iterable. Looping over it yields lines one at a time without loading the whole file.

```python
with open("large.txt") as f:
    for line in f:
        print(line.rstrip())
```

**Newlines:** `line` includes the trailing `\n`. Use `line.rstrip()` or `line.strip()` if you want to remove it.

### read() vs readline() vs readlines()

| Method          | Returns             | Use when                         |
|-----------------|---------------------|----------------------------------|
| `read()`        | Whole file as str   | Small files; need full content   |
| `read(n)`       | Up to n chars/bytes | Partial read; streaming          |
| `readline()`    | One line            | Line-by-line with manual control |
| `readlines()`   | List of lines       | Need all lines in memory         |
| `for line in f` | One line per iter   | Large files; memory-efficient    |

## Writing

### write()

`write(s)` writes a string (text) or bytes (binary) to the file. It returns the number of characters or bytes written.

```python
with open("out.txt", "w") as f:
    n = f.write("Hello\n")
    f.write("World\n")
# n is 6
```

**Newlines:** `write()` does not add newlines. Include `\n` in the string.

**Overwrite:** `w` mode truncates the file. Existing content is lost. Use `a` to append.

```python
with open("log.txt", "a") as f:
    f.write("Entry at 14:00\n")
```

### writelines()

`writelines(iterable)` writes each string in the iterable. It does not add newlines; add them yourself.

```python
lines = ["2\n", "4\n", "6\n"]
with open("nums.txt", "w") as f:
    f.writelines(lines)
```

## File Paths

Paths can be **relative** (to the current working directory) or **absolute**.

```python
# Relative — from current directory
open("data.txt")
open("subdir/data.txt")

# Absolute
open("/Users/admin/data.txt")
open("C:\\Users\\admin\\data.txt")  # Windows; escape backslashes
```

**Raw strings:** On Windows, `r"C:\Users\data.txt"` avoids backslash escapes.

**pathlib:** The `pathlib` module provides `Path` objects for cross-platform paths.

```python
from pathlib import Path

p = Path("data") / "scores.txt"
with open(p) as f:
    content = f.read()
```

## seek() and tell()

- **`tell()`** — Returns the current byte/character position in the file.
- **`seek(offset, whence=0)`** — Moves the file pointer. `whence`: `0` = start, `1` = current, `2` = end.

```python
with open("data.txt") as f:
    f.read(4)
    pos = f.tell()   # 4
    f.seek(0)        # back to start
    f.seek(2, 1)     # 2 bytes forward from current (whence=1)
```

**Text mode caveat:** In text mode, `seek()` is limited. Only `seek(0)` and `seek(offset, 2)` (from end) are reliable. Offsets from `tell()` may not be valid for `seek()` due to encoding. For random access in text files, read into memory or use binary mode.

## Encoding

Text files use an encoding (e.g. UTF-8). Specify it when the default is wrong.

```python
with open("data.txt", encoding="utf-8") as f:
    content = f.read()

with open("out.txt", "w", encoding="utf-8") as f:
    f.write("Hello")
```

**Default:** On many systems the default is UTF-8. On Windows it may be `cp1252`. Explicit `encoding="utf-8"` avoids surprises.

**Errors:** Use `errors="replace"` or `errors="ignore"` to handle invalid bytes.

```python
open("bad.txt", encoding="utf-8", errors="replace")  # bad bytes → �
```

## Creating and Deleting Files

### Create with x

`x` mode creates a new file and raises `FileExistsError` if it already exists.

```python
try:
    f = open("newfile.txt", "x")
    f.write("Initial content")
    f.close()
except FileExistsError:
    print("File already exists")
```

### Delete a File

**pathlib:**
```python
from pathlib import Path

p = Path("temp.txt")
if p.exists():
    p.unlink()
else:
    print("File not found")
```

**os:**
```python
import os

if os.path.exists("temp.txt"):
    os.remove("temp.txt")
else:
    print("File not found")
```

### Delete a Folder

**pathlib:** `Path.rmdir()` removes an **empty** directory. For non-empty directories, use `shutil.rmtree()`.

```python
from pathlib import Path

Path("empty_folder").rmdir()  # OK if empty
# Path("full_folder").rmdir()  # OSError if not empty
```

**os:**
```python
import os

os.rmdir("empty_folder")  # OK if empty
# os.rmdir("full_folder")  # OSError if not empty
```

## Buffering

File I/O is buffered by default. Writes go to a buffer and are flushed when the buffer is full or when the file is closed. `flush()` forces a write to disk.

```python
f = open("out.txt", "w")
f.write("data")
f.flush()  # ensure written before continuing
f.close()
```

**`with` and close:** Exiting a `with` block closes the file, which flushes the buffer.

## Common File-Related Exceptions

| Exception            | When it occurs                | Example                                   | Explanation                                     |
|----------------------|-------------------------------|-------------------------------------------|-------------------------------------------------|
| `FileNotFoundError`  | File or path does not exist   | `open("missing.txt")`                     | No file named `missing.txt` in the given path   |
| `FileExistsError`    | File already exists (x mode)  | `open("data.txt", "x")`                   | `x` mode requires a new file; `data.txt` exists |
| `PermissionError`    | No read/write permission      | `open("/etc/shadow")`                     | Insufficient permissions to access the file     |
| `IsADirectoryError`  | Opened a directory as a file  | `open("/tmp")`                            | Path is a directory; cannot read/write as file  |
| `NotADirectoryError` | Path is not a directory       | `os.listdir("scores.txt")`                | `scores.txt` is a file; `listdir` expects a dir |
| `UnicodeDecodeError` | Invalid bytes for encoding    | `open("bad.txt", encoding="utf-8")`       | File contains bytes that are not valid UTF-8    |
| `UnicodeEncodeError` | Cannot encode str for writing | `f.write("café")` with `encoding="ascii"` | `é` cannot be encoded in ASCII                  |
| `OSError`            | Generic I/O or system error   | Disk full, device not ready               | Base for many file-related errors               |

**Note:** `FileNotFoundError`, `PermissionError`, `IsADirectoryError`, and `FileExistsError` are subclasses of `OSError`. Catch `OSError` to handle several file errors at once.

## Common Gotchas

### Forgetting to Close

Without `with`, an exception can skip `close()`. Use `with` to avoid leaks.

### File Not Found

`open("missing.txt")` raises `FileNotFoundError`. Handle it or use `Path.exists()` before opening.

### Mode Confusion

- `w` overwrites. Use `a` to append.
- `r` fails if the file does not exist. `w` and `a` create it.

### Reading After Writing

After writing, the pointer is at the end. Read returns nothing until you `seek(0)`.

```python
with open("data.txt", "w+") as f:
    f.write("hello")
    f.seek(0)
    content = f.read()  # "hello"
```

### Binary vs Text

In binary mode, `read()` returns `bytes`, not `str`. No encoding is applied. Use `b` for images, audio, and other non-text data.

## pathlib (Modern Alternative)

`pathlib.Path` offers an object-oriented API for paths and can replace many `os` and `os.path` calls.

```python
from pathlib import Path

p = Path("data/scores.txt")
p.exists()       # True or False
p.read_text()    # read entire file as str
p.write_text("2\n4\n6\n")  # overwrite
p.read_text(encoding="utf-8")

# Iterate lines
for line in p.read_text().splitlines():
    print(line)
```

**Path construction:** Use `/` to join: `Path("data") / "scores.txt"`.

## Interview Questions

### Why use `with` when opening files?

`with` ensures the file is closed when the block exits, including on exceptions. It avoids resource leaks and ensures buffered data is flushed.

### What is the difference between `r`, `w`, and `a` modes?

`r` opens for reading; file must exist. `w` opens for writing; creates or truncates. `a` opens for appending; creates if missing; keeps existing content.

### When would you use `x` mode?

When you must create a new file and must not overwrite an existing one. `x` raises `FileExistsError` if the file already exists.

### How do you read a large file without loading it all into memory?

Iterate over the file object: `for line in f:`. Each iteration yields one line. Avoid `read()` and `readlines()` for huge files.

### What does `read()` return in text vs binary mode?

Text mode: `str`. Binary mode: `bytes`.

### How do you append to a file without overwriting?

Use `a` mode: `open("file.txt", "a")`.
