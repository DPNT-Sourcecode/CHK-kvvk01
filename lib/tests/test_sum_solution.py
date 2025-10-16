import pytest
from lib.solutions.SUM.sum_solution import SumSolution


@pytest.fixture
def calculator():
    return SumSolution()


@pytest.mark.parametrize("x,y, expected", [
    (0, 1, 1),
    (2, 6, 8),
    (1, 100, 101),
])
    
def test_sum_with_valid_inputs(calculator, x, y, expected):
    assert calculator.sum(x, y) == expected
