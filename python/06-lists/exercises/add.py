"""
Add list items: append, insert, extend.

nums = [2, 4, 6, 8, 10, 12, 14, 16]

Exercises:
 1. Using append(8) and insert(2, 0) in sequence, return the resulting list.
 2. Concatenate nums and other using the + operator (returns a new list).
 3. Concatenate nums and other using extend (copy first, extend, return).
"""


def add_items(nums: list) -> list:
    """Append 8 and insert 0 at index 2. Return a new list."""
    pass


def concat_with_plus(nums: list, other: list) -> list:
    """Concatenate nums and other using the + operator. Returns a new list."""
    pass


def concat_with_extend(nums: list, other) -> list:
    """Concatenate nums and other using extend. Copy first, extend, return. Accepts any iterable.

    Examples:
        list:   concat_with_extend([2,4,6,8,10,12,14,16], [8, 10])   → [..., 8, 10] (order preserved)
        tuple:  concat_with_extend([2,4,6,8,10,12,14,16], (8, 10))   → [..., 8, 10] (order preserved)
        set:    concat_with_extend([2,4,6,8,10,12,14,16], {8, 10})   → [..., 8, 10] (order may vary)
        dict:   concat_with_extend([2,4,6,8,10,12,14,16], {8:'a', 10:'b'}) → [..., 8, 10] (keys only, insertion order)
    """
    pass


def main() -> None:
    nums = [2, 4, 6, 8, 10, 12, 14, 16]
    print("nums =", nums)
    print("add_items(nums) =", add_items(nums))
    print("concat_with_plus(nums, [8, 10]) =", concat_with_plus(nums, [8, 10]))
    print("concat_with_extend(nums, [8, 10])   [list]  =", concat_with_extend(nums, [8, 10]))
    print("concat_with_extend(nums, (8, 10))   [tuple] =", concat_with_extend(nums, (8, 10)))
    print("concat_with_extend(nums, {8, 10})   [set]   =", concat_with_extend(nums, {8, 10}))
    print("concat_with_extend(nums, {8:'a', 10:'b'}) [dict]  =", concat_with_extend(nums, {8: "a", 10: "b"}))
    print("nums unchanged =", nums)


if __name__ == "__main__":
    main()
