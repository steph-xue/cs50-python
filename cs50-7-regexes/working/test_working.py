# The "test_working" program is a unit test program to test the convert function in working.py
# Tests for hour only conversions, hour and minute conversions, and ValueError (incorrect hours, incorrect minutes, incorrect format)

import pytest
from working import convert


def main():
    test_hour()
    test_hourmin()
    test_ValueError()


# Testing for hour only conversions
def test_hour():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"


# Testing for hour and minute conversions
def test_hourmin():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


# Testing for ValueError (incorrect hours, incorrect minutes, incorrect format)
def test_ValueError():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")


if __name__ == "__main__":
    main()
