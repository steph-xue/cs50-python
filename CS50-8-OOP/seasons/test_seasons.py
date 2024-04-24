# The "test_seasons" program is a unit test program to test the check_birthdate function in seasons.py
# Tests to make sure correct formats and incorrect formats for birthdates give proper outputs

from seasons import check_birthdate
import pytest


def main():
    test_correctformat()


# Testing to make sure correct formats and incorrect formats for birthdates give proper outputs
def test_correctformat():
    assert check_birthdate("2024-01-31") == (2024, 1, 31)
    assert check_birthdate("January 31, 1999") == None


if __name__ == "__main__":
    main()
