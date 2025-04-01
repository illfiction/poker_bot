from card import Card

ranks = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k"]
suits = ["s", "d", "c", "h"]  # Spades, Hearts, Diamonds, Clubs

deck = [Card(rank, suit) for suit in suits for rank in ranks]
print(deck)