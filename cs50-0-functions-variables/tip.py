# The "tip" program allows the user to input the cost of the meal and percentage they want to tip
# It tells the user the amount to tip in dollars

def main():

    # Gets the user to input the cost of the meal and percentage they want to tip
    dollars = dollars_to_float(input("How much was the meal?: "))
    percent = percent_to_float(input("What percentage would you like to tip?: "))

    # Calculates and prints out the amount to tip in dollars
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


# Takes the cost of the meal, removes the $, and converts it into a float
def dollars_to_float(d):
    d = float(d.replace("$", ""))
    return d


# Takes the tip percentage, removes the %, and converts it into a float decimal number
def percent_to_float(p):
    p = float(p.replace("%", ""))/100
    return p


if __name__ == "__main__":
    main()
