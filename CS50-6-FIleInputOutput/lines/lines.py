# The "lines" program allows the user to input a python file as a command-line argument and then prints out how many lines of code there are in the file
    # Run the code as python lines.py [_.py]
# Comments and blank lines do not count as lines of code

import sys

def main():

    # Must have exactly 1 command-line argument
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

    # Command-line argument must be a python file (ends with .py)
    if not sys.argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit(1)

    # Sets initial number of code lines as 0
    codelines = 0

    try:
        # Opens up the python file inputed as a command-line argument
        with open(sys.argv[1]) as file:
            # Checks each line in the line to see if it as actual line of code (no comments or blank lines) to add to the codeline count
            for line in file:
                if line.lstrip().startswith("# ") or line.isspace():
                    continue
                else:
                    codelines += 1
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

    # Prints the total number of code lines in the file
    print(codelines)

if __name__ == "__main__":
    main()
