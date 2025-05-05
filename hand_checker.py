from collections import Counter
from parse_cards import parse_cards

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


def is_straight_flush(card_set):
    suit_counts = {suit: 0 for suit in "shdc"}  # Initialize suit count dictionary

    for card in card_set:
        suit_counts[card.suit] += 1  # Increment suit count

    if max(suit_counts) < 5:
        return 0
    max_suit = max(suit_counts, key=suit_counts.get)

    flush_cards = set()
    for card in card_set:
        if card.suit == max_suit:
            flush_cards.add(card)

    return is_straight(flush_cards)


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
    for i in range(len(ranks)-4):
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

    return counts.count(3) + counts.count(2) >= 2 and counts.count(3) >= 1

def hand_checker(card_set):
    if is_royal_flush(card_set):
        user_hand_score = 10
        # print('Royal Flush')
    elif is_straight(card_set) and is_flush(card_set):
        # print('Straight Flush')
        user_hand_score = 9
    elif is_four_of_a_kind(card_set):
        # print('Four of a Kind')
        user_hand_score = 8
    elif is_full_house(card_set):
        # print('Full House')
        user_hand_score = 7
    elif is_flush(card_set):
        # print('Flush')
        user_hand_score = 6
    elif is_straight(card_set):
        # print('Straight')
        user_hand_score = 5
    elif is_three_of_a_kind(card_set):
        # print('Three of a Kind')
        user_hand_score = 4
    elif is_two_pair(card_set):
        # print('Two Pair')
        user_hand_score = 3
    elif is_single_pair(card_set):
        # print('Single Pair')
        user_hand_score = 2
    else:
        # print('No Pair')
        user_hand_score = 1
    return user_hand_score

if __name__ == '__main__':
    pocket_cards = parse_cards("2d qs")
    board_cards = parse_cards("9h 7c 10s 2s 3d")
    opp_cards = parse_cards("6s 8d")
    print(pocket_cards, board_cards, opp_cards)
    user_hand = set(pocket_cards + board_cards)
    opp_hand = set(board_cards + opp_cards)

    print(user_hand, opp_hand)
    #
    # print(hand_checker(user_hand))
    print(is_straight(user_hand))