# The "comparexy" program allows the user to input x and y and tells the user if x is less than, greater than, or equal to y

def main():

    # Gets the user to input an integer for x and y
    x = int(input("What is x?: "))
    y = int(input("What is y?: "))

    # Tells the user if x is less than, greater than, or equal to y
    if x < y:
        print("x is less than y")
    elif x > y:
        print("x is greater than y")
    else:
        print("x is equal to y")

if __name__ == "__main__":
    main()
