def assignment(x: float, n: float, op: str) -> float:
    """
    Return the value after applying the assignment operator.
    op: one of "=", "+=", "-=", "*=", "/=", "%=", "//=", "**="
    """
    match op:
        case "=":
            x = n
        case "+=":
            pass
        case "-=":
            pass
        case "*=":
            pass
        case "/=":
            pass
        case "%=":
            pass
        case "//=":
            pass
        case "**=":
            pass
        case _:
            raise ValueError(f"Unknown operator: {op}")
    return x


def walrus(value: float) -> float:
    """Use := to assign value to a variable and return it in one expression."""
    pass  # noqa: F841
