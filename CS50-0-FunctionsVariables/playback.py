# The "playback" program allows the user to input text and then outputs the text with a pause between word (replaces spaces with ...)

def main():

    # Gets the user to input text and replaces the spaces with ... to print out
    text = input("Type in text: ").strip().replace(" ", "...")
    print(text)

if __name__ == "__main__":
    main()
