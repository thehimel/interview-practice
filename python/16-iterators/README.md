# Iterators

An iterator is an object that produces values one at a time. It supports the iterator protocol: `__iter__()` and `__next__()`. Iteration stops when `StopIteration` is raised.

## Iterable vs Iterator

| Concept      | Meaning                                                                        |
|--------------|--------------------------------------------------------------------------------|
| **Iterable** | An object that can produce an iterator (e.g. list, tuple, str, dict, set)      |
| **Iterator** | An object that yields values via `next()` and raises `StopIteration` when done |

An iterable has `__iter__()` (or `__getitem__` for legacy support). An iterator has both `__iter__()` and `__next__()`. Every iterator is iterable; not every iterable is an iterator.

**Obtaining an iterator:** Call `iter(obj)` on an iterable. `iter()` invokes `obj.__iter__()` and returns the iterator.

```python
items = (2, 4, 6, 8)
it = iter(items)
next(it)  # 2
next(it)  # 4
next(it)  # 6
next(it)  # 8
next(it)  # StopIteration
```

## iter() and next()

| Function    | Purpose                                                       |
|-------------|---------------------------------------------------------------|
| `iter(obj)` | Returns an iterator for the object                            |
| `next(it)`  | Returns the next value; raises `StopIteration` when exhausted |

`next(it, default)` returns `default` instead of raising when the iterator is exhausted.

```python
it = iter([2, 4, 6])
next(it, None)  # 2
next(it, None)  # 4
next(it, None)  # 6
next(it, None)  # None (no StopIteration)
```

## Strings Are Iterable

Strings yield one character per iteration:

```python
it = iter("data")
next(it)  # 'd'
next(it)  # 'a'
```

## How for Loops Work

A `for` loop calls `iter()` on the target, then repeatedly calls `next()` on the iterator until `StopIteration` is raised. The loop catches `StopIteration` and exits.

```python
for x in [2, 4, 6]:
    print(x)
```

Is equivalent to:

```python
it = iter([2, 4, 6])
while True:
    try:
        x = next(it)
    except StopIteration:
        break
    print(x)
```

## Creating a Custom Iterator

Implement `__iter__()` and `__next__()`. `__iter__()` returns the iterator (often `self`). `__next__()` returns the next value or raises `StopIteration`.

```python
class CountByTwo:
    def __iter__(self):
        self.n = 2
        return self

    def __next__(self):
        x = self.n
        self.n += 2
        return x

it = iter(CountByTwo())
next(it)  # 2
next(it)  # 4
next(it)  # 6
```

**Without a stop condition:** This iterator runs forever. Use it in a `for` loop with `break`, or wrap in `itertools.islice`.

## StopIteration

Raise `StopIteration` in `__next__()` when there are no more values. The `for` loop and other iteration machinery catch it and stop cleanly.

```python
class CountToTen:
    def __iter__(self):
        self.n = 2
        return self

    def __next__(self):
        if self.n <= 10:
            x = self.n
            self.n += 2
            return x
        raise StopIteration

list(CountToTen())  # [2, 4, 6, 8, 10]
```

## Iterable vs Iterator: Subtle Points

**List is iterable, not iterator:** `[2, 4, 6]` has `__iter__` but no `__next__`. Each call to `iter([2, 4, 6])` returns a new iterator. A list can be iterated multiple times; each iteration gets a fresh iterator.

**Iterator is single-use:** Once exhausted, calling `next()` again raises `StopIteration`. To iterate again, obtain a new iterator from the original iterable.

**Iterator returns self from __iter__:** An iterator's `__iter__()` typically returns `self`, so an iterator can be used in a `for` loop directly.

## Common Gotchas

### Exhausted iterator

Reusing an exhausted iterator does not reset it. Get a new iterator from the iterable.

```python
it = iter([2, 4, 6])
list(it)  # [2, 4, 6]
list(it)  # []
```

### Modifying during iteration

Changing a list (or other mutable iterable) while iterating over it can lead to skipped items or errors. Iterate over a copy if the collection may change.

### Generators are iterators

Generator functions (using `yield`) produce iterator objects. They implement `__iter__` and `__next__` automatically.

## Interview Questions

### What is the difference between an iterable and an iterator?

An iterable can produce an iterator via `iter()`. An iterator yields values via `next()` and raises `StopIteration` when done. Lists, tuples, and strings are iterables; the object returned by `iter()` is an iterator.

### What methods must an iterator implement?

`__iter__()` (returning itself) and `__next__()` (returning the next value or raising `StopIteration`).

### How does a for loop use an iterator?

It calls `iter()` on the target to get an iterator, then repeatedly calls `next()` until `StopIteration` is raised.

### Can an exhausted iterator be reused?

No. Once `StopIteration` is raised, further `next()` calls keep raising it. Obtain a new iterator from the original iterable to iterate again.

### What does next(it, default) do?

Returns the next value, or `default` if the iterator is exhausted, instead of raising `StopIteration`.
