class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        rank_str = {11: 'J', 12: 'Q', 13: 'K', 14: 'A',10: 'T'}.get(self.rank, str(self.rank))
        return f"{rank_str}{self.suit}"

    def __eq__(self, other):
        return isinstance(other, Card) and self.rank == other.rank and self.suit == other.suit

    def __hash__(self):
        return hash((self.rank, self.suit))
    def treys_format(self):
        rank_str = {11: 'J',12: 'Q',13: 'K',14: 'A'}.get(self.rank, str(self.rank))
        return f"{self.rank_str}{self.suit}"