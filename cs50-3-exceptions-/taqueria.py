# The "taqueria" program allows the user to input taqueria menu items one by one and tells the user the total cost after each item is added
# Once finished adding items, pressing Enter will exit the program

def main():

    # Define dictionary of taqueria menu items and corresponding costs
    taqueria = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    # Set total cost initally to 0
    total = 0

    while True:
        try:
            # Gets user to input a menu item
            item = input("Item: ").lower().title()

            # If nothing is inputed and Enter is pressed, then the program exits
            if item == "":
                break
            # If the item inputed is in the taqueria menu, the cost is added to the total cost and then it is printed out
            else:
                if item in taqueria:
                    total = total + taqueria[item]
                    print(f"Total: ${total:.2f}")
        except (EOFError, KeyError):
            break


if __name__ == "__main__":
    main()
