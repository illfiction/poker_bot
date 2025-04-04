import numpy as np
from deck import deck
from hand_checker import flush_checker,straight_checker,is_two_pair,is_single_pair,is_full_house,is_four_of_a_kind,is_three_of_a_kind

def flop_probability(pocket_cards,flop_cards):

    opened_cards_list = pocket_cards + flop_cards #all cards that are visible to user

    # to check if cards are same
    # for card1 in opened_cards_list:
    #     opened_cards_list.remove(card1)
    #     for card2 in opened_cards_list:
    #         if card1 == card2:
    #             print("ERROR: 2 cards are equal")
    #             return -1
    #     opened_cards_list.append(card1)
    # TODO:make a better card checker to check if 2 cards are same


    opened_cards = set(opened_cards_list) #
    '''    
    changing list to set so they can be easily checked
    Used set because it removes duplicate elements
    faster look up times due to not needing to loop 
    sets are also unordered
    '''

    remaining_cards = [card for card in deck if card not in opened_cards]
    print(remaining_cards)

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
    win_tally_counter = 0

    for card1 in remaining_cards:
        for card2 in remaining_cards:

            total_count += 1 #TOTAL COUNT HAS BEEN INCREMENTED.

            if countOf({card1, card2}):
                print("Card1 is equal to card2")
                break

            user_hand = opened_cards.union(set([card1, card2]))
            print("NEW CASE with cards:",opened_cards,card1,card2)
            # set that contains one possible cases with 2 random cards to fulfill 7 cards that are visible to player
            # use that set to check if 5 best cards for a hand or not in order of hands
            # 2 diff cards from remaining cards to find probability


            is_flush = flush_checker(user_hand)
            is_straight = (straight_checker(user_hand) != 0)
            is_royal_straight = (straight_checker(user_hand) == 2)
            '''
                used this way just so it is more efficient as flush straight are checked multiple times as there are many sub cases
                the following if elif ladder is implemented so that in a particular 7 card set only the highest hand win, more efficient
            '''

            if is_flush and is_royal_straight:
                hands_tally_counter['Royal Flush'] += 1
                user_hand_rank = 10
                print('Royal Flush')
            elif is_straight and is_flush:
                hands_tally_counter['Straight Flush'] += 1
                print('Straight Flush')
                user_hand_rank = 9
            elif is_four_of_a_kind(user_hand):
                hands_tally_counter['Four of a Kind'] += 1
                print('Four of a Kind')
                user_hand_rank = 8
            elif is_full_house(user_hand):
                hands_tally_counter['Full House'] += 1
                print('Full House')
                user_hand_rank = 7
            elif is_flush:
                hands_tally_counter['Flush'] += 1
                print('Flush')
                user_hand_rank = 6
            elif is_straight:
                hands_tally_counter['Straight'] += 1
                print('Straight')
                user_hand_rank = 5
            elif is_three_of_a_kind(user_hand):
                hands_tally_counter['Three of a Kind'] += 1
                print('Three of a Kind')
                user_hand_rank = 4
            elif is_two_pair(user_hand):
                hands_tally_counter['Two Pair'] += 1
                print('Two Pair')
                user_hand_rank = 3
            elif is_single_pair(user_hand):
                hands_tally_counter['Single Pair'] += 1
                print('Single Pair')
                user_hand_rank = 2
            else:
                hands_tally_counter['No Pair'] += 1
                print('No Pair')
                user_hand_rank = 1


            print("Remaining cards:",remaining_cards)


            # for opp_card1 in remaining_cards:
            #
            #     if opp_card1 == card2 and opp_card1 == card1:
            #         break
            #
            #     remaining_cards.remove(opp_card1)
            #     for opp_card2 in remaining_cards:
            #
            #         if opp_card2 == card1 and opp_card2 == card2 and opp_card2 == opp_card1:
            #             break
            #
            #         print(card1,opp_card1,card2,opp_card2)
            #
            #         print("Reaming cards:",remaining_cards)
            #         flop_cards_set = set(flop_cards)
            #
            #         opp_hand = flop_cards_set.union(set([opp_card1, opp_card2, card1, card2]))
            #         print("Opp hand:",opp_hand)
            #         print("Opp cards:",flop_cards,opp_card1,opp_card2,card1,card2)
            #
            #         is_flush = flush_checker(opp_hand)
            #         # print("flush:", is_flush)
            #         # print(straight_checker(opp_hand))
            #         is_straight = (straight_checker(opp_hand) != 0)
            #         # print("straight:", is_straight)
            #         is_royal_straight = (straight_checker(opp_hand) == 2)
            #
            #         opp_hand_rank = 0
            #         print('Opp got')
            #         if is_flush and is_royal_straight:
            #             print('Royal Flush')
            #             opp_hand_rank = 10
            #         elif is_straight and is_flush:
            #             print('Straight Flush')
            #             opp_hand_rank = 9
            #         elif is_four_of_a_kind(opp_hand):
            #             print('Four of a Kind')
            #             opp_hand_rank = 8
            #         elif is_full_house(opp_hand):
            #             print('Full House')
            #             opp_hand_rank = 7
            #         elif is_flush:
            #             print('Flush')
            #             opp_hand_rank = 6
            #         elif is_straight:
            #             print('Straight')
            #             opp_hand_rank = 5
            #         elif is_three_of_a_kind(opp_hand):
            #             print('Three of a Kind')
            #             opp_hand_rank = 4
            #         elif is_two_pair(opp_hand):
            #             print('Two Pair')
            #             opp_hand_rank = 3
            #         elif is_single_pair(opp_hand):
            #             print('Single Pair')
            #             opp_hand_rank = 2
            #         else:
            #             print('No Pair')
            #             opp_hand_rank = 1
            #
            #         if user_hand_rank > opp_hand_rank:
            #             print("User Won")
            #             win_tally_counter += 1
            #         elif user_hand_rank < opp_hand_rank:
            #             print("User Lost")
            #         else:
            #             print("sort of Tie")
            #             win_tally_counter += 0.5

    #end of for loops

    print(hands_tally_counter)
    print("Total Count:",total_count)


