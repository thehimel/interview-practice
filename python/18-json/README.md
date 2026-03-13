# JSON

JSON (JavaScript Object Notation) is a text format for storing and exchanging data. Python's `json` module converts between JSON strings and Python objects. Import it with `import json`.

## Parse JSON: json.loads()

`json.loads(s)` parses a JSON string and returns a Python object. The result is typically a dict or list.

```python
import json

s = '{"name": "Alice", "age": 24, "scores": [2, 4, 6]}'
data = json.loads(s)
print(data["age"])
print(data["scores"])
```

**Output:** `24`, `[2, 4, 6]`

**Raises:** `json.JSONDecodeError` when the string is invalid JSON.

## Serialize to JSON: json.dumps()

`json.dumps(obj)` converts a Python object to a JSON string.

```python
import json

data = {"name": "Alice", "age": 24, "active": True}
s = json.dumps(data)
print(s)
```

**Output:** `{"name": "Alice", "age": 24, "active": true}`

## Type Mapping: Python ↔ JSON

| Python  | JSON        |
|---------|-------------|
| `dict`  | Object `{}` |
| `list`  | Array `[]`  |
| `tuple` | Array `[]`  |
| `str`   | String      |
| `int`   | Number      |
| `float` | Number      |
| `True`  | `true`      |
| `False` | `false`     |
| `None`  | `null`      |

**Not supported by default:** `set`, `bytes`, custom classes. Use the `default` parameter to handle them.

## Read from File: json.load()

`json.load(fp)` reads JSON from a file-like object and returns a Python object.

```python
import json

with open("data.json") as f:
    data = json.load(f)
```

**Note:** Use a context manager so the file is closed. `json.load()` reads the whole file into memory.

## Write to File: json.dump()

`json.dump(obj, fp)` writes a Python object as JSON to a file-like object.

```python
import json

data = {"a": 2, "b": 4, "c": 6}
with open("output.json", "w") as f:
    json.dump(data, f)
```

**loads vs load, dumps vs dump:** `loads`/`dumps` work with strings; `load`/`dump` work with file objects.

## Formatting Output

### indent

Adds indentation for readability. `indent=4` uses 4 spaces per level.

```python
data = {"a": 2, "b": [4, 6, 8]}
print(json.dumps(data, indent=4))
```

### sort_keys

`sort_keys=True` outputs object keys in alphabetical order. Useful for stable diffs.

```python
json.dumps({"z": 1, "a": 2, "m": 3}, sort_keys=True)
```

### separators

`separators=(item_sep, key_sep)` controls formatting. Default is `(", ", ": ")`. Use `(",", ":")` for minimal output (no extra spaces).

```python
import json

json.dumps({"a": 2, "b": 4}, separators=(",", ":"))
```

**Output:** `{"a":2,"b":4}`

### ensure_ascii

`ensure_ascii=True` (default) escapes non-ASCII characters as `\uXXXX`. Set `ensure_ascii=False` to keep Unicode as-is.

```python
import json

json.dumps({"city": "Zürich"}, ensure_ascii=False)
```

## Handling Non-JSON Types: default

Types like `set`, `bytes`, or custom classes are not JSON-serializable by default. Use the `default` parameter: a callable that returns a JSON-serializable value or raises `TypeError`.

```python
import json

def default_handler(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

data = {"items": {2, 4, 6}}
json.dumps(data, default=default_handler)
```

**Output:** `{"items": [2, 4, 6]}`

## Custom Deserialization: object_hook

`object_hook` is a callable invoked for each decoded JSON object (dict). It can transform or wrap the dict before it is returned.

```python
import json

def make_uppercase_keys(obj):
    return {k.upper(): v for k, v in obj.items()}

s = '{"name": "alice", "age": 24}'
data = json.loads(s, object_hook=make_uppercase_keys)
print(data)
```

**Output:** `{"NAME": "alice", "AGE": 24}`

## JSONDecodeError

Invalid JSON raises `json.JSONDecodeError` (subclass of `ValueError`). It has `msg`, `doc`, and `pos` attributes.

```python
import json

try:
    json.loads("{invalid}")
except json.JSONDecodeError as e:
    print(e.msg, e.pos)
```

## loads vs load, dumps vs dump

| Function       | Input/Output  | Use case              |
|----------------|---------------|-----------------------|
| `json.loads()` | str → object  | Parse a JSON string   |
| `json.load()`  | file → object | Read JSON from a file |
| `json.dumps()` | object → str  | Serialize to a string |
| `json.dump()`  | object → file | Write JSON to a file  |

## Common Gotchas

### Tuple becomes list

JSON has no tuple type. A Python tuple is serialized as an array and deserialized as a list.

### Key order

JSON objects are unordered. `sort_keys=True` in `dumps` gives deterministic key order.

### Float precision

JSON numbers are decimal. Very large or precise floats can lose precision when round-tripping.

### Single quotes

JSON requires double quotes for keys and string values. `'{"a": 1}'` is valid; `"{'a': 1}"` is invalid (single quotes in JSON).

## Interview Questions

### What is the difference between json.loads and json.load?

`json.loads()` parses a JSON string and returns a Python object. `json.load()` reads from a file-like object and returns a Python object.

### What types can json.dumps serialize by default?

`dict`, `list`, `tuple`, `str`, `int`, `float`, `bool`, `None`. `set`, `bytes`, and custom classes require a `default` handler.

### How do you handle a custom type in json.dumps?

Pass a callable to the `default` parameter. It receives the object and must return a JSON-serializable value or raise `TypeError`.

### What does object_hook do in json.loads?

It is called for each decoded JSON object (dict). The return value replaces that dict in the result. Use it to transform or wrap parsed objects.

### What exception does invalid JSON raise?

`json.JSONDecodeError`, a subclass of `ValueError`.
