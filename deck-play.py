import random

class Deck:
    def __init__(self):
        self.cards = []
        self.generate_deck()

    def generate_deck(self):
        """Generates a full deck of 52 cards"""
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [f'{value} of {suit}' for suit in suits for value in values]

    def shuffle(self):
        """Shuffles the deck of cards"""
        random.shuffle(self.cards)

    def draw_card(self):
        """Draws a card from the deck"""
        if self.cards:
            return self.cards.pop()
        else:
            return None  # No cards left
