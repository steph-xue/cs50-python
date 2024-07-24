# The "test_plates" program is a unit test program to test the is_valid function in plates.py
    # Checks for beginning alphabetical start (2 letters), length (2-6 characters), number placement (not in middle, only at end)
    # Also checks for zero placement (not first number), and alphanumeric characters only (no punctuation)

from plates import is_valid


def main():
    test_2letterstart()
    test_charmax()
    test_num()
    test_punct()


# Checks for beginning alphabetical start (2 letters)
def test_2letterstart():
    assert is_valid("CS") == True
    assert is_valid("5C") == False
    assert is_valid("55") == False


# Checks for correct length (2-6 characters)
def test_charmax():
    assert is_valid("CS") == True
    assert is_valid("C") == False
    assert is_valid("CSCS500") == False


# Checks for number placement (not in middle, only at end) and zero placement (not first number)
def test_num():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False


# Checks for alphanumeric characters only (no punctuation)
def test_punct():
    assert is_valid("CS.50") == False


if __name__ == "__main__":
    main()
