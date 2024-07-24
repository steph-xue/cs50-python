# The "um" program allows the user to input text and it prints out how many counts of "um" there are in the text (not including within words e.g. yummy)

import re
import sys


def main():
    # Gets the user to input text, determines how many counts of "um" there are (not including within words e.g. yummy), and prints out the count
    print(count(input("Text: ")))


def count(s):
    # Determines how many counts of "um" there are (not including within words e.g. yummy),
    return len(re.findall(r"\b\W*um\b\W*", s, re.IGNORECASE))


if __name__ == "__main__":
    main()
