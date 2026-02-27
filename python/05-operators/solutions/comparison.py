from enum import StrEnum


class Result(StrEnum):
    EQUAL = "equal"
    NOT_EQUAL = "not equal"
    GREATER = "greater"
    NOT_GREATER = "not greater"
    LESS = "less"
    NOT_LESS = "not less"
    GREATER_OR_EQUAL = "greater or equal"
    LESS_OR_EQUAL = "less or equal"


def comparison(x: float, y: float, op: str) -> str:
    """
    Apply the comparison operator op to x and y, return a string describing the result.
    op: one of "==", "!=", ">", "<", ">=", "<="
    """
    match op:
        case "==":
            return Result.EQUAL if x == y else Result.NOT_EQUAL
        case "!=":
            return Result.NOT_EQUAL if x != y else Result.EQUAL
        case ">":
            return Result.GREATER if x > y else Result.NOT_GREATER
        case "<":
            return Result.LESS if x < y else Result.NOT_LESS
        case ">=":
            return Result.GREATER_OR_EQUAL if x >= y else Result.LESS
        case "<=":
            return Result.LESS_OR_EQUAL if x <= y else Result.GREATER
        case _:
            raise ValueError(f"Unknown operator: {op}")
