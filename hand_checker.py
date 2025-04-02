from collections import Counter


def flush_checker(card_set):
    suit_counts = {suit: 0 for suit in "shdc"}  # Initialize suit count dictionary

    for card in card_set:
        suit_counts[card.suit] += 1  # Increment suit count

    max_suit_count = max(suit_counts.values())  # Find the highest suit count

    return max_suit_count >= 5


def straight_checker(card_set):
    rank_values = {'1':1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                   'j': 11, 'q': 12, 'k': 13}  # Ace can also be 1 for A-2-3-4-5 straight

    ranks = sorted(set(rank_values[card.rank] for card in card_set))  # Get unique sorted ranks

    # Check for any 5-card consecutive sequence
    for i in range(len(ranks) - 4):
        if ranks[i + 4] - ranks[i] == 4:
            return 1

    # Special case: A-2-3-4-5 straight
    if {1, 10, 11, 12, 13,}.issubset(ranks):
        return 2

    return 0


def is_single_pair(card_set):
    rank_counts = Counter(card.rank for card in card_set)  # Extract ranks and count occurrences
    counts = list(rank_counts.values())  # Get list of rank frequencies

    return counts.count(2) == 1 and counts.count(1) == 5


def is_two_pair(card_set):
    rank_counts = Counter(card.rank for card in card_set)  # Extract ranks and count occurrences
    counts = list(rank_counts.values())  # Get list of rank frequencies

    return counts.count(2) == 2 and counts.count(1) == 3


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

