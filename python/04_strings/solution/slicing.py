def first_char(s: str) -> str:
    """Return the first character of the string using indexing."""
    return s[0]


def last_char(s: str) -> str:
    """Return the last character of the string using negative indexing."""
    return s[-1]


def first_n(s: str, n: int) -> str:
    """Return the first n characters of the string using slicing."""
    return s[:n]


def n_to_last(s: str, n: int) -> str:
    """Return the substring from index n to the end using slicing."""
    return s[n:]


def negative_slice(s: str, m: int, n: int) -> str:
    """Return the substring using negative indices s[-m:-n]."""
    return s[-m:-n]


def reversed_str(s: str) -> str:
    """Return the string reversed using the [::-1] slice."""
    return s[::-1]


def reversed_str_reversed(s: str) -> str:
    """Return the string reversed using reversed() and join()."""
    return "".join(reversed(s))


def string_length(s: str) -> int:
    """Return the length of the string using len()."""
    return len(s)
