# The "camel" program allows the user to input text in camelCase and will print it out in snake_case

def main():

    # Gets the user to input text in camelCase
    text = input("camelCase: ").strip()

    # Prints header for snake_case conversion
    print("snake_case: ", end="")

    # Iterates through each character in the text
    # If uppercase, turns the character to lowercase and puts an underscore in front
    for letter in text:
        if letter.isupper():
            print("_" + letter.lower(), end="")
        else:
            print(letter, end="")
    print()


if __name__ == "__main__":
    main()
