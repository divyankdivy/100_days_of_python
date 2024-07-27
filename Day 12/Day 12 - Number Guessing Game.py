import random
from art import number_game_logo
answer = random.randint(1,100)

EASY_LEVEL_TURNS = 10
MEDIUM_LEVEL_TURNS = 5
HARD_LEVEL_TURNS = 3

def difficulty_level():
    level = input("Which level would you like to guess the number?'easy', 'medium' or 'hard'\n")
    if level == 'easy':
        turns_left = EASY_LEVEL_TURNS
        return turns_left
    elif level == 'medium':
        turns_left = MEDIUM_LEVEL_TURNS
        return turns_left
    elif level == 'hard':
        turns_left = HARD_LEVEL_TURNS
        return turns_left

def check_guess(guess, actual_number, turns_left):
    if guess == actual_number:
        print("Congratulations! You guessed the number!")
    elif guess > actual_number + 10:
        print("Your guess is too high!")
        return turns_left - 1
    elif guess < actual_number - 10:
        print("Your guess is too low!")
        return turns_left - 1
    elif guess > actual_number:
        print("Your guess is high")
        return turns_left - 1
    elif guess < actual_number:
        print("Your guess is low")
        return turns_left - 1

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    turns = difficulty_level()

    guess_number = 0
    while guess_number != answer:
        print(f"You have {turns} attempts to guess the number.")
        guess_number = int(input("Guess a number between 1 and 100!\n"))
        turns = check_guess(guess_number, answer, turns)
        if turns == 0:
            print("You are out of guesses!\nYou Loose")
            return

number_guessing_game()

