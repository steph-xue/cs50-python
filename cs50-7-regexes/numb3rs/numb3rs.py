# The "numb3rs" program allows the user to input a IPv4 address as #.#.#.# where each number is in the range 0-255
# It tells the user if it is a valid IPv4 address (consistent format, numbers in range, only numbers)

import re
import sys


def main():
    # Gets IPv4 address from user, validates it, and prints out if the IPv4 address is valid or not
    print(validate(input("IPv4 Address: ").strip()))


# Determines if the IPv4 address is valid or not
def validate(ip):

    # Searches the IPv4 address using regular expressions
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        numbers = ip.split(".")
        
        # Each number must be between 0 and 255
        for number in numbers:
            if int(number) < 0 or int(number) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
