def rpn_calculator(expression: str) -> float:
    stack: list[float] = []
    for token in expression.split():
        if token in {"+", "-", "*", "/"}:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
        else:
            stack.append(float(token))
    if len(stack) != 1:
        raise ValueError("Invalid RPN expression: stack should contain exactly one element after evaluation.")
    return stack[0]
