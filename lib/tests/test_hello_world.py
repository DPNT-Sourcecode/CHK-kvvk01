import pytest

from lib.solutions.HLO.hello_solution import HelloSolution


def test_hello_world_msg_for_valid_string():

    h = HelloSolution()
    actual = h.hello("Mr. X")
    assert actual == "Hello, Mr. X!"





