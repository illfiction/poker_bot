import numpy as np
from deck import deck
from card import Card

def flop_probability(pocket_cards,flop_cards):\

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

    for card1 in remaining_cards:
        remaining_cards.remove(card1)
        for card2 in remaining_cards:
            all_open_cards = opened_cards.union(set([card1, card2]))
            # set that contains one possible cases with 2 random cards to fulfill 7 cards that are visible to player
            # use that set to check if 5 best cards for a hand or not in order of hands

            print("ABC",all_open_cards)
            #TODO:

            # 2 diff cards from remaining cards to find probabilty

