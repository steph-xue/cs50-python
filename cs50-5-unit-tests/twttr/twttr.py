# The "twttr" program allows the user to input text and it outputs the text with all vowels removed

def main():

    # Gets user to input text
    text = input("Input: ")

    # Removes vowels from inputed text
    shortenedtext = shorten(text)

    # Prints out the output text without vowels
    print(f"Output: {shortenedtext}")


# Removes vowels from inputed text
def shorten(word):

    # Create new word for removing vowe,s
    word_without_vowels = ""

    # Iterates through each character and adds non-vowels to the new word
    for letter in word:
        if letter.lower() == "a" or letter.lower() == "e" or letter.lower() == "i" or letter.lower() == "o" or letter.lower() == "u":
            continue
        else:
            word_without_vowels += letter
    return word_without_vowels


if __name__ == "__main__":
    main()
