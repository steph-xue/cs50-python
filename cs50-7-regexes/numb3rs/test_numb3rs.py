# The "test_numb3rs" program is a unit test program to test the validate function in numb3rs.py
    # Checks for number tests and other input tests

from numb3rs import validate


def main():
    test_numbers()
    test_others()


# Checks for number tests
def test_numbers():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("300.300.300.300") == False
    assert validate("300.10.10.10") == False
    assert validate("10.300.300.300") == False


# Checks for other input tests
def test_others():
    assert validate("cat.dog.yes.no") == False
    assert validate("cat") == False


if __name__ == "__main__":
    main()
