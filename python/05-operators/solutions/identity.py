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
            return Result.IS_NOT_NONE if x is not None else Result.IS_NONE
        case "is true":
            return Result.IS_TRUE if x is True else Result.IS_NOT_TRUE
        case "is not true":
            return Result.IS_NOT_TRUE if x is not True else Result.IS_TRUE
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
            return Result.SAME if x != y else Result.DIFFERENT
        case _:
            raise ValueError(f"Unknown operator: {op}")
