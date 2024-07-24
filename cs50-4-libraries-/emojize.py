# The "emojize" program allows the user to input an emoji code or alias in when prompted for text and it outputs the text with emojis

import emoji

def main():

    # Gets user to input text with emoji code or alias
    text = input("Input: ")

    # Converts and prints out the text with emojis
    output = emoji.emojize(text, language='alias')
    print("Output:", output)
    

if __name__ == "__main__":
    main()
