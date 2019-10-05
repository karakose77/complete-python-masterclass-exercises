from random import randint


def guess_right():
    """
    The function lets the player guess a randomly selected number between 1 and highest variable.
    After the player guessed correctly the function returns the guess count.
    """
    highest = int(input("Enter the highest limit for the guessing game?: "))
    target_number = randint(1, highest + 1)
    guessed_number = int(input(f"Please guess a number between 1 and {highest}: "))
    guess_count = 1

    while guessed_number != target_number and guessed_number != 0:
        if guessed_number < target_number:
            guessed_number = int(input("Guess higher: "))
            guess_count += 1
        elif guessed_number > target_number:
            guessed_number = int(input("Guess lower: "))
            guess_count += 1

    if guessed_number == target_number:
        print(f"Well done! You guessed right in {guess_count} tries!")
    elif guessed_number == 0:
        print("You quit!")


guess_right()
