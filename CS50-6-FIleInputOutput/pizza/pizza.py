# The "pizza" program allows the user to input a pizza menu csv file as a command-line argument, and prints it out in a table format

import sys
import csv
from tabulate import tabulate


def main():

    # Must have exactly 1 command-line argument
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

    # Command-line argument must be a csv file (ends with .csv)
    if not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)

    # Create an empty table
    table = []

    # Try to open file
    try:
        with open(sys.argv[1]) as file:
            # Add csv file as a list of lists to the empty table
            filereader = csv.reader(file)
            for row in filereader:
                table.append(row)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

    # Print the table contents 
    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))


if __name__ == "__main__":
    main()
