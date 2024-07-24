# The "seasons" program allows the user to input a date of birth in the format year-month-day
# It then calculates and prints out the time difference between the date of birth and today's date in minutes (spelled out in words)

from datetime import date
import sys
import re
import inflect

p = inflect.engine()


def main():

    # Get user to input date of birth in format year-month-day
    birthdate = input("Date of Birth: ")

    # Checks the format of the date to see if it is valid (year-month-day), and extracts the year, month, and day as integers
    try:
        year, month, day = check_birthdate(birthdate)
    except:
        print("Invalid date format")
        sys.exit(1)

    # Gets the date of birth, checking to make sure it is a valid date
    try:
        date_of_birth = date(year, month, day)
    except ValueError:
        print("Invalid date")
        sys.exit(1)

    # Gets today's date
    date_of_today = date.today()

    # Determines the time difference between the date of birth and todays date
    timediff = date_of_today - date_of_birth

    # Converts the time difference to minutes
    timediffminutes = timediff.days * 24 * 60

    # Converts the time difference in minutes to words and prints it out (capitalized and without the 'and')
    timediffminwords = p.number_to_words(timediffminutes, andword="").capitalize()
    print(timediffminwords + " minutes")


# Checks the format of the date to see if it is valid (year-month-day), and extracts the year, month, and day as integers
def check_birthdate(birthdate):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birthdate):
        year, month, day = birthdate.split("-")
        return int(year), int(month), int(day)


if __name__ == "__main__":
    main()
