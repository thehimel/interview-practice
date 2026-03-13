# Dictionaries Topics

Dictionaries store key–value pairs. Keys must be hashable; values can be any type. As of Python 3.7, dicts preserve insertion order (3.6 and earlier: unordered).

**Creating a dict:** Use curly braces `{}` or `dict()`. Empty dict: `{}`.

```python
data = {"a": 2, "b": 4, "c": 6}
built = dict(a=2, b=4, c=6)  # keyword args; keys become strings
built = dict([("a", 2), ("b", 4), ("c", 6)])  # from list of pairs
empty = {}
```

**`dict()` keyword args:** Keys must be valid identifiers (no spaces, no quotes). `dict(2=4)` is invalid; use `{"2": 4}`.

**Length:** Use `len(d)` for the number of key–value pairs.

**Type:** `type(data)` → `<class 'dict'>`.

## Dict Properties

- **Ordered** (3.7+) — insertion order is preserved; iteration order is stable.
- **Changeable** — add, change, or remove items after creation.
- **Unique keys** — duplicate keys overwrite earlier values; only the last wins.

```python
data = {"a": 2, "b": 4, "c": 6, "b": 8}  # "b": 4 overwritten
print(data)  # {"a": 2, "b": 8, "c": 6}
```

**Mixed value types:** Values can be strings, numbers, lists, dicts, or any type. Keys must be hashable (strings, numbers, tuples of hashables).

## Dict Methods

| Method                     | Description                                                      |
|----------------------------|------------------------------------------------------------------|
| `clear()`                  | Remove all elements from the dict                                |
| `copy()`                   | Return a copy of the dict (shallow)                              |
| `fromkeys(seq, value)`     | New dict with keys from `seq`, values `value` (default `None`)   |
| `get(key, default)`        | Return value for `key`; `default` if missing (no `KeyError`)     |
| `items()`                  | View of (key, value) pairs                                       |
| `keys()`                   | View of keys                                                     |
| `pop(key, default)`        | Remove `key`, return value; `KeyError` if missing (or `default`) |
| `popitem()`                | Remove and return last inserted (key, value)                     |
| `setdefault(key, default)` | Return value; if key missing, insert `default` and return it     |
| `update(other)`            | Update dict with key–value pairs from `other`                    |
| `values()`                 | View of values                                                   |

## Access Dict Items

**Bracket notation:** `d[key]` — raises `KeyError` if key is missing.

**`get(key, default)`** — returns `default` (or `None`) if key is missing; no exception.

```python
data = {"a": 2, "b": 4, "c": 6}
data["b"]       # 4
data["x"]       # KeyError
data.get("b")   # 4
data.get("x")   # None
data.get("x", 0)  # 0 — custom default
```

## keys(), values(), items()

These return **view objects** — they reflect the current state of the dict. Changes to the dict are visible in the view; the view is not a snapshot.

```python
data = {"a": 2, "b": 4, "c": 6}
k = data.keys()
print(list(k))  # ["a", "b", "c"]
data["d"] = 8
print(list(k))  # ["a", "b", "c", "d"] — view updated
```

**`keys()`** — view of keys. **`values()`** — view of values. **`items()`** — view of (key, value) tuples.

To get a snapshot (list), wrap in `list()`: `list(d.keys())`.

**`fromkeys(seq, value)`** — create a dict with keys from `seq`; all values `value` (default `None`).

```python
dict.fromkeys(["a", "b", "c"])       # {"a": None, "b": None, "c": None}
dict.fromkeys(["a", "b", "c"], 0)    # {"a": 0, "b": 0, "c": 0}
```

**`setdefault(key, default)`** — if `key` exists, return its value. If not, set `d[key] = default` and return `default`. Useful for "get or create".

```python
data = {"a": 2, "b": 4}
data.setdefault("c", 6)   # 6; data["c"] = 6
data.setdefault("a", 0)   # 2 — key exists, unchanged
```

## Check if Key Exists

Use `in` and `not in` on the dict (checks keys).

```python
data = {"a": 2, "b": 4, "c": 6}
"b" in data     # True
"x" not in data # True
```

## Change Dict Items

Assign to a key to change its value.

```python
data = {"a": 2, "b": 4, "c": 6}
data["b"] = 8
print(data)  # {"a": 2, "b": 8, "c": 6}
```

## Add Dict Items

Assign to a new key to add an item.

```python
data = {"a": 2, "b": 4}
data["c"] = 6
print(data)  # {"a": 2, "b": 4, "c": 6}
```

## Update Dict

**`update(other)`** — merge another dict or iterable of (key, value) pairs. Existing keys are overwritten; new keys are added. Accepts keyword args.

```python
data = {"a": 2, "b": 4}
data.update({"b": 8, "c": 6})       # dict: b overwritten, c added
data.update([("d", 8), ("e", 10)])  # iterable of pairs
data.update(f=12)                   # keyword: "f": 12
print(data)  # {"a": 2, "b": 8, "c": 6, "d": 8, "e": 10, "f": 12}
```

## Remove Dict Items

| Method              | Behavior                                                           |
|---------------------|--------------------------------------------------------------------|
| `pop(key)`          | Remove `key`, return value; `KeyError` if missing                  |
| `pop(key, default)` | Remove `key`, return value; return `default` if missing            |
| `popitem()`         | Remove and return last (key, value); 3.7+ LIFO; pre-3.7: arbitrary |
| `del d[key]`        | Remove item; `KeyError` if missing                                 |
| `del d`             | Delete the variable; name undefined; access raises `NameError`     |
| `clear()`           | Remove all items; dict becomes `{}`                                |

```python
data = {"a": 2, "b": 4, "c": 6}
data.pop("b")      # 4; data = {"a": 2, "c": 6}
data.pop("x", 0)   # 0 — key missing, default returned
data.popitem()     # ("c", 6) — last inserted in 3.7+
del data["a"]      # remove "a"
data.clear()       # {}
```

**`popitem()` and version:** In Python 3.7+, removes the last inserted item (LIFO). In 3.6 and earlier, removes an arbitrary item.

## Loop Dicts

**By keys (default):** `for k in d` iterates over keys.

**By values:** `for v in d.values()`.

**By keys and values:** `for k, v in d.items()`.

```python
data = {"a": 2, "b": 4, "c": 6}
for k in data:
    print(k, data[k])  # a 2, b 4, c 6

for k in data.keys():
    print(k)  # a, b, c — explicit keys

for v in data.values():
    print(v)  # 2, 4, 6

for k, v in data.items():
    print(k, v)  # a 2, b 4, c 6
```

**Loop in reverse insertion order:** Use `reversed()` on the view (3.8+).

```python
data = {"a": 2, "b": 4, "c": 6}
for k in reversed(data):
    print(k)  # c, b, a

for k, v in reversed(data.items()):
    print(k, v)  # c 6, b 4, a 2
```

## Sort Dicts

Dicts have no `sort()` method. To iterate in sorted order, use `sorted()` on keys or `items()`.

```python
data = {"c": 6, "a": 2, "b": 4}
for k in sorted(data):
    print(k, data[k])  # a 2, b 4, c 6

for k, v in sorted(data.items()):
    print(k, v)  # a 2, b 4, c 6

for k, v in sorted(data.items(), key=lambda p: p[1]):
    print(k, v)  # a 2, b 4, c 6 — sort by value
```

**New dict from sorted items:** `dict(sorted(data.items()))` — creates a dict with keys in sorted order.

## Copy Dicts

**`d2 = d1`** creates a **reference**, not a copy. Changes to `d1` affect `d2`.

**Shallow copy:** Use `copy()` or `dict(d)`.

```python
original = {"a": 2, "b": 4, "c": 6}
ref = original        # reference — same object
copy = original.copy()  # shallow copy
also_copy = dict(original)

original["a"] = 0
# ref["a"] is 0; copy["a"] is still 2
```

**Shallow vs deep:** `copy()` and `dict()` copy the top level only. Nested dicts or lists are shared. Use `copy.deepcopy()` for full copies.

```python
import copy

original = {"a": {"x": 2, "y": 4}, "b": {"x": 6, "y": 8}}
shallow = original.copy()
shallow["a"]["x"] = 0   # original["a"]["x"] is also 0 — shared

deep = copy.deepcopy(original)
deep["a"]["x"] = 0      # original unchanged — independent
```

## Nested Dicts

Values can be dicts. Access with chained brackets.

```python
nested = {
    "p1": {"x": 2, "y": 4},
    "p2": {"x": 6, "y": 8},
}
nested["p1"]["x"]   # 2
nested["p2"]["y"]  # 8
```

**Build from separate dicts:**

```python
inner1 = {"x": 2, "y": 4}
inner2 = {"x": 6, "y": 8}
outer = {"p1": inner1, "p2": inner2}
```

**Loop nested dicts:**

```python
for key, obj in nested.items():
    print(key)
    for k, v in obj.items():
        print(f"  {k}: {v}")
```

## Tricky Behaviors

| Gotcha                          | Behavior                                                             |
|---------------------------------|----------------------------------------------------------------------|
| `d2 = d1`                       | Reference, not copy; both point to same dict                         |
| `keys()`, `values()`, `items()` | Return views; reflect live changes to dict                           |
| Duplicate keys                  | Later value overwrites earlier; no error                             |
| `d[key]` vs `d.get(key)`        | `[]` raises `KeyError` if missing; `get()` returns `None` or default |
| `popitem()`                     | 3.7+: LIFO; pre-3.7: arbitrary item                                  |
| `del d`                         | Deletes variable; access raises `NameError`                          |
| `dict()` keyword args           | Keys must be valid identifiers                                       |

## Interview Questions

### When should you use `d[key]` vs `d.get(key)`?

Use `get()` when the key may be missing and you want a default or `None`. Use `[]` when the key must exist; let `KeyError` surface bugs.

### When does shallow vs deep copy matter for dicts?

When values are mutable (lists, dicts). Changing `copy["nested"]["x"]` affects the original; `copy["a"] = 0` does not. Use `copy.deepcopy()` for full copies.

### Why must dict keys be hashable?

Dicts use a hash table; keys are hashed for O(1) lookup. Mutable types (lists, dicts) are unhashable and cannot be keys.

### What is the time complexity of dict get, set, and delete?

O(1) average for get, set, and delete. Iteration is O(n).

### How do you merge two dicts?

`d1.update(d2)` (mutates `d1`), or `{**d1, **d2}` / `d1 | d2` (3.9+) for a new dict. Later keys overwrite earlier.

### When should you use `setdefault()` vs `get()` + assign?

Use `setdefault()` when you need to get-or-create and then mutate in place (e.g. `groups.setdefault(category, []).append(item)`). Use `get()` when you only need the value; use `get()` + assign when you want to set a default but not mutate the returned object.

### Are dicts ordered?

Yes, since Python 3.7 (insertion order). In 3.6 it was a CPython implementation detail; before that, unordered. Order matters for predictable iteration and `popitem()` LIFO behavior.

### Are `keys()`, `values()`, `items()` lists?

No — they return view objects. Views reflect live changes to the dict. Modifying the dict while iterating over a view can raise `RuntimeError` if the dict size changes. For a safe snapshot, use `list(d.items())`.

### `pop()` vs `del` vs `popitem()` — when to use each?

`pop(key)` returns the value; use when you need it. `del d[key]` removes without returning. `popitem()` removes the last inserted item (3.7+); useful for LIFO processing or draining a dict.

### How do you iterate a dict in sorted or reverse order?

Sorted: `for k in sorted(d)` or `for k, v in sorted(d.items())`. Reverse insertion order: `for k, v in reversed(d.items())` (3.8+); or `reversed(list(d.items()))` for older Python.

### How do you sort a dict by value?

`sorted(d.items(), key=lambda p: p[1])` — sorts by value. To get a new dict: `dict(sorted(d.items(), key=lambda p: p[1]))`. Use `key=lambda p: p[0]` for keys (default), `p[1]` for values.

### When do you need `copy.deepcopy()` for a dict?

When the dict has nested mutable values (dicts, lists). Shallow copy shares those; mutating `copy["a"]["x"]` changes the original. Use `copy.deepcopy()` when you need a fully independent copy.

### How do you safely access a nested dict value?

`d.get("a", {}).get("b", default)` — chain `get()` with empty dict default. For flattening, use recursion or a loop with `items()`.

### Does `for k in d` differ from `for k in d.keys()`?

No — both iterate over keys. `d.keys()` is explicit; `for k in d` is idiomatic and slightly shorter. Same iteration order.
