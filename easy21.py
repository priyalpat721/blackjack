"""
   CS5001
   Fall 2020
   Priyal Patel
   Homework 4: easy21

   A program that implements a version of blackjack called easy21
"""
from cards import *
import random

NUMBER_OF_CARDS = 2
MAXIMUM = 21


def remaining_deck(shuffled_cards: list, hands: list) -> list:
    """
        Takes in shuffled deck of cards and cards dealt
        to determine how many cards are remaining in the deck
        Parameters:
            shuffled_cards (list)
            hands (list)
        Return:
            deal_card (list)
    """
    deal_card = []

    for item in shuffled_cards:
        deal_card.append(item)

    for hand in hands:
        for i, card in hand:
            if card in deal_card:
                # finds the index the card is stored and removes it
                deal_card.pop(i)

    for i in range(len(deal_card)):
        deal_card.append(deal_card[i])

    return deal_card


def draw_card(player_num: int, hands: list, deal_card: list):
    """
        Takes in input from user and cards dealt
        Parameters:
            player_num (int)
            hands (list)
            deal_card (list)
        Return:
            None
    """
    player_num -= 1
    cards_left = len(deal_card)

    # accounts for scenario where no cards are left in deck
    if cards_left == 0:
        card_values = remove_suits(hands)
        total_value = tally_cards(card_values)
        print_winner(total_value)
        exit(1)

    # card is an index for the list of remaining cards
    card = random.randint(0, cards_left - 1)
    hands[player_num].append(deal_card[card])
    print("You took a", deal_card[card], "from the deck")

    # removes element at the index(card)
    deal_card.pop(card)


def remove_suits(hands: list) -> list:
    """
        Takes cards dealt and removes the suit from the card
        Parameters:
            hands (list)
        Return:
            hand_number (list)
    """
    hand_number = []
    for i in range(len(hands)):
        hand_value = []
        string_card = "".join(hands[i])

        for j in range(0, len(string_card), 2):
            hand_value.append(string_card[j])
        hand_number.append(hand_value)

    return hand_number


def tally_cards(card_values: list) -> list:
    """
        Takes in shuffled deck of cards and cards dealt
        to determine how many cards are remaining in the deck
        Parameters:
            card_values (list)
        Return:
            total_value (list)
    """
    total_value = []
    for card in card_values:
        total = 0

        # determines point value depending on digit or letter
        for values in card:
            if values.isdigit():
                total += int(values)
            if values.isalpha():
                total += 10
        total_value.append(total)

    return total_value


def print_winner(total_value: list):
    """
        Determines the winner of the game
        Parameters:
            total_value (list)
        Return:
            None
    """
    highest_so_far = 0
    for i in range(len(total_value)):
        if total_value[i] > MAXIMUM:
            total_value[i] = None

        else:
            if total_value[i] > highest_so_far:
                highest_so_far = total_value[i]

    for j in range(len(total_value)):
        if total_value[j] == highest_so_far:
            print("Hand", j + 1, "won this round with",
                  highest_so_far, "points")


def main():
    cards = create_deck()
    shuffled_cards = shuffle(cards)

    number_of_hands = int(input("Welcome to Easy21! \n"
                                "How many hands to deal (1 - 4)? "))

    while number_of_hands < 1 or number_of_hands > 4:
        number_of_hands = int(input("How many hands to deal (1 - 4)? "))
    print("\nDealt", number_of_hands, "hand(s), 2 cards each")

    hands = deal(number_of_hands, NUMBER_OF_CARDS, shuffled_cards)
    for i in range(number_of_hands):
        print("Hand", i + 1, hands[i])
    deal_card = remaining_deck(shuffled_cards, hands)

    choice = input("\nSelect:\n"
                   "       D to draw\n"
                   "       S to stand\n"
                   "       W to shoW hands\n"
                   "       C to show remaining cards in deck\n"
                   "       Q to quit: ")

    while choice.lower != 'q' or choice.lower != 's':
        if choice.lower() == 'w':
            print("\nCurrent Hands:")
            for i in range(number_of_hands):
                print("Hand", i + 1, hands[i])

        elif choice.lower() == 'c':
            print("\n", deal_card)

        elif choice.lower() == 'd':
            player_num = int(input("\nDraw for which hand?"))
            while player_num < 1 or player_num > number_of_hands:
                player_num = int(input("Draw for which hand?"))
                print(deal_card)
            draw_card(player_num, hands, deal_card)

        else:
            card_values = remove_suits(hands)
            total_value = tally_cards(card_values)
            print_winner(total_value)
            break

        choice = input("\nSelect:\n"
                       "       D to draw\n"
                       "       S to stand\n"
                       "       W to shoW hands\n"
                       "       C to show remaining cards in deck\n"
                       "       Q to quit: ")


if __name__ == "__main__":
    main()
