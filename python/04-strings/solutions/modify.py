def to_upper(s: str) -> str:
    """Convert the string to uppercase using upper()."""
    return s.upper()


def to_lower(s: str) -> str:
    """Convert the string to lowercase using lower()."""
    return s.lower()


def casefold_str(s: str) -> str:
    """Return a casefolded string for caseless comparison using casefold()."""
    return s.casefold()


def capitalized(s: str) -> str:
    """Capitalize the first character of the string using capitalize()."""
    return s.capitalize()


def swap_case(s: str) -> str:
    """Swap uppercase to lowercase and vice versa using swapcase()."""
    return s.swapcase()


def title_case(s: str) -> str:
    """Return the string with each word capitalized using title()."""
    return s.title()


def stripped(s: str) -> str:
    """Remove leading and trailing whitespace using strip()."""
    return s.strip()


def left_stripped(s: str) -> str:
    """Remove leading whitespace using lstrip()."""
    return s.lstrip()


def right_stripped(s: str) -> str:
    """Remove trailing whitespace using rstrip()."""
    return s.rstrip()


def stripped_chars(s: str, chars: str) -> str:
    """Remove leading and trailing characters in chars using strip(chars)."""
    return s.strip(chars)


def replaced(s: str, old: str, new: str) -> str:
    """Replace all occurrences of old with new using replace()."""
    return s.replace(old, new)


def replace_count(s: str, old: str, new: str, count: int) -> str:
    """Replace at most count occurrences of old with new using replace(old, new, count)."""
    return s.replace(old, new, count)


def split_str(s: str, sep: str) -> list:
    """Split the string by the given separator using split()."""
    return s.split(sep)


def rsplit_str(s: str, sep: str, maxsplit: int = -1) -> list:
    """Split from the right with optional maxsplit using rsplit()."""
    return s.rsplit(sep, maxsplit)


def split_lines(s: str) -> list:
    """Split the string into lines using splitlines()."""
    return s.splitlines()


def remove_prefix(s: str, prefix: str) -> str:
    """Remove the prefix if present using removeprefix()."""
    return s.removeprefix(prefix)


def remove_suffix(s: str, suffix: str) -> str:
    """Remove the suffix if present using removesuffix()."""
    return s.removesuffix(suffix)


def partition_str(s: str, sep: str) -> tuple:
    """Split into (before, sep, after) at the first occurrence using partition()."""
    return s.partition(sep)


def rpartition_str(s: str, sep: str) -> tuple:
    """Split into (before, sep, after) at the last occurrence using rpartition()."""
    return s.rpartition(sep)
