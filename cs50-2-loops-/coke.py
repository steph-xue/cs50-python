# The "coke" program simulates a coke machine where each coke costs 50 cents
# The user can insert 25, 10, and 5 cent coins and the program will tell you how many cents are left or will tell you the change owed
# The program doesn't except coins other than those listed above

def main():

    # Cents due for a coke is initially set as 50 cents
    centsleft = 50

    while True:

        # Prints the amount of cents left to give
        print(f"Amount Due: {centsleft}")

        # Gets user to input the coin inserted (25, 10, or 5 cent coins)
        cents = int(input("Insert Coin: ").strip())

        # If the coin inserted is less than the cents due and it is a valid coin, then the remaining cents due is calculated and the loop repeats
        if cents <= centsleft and (cents == 25 or cents == 10 or cents == 5):
            centsleft = centsleft - cents

            # If the cents left is calculated to be 0, then it prints that there is no change due
            if centsleft == 0:
                print(f"Change Owed: {centsleft}")
                break

        # If the coin inserted is more than the cents due and it is a valid coin, then the change owed is calculated and printed
        elif cents > centsleft and (cents == 25 or cents == 10 or cents == 5):
            change = cents - centsleft
            print(f"Change Owed: {change}")
            break


if __name__ == "__main__":
    main()
