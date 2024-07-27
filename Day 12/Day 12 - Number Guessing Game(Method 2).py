import random
from art import number_game_logo

print("Welcome to Number Guessing Game!")
difficulty = input("Choose your difficulty:'easy', 'medium' or 'hard': ")
if difficulty == 'easy':
    lives = 10
elif difficulty == 'medium':
    lives = 5
elif difficulty == 'hard':
    lives = 3

print("I am thinking of a number between 1 and 100")
answer = random.randint(1, 100)

print(f"You have {lives} attempts to guess the number.")

game_over = False
while not game_over:
    guess_number = int(input("Guess a number between 1 and 100: "))
    if guess_number == answer:
        game_over = True
        print("Congratulations! You guessed the correct number.")
    elif guess_number < answer-10:
        print("Your guess is too low.")
    elif guess_number > answer+10:
        print("Your guess is too high.")
    elif guess_number > answer:
        print("Your guess is high")
    elif guess_number < answer:
        print("Your guess is low")
    if guess_number != answer:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You are out of lives\nYou lost!")
    print(f"You have {lives} attempt left to find the answer.")