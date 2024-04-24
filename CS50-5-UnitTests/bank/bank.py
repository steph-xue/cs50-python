# The "bank" program allows the user to input a greeting
# If the greeting has "hello", then you get $0, if the greeting starts with "h", then you get $20, otherwise you get $100

def main():

    # Gets the user to input a greeting
    text = input("Greeting: ").strip().lower()

    # Determines the value of money you get depending on the greeting
    money = value(text)

    # Prints the value of money
    print(f"${money}")


def value(greeting):

    # If the greeting has "hello", then you get $0, if the greeting starts with "h", then you get $20, otherwise you get $100
    if greeting.startswith("hello"):
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
