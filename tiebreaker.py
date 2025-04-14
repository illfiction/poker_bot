#this file is used to decide who wins if both have the same hand score Eg both user and opp have single pair,etc

from parse_cards import parse_cards
from collections import Counter


def find_better_name(set1, set2, count):

    list1 = [card.rank for card in set1]
    list2 = [card.rank for card in set2]

    for i in range(count):
        if max(list1) > max(list2):
            return 1
        elif max(list1) < max(list2):
            return 0
        list1.remove(max(list1))
        list2.remove(max(list2))
    # print("tie")
    return 0.5


def high_card_tiebreaker(user_hand, opp_hand):
    count = 5
    return find_better_name(user_hand, opp_hand, count)


def one_pair_tiebreaker(user_hand, opp_hand):
    user_rank_counts = Counter(card.rank for card in user_hand)  # Extract ranks and count occurrences
    opp_rank_counts = Counter(card.rank for card in opp_hand)  # Extract ranks and count occurrences

    user_pair_rank = 0
    opp_pair_rank = 0

    temp_user_hand = set()
    temp_opp_hand = set()

    for user_rank in user_rank_counts:
        if user_rank_counts[user_rank] == 2:
            if user_rank_counts[user_rank] > user_pair_rank:
                user_pair_rank = user_rank
        else:
            for card in user_hand:
                if card.rank == user_rank:
                    temp_user_hand.add(card)

    for opp_rank in opp_rank_counts:
        if opp_rank_counts[opp_rank] == 2:
            if opp_rank_counts[opp_rank] > opp_pair_rank:
                opp_pair_rank = opp_rank
        else:
            for card in opp_hand:
                if card.rank == opp_rank:
                    temp_opp_hand.add(card)


    if user_pair_rank == opp_pair_rank:
        return find_better_name(temp_user_hand, temp_opp_hand, count = 3)
    elif user_pair_rank > opp_pair_rank:
        return 1
    else:
        return 0


def two_pair_tiebreaker(user_hand, opp_hand):
    user_rank_counts = Counter(card.rank for card in user_hand)  # Extract ranks and count occurrences
    opp_rank_counts = Counter(card.rank for card in opp_hand)  # Extract ranks and count occurrences

    user_pair_ranks = [0,0]     #This arrays first element contains the max element of the pairs will use this to compare
    opp_pair_ranks = [0,0]

    temp_user_hand = set()
    temp_opp_hand = set()

    for user_rank in user_rank_counts:
        if user_rank_counts[user_rank] == 2:
            if user_rank > user_pair_ranks[0]:
                user_pair_ranks[1] = user_pair_ranks[0]
                user_pair_ranks[0] = user_rank
            elif user_rank > user_pair_ranks[1]:
                user_pair_ranks[1] = user_rank

    for card in user_hand:
        if card.rank != user_pair_ranks[0] and card.rank != user_pair_ranks[1]:
            temp_user_hand.add(card)

    for opp_rank in opp_rank_counts:
        if opp_rank_counts[opp_rank] == 2:
            if opp_rank >= opp_pair_ranks[0]:
                opp_pair_ranks[1] = opp_pair_ranks[0]
                opp_pair_ranks[0] = opp_rank
            elif opp_rank > opp_pair_ranks[1]:
                opp_pair_ranks[1] = opp_rank

    for card in opp_hand:
        if card.rank != user_pair_ranks[0] and card.rank != user_pair_ranks[1]:
            temp_opp_hand.add(card)

    if user_pair_ranks[0] > opp_pair_ranks[0]:
        return 1
    elif user_pair_ranks[0] < opp_pair_ranks[0]:
        return 0
    else:
        if user_pair_ranks[1] > opp_pair_ranks[1]:
            return 1
        elif user_pair_ranks[1] < opp_pair_ranks[1]:
            return 0
        else:
            return find_better_name(temp_user_hand, temp_opp_hand, count = 1)



def three_of_a_kind_tiebreaker(user_hand, opp_hand):
    user_rank_counts = Counter(card.rank for card in user_hand)  # Extract ranks and count occurrences
    opp_rank_counts = Counter(card.rank for card in opp_hand)  # Extract ranks and count occurrences

    user_triples_rank = 0
    opp_triples_rank = 0

    temp_user_hand = set()
    temp_opp_hand = set()

    for user_rank in user_rank_counts:
        if user_rank_counts[user_rank] == 3:
            if user_rank_counts[user_rank] > user_triples_rank:
                user_triples_rank = user_rank
        else:
            for card in user_hand:
                if card.rank == user_rank:
                    temp_user_hand.add(card)

    for opp_rank in opp_rank_counts:
        if opp_rank_counts[opp_rank] == 3:
            if opp_rank_counts[opp_rank] > opp_triples_rank:
                opp_triples_rank = opp_rank
        else:
            for card in opp_hand:
                if card.rank == opp_rank:
                    temp_opp_hand.add(card)

    if user_triples_rank == opp_triples_rank:
        return find_better_name(temp_user_hand, temp_opp_hand, count = 2)
    elif user_triples_rank > opp_triples_rank:
        return 1
    else:
        return 0



def four_of_a_kind_tiebreaker(user_hand, opp_hand):
    user_rank_counts = Counter(card.rank for card in user_hand)  # Extract ranks and count occurrences
    opp_rank_counts = Counter(card.rank for card in opp_hand)  # Extract ranks and count occurrences

    user_quadruples_rank = 0
    opp_quadruples_rank = 0

    temp_user_hand = set()
    temp_opp_hand = set()

    for user_rank in user_rank_counts:
        if user_rank_counts[user_rank] == 4:
            if user_rank_counts[user_rank] > user_quadruples_rank:
                user_quadruples_rank = user_rank
        else:
            for card in user_hand:
                if card.rank == user_rank:
                    temp_user_hand.add(card)

    for opp_rank in opp_rank_counts:
        if opp_rank_counts[opp_rank] == 4:
            if opp_rank_counts[opp_rank] > opp_quadruples_rank:
                opp_quadruples_rank = opp_rank
        else:
            for card in opp_hand:
                if card.rank == opp_rank:
                    temp_opp_hand.add(card)

    if user_quadruples_rank == opp_quadruples_rank:
        return find_better_name(temp_user_hand, temp_opp_hand, count = 1)
    elif user_quadruples_rank > opp_quadruples_rank:
        return 1
    else:
        return 0


def full_house_tiebreaker(user_hand, opp_hand):
    user_rank_counts = Counter(card.rank for card in user_hand)  # Extract ranks and count occurrences
    opp_rank_counts = Counter(card.rank for card in opp_hand)   # Extract ranks and count occurrences

    user_triples_rank = 0
    opp_triples_rank = 0

    user_doubles_rank = 0
    opp_doubles_rank = 0

    temp_user_hand = set()
    temp_opp_hand = set()

    for user_rank in user_rank_counts:
        if user_rank_counts[user_rank] == 3:
            if user_rank_counts[user_rank] > user_triples_rank:
                user_triples_rank = user_rank
            else:
                user_doubles_rank = user_rank
        elif user_rank_counts[user_rank] == 2:
            if user_rank_counts[user_rank] > user_doubles_rank:
                user_doubles_rank = user_rank
        else:
            for card in user_hand:
                if card.rank == user_rank:
                    temp_user_hand.add(card)

    for opp_rank in opp_rank_counts:
        if opp_rank_counts[opp_rank] == 3:
            if opp_rank_counts[opp_rank] > opp_triples_rank:
                opp_triples_rank = opp_rank
            else:
                opp_doubles_rank = opp_rank
        elif opp_rank_counts[opp_rank] == 2:
            if opp_rank_counts[opp_rank] > opp_triples_rank:
                opp_doubles_rank = opp_rank
        else:
            for card in opp_hand:
                if card.rank == opp_rank:
                    temp_opp_hand.add(card)

    if user_triples_rank == opp_triples_rank:
        if user_doubles_rank == opp_doubles_rank:
            return 0.5
        elif user_doubles_rank > opp_doubles_rank:
            return 1
        else:
            return 0
    elif user_triples_rank > opp_triples_rank:
        return 1
    else:
        return 0

def straight_tiebreaker(user_hand, opp_hand):

    user_ranks = sorted(set(card.rank for card in user_hand))
    opp_ranks = sorted(set(card.rank for card in opp_hand))


    for i in range(len(user_ranks)-4):
        if user_ranks[i+4] - user_ranks[i] == 4:
            user_straight_high_card = user_ranks[i]
    if max(user_ranks) == 14:
        user_straight_high_card = max(user_ranks)
    for i in range(len(opp_ranks)-4):
        if opp_ranks[i+4] - opp_ranks[i] == 4:
            opp_straight_high_card = opp_ranks[i]
    if max(opp_ranks) == 14:
        opp_straight_high_card = max(opp_ranks)
    if user_straight_high_card == opp_straight_high_card:
        # print("TIE")
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

    flush_suit = max(user_suit_counts, key=user_suit_counts.get)

    user_flush_cards = {card for card in user_hand if card.suit == flush_suit}
    opp_flush_cards = {card for card in opp_hand if card.suit == flush_suit}

    return high_card_tiebreaker(user_flush_cards, opp_flush_cards)


def tiebreaker(user_hand,opp_hand,hand_rank): #returns 1 is user wins and 0 if user looses
    if hand_rank == 10:     #Royal Flush
        # print("TIE")
        return 0.5 #always tie in royal flush
    elif hand_rank == 9:    #Straight Flush
        return straight_tiebreaker(user_hand, opp_hand)
    elif hand_rank == 8:    #Four of a kind
        return four_of_a_kind_tiebreaker(user_hand, opp_hand)
    elif hand_rank == 7:    #Full House
        return full_house_tiebreaker(user_hand, opp_hand)
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

    pocket_cards = parse_cards("6h kc")
    board_cards = parse_cards("8d 5s ac as ks")
    opp_cards = parse_cards("8s kd")
    print(pocket_cards,board_cards,opp_cards)
    user_hand = set(pocket_cards + board_cards)
    opp_hand = set(board_cards + opp_cards)

    print(user_hand,opp_hand)

    print(two_pair_tiebreaker(user_hand, opp_hand))

# Enter pocket cards: 1s 2s
# Enter flop cards: 5c 6h 7d 10d 5h
# Enter opp cards: ks qh