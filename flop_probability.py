import sys
import os
from deck import deck
from hand_checker import *
from tiebreaker import tiebreaker
import numpy as np

def get_hand_score(hand):
    if is_royal_flush(hand):
        return 10, 'Royal Flush'
    elif is_straight_flush(hand):
        return 9, 'Straight Flush'
    elif is_four_of_a_kind(hand):
        return 8, 'Four of a Kind'
    elif is_full_house(hand):
        return 7, 'Full House'
    elif is_flush(hand):
        return 6, 'Flush'
    elif is_straight(hand):
        return 5, 'Straight'
    elif is_three_of_a_kind(hand):
        return 4, 'Three of a Kind'
    elif is_two_pair(hand):
        return 3, 'Two Pair'
    elif is_single_pair(hand):
        return 2, 'Single Pair'
    else:
        return 1, 'No Pair'

def flop_probability(pocket_cards,flop_cards,pocket_cards_str,flop_cards_str):


    opened_cards = set(pocket_cards + flop_cards) #all cards that are visible to user
    '''    
    changing list to set so they can be easily checked
    Used set because it removes duplicate elements
    faster look up times due to not needing to loop 
    sets are also unordered
    '''

    if len(opened_cards) != 5:
        raise ValueError("Error: Invalid input detected!")
    #checking if total no. of cards given is proper

    remaining_cards = np.array([card for card in deck if card not in opened_cards])

    hands_tally_counter = {
        'Royal Flush': 0,
        'Straight Flush': 0,
        'Four of a Kind': 0,
        'Full House': 0,
        'Flush': 0,
        'Straight': 0,
        'Three of a Kind': 0,
        'Two Pair': 0,
        'Single Pair': 0,
        'No Pair': 0
    }

    total_count = 0
    total_total_count = 0
    win_tally_counter = 0

    for user_index,card1 in enumerate(remaining_cards):
        for card2 in remaining_cards[user_index+1:]:
            total_count += 1  # TOTAL COUNT HAS BEEN INCREMENTED.

            user_hand = opened_cards.union({card1, card2})
            # set that contains one possible cases with 2 random cards to fulfill 7 cards that are visible to player
            # use that set to check if 5 best cards for a hand or not in order of hands
            # 2 diff cards from remaining cards to find probability
            user_score, hand_name = get_hand_score(user_hand)
            hands_tally_counter[hand_name] += 1

            for opp_index,opp_card1 in enumerate(remaining_cards):
                if len({opp_card1, card1, card2}) != 3:
                    continue
                for opp_card2 in remaining_cards[opp_index+1:]:
                    if len({opp_card1, opp_card2, card1, card2}) != 4:
                        continue

                    total_total_count += 1
                    opp_hand = set(flop_cards).union({opp_card1, opp_card2, card1, card2})
                    opp_score, _ = get_hand_score(opp_hand)

                    if user_score > opp_score:
                        win_tally_counter += 1
                    elif user_score == opp_score:
                        win_tally_counter += tiebreaker(user_hand, opp_hand, user_score) or 0.0

    #end of for loops

    print("Hand tallies:", hands_tally_counter)
    print("Total Count:",total_count)

    final_probability = {key:value * 100 / total_count for key, value in hands_tally_counter.items()}
    print("Hand probabilities (%):", final_probability)


    print("Total Simulations:",total_total_count)

    print("Win tally:",win_tally_counter)
    print("Prob of win:",win_tally_counter * 100/total_total_count)


