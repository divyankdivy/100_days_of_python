print("Welcome to Blackjack")
import random
from art import blackjack_logo
deck_of_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    card = random.choice(deck_of_cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

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

def play_game():
    user_cards = []
    computer_cards = []

    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, user scores: {user_score}")
        print(f"Computer's first cards: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card or type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
                if user_score == 21:
                    is_game_over = True
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer final hand: {computer_cards}, final score: {computer_score}")

    print(compare_cards(user_score, computer_score))

while input("Do you want to play BlackJack Game? (y/n) ") == "y":
    play_game()