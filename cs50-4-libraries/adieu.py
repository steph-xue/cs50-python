# The "adieu" program allows the user to type in names until Enter or cmd D is pressed, and will print out the adieu lyrics with each name

import inflect
p = inflect.engine()

def main():

    # Create an empty list of names
    names = []

    while True:
        try:
            # Get user to input names until Enter or cmd D is pressed
            name = input("Name: ").strip()

            # Break out of loop if Enter is pressed
            if name == "":
                break

            # Add name to names list
            names.append(name)
        except EOFError:
            break

    # Join names together with commas and 'and'
    mylist = p.join(names)

    # Print out the adieu lyrics with the joined names
    print(f"Adieu, adieu, to {mylist}")


if __name__ == "__main__":
    main()
