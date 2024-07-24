# The "game" program allows the user to input a level (to guess numbers from 1 to that level)
# It then generates a random number (target) from 1 to the level inputed and prompts the user to input a guess
# The program tells the user if the guess is too big, too small, or just right

import random

def main():
    while True:
        try:
            # Gets user to input a level (positive number) to guess numbers from 1 to that level
            n = int(input("Level: ").strip())
            if n >= 1:
                break
        except ValueError:
            print("Level must be a positive integer")
            pass

    # Generates a random number (target) from 1 to the level inputed
    target = random.randint(1, n)

    while True:
        try:
            # Prompts the user to input a guess (positive number)
            guess = int(input("Guess: ").strip())
            if n >= 1:
                # Tells the user if the guess is too big, too small, or just right
                if guess < target:
                    print("Too small!")
                    pass
                elif guess > target:
                    print("Too large!")
                    pass
                else:
                    print("Just right!")
                    break
        except ValueError:
            print("Guess must be a positive integer")
            pass


if __name__ == "__main__":
    main()
