def check(nums, x, y):
    """
    Combine logical (and, or) and membership (in, not in) operators with conditionals.

    Args:
        nums: collection to search
        x: value to check
        y: threshold for comparison

    Returns:
        -1 if x is not present in nums or x is None
        True if x is in nums and x > y
        False if x is in nums and x <= y
    """
    if x not in nums or x is None:
        return -1
    elif x in nums and x > y:
        pass
    else:
        pass
