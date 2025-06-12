from typing import Callable


calculation_dictionary: dict[str, Callable[[float, float], float]] = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}

def rpn_calculator(expression: str) -> float:
    stack: list[float] = []

    if not expression.strip():
        raise ValueError("Empty expression")

    for token in expression.split():
        if token in calculation_dictionary:
            
            try:
                b = stack.pop()
                a = stack.pop()
            except IndexError:
                raise ValueError("Insufficient operands")

            stack.append(calculation_dictionary[token](a, b))
        else:
            try:
                stack.append(float(token))
            except ValueError:
                raise ValueError(f"Invalid token: {token}")

    if len(stack) != 1:
        raise ValueError("Invalid RPN expression: stack should contain exactly one element after evaluation.")

    return stack[0]
