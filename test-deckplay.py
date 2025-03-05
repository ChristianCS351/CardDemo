import unittest

from deck-play import Deck


class TestDeck(unittest.TestCase):
    
    def test_deck_generate_deck(self):
        """Test that the deck is correctly generated with 52 cards."""
        deck = Deck()
        self.assertEqual(len(deck.cards), 52, "Deck should have 52 cards")
        self.assertIn('2 of Hearts', deck.cards, "Deck should contain '2 of Hearts'")
        self.assertIn('A of Spades', deck.cards, "Deck should contain 'A of Spades'")

    def test_deck_shuffle(self):
        """Test that shuffling the deck changes the order of the cards."""
        deck = Deck()
        original_order = deck.cards[:]
        deck.shuffle()
        self.assertNotEqual(original_order, deck.cards, "Deck should be shuffled")

    def test_deck_draw_card(self):
        """Test drawing a card from the deck."""
        deck = Deck()
        card = deck.draw_card()
        self.assertIsNotNone(card, "Card should not be None when drawn")
        self.assertEqual(len(deck.cards), 51, "Deck should have one less card after drawing")
        # Draw all cards to check for the deck running out
        for _ in range(51):
            deck.draw_card()
        last_card = deck.draw_card()
        self.assertIsNone(last_card, "No card should be drawn when the deck is empty")
    

if __name__ == '__main__':
    unittest.main()
