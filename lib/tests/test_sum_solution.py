import pytest
from lib.solutions.SUM.sum_solution import SumSolution


@pytest.fixture
def calculator():
    return SumSolution()


@pytest.mark.parametrize("x,y,expected", [
    (0, 1, 1),
    (2, 6, 8),
    (1, 100, 101),
])

def test_sum_with_valid_inputs(calculator, x, y, expected):
    assert calculator.sum(x, y) == expected


@pytest.mark.parametrize("x,y", [
    (-1, 1),
    (2, 101),
])

def test_sum_raises_value_error_for_out_of_range(calculator, x,y):
    with pytest.raises(ValueError):
        calculator.sum(x,y)


@pytest.mark.parametrize("x,y", [
    (8, None),
    (9, "9"),
    (10, [20]),
])

def test_sum_raises_type_error_for_non_ints(calculator, x,y):
    with pytest.raises(TypeError):
        calculator.sum(x,y)




