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

    for card1 in remaining_cards:
        remaining_cards.remove(card1)
        for card2 in remaining_cards:
            all_open_cards = opened_cards.union(set([card1, card2]))
            print("NEW CASE with cards:",all_open_cards)
            # set that contains one possible cases with 2 random cards to fulfill 7 cards that are visible to player
            # use that set to check if 5 best cards for a hand or not in order of hands
            # 2 diff cards from remaining cards to find probability

            total_count += 1 #TOTAL COUNT HAS BEEN INCREMENTED.

            is_flush = flush_checker(all_open_cards)
            print(is_flush)
            print(straight_checker(all_open_cards))
            is_straight = (straight_checker(all_open_cards) != 0)
            print(is_straight)
            is_royal_straight = (straight_checker(all_open_cards) == 2)
            '''
                used this way just so it is more efficient as flush straight are checked multiple times as there are many sub cases
                the following if elif ladder is implemented so that in a particular 7 card set only the highest hand win, more efficient
            '''

            if is_flush and is_royal_straight:
                hands_tally_counter['Royal Flush'] += 1
                print('Royal Flush')
            elif is_straight and is_flush:
                hands_tally_counter['Straight Flush'] += 1
                print('Straight Flush')
            elif is_four_of_a_kind(all_open_cards):
                hands_tally_counter['Four of a Kind'] += 1
                print('Four of a Kind')
            elif is_full_house(all_open_cards):
                hands_tally_counter['Full House'] += 1
                print('Full House')
            elif is_flush:
                hands_tally_counter['Flush'] += 1
                print('Flush')
            elif is_straight:
                hands_tally_counter['Straight'] += 1
                print('Straight')
            elif is_three_of_a_kind(all_open_cards):
                hands_tally_counter['Three of a Kind'] += 1
                print('Three of a Kind')
            elif is_two_pair(all_open_cards):
                hands_tally_counter['Two Pair'] += 1
                print('Two Pair')
            elif is_single_pair(all_open_cards):
                hands_tally_counter['Single Pair'] += 1
                print('Single Pair')
            else:
                hands_tally_counter['No Pair'] += 1
                print('No Pair')
    #end of for loops

    print(hands_tally_counter)
    print(total_count)
