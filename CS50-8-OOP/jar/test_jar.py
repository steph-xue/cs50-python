# The "test_jar" program is a unit test program to test the Jar class in jar.py
# Tests the Jar class in initializing the capacity, printing the object (in emojis), depositing cookies, and withdrawing cookies)


import pytest
from jar import Jar


# Testing the Jar class in initializing the capacity
def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar2 = Jar(3)
    assert jar2.capacity == 3


# Testing the Jar class in printing the object (in emojis)
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


# Testing the Jar class in depositing cookies
def test_deposit():
    jar = Jar()
    jar.deposit(6)
    assert jar.size == 6
    jar.deposit(3)
    assert jar.size == 9
    with pytest.raises(ValueError):
        assert jar.deposit(13)


# Testing the Jar class in withdrawing cookies
def test_withdraw():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(3)
    assert jar.size == 3
    jar.withdraw(1)
    assert jar.size == 2
    with pytest.raises(ValueError):
        assert jar.withdraw(13)
