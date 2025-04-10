from collections import Counter



def is_royal_flush(card_set):
    suit_counts = {suit: 0 for suit in "shdc"}  # Initialize suit count dictionary

    for card in card_set:
        suit_counts[card.suit] += 1  # Increment suit count

    max_suit = max(suit_counts, key=suit_counts.get)

    flush_cards_ranks = set()
    for card in card_set:
        if card.suit == max_suit:
            flush_cards_ranks.add(card.rank)


    if {14, 13, 12, 11, 10}.issubset(flush_cards_ranks):
        return 1
    return 0



def is_flush(card_set):
    suit_counts = {suit: 0 for suit in "shdc"}  # Initialize suit count dictionary

    for card in card_set:
        suit_counts[card.suit] += 1  # Increment suit count

    max_suit_count = max(suit_counts.values())  # Find the highest suit count

    return max_suit_count >= 5


def is_straight(card_set):
 # Ace can also be 1 for A-2-3-4-5 straight

    ranks = sorted(set(card.rank for card in card_set))  # Get unique sorted ranks

    # Check for any 5-card consecutive sequence
    for i in range(len(ranks) - 5):
        if ranks[i + 4] - ranks[i] == 4:
            return 1

    # Special case: A-2-3-4-5 straight
    if {2,3,4,5,14}.issubset(ranks):
        return 1

    return 0


def is_single_pair(card_set):
    rank_counts = Counter(card.rank for card in card_set)  # Extract ranks and count occurrences
    counts = list(rank_counts.values())  # Get list of rank frequencies

    return counts.count(2) == 1 and counts.count(1) == 5


def is_two_pair(card_set):
    rank_counts = Counter(card.rank for card in card_set)  # Extract ranks and count occurrences
    counts = list(rank_counts.values())  # Get list of rank frequencies

    return counts.count(2) >= 2 and counts.count(3) == 0 and counts.count(4) == 0


def is_three_of_a_kind(card_set):
    rank_counts = Counter(card.rank for card in card_set)  # Extract ranks and count occurrences
    counts = list(rank_counts.values())  # Get list of rank frequencies

    return counts.count(3) == 1 and counts.count(1) == 4


def is_four_of_a_kind(card_set):
    rank_counts = Counter(card.rank for card in card_set)  # Extract ranks and count occurrences
    counts = list(rank_counts.values())  # Get list of rank frequencies

    return counts.count(4) == 1


def is_full_house(card_set):
    rank_counts = Counter(card.rank for card in card_set)  # Extract ranks and count occurrences
    counts = list(rank_counts.values())  # Get list of rank frequencies

    return counts.count(3) == 1 and counts.count(2) >= 1

