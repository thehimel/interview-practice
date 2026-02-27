def find_sub(s: str, sub: str) -> int:
    """Return the lowest index where sub is found using find(). Return -1 if not found."""
    return s.find(sub)


def index_sub(s: str, sub: str) -> int:
    """Return the lowest index where sub is found using index(). Raises if not found."""
    return s.index(sub)


def rfind_sub(s: str, sub: str) -> int:
    """Return the highest index where sub is found using rfind(). Return -1 if not found."""
    return s.rfind(sub)


def rindex_sub(s: str, sub: str) -> int:
    """Return the highest index where sub is found using rindex(). Raises if not found."""
    return s.rindex(sub)


def count_sub(s: str, sub: str) -> int:
    """Return the number of non-overlapping occurrences of sub using count()."""
    return s.count(sub)


def contains_sub(s: str, sub: str) -> bool:
    """Return True if sub is a substring of s using the 'in' operator."""
    return sub in s


def starts_with(s: str, prefix: str) -> bool:
    """Return True if the string starts with the prefix using startswith()."""
    return s.startswith(prefix)


def ends_with(s: str, suffix: str) -> bool:
    """Return True if the string ends with the suffix using endswith()."""
    return s.endswith(suffix)
