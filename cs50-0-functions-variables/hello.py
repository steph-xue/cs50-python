# The "hello" program allows the user to input their name and outputs hello and then their name

# Main function gets the user to input their name and calls the hello function to print hello and then their name
def main():
    name = input("What is your name?: ").strip().title()
    hello(name)

# The hello function prints hello and then their name
def hello(n="world"):
    print(f"hello, {n}")

if __name__ == "__main__":
    main()
