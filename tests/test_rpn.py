from app.core.rpn import rpn_calculator

def test_rpn_calculator():
    assert rpn_calculator("5 1 2 + 4 * + 3 -") == 14.0

def test_rpn_invalid_operator():
    try:
        rpn_calculator("2 3 &")
        assert False, "Should raise ValueError for invalid operator"
    except ValueError:
        pass

def test_rpn_insufficient_operands():
    try:
        rpn_calculator("2 +")
        assert False, "Should raise ValueError for insufficient operands"
    except ValueError:
        pass

def test_rpn_empty_expression():
    try:
        rpn_calculator("")
        assert False, "Should raise ValueError for empty expression"
    except ValueError:
        pass

def test_rpn_division_by_zero():
    try:
        rpn_calculator("4 0 /")
        assert False, "Should raise ZeroDivisionError for division by zero"
    except ZeroDivisionError:
        pass

def test_rpn_too_many_operands():
    try:
        rpn_calculator("2 3 4 +")
        assert False, "Should raise ValueError for too many operands left"
    except ValueError:
        pass

def test_rpn_only_operators():
    try:
        rpn_calculator("+ - * /")
        assert False, "Should raise ValueError for operators without operands"
    except ValueError:
        pass

def test_rpn_whitespace_only():
    try:
        rpn_calculator("   ")
        assert False, "Should raise ValueError for whitespace-only expression"
    except ValueError:
        pass

def test_rpn_non_numeric_token():
    try:
        rpn_calculator("2 a +")
        assert False, "Should raise ValueError for non-numeric token"
    except ValueError:
        pass