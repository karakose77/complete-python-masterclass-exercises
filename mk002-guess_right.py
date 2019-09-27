from random import randint


def guess_right():
    """
    The function lets the player guess a randomly selected number between 1 and highest variable.
    After the player guessed correctly the function returns the guess count.
    """
    highest = int(input("Enter the highest limit for the guessing game?: "))
    num = randint(1, highest + 1)
    guess = int(input(f"Please guess a number between 1 and {highest}: "))
    guess_count = 1

    while guess != num and guess != 0:
        if guess < num:
            guess = int(input("Guess higher: "))
            guess_count += 1
        elif guess > num:
            guess = int(input("Guess lower: "))
            guess_count += 1

    if guess == num:
        print(f"Well done! You guessed right in {guess_count} tries!")
    elif guess == 0:
        print("You quit!")


guess_right()
