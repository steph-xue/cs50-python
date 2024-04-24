# The "jar" program allows the user to use the Jar() class to create an object with a specific capacity of cookies to hold (or default capacity of 12)
# It then allows the user to deposit and withdraw cookies (starts at 0 cookies), print the object (number of cookies in emojis)
# It can also tell the user the current number of cookies and the capacity of the jar



class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be non-negative")
        self._capacity = capacity
        self._size = 0


    def __str__(self):
        return self._size * "🍪"


    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Deposit exceeds capacity")
        self._size += n


    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError("Not enough cookies to withdraw")
        self._size -= n


    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size
