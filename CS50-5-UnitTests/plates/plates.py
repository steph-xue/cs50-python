# The "plates" program allows the user to input a vanity license plate and it tells the user if it is valid or invalid

"""
Valid vanity license plate:
1. Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
2. All vanity plates must start with at least two letters
3. No periods, spaces, or punctuation marks are allowed
4. Numbers cannot be used in the middle of a plate; they must come at the end
"""


def main():

    # Gets user to input a vanity license plate
    plate = input("Plate: ")

    # Determines and prints if the vanity license plate is valid or invalid
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


# Determines if the vanity license plate is valid or invalid
def is_valid(s):

    # Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # All vanity plates must start with at least two letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Define the first number in the license plate
    firstnum = 0

    # Iterate through each character of the license plate
    for i in range(len(s)):

        # No periods, spaces, or punctuation marks are allowed
        if not s[i].isalnum():
            return False

        # Numbers cannot be used in the middle of a plate, they must come at the end
        if s[i].isdigit():
            firstnum += 1
            if s[i] == "0" and firstnum == 1:
                return False
            elif i < len(s) - 1 and s[i + 1].isalpha():
                return False

    # If it passes all the requirements, it is valid
    return True


if __name__ == "__main__":
    main()
