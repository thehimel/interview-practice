"""
Remove list items: remove, pop, del, clear, remove all occurrences.

colors = ["red", "blue", "green", "yellow", "black", "white", "gray"]

Exercise:
- Remove the first occurrence of "green".
- Pop the element at index 2.
- Delete the slice 1:4.
- Clear the list.
- Return a new list.

Also: remove_all_occurrences(lst, value) — return new list (original unchanged).
Also: remove_all_occurrences_in_place(lst, value) — remove in place (original changed).
"""


def remove_items(colors: list) -> list:
    """Without changing the original list return a new list after applying the operations:
        - Remove the first occurrence of "green".
        - Pop the element at index 2.
        - Delete the slice 1:4.
        - Clear the list.
    """
    result = colors.copy()
    result.remove("green")   # ["red", "blue", "yellow", "black", "white", "gray"]
    result.pop(2)            # ["red", "blue", "black", "white", "gray"]
    del result[1:4]          # ["red", "gray"]
    result.clear()           # []
    return result


def remove_all_occurrences(nums: list, value) -> list:
    """Return a new list with all occurrences of value removed. Original unchanged.
    O(n). Must not use remove() — that would be O(n²)."""
    return [x for x in nums if x != value]


def remove_all_occurrences_in_place(nums: list, value) -> list:
    """Remove all occurrences of value in place. Original changed.
    O(n). Must not use remove() — that would be O(n²)."""
    nums[:] = [x for x in nums if x != value]
    return nums


def main() -> None:
    colors = ["red", "blue", "green", "yellow", "black", "white", "gray"]
    print("colors =", colors)
    print("remove_items(colors) =", remove_items(colors))
    print("colors unchanged =", colors)
    colors_with_dupes = ["red", "blue", "green", "blue", "black", "white", "blue"]
    print("remove_all_occurrences(colors_with_dupes, 'blue') =", remove_all_occurrences(colors_with_dupes, "blue"))
    print("colors_with_dupes unchanged =", colors_with_dupes)
    remove_all_occurrences_in_place(colors_with_dupes, "blue")
    print("after remove_all_occurrences_in_place, colors_with_dupes =", colors_with_dupes)


if __name__ == "__main__":
    main()
