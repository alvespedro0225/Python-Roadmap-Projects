from random import randint

if __name__ == "__main__":
    correctNumber: int = randint(1, 100)
    tries: int = 0
    maxTries: int = 0
    win: bool = False
    print(
        """
Choose a difficulty:
Easy (10 tries)
Medium (5 tries)
Hard (3 tries)
"""
    )
    while not maxTries:
        difficulty: str = input()

        match difficulty.lower():

            case "easy":
                maxTries = 10

            case "medium":
                maxTries = 5

            case "hard":
                maxTries = 3

            case _:
                print("\nChoose a valid difficulty:")

    print()
    while tries < maxTries and not win:
        guess: str = input("Choose a number: ")
        try:
            numberGuess = int(guess)
        except ValueError:
            print(f'"{guess}" is not a valid number.\n')
            continue
        match (correctNumber > numberGuess, correctNumber < numberGuess):
            case (True, False):
                print(f"{numberGuess} is  too small.\n")
                tries += 1

            case (False, True):
                print(f"{numberGuess} is too big.\n")
                tries += 1

            case (False, False):
                print("You guessed the correct number!")
                win = True
                break
    if not win:
        print(f"You are out of tries. The number was {correctNumber}.")
