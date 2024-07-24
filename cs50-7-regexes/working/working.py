# The "working" program allows the user to input a time range in a 12 hour clock in the following formats:
    # No minutes (e.g. 12 PM to 3 AM) or with minutes (e.g. 12:45 AM to 3:50 PM)
# The program will then convert the time to a 24 hour clock

import re
import sys


def main():
    # Gets the user to input a time range in a 12 hour clock (with or without minutes), converts it to a 24 hour clock, and prints the time range out
    print(convert(input("Hours: ").strip()))


def convert(s):
    # Checks if the 12 hour clock time is in the correct format, otherwise will raise a ValueError
    if time := re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s):

        # Checks to see if the hour is within range (< 12)
        if int(time.group(2)) > 12 or int(time.group(6)) > 12:
            raise ValueError

        # Checks to see if the minutes are within range (< 59) (if minutes are even specified)
        if time.group(3) != None or time.group(7) != None:
            if int(time.group(3)) > 59 or int(time.group(7)) > 59:
                raise ValueError

        # Gets the 12 hour clock string for each time (using the hours, minutes, and AM/PM specified for each time in the input string)
        firsttime = new_format(time.group(2), time.group(3), time.group(4))
        secondtime = new_format(time.group(6), time.group(7), time.group(8))

        # Adds the two 12 hour clock strings together to complete the time range
        return firsttime + " to " + secondtime

    else:
        raise ValueError


# Gets the 12 hour clock string for each time (using the hours, minutes, and AM/PM specified for each time in the input string)
def new_format(hour, min, am_pm):

    # If time in PM, converts the hours accordingly
    if am_pm == "PM":
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = 12 + int(hour)

    # If time in AM, converts the hours accordingly
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)

    # If no minutes specified, input 0
    if min == None:
        min = "00"

    # Returns the time with hour and minutes
    return f"{new_hour:02}:{min}"


if __name__ == "__main__":
    main()
