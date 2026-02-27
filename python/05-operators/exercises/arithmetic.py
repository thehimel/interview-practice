def arithmetic(x: float, y: float, op: str) -> float:
    """
    Apply the arithmetic operator op to x and y.
    op: one of "+", "-", "*", "/", "%", "**", "//"
    """
    match op:
        case "+":
            return x + y
        case "-":
            pass
        case "*":
            pass
        case "/":
            pass
        case "%":
            pass
        case "**":
            pass
        case "//":
            pass
        case _:
            raise ValueError(f"Unknown operator: {op}")
