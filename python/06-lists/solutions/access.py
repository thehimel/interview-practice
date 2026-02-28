"""
List access exercises.

nums = [2, 4, 6, 8, 10, 12, 14, 16]

Questions:
 1. Return the first, last, and element at index 2 of nums
 2. Return the first 4 elements and the rest from index 4
 3. Return the slice from index 2 to 6 (exclusive) and the slice from 4th-from-end to 2nd-from-end
 4. Return nums reversed using the [::-1] slice
 5. Return nums reversed using list(reversed(nums))
 6. Return nums reversed using the reverse() method (copy first to avoid mutating)
 7. Count the occurrences of 6 and find the index of 8 (or -1 if not present)
"""


def first_last_and_at_2(nums: list) -> tuple:
    """Return the first, last, and element at index 2 of nums."""
    return nums[0], nums[-1], nums[2]  # (2, 16, 6)


def split_at_4(nums: list) -> tuple:
    """Return the first 4 elements and the rest from index 4."""
    return nums[:4], nums[4:]  # ([2, 4, 6, 8], [10, 12, 14, 16])


def slices_2_to_6_and_negative(nums: list) -> tuple:
    """Return the slice from index 2 to 6 (exclusive) and the slice from 4th-from-end to 2nd-from-end."""
    return nums[2:6], nums[-4:-2]  # ([6, 8, 10, 12], [10, 12])


def nums_reversed_slice(nums: list) -> list:
    """Return nums reversed using the [::-1] slice."""
    return nums[::-1]  # [16, 14, 12, 10, 8, 6, 4, 2]


def nums_reversed_builtin(nums: list) -> list:
    """Return nums reversed using list(reversed(nums))."""
    return list(reversed(nums))  # [16, 14, 12, 10, 8, 6, 4, 2]


def nums_reversed_method(nums: list) -> list:
    """Return nums reversed using the reverse() method (copy first to avoid mutating)."""
    # Shallow copy is enough: reverse() only reorders references, it does not mutate the elements.
    result = nums.copy()
    result.reverse()
    return result  # [16, 14, 12, 10, 8, 6, 4, 2]


def count_six_and_find_eight(nums: list) -> tuple:
    """Count the occurrences of 6 and find the index of 8 (or -1 if not present)."""
    return nums.count(6), nums.index(8) if 8 in nums else -1  # (1, 3)


def main() -> None:
    nums = [2, 4, 6, 8, 10, 12, 14, 16]
    print("nums =", nums)
    print("1. first_last_and_at_2:", first_last_and_at_2(nums))
    print("2. split_at_4:", split_at_4(nums))
    print("3. slices_2_to_6_and_negative:", slices_2_to_6_and_negative(nums))
    print("4. nums_reversed_slice:", nums_reversed_slice(nums))
    print("5. nums_reversed_builtin:", nums_reversed_builtin(nums))
    print("6. nums_reversed_method:", nums_reversed_method(nums))
    print("7. count_six_and_find_eight:", count_six_and_find_eight(nums))


if __name__ == "__main__":
    main()
