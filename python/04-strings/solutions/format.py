def fstring_example(name: str, score: float) -> str:
    """Return a string using an f-string with variables: 'Name: {name}, Score: {score}'."""
    return f"Name: {name}, Score: {score}"


def decimal_format(x: float) -> str:
    """Format the float to 2 decimal places using :.2f in an f-string."""
    return f"{x:.2f}"


def expr_in_fstring(x: int, y: int) -> str:
    """Return an f-string with a mathematical expression inside braces: '{x}*{y}={x*y}'."""
    return f"{x}*{y}={x * y}"


def format_method(template: str, a: str, b: str) -> str:
    """Fill the template's placeholders using the format() method with a and b."""
    return template.format(a, b)


def centered(s: str, width: int) -> str:
    """Return the string centered in a string of given width using center()."""
    return s.center(width)


def left_justified(s: str, width: int) -> str:
    """Return the string left-justified in a string of given width using ljust()."""
    return s.ljust(width)


def right_justified(s: str, width: int) -> str:
    """Return the string right-justified in a string of given width using rjust()."""
    return s.rjust(width)


def zfill_str(s: str, width: int) -> str:
    """Pad the string with zeros on the left to reach width using zfill()."""
    return s.zfill(width)
