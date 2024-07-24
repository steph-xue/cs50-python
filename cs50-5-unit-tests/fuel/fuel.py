# The "fuel" program allows the user to input the fraction of fuel left as x/y and it outputs the percentage of fuel left
# Outputs E if fuel left is <= 1% and F if fuel left is >= 99%
# It reprompts the user if there are non-integer fractions, if x > y, or if y = 0

def main():

    # Gets the user to input the fraction of fuel left as x/y
    fraction = input("Fraction: ").strip()

    # Converts the string X/Y into a percentage rounded to the nearest int (between 0-100)
    z = convert(fraction)

    # Converts the fuel percentage (int) into an output (string) as the fuel percentage, or E if fuel left is <= 1%, or F if fuel left is >= 99%
    fuel = gauge(z)

    # Prints the output of fuel left as the percentage of fuel left, or E if fuel left is <= 1%, or F if fuel left is >= 99%
    print(fuel)



# Converts the string X/Y into a percentage rounded to the nearest int (between 0-100)
def convert(fraction):

    while True:
        try:
            # Splits the fraction into integers x and y
            x,y = fraction.split("/")
            x = int(x)
            y = int(y)

            # Get the fraction in decimal value
            z = x / y

            # If x < y, then return the percentage to the nearest integer
            if z <=1:
                return round(z * 100)
            # If x > y, then reprompt the user
            else:
                fraction = input("Fraction: ").strip()
                pass
        except (ValueError, ZeroDivisionError):
            raise


# Converts the fuel percentage (int) into an output (string) as the fuel percentage, or E if fuel left is <= 1%, or F if fuel left is >= 99%
def gauge(percentage):

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
