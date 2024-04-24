# The "test_twttr" program is a unit test program to test the shorten function in twttr.py (for lowercase, uppercase, numbers and punctuation)

from twttr import shorten

def main():
    test_lower()
    test_upper()
    test_numbers()
    test_punctuation()


# Testing lowercase inputs
def test_lower():
    assert shorten("twitter") == "twttr"


# Testing uppercase inputs
def test_upper():
    assert shorten("TWITTER") == "TWTTR"


# Testing number inputs
def test_numbers():
    assert shorten("1234") == "1234"


# Testing punctuation inputs
def test_punctuation():
    assert shorten(".?!") == ".?!"


if __name__ == "__main__":
    main()
