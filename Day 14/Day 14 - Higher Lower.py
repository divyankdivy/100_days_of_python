print("Welcome to Higher Lower Game")
import random
from art import logo
from art import vs
from game_data import data
print(logo)

def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['Country']
    return f"{account_name}, {account_description}, {account_country}"

def check_answer(person1, person2, guess):
    if person1 > person2 and guess == 'a':
        return True
    elif person1 < person2 and guess == 'b':
        return True
    elif person1 > person2 and guess == 'b':
        return False
    elif person1 < person2 and guess == 'a':
        return False

score = 0

game_over = False
account_b = random.choice(data)

while not game_over:
    account_a = account_b
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    guess_followers = input("Who has more followers? 'A' or 'B': ").lower()

    a_followers = account_a['followers']
    b_followers = account_b['followers']
    is_checker = check_answer(a_followers, b_followers, guess_followers)

    if is_checker:
        score += 1
        print(f"You're right! Your score is {score}.")
    else:
        game_over = True
        print(f"Game Over! Your final score is {score}")