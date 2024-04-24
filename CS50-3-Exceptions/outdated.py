# The "outdated" program allows the user to input a date in the format month/date/year or month date, year (middle-endian format)
# The program outputs the date in year-month-day (YYYY-MM-DD) order

def main():

    # Define list of months
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        # Gets user to input a date in the format month/date/year or month date, year (middle-endian format)
        date = input("Date: ").strip().capitalize()
        try:
            # If in format month/date/year, splits into 3 variables and checks to make sure month (1-12) and day (1-31) is valid
            month, day, year = date.split("/")
            if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                break
        except:
            try:
                # If in format month date, year, splits into 3 variables
                oldmonth, oldday, year = date.split(" ")

                # Reprompts the user if there is no comma
                if "," not in date:
                    raise SyntaxError

                # Checks if the month inputed is in the months list and outputs the month in a number format
                for i in range(len(months)):
                    if oldmonth == months[i]:
                        month = i + 1

                # Removes the comma from the day
                day = oldday.replace(",", "")

                # Checks to make sure month (1-12) and day (1-31) is valid
                if (int(month) >= 1 and int(month <= 12)) and (int(day) >= 1 and int(day) <= 31):
                    break
            # Reprompts the user if trying fails
            except:
                pass

    # Prints out the date in year-month-day (YYYY-MM-DD) order
    print(f"{year}-{int(month):02}-{int(day):02}")


if __name__ == "__main__":
    main()
