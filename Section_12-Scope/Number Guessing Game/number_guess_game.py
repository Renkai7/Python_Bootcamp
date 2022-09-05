# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

easy_mode = 10
hard_mode = 5


def set_difficulty():
    difficulty = input("Choose difficulty - Easy or Hard: ").lower()
    if difficulty == "easy":
        return easy_mode
    else:
        return hard_mode


def check_answer(guess, lives, answer):
    if guess > answer:
        print("Too high.")
        return lives - 1
    elif guess < answer:
        print("Too low.")
        return lives - 1
    else:
        print("Just right")
        return 0


def game():
    answer = random.randint(1, 100)
    print(answer)
    turns = set_difficulty()
    print(f"Number of guesses: {turns}")
    while turns != 0:
        user_guess = int(input("Guess a number: "))
        turns = check_answer(user_guess, turns, answer)
        if turns == 0 and user_guess != answer:
            print("Out of lives.")
            print(f"The number was: {answer}")
        elif user_guess != answer:
            print(f"Number of guesses: {turns}")


game()
