from enum import StrEnum


class Result(StrEnum):
    SAME = "same"
    DIFFERENT = "different"
    IS_NONE = "is none"
    IS_NOT_NONE = "is not none"
    IS_TRUE = "is true"
    IS_NOT_TRUE = "is not true"


def identity_check(x, op: str) -> str:
    """
    Apply identity operator for x and None or True.
    op: "is", "is not" (for None), "is true", "is not true"
    Returns: "is none", "is not none", "is true", or "is not true".
    """
    match op:
        case "is":
            return Result.IS_NONE if x is None else Result.IS_NOT_NONE
        case "is not":
            pass
        case "is true":
            pass
        case "is not true":
            pass
        case _:
            raise ValueError(f"Unknown operator: {op}")


def equality_check(x, y, op: str) -> str:
    """
    Apply equality operator for values.
    op: "==", "!="
    Returns: "same" or "different".
    """
    match op:
        case "==":
            return Result.SAME if x == y else Result.DIFFERENT
        case "!=":
            pass
        case _:
            raise ValueError(f"Unknown operator: {op}")
