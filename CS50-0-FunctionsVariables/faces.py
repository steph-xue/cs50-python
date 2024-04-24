# The "faces" program allows the user to input text with :) or :( and it returns the text converting these faces to emojis

def main():

    # Gets the user to input text with :) or :(
    text = input("Type text here: ").strip()

    # Prints out the text converting these faces to emojis
    newtext = convert(text)
    print(newtext)


# Converts the :) or :( faces to emojis
def convert(str):
    str = str.replace(":)", "🙂").replace(":(", "🙁")
    return str

if __name__ == "__main__":
    main()
