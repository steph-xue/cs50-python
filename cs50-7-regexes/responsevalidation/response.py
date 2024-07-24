# The "response" program allows the user to input an email address and it tells the user if it is valid or invalid

import validators


def main():
    if validators.email(input("What's your email address? ")):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
