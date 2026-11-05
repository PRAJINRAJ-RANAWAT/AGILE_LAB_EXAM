import pytest
from price import final_price


@pytest.mark.parametrize("price, tax, expected", [
    (100, 0.1, 110.0),
    (50, 0.2, 60.0),
    (19.99, 0.05, 20.99),
])
def test_normal_price(price, tax, expected):
    assert final_price(price, tax) == expected


def test_zero_price():
    assert final_price(0) == 0


@pytest.mark.parametrize("price, tax", [(-1, 0.1), (100, -0.5)])
def test_invalid_input(price, tax):
    with pytest.raises(ValueError):
        final_price(price, tax)


@pytest.mark.parametrize("price, tax, expected", [
    (0.01, 0.1, 0.01),
    (100, 0, 100),
    (100, 1, 200),
])
def test_boundary_values(price, tax, expected):
    assert final_price(price, tax) == expected
