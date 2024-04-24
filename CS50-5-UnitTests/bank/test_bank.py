# The "test_bank" program is a unit test program to test the value function in bank.py (for outputs of 0, 20, and 100)


from bank import value


def main():
    test_0()
    test_20()
    test_100()


# Testing output of 0
def test_0():
    assert value("hello there") == 0
    assert value("Hello") == 0


# Testing output of 20
def test_20():
    assert value("hi there") == 20
    assert value("Hey") == 20


# Testing output of 100
def test_100():
    assert value("what is up") == 100
    assert value("Greetings") == 100


if __name__ == "__main__":
    main()
