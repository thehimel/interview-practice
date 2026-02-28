"""
Loop lists: direct iteration, index-based, while loop, and loop in reverse patterns.

Exercises:
 1. Collect elements using direct iteration: for x in nums
 2. Collect elements using index-based loop: for i in range(len(nums))
 3. Collect elements at step intervals using while: i = 0; while i < len(nums); i += step
 4. Collect elements in reverse using reversed(nums)
 5. Collect elements in reverse using nums[::-1]
 6. Collect elements in reverse using range(len(nums)-1, -1, -1)
"""


def collect_direct(nums: list) -> list:
    """Return a list of elements collected using direct iteration (for x in nums). nums = [2, 4, 6, 8] → [2, 4, 6, 8]."""
    pass


def collect_by_index(nums: list) -> list:
    """Return a list of elements collected using index-based loop (for i in range(len(nums))). nums = [2, 4, 6, 8] → [2, 4, 6, 8]."""
    pass


def collect_while_step(nums: list, step: int) -> list:
    """Return elements at indices 0, step, 2*step, ... using a while loop. nums = [2, 4, 6, 8], step=2 → [2, 6]."""
    pass


def collect_reversed(nums: list) -> list:
    """Return elements in reverse order using reversed(nums). nums = [2, 4, 6, 8] → [8, 6, 4, 2]."""
    pass


def collect_reversed_slice(nums: list) -> list:
    """Return elements in reverse order using nums[::-1]. nums = [2, 4, 6, 8] → [8, 6, 4, 2]."""
    pass


def collect_reversed_by_index(nums: list) -> list:
    """Return elements in reverse order using range(len(nums)-1, -1, -1). nums = [2, 4, 6, 8] → [8, 6, 4, 2]."""
    pass


def main() -> None:
    nums = [2, 4, 6, 8]
    print("collect_direct(nums) =", collect_direct(nums))
    print("collect_by_index(nums) =", collect_by_index(nums))
    print("collect_while_step(nums, 2) =", collect_while_step(nums, 2))
    print("collect_reversed(nums) =", collect_reversed(nums))
    print("collect_reversed_slice(nums) =", collect_reversed_slice(nums))
    print("collect_reversed_by_index(nums) =", collect_reversed_by_index(nums))


if __name__ == "__main__":
    main()
