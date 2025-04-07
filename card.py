class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        rank_str = {11: 'j', 12: 'q', 13: 'k', 14: 'a'}.get(self.rank, str(self.rank))
        return f"{rank_str}{self.suit}"

    def __eq__(self, other):
        return isinstance(other, Card) and self.rank == other.rank and self.suit == other.suit

    def __hash__(self):
        return hash((self.rank, self.suit))
