# The "test_um" program is a unit test program to test the count function in um.py
# Tests for um in words, um surrounded by space, and um with other variations of upper/lower case

from um import count

def main():
    test_inword()
    test_surroundedbyspace()
    test_upperlower()


# Testing for um in words
def test_inword():
    assert count("Yummy") == 0


# Testing for um surrounded by space
def test_surroundedbyspace():
    assert count("Ok um ok") == 1
    assert count("Ok um ok um ok") == 2


# Testing for um with other variations of upper/lower case
def test_upperlower():
    assert count("Um, ok") == 1
    assert count("Um, thanks, um...") == 2
    assert count("um?") == 1


if __name__ == "__main__":
    main()
