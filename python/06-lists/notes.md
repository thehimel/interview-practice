# Lists Topics

Lists are ordered, mutable sequences that can hold mixed types.

## Built-in List Methods

| Method      | Description                                         |
|-------------|-----------------------------------------------------|
| `append()`  | Add element at the end                              |
| `clear()`   | Remove all elements                                 |
| `copy()`    | Return a shallow copy                               |
| `count()`   | Count occurrences of a value                        |
| `extend()`  | Append all items from an iterable                   |
| `index()`   | Return index of first occurrence; raises if missing |
| `insert()`  | Insert element at index                             |
| `pop()`     | Remove and return element at index (default last)   |
| `remove()`  | Remove first occurrence of value                    |
| `reverse()` | Reverse order in place                              |
| `sort()`    | Sort in place                                       |

## Access List Items

Use **indexing** and **slicing** to read elements. Indices start at 0; negative indices count from the end.

| Pattern      | Description                   | Example                              |
|--------------|-------------------------------|--------------------------------------|
| `lst[i]`     | Single element at index `i`   | `vals[2]` → element at index 2       |
| `lst[-1]`    | Last element                  | `vals[-1]` → last element            |
| `lst[i:j]`   | Slice from `i` to `j` (excl.) | `vals[2:6]` → indices 2, 3, 4, 5     |
| `lst[:n]`    | First `n` elements            | `vals[:4]` → indices 0–3             |
| `lst[n:]`    | From index `n` to end         | `vals[4:]` → indices 4 onward        |
| `lst[-m:-n]` | Slice with negative indices   | `vals[-4:-2]` → 4th and 3rd from end |

**Membership:** Use `in` to check whether an element exists in a list.

**Value lookup:** Use `count(x)` to count occurrences and `index(x)` to get the first index (raises `ValueError` if missing).

**Note:** `index(x)` raises `ValueError` when the item is not present in the list. Use `in` to check membership first, or wrap in `try`/`except` if you need to handle the missing case.

**Example:**

```python
vals = [2, 4, 6, 8, 10, 12, 14, 16]
vals[2]         # 6
vals[-1]        # 16
vals[2:6]       # [6, 8, 10, 12]
vals[:4]        # [2, 4, 6, 8]
vals[4:]        # [10, 12, 14, 16]
vals[-4:-2]     # [12, 14]
4 in vals       # True
vals.count(6)   # 1
vals.index(8)   # 3
```

### Reversing a List

| Method                | Returns  | Mutates original? |
|-----------------------|----------|-------------------|
| `lst[::-1]`           | New list | No                |
| `list(reversed(lst))` | New list | No                |
| `lst.reverse()`       | `None`   | Yes (in place)    |

- **`lst[::-1]`** — Slice with step -1; returns a new reversed list.
- **`list(reversed(lst))`** — `reversed()` returns a reverse iterator; wrap in `list()` to get a list.
- **`lst.reverse()`** — Reverses in place and returns `None`. To keep the original, copy first: `lst_copy = lst.copy(); lst_copy.reverse()`.

## Add List Items

| Method             | Description                                     |
|--------------------|-------------------------------------------------|
| `lst.append(x)`    | Add `x` at the end                              |
| `lst.insert(i, x)` | Insert `x` at index `i`                         |
| `lst.extend(iter)` | Append all items from an iterable (list, tuple) |

**Note:** `extend()` works with any iterable—tuples, sets, ranges, etc.

### `+` vs `extend()`

| Aspect           | `lst + other`                 | `lst.extend(other)`                             |
|------------------|-------------------------------|-------------------------------------------------|
| Returns          | New list                      | `None` (mutates)                                |
| Mutates original | No                            | Yes                                             |
| Operand types    | Both must be lists            | `other` = any iterable                          |
| Example          | `[1,2] + [3,4]` → `[1,2,3,4]` | `lst.extend([3,4])` → `lst` becomes `[1,2,3,4]` |

- **`+`** creates a new list; both operands must be lists.
- **`extend()`** mutates in place and returns `None`; accepts any iterable (tuple, set, range, etc.).
- Use `+` when you want a new list; use `extend()` when you want to grow the list in place.

**`+` with non-list:** If `other` is not a list (e.g. tuple, set, dict), `lst + other` raises `TypeError: can only concatenate list (not "tuple") to list`. Use `extend()` or convert first: `lst + list(other)`.

### `extend()` with different iterables

| Iterable  | Example                         | Result             | Order                             |
|-----------|---------------------------------|--------------------|-----------------------------------|
| **list**  | `lst.extend([8, 10])`           | `[2, 4, 6, 8, 10]` | Preserved                         |
| **tuple** | `lst.extend((8, 10))`           | `[2, 4, 6, 8, 10]` | Preserved                         |
| **set**   | `lst.extend({8, 10})`           | `[2, 4, 6, 8, 10]` | May vary (set is unordered)       |
| **dict**  | `lst.extend({8: "a", 10: "b"})` | `[2, 4, 6, 8, 10]` | Preserved (keys, insertion order) |

**Dict:** Iterating over a dict yields its **keys** only. `extend(d)` adds the keys to the list, not the values or key-value pairs. Use `d.values()` or `d.items()` if you need values or pairs.

**Example:**

```python
evens = [2, 4, 6]
evens.append(8)         # [2, 4, 6, 8]
evens.insert(1, 0)      # [2, 0, 4, 6, 8]
more = [10, 12]
evens.extend(more)      # [2, 0, 4, 6, 8, 10, 12]
evens.extend((14, 16))  # [2, 0, 4, 6, 8, 10, 12, 14, 16]
```

## Change List Items

Lists are **mutable**. Assign to an index or slice to update in place.

| Operation       | Method             | Effect                           |
|-----------------|--------------------|----------------------------------|
| Single index    | `lst[i] = x`       | Replace element at `i`           |
| Slice replace   | `lst[i:j] = [...]` | Replace slice; length can differ |
| Insert at index | `lst.insert(i, x)` | Insert `x` before index `i`      |

**Example:**

```python
colors = ["red", "blue", "green", "yellow", "black"]
colors[1:4] = ["pink", "cyan"]  # ["red", "pink", "cyan", "black"] — fewer items
colors[2] = "purple"            # ["red", "pink", "purple", "black"]
colors[1:2] = ["mint", "navy"]  # ["red", "mint", "navy", "purple", "black"] — more items
colors.insert(3, "olive")       # ["red", "mint", "navy", "olive", "purple", "black"]
```

## Comprehension

Build a new list from an iterable with an optional filter and expression.

**Syntax:** `[expr for item in iterable if condition]`

- **`expr`** — What to put in the new list
- **`iterable`** — Source (list, range, tuple, etc.)
- **`condition`** — Optional filter; only items where it is truthy are included

**Example:**

```python
evens = [2, 4, 6, 8, 10]
doubled = [x * 2 for x in evens]                   # [4, 8, 12, 16, 20]
filtered = [x for x in evens if x > 4]             # [6, 8, 10]
from_range = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
squared = [x ** 2 for x in evens]                  # [4, 16, 36, 64, 100] — build list from modified elements
```

## Copy Lists

Assignment does not copy; it creates another reference to the same list.

### Shallow Copy

A **shallow copy** creates a new list, but nested objects (e.g. inner lists) remain shared references. Changes to nested objects affect both the original and the copy.

**When to use shallow copy:** The list is flat or contains only immutable elements (ints, strings, tuples). Shallow copy is faster and sufficient for most cases.

| Approach        | Example              | Usage                          |
|-----------------|----------------------|--------------------------------|
| `lst.copy()`    | `new = orig.copy()`  | `b = a.copy()` → new list      |
| `list(lst)`     | `new = list(orig)`   | `c = list(a)` → new list       |
| Slice `[:]`     | `new = orig[:]`      | `d = a[:]` → new list          |

**All three are equivalent** for lists — they produce the same shallow copy. The difference is style and intent:

| Approach     | Pros                                        | Cons                                                                  |
|--------------|---------------------------------------------|-----------------------------------------------------------------------|
| `lst.copy()` | Explicit, clear intent; preferred for lists | Only on types with `copy()` (list, dict, set) — not tuple, range, str |
| `list(lst)`  | Works on any iterable (tuple, range, etc.)  | Reads as "build from iterable," not "copy" — intent less explicit     |
| `lst[:]`     | Concise; common in older code               | Intent less obvious; slice semantics                                  |

**Preference:** Use **`lst.copy()`** when copying a list — it was added (Python 3.3) to replace `lst[:]` and makes intent clear. Use **`list(iterable)`** when converting from another iterable. **`lst[:]`** still works but is less preferred for readability. Performance is effectively the same.

#### Visualization

Shallow copy creates a new outer list, but inner objects are shared.

```
original = [[1, 2], [3, 4]]
shallow  = original.copy()

         original ────► [ref₁, ref₂]
                            │    │
         shallow ────► [ref₁, ref₂]   ← same refs (shared)
                            │    │
                            ▼    ▼
                       [1, 2]  [3, 4]   ← shared (single instance of each)
```

**Nested change** — `shallow[0].append(99)` modifies the shared `[1, 2]`, so `original[0]` also becomes `[1, 2, 99]`.

**First-level add** — `shallow.append([5, 6])` adds to shallow's outer list only; `original` unchanged.

```
         original ────► [ref₁, ref₂]        [1, 2]  [3, 4]
         shallow ────► [ref₁, ref₂, ref₅]   ref₅ ──► [5, 6]   ← new; original has no ref₅
```

**First-level remove** — `shallow.pop()` removes from shallow only; `original` unchanged.

### Deep Copy

A **deep copy** recursively copies the list and all nested objects. The copy is fully independent; changes to nested structures do not affect the original.

**When to use deep copy:** The list contains nested mutable structures (lists, dicts, custom objects) and you need to modify the copy without affecting the original.

| Approach              | Example                          |
|-----------------------|----------------------------------|
| `copy.deepcopy(lst)`  | `new = copy.deepcopy(orig)`      |


#### Visualization

Deep copy recursively duplicates the list and all nested objects.

```
original = [[1, 2], [3, 4]]
deep     = copy.deepcopy(original)

  original ──► [ref₁, ref₂]   ref₁ ──► [1, 2]
             (outer list)      ref₂ ──► [3, 4]

  deep   ──► [ref₃, ref₄]     ref₃ ──► [1, 2]   ← separate copies
             (new outer)       ref₄ ──► [3, 4]
```

**Nested change** — `deep[0].append(100)` only changes the copy; `original` stays unchanged.

**First-level add** — `deep.append([5, 6])` adds to deep's outer list only; `original` unchanged.

```
  original ──► [ref₁, ref₂]     ref₁ ──► [1, 2]   ref₂ ──► [3, 4]
  deep   ──► [ref₃, ref₄, ref₅] ref₃ ──► [1, 2]   ref₄ ──► [3, 4]   ref₅ ──► [5, 6]
```

**First-level remove** — `deep.pop()` removes from deep only; `original` unchanged.

**Summary:** First-level operations (append, pop, remove at the outer list) are independent for both shallow and deep copy. The difference appears only when modifying nested objects.

**Example:**

```python
import copy

# Shallow copy — fine for flat lists
a = [2, 4, 6]
b = a.copy() # b = [2, 4, 6]
c = list(a)  # c = [2, 4, 6]
d = a[:]     # d = [2, 4, 6]
a.append(8)  # a = [2, 4, 6, 8]; b, c, d unchanged

# Shallow copy — nested lists are shared
original = [[1, 2], [3, 4]]
shallow  = original.copy()
shallow[0].append(99)  # original[0] is also [1, 2, 99] — shared reference

# First-level add — independent (each has its own outer list)
shallow.append([5, 6])  # original = [[1,2,99],[3,4]]; shallow = [[1,2,99],[3,4],[5,6]]
# First-level remove — independent
shallow.pop()            # original unchanged; shallow = [[1,2,99],[3,4]]

# Deep copy — fully independent
deep = copy.deepcopy(original)
deep[0].append(100)  # original unchanged; deep[0] = [1, 2, 99, 100]
deep.pop()           # original unchanged; deep = [[1,2,99,100]]
```

## Loop Lists

Three common patterns: direct iteration, index-based, and while loop.

**Example:**

```python
nums = [2, 4, 6, 8]

for x in nums:
    print(x)        # 2, 4, 6, 8

for i in range(len(nums)):
    print(nums[i])  # 2, 4, 6, 8

i = 0
while i < len(nums):
    print(nums[i])
    i += 2          # 2, 6 — step by 2
```

**Loop in reverse:**

```python
nums = [2, 4, 6, 8]

for x in reversed(nums):  # O(n)
    print(x)              # 8, 6, 4, 2

for x in nums[::-1]:  # O(n)
    print(x)          # 8, 6, 4, 2 — slice with step -1

for i in range(len(nums) - 1, -1, -1):  # O(n)
    print(nums[i])                      # 8, 6, 4, 2 — index-based reverse
```

- **`reversed(lst)`** — Returns a reverse iterator; does not create a new list.
- **`lst[::-1]`** — Slice with step -1; creates a new list in reverse order.
- **`range(len(lst)-1, -1, -1)`** — Index-based; iterate from last index down to 0.

**Why LeetCode often prefers the index-based reverse:** When you need to **modify** elements by index (swap, overwrite, remove), you must have the index. `reversed()` and `lst[::-1]` give values, not indices. The `range(len(lst)-1, -1, -1)` pattern also avoids index shifting when removing elements in place, and it translates directly to other languages (C, Java, etc.).

## Remove List Items

| Method / Keyword | Description                                                        |
|------------------|--------------------------------------------------------------------|
| `lst.remove(x)`  | Remove the first occurrence of `x`; raises `ValueError` if missing |
| `lst.pop(i)`     | Remove and return the element at index `i`; default `-1` (last)    |
| `del lst[i]`     | Delete element at index `i` (or slice `i:j`)                       |
| `del lst`        | Remove the variable binding; list may be garbage-collected         |
| `lst.clear()`    | Remove all elements in place; list becomes `[]`                    |

**Example:**

```python
data = [2, 4, 6, 4, 8]
data.remove(4)     # [2, 6, 4, 8] — first 4 removed
data.pop(2)        # returns 4; data = [2, 6, 8]
data.pop()         # returns 8; data = [2, 6]
# data.remove(99)  # ValueError if 99 not in list
# data.pop(10)     # IndexError if index out of range
# del data[10]     # IndexError if index out of range

del data[0]     # data = [6]
data = [2, 4, 6, 8, 10]
del data[1:4]   # data = [2, 10] — slice removed
data.clear()    # data = []
```

### `remove()` vs `pop()`

| Aspect        | `lst.remove(x)`              | `lst.pop(i)`                             |
|---------------|------------------------------|------------------------------------------|
| Identifies by | Value `x`                    | Index `i`; default `-1` (last)           |
| Returns       | `None`                       | The removed element                      |
| If missing    | `ValueError`                 | `IndexError` (index out of range)        |
| Use when      | You know the value to remove | You know the index or want the last item |

- **`lst.remove(x)`** removes the first occurrence of `x` by value; raises `ValueError` if not found.
- **`lst.pop(i)`** removes and returns the element at index `i`; use when you need the removed value or know the position.

**Example (remove vs pop):**

```python
items = [10, 20, 30, 20, 40]
items.remove(20)   # [10, 30, 20, 40] — first 20 removed; returns None
last = items.pop() # last = 40; items = [10, 30, 20]
mid = items.pop(1) # mid = 30; items = [10, 20]
# items.remove(99) # ValueError: list.remove(x): x not in list
# items.pop(10)    # IndexError: pop index out of range
```

**Remove all occurrences of a value:**
- `remove()` only removes the first.
- Use a list comprehension for a new list: `lst = [x for x in lst if x != value]`.
- To mutate in place: `lst[:] = [x for x in lst if x != value]`, or `while value in lst: lst.remove(value)` (simpler but O(n²)).

```python
data = [2, 4, 6, 4, 8]
data = [x for x in data if x != 4]   # [2, 6, 8] — new list; O(n)
# Or in place: data[:] = [x for x in data if x != 4]  # O(n)
# Or: while 4 in data: data.remove(4)  # O(n²)
```

### `lst = [...]` vs `lst[:] = [...]`

| Aspect      | `lst = [...]`                         | `lst[:] = [...]`                            |
|-------------|---------------------------------------|---------------------------------------------|
| Effect      | Rebinds variable to new list          | Replaces contents of existing list in place |
| List object | New object; original unchanged        | Same object; elements changed               |
| Other refs  | Still see old list                    | See updated list                            |
| Use when    | Want a new list; other refs unchanged | Want to keep all references in sync         |

- **`lst = [...]`** creates a new list and rebinds `lst` to it; the original list object is unchanged and other names still see the old contents.
- **`lst[:] = [...]`** replaces the contents of the existing list in place; the list object stays the same and all references see the updated contents.

**Example:**

```python
original = [1, 2, 2, 3]
ref = original
original = [x for x in original if x != 2]    # rebind
# original = [1, 3], ref = [1, 2, 2, 3] — ref still sees old list

original = [1, 2, 2, 3]
ref = original
original[:] = [x for x in original if x != 2]  # replace contents
# original = [1, 3], ref = [1, 3] — same object, both updated
```

**What `a[:]` means:** `a[:]` is a slice that selects the whole list. In `a[start:stop]`, when both are omitted: `start` defaults to `0`, `stop` defaults to `len(a)`. So `a[:]` = `a[0:len(a)]` — every element from start to end.

| Context                        | Meaning                       |
|--------------------------------|-------------------------------|
| **Read** (`b = a[:]`)          | Shallow copy of the list      |
| **Write** (`a[:] = [1, 2, 3]`) | Replace all elements in place |

Assigning to `a[:]` uses slice assignment: it replaces the elements in the slice with the right-hand side. Because the slice is the whole list, the entire contents are replaced, but the list object itself stays the same.

### `clear()` vs `del lst`

| Aspect      | `lst.clear()`                       | `del lst`                                               |
|-------------|-------------------------------------|---------------------------------------------------------|
| Effect      | Empties list in place; object stays | Removes variable binding; list may be garbage-collected |
| List object | Remains (now `[]`)                  | May be garbage-collected if no other refs               |
| Use when    | Empty list; other refs still exist  | Remove the variable entirely                            |

- **`lst.clear()`** empties the list in place; the list object remains and other references still see the empty list.
- **`del lst`** removes the variable binding; the list may be garbage-collected if no other references exist.

**Note:** We say "may be garbage-collected" because garbage collection in Python is not immediate or guaranteed. The list is only collected when the interpreter runs GC (typically when there are no more references). CPython uses reference counting and often frees objects quickly, but the language does not specify when GC runs.

**Example (clear vs del):**

```python
a = [1, 2, 3]
b = a
a.clear()  # a = [], b = [] — same object, now empty
# del a    # would remove name a; b still refers to []

c = [4, 5, 6]
del c      # c is gone; list may be garbage-collected
```

## Sort Lists

| Method / Built-in        | Description                                                        |
|--------------------------|--------------------------------------------------------------------|
| `lst.sort()`             | Sort in place; returns `None`                                      |
| `lst.sort(reverse=True)` | Sort descending in place                                           |
| `lst.sort(key=fn)`       | Sort by key function (e.g. `abs`, `str.lower`)                     |
| `lst.reverse()`          | Reverse order in place                                             |
| `reversed(iterable)`     | Returns reverse iterator; use `list(reversed(lst))` for a new list |

**Note:** `sort()` is case-sensitive by default. Use `key=str.lower` for case-insensitive string sorting.

**Example:**

```python
nums = [22, 4, 16, 8, 10]
nums.sort()                 # [4, 8, 10, 16, 22]
nums.sort(reverse=True)     # [22, 16, 10, 8, 4]

labels = ["Beta", "alpha", "Gamma"]
labels.sort()               # ['Beta', 'Gamma', 'alpha']

labels = ["Beta", "alpha", "Gamma"]
labels.sort(key=str.lower)  # ["alpha", "Beta", "Gamma"]
labels.reverse()            # ["Gamma", "Beta", "alpha"]

nums = [1, 2, 3]
print(list(reversed(nums))) # [3, 2, 1]; nums unchanged

nums = [22, 4, 16, 8, 10]

# abs(22-12)=10, abs(4-12)=8, abs(16-12)=4, abs(8-12)=4, abs(10-12)=2 → [10, 8, 4, 4, 2] → sort by keys → [10, 16, 8, 4, 22]
nums.sort(key=lambda n: abs(n - 12))  # [10, 16, 8, 4, 22]
```

**Why `list(reversed(lst))` and not just `reversed(lst)`:** `reversed()` returns a reverse iterator, not a list. Returning `reversed(lst)` alone gives an iterator object; wrap it in `list()` to get a list.

### `lst.sort(reverse=True)` vs `lst.reverse()`

| Aspect   | `lst.sort(reverse=True)`             | `lst.reverse()`               |
|----------|--------------------------------------|-------------------------------|
| Effect   | Sorts descending (by value)          | Reverses element order only   |
| Logic    | Compares elements; reorders by value | Flips indices; no comparison  |
| Use when | Want descending sort                 | Want reverse of current order |

- **`sort(reverse=True)`** sorts the list in descending order. For `[3, 1, 2]` → `[3, 2, 1]`.
- **`reverse()`** reverses the order without sorting. For `[3, 1, 2]` → `[2, 1, 3]`.

If the list is already sorted ascending, both yield the same result. Otherwise they differ.

### Lambda vs Built-in / Method

- **Use built-in or method when one exists:** `str.lower` is already a function that takes one argument; `str.lower("Beta")` returns `"beta"`. Pass it directly: `key=str.lower`.
- **Use lambda when you need custom logic:** There is no built-in "distance from 12". Use `key=lambda n: abs(n - 12)`.
- **Rule of thumb:** If a suitable function exists (`len`, `str.lower`, `abs`), pass it directly. If not, use a lambda or a named function.

### The `key` Parameter

For each element `x`, Python computes `key(x)` and compares those values instead of the elements themselves. It creates an intermediate array of keys (e.g. `[10, 8, 4, 4, 2]`), sorts by comparing those keys, and reorders the original elements accordingly — it does not compare the original elements directly. Equivalent long-form:

**Example** — step-by-step equivalent of `words.sort(key=len)`:

```python
words = ["apple", "pie", "a", "zebra"]
pairs = [(len(x), x) for x in words]  # [(5, 'apple'), (3, 'pie'), (1, 'a'), (5, 'zebra')]
pairs.sort(key=lambda p: p[0])        # sort by key only (preserves stability)
words[:] = [x for _, x in pairs]      # ["a", "pie", "apple", "zebra"] - replaced list with original elements in new order
```

In other words: sort as if each element were `key(element)`.

- **Use `words.sort(key=len)` when writing code.**
- Use the pairs version only when explaining how `key` works.

### Common `key` Conventions

`key` accepts any callable that takes one argument and returns a comparable value. Common patterns:

| Type               | Key                       | Usage                                     | Output                           | Use case                            |
|--------------------|---------------------------|-------------------------------------------|----------------------------------|-------------------------------------|
| **Built-in**       | `len`                     | `words.sort(key=len)`                     | `["a", "pie", "apple", "zebra"]` | Sort by length                      |
|                    | `str`                     | `nums.sort(key=str)`                      | `[1, 10, 2]` (lexicographic)     | Sort by string representation       |
|                    | `int`                     | `vals.sort(key=int)`                      | `["1", "2", "10"]`               | Convert before comparing            |
|                    | `abs`                     | `nums.sort(key=abs)`                      | `[-1, 2, -3]`                    | Sort by absolute value              |
| **Unbound method** | `str.lower`               | `labels.sort(key=str.lower)`              | `["alpha", "Beta", "Gamma"]`     | Case-insensitive string sort        |
|                    | `str.strip`               | `items.sort(key=str.strip)`               | By stripped value                | Sort by stripped string             |
| **operator**       | `itemgetter(1)`           | `pairs.sort(key=itemgetter(1))`           | By second element of each tuple  | Sort by index (from `operator`)     |
|                    | `attrgetter('name')`      | `people.sort(key=attrgetter('name'))`     | By `.name` attribute             | Sort by attribute (from `operator`) |
| **Lambda**         | `lambda x: x[1]`          | `pairs.sort(key=lambda x: x[1])`          | By second element                | Sort by second element              |
|                    | `lambda x: (x[0], -x[1])` | `items.sort(key=lambda x: (x[0], -x[1]))` | Asc first, desc second           | Multi-criteria sort                 |
| **Custom**         | `fn`                      | `items.sort(key=fn)`                      | By return value of `fn(x)`       | Any custom comparison               |

**Rule:** Pass the function reference, not a call; use `key=len`, not `key=len(x)`. Python calls it once per element.
