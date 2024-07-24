# The "bank" program allows the user to input a greeting
# If the greeting has "hello", then you get $0, if the greeting starts with "h", then you get $20, otherwise you get $100

def main():

    # Gets the user to input a greeting
    greeting = input("Greeting: ").strip().lower()

    # If the greeting has "hello", then you get $0, if the greeting starts with "h", then you get $20, otherwise you get $100
    if "hello" in greeting:
        print("$0")
    elif greeting[0] == "h":
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()
