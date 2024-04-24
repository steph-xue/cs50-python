# The "twttr" program allows the user to input text and it outputs the text with all vowels removed

def main():

    # Gets user to input text
    text = input("Input: ")

    # Prints out the header for the output
    print("Output: ", end="")

    # Iterates through each character and prints out non-vowels
    for letter in text:
        if letter.lower() == "a" or letter.lower() == "e" or letter.lower() == "i" or letter.lower() == "o" or letter.lower() == "u":
            continue
        else:
            print(letter, end="")
    print()


if __name__ == "__main__":
    main()
