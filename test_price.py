import pytest
from price import final_price


def test_normal_price():
    assert final_price(100, 0.1) == 110


def test_zero_price():
    assert final_price(0, 0.1) == 0


def test_invalid_price():
    with pytest.raises(ValueError):
        final_price(-5, 0.1)


def test_boundary_tax():
    assert final_price(100, 0) == 100
