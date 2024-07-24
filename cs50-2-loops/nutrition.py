# The "nutrition" program allows the user to input a fruit and then prints out the corresponding calories
# This is based on the The U.S. Food & Drug Adminstration (FDA) nutrition information for the 20 most frequently consumed raw fruits

def main():

    # Defines fruits and their calories in a dictionary
    fruitlist = {
        "apple" : 130,
        "avocado" : 50,
        "banana" : 110,
        "cantaloupe" : 50,
        "grapefruit" : 60,
        "grapes" : 90,
        "honeydew melon" : 50,
        "kiwifruit" : 90,
        "lemon" : 15,
        "lime" : 20,
        "nectarine" : 60,
        "orange" : 80,
        "peach" : 60,
        "pear" : 100,
        "pineapple" : 50,
        "plums" : 70,
        "stawberries" : 50,
        "sweet cherries" : 100,
        "tangerine" : 50,
        "watermelon" : 80,
    }

    # Gets user to input a fruit
    item = input("Item: ").lower()

    # If the fruit is in the dictionary, it prints out the corresponding calories
    if item in fruitlist:
        print(f"Calories: {fruitlist[item]}")


if __name__ == "__main__":
    main()
