import pytest
from app import add, sub, mul


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(5, 3) == 2


def test_mul():
    assert mul(4, 3) == 12


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (-1, 1, 0),
        (0, 0, 0),
    ],
)
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 2, 3),
        (0, 5, -5),
        (-3, -2, -1),
    ],
)
def test_sub_parametrized(a, b, expected):
    assert sub(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (-2, 3, -6),
        (0, 10, 0),
    ],
)
def test_mul_parametrized(a, b, expected):
    assert mul(a, b) == expected