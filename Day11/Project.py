#Black Jack
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(your_score, computer_score):
    if your_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif your_score == 0:
        return "Win with a Blackjack"
    elif your_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif your_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_blackjack():

    your_cards = []
    computer_cards = []

    your_score = -1
    computer_score = -1

    play = True

    for i in range(2):
        your_cards.append(deal_card())
        computer_cards.append(deal_card())


    while play:
        your_score = calculate_score(your_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {your_cards})")
        print(f"Computer's first card: {computer_cards[0]}")
        if your_score == 0 or computer_score == 0 or your_score > 21:
            play = False
        else:
            get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if get_another_card == 'y':
                your_cards.append(deal_card())
                your_score = calculate_score(your_cards)
            else:
                play = False

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {your_cards}, final score: {your_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(your_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print("\n"*20)
    play_blackjack()