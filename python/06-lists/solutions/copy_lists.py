"""
Copy lists: shallow copy (copy, list, slice), deep copy, nested vs first-level behavior.

Exercises:
 1. Shallow copy using original.copy(), append 8, return copy. Original unchanged.
 2. Shallow copy using list(original), append 8, return copy. Original unchanged.
 3. Shallow copy using original[:], append 8, return copy. Original unchanged.
 4. Shallow copy — nested change: copy, append 99 to shallow[0], return shallow. Mutates original (shared).
 5. Shallow copy — first-level add: copy, append [5, 6], return shallow. Original unchanged.
 6. Shallow copy — first-level remove: copy, pop, return shallow. Original unchanged.
 7. Deep copy using copy.deepcopy(original), append [5, 6], return copy. Original unchanged.
 8. Deep copy — nested change: deepcopy, append 100 to deep[0], return deep. Original unchanged.
 9. Deep copy — first-level add: deepcopy, append [5, 6], return deep. Original unchanged.
10. Deep copy — first-level remove: deepcopy, pop, return deep. Original unchanged.
"""

import copy


def copy_with_copy(original: list) -> list:
    """Return a shallow copy using original.copy(), append 8, return copy. Original unchanged."""
    result = original.copy()  # original = [2, 4, 6]
    result.append(8)          # [2, 4, 6, 8]; original still [2, 4, 6]
    return result


def copy_with_list(original: list) -> list:
    """Return a shallow copy using list(original), append 8, return copy. Original unchanged."""
    result = list(original)  # original = [2, 4, 6]
    result.append(8)              # [2, 4, 6, 8]; original still [2, 4, 6]
    return result  


def copy_with_slice(original: list) -> list:
    """Return a shallow copy using original[:], append 8, return copy. Original unchanged."""
    result = original[:]  # original = [2, 4, 6]
    result.append(8)      # [2, 4, 6, 8]; original still [2, 4, 6]
    return result  


def shallow_nested_append(original: list) -> list:
    """Copy original, append 99 to shallow[0], return shallow. Mutates original (shared reference)."""
    shallow = original.copy()  # [[1, 2], [3, 4]]
    shallow[0].append(99)      # original[0] also [1, 2, 99] — shared
    return shallow             # [[1, 2, 99], [3, 4]]


def shallow_first_level_append(original: list) -> list:
    """Copy original, append [5, 6] to shallow, return shallow. Original unchanged."""
    shallow = original.copy()  # [[1, 2], [3, 4]]
    shallow.append([5, 6])     # shallow only; original unchanged
    return shallow             # [[1, 2], [3, 4], [5, 6]]


def shallow_first_level_pop(original: list) -> list:
    """Copy original, pop from shallow, return shallow. Original unchanged."""
    shallow = original.copy()  # [[1, 2], [3, 4]]
    shallow.pop()              # shallow only; original unchanged
    return shallow             # [[1, 2]]


def copy_with_deepcopy(original: list) -> list:
    """Return a deep copy using copy.deepcopy(original), append [5, 6], return copy. Original unchanged."""
    result = copy.deepcopy(original)  # original = [[1, 2], [3, 4]]
    result.append([5, 6])             # [[1, 2], [3, 4], [5, 6]]; original still [[1, 2], [3, 4]]
    return result  


def deep_nested_append(original: list) -> list:
    """Deepcopy original, append 100 to deep[0], return deep. Original unchanged."""
    deep = copy.deepcopy(original)  # [[1, 2], [3, 4]]
    deep[0].append(100)             # deep only; original unchanged
    return deep                     # [[1, 2, 100], [3, 4]]


def deep_first_level_append(original: list) -> list:
    """Deepcopy original, append [5, 6] to deep, return deep. Original unchanged."""
    deep = copy.deepcopy(original)  # [[1, 2], [3, 4]]
    deep.append([5, 6])             # deep only; original unchanged
    return deep                     # [[1, 2], [3, 4], [5, 6]]


def deep_first_level_pop(original: list) -> list:
    """Deepcopy original, pop from deep, return deep. Original unchanged."""
    deep = copy.deepcopy(original)  # [[1, 2], [3, 4]]
    deep.pop()                      # deep only; original unchanged
    return deep                     # [[1, 2]]


def main() -> None:
    original = [2, 4, 6]
    print("copy_with_copy(original) =", copy_with_copy(original))
    print("copy_with_list(original) =", copy_with_list(original))
    print("copy_with_slice(original) =", copy_with_slice(original))
    print("original unchanged =", original)

    original = [[1, 2], [3, 4]]
    print("shallow_nested_append(original) =", shallow_nested_append(original))
    print("original mutated (shared) =", original)

    original = [[1, 2], [3, 4]]
    print("shallow_first_level_append(original) =", shallow_first_level_append(original))
    print("original unchanged =", original)

    original = [[1, 2], [3, 4]]
    print("shallow_first_level_pop(original) =", shallow_first_level_pop(original))
    print("original unchanged =", original)

    original = [[1, 2], [3, 4]]
    print("copy_with_deepcopy(original) =", copy_with_deepcopy(original))
    print("deep_nested_append(original) =", deep_nested_append(original))
    print("original unchanged =", original)

    original = [[1, 2], [3, 4]]
    print("deep_first_level_append(original) =", deep_first_level_append(original))
    print("deep_first_level_pop(original) =", deep_first_level_pop(original))
    print("original unchanged =", original)


if __name__ == "__main__":
    main()
