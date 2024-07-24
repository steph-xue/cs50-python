# The "meal" program gets the user to input the current time on a 24 clock and it outputs if it is breakfast, lunch, or dinner time
# Breakfast is between 7:00 to 8:00, lunch is between 12:00 to 13:00, and dinner is between 18:00 to 19:00

def main():

    # Gets the user to input the current time on a 24 clock
    time = input("What time is it?: ").strip()

    # Converts the time on a 24 clock to number of hours (float)
    hours = convert(time)

    # Determines and prints out if it is breakfast, lunch, or dinner time depending
    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")


# Converts the time on a 24 clock to number of hours (float)
def convert(time):
    splittime = time.split(":")
    hours = float(splittime[0]) + float(splittime[1])/60
    return hours


if __name__ == "__main__":
    main()
