# The "einstein" program allows the user to input a mass (in kg) and outputs the energy (in Joules) using the formula E = mc^2

def main():

    # Gets the user to input a mass (in kg)
    m = int(input("m (in kg): "))

    # Prints out the energy (in Joules) using the formula E = mc^2
    E = m * (300000000)**2
    print(f"E: {E}")

if __name__ == "__main__":
    main()
