
# Online Python - IDE, Editor, Compiler, Interpreter

import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # Includes face cards and Ace
    return random.choice(cards)

def calculate_score(hand):
    """Calculates the score of a hand."""
    if sum(hand) == 21 and len(hand) == 2:
        return 0  # Blackjack
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def play_blackjack():
    user_hand = [deal_card(), deal_card()]
    computer_hand = [deal_card(), deal_card()]
    game_over = False

    while not game_over:
        user_score = calculate_score(user_hand)
        computer_score = calculate_score(computer_hand)
        print(f"Your cards: {user_hand}, current score: {user_score}")
        print(f"Computer's first card: {computer_hand[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, 'n' to pass: ")
            if should_continue == 'y':
                user_hand.append(deal_card())
            else:
                game_over = True

    while computer_score < 17 and computer_score != 0:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print(f"Your final hand: {user_hand}, final score: {user_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
    
    if user_score > 21:
        print("You went over. You lose!")
    elif computer_score > 21 or user_score > computer_score:
        print("You win!")
    elif user_score < computer_score:
        print("You lose!")
    else:
        print("It's a draw!")

play_blackjack()
