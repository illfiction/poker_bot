# import numpy as np
# from deck import deck
# from hand_checker import flush_checker,straight_checker,is_two_pair,is_single_pair,is_full_house,is_four_of_a_kind,is_three_of_a_kind
#
# def opp_prob(card1,card2,opened_cards,remaining_cards,flop_cards,hands):
#     user_hand = opened_cards.union(set([card1, card2]))
#     print("NEW CASE with users cards:", opened_cards, card1, card2)
#     total_count += 1  # TOTAL COUNT HAS BEEN INCREMENTED.
#
#     is_flush = flush_checker(user_hand)
#     print("flush:", is_flush)
#     print(straight_checker(user_hand))
#     is_straight = (straight_checker(user_hand) != 0)
#     print("straight:", is_straight)
#     is_royal_straight = (straight_checker(user_hand) == 2)
#     '''
#         used this way just so it is more efficient as flush straight are checked multiple times as there are many sub cases
#         the following if elif ladder is implemented so that in a particular 7 card set only the highest hand win, more efficient
#     '''
#
#     if is_flush and is_royal_straight:
#         hands_tally_counter['Royal Flush'] += 1
#         print('Royal Flush')
#     elif is_straight and is_flush:
#         hands_tally_counter['Straight Flush'] += 1
#         print('Straight Flush')
#     elif is_four_of_a_kind(user_hand):
#         hands_tally_counter['Four of a Kind'] += 1
#         print('Four of a Kind')
#     elif is_full_house(user_hand):
#         hands_tally_counter['Full House'] += 1
#         print('Full House')
#     elif is_flush:
#         hands_tally_counter['Flush'] += 1
#         print('Flush')
#     elif is_straight:
#         hands_tally_counter['Straight'] += 1
#         print('Straight')
#     elif is_three_of_a_kind(user_hand):
#         hands_tally_counter['Three of a Kind'] += 1
#         print('Three of a Kind')
#     elif is_two_pair(user_hand):
#         hands_tally_counter['Two Pair'] += 1
#         print('Two Pair')
#     elif is_single_pair(user_hand):
#         hands_tally_counter['Single Pair'] += 1
#         print('Single Pair')
#     else:
#         hands_tally_counter['No Pair'] += 1
#         print('No Pair')
#     for opp_card1 in remaining_cards:
#         remaining_cards.remove(opp_card1)
#         for opp_card2 in remaining_cards:
#             remaining_cards.remove(opp_card2)
#             opponent_hand = flop_cards.union(set([opp_card1, opp_card2, card1, card2]))
#             print("Opponents Cards",flop_cards, opp_card1, opp_card2, card1, card2)
#
