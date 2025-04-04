#this file is used to decide who wins if both have the same hand rank


from collections import Counter
from card import Card


def high_card_tiebreaker(user_hand, opp_hand):
    for i in range(5):
        if max(user_hand) > max(opp_hand):
            return 1
        elif min(user_hand) < min(opp_hand):
            return 0
    return 0.5


def one_pair_tiebreaker(user_hand, opp_hand):
    user_rank_counts = Counter(card.rank for card in user_hand)  # Extract ranks and count occurrences

    opp_rank_counts = Counter(card.rank for card in opp_hand)  # Extract ranks and count occurrences

    for user_rank in user_rank_counts:
        for opp_rank in opp_rank_counts:
            if user_rank == opp_rank:
                return 0.5
            elif user_rank > opp_rank:
                return 1
            elif user_rank < opp_rank:
                return 0

def two_pair_tiebreaker(user_hand, opp_hand):
    user_rank_counts = Counter(card.rank for card in user_hand)  # Extract ranks and count occurrences

    opp_rank_counts = Counter(card.rank for card in opp_hand)  # Extract ranks and count occurrences

    user_pairs_list = []
    opp_pairs_list = []

    for user_rank in user_rank_counts:
        if user_rank.value == 2:
            user_pairs_list.append(user_rank)

    for opp_rank in opp_rank_counts:
        if opp_rank.value == 2:
            opp_pairs_list.append(opp_rank)

    for i in range(max(len(user_pairs_list), len(opp_pairs_list))):
        if max(user_pairs_list[i]) > max(opp_pairs_list[i]):
            return 1
        elif min(user_pairs_list[i]) < min(opp_pairs_list[i]):
            return 0
        else:
            return 0.5




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
        ...
    elif hand_rank == 3:    #Two pair
        ...
    elif hand_rank == 2:    #One Pair
        ...
    elif hand_rank == 1:    #High Card
        return high_card_tiebreaker(user_hand, opp_hand)
