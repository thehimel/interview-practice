def to_upper(s: str) -> str:
    """Convert the string to uppercase using upper()."""
    pass


def to_lower(s: str) -> str:
    """Convert the string to lowercase using lower()."""
    pass


def casefold_str(s: str) -> str:
    """Return a casefolded string for caseless comparison using casefold()."""
    pass


def capitalized(s: str) -> str:
    """Capitalize the first character of the string using capitalize()."""
    pass


def swap_case(s: str) -> str:
    """Swap uppercase to lowercase and vice versa using swapcase()."""
    pass


def title_case(s: str) -> str:
    """Return the string with each word capitalized using title()."""
    pass


def stripped(s: str) -> str:
    """Remove leading and trailing whitespace using strip()."""
    pass


def left_stripped(s: str) -> str:
    """Remove leading whitespace using lstrip()."""
    pass


def right_stripped(s: str) -> str:
    """Remove trailing whitespace using rstrip()."""
    pass


def stripped_chars(s: str, chars: str) -> str:
    """Remove leading and trailing characters in chars using strip(chars)."""
    pass


def replaced(s: str, old: str, new: str) -> str:
    """Replace all occurrences of old with new using replace()."""
    pass


def replace_count(s: str, old: str, new: str, count: int) -> str:
    """Replace at most count occurrences of old with new using replace(old, new, count)."""
    pass


def split_str(s: str, sep: str) -> list:
    """Split the string by the given separator using split()."""
    pass


def rsplit_str(s: str, sep: str, maxsplit: int = -1) -> list:
    """Split from the right with optional maxsplit using rsplit()."""
    pass


def split_lines(s: str) -> list:
    """Split the string into lines using splitlines()."""
    pass


def remove_prefix(s: str, prefix: str) -> str:
    """Remove the prefix if present using removeprefix()."""
    pass


def remove_suffix(s: str, suffix: str) -> str:
    """Remove the suffix if present using removesuffix()."""
    pass


def partition_str(s: str, sep: str) -> tuple:
    """Split into (before, sep, after) at the first occurrence using partition()."""
    pass


def rpartition_str(s: str, sep: str) -> tuple:
    """Split into (before, sep, after) at the last occurrence using rpartition()."""
    pass
