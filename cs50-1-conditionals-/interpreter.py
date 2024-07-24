# The "interpreter" program allows the user to input a simple math expression (e.g 1 + 1) using + - * or / (simple calculator)
# The program outputs the answer as a float rounded to 1 decimal point

def main():

    # Gets user to input a simple math expression (e.g 1 + 1) using + - * or /
    expression = input("Expression: ").strip()

    # Splits the math expression into a list of 3 strings separated by the spaces in the original string
    value = expression.split()

    # Calculates the answer based on the operator used converted to a float rounded to 1 decimal point
    if value[1] == "+":
        z = float(value[0]) + float(value[2])
        print(f"{z:.1f}")
    elif value[1] == "-":
        z = float(value[0]) - float(value[2])
        print(f"{z:.1f}")
    elif value[1] == "*":
        z = float(value[0]) * float(value[2])
        print(f"{z:.1f}")
    elif value[1] == "/":
        z = float(value[0]) / float(value[2])
        print(f"{z:.1f}")
    else:
        print("Not valid math expression")

if __name__ == "__main__":
    main()
