import pytest
from Solved import withdraw


def test_valid_withdrawal():
    assert withdraw(1000, 200) == 800


def test_zero_amount():
    with pytest.raises(ValueError):
        withdraw(1000, 0)


def test_negative_amount():
    with pytest.raises(ValueError):
        withdraw(1000, -100)


def test_insufficient_balance():
    with pytest.raises(ValueError):
        withdraw(500, 600)


def test_invalid_type():
    with pytest.raises(TypeError):
        withdraw(1000, "100")
