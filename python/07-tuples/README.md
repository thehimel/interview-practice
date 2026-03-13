# Tuples Topics

Tuples are ordered, immutable sequences. They can hold mixed types and allow duplicate values.

**Creating a tuple:** Use parentheses or `tuple()`. A single-element tuple requires a trailing comma: `(2,)` — without the comma, `(2)` is just an integer in parentheses.

```python
nums = (2, 4, 6, 8, 10)
single = (2,)           # tuple
not_tuple = (2)         # int
built = tuple([2, 4, 6])  # (2, 4, 6)
```

**Length:** Use `len(t)` to get the number of elements.

## Tuple Methods

| Method     | Description                                                                     |
|------------|---------------------------------------------------------------------------------|
| `count(x)` | Return the number of occurrences of `x`                                         |
| `index(x)` | Return the index of the first occurrence of `x`; raises `ValueError` if missing |

Tuples have only these two methods because they are immutable. No `append`, `remove`, `sort`, or `reverse`.

## Access Tuples

Use **indexing** and **slicing** the same way as lists. Indices start at 0; negative indices count from the end.

| Pattern      | Description                   | Example                              |
|--------------|-------------------------------|--------------------------------------|
| `t[i]`       | Single element at index `i`   | `nums[2]` → 6                        |
| `t[-1]`      | Last element                  | `nums[-1]` → 10                      |
| `t[i:j]`     | Slice from `i` to `j` (excl.) | `nums[2:5]` → (6, 8, 10)             |
| `t[:n]`      | First `n` elements            | `nums[:4]` → (2, 4, 6, 8)            |
| `t[n:]`      | From index `n` to end         | `nums[4:]` → (10,)                   |
| `t[-m:-n]`   | Slice with negative indices   | `nums[-4:-2]` → (4, 6)               |

**Membership:** Use `in` to check whether an element exists in the tuple.

**Value lookup:** Use `count(x)` to count occurrences and `index(x)` to get the first index (raises `ValueError` if missing).

```python
nums = (2, 4, 6, 8, 10, 12, 14, 16)
nums[2]         # 6
nums[-1]        # 16
nums[2:6]       # (6, 8, 10, 12)
nums[:4]        # (2, 4, 6, 8)
nums[4:]        # (10, 12, 14, 16)
nums[-4:-2]     # (12, 14)
4 in nums       # True
nums.count(6)   # 1
nums.index(8)   # 3
```

## Update Tuples

Tuples are **immutable** — you cannot change, add, or remove elements in place. To "update" a tuple, create a new one.

**Replace an element:** Convert to list, modify, convert back.

```python
nums = (2, 4, 6, 8, 10)
temp = list(nums)
temp[1] = 0
nums = tuple(temp)  # (2, 0, 6, 8, 10)
```

**Add an element:** Convert to list, append, convert back — or concatenate with a single-element tuple.

```python
nums = (2, 4, 6, 8, 10)
temp = list(nums)
temp.append(12)
nums = tuple(temp)  # (2, 4, 6, 8, 10, 12)
print(nums)

nums = (2, 4, 6, 8, 10)
nums += (12,)  # (2, 4, 6, 8, 10, 12)
```

**Remove an element:** Convert to list, remove or filter, convert back.

```python
nums = (2, 4, 6, 8, 10)
temp = list(nums)
temp.remove(6)
nums = tuple(temp)  # (2, 4, 8, 10)
```

## Unpack Tuples

Assign tuple elements to variables in one statement.

```python
nums = (2, 4, 6)
a, b, c = nums  # a=2, b=4, c=6
```

**Asterisk `*`:** Collect remaining elements into a list.

```python
nums = (2, 4, 6, 8, 10)
first, second, *rest = nums  # first=2, second=4, rest=[6, 8, 10]
print(type(rest))            # <class 'list'>
```

**Middle unpacking:** Use `*` at any position to capture the rest.

```python
nums = (2, 4, 6, 8, 10)
a, *mid, z = nums  # a=2, mid=[4, 6, 8], z=10
```

**Mismatched count:** The number of variables must match the number of elements, unless `*` is used to absorb extras.

```python
nums = (2, 4, 6)
a, b = nums        # ValueError: too many values to unpack
a, b, c, d = nums  # ValueError: not enough values to unpack

a, b, c, *d = (2, 4, 6)  # a=2, b=4, c=6, d=[]
```

## Reverse Tuples

Create a new tuple with elements in reverse order. The original tuple is unchanged.

| Approach             | Example                 | Returns   | Mutates original? |
|----------------------|-------------------------|-----------|-------------------|
| `tuple(reversed(t))` | `tuple(reversed(nums))` | New tuple | No                |
| Slice `[::-1]`       | `nums[::-1]`            | New tuple | No                |


```python
original = (4, 2, 8, 6, 10)
# reversed() returns a reverse iterator; wrap in tuple() to get a tuple
nums = tuple(reversed(original))  # nums = (10, 6, 8, 2, 4); original = (4, 2, 8, 6, 10)

original = (4, 2, 8, 6, 10)
nums = original[::-1]  # nums = (10, 6, 8, 2, 4); original = (4, 2, 8, 6, 10)
```

- **`tuple(reversed(t))`** — `reversed()` returns a reverse iterator; wrap in `tuple()` to get a tuple. O(n) time, O(n) space.
- **`t[::-1]`** — Slice with step -1; creates a new tuple. O(n) time, O(n) space.

> Tuples have no `reverse()` method (unlike lists) because they are immutable.

## Loop Tuples

Three common patterns: direct iteration, index-based, and while loop.

**Direct iteration:**

```python
nums = (2, 4, 6, 8)
for x in nums:
    print(x)  # 2, 4, 6, 8
```

**Index-based:**

```python
nums = (2, 4, 6, 8)
for i in range(len(nums)):
    print(nums[i])  # 2, 4, 6, 8
```

**While loop:**

```python
nums = (2, 4, 6, 8)
i = 0
while i < len(nums):
    print(nums[i])
    i += 2  # 2, 6 — step by 2
```

**Loop in reverse:**

```python
nums = (2, 4, 6, 8)

for x in reversed(nums):  # O(n)
    print(x)              # 8, 6, 4, 2

for x in nums[::-1]:  # O(n)
    print(x)          # 8, 6, 4, 2 — slice with step -1

for i in range(len(nums) - 1, -1, -1):  # O(n)
    print(nums[i])                      # 8, 6, 4, 2 — index-based reverse
```

- **`reversed(t)`** — Returns a reverse iterator; does not create a new tuple.
- **`t[::-1]`** — Slice with step -1; creates a new tuple in reverse order.
- **`range(len(t)-1, -1, -1)`** — Index-based; iterate from last index down to 0.

**Why LeetCode often prefers the index-based reverse:** When you need to **modify** elements by index (swap, overwrite, remove), you must have the index. `reversed()` and `t[::-1]` give values, not indices. The `range(len(t)-1, -1, -1)` pattern also avoids index shifting when removing elements in place, and it translates directly to other languages (C, Java, etc.).

## Join Tuples

**Concatenation with `+`:** Both operands must be tuples. Returns a new tuple.

```python
a = (2, 4, 6)
b = (8, 10, 12)
c = a + b  # (2, 4, 6, 8, 10, 12)
```

**Repetition with `*`:** Repeat the tuple a given number of times.

```python
nums = (2, 4, 6)
doubled = nums * 2  # (2, 4, 6, 2, 4, 6)
```

**Note:** `+` and `*` create new tuples; they do not modify the original.

## Sort Tuples

Tuples have no `sort()` method because they are immutable. To get a sorted tuple, create a new one using `sorted()`.

**`sorted(t)`** returns a **list**, not a tuple. Wrap in `tuple()` to get a tuple.

```python
nums = (10, 4, 8, 2, 6)
tuple(sorted(nums))                # (2, 4, 6, 8, 10)
tuple(sorted(nums, reverse=True))  # (10, 8, 6, 4, 2)
```

**With `key`:** Use `key` for custom sort order, same as for lists.

```python
nums = (2, 4, 6, 8, 10, 12, 14, 16)
tuple(sorted(nums, key=lambda n: abs(n - 10)))  # sort by distance from 10
# (10, 8, 12, 6, 14, 4, 16, 2)
```

**Alternative:** Convert to list, sort in place, convert back. `sorted(t)` is simpler and preferred.

```python
nums = (10, 4, 8, 2, 6)
temp = list(nums)
temp.sort()
tuple(temp)  # (2, 4, 6, 8, 10)
```

## Interview Questions

### Why use a tuple instead of a list?

Immutability (safe as dict key, set element); slightly less memory; semantic "fixed structure." Tuples are hashable if all elements are hashable.

### How do you create a single-element tuple?

Use a trailing comma: `(2,)`. Without the comma, `(2)` is just an integer in parentheses.

### Can you "modify" a tuple? How?

Tuples are immutable. To change, add, or remove elements, convert to list, modify, convert back: `tuple(list(t))` or use `+` for concatenation.

### What does `*` do in tuple unpacking?

Collects remaining elements into a list: `first, *rest = nums` → `rest = [4, 6, 8, 10]`. Use at any position: `a, *mid, z = nums`.

### How do you sort a tuple?

`tuple(sorted(t))` — `sorted()` returns a list, so wrap in `tuple()`. Use `key` for custom order: `tuple(sorted(t, key=fn))`.

### Why does a tuple have only `count` and `index`?

Tuples are immutable, so they have no mutating methods. `count` and `index` are the only read-only operations needed; no `append`, `remove`, `sort`, or `reverse`.
