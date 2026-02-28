"""
Sort lists: sort, sort(reverse=True), reverse, reversed, sort(key=fn).

nums = [2, 4, 6, 8, 10, 12, 14, 16]
labels = ["Beta", "alpha", "Gamma"]
colors = ["red", "blue", "green", "yellow", "black", "white", "gray"]

Exercises:
 1. Sort nums ascending (copy first, sort, return). Original unchanged.
 2. Sort nums descending (copy, sort(reverse=True), return). Original unchanged.
 3. Reverse nums (copy, reverse(), return). Original unchanged.
 4. Return a new reversed list using reversed(). Original unchanged.
 5. Sort by len (key=len). Original unchanged.
 6. Sort by str (key=str). Original unchanged.
 7. Sort by int (key=int). Original unchanged.
 8. Sort by abs (key=abs). Original unchanged.
 9. Sort by str.lower (key=str.lower). Original unchanged.
10. Sort by str.strip (key=str.strip). Original unchanged.
11. Sort by distance from 12 (key=lambda n: abs(n - 12)). Original unchanged.
"""


def sort_ascending(nums: list) -> list:
    """Copy nums, sort ascending, return. Original unchanged."""
    result = nums.copy()  # [2, 4, 6, 8, 10, 12, 14, 16]
    result.sort()         # [2, 4, 6, 8, 10, 12, 14, 16]
    return result


def sort_descending(nums: list) -> list:
    """Copy nums, sort descending, return. Original unchanged."""
    result = nums.copy()       # [2, 4, 6, 8, 10, 12, 14, 16]
    result.sort(reverse=True)  # [16, 14, 12, 10, 8, 6, 4, 2]
    return result


def reverse_items(nums: list) -> list:
    """Copy nums, reverse in place, return. Original unchanged."""
    result = nums.copy()  # [2, 4, 6, 8, 10, 12, 14, 16]
    result.reverse()      # [16, 14, 12, 10, 8, 6, 4, 2]
    return result


def reversed_new_list(nums: list) -> list:
    """Return a new list with elements in reverse order using reversed(). Original unchanged."""
    return list(reversed(nums))  # [16, 14, 12, 10, 8, 6, 4, 2]


def sort_by_len(colors: list) -> list:
    """Copy colors, sort by length (key=len), return. Original unchanged."""
    result = colors.copy()  # ["red", "blue", "green", "yellow", "black", "white", "gray"]
    result.sort(key=len)    # ["red", "blue", "gray", "green", "black", "white", "yellow"]
    return result


def sort_by_str(nums: list) -> list:
    """Copy nums, sort by string representation (key=str), return. Original unchanged."""
    result = nums.copy()  # [2, 4, 6, 8, 10, 12, 14, 16]
    result.sort(key=str)  # [10, 12, 14, 16, 2, 4, 6, 8]
    return result


def sort_by_int(vals: list) -> list:
    """Copy vals (list of numeric strings), sort by int (key=int), return. Original unchanged."""
    result = vals.copy()  # ["2", "10", "1"]
    result.sort(key=int)  # ["1", "2", "10"]
    return result


def sort_by_abs(nums: list) -> list:
    """Copy nums, sort by absolute value (key=abs), return. Original unchanged.

    abs(-3)=3, abs(2)=2, abs(-1)=1 → [3, 2, 1] → sort by keys → [-1, 2, -3]
    """
    result = nums.copy()  # [-3, 2, -1]
    result.sort(key=abs)  # [-1, 2, -3]
    return result


def sort_by_str_lower(labels: list) -> list:
    """Copy labels, sort case-insensitive (key=str.lower), return. Original unchanged."""
    result = labels.copy()      # ["Beta", "alpha", "Gamma"]
    result.sort(key=str.lower)  # ["alpha", "Beta", "Gamma"]
    return result


def sort_by_str_strip(items: list) -> list:
    """Copy items, sort by stripped string (key=str.strip), return. Original unchanged."""
    result = items.copy()       # ["  red", "blue  ", " green "]
    result.sort(key=str.strip)  # ["blue  ", " green ", "  red"]
    return result


def sort_by_distance_from_12(nums: list) -> list:
    """Copy nums, sort by distance from 12 (key=lambda n: abs(n - 12)), return. Original unchanged."""
    result = nums.copy()                    # [2, 4, 6, 8, 10, 12, 14, 16]
    result.sort(key=lambda n: abs(n - 12))  # [12, 10, 14, 8, 16, 6, 4, 2]
    return result


def main() -> None:
    nums = [2, 4, 6, 8, 10, 12, 14, 16]
    print("nums =", nums)
    print("sort_ascending(nums) =", sort_ascending(nums))
    print("sort_descending(nums) =", sort_descending(nums))
    print("reverse_items(nums) =", reverse_items(nums))
    print("reversed_new_list(nums) =", reversed_new_list(nums))
    print("nums unchanged =", nums)

    colors = ["red", "blue", "green", "yellow", "black", "white", "gray"]
    print("sort_by_len(colors) =", sort_by_len(colors))

    print("sort_by_str(nums) =", sort_by_str(nums))

    vals = ["2", "10", "1"]
    print("sort_by_int(vals) =", sort_by_int(vals))

    nums_abs = [-3, 2, -1]
    print("sort_by_abs(nums) =", sort_by_abs(nums_abs))

    labels = ["Beta", "alpha", "Gamma"]
    print("sort_by_str_lower(labels) =", sort_by_str_lower(labels))

    items = ["  red", "blue  ", " green "]
    print("sort_by_str_strip(items) =", sort_by_str_strip(items))

    print("sort_by_distance_from_12(nums) =", sort_by_distance_from_12(nums))


if __name__ == "__main__":
    main()
