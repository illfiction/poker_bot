def fast_rank_count(hand):
    counts = {}
    for card in hand:
        counts[card.rank] = counts.get(card.rank, 0) + 1
    return counts
