#

import pytest
from fuel import convert, gauge

def main():
    test_fraction()
    test_ZeroDivisionError()
    test_ValueError()


def test_fraction():
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("99/100") == 99 and gauge(99) == "F"
    assert convert("1/4") == 25 and gauge(25) == "25%"


def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        assert convert("1/0")


def test_ValueError():
    with pytest.raises(ValueError):
        assert convert("hi/there")


if __name__ == "__main__":
    main()
