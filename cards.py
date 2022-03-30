"""
   CS5001
   Fall 2020
   Priyal Patel
   Homework 4: cards

   A program that creates, shuffles and deals cards
"""

import random
from cards import *

SUITS = ['s', 'h', 'd', 'c']
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


def create_deck() -> list:
    """
    Creates a deck of 52 cards
    Parameters:
        Takes in constants VALUES and SUITS
    Return value:
        A list of cards, not shuffled.
    """
    new_deck = []
    for i in range(len(SUITS)):
        for j in range(len(VALUES)):
            string_of_values = VALUES[j] + SUITS[i]
            new_deck.append(string_of_values)

    return new_deck


def shuffle(cards: list) -> list:
    """
    Takes in a deck of cards and creates a new list of a
    randomly shuffled deck of cards
    Parameters:
        cards (list) - not shuffled cards
    Return:
        shuffled_cards (list) - randomly shuffled deck
    """
    shuffled_cards = []

    for item in cards:
        shuffled_cards.append(item)
    random.shuffle(shuffled_cards)

    # print("Shuffled deck of cards \n", shuffled_cards)
    return shuffled_cards


def deal(number_of_hands: int, number_of_cards: int, shuffled_cards: list) -> list:
    """
    Takes in a deck of randomly card and creates a new nested list;
    the outer list represents the # of hands
    the inner list represents the # of cards
    Parameters:
        number_of_hands (int)
        number_of_cards (int)
        shuffled_cards (list) - shuffled cards
    Return:
        deal_hands (list) - hands with cards
    """
    total_cards = 51
    deal_to_player = []
    for item in shuffled_cards:
        deal_to_player.append(item)
    deal_hands = []
    counter = 0

    for i in range(number_of_hands):
        deal_cards = []
        for j in range(number_of_cards):

            # determines cards remaining in deck
            cards_left = total_cards - counter

            # card is a number to represent the index
            card = random.randint(0, cards_left)
            deal_cards.append(deal_to_player[card])
            deal_to_player.pop(card)
            counter += 1
        deal_hands.append(deal_cards)
    # print("Cards remaining in deck \n", deal_to_player)
    return deal_hands


def main():
    cards = create_deck()
    shuffled_cards = shuffle(cards)

    number_of_hands = int(input("How many hands to deal? "))
    while number_of_hands < 1 or number_of_hands > 4:
        number_of_hands = int(input("How many hands to deal? "))
    number_of_cards = int(input("How many cards to deal? "))
    while number_of_cards < 1 or number_of_cards > 13:
        number_of_cards = int(input("How many cards to deal? "))

    hands = deal(number_of_hands, number_of_cards, shuffled_cards)
    for i in range(number_of_hands):
        print("\nHand", i + 1, hands[i])


if __name__ == "__main__":
    main()
