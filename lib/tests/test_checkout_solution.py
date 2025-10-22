



# python
# tests/test_checkout_solution.py
import pytest
from lib.solutions.CHK.checkout_solution import CheckoutSolution

@pytest.fixture
def solver():
    return CheckoutSolution()

def test_empty_basket_returns_zero(solver):
    assert solver.checkout("") == 0

@pytest.mark.parametrize("input_val", [None, 123, [], {}])
def test_non_string_input_returns_minus_one(solver, input_val):
    assert solver.checkout(input_val) == -1
#
def test_invalid_sku_returns_minus_one(solver):
    assert solver.checkout("A≈") == -1
    assert solver.checkout("a") == -1

def test_single_items(solver):
    assert solver.checkout("A") == 50

def test_offers_A(solver):
    assert solver.checkout("AAA") == 130
    # assert solver.checkout("AAAA") == 180
    # assert solver.checkout("AAAAAA") == 260
#
# def test_offers_B(solver):
#     assert solver.checkout("BB") == 45
#     assert solver.checkout("BBB") == 75
#
# def test_mixed_basket(solver):
#     # A x4 -> 130 + 50 = 180, B x2 -> 45, C -> 20, D -> 15 => total 260
#     assert solver.checkout("ABCDABA") == 260
#
# def test_idempotent_calls(solver):
#     inp = "AAAB"
#     first = solver.checkout(inp)
#     second = solver.checkout(inp)
#     assert first == second

