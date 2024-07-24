# The "fuel" program allows the user to input the fraction of fuel left as x/y and it outputs the percentage of fuel left
# Outputs E if fuel left is <= 1% and F if fuel left is >= 99%
# It reprompts the user if there are non-integer fractions, if x > y, or if y = 0

def main():

    while True:
        try:
            # Gets the user to input the fraction of fuel left as x/y
            fraction = input("Fraction: ").strip()

            # Splits the fraction into integers x and y
            x,y = fraction.split("/")
            x = int(x)
            y = int(y)

            # Reprompts the user if x > y
            if x > y:
                continue

            # Calculate the percentage of fuel left
            z = x / y * 100

            # Outputs the fuel percentage, or E if fuel left is <= 1%, or F if fuel left is >= 99%
            if z <= 1:
                print("E")
            elif z >= 99:
                print("F")
            else:
                print(f"{round(z)}%")

        # Reprompts the user if there are non-integer fractions or if y = 0
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break


if __name__ == "__main__":
    main()
