# The "figlet" program allows the user to input a text to convert to an output with a specialized font
# The user can type in 0 command-line arguments (randomized font) or type "-f" or "--font" followed by the font name as 2 command-line arguments

import sys
import random
from pyfiglet import Figlet

def main():

    # Rename the figlet functio
    figlet = Figlet()

    # If no command-line arguments, font is randomized
    if len(sys.argv) == 1:
        randomfont = True
    # If 2 command-line arguments, (first is either "-f" or "--font" followed by the font name), font is specified by the 2nd command-line argument
    elif len(sys.argv) == 3:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            print("First command-line argument must be -f or --font")
            sys.exit(1)
        randomfont = False
    else:
        print("Must have 0 or 2 command-line arguments")
        sys.exit(1)

    # Gets a list of all the fonts
    figlet.getFonts()

    # If the font is supposed to be randomized, select a random choice from the list of fonts
    if randomfont == True:
        font = random.choice(figlet.getFonts())
        figlet.setFont(font=font)
    # If the font is not randomized, try the 2nd command-line argument font
    else:
        try:
            figlet.setFont(font=sys.argv[2])
        except:
            print("Font not found")
            sys.exit(1)

    # Gets user to input the message and prints it out converted to the randomized/non-randomized font
    message = input("Input: ")
    print(f"Output: {figlet.renderText(message)}")


if __name__ == "__main__":
    main()
