print("Welcome to BlackJack Game!")
print("Do you want to start BlackJack? Type y to start BlackJack, or q to quit")
import random
deck_of_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
for i in range(2):
    user_cards.append(random.choice(deck_of_cards))
    computer_cards.append(random.choice(deck_of_cards))

user_score = 0
computer_score = 0
is_game_over = False

while not is_game_over:
    for card in user_cards:
        user_score += card

    if user_score > 21:
        user_cards.remove(11)
        user_cards.append(1)
    elif user_score == 21:
    for card in computer_cards:
        computer_score += card

    print(f"Your cards: {user_cards}, user scores: {user_score}")
    print(f"Computer's first cards: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card or type 'n' to pass: ")
        if user_should_deal == 'y':
            user_cards.append(random.choice(deck_of_cards))
            user_score += user_cards[-1]
            if user_score == 21:
                is_game_over = True
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(random.choice(deck_of_cards))
    computer_score += computer_cards[-1]

print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer final hand: {computer_cards}, final score: {computer_score}")

def compare_cards(card1, card2):
    if card1 == card2:
        return "Draw"
    elif card2 == 0:
        return "Lose, Opponent has BlackJack"
    elif card1 == 0:
        return "Win with a BlackJack"
    elif card1 > 21:
        return "You Went Over, You Loose"
    elif card2 > 21:
        return "Opponent Went Over, You Win"
    elif card1 > card2:
        return "You Win"
    elif card2 > card1:
        return "You Loose"
