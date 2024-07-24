# The "professor" program allows the user to implement a toy that generates math problems to solve
# The user can input a level (1, 2, or 3) which determines the number of digits of the integers in the math problems
# The program will give ten x + y math problems based on the level specified, and the user has 3 tries to answer it correctly
# The program will display the score (out of 10) once all ten math problems are answered

import random
import sys


def main():
    # Get level from the user (1, 2, or 3)
    level = get_level()

    # Set inital score as 0
    score = 0

    # Generates 10 math problems
    for i in range(10):
        # Random integers with a corresponding number of digits to the level will be generated for x and y
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y

        # Prints out the math problem
        print(f"{x} + {y} = ", end="")

        # Gives the user 3 tries to guess the answer
        for i in range(3):
            try:
                # Gets guess from the user
                guess = int(input().strip())

                # If the guess is correct, add 1 to the score
                if guess == z:
                    score += 1
                    break
                # If the guess is incorrect, print "EEE" and reprompt the user or print the answer if 3 guesses are reached
                else:
                    print("EEE")
                    if i < 2:
                        print(f"{x} + {y} = ", end="")
                        pass
                    if i == 2:
                        print(f"{x} + {y} = {z}")
                        break
            # If the guess is not an integer, print "EEE" and reprompt the user or print the answer if 3 guesses are reached
            except ValueError:
                print("EEE")
                if i < 2:
                        print(f"{x} + {y} = ", end="")
                        pass
                if i == 2:
                    print(f"{x} + {y} = {z}")
                    break

    # Prints the score at the end of the 10 math question s
    print(f"Score: {score}")


# Get level from the user (1, 2, or 3)
def get_level():
    while True:
        try:
            n = int(input("Level: ").strip())
            if 1 <= n <= 3:
                return n
            print("Level must be 1, 2, or 3")
        except ValueError:
            print("Level must be 1, 2, or 3")
            pass


# Based on the level specified (1, 2, or 3), a random integer with a corresponding number of digits will be generated for the math problem
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
