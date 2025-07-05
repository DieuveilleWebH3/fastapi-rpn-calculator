import pytest
from app.core.rpn import rpn_calculator

def test_rpn_calculator():
    assert rpn_calculator("5 1 2 + 4 * + 3 -") == 14.0

def test_rpn_invalid_operator():
    with pytest.raises(ValueError, match="Invalid token|operator"):
        rpn_calculator("2 3 &")

def test_rpn_insufficient_operands():
    with pytest.raises(ValueError, match="Insufficient operands"):
        rpn_calculator("2 +")

def test_rpn_empty_expression():
    with pytest.raises(ValueError, match="Empty expression"):
        rpn_calculator("")

def test_rpn_division_by_zero():
    with pytest.raises(ZeroDivisionError, match="Division by zero is not allowed"):
        rpn_calculator("4 0 /")

def test_rpn_too_many_operands():
    with pytest.raises(ValueError):
        rpn_calculator("2 3 4 +")

def test_rpn_only_operators():
    with pytest.raises(ValueError):
        rpn_calculator("+ - * /")

def test_rpn_whitespace_only():
    with pytest.raises(ValueError):
        rpn_calculator("   ")

def test_rpn_non_numeric_token():
    with pytest.raises(ValueError):
        rpn_calculator("2 a +")

