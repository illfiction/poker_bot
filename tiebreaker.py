#this file is used to decide who wins if both have the same hand rank


from collections import Counter
from parse_cards import parse_cards

def

def high_card_tiebreaker(user_hand, opp_hand):

    user_rank_list = [card.rank for card in user_hand]
    opp_rank_list = [card.rank for card in opp_hand]

    print(user_rank_list)
    print(opp_rank_list)
    count = 5

    return high_card_checker(user_rank_list, opp_rank_list, count)



def one_pair_tiebreaker(user_hand, opp_hand):
    user_rank_counts = Counter(card.rank for card in user_hand)  # Extract ranks and count occurrences

    opp_rank_counts = Counter(card.rank for card in opp_hand)  # Extract ranks and count occurrences

    for user_rank in user_rank_counts:
        for opp_rank in opp_rank_counts:
            if user_rank == opp_rank:
                return high_card_tiebreaker(user_hand, opp_hand)
            else:
                count = 1
                return high_card_checker(user_rank_counts, opp_rank_counts, count)


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
        elif min(user_pairs_list[i]) < min(opp_pairs_list[i]):
            return 0
        else:
            return high_card_tiebreaker(user_hand, opp_hand)


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
        elif min(user_triples_list[i]) < min(opp_triples_list[i]):
            return 0
        else:
            return high_card_tiebreaker(user_hand, opp_hand)


def straight_tiebreaker(user_hand, opp_hand):

    rank_values = {'1':1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                   'j': 11, 'q': 12, 'k': 13}

    user_ranks = sorted(set(rank_values[card.rank] for card in user_hand))
    opp_ranks = sorted(set(rank_values[card.rank] for card in opp_hand))


def tiebreaker(user_hand,opp_hand,hand_rank): #returns 1 is user wins and 0 if user looses

    if hand_rank == 10:     #Royal Flush
        ...
    elif hand_rank == 9:    #Straight Flush
        ...
    elif hand_rank == 8:    #Four of a kind
        ...
    elif hand_rank == 7:    #Full House
        ...
    elif hand_rank == 6:    #Flush
        ...
    elif hand_rank == 5:    #Straight
        ...
    elif hand_rank == 4:    #Three of a kind
        return three_of_a_kind_tiebreaker(user_hand, opp_hand)
    elif hand_rank == 3:    #Two pair
        return two_pair_tiebreaker(user_hand, opp_hand)
    elif hand_rank == 2:    #One Pair
        return one_pair_tiebreaker(user_hand, opp_hand)
    elif hand_rank == 1:    #High Card
        return high_card_tiebreaker(user_hand, opp_hand)

if __name__ == '__main__':
    input_str = "3h 5c 9s 10s 5s"
    user_hand = parse_cards(input_str)

    input_str = "8c 7s 9c 2s 7h"
    opp_hand = parse_cards(input_str)

    print(one_pair_tiebreaker(user_hand, opp_hand))


