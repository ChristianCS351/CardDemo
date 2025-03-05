import random

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        """Adds a card to the hand"""
        self.cards.append(card)

    def display_hand(self):
        """Displays the current hand of cards"""
        return ', '.join(self.cards)

    def num_cards(self):
        """Returns the number of cards in the hand"""
        return len(self.cards)
