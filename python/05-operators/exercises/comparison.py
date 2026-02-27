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
            pass
        case ">":
            pass
        case "<":
            pass
        case ">=":
            pass
        case "<=":
            pass
        case _:
            raise ValueError(f"Unknown operator: {op}")
