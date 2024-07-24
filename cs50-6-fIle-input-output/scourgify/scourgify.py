# The "scourgify" program allows the user to input 2 command-line arguments as csv input and output files:
    # python scoourgify.py [input.csv] [output.csv]
# The program takes the 1st csv file (name and house as dictionaries) and cleans it up
# It outputs it into the 2nd csv file (first name, last name, and house as dictionaries)

import csv
import sys


def main():

    # Must have 2 command-line arguments
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    # Creating an empty table to fill the new list of dictionaries (first name, last name, house)
    table = []

    # Try to open the input csv file
    try:
        with open(sys.argv[1], "r") as inputfile:
            # Read the csv input file and splits the name into first and last names, then adds these as a dictionary to the empty table list
            filereader = csv.DictReader(inputfile)
            for row in filereader:
                last, first = row["name"].split(",")
                table.append({"first": first.strip(), "last": last.strip(), "house": row["house"].strip()})
    except FileNotFoundError:
        print("Could not read invalid_file.csv")
        sys.exit(1)

    # Open the output csv file
    with open(sys.argv[2], "w") as outputfile:
        # Write each row as a csv dictionary (including a header)
        writer = csv.DictWriter(outputfile, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in table:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})


if __name__ == "__main__":
    main()
