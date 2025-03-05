import.unittest

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
        
    def test_hand_add_card(self):
        """Test adding a card to the hand."""
        hand = Hand()
        hand.add_card('2 of Hearts')
        self.assertEqual(hand.num_cards(), 1, "Hand should have 1 card after adding a card")
        self.assertEqual(hand.display_hand(), "2 of Hearts", "Hand should contain '2 of Hearts'")

    def test_hand_display_hand(self):
        """Test displaying the hand."""
        hand = Hand()
        hand.add_card('2 of Hearts')
        hand.add_card('3 of Diamonds')
        self.assertEqual(hand.display_hand(), "2 of Hearts, 3 of Diamonds", "Hand should display all cards correctly")

    def test_hand_num_cards(self):
        """Test the number of cards in the hand."""
        hand = Hand()
        hand.add_card('2 of Hearts')
        hand.add_card('3 of Diamonds')
        self.assertEqual(hand.num_cards(), 2, "Hand should have 2 cards after adding two cards")
        hand.add_card('4 of Clubs')
        self.assertEqual(hand.num_cards(), 3, "Hand should have 3 cards after adding one more card")

if __name__ == '__main__':
    unittest.main()
