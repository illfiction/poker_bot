import sys
import os
from deck import deck
from hand_checker import is_royal_flush,is_flush,is_straight,is_two_pair,is_single_pair,is_full_house,is_four_of_a_kind,is_three_of_a_kind
from tiebreaker import tiebreaker
# from verify_using_treys import treys_checker

def flop_probability(pocket_cards,flop_cards,pocket_cards_str,flop_cards_str):

    opened_cards_list = pocket_cards + flop_cards #all cards that are visible to user

    opened_cards = set(opened_cards_list) #
    '''    
    changing list to set so they can be easily checked
    Used set because it removes duplicate elements
    faster look up times due to not needing to loop 
    sets are also unordered
    '''

    if len(opened_cards) != 5:
        raise ValueError("Error: Invalid input detected!")
    #checking if total no of cards given is proper

    remaining_cards = [card for card in deck if card not in opened_cards]

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

    for card1 in remaining_cards:
        for card2 in remaining_cards:

            if len({card1, card2}) < 2:
                # print("##Card1 is equal to card2", card1, card2)
                ...

            else:
                total_count += 1  # TOTAL COUNT HAS BEEN INCREMENTED.

                user_hand = opened_cards.union(set([card1, card2]))
                # print("NEW CASE with cards:",opened_cards,card1,card2)
                # set that contains one possible cases with 2 random cards to fulfill 7 cards that are visible to player
                # use that set to check if 5 best cards for a hand or not in order of hands
                # 2 diff cards from remaining cards to find probability



                '''
                    the following if elif ladder is implemented so that in a particular 7 card set only the highest hand win, more efficient
                '''

                if is_royal_flush(user_hand):
                    hands_tally_counter['Royal Flush'] += 1
                    user_hand_score = 10
                    # print('Royal Flush')
                elif is_straight(user_hand) and is_flush(user_hand):
                    hands_tally_counter['Straight Flush'] += 1
                    # print('Straight Flush')
                    user_hand_score = 9
                elif is_four_of_a_kind(user_hand):
                    hands_tally_counter['Four of a Kind'] += 1
                    # print('Four of a Kind')
                    user_hand_score = 8
                elif is_full_house(user_hand):
                    hands_tally_counter['Full House'] += 1
                    # print('Full House')
                    user_hand_score = 7
                elif is_flush(user_hand):
                    hands_tally_counter['Flush'] += 1
                    # print('Flush')
                    user_hand_score = 6
                elif is_straight(user_hand):
                    hands_tally_counter['Straight'] += 1
                    # print('Straight')
                    user_hand_score = 5
                elif is_three_of_a_kind(user_hand):
                    hands_tally_counter['Three of a Kind'] += 1
                    # print('Three of a Kind')
                    user_hand_score = 4
                elif is_two_pair(user_hand):
                    hands_tally_counter['Two Pair'] += 1
                    # print('Two Pair')
                    user_hand_score = 3
                elif is_single_pair(user_hand):
                    hands_tally_counter['Single Pair'] += 1
                    # print('Single Pair')
                    user_hand_score = 2
                else:
                    hands_tally_counter['No Pair'] += 1
                    # print('No Pair')
                    user_hand_score = 1


            # print("Remaining cards:",remaining_cards)


            for opp_card1 in remaining_cards:
                if len({opp_card1,card2,card1}) < 3:
                    # print("duplicate",card1,card2,opp_card1)
                    ...

                else:
                    for opp_card2 in remaining_cards:

                        if len({opp_card1, opp_card2,card1 ,card2}) < 4:
                            # print("There are duplicate cards:",opp_card1,opp_card2,card1,card2)
                            ...

                        else:

                            total_total_count += 1
                            # print("Percentage done",total_total_count/42807.60)

                            # print("Remaining cards:",remaining_cards)
                            flop_cards_set = set(flop_cards)

                            opp_hand = flop_cards_set.union(set([opp_card1, opp_card2, card1, card2]))
                            # print("Opp hand:",opp_hand)
                            # print("Opp cards:",flop_cards,opp_card1,opp_card2,card1,card2)


                            if is_royal_flush(opp_hand):
                                # print('Opp got Royal Flush')
                                opp_hand_score = 10
                            elif is_straight(opp_hand) and is_flush(opp_hand):
                                # print('Opp got Straight Flush')
                                opp_hand_score = 9
                            elif is_four_of_a_kind(opp_hand):
                                # print('Opp got Four of a Kind')
                                opp_hand_score = 8
                            elif is_full_house(opp_hand):
                                # print('Opp got Full House')
                                opp_hand_score = 7
                            elif is_flush(opp_hand):
                                # print('Opp got Flush')
                                opp_hand_score = 6
                            elif is_straight(opp_hand):
                                # print('Opp got Straight')
                                opp_hand_score = 5
                            elif is_three_of_a_kind(opp_hand):
                                # print('Opp got Three of a Kind')
                                opp_hand_score = 4
                            elif is_two_pair(opp_hand):
                                # print('Opp got Two Pair')
                                opp_hand_score = 3
                            elif is_single_pair(opp_hand):
                                # print('Opp got Single Pair')
                                opp_hand_score = 2
                            else:
                                # print('Opp got No Pair')
                                opp_hand_score = 1

                            if user_hand_score > opp_hand_score:
                                # print("User Won")
                                win_tally_counter += 1
                                # if treys_checker(pocket_cards,flop_cards,card1,card2,opp_card1,opp_card2) == 1:
                                #     # print("matches with treys")
                                #     ...
                                # else:
                                #     print("me:user won")
                                #     print("treys:",treys_checker(pocket_cards,flop_cards,card1,card2,opp_card1,opp_card2))
                                #     print("does not matches with treys")
                                #     print(pocket_cards,flop_cards,card1,card2,opp_card1,opp_card2)
                                #     print(user_hand_score,opp_hand_score)
                                #     os.system("say beep")
                                #     sys.exit(1)
                            elif user_hand_score < opp_hand_score:
                                ...
                                # print("User Lost")
                                # if treys_checker(pocket_cards,flop_cards,card1,card2,opp_card1,opp_card2) == 0:
                                #     # print("matches with treys")
                                #     ...
                                # else:
                                #     print("me:user lost")
                                #     print("treys:",treys_checker(pocket_cards,flop_cards,card1,card2,opp_card1,opp_card2))
                                #     print("does not matches with treys")
                                #     print(pocket_cards,flop_cards,card1,card2,opp_card1,opp_card2)
                                #     print(user_hand_score,opp_hand_score)
                                #     os.system("say beep")
                                #     sys.exit(1)
                            else:
                                # print("sort of Tie")
                                tiebreaker_score = tiebreaker(user_hand, opp_hand, user_hand_score)
                                # treys_score = treys_checker(pocket_cards,flop_cards,card1,card2,opp_card1,opp_card2)
                                win_tally_counter += tiebreaker_score or 0.0
                                # if tiebreaker_score == treys_score:
                                #     # print("matches with treys")
                                #     ...
                                # else:
                                #     print("me:",tiebreaker_score)
                                #     print("treys:",treys_score)
                                #     print("does not matches with treys")
                                #     print(pocket_cards,flop_cards,card1,card2,opp_card1,opp_card2)
                                #     print(user_hand_score,opp_hand_score)
                                #     os.system("say beep")
                                #     sys.exit(1)

    #end of for loops

    print(hands_tally_counter)
    print("Total Count:",total_count)

    final_probability = {key:value * 100 / total_count for key, value in hands_tally_counter.items()}
    print(final_probability)


    print("Total Total Count:",total_total_count)

    print("Win tally:",win_tally_counter)
    print("Prob of win:",win_tally_counter * 100/total_total_count)


