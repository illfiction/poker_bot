#this file is used to decide who wins if both have the same hand rank


from collections import Counter
from parse_cards import parse_cards

def find_better_name(set1, set2, count):

    list1 = [card.rank for card in set1]
    list2 = [card.rank for card in set2]

    for i in range(count):
        print("i:",i)
        print(max(list1),max(list2))
        if max(list1) > max(list2):
            return 1
        elif max(list1) < max(list2):
            return 0
        list1.remove(max(list1))
        list2.remove(max(list2))
    return 0.5


def high_card_tiebreaker(user_hand, opp_hand):
    count = 5
    return find_better_name(user_hand, opp_hand, count)


def one_pair_tiebreaker(user_hand, opp_hand):
    user_rank_counts = Counter(card.rank for card in user_hand)  # Extract ranks and count occurrences
    opp_rank_counts = Counter(card.rank for card in opp_hand)  # Extract ranks and count occurrences

    for user_rank in user_rank_counts:
        for opp_rank in opp_rank_counts:
            if user_rank == opp_rank:
                return high_card_tiebreaker(user_hand, opp_hand)
            else:
                count = 3
                return find_better_name(user_hand, opp_hand, count)


def two_pair_tiebreaker(user_hand, opp_hand):
    user_rank_counts = Counter(card.rank for card in user_hand)  # Extract ranks and count occurrences
    opp_rank_counts = Counter(card.rank for card in opp_hand)  # Extract ranks and count occurrences

    user_pairs_list = []
    opp_pairs_list = []

    for user_rank in user_rank_counts:
        if user_rank.value == 2:
            user_pairs_list.append(user_rank)
            user_hand.remove(user_rank)

    for opp_rank in opp_rank_counts:
        if opp_rank.value == 2:
            opp_pairs_list.append(opp_rank)
            opp_hand.remove(opp_rank)

    for i in range(max(len(user_pairs_list), len(opp_pairs_list))):
        if max(user_pairs_list[i]) > max(opp_pairs_list[i]):
            return 1
        elif max(user_pairs_list[i]) < max(opp_pairs_list[i]):
            return 0
        else:
            count = 1
            return find_better_name(user_hand, opp_hand, count)


def three_of_a_kind_tiebreaker(user_hand, opp_hand):
    user_rank_counts = Counter(card.rank for card in user_hand)  # Extract ranks and count occurrences

    opp_rank_counts = Counter(card.rank for card in opp_hand)  # Extract ranks and count occurrences

    user_triples_list = []
    opp_triples_list = []

    for user_rank in user_rank_counts:
        if user_rank.value == 3:
            user_triples_list.append(user_rank)
            user_hand.remove(user_rank)

    for opp_rank in opp_rank_counts:
        if opp_rank.value == 3:
            opp_triples_list.append(opp_rank)
            opp_hand.remove(opp_rank)

    for i in range(max(len(user_triples_list), len(opp_triples_list))):
        if max(user_triples_list[i]) > max(opp_triples_list[i]):
            return 1
        elif max(user_triples_list[i]) < max(opp_triples_list[i]):
            return 0
        else:
            count = 2
            return find_better_name(user_hand, opp_hand, count)


def four_of_a_kind_tiebreaker(user_hand, opp_hand):
    user_rank_counts = Counter(card.rank for card in user_hand)  # Extract ranks and count occurrences

    opp_rank_counts = Counter(card.rank for card in opp_hand)  # Extract ranks and count occurrences

    user_quadruples_list = []
    opp_triples_list = []

    for user_rank in user_rank_counts:
        if user_rank.value == 4:
            user_quadruples_list.append(user_rank)
            user_hand.remove(user_rank)

    for opp_rank in opp_rank_counts:
        if opp_rank.value == 4:
            opp_triples_list.append(opp_rank)
            opp_hand.remove(opp_rank)

    for i in range(max(len(user_quadruples_list), len(opp_triples_list))):
        if max(user_quadruples_list[i]) > max(opp_triples_list[i]):
            return 1
        elif max(user_quadruples_list[i]) < max(opp_triples_list[i]):
            return 0
        else:
            count = 1
            return find_better_name(user_hand, opp_hand, count)


def full_house_tiebreaker(user_hand, opp_hand):
    user_rank_counts = Counter(card.rank for card in user_hand)  # Extract ranks and count occurrences

    opp_rank_counts = Counter(card.rank for card in opp_hand)  # Extract ranks and count occurrences

    user_triples_list = []
    opp_triples_list = []

    for user_rank in user_rank_counts:
        if user_rank.value == 3:
            user_triples_list.append(user_rank)
            user_hand.remove(user_rank)

    for opp_rank in opp_rank_counts:
        if opp_rank.value == 3:
            opp_triples_list.append(opp_rank)
            opp_hand.remove(opp_rank)

    for i in range(max(len(user_triples_list), len(opp_triples_list))):
        if max(user_triples_list[i]) > max(opp_triples_list[i]):
            return 1
        elif max(user_triples_list[i]) < max(opp_triples_list[i]):
            return 0
        else:
            count = 2
            return find_better_name(user_hand, opp_hand, count)


def straight_tiebreaker(user_hand, opp_hand):

    user_ranks = sorted(set(card.rank for card in user_hand))
    opp_ranks = sorted(set(card.rank for card in opp_hand))

    for i in range(len(user_ranks)):
        if user_ranks[i] - user_ranks[i-4] == 4:
            user_straight_high_card = user_ranks[i]
        if opp_ranks[i] - opp_ranks[i-4] == 4:
            opp_straight_high_card = opp_ranks[i]

    if user_straight_high_card == opp_straight_high_card:
        return 0.5
    elif user_straight_high_card >= opp_straight_high_card:
        return 1
    else:
        return 0


def flush_tiebreaker(user_hand, opp_hand):
    user_suit_counts = {suit: 0 for suit in "shdc"}  # Initialize suit count dictionary
    #We only need to for user because if there is a flush its suit will be same for both user and opp
    # 5 cards common and only 2 cards in hand no possible case where there is different suit flushes

    for card in user_hand:
        user_suit_counts[card.suit] += 1  # Increment suit count
    print(user_suit_counts)

    flush_suit = max(user_suit_counts, key=user_suit_counts.get)

    user_flush_cards = {card for card in user_hand if card.suit == flush_suit}
    opp_flush_cards = {card for card in opp_hand if card.suit == flush_suit}

    return high_card_tiebreaker(user_flush_cards, opp_flush_cards)


def tiebreaker(user_hand,opp_hand,hand_rank): #returns 1 is user wins and 0 if user looses

    if hand_rank == 10:     #Royal Flush
        return 0.5 #always tie in royal flush
    elif hand_rank == 9:    #Straight Flush
        return straight_tiebreaker(user_hand, opp_hand)
    elif hand_rank == 8:    #Four of a kind
        return four_of_a_kind_tiebreaker(user_hand, opp_hand)
    elif hand_rank == 7:    #Full House
        ...
    elif hand_rank == 6:    #Flush
        return flush_tiebreaker(user_hand, opp_hand)
    elif hand_rank == 5:    #Straight
        return straight_tiebreaker(user_hand, opp_hand)
    elif hand_rank == 4:    #Three of a kind
        return three_of_a_kind_tiebreaker(user_hand, opp_hand)
    elif hand_rank == 3:    #Two pair
        return two_pair_tiebreaker(user_hand, opp_hand)
    elif hand_rank == 2:    #One Pair
        return one_pair_tiebreaker(user_hand, opp_hand)
    elif hand_rank == 1:    #High Card
        return high_card_tiebreaker(user_hand, opp_hand)

if __name__ == '__main__':
    input_str = "9h 8h 7h 6h 2h"
    user_hand = parse_cards(input_str)

    input_str = "10h 9h 8h 7h 4h"
    opp_hand = parse_cards(input_str)

    print(flush_tiebreaker(user_hand, opp_hand))