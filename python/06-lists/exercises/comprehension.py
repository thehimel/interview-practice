"""
List comprehension: build a new list from an iterable with optional filter and expression.

Exercises:
 1. Double each element: [x * 2 for x in nums]
 2. Filter greater than n: [x for x in nums if x > n]
 3. Evens from range: [x for x in range(n) if x % 2 == 0]
 4. Square each element: [x ** 2 for x in nums]
"""


def double_elements(nums: list) -> list:
    """Return a list with each element doubled. nums = [2, 4, 6, 8, 10] → [4, 8, 12, 16, 20]."""
    pass


def filter_greater_than(nums: list, n: int) -> list:
    """Return elements greater than n. nums = [2, 4, 6, 8, 10], n=4 → [6, 8, 10]."""
    pass


def evens_from_range(n: int) -> list:
    """Return even numbers from 0 to n-1. n=10 → [0, 2, 4, 6, 8]."""
    pass


def square_elements(nums: list) -> list:
    """Return a list with each element squared. nums = [2, 4, 6, 8, 10] → [4, 16, 36, 64, 100]."""
    pass


def main() -> None:
    nums = [2, 4, 6, 8, 10]
    print("double_elements(nums) =", double_elements(nums))
    print("filter_greater_than(nums, 4) =", filter_greater_than(nums, 4))
    print("evens_from_range(10) =", evens_from_range(10))
    print("square_elements(nums) =", square_elements(nums))


if __name__ == "__main__":
    main()
