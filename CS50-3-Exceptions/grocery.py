# The "grocery" program allows the user to input grocery items one at a time and returns the list of grocery items and corresponding counts
# Once the user is finished adding items to the grocery list, they can press Enter

from collections import OrderedDict

def main():

    # Creates the grocery list
    grocery = {}

    while True:
        try:
            # Gets the user to input grocery items one at a time
            item = input().strip().upper()

            # If Enter is pressed, the user has finished inputing grocery items
            if item == "":
                break
            # If the item is in the grocery dictionary, add 1 to the count and if not, add it to the dictionary
            elif item in grocery:
                grocery[item] += 1
            else:
                grocery[item] = 1
        except (EOFError, KeyError):
            break
        else:
            continue

    # Sort the dictionary of grocery items
    sortedgrocery = OrderedDict(sorted(grocery.items()))

    # Print out each grocery item and corresponding counts
    for item in sortedgrocery:
        print(f"{sortedgrocery[item]} {item}")
        

if __name__ == "__main__":
    main()
