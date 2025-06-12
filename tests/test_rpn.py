from app.core.rpn import rpn_calculator

def test_rpn_calculator():
    assert rpn_calculator("5 1 2 + 4 * + 3 -") == 14.0
