# The "indoor" program allows the user to input text and then converts it to an indoor voice (lowercase)

def main():

    # Gets the user to input text and converts it to an indoor voice (lowercaes) to print out
    text = input("Type in text: ").strip().lower()
    print(text)

if __name__ == "__main__":
    main()
